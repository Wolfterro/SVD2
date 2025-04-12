"""
The MIT License (MIT)

Copyright (c) 2025 Wolfgang Almeida <wolfgang.almeida@yahoo.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Imports gerais
# ==============
import subprocess
import platform
import os

# Imports do programa
# ===================
from src.global_vars import GlobalVars
from src.window_message_box import ShowMessageBox

# Classe de downloads do programa
# ===============================
class Downloader(object):
    def __init__(self, videoURL, saveOption, keepOriginal):
        # Propriedades da classe
        self.videoURL = videoURL
        self.saveOption = saveOption
        self.keepOriginal = keepOriginal

        self.messageBox = ShowMessageBox()

        self.saveFormat = ""
        self.isConversion = None
        self.downloadCommand = ""

        # Inicializa os métodos para configurar o download
        self.getSaveFormat()
        self.assembleDownloadCommand()

    # Resgata o formato desejado pelo usuário
    # =========================================
    def getSaveFormat(self):
        if "(Conversão)" in self.saveOption:
            self.isConversion = True
        else:
            self.isConversion = False
        self.saveFormat = str(self.saveOption).replace(" (Conversão)", "").lower()

    # Monta o comando para o download do vídeo
    # ========================================
    def assembleDownloadCommand(self):
        base = "\"%s\" --ignore-errors" % (GlobalVars.Youtube_dl)
        
        if self.keepOriginal:
            extra1 = "-k"
        else:
            extra1 = ""
        
        if self.saveFormat in GlobalVars.AudioFormats:
            extra2 = "--extract-audio --audio-quality 0 --audio-format %s %s" % (self.saveFormat, self.videoURL)
        elif self.isConversion:
            extra2 = "--recode-video %s %s" % (self.saveFormat, self.videoURL)
        else:
            extra2 = "--format %s %s" % (self.saveFormat, self.videoURL)

        # Monta o comando completo sem codificação adicional
        self.downloadCommand = "%s %s %s" % (base, extra2, extra1)

    # Realiza o download do vídeo selecionado
    # ========================================
    def download(self, freezeProgramFields, openChosenDirAfterDownload, selectedDir):
        print("\n[SVD] Baixando Vídeo no formato \".%s\" ..." % (self.saveFormat))
        print("-------------------------------------------")
        
        # Execute o comando com shell=True para que a string seja interpretada corretamente
        subprocess.call(self.downloadCommand, shell=True)
        
        print("\n=================================")
        print("[SVD] Download Finalizado!")

        if openChosenDirAfterDownload:
            if platform.system() == "Windows":
                os.startfile(self.selectedDir)
            else:
                try:
                    subprocess.Popen(["xdg-open", selectedDir])
                except Exception as e:
                    pass

        freezeProgramFields(False)

    # Imprime o comando na tela para fins de debug
    # =============================================
    def printCommand(self):
        print(self.downloadCommand)
