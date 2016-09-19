"""Fasta parser tests."""

import pytest
import fasta


@pytest.fixture
def record():
    """Return a sequence record in fasta format."""
    record = ('>seq0\n'
              'GAAACAGTGAACGGGAAGGATTTGGGGCAGCAGTACCTTCGACCTCTCAAGTCATACTACATGGAAATCTTTCTA\n'
              '>seq1\n'
              'CTCCAAATATACAAAGGCAAGGTATCATATGTCCTGGTCTCGATGAAATGGCAGAACCTGCTATAACCCACCCGAGAAAT\n'
              '>seq2\n'
              'ACGTTCTTGGAGATAGTAGTACATCCCAACCAAATAGCTAGCACTGCGTCAGAACGTGGCCACATAGTTTCCCCTGGAGA\n'
              'AATCAATGCTACCTGGAGATTGCAATGAATCTGTCTTACTGAACCCGGGACAGGTATCGTATCGTCGAACGAGAACCGGT\n'
              'AATGCCTCGACGCTTCTGCT\n'
              )
    return record


@pytest.fixture
def parser():
    """Return a fasta parser."""
    parser = fasta.Parser()
    return parser


def test_string_2_sequences(record, parser):
    """Fasta parser should parse a record string into sequence objects."""
    assert parser(record) == [fasta.Sequence('seq0', 'GAAACAGTGAACGGGAAGGATTTGGGGCAGCAGTACCTTCGACCTCTCAAGTCATACTACATGGAAATCTTTCTA\n'),
                              fasta.Sequence('seq1', 'CTCCAAATATACAAAGGCAAGGTATCATATGTCCTGGTCTCGATGAAATGGCAGAACCTGCTATAACCCACCCGAGAAAT\n'),
                              fasta.Sequence('seq2', 'ACGTTCTTGGAGATAGTAGTACATCCCAACCAAATAGCTAGCACTGCGTCAGAACGTGGCCACATAGTTTCCCCTGGAGA\nAATCAATGCTACCTGGAGATTGCAATGAATCTGTCTTACTGAACCCGGGACAGGTATCGTATCGTCGAACGAGAACCGGT\nAATGCCTCGACGCTTCTGCT\n')
                              ]


def test_reduce_multiline_sequence(parser, sequence):
    """Parser should take a multiline sequence and return a single line sequence."""
