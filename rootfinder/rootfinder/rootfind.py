"""Calculate the roots of a quadratic equation."""


def calculate_quadratic_equation_roots(a: float, b: float, c: float):
    # Calculate the roots of a quadratic equation.
    D = (b * b - 4 * a * c) ** 0.5
    x_one = (-b + D) / (2 * a)
    x_two = (-b - D) / (2 * a)
    return x_one, x_two
