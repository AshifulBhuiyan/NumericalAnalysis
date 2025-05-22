# Exercises: Partial Differential Equations

This section contains exercises related to the Partial Differential Equations module.

## Exercise 1: Classification

Classify the following PDEs as elliptic, parabolic, or hyperbolic:

1.  `∂²u/∂x² + 3 ∂²u/∂x∂y + 2 ∂²u/∂y² = 0`
2.  `∂u/∂t = ∂²u/∂x² - ∂u/∂x`
3.  `∂²u/∂x² - 4 ∂²u/∂x∂y + 4 ∂²u/∂y² + ∂u/∂x + 2u = 0`
4.  `uxx + uyy + uzz = f(x,y,z)` (for `u(x,y,z)`)

## Exercise 2: Heat Equation

Consider the 1D heat equation `∂u/∂t = α ∂²u/∂x²` with initial condition `u(x,0) = sin(πx)` for `0 ≤ x ≤ 1`, and boundary conditions `u(0,t) = 0`, `u(1,t) = 0`.

*   Briefly describe how you would set up a finite difference scheme (e.g., FTCS - Forward Time Centered Space) to solve this problem numerically.
*   What is the stability condition for the FTCS scheme for the heat equation?

## Exercise 3: Wave Equation

Consider the 1D wave equation `∂²u/∂t² = c² ∂²u/∂x²`.

*   Discretize this equation using central differences for both time and space derivatives.
*   What is the Courant-Friedrichs-Lewy (CFL) condition for this explicit scheme?

(More exercises to be added)
