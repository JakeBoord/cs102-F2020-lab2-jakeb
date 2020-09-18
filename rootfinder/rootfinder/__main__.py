"""Define the command-line interface for the rootfinder program."""

import typer

from rootfinder import rootfind


def main(
    a: float = typer.Option(1), b: float = typer.Option(2), c: float = typer.Option(3)
):
    """Calculate the roots of a quadratic equation using the quadratic formula."""
    # display the debugging output for the program's command-line arguments
    typer.echo(f"Calculating the reals of a quadratic equation with:")
    typer.echo(f"   a = {a}")
    typer.echo(f"   b = {b}")
    typer.echo(f"   c = {c}")
    # perform the calculation of the roots for the quadratic equation
    x_one, x_two = rootfind.calculate_quadratic_equation_roots(a, b, c)
    # output the values from running the calculation of the quadratic
    # equation's roots with the calculate_quadratic_equation_roots function
    typer.echo(f"   x_one = {x_one}")
    typer.echo(f"   x_two = {x_two}")


if __name__ == "__main__":
    typer.run(main)
