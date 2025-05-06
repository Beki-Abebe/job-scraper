from playwright.sync_api import sync_playwright
from rich import print

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(user_agent="Mozilla/5.0")
    page = context.new_page()

    page.goto("https://afriworket.com/jobs", timeout=60000)

    # Wait for at least one job header to load
    page.wait_for_selector('h3[class*="font-semibold"]', timeout=15000)

    # Scroll to load more (simulate user scroll)
    page.mouse.wheel(0, 2000)
    page.wait_for_timeout(3000)

    # Locate all job titles
    job_titles = page.locator('h3[class*="font-semibold"]').all_text_contents()

    print(f"[bold green]Found {len(job_titles)} job titles[/bold green]")
    for title in job_titles[:10]:  # Limit output to first 10
        print(f"- {title.strip().lower()}")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
