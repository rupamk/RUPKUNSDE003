'''
Author: Rupam Kundu, The Ohio State University
'''
import mechanize
import requests
from bs4 import BeautifulSoup
import json
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import unicodedata

class GoodRead():
    def __init__(self):
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.base_url = ""
        self.email = ""
        self.password = ""
        self.sign_in_url = ""
        self.redirect_url = ""
        self.auth_flag = False
        self.author_query = ""
        self.query_url = ""
        self.filename = ""
        self.jsondata = {}
        self.numQuotes = 0
        self.exitcondition = False

    # functions
    def set_author_query(self,author):
        try:
            if not author:
                raise ValueError('No author name provided')
            if self.hasNumbers(str(author)):
                raise ValueError('Name cannot contain Numbers! Enter proper author name !')
            temp = []
            for item in author.split(' '):
                 temp.append(item.lower().capitalize())
            self.author_query = ' '.join(temp)
        except ValueError as e:
            self.exitcondition = True
            print(e)
            return e

    def hasNumbers(self,inputString):
        return any(char.isdigit() for char in inputString)

    def set_quotesquery_name(self):
        try:
            if(len(self.author_query)>0):
                temp = self.author_query.split(' ')
                s=''
                for item in temp:
                    s = s + str(item) + '_'
                self.filename = s[:-1] + '_top_quotes.json'
            else:
                raise ValueError('Author Name not provided')
        except ValueError as e:
            self.exitcondition = True
            print(e)
            return e

    def set_query_url(self):
        temp = self.author_query.split(' ')
        s = ''
        for item in temp:
            s= s+str(item)+'+'
        self.query_url = self.base_url + "quotes/search?"+"&q="+s[:-1]+"&commit=Search"

    def set_base_url(self,url):
        try:
            if not url:
                raise ValueError('Empty URL provided')
            self.base_url = str(url)
            self.redirect_url = self.base_url
            self.sign_in_url = self.base_url +"user/sign_in"
        except ValueError as e:
            self.exitcondition = True
            print(e)
            return e

    def set_email(self,username):
        try:
            if not username:
                raise ValueError('Empty email! please provide a proper email!')
            self.email = str(username)
            return self.email
        except ValueError as e:
            self.exitcondition = True
            print(e)
            return e

    def set_password(self,password):
        try:
            if not password:
                raise ValueError('Empty password! please provide a proper password!')
            self.password = str(password)
            return self.password
        except ValueError as e:
            self.exitcondition = True
            print(e)
            return e

    def set_credential(self):
        # 3 times login attempts
        # count = 2
        # while not self.authenticate(self.email,self.password,self.sign_in_url,self.redirect_url) and count > 0:
        #     print("-----------------Attempt " + str(3-count) + "-------------------------")
        #     print('')
        #     print('Please verify Email/Password!!!!!!!!!!!!')
        #     print('')
        #     self.set_email(raw_input('Please Enter your GoodReads.com email address:'))
        #     print('')
        #     self.set_password(raw_input('Please Enter your GoodReads.com password:'))
        #     print('')
        #     count = count - 1
        # if count > 0:
        #     print("-------------------------------------------------")
        #     print("----------Authentication Successful--------------")
        #     print("-------------------------------------------------")
        #     self.auth_flag = True
        # else:
        #     print("-------------------------------------------------")
        #     print("-----Authentication Failed. Try Again Later------")
        #     print("-------------------------------------------------")
        if self.authenticate(self.email,self.password,self.sign_in_url,self.redirect_url):
            self.auth_flag = True
            print('Authenticated!! You are now logged in!')
            return True
        print('Authentication Failed')
        return False

    def authenticate(self,email,password,sign_in_url,redirect_url):
        try:
            if not password or not email:
                raise ValueError('Empty email/password! Please provide proper email/password')
            try:
                self.br.open(sign_in_url)
                self.br.select_form(name="sign_in")
                self.br["user[email]"] =   email
                self.br["user[password]"] = password
                self.br.submit()
                if (self.br.geturl()) == redirect_url:
                    return True
                else:
                    return False
            except (mechanize.HTTPError,mechanize.URLError) as e:
                print('Check Connection')
        except ValueError as e:
            self.exitcondition = True
            return e

    def clean_quotes(self,s):
        start = "\n      \xe2\x80\x9c"
        end = ".\xe2\x80\x9d\n    \xe2\x80\x95\n  \n    "+self.author_query
        return s.split(start)[1].split(end)[0]

    def set_numQuotes(self,num):
        try:
            if num==0 or num<0:
                raise ValueError('Number of quotes should be >=1')
            if type(num) is not int:
                raise ValueError('Num of Quotes should be an Integer Value')
            if not all(x.isdigit() for x in str(num)):
                raise ValueError('Num of Quotes should be an Integer Value')
            self.numQuotes = num
        except ValueError as e:
            self.exitcondition = True
            print(e)
            return e

    def get_top_quotes(self,author, numQuotes,query_url,filename,isPrint = False):
        try:
            if not query_url:
                raise ValueError('Please provide a Link properly')
            try:
                page = requests.get(query_url, timeout=6.0)
            except  (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError) as e:
                self.exitcondition = True
                print(e)
                return e
            if type(numQuotes) is not int:
                  raise ValueError('Num of Quotes should be an Integer Value')
            self.numQuotes = int(numQuotes)
            if not author:
                raise ValueError('Please provide an author name properly.')
            soup = BeautifulSoup(page.content, 'html.parser')
            post = soup.find_all('div', {'class': 'quoteText'})
            for script in soup.find_all('script'):
                script.extract()
            if len(post)==0:
                raise ValueError('No quotes Found')
            data = {}
            index = "Quotes By:" + author
            data[index] = []
            self.numQuotes = min(self.numQuotes, len(post))
            i = 0
            count = self.numQuotes
            while count > 0 and i < len(post):
                if (author == str(post[i].find("span", class_="authorOrTitle").text).rstrip().lstrip()):
                    val =post[i].get_text()
                    content = self.clean_quotes(val.encode("utf-8"))
                    data[index].append({
                        'Content': content,
                        'Author': author
                    }
                    )
                    count -= 1
                i += 1
            if len(data)==0:
                raise ValueError('No quotes Found')
            self.jsondata = data
            self.dumpjson(self.jsondata,filename)
            if isPrint:
                self.outputjson(author,self.numQuotes)
            return data
        except ValueError as e:
            self.exitcondition = True
            print(e)
            return e

    def dumpjson(self,data,filename):
        path = "./TopQuotesGUI/Data/"
        with open(path+filename, 'w') as outfile:
            json.dump(data, outfile)
        print("-------------------------------------------------------")
        print("Check " + self.filename + " in ./TopQuotes/Data/ ")
        print("-------------------------------------------------------")

    def outputjson(self,author,x):
        print('')
        print('Top ' + str(x) + ' Quotes of '+ str(self.author_query))
        print('********************************************************')
        index = "Quotes By:" + author
        path = "./TopQuotesGUI/Data/"
        with open(path+self.filename) as json_file:
            data = json.load(json_file)
            try:
                if not data[index]:
                    print('Empty File')
                for i,p in enumerate(data[index]):
                    print('Quote '+ str(i+1)+':' + p['Content'])
                    print('')
                    print('********************************************************')
            except ValueError as e:
                print(e)
                return(e)

    def read_file_data(self,path,filename):
        with open(path+filename) as data_file:
            json_data = json.load(data_file)
        return json_data

if __name__ == "__main__":
    obj = GoodRead()
    obj.set_base_url("https://www.goodreads.com/")
    print("-------------------------------------------------")
    print("---------Authentication to Goodreads.com---------")
    print("-------------------------------------------------")
    # print('')
    # print("-----------------Attempt 0-------------------------")
    # print('')
    obj.set_email(raw_input('Please Enter your GoodReads.com email address:'))
    print('')
    obj.set_password(raw_input('Please Enter your GoodReads.com password:'))
    print('')
    if not obj.exitcondition:
        obj.set_credential()
    '''Get Quotes'''
    if(obj.auth_flag):
        obj.set_author_query("Mark Twain")
        if not obj.exitcondition:
            obj.set_numQuotes(10)
        if not obj.exitcondition:
            obj.set_query_url()
        if not obj.exitcondition:
            obj.set_quotesquery_name()
        if not obj.exitcondition:
            obj.get_top_quotes(obj.author_query,obj.numQuotes,obj.query_url,obj.filename,True)
        if not obj.exitcondition:
            obj.dumpjson(obj.jsondata, obj.filename)
#%-----------------------------------------------------EOF------------------------------------------------------------%/








