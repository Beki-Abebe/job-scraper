from playwright.sync_api import sync_playwright
from rich import print

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(user_agent="Mozilla/5.0")
    page = context.new_page()

    # Open the website
    page.goto("https://afriworket.com/jobs", timeout=60000)

    # Wait for the search input field to appear
    search_input = page.wait_for_selector('input[placeholder="Search for job"]', timeout=15000)

    # Enter "developer" into the search bar and press Enter
    search_input.fill("developer")
    search_input.press("Enter")

    # Wait for the results to load
    page.wait_for_selector('div[class*="group w-full cursor-pointer space-y-4 p-4 duration-300 hover:bg-gray-100 md:px-8 md:py-6 lg:space-y-6"]', timeout=15000)

    # Scroll to load more results (simulate user scroll)
    page.mouse.wheel(0, 2000)
    page.wait_for_timeout(3000)

    # Scrape the entire result blocks
    job_blocks = page.locator('div[class*="group w-full cursor-pointer space-y-4 p-4 duration-300 hover:bg-gray-100 md:px-8 md:py-6 lg:space-y-6"]').all_text_contents()

    print(f"[bold green]Found {len(job_blocks)} job listings[/bold green]")
    for idx, block in enumerate(job_blocks, start=1):
        print(f"\n[bold yellow]Job {idx}:[/bold yellow]\n{block.strip()}")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
