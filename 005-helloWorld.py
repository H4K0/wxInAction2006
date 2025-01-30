#!/usr/bin/env python3

import wx

'''
Simlpe frame with useful menubar
'''

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame("Hello World", (50, 60), (450, 340))
        frame.Show()
        self.SetTopWindow(frame)
        return True

class MyFrame(wx.Frame):
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)
        menuFile = wx.Menu()
        menuFile.Append(1, "&About...")
        menuFile.AppendSeparator()
        menuFile.Append(2, "E&xit")
  
        menuOptions = wx.Menu()
        menuOptions.Append(1, "O&ptions1")
        menuOptions.Append(2, "Opt&ions2")
        menuOptions.Append(3, "Opti&ons3")
        menuOptions.Append(4, "Optio&ns4")
        menuOptions.Append(5, "Option&s5")
        menuOptions.AppendSeparator()
        menuOptions.Append(6, "A&bout Options")
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&File")
        menuBar.Append(menuOptions, "&Options")
        
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()

        self.SetStatusText("Welcome to wxPython!")

        self.Bind(wx.EVT_MENU, self.OnAbout, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=2)
        self.Bind(wx.EVT_MENU, self.OnAboutOptions, id=6)

    def OnQuit(self, event):
        self.Close()

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello world sample", "About Hello World", wx.OK | wx.ICON_INFORMATION, self)

    def OnAboutOptions(self, event):
        wx.MessageBox("     H4K0 message box     ", "About H4K0 Hello World", wx.OK | wx.ICON_INFORMATION, self)

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()