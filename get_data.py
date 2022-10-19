from bs4 import BeautifulSoup
import requests


class GetData:

    def __init__(self):
        request_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "_ga=GA1.2.475502901.1665258693",
            "Host": "myhttpheader.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44"
        }
        self.response = requests.get(
            "https://nigeriapropertycentre.com/for-rent/houses/lagos/ajah?bedrooms=4&maxprice=5000000&selectedLoc=1&q=for-rent+houses+lagos+ajah+4+bedrooms+maxprice+5000000")
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def get_addresses(self):
        all_addresses = self.soup.find_all("address")
        return [address.get_text() for address in all_addresses]

    def get_prices(self):
        all_prices = self.soup.select("span.pull-sm-left")
        return [price.get_text() for price in all_prices]

    def get_links(self):
        all_links = self.soup.select(".wp-block-content a")
        return [link['href'] for link in all_links]
