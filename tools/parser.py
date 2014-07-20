from bs4 import BeautifulSoup
import urllib2


browser_dict = {
    'opera': 'Opera/9.80 (X11; Linux x86_64) Presto/2.12.388 Version/12.16',
    'chromium': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
    'firefox': 'Mozilla/5.0 (X11; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0',
}


class Parser():

    def get_html(self, url):
        request = urllib2.Request(url)
        request.add_header('User-Agent', browser_dict['chromium'])
        try:
            response = urllib2.urlopen(request)
            if response.code == 200:
                html = response.read()
                return BeautifulSoup(html)#, 'lxml')
            else:
                return None
        except:
            return None

    def get_table(self, url):
        page = self.get_html(url)
        if page:
            return page.find('table', { "class" : "price-list" })
        else:
            return None
