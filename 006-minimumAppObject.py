#!/usr/bin/env python3

import wx

'''
Create my very simple wxPython App class: pySimpleApp()
'''
class PySimpleApp(wx.App):
    def __init__(self, redirect=False, filename=None, 
                 useBestVisual=False, clearSigInt=True):
        wx.App.__init__(self, redirect, filename, useBestVisual,
        clearSigInt)
        def OnInit(self):
            return True

class MyNewFrame(wx.Frame):
   pass

if __name__ == '__main__':
    app = PySimpleApp()
    frame = MyNewFrame(None)
    frame.Show(True)
    app.MainLoop()