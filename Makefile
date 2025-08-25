install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall hexlet-code

lint:
	uv run ruff check gendiff