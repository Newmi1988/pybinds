from pybinds.moving_average import python_moving_average
from pybinds import rust_moving_average

from timeit import default_timer as timer

l = list(range(2000))

start = timer()
rma = rust_moving_average(
    v=l,
    window=2,
)
end = timer() - start
print(f"Time taken for rust implementation: {end:2}s")

start = timer()
pma = python_moving_average(
    v=l,
    window=2,
)
end = timer() - start
print(f"Time taken for implementation: {end:2}s")

