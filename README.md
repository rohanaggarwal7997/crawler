# crawler
This is a crawler made in python.
It fucntions basically by crawling the complete site by visiting each link given on the base webpage and searching for the necessary keywords.
It is implemented using MULTI Threading and the concept of taking only the necessary things in the ram at a time.
It maintains three files queue.txt crawled.txt and final.txt for each domain name.
It takes links from queue.txt(waiting list),crawls them and puts them in crawled.txt and puts the desired links in final.txt.
