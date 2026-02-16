"""MCP server that exposes a get_youtube_transcript tool."""

import re

from mcp.server.fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

mcp = FastMCP("youtube-transcript")


def extract_video_id(url: str) -> str | None:
    """Extract a YouTube video ID from various URL formats or a bare ID."""
    patterns = [
        r"(?:youtube\.com/watch\?.*v=|youtu\.be/|youtube\.com/embed/|youtube\.com/v/|youtube\.com/shorts/)([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    # Check if the input is already a bare video ID
    if re.fullmatch(r"[a-zA-Z0-9_-]{11}", url.strip()):
        return url.strip()
    return None


def format_timestamp(seconds: float) -> str:
    """Format seconds into MM:SS."""
    mins = int(seconds) // 60
    secs = int(seconds) % 60
    return f"{mins:02d}:{secs:02d}"


@mcp.tool()
def get_youtube_transcript(url: str, include_timestamps: bool = False) -> str:
    """Fetch the transcript of a YouTube video.

    Args:
        url: Any YouTube URL format (youtu.be, youtube.com/watch?v=, etc.) or a video ID.
        include_timestamps: If True, prefix each line with [MM:SS].

    Returns:
        The transcript as plain text.
    """
    video_id = extract_video_id(url)
    if not video_id:
        return f"Error: Could not extract a video ID from the provided URL: {url}"

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    except TranscriptsDisabled:
        return f"Error: Transcripts are disabled for video {video_id}."
    except NoTranscriptFound:
        return f"Error: No transcript found for video {video_id}."
    except VideoUnavailable:
        return f"Error: Video {video_id} is unavailable (private, deleted, or does not exist)."
    except Exception as e:
        return f"Error fetching transcript for video {video_id}: {e}"

    lines = []
    for entry in transcript_list:
        text = entry["text"]
        if include_timestamps:
            ts = format_timestamp(entry["start"])
            lines.append(f"[{ts}] {text}")
        else:
            lines.append(text)

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")
