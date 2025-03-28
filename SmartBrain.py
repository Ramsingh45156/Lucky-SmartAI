import time
import os
import pathlib
from Text_to_speek import speak
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

LAST_RESPONSE_FILE = "last_response.txt"

def close_old_drivers():
    """पुराने ChromeDriver प्रोसेस को बंद करता है।"""
    os.system("taskkill /f /im chromedriver.exe >nul 2>&1")

def configure_driver():
    """Chrome WebDriver को कॉन्फ़िगर करता है।"""
    close_old_drivers()

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # chrome_options.add_argument("--headless")  # Agar chahiye to enable karo

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver

def login(driver):
    """वेबसाइट में लॉगिन करता है।"""
    driver.get("https://pi.ai/")
    
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[4]/div/div/textarea"))
        )
        print("✅ Already logged in.")
    except:
        try:
            for _ in range(3):
                next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[2]/div/button'))
                )
                next_button.click()
        except Exception as e:
            print(f"❌ Login failed: {e}")

def save_response(response):
    """Response ko file me save karta hai aur return karta hai."""
    with open(LAST_RESPONSE_FILE, "w", encoding="utf-8") as file:
        file.write(response)

def get_last_response():
    """Agar last response file exist karti hai, to uska content return karo."""
    if os.path.exists(LAST_RESPONSE_FILE):
        with open(LAST_RESPONSE_FILE, "r", encoding="utf-8") as file:
            return file.read().strip()
    return None

def chat(driver, message):
    """चैट बॉट को मैसेज भेजता है और रिस्पॉन्स प्राप्त करता है।"""
    try:
        chat_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[4]/div/div/textarea"))
        )
        chat_input.clear()
        chat_input.send_keys(message)

        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[4]/div/button"))
        )
        send_button.click()

        time.sleep(3)

        result_area = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='__next']/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div"))
        )
        result_text = result_area.text.strip()

        # Response save karo
        save_response(result_text)

        speak(f"💬 ChatBot Response: {result_text}")

    except Exception as e:
        print(f"❌ Chat failed: {e}")

def SmartBrain():
    """मुख्य प्रोग्राम जिसे यूज़र चला सकता है।"""
    driver = configure_driver()
    login(driver)

    while True:
        message = input("📩 Enter your message (or press Enter to repeat last response): ").strip()

        if message.lower() == "exit":
            print("👋 Exiting chat...")
            driver.quit()
            break

        if message == "":
            last_response = get_last_response()
            if last_response:
                print(f"🔄 Last Response: {last_response}")
                speak(f"🔄 Last Response: {last_response}")
            else:
                print("⚠️ No previous response found!")
            continue  # Loop wapas start hoga

        chat(driver, message)

if __name__ == "__main__":
    SmartBrain()
