# 🎥 SVD2 - Simple Video Downloader 2.0

[![Licença MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)](https://www.python.org/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-Suportado-lightgrey?logo=youtube)](https://github.com/yt-dlp/yt-dlp)
[![ffmpeg](https://img.shields.io/badge/ffmpeg-Requerido-green?logo=ffmpeg)](https://ffmpeg.org/)

**SVD2** é um aplicativo simples e poderoso para download e conversão de vídeos e áudios, utilizando o `yt-dlp` como motor principal.  
Com uma interface gráfica intuitiva criada em PyQt5, você pode baixar conteúdos de plataformas como YouTube, Twitter, entre outras — tudo com poucos cliques!

---

## ✨ Funcionalidades

✅ Baixe vídeos e áudios em diversos formatos (MP4, MP3, MKV, WEBM...)  
✅ Interface gráfica simples e funcional com PyQt5  
✅ Integração com `yt-dlp` e `ffmpeg`  
✅ Atualização automática do `yt-dlp` pelo app  
✅ Suporte a URLs individuais e playlists  

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.6 ou superior
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) instalado e disponível na pasta `bin`
- [`ffmpeg`](https://ffmpeg.org/) instalado e acessível na pasta `bin`
- Dependências Python (ver abaixo)

### Passos

```bash
git clone https://github.com/Wolfterro/SVD2.git
cd SVD2
pip install -r requirements.txt
```

> 💡 Recomenda-se o uso de um ambiente virtual (`venv` ou `virtualenv`).

---

## 🧑‍💻 Como Usar

Execute o aplicativo com:

```bash
python main.py
```

1. Insira o link do vídeo ou playlist.
2. Selecione o formato desejado (áudio ou vídeo).
3. Escolha o diretório de destino.
4. Clique em **Download** e aguarde o processo!

---

## 🛠️ Compilação para Executável

Você pode gerar uma versão executável com PyInstaller para facilitar a distribuição:

### No Windows:

```bash
build.bat
```

### No Linux:

```bash
./build.sh
```

O executável será gerado na pasta `dist/`.

---

## 🧾 Licença

Este projeto é licenciado sob os termos da [Licença MIT](LICENSE).  
Sinta-se à vontade para usar, modificar e distribuir conforme necessário!

---

## 🔗 Links Úteis

- [yt-dlp - Repositório Oficial](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg - Site Oficial](https://ffmpeg.org/)
- [Documentação do PyInstaller](https://pyinstaller.org/)
- [PyQt5 Documentation](https://doc.qt.io/qtforpython/)

---

Feito com 💻 por [Wolfterro](https://github.com/Wolfterro)
