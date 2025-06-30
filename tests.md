# Calculator Unit Tests

This document outlines the unit tests created for the `Calc` class in `calc.py`. The tests are written using Python's built-in `unittest` framework.

## Test Coverage

The test suite covers all public methods of the `Calc` class. For each method, we test the basic functionality as well as important edge cases to ensure the code is robust.

### Addition: `test_add`

* Tests basic addition of two positive numbers.
* **Edge Case**: Tests addition with a negative number.
* **Edge Case**: Tests addition of two negative numbers.

### Subtraction: `test_sub`

* Tests basic subtraction.
* **Edge Case**: Tests subtraction with negative numbers.

### Multiplication: `test_mul`

* Tests basic multiplication.
* **Edge Case**: Tests multiplication by zero.
* **Edge Case**: Tests multiplication with a negative number.

### Division: `test_div`

* Tests basic division.
* **Edge Case**: Tests division that results in a floating-point number.
* **Edge Case**: Tests for `ZeroDivisionError` when dividing by zero.
    ```python
    with self.assertRaises(ZeroDivisionError):
        self.calc.div(10, 0)
    ```

### Power: `test_pow`

* Tests raising a number to a power.
* **Edge Case**: Tests raising a number to the power of zero.

### Square Root: `test_sqrt`

* Tests the square root of a perfect square.
* **Edge Case**: Tests the square root of zero.
* **Edge Case**: Tests the square root of a number that results in a float, using `assertAlmostEqual` for precision.