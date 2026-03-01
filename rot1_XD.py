import platform
import sys

def main():
    if platform.architecture()[0] == "64bit":
        import or_XD

        # safe runner: or_XD এর ভিতরে কোন entrypoint আছে সেটা খুঁজে চালাবে
        if hasattr(or_XD, "main"):
            r = or_XD.main()
        elif hasattr(or_XD, "run"):
            r = or_XD.run()
        elif hasattr(or_XD, "asyncio") and hasattr(or_XD.asyncio, "run"):
            return or_XD.asyncio.run()
        else:
            print("or_XD module e kono runnable entrypoint pai nai (main/run/asyncio.run)")
            return

        # যদি main/run coroutine return করে, তাহলে asyncio.run() দিয়ে চালাবে
        if hasattr(r, "__await__"):
            import asyncio
            asyncio.run(r)

    else:
        print("32bit Not Supported! Sorry")
        sys.exit(1)

if __name__ == "__main__":
    main()
