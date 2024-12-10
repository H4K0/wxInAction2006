#!/usr/bin/env python3

import wx

"""
Hello, wxPython! program. For PNG image.
"""

class ImageFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(ImageFrame, self).__init__(*args, **kwargs)
        self.image = wx.Image("src/splash.png", wx.BITMAP_TYPE_PNG) # Load the PNG image
        self.bitmap = wx.StaticBitmap(self, bitmap=self.image.ConvertToBitmap()) # Create a StaticBitmap to display the image
        self.SetSize(self.image.GetSize()) # Set the frame size to the size of the image
        self.SetTitle("PNG Image Display") # Set the frame title
        
        self.Centre() # Center the window on the screen
        self.Show() # Show the frame

def main():
    app = wx.App(False)  # Create a new application
    frame = ImageFrame(None)  # Create a frame instance
    app.MainLoop()  # Start the event loop

if __name__ == "__main__":
    main()