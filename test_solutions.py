"""Solutions tests."""

import pytest
import csv


@pytest.fixture
def solver():
    """Return a solver object as a fixture."""
    import rosalind
    return rosalind.Solver


def load_csv(filepath, cols=None):
    """Load data from a csv."""
    with open(filepath) as f:
        reader = csv.reader(f)
        if cols is None:
            data = [row for row in reader]
        else:
            data = [[row[col] for col in sorted(cols)] for row in reader if len(row) > 0]
    # drop the header
    return data[1:]


@pytest.mark.parametrize('input_data, output_data',
                         load_csv('test_data.csv', cols=(1, 2))
                         )
def test_in_ne_out(input_data, output_data):
    """Input should never equal output."""
    assert input_data != output_data


@pytest.mark.parametrize('problem, input_data, output_data', load_csv('test_data.csv'))
def test_solution(solver, problem, input_data, output_data):
    """Output from problem function given input_data should exactly match output_data."""
    # if there is no solution implemented in solver fall back to comparing the
    # input and output strings, which will always fail.
    solver = solver()
    try:
        solver = getattr(solver, problem.lower())
    except AttributeError:
        solver = str
    assert solver(*input_data.split()) == output_data, problem
