import wx
import wx.adv

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Aplicación Principal", size=(400, 300))
        panel = wx.Panel(self)
        wx.StaticText(panel, label="Bienvenido a la aplicación", pos=(50, 50))

class MyApp(wx.App):
    def OnInit(self):
        bitmap = wx.Bitmap("src/splash.png", wx.BITMAP_TYPE_PNG)
        splash = wx.adv.SplashScreen(bitmap, 
                                     wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT, 
                                     5000, None)
        wx.Yield()  # Permite que se actualice la GUI mientras se muestra el splash
        
        # Abre la ventana principal después del splash
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
