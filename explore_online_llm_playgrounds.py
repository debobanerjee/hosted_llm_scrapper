import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import argparse

def get_xpath_model_name(args):
    if args.model_name == 'pplx-7b-online':
        xpath_model_name = '//*[@id="lamma-select"]/option[1]'
    elif args.model_name == 'pplx-70b-online':
        xpath_model_name = '//*[@id="lamma-select"]/option[2]'
    elif args.model_name == 'pplx-7b-chat':
        xpath_model_name = '//*[@id="lamma-select"]/option[3]'
    elif args.model_name == 'pplx-70b-chat':
        xpath_model_name = '//*[@id="lamma-select"]/option[4]'
    elif args.model_name == 'mistral-7b-instruct':
        xpath_model_name = '//*[@id="lamma-select"]/option[5]'
    elif args.model_name == 'codellama-34b-instruct':
        xpath_model_name = '//*[@id="lamma-select"]/option[6]'
    elif args.model_name == 'llama2-70b-chat':
        xpath_model_name = '//*[@id="lamma-select"]/option[7]'
    elif args.model_name ==  'llava-7b-chat':
        xpath_model_name = '//*[@id="lamma-select"]/option[8]'
    elif args.model_name ==  'mixtral-8x7b-instruct':
        xpath_model_name = '//*[@id="lamma-select"]/option[9]'
    elif args.model_name ==  'mistral-medium':
        xpath_model_name = '//*[@id="lamma-select"]/option[10]'
    else:
        raise NotImplementedError
    return xpath_model_name

def main(args, driver):
    driver.get(args.url)
    model_selection_dropdown = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[2]/div[1]/div/div[2]/div/div/div/div')
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
    
    copy_icon = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div/div[1]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button/div[2]/div')
    copy_icon.click()
    time.sleep(2)
    
    response = pyperclip.paste()
    time.sleep(2)

    print(f"Chosen Model: {args.model_name}")
    print(f"Input Query: {args.query}")
    print(f"Response: {response}")

    driver.close()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name", type=str, default="llama2-70b-chat", choices=["pplx-7b-online", 
                                                                                 "pplx-70b-online", "pplx-7b-chat", 
                                                                                 "pplx-70b-chat","mistral-7b-instruct","codellama-34b-instruct", "llama2-70b-chat", 
                                                                                 "llava-7b-chat", "mixtral-8x7b-instruct", "mistral-medium"])
    parser.add_argument("--url", type=str, default="https://labs.perplexity.ai/")
    parser.add_argument("--query", type=str, default="how to start learning generative ai?")
    args = parser.parse_args()
    main(args, driver)


