'''
Expedia Coding Challenge
Author: Rupam Kundu, The Ohio State University
'''
from Quotes import GoodRead
import unicodedata


def Get_quotes(author,numPosts):
    obj = GoodRead()
    obj.set_base_url("https://www.goodreads.com/")
    print("---------Top " + str(numPosts) + " Quotes of " + author +"---------")
    print("-------------------------------------------------")
    print('')
    try:
        #if obj.check_author_type(author):
        #    raise ValueError("Author name should only contain alphabetic characters!")
        if all(x.isdigit() for x in str(author)):
            obj.exitcondition = True
            raise ValueError("Author name should only contain alphabetic characters!")
        obj.set_author_query(str(author))
        if not all(x.isdigit() for x in str(numPosts)):
            obj.exitcondition = True
            raise ValueError("Number of Posts should be an Integer >0")
        if not obj.exitcondition:
            obj.set_numQuotes(int(numPosts))
        if not obj.exitcondition:
            obj.set_query_url()
        if not obj.exitcondition:
            obj.set_quotesquery_name()
        if not obj.exitcondition:
            obj.get_top_quotes(obj.author_query, obj.numQuotes, obj.query_url, obj.filename)

        return obj.filename
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    Get_quotes()

