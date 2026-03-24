import platform
import asyncio
import sys

def load_module():
    arch = platform.machine()

    if "aarch64" in arch or "64" in arch:
        import pss_XD as Facebook_XD
    else:
        import Facebook_XD_32 as pss_XD

    return pss_XD


async def main():
    pss_XD = load_module()

    if hasattr(pss_XD, "sub"):
        await pss_XD.sub()

    elif hasattr(pss_XD, "main"):
        r = pss_XD.main()
        if asyncio.iscoroutine(r):
            await r

    else:
        print("Module e kon runnable function pai nai (sub/main)")


if __name__ == "__main__":
    asyncio.run(main())

