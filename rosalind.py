"""Problem solver module."""

import collections
import re

import click
import requests

# log in
# get problems in list view
# parse page for links to problems
#


class Solver(object):
    """A class for solving Rosalind problems and submitting the answers online."""

    def __init__(self):
        self.logged_in = False
        self.s = requests.session()

    def login(self, username, password):
        """Log into rosalind.info."""
        # get /login to find the csrf token
        self.r = self.s.get(r'http://rosalind.info/accounts/login/')
        form_data = {
            'csrfmiddlewaretoken': self.r.headers['Set-Cookie'].split(';')[0].split('=')[-1],
            'next': '',
            'username': str(username),
            'password': str(password)
        }
        # post credentials + token to /login
        self.r = self.s.post(r'http://rosalind.info/accounts/login/', data=form_data)
        self.r.raise_for_status()
        self.logged_in = True

    # TODO
    def download_dataset(self, problem):
        """Download a dataset from Rosalind.info."""
        url = r'rosalind.info/problems/'
        url = url + problem

        self.r = self.s.get(url, stream=True)

    def dna(self, s):
        """Count the nucleotides in the a DNA string.

        returns a space delimited list of nucleotide counts in the format: A C G T
        """
        counts = collections.defaultdict(int)

        for base in s:
            counts[base] += 1

        return '%s %s %s %s' % (counts['A'], counts['C'], counts['G'], counts['T'])

    def rna(self, t):
        """Convert DNA to RNA.

        Returns an RNA string.
        """
        return t.replace('T', 'U')

    def revc(self, s):
        """Find the reverse compliment of a DNA string."""


@click.command('solve')
@click.argument('problem')
@click.option('--username', prompt='username: ')
@click.password_option()
def solve(problem, username, password):
    """Solve Rosalind.info problems.

    This is a set of tools for downloading datasets, solving problems and
    uploading the answers back to the web.
    """
    solver = Solver()
    solver.login(username, password)


if __name__ == '__main__':
    solve()
