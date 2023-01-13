import logging
from timeit import default_timer

import pytest
from timer import timer

from pybinds import rust_moving_average
from pybinds.moving_average import python_moving_average

logging.basicConfig(level=logging.DEBUG)

# @pytest.fixture
# def long_list() -> List[int]:
# l = list(range(2_000_000))
# w = 1000

def test_python_implementation():
    assert [1] == python_moving_average(
        v = [1,1,1],
        window = 3
    )

def test_rust_implementation():
    assert [1] == rust_moving_average(
        v = [1,1,1],
        window = 3
    )

@pytest.mark.parametrize("l", [list(range(10**i)) for i in range(4,7)])
@pytest.mark.parametrize("w", [10**i for i in range(4)])
def test_moving_average_implementation(l, w):
    print(f"len(v): {len(l)}, window:{w}")
    start = default_timer()
    with timer():
        rma = rust_moving_average(
            v=l,
            window=w,
        )
    rust_end = default_timer() - start
    print(f"Time taken for rust implementation: {rust_end:.6E}s")

    start = default_timer()
    with timer():
        pma = python_moving_average(
            v=l,
            window=w,
        )
    python_end = default_timer() - start
    print(f"Time taken for implementation: {python_end:.6E}s")

    print(f"Rust is {python_end / rust_end:.4F} faster than python")

    assert pytest.approx(rma,0.01) == pma
    assert rust_end < python_end
