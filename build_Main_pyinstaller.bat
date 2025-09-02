pyinstaller  --clean --windowed --noconfirm --icon=Data/icon.ico --add-data Data;Data --add-data Config;Config --name SCUFFLE GUI_Main.py
rmdir /S /Q "./dist/SCUFFLE/Data/Scripts/Custom/"

cd ./dist
del /Q "SCUFFLE_VV_%1.rar"
"C:\Program Files\WinRAR\winrar.exe" a -r -m5 -af ./SCUFFLE_VV_%1.rar ./SCUFFLE
cd ..

