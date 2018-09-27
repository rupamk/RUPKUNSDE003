#!/usr/bin/env python
'''
Expedia Coding Challenge
Author: Rupam Kundu, The Ohio State University
GUI for Scrape Fb Page Posts
'''
import os
import wx
import json
from Get_posts import Get_posts
import os.path
import string
import wx.lib.agw.hyperlink as hl

class ScrapeFbdataGUI(wx.Frame):
    def __init__(self, parent, title):
        super(ScrapeFbdataGUI, self).__init__(parent, title=title,
                                          )
        self.InitUI()
        self.Centre()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel.Fit()
        self.panel.SetBackgroundColour("Gray")

        # Get Fb page
        self.header1 = wx.StaticText(self.panel,
                                     label="Get the top posts of a Facebook Page")
        self.header1.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.header1.SetForegroundColour("blue")

        self.link = hl.HyperLinkCtrl(self.panel, -1, "Link to Facebook.com", pos=(100, 100),
                                     URL="https://www.facebook.com/")

        self.header2 = wx.StaticText(self.panel,
                                     label="Note: Make sure to input the proper Facebook Page Name as appears as * in https://www.facebook.com/*")
        self.header2.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.header2.SetForegroundColour("white")

        self.page = wx.StaticText(self.panel,
                                    label="Enter the name of the page:")
        self.page.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.page_field = wx.TextCtrl(self, value="", size=(300, 20))

        self.numpost = wx.StaticText(self.panel,
                                     label="Number of Post(0<Input<20):")
        self.numpost.SetFont(wx.Font(15, wx.SWISS, wx.ITALIC, wx.BOLD, False, 'Courier'))
        self.numpost_field = wx.TextCtrl(self, value="", size=(300, 20))

        self.get_post = wx.Button(self.panel, label="Get Posts")
        self.get_post.SetFont(wx.Font(15, wx.SWISS, wx.NORMAL, wx.FONTWEIGHT_BOLD, False, 'Times'))
        self.get_post.SetBackgroundColour("Gray")

        # Consolidate
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)
        self.sizer = wx.GridBagSizer(20, 10)
        self.sizer.Add(self.header1, (0, 0))
        self.sizer.Add(self.header2, (1, 0))
        self.sizer.Add(self.link, (2, 0))
        self.sizer.Add(self.page, (3, 0))
        self.sizer.Add(self.page_field, (4, 0))
        self.sizer.Add(self.numpost, (5, 0))
        self.sizer.Add(self.numpost_field, (6, 0))
        self.sizer.Add(self.get_post, (7, 0))
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 2, wx.ALL | wx.EXPAND, 5)
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)
        self.get_post.Bind(wx.EVT_BUTTON, self.onButton)

    def onButton(self, event):
        button = event.GetEventObject()
        if (button.GetLabel() == "Get Posts"):
            try:
                if not self.page_field.GetValue():
                    raise ValueError('No Page name provided')
                if not self.numpost_field.GetValue():
                    raise ValueError('Please provide something in the Number of Post field')
                Get_posts(self.page_field.GetValue(), self.numpost_field.GetValue())

                path = "./GetFbPostGUI/Data/"
                name = self.page_field.GetValue()
                if (os.path.isfile(path + 'Top_' + name + '_Facebook_Post.json')):
                    index = "Top " + self.page_field.GetValue() + " Facebook Post"
                    print('************************************************')
                    with open(path + 'Top_' + name + '_Facebook_Post.json') as json_file:
                        data = json.load(json_file)
                        try:
                            if not data[index]:
                                raise ValueError('No data to print')
                            for i, p in enumerate(data[index]):
                                print('Content: ' + p['Content'])
                                print('Timestamp: ' + p['Timestamp'])
                                print('****************************************')
                        except ValueError as e:
                            print(e)
                    os.rename(path + 'Top_' + name + '_Facebook_Post.json', path + 'Top_' + name + '_FB_Post.json')
            except ValueError as e:
                print(e)

def main():
    app = wx.App(redirect=True)
    ex = ScrapeFbdataGUI(None, title='Scrape Fb Page Posts')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
