import asyncio
import or_XD

async def main():
    
    if hasattr(or_XD, "sub"):
        await or_XD.sub()
    
    elif hasattr(or_XD, "main"):
        r = or_XD.main()
        if asyncio.iscoroutine(r):
            await r
    else:
        print("or_XD module e kon function call korte hobe bujha jacche na:", [x for x in dir(or_XD) if not x.startswith("_")])

if __name__ == "__main__":
    asyncio.run(main())
