from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Chrome seçeneklerini başlatma (ekran olmadan çalışma)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("disable-dev-shm-usage")

# Chrome-driver'ı chrome seçenekleriyle güncelleme
driver = webdriver.Chrome(options=chrome_options)

# Uygulamaya bağlanma
APP_IP = os.environ['MASTER_PUBLIC_IP']
url = "http://"+APP_IP.strip()+":30001/"
driver.get(url)

# Bekleme ekleyerek "OWNERS" bağlantısını bulma
owners_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "OWNERS")))
owners_link.click()

# Bekleme ekleyerek "ALL" bağlantısını bulma
all_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "ALL")))
all_link.click()

# Tablonun yüklendiğini doğrulama
verify_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
print("Table loaded")

driver.quit()
