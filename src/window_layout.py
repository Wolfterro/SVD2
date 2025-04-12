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

import sys
import os

# Imports do PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Imports do programa
from src.global_vars import GlobalVars
from src.window_handler import WindowHandler

# Funções auxiliares para compatibilidade de tradução (não são mais necessárias no Python 3,
# mas foram mantidas para preservar a estrutura original)
def _fromUtf8(s):
    return s

def _translate(context, text, disambig):
    return QtCore.QCoreApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, Handler):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(648, 253)
        MainWindow.setMaximumSize(QtCore.QSize(648, 253))
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(GlobalVars.IconName)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 2)
        
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 0, 1, 1)
        
        self.toolButton = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout_2.addWidget(self.toolButton, 0, 1, 1, 1)
        
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 1)
        
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 1)
        
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_3.addWidget(self.comboBox, 0, 0, 1, 1)
        
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout_3.addWidget(self.checkBox_2, 1, 0, 1, 1)
        
        self.gridLayout_5.addWidget(self.groupBox_3, 1, 1, 1, 1)
        
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)
        
        self.gridLayout_5.addWidget(self.groupBox_4, 2, 0, 1, 2)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 648, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menuAtualizar = QtWidgets.QMenu(self.menubar)
        self.menuAtualizar.setObjectName(_fromUtf8("menuAtualizar"))
        
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionYoutube_dl = QtWidgets.QAction(MainWindow)
        self.actionYoutube_dl.setObjectName(_fromUtf8("actionYoutube_dl"))
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionSimple_Video_Downloader = QtWidgets.QAction(MainWindow)
        self.actionSimple_Video_Downloader.setObjectName(_fromUtf8("actionSimple_Video_Downloader"))
        
        self.menuAtualizar.addAction(self.actionYoutube_dl)
        self.menuAtualizar.addSeparator()
        self.menuAtualizar.addAction(self.actionSair)
        self.menuSobre.addAction(self.actionSimple_Video_Downloader)
        
        self.menubar.addAction(self.menuAtualizar.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Conecta o sinal aboutToQuit para executar o método exitProgram do Handler
        QtWidgets.QApplication.instance().aboutToQuit.connect(Handler.exitProgram)
        
        # Conectando os botões e menus da janela principal do programa
        self.pushButton.clicked.connect(Handler.gatherUserInformation)
        self.toolButton.clicked.connect(Handler.selectOutputDir)
        
        self.actionYoutube_dl.triggered.connect(Handler.updateYoutube_dl)
        self.actionSair.triggered.connect(Handler.exitProgram)
        self.actionSimple_Video_Downloader.triggered.connect(Handler.displayAbout)
        
        # Guarda o objeto Handler para ser utilizado internamente
        self.Handler = Handler
        
        # Declarações de inicialização
        Handler.setDefaultDir()
        self.populateSaveOptions()
        Handler.displayInfo()

    # Populando a lista de opções de salvamento
    def populateSaveOptions(self):
        if self.Handler.isFFmpegPresent:
            counter = 0
            for option in GlobalVars.PossibleSaveOptions:
                self.comboBox.addItem("")
                self.comboBox.setItemText(counter, _translate("MainWindow", option, None))
                counter += 1
            self.checkBox_2.setEnabled(True)
        else:
            counter = 0
            for option in GlobalVars.PossibleSaveOptions:
                if "(Conversão)" in option:
                    continue
                else:
                    self.comboBox.addItem("")
                    self.comboBox.setItemText(counter, _translate("MainWindow", option, None))
                    counter += 1
            self.checkBox_2.setEnabled(False)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            _translate("MainWindow", "SVD - Simple Video Downloader - v%s" % GlobalVars.Version, None)
        )
        self.groupBox.setTitle(_translate("MainWindow", "Endereço", None))
        self.label.setText(_translate("MainWindow", "URL do Vídeo ou Playlist:", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Pasta de destino", None))
        self.toolButton.setText(_translate("MainWindow", "...", None))
        self.checkBox.setText(
            _translate("MainWindow", "Abrir pasta de destino quando o download for concluído", None)
        )
        self.groupBox_3.setTitle(_translate("MainWindow", "Opções de Salvamento", None))
        self.checkBox_2.setText(
            _translate("MainWindow", "Manter arquivo original (em conversões)", None)
        )
        self.groupBox_4.setTitle(_translate("MainWindow", "Iniciar download", None))
        self.pushButton.setText(_translate("MainWindow", "Download", None))
        self.menuAtualizar.setTitle(_translate("MainWindow", "Atualizar", None))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre", None))
        self.actionYoutube_dl.setText(_translate("MainWindow", "yt-dlp", None))
        self.actionSair.setText(_translate("MainWindow", "Sair", None))
        self.actionSimple_Video_Downloader.setText(_translate("MainWindow", "Simple Video Downloader", None))


def initializeWindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    
    # Instanciando o handler da janela – os métodos definidos em WindowHandlerClass serão responsáveis
    # por tratar os eventos da interface
    Handler = WindowHandler(ui, MainWindow)
    GlobalVars.Ui = ui
    GlobalVars.MainWindow = MainWindow
    GlobalVars.IconPath = os.path.abspath(GlobalVars.IconName)
    
    ui.setupUi(MainWindow, Handler)
    MainWindow.show()
    sys.exit(app.exec_())
