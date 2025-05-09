# Job Scraper – Which fetches custom Jobs from Job portals in ethioipa that permit this on their robots.txt.  
A robots.txt file is a text file placed in the root directory of a website that instructs web crawlers  
(like Googlebot) which parts of the site they are allowed or disallowed from accessing.

This is a Playwright-based job scraper that fetches job titles from Job portals in ethiopia. 
It uses Python and Playwright to dynamically interact with the site and extract job listings.

## Features

- Uses Playwright to control Chromium browser  
- Simulates scroll to load more job listings  
- Scrapes job titles from the page  
- Prints the first 10 job titles  
- Supports headless and non-headless modes  

## Prerequisites

- Python 3.7+  
- Git (to clone the repository)  

## Setup

```bash
git clone https://github.com/Beki-Abebe/job-scraper.git
cd job-scraper

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install playwright rich
playwright install

python main.py
