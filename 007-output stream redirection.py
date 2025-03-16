#!/usr/bin/env python

import wx
import sys

'''
docstring: strange print behaivor
'''

class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        print("Frame __init__", file=sys.stderr)
        wx.Frame.__init__(self, parent, id, title)

class App(wx.App):
    def __init__(self, redirect=True, filename=None):
        print("App __init__", file=sys.stderr)
        wx.App.__init__(self, redirect, filename)

    def OnInit(self):
        print("OnInit", file=sys.stderr)
        self.frame = Frame(parent=None, id=-1, title='Startup')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print("A pretend error message", file=sys.stderr)
        return True

    def OnExit(self):
        print("OnExit", file=sys.stderr)

if __name__ == '__main__':
    app = App(redirect=True)
    print("before MainLoop", file=sys.stderr)
    print("Print -> before MainLoop")
    app.MainLoop()
    #Esta parte de la app corre cuando se cierra el frame y también sale al sys.stdout
    print("after MainLoop", file=sys.stderr)
    print("Print -> after MainLoop")
