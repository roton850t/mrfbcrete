import platform
import sys
import asyncio

def run_or_xd():
    import or_XD

    if hasattr(or_XD, "main"):
        r = or_XD.main()
    elif hasattr(or_XD, "run"):
        r = or_XD.run()
    elif hasattr(or_XD, "asyncio") and hasattr(or_XD.asyncio, "run"):
        return or_XD.asyncio.run()
    else:
        print("or_XD module e runnable entrypoint nai (main/run/asyncio.run)")
        return

    if hasattr(r, "__await__"):
        asyncio.run(r)

async def main_async():
    if platform.architecture()[0] != "64bit":
        print("32bit Not Supported! Sorry")
        sys.exit(1)

    # ✅ আগে check (তোমার gatekeeper/sub)
    from gate import sub   # gate.py তে তোমার sub() থাকবে
    ok = await sub()       # sub() True/False return করবে বলে ধরে নিচ্ছি

    if not ok:
        print("Not allowed / Not approved")
        return

    # ✅ তারপর আসল .so চালাও
    run_or_xd()

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
