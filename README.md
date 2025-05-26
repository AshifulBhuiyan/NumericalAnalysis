# Numerical Analysis

## Overview
This repository contains a comprehensive collection of numerical methods and techniques used for solving various mathematical problems, particularly in the fields of calculus, differential equations, and numerical integration. The methods are implemented and demonstrated through Jupyter notebooks, providing a practical approach to understanding numerical analysis.

Mainly, what I used to study and learn Numerical Analysis.

## Contents

### 1. Differentiation
- **Finite Difference Methods**: Implementation of forward, backward, and central difference methods for numerical differentiation.
- **Automatic Differentiation**: A custom implementation of automatic differentiation using `Tensor` and `Variable` classes to compute derivatives to machine precision.
- **Graphing Tangents**: Visualizing functions and their tangent lines using numerical derivatives.

### 2. Series
- **Geometric Series**: Functions to compute the sum of geometric series.

### 3. Differential Equations
- **First Order Linear ODEs**: Implementation of methods to solve first-order linear differential equations using analytical techniques and numerical methods like Euler's method.
- **Runge-Kutta Methods**: High-order methods for solving ordinary differential equations (ODEs) with improved accuracy.

### 4. Numerical Integration
- **Composite Simpson's Rule**: A method for numerical integration using Simpson's rule.
- **Romberg Integration**: An implementation of Romberg integration which combines the trapezoidal rule with Richardson extrapolation for increased accuracy.
- **Adaptive Quadrature**: Techniques for adaptive integration based on error estimates.

### 5. Root Finding
- **Bisection Method**: A method for finding roots of functions by repeatedly dividing an interval in half.
- **Newton's Method**: An iterative method for finding successively better approximations to the roots of a real-valued function.

### 6. Interpolation
- **Neville's Method**: Implementation of Neville's iteration for polynomial interpolation.
- **Lagrange Interpolation**: A method for polynomial interpolation based on Lagrange polynomials.

### 7. Matrix Methods
- **Gaussian Elimination**: Techniques for solving systems of linear equations.
- **Gauss-Seidel Method**: An iterative method for solving a system of linear equations.

### 8. Partial Differential Equations
- **Heat Equation**: Numerical methods for solving the heat equation using finite difference methods.
- **Poisson's Equation**: Implementation of finite difference methods to solve Poisson's equation.

## Requirements
To run the notebooks, you will need the following Python packages:
- NumPy
- Matplotlib
- SciPy
- Pandas

You can install the required packages using the following command:
```bash
pip install numpy matplotlib scipy pandas
