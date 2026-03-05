import asyncio
import Facebook_XD_64

async def main():
    
    if hasattr(Facebook_XD_64, "sub"):
        await Facebook_XD_64.sub()
    
    elif hasattr(Facebook_XD_64, "main"):
        r = Facebook_XD_64.main()
        if asyncio.iscoroutine(r):
            await r
    else:
        print("or_XD module e kon function call korte hobe bujha jacche na:", [x for x in dir(or_XD) if not x.startswith("_")])

if __name__ == "__main__":
    asyncio.run(main())
