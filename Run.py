import platform
import asyncio
import sys

def load_module():
    arch = platform.machine().lower()

    try:
        if "aarch64" in arch or "arm64" in arch or "64" in arch:
            import pss_XD as module
        else:
            import Facebook_XD_32 as module

        return module

    except Exception as e:
        print(f"MODULE LOAD ERROR: {e}")
        sys.exit(1)


async def main():
    module = load_module()

    if hasattr(module, "sub"):
        result = module.sub()
        if asyncio.iscoroutine(result):
            await result

    elif hasattr(module, "main"):
        result = module.main()
        if asyncio.iscoroutine(result):
            await result

    else:
        print("Module e 'sub' ba 'main' function nai")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
