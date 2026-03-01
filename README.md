# aztools

Python Azure tools.

## Installation

The Python tools are should work with all versions of Python >= 3.10 but has been designed to work best with [uv](https://docs.astral.sh/uv/getting-started/installation/).

## Usage

```sh
az login # if needed
uv run <script>
```

For more information on logging on with [AZ CLI](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest#az-login)

## Development

```sh

uv sync # install with dev dependencies
uv run ruff check . # lint
uv run ruff format . # format
uv run pyright # type check
uv run pytest # run tests
```
