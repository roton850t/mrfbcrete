import platform
import asyncio
import sys

def load_module():
    arch = platform.machine()

    if "aarch64" in arch or "64" in arch:
        import Facebook_XD_64 as Facebook_XD
    else:
        import Facebook_XD_32 as Facebook_XD

    return Facebook_XD


async def main():
    Facebook_XD = load_module()

    if hasattr(Facebook_XD, "sub"):
        await Facebook_XD.sub()

    elif hasattr(Facebook_XD, "main"):
        r = Facebook_XD.main()
        if asyncio.iscoroutine(r):
            await r

    else:
        print("Module e kon runnable function pai nai (sub/main)")


if __name__ == "__main__":
    asyncio.run(main())
