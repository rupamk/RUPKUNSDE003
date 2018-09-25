'''
Author: Rupam Kundu, The Ohio State University
'''
from ScrapeFbdata import Fbpagepostquery

def Get_posts(page,numPosts):
    obj = Fbpagepostquery()
    print("---------Top " + str(numPosts) + " Posts of " + page +" Facebook Page---------")
    print("-------------------------------------------------")
    print('')
    obj.set_page_query(page)
    if not all(x.isdigit() for x in str(numPosts)):
        obj.exitcondition = True
        raise ValueError("Number of Posts should be an Integer >0")
    obj.get_top_post(int(numPosts))

if __name__ == '__main__':
    Get_posts()

