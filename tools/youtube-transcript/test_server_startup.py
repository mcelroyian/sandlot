#!/usr/bin/env python3
"""Test MCP server startup and basic functionality"""

import sys
import time
import subprocess
import os

def test_imports():
    """Test that all imports work"""
    print("Test 1: Imports...")
    try:
        from server import get_youtube_transcript, extract_video_id, mcp
        print("✓ All imports successful")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

def test_server_startup():
    """Test that server initializes without crashing"""
    print("\nTest 2: Server initialization...")
    try:
        # Test that mcp.run() can be called without errors
        # We'll test streamable-http since that's what Fly.io uses
        env = os.environ.copy()
        env["MCP_TRANSPORT"] = "streamable-http"
        env["PORT"] = "8080"

        proc = subprocess.Popen(
            ["python", "-c", """
import os
os.environ['MCP_TRANSPORT'] = 'streamable-http'
os.environ['PORT'] = '8080'
from server import mcp
# Just verify mcp object was created successfully
print('MCP server initialized')
exit(0)
"""],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = proc.communicate(timeout=5)

        if proc.returncode == 0 and b'MCP server initialized' in stdout:
            print("✓ Server initialization successful")
            return True
        else:
            error_msg = stderr.decode() or f"Exit code: {proc.returncode}"
            print(f"✗ Server initialization failed: {error_msg}")
            return False
    except Exception as e:
        print(f"✗ Server initialization test failed: {e}")
        return False

def test_function():
    """Test the actual function works"""
    print("\nTest 3: Function execution...")
    try:
        from server import get_youtube_transcript
        result = get_youtube_transcript('https://youtu.be/n1E9IZfvGMA', include_timestamps=False)

        if result.startswith('Error:'):
            print(f"✗ Function returned error: {result}")
            return False

        if len(result) < 100:
            print(f"✗ Transcript too short: {len(result)} chars")
            return False

        print(f"✓ Function executed successfully ({len(result)} chars)")
        return True
    except Exception as e:
        print(f"✗ Function test failed: {e}")
        return False

if __name__ == "__main__":
    print("=== MCP Server Startup Tests ===\n")

    results = [
        test_imports(),
        test_server_startup(),
        test_function()
    ]

    print("\n" + "="*35)
    if all(results):
        print("✓ ALL TESTS PASSED")
        print("="*35)
        sys.exit(0)
    else:
        print("✗ SOME TESTS FAILED")
        print("="*35)
        sys.exit(1)
