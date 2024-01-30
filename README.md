# Let's Prompt Hosted LLMs
Prompting Hosted LLMs for Free

#### **Instructions for MAC users**
- Download stable chromedriver (from https://googlechromelabs.github.io/chrome-for-testing/) for MAC (that aligns with the currently installed chrome version)
- unzip and copy chromdriver file to the path: `/usr/local/bin/`
- then execute:
    ```
    sudo xattr -d com.apple.quarantine /usr/local/bin/chromedriver
    ```
- install the required python packages: 
  ```
  pip install -r requirements.py
  ```

#### How to Use ###
```
python explore_online_llm_playground.py --url https://labs.perplexity.ai/ --model-name llama2-70b-chat --query """how to start learning generative ai?"""
```

#### ** References **
- https://googlechromelabs.github.io/chrome-for-testing/ 
- https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
- https://copyprogramming.com/howto/python-selenium-copy-text-to-clipboard-a-comprehensive-guide


