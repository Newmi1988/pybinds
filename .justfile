# install python deps
init:
  poetry install --sync

# update python and rust packages
update:
  poetry update
  cargo update

# build rust code
build:
  poetry run maturin build --release

# install compiled package
install: init build
  poetry run pip install --force-reinstall "./target/wheels/$(ls -Art ./target/wheels| tail -n 1 | xargs)"

# compile develop version
develop:
  poetry run maturin develop
  poetry run pip install --force-reinstall "./target/wheels/$(ls -Art ./target/wheels| tail -n 1 | xargs)"

# test the package
test *FLAGS:
  poetry run pytest --cov=pybinds -v -rpa {{FLAGS}}

# build the package using a docker image
docker-build:
  docker run --rm -v $(pwd):/io ghcr.io/pyo3/maturin build --release  # or other maturin arguments
