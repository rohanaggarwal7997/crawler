from html.parser import HTMLParser
from urllib import parse
import requests

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass

#finder=LinkFinder('http://www.iitg.ernet.in','http://www.iitg.ernet.in')
#finder.feed(requests.get('http://www.iitg.ernet.in').text)
#print(finder.page_links())

#finder=LinkFinder('http://www.iitg.ernet.in','http://www.iitg.ernet.in/eee/majhi.html#majhiStart')
#finder.feed(requests.get('http://www.iitg.ernet.in/eee/majhi.html#majhiStart').text)