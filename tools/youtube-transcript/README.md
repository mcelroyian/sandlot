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

## Testing

### Quick Function Testing (Local - Python 3.8+)
Test the library and function logic locally:
```bash
cd tools/youtube-transcript
source venv/bin/activate  # Uses Python 3.8 venv
python test_transcript.py
python test_mcp_function.py
```

### Full MCP Server Testing (Docker - Recommended before deploy)
Test the complete MCP server in Docker (matches production environment):
```bash
cd tools/youtube-transcript
docker build -t youtube-transcript .
docker run --rm youtube-transcript python test_server_startup.py
```

This validates:
- All imports work correctly
- MCP server initializes without errors
- Transcript fetching works end-to-end

**Run this before every deployment** to catch issues early!

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
