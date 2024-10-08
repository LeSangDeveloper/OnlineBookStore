from selenium import webdriver
import unittest
class TestAdmin420(unittest.TestCase):
    def test_TC420(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("12345!!")
        el = driver.find_element_by_name('author')
        el.send_keys("Khang Nguyen")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC421(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("yourlife!!!")
        el = driver.find_element_by_name('author')
        el.send_keys("Khang Nguyen")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC422(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("YOURLIFE!!")
        el = driver.find_element_by_name('author')
        el.send_keys("Khang Nguyen")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC423(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("Your Life!!")
        el = driver.find_element_by_name('author')
        el.send_keys("Khang Nguyen")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC424(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("Your Life")
        el = driver.find_element_by_name('author')
        el.send_keys(" ")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC425(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("Your Life")
        el = driver.find_element_by_name('author')
        el.send_keys("Khang  Nguyen")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC426(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("Your Life")
        el = driver.find_element_by_name('author')
        el.send_keys("KhangNguyen ")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC427(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("Your Life")
        el = driver.find_element_by_name('author')
        el.send_keys("!!@@##")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC428(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("Your Life")
        el = driver.find_element_by_name('author')
        el.send_keys("12345")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
    def test_TC429(self):
        driver = webdriver.Chrome("C:/chromedriver.exe")
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/user/signin")

        el = driver.find_element_by_name('email')
        el.send_keys("admin@lsbookstore.com")
        el = driver.find_element_by_name('password')
        el.send_keys("Sa!12345")
        el = driver.find_element_by_name('signin').click()
        
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/index")
        driver.find_element_by_css_selector("body > div > div > div:nth-child(1) > a").click()
        driver.get("http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        el = driver.find_element_by_name('title')
        el.send_keys("Your Life")
        el = driver.find_element_by_name('author')
        el.send_keys("khangnguyen")
        el = driver.find_element_by_name('price')
        el.send_keys("20")
        el = driver.find_element_by_name('in-stock')
        el.send_keys("5")
        el = driver.find_element_by_name('description')
        el.send_keys("Best for your Life")
        driver.find_element_by_css_selector("body > div > form > button").click()
        result = driver.current_url
        self.assertEqual(result, "http://localhost/TH71-WebBanHangTrucTuyen/admin/addProduct")
        driver.quit()
if __name__ == '__main__':
 suite = unittest.TestLoader().loadTestsFromTestCase(TestAdmin420)
 unittest.TextTestRunner(verbosity=2).run(suite)
