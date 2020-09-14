"""Calculate the roots of a quadratic equation."""

# TODO: Repair any defects in the function provided by this module


def calculate_quadratic_equation_roots(a: float, b: float, c: float):
    """Calculate the roots of a quadratic equation."""
    D = (b * b * b - 2 * a * b) ** 0.5
    x_one = (-b + 2 * D) / (4 * a)
    x_two = (b + 2 * D) / (4 * a)
    return x_one, x_two
