install:
  poetry run pip install --force-reinstall ./target/wheels/pybinds-0.1.0-cp310-cp310-macosx_11_0_arm64.whl

build:
  poetry run maturin build --release
  poetry run pip install --force-reinstall ./target/wheels/pybinds-0.1.0-cp310-cp310-macosx_11_0_arm64.whl

debug:
  poetry run maturin develop
  poetry run pip install --force-reinstall ./target/wheels/pybinds-0.1.0-cp310-cp310-macosx_11_0_arm64.whl

test:
  poetry run pytest --cov=pybinds -v -rpa
