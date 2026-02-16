# YouTube Transcript MCP Server

An MCP server that fetches YouTube transcripts, hosted on Fly.io.

## What it does

Exposes a single MCP tool — `get_youtube_transcript` — that accepts a YouTube URL and returns the video's transcript as plain text.

## Local Development

```bash
cd tools/youtube-transcript
pip install -r requirements.txt
python server.py
```

## Deployment

Deployed automatically to Fly.io via GitHub Actions on push to `main`.

Manual deploy:

```bash
fly deploy
```

## Connecting to Claude

### Claude Desktop / Claude.ai

Add to your MCP settings:

```json
{
  "mcpServers": {
    "youtube-transcript": {
      "url": "https://youtube-transcript-mcp.fly.dev"
    }
  }
}
```

### Claude Code CLI

```bash
claude mcp add youtube-transcript https://youtube-transcript-mcp.fly.dev
```

### Claude Code on the Web

Whitelist `youtube-transcript-mcp.fly.dev` in your Cloud Environment network settings.

## Environment Variables

None required for basic operation.

## Dependencies

- [mcp](https://github.com/anthropics/mcp) — MCP Python SDK
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) — Transcript fetching
