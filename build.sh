#!/bin/bash
pyinstaller --icon="Icon.ico" --onefile --name="Simple Video Downloader" main.py
mv "dist/Simple Video Downloader" .