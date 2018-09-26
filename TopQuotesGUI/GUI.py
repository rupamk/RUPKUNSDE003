#!/ven/bin/env python
'''
Expedia Coding Challenge
Author: Rupam Kundu, The Ohio State University
'''
import os
import wx
from Quotes import GoodRead
import wx.lib.agw.hyperlink as hl
import json
from Get_quotes import Get_quotes
from Authenticate import Authenticate
import os.path
from Test_quotes import TestMethods
import unittest

class GoodReadGUI(wx.Frame):
    def __init__(self, parent, title):
        super(GoodReadGUI, self).__init__(parent, title=title,
                                      )
        self.InitUI()
        self.Centre()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel.Fit()
        self.panel.SetBackgroundColour("gray")
        # Authenticate Me
        self.header1 = wx.StaticText(self.panel, label="Authenticate your credentials to Goodread.com")
        self.header1.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.header1.SetForegroundColour("blue")
        self.warning = wx.StaticText(self.panel,
                                     label="NOTE: If you have not created an account yet go ahead and create an account at Goodreads.com ")
        self.warning.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.warning.SetForegroundColour("white")
        self.email = wx.StaticText(self.panel,label="Email")
        self.email.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.email_field = wx.TextCtrl(self, value="", size=(300, 20))
        self.password = wx.StaticText(self.panel,label="Password")
        self.password.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.password_field = wx.TextCtrl(self, value="", size=(300, 20))
        self.link = hl.HyperLinkCtrl(self.panel, -1, "Link to Goodreads.com", pos=(100, 100),URL="https://www.goodreads.com/user/sign_in")
        self.link.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.NORMAL, False, 'Courier'))
        self.authenticate_me = wx.Button(self.panel, label="Authenticate me", )
        self.authenticate_me.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.FONTWEIGHT_BOLD, False, 'Times'))
        self.authenticate_me.SetBackgroundColour("Gray")
        #Get Quotes
        self.header2 = wx.StaticText(self.panel,
                                     label="Get the top quotes from Goodread.com")
        self.header2.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.header2.SetForegroundColour("blue")
        self.author = wx.StaticText(self.panel,
                                     label="Enter the name of the author:")
        self.author.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.author_field = wx.TextCtrl(self, value="", size=(300, 20))
        self.numpost = wx.StaticText(self.panel,
                                     label="Number of Post:")
        self.numpost.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.numpost_field = wx.TextCtrl(self, value="", size=(300, 20))
        self.get_quotes = wx.Button(self.panel, label="Get Quotes", )
        self.get_quotes.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.FONTWEIGHT_BOLD, False, 'Times'))
        self.get_quotes.SetBackgroundColour("Gray")
        # Run Unit Test
        self.run_unit_test = wx.Button(self.panel, label="Run Unit Test For User Authentication and Get Quotes" )
        self.run_unit_test.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.FONTWEIGHT_BOLD, False, 'Times'))
        self.run_unit_test.SetBackgroundColour("Gray")
        #Consolidate
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)
        self.sizer = wx.GridBagSizer(20, 10)
        self.sizer.Add(self.header1, (0, 0))
        self.sizer.Add(self.warning, (1, 0))
        self.sizer.Add(self.link, (2, 0))
        self.sizer.Add(self.email, (3, 0))
        self.sizer.Add(self.email_field, (4, 0))
        self.sizer.Add(self.password, (5, 0))
        self.sizer.Add(self.password_field, (6, 0))
        self.sizer.Add(self.authenticate_me, (7, 0), (0,0))
        self.sizer.Add(self.header2, (8, 0))
        self.sizer.Add(self.author,(9,0 ))
        self.sizer.Add(self.author_field,(10,0 ) )
        self.sizer.Add(self.numpost, (11, 0))
        self.sizer.Add(self.numpost_field, (12, 0))
        self.sizer.Add(self.get_quotes, (13, 0))
        self.sizer.Add(self.run_unit_test, (14, 0), flag = wx.EXPAND)
        self.link.EnableRollover(True)
        self.link.UpdateLink()
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 2, wx.ALL | wx.EXPAND, 5)
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)
        self.authenticate_me.Bind(wx.EVT_BUTTON, self.onButton)
        self.get_quotes.Bind(wx.EVT_BUTTON, self.onButton)
        self.run_unit_test.Bind(wx.EVT_BUTTON, self.onButton)

    def onButton(self, event):
        button = event.GetEventObject()
        if(button.GetLabel()=="Run Unit Test For User Authentication and Get Quotes"):
            print('Check Terminal for output')
            os.system('python test_quotes.py')


        if(button.GetLabel()=="Authenticate me"):
            #os.system('python authenticate.py')
            try:
                if not self.email_field.GetValue():
                    raise ValueError('Blank Email')
                if not self.password_field.GetValue():
                    raise ValueError('Blank Password')
                Authenticate(self.email_field.GetValue(),self.password_field.GetValue())
            except ValueError as e:
                print(e)

        if (button.GetLabel() == "Get Quotes"):
            try:
                if not self.author_field.GetValue():
                    raise ValueError('No author name provided')
                if not self.numpost_field.GetValue():
                    raise ValueError('Please provide something in the Number of Post field')
                Get_quotes(self.author_field.GetValue(), self.numpost_field.GetValue())
                text = self.author_field.GetValue().split(' ')
                s = ''
                for item in text:
                    s = s + str(item) + '_'
                name = s[:-1]
                path = "./TopQuotesGUI/Data/"
                temp = []
                for item in str(self.author_field.GetValue()).split(' '):
                    temp.append(item.lower().capitalize())
                author = ' '.join(temp)
                if(os.path.isfile(path+name+ '_top_quotes.json')):

                    index = "Quotes By:" + author

                    with open(path+name+ '_top_quotes.json') as json_file:
                        data = json.load(json_file)
                        try:
                            if not data[index]:
                                raise  ValueError('No data to print')
                            for i,p in enumerate(data[index]):
                                print(p['Content'])
                                print('')
                                print('********************************************************')
                        except ValueError as e:
                            print(e)

                    os.remove(path+name+ '_top_quotes.json')
            except ValueError as e:
                print(e)

def main():
    app = wx.App(redirect=True)
    ex = GoodReadGUI(None, title='GoodRead Quotes')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
