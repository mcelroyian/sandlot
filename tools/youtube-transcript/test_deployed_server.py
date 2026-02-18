#!/usr/bin/env python3
"""Test the deployed MCP server on Fly.io"""

import asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

async def test_deployed_server():
    """Test the get_youtube_transcript tool on the deployed server"""

    server_url = "https://youtube-transcript-mcp-solitary-sunset-6925.fly.dev/mcp"

    print("🔍 Testing deployed MCP server...")
    print(f"   URL: {server_url}\n")

    try:
        async with sse_client(server_url) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize
                await session.initialize()

                # List available tools
                print("📋 Available tools:")
                tools = await session.list_tools()
                for tool in tools.tools:
                    print(f"   • {tool.name}: {tool.description}")

                print("\n🎬 Testing get_youtube_transcript...")

                # Call the tool
                result = await session.call_tool(
                    "get_youtube_transcript",
                    arguments={
                        "url": "https://youtu.be/n1E9IZfvGMA",
                        "include_timestamps": False
                    }
                )

                # Check result
                if result.content:
                    text_content = result.content[0].text if result.content else ""

                    if text_content.startswith("Error:"):
                        print(f"   ✗ Tool returned error: {text_content}")
                        return False

                    if len(text_content) < 100:
                        print(f"   ✗ Transcript too short: {len(text_content)} chars")
                        return False

                    print(f"   ✓ Success! Got {len(text_content)} character transcript")
                    print(f"   Preview: {text_content[:100]}...")
                    return True
                else:
                    print("   ✗ No content in result")
                    return False

    except Exception as e:
        print(f"   ✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_deployed_server())

    print("\n" + "="*50)
    if success:
        print("✅ DEPLOYED SERVER WORKING!")
        print("Safe to connect to Claude.")
    else:
        print("❌ SERVER TEST FAILED")
        print("Do not connect to Claude yet.")
    print("="*50)

    exit(0 if success else 1)
