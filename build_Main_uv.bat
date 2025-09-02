cd ./dist
rmdir /S /Q "SCUFFLE" 
del /Q "SCUFFLE_VV_%1.rar"
cd ..
uv run nuitka --standalone --enable-plugin=tk-inter ./GUI_Main.py --output-dir=./dist --output-filename=SCUFFLE --remove-output --windows-console-mode=disable --windows-icon-from-ico=.\Data\icon.ico --product-name=SCUFFLE --file-version=%1 --product-version=%1 --include-data-dir=./Config=Config --include-data-dir=./Data=Data 
move "./dist/GUI_Main.dist" "./dist/SCUFFLE"
rmdir /S /Q "./dist/SCUFFLE/Data/Scripts/Custom/"

cd ./dist
"C:\Program Files\WinRAR\winrar.exe" a -r -m5 -af ./SCUFFLE_VV_%1.rar ./SCUFFLE
cd ..