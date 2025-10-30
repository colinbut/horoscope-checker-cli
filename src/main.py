import typer

app = typer.Typer()

@app.command()
def version():
    print("v0.0.1")

@app.command()
def check(day: str, month: str):
    pass

if __name__ == "__main__":
    app()