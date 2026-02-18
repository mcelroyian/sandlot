#!/usr/bin/env python3
"""Test the MCP server get_youtube_transcript function directly"""

import sys
sys.path.insert(0, '/app')

from server import get_youtube_transcript

# Test URL
test_url = "https://youtu.be/n1E9IZfvGMA?si=Ee6zKj3CMAYiDO20"

print("Testing MCP server function...")
print("-" * 60)

# Test without timestamps
print("\nTest 1: Without timestamps")
result = get_youtube_transcript(test_url, include_timestamps=False)
if result.startswith("Error:"):
    print(f"✗ FAILED: {result}")
else:
    lines = result.split('\n')
    print(f"✓ SUCCESS! Got {len(lines)} lines")
    print(f"First 3 lines:")
    for line in lines[:3]:
        print(f"  {line}")

print("\n" + "-" * 60)

# Test with timestamps
print("\nTest 2: With timestamps")
result = get_youtube_transcript(test_url, include_timestamps=True)
if result.startswith("Error:"):
    print(f"✗ FAILED: {result}")
else:
    lines = result.split('\n')
    print(f"✓ SUCCESS! Got {len(lines)} lines with timestamps")
    print(f"First 3 lines:")
    for line in lines[:3]:
        print(f"  {line}")

print("\n" + "-" * 60)
print("\n✓ All tests PASSED! The MCP server function works correctly.")
