from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import numpy as np

# ===== SETUP =====
URL = "https://www.alibaba.com/search/page?spm=a2700.prosearch.the-new-header_fy23_pc_search_bar.keydown__Enter&SearchScene=proSearch&SearchText=mobile+phones&pro=true&from=pcHomeConten"
CHROME_PATH = r"C:\Users\HP\Downloads\chrome drivers\chromedriver-win64\chromedriver.exe"

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# act like real browser (IMPORTANT)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# disable images (faster)
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(CHROME_PATH), options=options)
wait = WebDriverWait(driver, 20)

driver.get(URL)

# ===== CSV SETUP =====
with open("alibaba_mobiles.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "product_name", "price", "product_sold",
        "reviews", "reviews_rating", "image_link", "product_link"
    ])

    # ===== SCRAPING =====
    for page in range(1, 6):
        print(f"Scraping Page {page}")

        # wait for page load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)

        # scroll for lazy loading
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        # ===== DETECT LAYOUT =====
        # use document.querySelectorAll(div.fy26-product-card)
        # to check your selector will work or not
        products = driver.find_elements(By.CSS_SELECTOR, "div.fy26-product-card")

        if not products:
            products = driver.find_elements(By.XPATH, '//div[contains(@class,"fy26-product-card")]')

        if not products:
            print("Still no products — saving debug...")
            driver.save_screenshot("debug.png")
            print(driver.page_source[:1000])  # preview HTML
            break

        # ===== EXTRACT DATA =====
        for product in products:
            try:
                # product_name
                try:
                    product_name = product.find_element(By.CSS_SELECTOR, "h2 span").text
                    if not product_name:
                        product_name = product.find_element(By.XPATH, ".//h2//span").text
                    # if not product_name:
                    #     product_name = product.find_element(By.TAG_NAME, "h2").text
                except:
                    product_name = np.nan


                # price:
                try:
                    price = product.find_element(By.XPATH, './/div[contains(@class,"product-price-price-main")]').text
                except:
                    price = np.nan

                # sold: 
                try:
                    sold = product.find_element(By.XPATH, './/div[contains(@class, "searchx-sold-order")]').text
                    if 'sold' in sold.lower():
                        product_sold = sold 
                    else: 
                        product_sold = np.nan 
                except:
                    product_sold = np.nan

                # reviews
                try:
                    raw_reviews = product.find_element(By.XPATH, './/span[contains(text(),"()")]').text
                    reviews = raw_reviews.replace("(","").replace(")","").strip()

                except:
                    reviews = np.nan

                # reviews_rating:
                try:
                    reviews_rating = product.find_element(By.XPATH, './/span[contains(@class, "searchx-review")]').text

                except:
                    reviews = np.nan

                # image
                try:
                    img = product.find_element(By.XPATH, './/img[contains(@class,"searchx-product-e-slider__img")]') 
                    image_link = img.get_attribute('src') 
                    if not image_link:
                        img = product.find_element(By.CSS_SELECTOR, "img.searchx-product-e-slider__img")
                        image_link = img.get_attribute("src")
                except:
                    image_link = np.nan

                # link
                try:
                    product_link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
                    if not product_link:
                        product_link = product.find_element(By.XPATH, ".//a//href").text
                        product_link.split('?')[0].strip()

                except:
                    product_link = np.nan

                writer.writerow([product_name, price, product_sold, reviews, reviews_rating, image_link, product_link])

            except Exception as e:
                print("Skipped:", e)

        # ===== NEXT PAGE =====
        try:
            next_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span.pagination-item"))
            )
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(3)

        except:
            print("No more pages.")
            break

driver.quit()
print(" File saved: alibaba_mobiles.csv")