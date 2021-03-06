#!/usr/bin/env python3

# Note: This script runs depth
import sys
import asyncio
from depth import __main__

if __name__ == '__main__':
    platform = sys.platform
    if platform == 'win32':
        # Required or things will break if trying to take screenshots
        import multiprocessing
        multiprocessing.freeze_support()
        asyncio.DefaultEventLoopPolicy = asyncio.WindowsSelectorEventLoopPolicy
    else:
        import uvloop
        uvloop.install()

        if "linux" in platform:
            import aiomultiprocess
            # As I am not using Windows I can change the spawn method to fork for greater performance
            aiomultiprocess.set_context("fork")
    asyncio.run(__main__.entry_point())
