#!/usr/bin/env python3
import wx

"""
[Spare.py] extend-bare-minimum.py is a starting point for a wxPython program.
"""

"""Example of docstring usage:
Module docstring:
    import spare
    print spare.__doc__
    [Spare.py] extend-bare-minimum.py is a starting point for a wxPython program.
"""

class Frame(wx.Frame):
   pass

class App(wx.App):
   def OnInit(self):
      self.frame = Frame(parent=None, title='Extend-bare-minimum')
      self.frame.Show()
      self.SetTopWindow(self.frame)
      return True

if __name__ == '__main__':
   app = App()
   app.MainLoop()