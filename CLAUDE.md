# Sandlot Project

## Repository Structure
- **MCP servers**: Located in `tools/` directory
- Each MCP server has its own:
  - `Dockerfile` for deployment
  - `requirements.txt` for dependencies
  - `server.py` as main entry point
- **Skills**: Custom Claude Code skills stored in `.claude/skills/`

## MCP Servers

### Testing Pattern
Test MCP servers in Docker before deployment:
1. **Import test**: Verify all imports work without errors
2. **Initialization test**: Verify MCP object initializes successfully
3. **Function test**: Verify tool functions execute correctly

No need to test full MCP protocol - startup and basic functionality is sufficient. See `test_server_startup.py` for example.

### YouTube Transcript (`tools/youtube-transcript/`)
- Fetches YouTube video transcripts using `youtube-transcript-api`
- MCP tool: `get_youtube_transcript(url, include_timestamps=False)`
- Python 3.12 in Docker, may differ from local Python version
- Uses FastMCP framework from Anthropic
- Test with: `docker run --rm youtube-transcript python test_server_startup.py`
- **Local-only deployment**: YouTube blocks cloud provider IPs (Fly.io, AWS, etc.). Must run locally via Docker stdio, not deployed to cloud.
- **Claude Code MCP config**: `claude mcp add youtube-transcript stdio -- sudo docker run -i --rm youtube-transcript sh -c 'MCP_TRANSPORT=stdio python server.py'`
