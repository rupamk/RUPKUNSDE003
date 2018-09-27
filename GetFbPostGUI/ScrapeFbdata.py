'''
Author: Rupam Kundu, The Ohio State University
'''
import requests
from bs4 import BeautifulSoup
import json
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import re

class Fbpagepostquery(object):
    def __init__(self):
        self.base_url = "https://www.facebook.com/pg/"
        self.page_query = ""
        self.page_link = ""
        self.link_prefix="/posts/?ref=page_internal"
        self.filename =""
        self.exitcondition = False

    def set_linkquery_name(self):
        self.page_link = self.base_url + self.page_query +self.link_prefix

    def set_page_query(self,name):
        try:
            if not name:
                raise ValueError('Provide a proper facebook page name')
            self.page_query = name
        except ValueError as e:
            self.exitcondition = True
            print(e)

    def set_base_url(self,url):
        try:
            if not url:
                raise ValueError('Empty URL')
            self.base_url = str(url)
        except ValueError as e:
            self.exitcondition = True
            print(e)

    def set_postquery_name(self):
        self.filename = "Top_"+self.page_query+"_Facebook_Post.json"

    def post_cleanup(self,string):
        emoji = re.findall(r'[^\w\s,]', string)
        L = list(string)
        content = ''
        for item in L:
            if item not in emoji:
                content += item
        return content

    def get_top_post(self, numPost):
        self.set_linkquery_name()
        try:
            if not all(x.isdigit for x in str(numPost)):
                raise ValueError('Number of Post should be an Integer')
            if numPost==0 or numPost<0:
                raise ValueError('Number of Post should be >=1')
            if numPost>=20:
                raise ValueError('Number of Post should be <20')
            try:
                page = requests.get(self.page_link, timeout=6.0)
                soup = BeautifulSoup(page.content, 'html.parser')
                timestamps = soup.find_all('abbr', {'class': '_5ptz'})
                post = soup.find_all('div', {'class': '_5pbx userContent _3576'})
                data = {}
                index = "Top " + self.page_query + " Facebook Post"
                data[index] = []
                for i in range(min(numPost, len(post))):
                    time = timestamps[i].get_text()
                    content = self.post_cleanup(post[i].get_text())
                    if ("hrs" in timestamps[i].get_text()):
                        time = time + " ago"
                    data[index].append({
                        'Timestamp': time,
                        'Content': content
                    }
                    )
                self.dumpjson(data)
                #self.outputjson(numPost)
            except  (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
                print(e)
        except ValueError as e:
            self.exitcondition = True
            print(e)

    def dumpjson(self,data):
        try:
            path = "./GetFbPostGUI/Data/"
            if data==  {"Top Facebook Post": []}:
                raise ValueError('No post found')
            self.set_postquery_name()
            with open(path+self.filename, 'w') as outfile:
                json.dump(data, outfile)
            print("-------------------------------------------------------")
            print("Check inside" + path)
            print("-------------------------------------------------------")
        except ValueError as e:
            self.exitcondition = True
            print(e)

    def outputjson(self,x):
        try:
            if not x:
                raise ValueError('Empty Filename')
            print('Top ' + str(x) + ' Posts of ' + str(self.page_query))
            print("-------------------------------------------------------")
            path = "./GetFbPostGUI/Data/"
            index = "Top " + self.page_query + " Facebook Post"
            with open(path+self.filename) as json_file:
                data = json.load(json_file)
                for i,p in enumerate(data[index]):
                    print('Post '+ str(i+1) + ': ' + p['Content'])
                    print('')
        except ValueError as e:
            self.exitcondition = True
            print(e)

#if __name__ == "__main__":
#    obj = Fbpagepostquery()
#    '''Get Posts'''
#    obj.set_page_query("expedia")
#    obj.get_top_post(10)

#%-----------------------------------------------------EOF------------------------------------------------------------%/








