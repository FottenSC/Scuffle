pyinstaller  --clean --windowed --noconfirm --icon=Data/icon.ico --add-data Data;Data --add-data Config;Config --name SCUFFLE_Editor GUI_MoveViewer.py
rmdir /S /Q "./dist/SCUFFLE/Data/Scripts/Custom/"

cd ./dist
del /Q "SCUFFLE_Editor_VV_%1.rar"
"C:\Program Files\WinRAR\winrar.exe" a -r -m5 -af ./SCUFFLE_Editor_VV_%1.rar ./SCUFFLE_Editor
cd ..