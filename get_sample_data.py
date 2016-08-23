"""This module crawls the problems page, scrapes the sample data sets from the problems, and stores them."""

import requests
from bs4 import BeautifulSoup

def scrape_listview(html):
    """Scrape the problems list-view for links to the problem pages."""
    urls = []
    soup = BeautifulSoup(html)
    problem_list = soup.find_all('table', class_='problem-list')
    for link in problem_list.find_all('a'):
        urls.append(link['href'])

    return urls

def scrape_problem(html):
    """"""

def main():
    """Scrape the problems pages on rosalind.info for sameple datasets and output."""
    # get problems list-view page
     listview_page = requests.get('http://rosalind.info/problems/list-view/')
     # parse it for links to problems
     problem_urls = scrape_listview(listview_page.content)
     # scrape problems for sample datasets and sample output
     for url in problem_urls:
         problem_page = requests.get(url)
         scrape_problem(problem_page.content)


if __name__ == '__main__':
    main()
