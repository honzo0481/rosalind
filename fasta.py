"""Fasta parser.

FASTA is a textual format for representing sequence information. It consists of
a description line which starts with a `>` symbol followed by sequence lines
consisting of standard IUB/IUPAC amino or nucleic acid codes usually 80 characters
or less. Input is not case sensitive but output should be uppercase. Numbers in
sequence data are either removed or replaced with unknown letter codes.

The codes map as follows:

nucleic acids:
 code: meaning             code: meaning
 ----  -------             ----  -------
    A: adenosine              M: A or C (amino)
    T: thymidine              B: G or T or C
    C: cytidine               S: G or C (strong)
    G: guanine                W: A or T (weak)
    U: uridine                D: G or A or T
    R: G or A (purine)        H: A or C or T
    Y: T or C (pyrimidine)    V: G or C or A
    K: G or T (keto)          N: A or G or C or T
    -: arbitrary gap

amino acids:
 code: codon: meaning                      code: codon: meaning
 ----  -----  -------                      ----  -----  -------
    A:   ALA: alanine                         P:   PRO: proline
    B:   ASX: aspartate or asparagine         Q:   GLN: glutamine
    C:   CYS: cystine                         R:   ARG: arginine
    D:   ASP: aspartate                       S:   SER: serine
    E:   GLU: glutamate                       T:   THR: threonine
    F:   PHE: phenylalanine                   U:      : selenocysteine
    G:   GLY: glycine                         V:   VAL: valine
    H:   HIS: histidine                       W:   TRP: tryptophan
    I:   ILE: isoleucine                      Y:   TYR: tyrosine
    K:   LYS: lysine                          Z:   GLX: glutamate or glutamine
    L:   LEU: leucine                         X:      : any
    M:   MET: methionine                      *:      : stop codon
    N:   ASN: asparagine                      -:      : arbitrary gap
"""

import re
from collections import namedtuple


Sequence = namedtuple('Sequence', 'description sequence')


class Parser:
    """Parses FASTA sequence records.

    Only uppercase nucleic acid sequences without numbers can be parsed.
    """

    def __call__(record):
        """Parse a FASTA sequence record."""
        pattern = r'\>(.+)\s([-ATCGURYKMBSWDHVN\n]+)'
        parse = re.findall(pattern, record)
        result = [Sequence(*item) for item in parse]
        return result
