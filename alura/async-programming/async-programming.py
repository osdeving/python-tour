import marimo

__generated_with = "0.15.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import asyncio
    return (asyncio,)


@app.cell
def _(asyncio):
    async def temporizador():
        print("Iniciando temporizador...")
        await asyncio.sleep(3)
        print("Tempo finalizado após 3 segundos!")
    return (temporizador,)


@app.cell
def _(asyncio, temporizador):
    asyncio.run(temporizador())
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
