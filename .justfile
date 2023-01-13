init:
  poetry install

update:
  poetry update
  cargo update

install:
  poetry run pip install --force-reinstall "./target/wheels/$(ls -Art ./target/wheels| tail -n 1 | xargs)"

build:
  poetry run maturin build --release
  poetry run pip install --force-reinstall "./target/wheels/$(ls -Art ./target/wheels| tail -n 1 | xargs)"

develop:
  poetry run maturin develop
  poetry run pip install --force-reinstall "./target/wheels/$(ls -Art ./target/wheels| tail -n 1 | xargs)"

test *FLAGS:
  poetry run pytest --cov=pybinds -v -rpa {{FLAGS}}
