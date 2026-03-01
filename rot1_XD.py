import platform
import sys

def main():
    if platform.architecture()[0] == "64bit":
        import stex_XD
        stex_XD.asyncio.run()
    else:
        print("32bit Not Supported! Sorry")
        sys.exit(1)
