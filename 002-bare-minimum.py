#!/bin/env python3

'''
One of the best learning start point
'''

import wx

class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True

app = App()
app.MainLoop()