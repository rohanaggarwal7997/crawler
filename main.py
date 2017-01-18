import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

PROJECT_NAME='iitg'
HOMEPAGE=input('Give the homepage of the website or the site that you want to crawl')
n=input('Give the number of words that you want to search')
print('Enter each word with a enter')
wlist = set()
for i in range(int(n)):
    k = input()
    wlist.add(k)
DOMAIN_NAME=get_domain_name(HOMEPAGE)
QUEUE_FILE=PROJECT_NAME+'/queue.txt'
CRAWLED_FILE=PROJECT_NAME+'/crawled.txt'
NUMBER_OF_THREADS=4
queue=Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME,wlist)


#contine to crawl the queue list

def crawl():
    queued_links=file_to_set(QUEUE_FILE)
    if len(queued_links)>0:
        print(str(len(queued_links))+'Links in the queue')
        create_jobs()

#each link in the queue is a job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#Create worker threads(will die when main exits)

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)
        t.daemon=True #Dies at end
        t.start()


#Do the next job in the queue
def work():
    while True:
        url=queue.get()
        Spider.crawl_page(threading.current_thread().name,url,wlist)
        queue.task_done()


create_workers()
crawl()