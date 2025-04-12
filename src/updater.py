#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports gerais
# ==============
import os
import urllib.request

# Imports do programa
# ===================
from src.global_vars import GlobalVars

# Classe de atualização dos binários do programa
# ==============================================
class Updater(object):
    # Método de atualização do youtube-dl
    # ===================================
    def Youtube_DL(self):
        os.chdir(GlobalVars.BinFolder)
        downloadStatus = self.download(GlobalVars.ExecutableName1, GlobalVars.YtDlLatestVersionURL)
        return downloadStatus

    # Método de download do executável atualizado
    # ===========================================
    def download(self, filename, url):
        try:
            request = urllib.request.Request(url, headers={'User-agent': GlobalVars.UserAgent})
            
            # DEBUG APENAS!
            # =============
            response = urllib.request.urlopen(request)
            
            fSize = response.headers.get('content-length')
            fSize = int(fSize) if fSize is not None else None

            downloaded = 0
            with open(filename, 'wb') as f:
                while True:
                    fData = response.read(4096)
                    if not fData:
                        break
                    downloaded += len(fData)
                    f.write(fData)
                    if fSize:
                        self.showProgress(downloaded, fSize)
            return True
        except Exception as e:
            print("[SVD] Erro: %s" % (e))
            return False

    # Método para calcular o progresso do download do executável
    # O método imprime uma barra de processo no terminal
    # ==========================================================
    def showProgress(self, now, total, width=50):
        progress = float(now) / float(total)
        bar = ('#' * int(width * progress)).ljust(width)
        percent = progress * 100.0
        to_print = '[SVD] Baixando: [%s] %.2f%%\r' % (bar, percent)
        print(to_print, end='')
        if round(percent) >= 100:
            print('%s\r' % (' ' * len(to_print)), end='')
