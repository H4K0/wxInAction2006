#!/usr/bin/env python3

import wx
import os.path
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Alignment

'''
@docstring

Explicación del código

    wx.FileDialog: Es el cuadro de diálogo que permite navegar por el sistema de archivos.
        wildcard="Todos los archivos (*.*)|*.*" define el tipo de archivos que se pueden seleccionar.
        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST asegura que se seleccione un archivo existente.

    Botón (wx.Button): Al hacer clic en el botón, se abre el explorador de archivos.

    Campo de texto (wx.TextCtrl): Se usa para mostrar la ruta completa del archivo seleccionado.

Este ejemplo es completamente funcional y se puede ejecutar directamente en cualquier entorno con wxPython instalado.
'''

myPath = ''
print("Ruta absoluta de myPath:", os.path.abspath(myPath))

filas =     ['B','C','D','E','F','G','N','P','R','T','V',
            'X','Z','AB','AD','AF','AH','AJ','AL','AN',
            'AP','AR','AT','AV'
            ]
filasImp =  ['D','N','P','R','T','V','X','Z','AB','AD',
            'AF','AH','AJ','AL','AN','AP','AR','AT'
            ]
sl =        ['','Álgebra', 'Arts', 'Biology', 'Citizenship', 'Computer Science',
            'Desarrollo Humano', 'English', 'Estadística', 'Filosofía', 'Física',
            'Geography', 'Geometría', 'Historia', 'Lenguaje', 'Ortografía',
            'Physical Education', 'Química'
            ]
columnas = [10, 77]
paso =[]

class extraerMateriasApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        # Botón para abrir el explorador de archivos
        self.button = wx.Button(panel, label="Seleccionar Archivo", pos=(20, 20))
        self.button.Bind(wx.EVT_BUTTON, self.OnFileBrowser)

        # Botón para procesar el archivo
        self.button = wx.Button(panel, label="Procesar archivo", pos=(20, 20))
        self.button.Bind(wx.EVT_BUTTON, self.OnFileBrowser)

        # Campo de texto para mostrar la ruta del archivo seleccionado
        self.text_ctrl = wx.TextCtrl(panel, pos=(20, 70), size=(300, -1))

        # Configuración de la ventana principal
        self.SetTitle("Explorador de Archivos")
        self.SetSize((400, 200))
        self.Centre()

    def OnFileBrowser(self, event):
        # Creación del cuadro de diálogo para seleccionar archivo
        with wx.FileDialog(self, "Seleccione un archivo", wildcard="Todos los archivos (*.*)|*.*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # Si se cancela, no hace nada

            # Obtiene la ruta del archivo seleccionado
            path = fileDialog.GetPath()
            self.text_ctrl.SetValue(path)
            myPath = path

    def OnProcessFile(self, event):
        #Procesamos el archivo
        print('Procesamos el archivo')


if __name__ == "__main__":
    app = wx.App(False)
    frame = extraerMateriasApp(None)
    frame.Show()
    app.MainLoop()
