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

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

test:
	uv run pytest

lint:
	uv run ruff check gendiff

check: test lint

.PHONY: install gendiff build package-install package-uninstall test-coverage test lint check