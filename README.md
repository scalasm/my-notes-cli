# My Notes CLI

This is a simple REST client for validating how the API works

# How to update requirements.txt

We use `Pipenv` locally byt GitHub actions uses `requirements.txt`.

```
pipenv lock -d -r > requirements.txt
```

# References

* [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
* [Typer](https://typer.tiangolo.com/)
* [FastAPI](https://fastapi.tiangolo.com/)
