#!/usr/bin/env python3
"""Simple status viewer for the JX project."""

import platform
import datetime
import os


def get_status():
    """Collect and display current status information."""
    print("=" * 40)
    print("JX Status Viewer")
    print("=" * 40)
    print(f"Time     : {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"OS       : {platform.system()} {platform.release()}")
    print(f"Python   : {platform.python_version()}")
    print(f"Host     : {platform.node()}")
    print(f"Directory: {os.getcwd()}")
    print("=" * 40)


if __name__ == "__main__":
    get_status()
