# youtube-transcript MCP Tool

## What it does
Fetches the transcript of any YouTube video given a URL.

## Tool name
`get_youtube_transcript`

## Parameters
- `url` (string, required): Any YouTube URL format — youtu.be, youtube.com/watch?v=, etc.
- `include_timestamps` (boolean, optional, default false): Prefix each line with [MM:SS]

## When to use it
- User shares a YouTube URL and wants to discuss, summarize, or reference its content
- User asks about something from a video
- Any task that requires reading or working with YouTube video content

## Example
`get_youtube_transcript(url="https://youtu.be/dQw4w9WgXcQ", include_timestamps=True)`

## Hosted at
`https://youtube-transcript-mcp.fly.dev`
