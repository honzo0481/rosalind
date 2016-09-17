"""Problem solver module."""

import collections

import click
import requests

# log in
# get problems in list view
# parse page for links to problems
#


class Solver(object):
    """A class for solving Rosalind problems and submitting the answers online."""

    def __init__(self):
        """Initialize a Solver."""
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
        base_converter = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
        compliment = ''
        for base in s:
            compliment = compliment + base_converter[base]
        reverse_compliment = compliment[::-1]
        return reverse_compliment

    def fib(self, n, k):
        """Find the sum of of a modified fibonacci sequence.

        Return the fibonacci number Fn if Fn = k * Fn-2 + Fn-1
        instead of Fn-2 + Fn-1
        """
        n, k = int(n), int(k)

        memo = {0: 0, 1: 1}

        def inner(n):
            if n not in memo:
                n = inner(n-1) + inner(n-2) * k
                memo[n] = n
            return memo[n]

        return str(inner(n))


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
