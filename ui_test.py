# Selenium ile headless UI testi.
# example.com sayfasinin dogru yuklendigini dogrular.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_example_com_loads_correctly():
    # example.com'a git ve sayfa basliginin dogru geldigini dogrula.
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://example.com")
        title = driver.title
        print(f"[UI TEST] Sayfa basligi: {title}")
        assert "Example Domain" in title, f"Beklenen baslik bulunamadi: {title}"
        print("[UI TEST] Test basariyla gecti.")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_example_com_loads_correctly()