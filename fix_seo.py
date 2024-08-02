from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, choice

# Set up the WebDriver (Chrome in this case)
driver = webdriver.Chrome()  # Make sure 'chromedriver' is in your PATH

try:
    # Open Google
    driver.get("https://www.google.com")

    # Locate the search box
    search_box = driver.find_element(By.NAME, "q")

    # Type the query, simulating real user keystrokes
    queries = [
      "query1",
      "query2",
      "query3",
      "query4"
    ]
    query = random.choice(queries)
    for char in query:
        search_box.send_keys(char)
        time.sleep(0.1)  # Add a slight delay between keystrokes

    # Press Enter to search
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#search")))

    # Find all search results
    search_results = driver.find_elements(By.CSS_SELECTOR, "div.yuRUbf > a")

    # Check for matching domain and click the first result found
    for result in search_results:
        href = result.get_attribute("href")
        if "query.domain.org" in href:
            result.click()
            break

    # Optional: wait for the new page to load and interact further if needed
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()
