# Module 1: Partial Differential Equations (PDEs)

This module introduces the concepts of Partial Differential Equations, their classification, and fundamental numerical solution techniques.

## Topics Covered

*   Introduction to PDEs
*   Types of PDEs (Elliptic, Parabolic, Hyperbolic)
*   Finite Difference Methods
*   Finite Element Methods (Overview)

## Learning Objectives

*   Understand the definition and origin of PDEs.
*   Classify PDEs into elliptic, parabolic, and hyperbolic types.
*   Understand the discretization principles of Finite Difference Methods.
*   Be aware of the basic concepts of Finite Element Methods.

## Introduction to PDEs

A Partial Differential Equation (PDE) is an equation that involves partial derivatives of an unknown multivariable function. PDEs are used to model a wide variety of phenomena in science and engineering, such as heat flow, wave propagation, fluid dynamics, and electromagnetism.

Unlike Ordinary Differential Equations (ODEs), which involve derivatives with respect to a single independent variable, PDEs deal with functions of two or more independent variables (e.g., `u(x,y)`, `u(x,t)`, `u(x,y,z,t)`).

The general form of a PDE can be complex, but many important PDEs are of first or second order.

**Examples of famous PDEs:**

*   **Laplace's Equation:** `∇²u = ∂²u/∂x² + ∂²u/∂y² = 0` (Elliptic)
*   **Heat Equation:** `∂u/∂t = α ∇²u` (Parabolic)
*   **Wave Equation:** `∂²u/∂t² = c² ∇²u` (Hyperbolic)

## Types of PDEs

Second-order linear PDEs in two variables are generally classified into three types: elliptic, parabolic, and hyperbolic. This classification is based on the characteristics of the PDE and is crucial because each type describes different kinds of phenomena and often requires different solution techniques.

Consider a general second-order linear PDE of the form:

`A ∂²u/∂x² + B ∂²u/∂x∂y + C ∂²u/∂y² + D ∂u/∂x + E ∂u/∂y + Fu + G = 0`

The classification depends on the discriminant `Δ = B² - 4AC`:

*   **Elliptic PDEs (Δ < 0):** These equations typically model steady-state phenomena or equilibrium states. They often describe processes that have already reached a stable condition. Boundary conditions must be specified on the entire boundary of the domain.
    *   *Example:* Laplace's equation, Poisson's equation.

*   **Parabolic PDEs (Δ = 0):** These equations usually describe time-dependent diffusion processes, like heat conduction or a diffusing chemical concentration. They are often associated with initial value problems that evolve over time.
    *   *Example:* Heat equation, Black-Scholes equation.

*   **Hyperbolic PDEs (Δ > 0):** These equations typically model wave propagation phenomena and other transport processes. They also are often associated with initial value problems.
    *   *Example:* Wave equation, advection equation.

This classification can be extended to PDEs with more than two independent variables or higher-order PDEs, but it becomes more complex.
