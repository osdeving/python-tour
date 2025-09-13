import asyncio

async def temporizador():
    print("Iniciando...")
    await asyncio.sleep(3)
    print("Finalizado após 3 segundos")

asyncio.run(temporizador())
