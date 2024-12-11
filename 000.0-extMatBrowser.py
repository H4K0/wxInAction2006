#!/bin/env python3
import wx
'''
docstring_space: FileBreowser global path variables
'''

class ExtracSignaturesApp(wx.App):
    def OnInit(self):
        '''
        Inicialización de la aplicación
        '''
        self.frame = esFrame(None)
        self.frame.Show()
        return True

class esFrame(wx.Frame):
    '''
    Implemented docstrings class MyFrame
    '''
    def __init__(self, *args, **kwargs):
        '''
        Implemented docstrings function init
        '''
        super().__init__(*args, **kwargs)
        self.path = ""  # Atributo para almacenar el path
        self.InitUI()

    def InitUI(self):
        '''
        Implemented docstrings function init
        '''
        # Crear panel
        panel = wx.Panel(self)

        # Botón para abrir el explorador de archivos
        self.button = wx.Button(panel, label="Seleccionar Archivo", pos=(20, 20))
        self.button.Bind(wx.EVT_BUTTON, self.OnFileBrowser)

        # Campo de texto para mostrar la ruta del archivo seleccionado
        self.text_ctrl = wx.TextCtrl(panel, pos=(20, 70), size=(300, -1))

        # Configuración de la ventana principal
        self.SetTitle("Explorador de Archivos")
        self.SetSize((400, 200))
        self.Centre()

    def OnFileBrowser(self, event):
        '''
        Manejador para abrir el explorador de archivos
        '''
        with wx.FileDialog(self, "Seleccione un archivo", wildcard="Todos los archivos (*.*)|*.*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return  # El usuario canceló el diálogo
            # Obtener la ruta del archivo seleccionado
            self.path = file_dialog.GetPath()
            self.text_ctrl.SetValue(self.path)  # Mostrar la ruta en el campo de texto
            global pathExt
            pathExt = self.path  # Obtener el valor almacenado en MyFrame
            print("Retornamos el path desde OnFileBrowser:", self.path)

#######
# 
# End of class declarations
#
######


def main():
    app = ExtracSignaturesApp()
    app.MainLoop()
    print("Retornamos el path en la función main:", pathExt)


if __name__ == '__main__':
    main()
    print("Retornamos el path en la llamada a main():", pathExt)