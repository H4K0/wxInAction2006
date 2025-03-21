#!/usr/bin/env python
import wx

"""
Hello, wxPython! program. For JPG image and main() correct function implementation.
"""

class Frame(wx.Frame):
        """Frame class that displays an image."""
        
        def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title='Hello, wxPython!'):
            """Create a Frame instance and display image."""
            temp = image.ConvertToBitmap()
            size = temp.GetWidth(), temp.GetHeight()
            wx.Frame.__init__(self, parent, id, title, pos, size)
            self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)

class App(wx.App):
        """Application class."""
        def OnInit(self):
            #image = wx.Image('src/splash.JPG', wx.BITMAP_TYPE_JPEG)
            image = wx.Image('src/splash.png', wx.BITMAP_TYPE_PNG)
            self.frame = Frame(image)
            self.frame.Show()
            self.SetTopWindow(self.frame)
            return True

def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()