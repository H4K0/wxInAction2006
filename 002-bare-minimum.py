#!/bin/env python3

'''
One of the best learning start point
'''

import wx

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='My Bare Minimum Frame/Window')
        frame.Show()
        return True

app = MyApp()
app.MainLoop()