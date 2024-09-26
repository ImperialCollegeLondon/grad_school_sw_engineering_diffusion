import math

import pytest

from diffusion import heat


def linspace(start, stop, num):
    return [start + x * (stop - start) / (num - 1) for x in range(num)]


def test_heat():
    nt = 10
    nx = 20
    alpha = 0.01
    L = 1
    tmax = 0.5

    xs = linspace(0, L, nx)

    numerical_solution = heat(
        [0] + [math.sin(math.pi * x / L) for x in xs][1:-1] + [0],
        nt,
        nx,
        alpha,
        L,
        tmax,
    )

    analytical_solution = (
        [0]
        + [
            math.sin(math.pi * x / L) * math.exp(-tmax * alpha * (math.pi / L) ** 2)
            for x in xs[1:-1]
        ]
        + [0]
    )

    assert numerical_solution == pytest.approx(analytical_solution, abs=1e-2)
