import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import argparse
import os
from dotenv import load_dotenv
load_dotenv()

def get_xpath_model_name(args):
    if args.model_name == os.environ.get('MODEL1'):
        xpath_model_name = os.environ.get('XPATH_MODEL1')
    elif args.model_name == os.environ.get('MODEL2'):
        xpath_model_name = os.environ.get('XPATH_MODEL2')
    elif args.model_name == os.environ.get('MODEL3'):
        xpath_model_name = os.environ.get('XPATH_MODEL3')
    elif args.model_name == os.environ.get('MODEL4'):
        xpath_model_name = os.environ.get('XPATH_MODEL4')
    elif args.model_name == os.environ.get('MODEL5'):
        xpath_model_name = os.environ.get('XPATH_MODEL5')
    elif args.model_name == os.environ.get('MODEL6'):
        xpath_model_name = os.environ.get('XPATH_MODEL6')
    elif args.model_name == os.environ.get('MODEL7'):
        xpath_model_name = os.environ.get('XPATH_MODEL7')
    elif args.model_name ==  os.environ.get('MODEL8'):
        xpath_model_name = os.environ.get('XPATH_MODEL8')
    elif args.model_name ==  os.environ.get('MODEL9'):
        xpath_model_name = os.environ.get('XPATH_MODEL9')
    elif args.model_name ==  os.environ.get('MODEL10'):
        xpath_model_name = os.environ.get('XPATH_MODEL10')
    else:
        raise NotImplementedError
    return xpath_model_name

def main(args, driver):
    

    driver.get(args.url)

    model_selection_dropdown = driver.find_element(By.XPATH, os.environ.get('MODEL_SELECTION_XPATH'))
    
    model_selection_dropdown.click()

    xpath_model_name = get_xpath_model_name(args)
    
    chosen_model = driver.find_element(By.XPATH, xpath_model_name)
    chosen_model.click()
    time.sleep(2)

    search_bar = driver.find_element(By.TAG_NAME, "textarea")
    search_bar.clear()

    search_bar.send_keys(args.query)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(20) # increase or reduce the sleep time based on requirements
    
    copy_icon = driver.find_element(By.XPATH, os.environ.get('COPY_ICON_XPATH'))
    copy_icon.click()
    time.sleep(2)
    
    response = pyperclip.paste()
    time.sleep(2)

    print(f"Chosen Model: {args.model_name}")
    print(f"Input Query: {args.query}")
    print(f"Response: {response}")

    driver.close()

if __name__ == "__main__":
    # driver = webdriver.Chrome()
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", type=str, default=os.environ.get('MODEL7'))
    parser.add_argument("--url", type=str, default=os.environ.get('HOSTED_URL'))
    parser.add_argument("--query", type=str, default="how to start learning generative ai?")
    args = parser.parse_args()
    main(args, driver)


