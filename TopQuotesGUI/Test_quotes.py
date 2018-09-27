'''
Author: Rupam Kundu, The Ohio State University
'''
import unittest
from Quotes import GoodRead

class TestMethods(unittest.TestCase):
    #**************************************Test 2.1*****************************************************
    #@unittest.skip('')
    def test_email(self):
        obj = GoodRead()
        self.assertEqual(obj.set_email("rupam2422@gmail.com"), "rupam2422@gmail.com")

    #@unittest.skip('')
    def test_password(self):
        obj = GoodRead()
        self.assertEqual(obj.set_password("rupam.K@19"), "rupam.K@19")

    #@unittest.skip('')
    def test_empty_password(self):
        obj = GoodRead()
        self.assertRaises(obj.set_password(""))

    #@unittest.skip('')
    def test_empty_email(self):
        obj = GoodRead()
        self.assertRaises(obj.set_email(""))

    #**************************************Test 2.2*****************************************************
    #@unittest.skip('')
#    def test_correct_email_password(self):
#        obj = GoodRead()
#        obj.set_email("rupam2422@gmail.com")
#        obj.set_password("******") // hidden for security reasons
#        obj.set_base_url("https://www.goodreads.com/")
#        self.assertEqual(obj.authenticate(obj.email,obj.password,obj.sign_in_url,obj.redirect_url ), True)

    #@unittest.skip('')
    def test_wrong_email(self):
        obj = GoodRead()
        obj.set_email("abc@gmail.com")
        obj.set_password("*****")
        obj.set_base_url("https://www.goodreads.com/")
        self.assertEqual(obj.authenticate(obj.email, obj.password, obj.sign_in_url, obj.redirect_url), False)

    #@unittest.skip('')
    def test_wrong_password(self):
        obj = GoodRead()
        obj.set_email("rupam2422@gmail.com")
        obj.set_password("abc")
        obj.set_base_url("https://www.goodreads.com/")
        self.assertEqual(obj.authenticate(obj.email, obj.password, obj.sign_in_url, obj.redirect_url), False)

    #**************************************Test 2.3*****************************************************
    #@unittest.skip('')
    def test_blank_author_get_quotes(self):
        obj = GoodRead()
        obj.query_url = "https://www.goodreads.com/quotes/search?&q=mark+twain&commit=Search"
        self.assertRaises(obj.get_top_quotes("", 8,obj.query_url,"abc.json"))

    #@unittest.skip('')
    def test_zero_quotes_get_quotes(self):
        obj = GoodRead()
        self.assertRaises(obj.get_top_quotes("Mark Twain", 0,"https://www.goodreads.com/quotes/search?&q=mark+twain&commit=Search","abc.json"))

    #@unittest.skip('')
    def test_random_author_get_quotes(self):
        obj = GoodRead()
        self.assertRaises(obj.get_top_quotes("Mark XYZ", 0,"https://www.goodreads.com/quotes/search?&q=mark+twain&commit=Search","abc.json"))

    # @unittest.skip('')
    def test_invalid_authorInt(self):
        obj = GoodRead()
        self.assertRaises(obj.set_author_query(1))

    def test_invalid_authorNegativeInt(self):
        obj = GoodRead()
        self.assertRaises(obj.set_author_query(-1))

    def test_invalid_numpostalpha(self):
        obj = GoodRead()
        self.assertRaises(obj.set_numQuotes('a'))

    def test_invalid_numpostNegativeInt(self):
        obj = GoodRead()
        self.assertRaises(obj.set_numQuotes(-10))

    # @unittest.skip('')
    def test_wrong_link_get_quotes(self):
        obj = GoodRead()
        self.assertRaises(
            obj.get_top_quotes("Mark XYZ", 0, "https://www.xxxxxxxxxxxs.com/quotes/search?&q=mark+twain&commit=Search",
                               "abc.json"))

    # @unittest.skip('')
    def test_blank_link_get_quotes(self):
        obj = GoodRead()
        self.assertRaises(
            obj.get_top_quotes("Mark XYZ", 0, "",
                               "abc.json"))

    ''''''

if __name__ == '__main__':
    print("-------------------------------------------------")
    print("--------Unit Testing Framework: quotes.py--------")
    print("-------------------------------------------------")
    unittest.main()
#%-----------------------------------------------------EOF------------------------------------------------------------%/
