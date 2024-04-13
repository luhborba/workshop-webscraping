from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# def get_browser():
#     # https://peter.sh/experiments/chromium-command-line-switches/  Site com options do Chrome
#     # https://www.selenium.dev/blog/2023/headless-is-going-away/
#     chrome_options = Options()
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--headless")
#     browser = webdriver.Chrome(options=chrome_options) # "options={--headless}" para não abrir o Navegador Gráfico

#     browser.get("https://globo.com")
#     print(browser.page_source)


# if __name__ == "__main__":
#     get_browser()


class BrowserML:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable--web-security")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--memmory_peassure-off")


        self.browser = webdriver.Chrome(options=self.crome_options)

    def execute_command(self):
        pass

    def transform_df(self):
        pass