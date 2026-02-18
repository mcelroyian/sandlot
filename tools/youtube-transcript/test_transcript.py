#!/usr/bin/env python3
"""Simple test script for youtube-transcript-api"""

from youtube_transcript_api import YouTubeTranscriptApi
from typing import Optional
import re

def extract_video_id(url: str) -> Optional[str]:
    """Extract a YouTube video ID from various URL formats."""
    patterns = [
        r"(?:youtube\.com/watch\?.*v=|youtu\.be/|youtube\.com/embed/|youtube\.com/v/|youtube\.com/shorts/)([a-zA-Z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    if re.fullmatch(r"[a-zA-Z0-9_-]{11}", url.strip()):
        return url.strip()
    return None

# Test URL
test_url = "https://youtu.be/n1E9IZfvGMA?si=Ee6zKj3CMAYiDO20"

print(f"Testing YouTube Transcript API with URL: {test_url}")
print("-" * 60)

video_id = extract_video_id(test_url)
print(f"Extracted Video ID: {video_id}")
print("-" * 60)

try:
    api = YouTubeTranscriptApi()
    transcript_obj = api.fetch(video_id)
    transcript = transcript_obj.to_raw_data()
    print(f"✓ Successfully fetched transcript!")
    print(f"✓ Total segments: {len(transcript)}")
    print(f"\nFirst 5 segments:")
    print("-" * 60)

    for i, entry in enumerate(transcript[:5]):
        start = int(entry['start'])
        mins = start // 60
        secs = start % 60
        print(f"[{mins:02d}:{secs:02d}] {entry['text']}")

    print("-" * 60)
    print(f"\n✓ Test PASSED! The youtube-transcript-api library works correctly.")

except Exception as e:
    print(f"✗ Test FAILED!")
    print(f"Error: {e}")
