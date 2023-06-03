def romberg_integration(f, a, b, n):
    h = b - a
    R = [[0] * (n+1) for _ in range(n+1)]

    R[0][0] = 0.5 * h * (f(a) + f(b))

    power_of_two = 1
    for i in range(1, n+1):
        h /= 2
        total = 0

        power_of_two *= 2
        for k in range(1, power_of_two, 2):
            total += f(a + k * h)

        R[i][0] = 0.5 * (R[i-1][0] + h * total)

        for j in range(1, i+1):
            R[i][j] = R[i][j-1] + (R[i][j-1] - R[i-1][j-1]) / ((4 ** j) - 1)

    return R[n][n]

# Define the function f(x)
def f(x):
    return x ** 2

# Define the limits of integration
a = 0
b = 2

# Set the desired order of accuracy
n = 15

# Call the Romberg integration function
result = romberg_integration(f, a, b, n)
print(result)