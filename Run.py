import asyncio
import Facebook_XD

async def main():
    
    if hasattr(Facebook_XD, "sub"):
        await Facebook_XD.sub()
    
    elif hasattr(Facebook_XD, "main"):
        r = Facebook_XD.main()
        if asyncio.iscoroutine(r):
            await r
    else:
        print("or_XD module e kon function call korte hobe bujha jacche na:", [x for x in dir(or_XD) if not x.startswith("_")])

if __name__ == "__main__":
    asyncio.run(main())
