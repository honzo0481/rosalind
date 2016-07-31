"""Tests module."""

import pytest


@pytest.fixture
def solver():
    import rosalind
    return rosalind.Solver


def test_dna(solver):
    """Test for dna."""
    s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
    solver = solver()
    assert solver.dna(s) == '20 12 17 21'
