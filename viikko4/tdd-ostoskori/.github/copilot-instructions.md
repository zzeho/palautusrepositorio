# Repository instructions

## Project and environment

- This is a small Python 3.14 shopping-cart exercise managed by uv.
- The project has no application entry point in `src/index.py`; it currently contains placeholder text.
- Python dependencies are declared in `pyproject.toml`, and the lockfile is `uv.lock`.
- Install or refresh the development environment with `uv sync --group dev`.
- Use Python 3.14, matching `.python-version` and `requires-python`.

## Build, test, and lint commands

- Always implement absolutely minimal code that makes the tests pass
- Tests should not be edited unless explicitly asked
- Code of `src/ostos.py` and `src/tuote.py` should not be changed
- Tests executed with uv run pytest
- Run the complete test suite from the repository root: `uv run pytest`
- Run one test file: `uv run pytest src/tests/ostoskori_test.py`
- Run one test by node ID:
  `uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa`
- The tests use the standard-library `unittest` style and pytest discovery. New tests in `src/tests/` should follow existing `*_test.py` and `Test...` naming.
- There is currently no configured build, formatter, or linter command.

## Architecture

- `src/tuote.py` defines `Tuote`, which owns a name and integer price.
- `src/ostos.py` defines `Ostos`, the quantity-bearing item wrapper around one `Tuote`. `Ostos.hinta()` is quantity multiplied by the product price.
- `src/ostoskori.py` defines `Ostoskori`, the aggregate cart. It stores a list of `Ostos` values and:
  - groups repeated products by matching product name;
  - sums item quantities for `tavaroita_korissa()` and line totals for `hinta()`;
  - removes a line when its quantity reaches zero;
  - exposes `tyhjenna()` for clearing the cart.
- Runtime modules are in `src/` and import sibling modules directly, for example `from tuote import Tuote`; maintain that layout rather than introducing package-relative imports unless the project structure is changed deliberately.

## Code conventions

- Source and test identifiers are primarily Finnish; keep names consistent with the existing domain vocabulary (`ostoskori`, `ostos`, `tuote`, `lisattava`, `poistettava`, `lukumaara`).
- Public behavior is expressed through methods rather than properties. Preserve the established method-style API unless a change intentionally updates the full call surface.
- `Ostoskori.ostokset()` and `Ostoskori.ostokset` currently name both a method and the instance attribute. Changes around that API should consider both existing call patterns.
- Quantity mutation is expected to prevent negative quantities; keep cart and line quantity behavior coherent when changing `Ostos` or `Ostoskori`.
