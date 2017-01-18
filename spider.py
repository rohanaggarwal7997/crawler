from urllib.request import urlopen
import requests
from link_finder import LinkFinder
from general import *
from domain import *


class Spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()
    wlist=set()

    def __init__(self, project_name, base_url, domain_name,wlist1):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.final_file=Spider.project_name+'/final.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url,wlist1)

    # Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name,Spider.base_url)
        Spider.queue=file_to_set(Spider.queue_file)
        Spider.crawled=file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name,page_url,wlist):
        if page_url not in Spider.crawled:
            print(thread_name+'now crawling'+page_url)
            print('Queue '+str(len(Spider.queue))+' Crawled' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            text= requests.get(page_url).text.lower()
            print('Rohan')
           # print(text)
            print('Rohan')
            check=True
            for word in wlist:
                if(word not in text):check=False
            if check:
                append_to_file(Spider.final_file,page_url+'\n')
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_link(page_url):
        #one way
        #requests.get('https://docs.python.org/2/library/htmlparser.html').text

        html_string=''
        try:
            response=urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes=response.read()
                html_string=html_bytes.decode("utf-8")
            finder=LinkFinder(Spider.base_url,page_url)
            finder.feed(html_string)
        except:
            print('Cant crawl set')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name != get_domain_name(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue,Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
