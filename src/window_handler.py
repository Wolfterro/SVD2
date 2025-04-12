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
from io import StringIO
import time
from PyQt5 import QtCore, QtGui, QtWidgets

import os
import sys
import ctypes
import platform
import subprocess
import threading
from os.path import expanduser

# Imports do programa
# ===================
from src.global_vars import GlobalVars
from src.downloader import Downloader
from src.window_message_box import ShowMessageBox
from src.updater import Updater

# Determinando a pasta 'home' do usuário.
# =======================================
if platform.system() == "Windows":
    buf = ctypes.create_unicode_buffer(1024)
    ctypes.windll.kernel32.GetEnvironmentVariableW("USERPROFILE", buf, 1024)
    home_dir = buf.value
else:
    home_dir = expanduser("~")


# Classe do gerenciador da janela principal
# =========================================
class WindowHandler(object):
    # Inicializando objetos da classe
    # ===============================
    def __init__(self, ui, MainWindow):
        self.ui = ui
        self.MainWindow = MainWindow
        self.messageBox = ShowMessageBox()

        # Propriedades da classe
        # ----------------------
        if platform.system() == "Windows":
            self.div = "\\"
        else:
            self.div = "/"
        self.isFFmpegPresent = False

        self.videoURL = ""
        self.selectedDir = ""
        self.saveOption = ""
        self.keepOriginal = None
        self.openChosenDirAfterDownload = None

        # Declarações da classe
        # ---------------------
        self.checkBinaries()

    # Verificando se os binários do youtube-dl e ffmpeg estão na pasta /bin
    # =====================================================================
    def checkBinaries(self):
        programLocation = os.getcwd()  # Substituição do os.getcwdu() por os.getcwd()
        GlobalVars.BinFolder = "%s%s%s" % (programLocation, self.div, "bin")

        GlobalVars.Youtube_dl = "%s%s%s" % (GlobalVars.BinFolder, self.div, GlobalVars.ExecutableName1)
        ffmpegBin = "%s%s%s" % (GlobalVars.BinFolder, self.div, GlobalVars.ExecutableName2)

        if not os.path.isfile(GlobalVars.Youtube_dl):
            self.messageBox.show("Erro!",
                                 QtWidgets.QMessageBox.Critical,
                                 "Binário '%s' não está presente na pasta /bin!" % (GlobalVars.ExecutableName1),
                                 "É necessário que o binário '%s' esteja presente na pasta /bin para"
                                 " realizar o download dos vídeos!" % (GlobalVars.ExecutableName1),
                                 QtWidgets.QMessageBox.Ok,
                                 1)

        if not os.path.isfile(ffmpegBin):
            self.messageBox.show("Aviso!",
                                 QtWidgets.QMessageBox.Warning,
                                 "Binário '%s' não está presente na pasta /bin!" % (GlobalVars.ExecutableName2),
                                 "O programa não poderá fazer conversões de formatos sem o ffmpeg!",
                                 QtWidgets.QMessageBox.Ok,
                                 0)
            self.isFFmpegPresent = False
        else:
            self.isFFmpegPresent = True

    # Mostrando informações do programa no terminal auxiliar
    # ======================================================
    def displayInfo(self):
        print("====================================")
        print("SVD - Simple Video Downloader - v%s" % (GlobalVars.Version))
        print("====================================\n")
        print("Este prompt de comando serve de apoio para o programa.")
        print("Mantenha este prompt aberto enquanto o programa estiver sendo executado!")

    # Mostrando informações do programa em uma MessageBox
    # ===================================================
    def displayAbout(self):
        self.messageBox.show("Simple Video Downloader",
                             QtWidgets.QMessageBox.Information,
                             "SVD - Simple Video Downloader - Versão %s" % (GlobalVars.Version),
                             "Criado por: Wolfgang Almeida - © 2025\n\n*** Este programa é licenciado sob a licença MIT ***"
                             "\nVisite o repositório no GitHub: \nhttps://github.com/Wolfterro/SVD2",
                             QtWidgets.QMessageBox.Ok,
                             0)

    # Inserindo a pasta de destino padrão
    # ===================================
    def setDefaultDir(self):
        self.ui.lineEdit_2.setText("%s%s%s" % (home_dir, self.div, GlobalVars.SaveFolder))

    # Saindo do programa
    # ==================
    def exitProgram(self):
        sys.exit(0)

    # Verificando a pasta de destino
    # ==============================
    def checkSelectedDir(self):
        if os.path.exists(self.selectedDir):
            os.chdir(self.selectedDir)
        else:
            os.makedirs(self.selectedDir)
            os.chdir(self.selectedDir)

    # Método para selecionar pasta de destino.
    # ========================================
    def selectOutputDir(self):
        self.selectedDir = QtWidgets.QFileDialog.getExistingDirectory(self.MainWindow,
                                                                       'Selecione a pasta de destino:',
                                                                       home_dir,
                                                                       QtWidgets.QFileDialog.ShowDirsOnly)
        if self.selectedDir != "":
            if platform.system() == "Windows":
                self.ui.lineEdit_2.setText(self.selectedDir.replace("/", "\\"))
            else:
                self.ui.lineEdit_2.setText(self.selectedDir)

    # Congelando os botões da janela principal
    # ========================================
    def freezeProgramFields(self, freeze):
        if freeze:
            self.ui.pushButton.setEnabled(False)
            self.ui.toolButton.setEnabled(False)
            QtWidgets.QApplication.processEvents()
        else:
            self.ui.pushButton.setEnabled(True)
            self.ui.toolButton.setEnabled(True)
            QtWidgets.QApplication.processEvents()

    # Resgatando informações do usuário
    # =================================
    def gatherUserInformation(self):
        self.videoURL = str(self.ui.lineEdit.text())
        self.selectedDir = str(self.ui.lineEdit_2.text())
        self.checkSelectedDir()

        self.saveOption = str(self.ui.comboBox.currentText())
        self.keepOriginal = self.ui.checkBox_2.isChecked()
        self.openChosenDirAfterDownload = self.ui.checkBox.isChecked()

        if self.videoURL != "":
            self.beginDownloadProcess()
        else:
            self.messageBox.show("Erro!",
                                 QtWidgets.QMessageBox.Critical,
                                 "URL do Vídeo ou Playlist vazia!",
                                 "Insira a URL do Vídeo ou Playlist desejada e tente novamente!",
                                 QtWidgets.QMessageBox.Ok,
                                 0)

    # Iniciando o processo de download
    # ================================
    def beginDownloadProcess(self):
        self.freezeProgramFields(True)
        # ------------------------------------------------------------------------
        downloader = Downloader(self.videoURL, self.saveOption, self.keepOriginal)
        threading.Thread(
            target=downloader.download, 
            args=(self.freezeProgramFields, self.openChosenDirAfterDownload, self.selectedDir, ), 
            daemon=True
        ).start()
        # ------------------------------------------------------------------------

    # Atualizando o binário do youtube-dl
    # ===================================
    def updateYoutube_dl(self):
        try:
            print("\n[SVD] Atualizando youtube-dl...")
            print("-------------------------------")

            self.freezeProgramFields(True)
            # -----------------------------------------------
            update = Updater()
            updateStatus = update.Youtube_DL()
            # -----------------------------------------------
            file = os.getcwd() + "/" + GlobalVars.ExecutableName1

            if updateStatus:
                if platform.system() != "Windows":
                    subprocess.Popen("chmod +x %s" % (file), shell=True)

                version = subprocess.Popen("%s %s" % (file, "--version"), shell=True, stdout=subprocess.PIPE)
                print("Versão atual: %s" % (version.stdout.read().decode("utf-8")), end="")
                print("\n[SVD] Atualização do yt-dlp concluída!")
                print("----------------------------------------")
            else:
                print("\n[SVD] Não foi possível atualizar o yt-dlp!")
                print("--------------------------------------------")
        except Exception as e:
            print("\n[SVD] Erro ao tentar atualizar o yt-dlp!")
            print("[SVD] Erro: %s" % (e))
        finally:
            self.freezeProgramFields(False)
