"""This module crawls the problems page, scrapes the sample data sets from the problems, and stores them."""

import requests
from bs4 import BeautifulSoup
import csv
import os.path

PROBLEMS = ('DNA RNA REVC FIB GC HAMM IPRB PROT SUBS CONS FIBD GRPH IEV LCSM LIA '
            'MPRT MRNA ORF PERM PRTM REVP SPLC LEXF LGIS LONG PMCH PPER PROB SIGN '
            'SSEQ TRAN TREE CAT CORR INOD KMER KMP LCSQ LEXV MMCH PDST REAR RSTR '
            'SSET ASPC EDIT EVAL MOTZ NWCK SCSP SETO SORT SPEC TRIE CONV CTBL DBRU '
            'EDTA FULL INDC ITWV LREP NKEW RNAS AFRQ CSTR CTEA CUNR GLOB PCOV PRSM '
            'QRT SGRA SUFF CHBP CNTQ EUBT GASM GCON LING LOCA MEND MGAP MREP MULT '
            'PDPL ROOT SEXL SPTD WFMD ALPH ASMQ CSET EBIN FOUN GAFF GREP OAP QRTD '
            'SIMS SMGB KSIM LAFF OSYM RSUB'
).split()

def scrape_problem(html):
    """Scrape the sample data and sample output from a problem page and return them."""
    soup = BeautifulSoup(html, 'lxml')
    results = [tag.string.strip() for tag in soup.find_all('div', class_='codehilite')[-2:]]
    return results


def save_sample(problem, sample, outfile='./test_data/test_data.csv'):
    """Save sample data and sample output in a csv file."""
    header = None
    if not os.path.isfile(outfile):
        header = 'problem data output'.split()

    with open(outfile, 'a', newline='') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerow([problem] + sample)


def main(problems):
    """Scrape the problems pages on rosalind.info for sample datasets and output, then save them."""
    for problem in problems:
        print(problem)
        r = requests.get('http://rosalind.info/problems/%s' % problem)
        results = scrape_problem(r.content)
        save_sample(problem, results)


if __name__ == '__main__':
    main(PROBLEMS)
