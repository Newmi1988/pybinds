use pyo3::{prelude::*, types::PyList};

/// Formats the sum of two numbers as string.
#[pyfunction]
fn rust_moving_average(v: &PyList, window : usize) -> PyResult<Vec<f32>> {

    let mut moving_average : Vec<f32> = Vec::new();

    let vec : Vec<f32> = v.extract()?;
    for slice in vec.iter().collect::<Vec<_>>().windows(window) {
        let slice_sum : f32 = slice.iter().copied().sum();
        let slice_average = slice_sum / (window as f32);
        moving_average.push(slice_average)
    }
    Ok(moving_average)
}


/// A Python module implemented in Rust.
#[pymodule]
fn pybinds(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rust_moving_average, m)?)?;
    Ok(())
}
