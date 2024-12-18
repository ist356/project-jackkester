from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

# Initialize the Chrome WebDriver
def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-logging")  # Suppress unnecessary logging
    options.add_argument("--log-level=3")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Scroll the page to load dynamic content
def scroll_page(driver):
    scroll_pause = 3
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Function to scrape UFC Rankings Page
def scrape_rankings(driver):
    url = "https://www.ufc.com/rankings"
    driver.get(url)

    # Scroll to load all content
    print("Scrolling through the page...")
    scroll_page(driver)
    time.sleep(5)  # Allow additional wait for JavaScript content

    # Wait for rankings container to load
    print("Waiting for rankings content to load...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.view-grouping"))
    )

    # Extract the page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    rankings = []

    # Find all sections containing rankings
    ranking_sections = soup.select("div.view-grouping")
    for section in ranking_sections:
        # Extract weight class name
        weight_class = section.select_one("div.view-grouping-header").get_text(strip=True)
        print(f"Found Weight Class: {weight_class}")

        # Extract all fighter names in the section
        fighters = section.select("td.views-field-title")
        for fighter in fighters:
            fighter_name = fighter.get_text(strip=True)
            print(f" - Fighter: {fighter_name}")
            rankings.append({"weight_class": weight_class, "fighter_name": fighter_name})

    return rankings





# Main function to scrape all fighters
def main():
    driver = init_driver()
    try:
        print("Scraping UFC Rankings...")
        rankings = scrape_rankings(driver)
        print("\nScraping Rankings Done.\n")
        
        keys = ['Name']
        men_pound_for_pound = pd.DataFrame(columns=keys)
        men_flyweight = pd.DataFrame(columns=keys)
        men_bantamweight = pd.DataFrame(columns=keys)
        men_featherweight = pd.DataFrame(columns=keys)
        men_lightweight = pd.DataFrame(columns=keys)
        men_welterweight = pd.DataFrame(columns=keys)
        men_middleweight = pd.DataFrame(columns=keys)
        men_light_heavyweight = pd.DataFrame(columns=keys)
        men_heavyweight = pd.DataFrame(columns=keys)
        women_pound_for_pound = pd.DataFrame(columns=keys)
        women_strawweight = pd.DataFrame(columns=keys)
        women_flyweight = pd.DataFrame(columns=keys)
        women_bantamweight = pd.DataFrame(columns=keys)

    
        # Print the scraped rankings
        for fighter in rankings:
            
            new_row = {'Name':fighter['fighter_name']}
            if fighter['weight_class'] == "Men's Pound-for-PoundTop Rank":              
                men_pound_for_pound = pd.concat([men_pound_for_pound, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Flyweight": 
                men_flyweight = pd.concat([men_flyweight, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Bantamweight":
                men_bantamweight = pd.concat([men_bantamweight, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Featherweight":
                men_featherweight = pd.concat([men_featherweight, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Lightweight":
                men_lightweight = pd.concat([men_lightweight, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Welterweight":
                men_welterweight = pd.concat([men_welterweight, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Middleweight":
                men_middleweight = pd.concat([men_middleweight, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Light Heavyweight":
                men_light_heavyweight = pd.concat([men_light_heavyweight, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Heavyweight":
                men_heavyweight = pd.concat([men_heavyweight, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Women's Pound-for-PoundTop Rank":
                women_pound_for_pound = pd.concat([women_pound_for_pound, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Women's Strawweight":
                women_strawweight = pd.concat([women_strawweight, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Women's Flyweight":
                women_flyweight = pd.concat([women_flyweight, pd.DataFrame([new_row])], ignore_index=True)
            elif fighter['weight_class'] == "Women's Bantamweight":
                women_bantamweight = pd.concat([women_bantamweight, pd.DataFrame([new_row])], ignore_index=True)


            #print(f"Weight Class: {fighter['weight_class']}, Fighter: {fighter['fighter_name']}")
            men_pound_for_pound.to_csv("cache/men_pound_for_pound.csv", index=False)
            men_flyweight.to_csv("cache/men_flyweight.csv", index=False)
            men_bantamweight.to_csv("cache/men_bantamweight.csv", index=False)
            men_featherweight.to_csv("cache/men_featherweight.csv", index=False)
            men_lightweight.to_csv("cache/men_lightweight.csv", index=False)
            men_welterweight.to_csv("cache/men_welterweight.csv", index=False)
            men_middleweight.to_csv("cache/men_middleweight.csv", index=False)
            men_light_heavyweight.to_csv("cache/men_light_heavyweight.csv", index=False)
            men_heavyweight.to_csv("cache/men_heavyweight.csv", index=False)
            women_pound_for_pound.to_csv("cache/women_pound_for_pound.csv", index=False)
            women_strawweight.to_csv("cache/women_strawweight.csv", index=False)
            women_flyweight.to_csv("cache/womens_flyweight.csv", index=False)
            women_bantamweight.to_csv("cache/womens_bantamweight.csv", index=False)
        
    finally:
        driver.quit()
        print("\nScraping Completed Successfully.")

    
if __name__ == "__main__":
    main()