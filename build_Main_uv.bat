cd ./dist
rmdir /S /Q "SCUFFLE" 
del /Q "SCUFFLE_VV_%1.rar"
rmdir /S /Q "SCUFFLE_Editor" 
del /Q "SCUFFLE_Editor_VV_%1.rar"
cd ..

uv run nuitka --standalone --enable-plugin=tk-inter ./GUI_Main.py --output-dir=./dist --output-filename=SCUFFLE --remove-output --windows-console-mode=disable --windows-icon-from-ico=.\Data\icon.ico --product-name=SCUFFLE --file-version=%1 --product-version=%1 --include-data-dir=./Config=Config --include-data-dir=./Data=Data 
move "./dist/GUI_Main.dist" "./dist/SCUFFLE"
rmdir /S /Q "./dist/SCUFFLE/Data/Scripts/Custom/"

uv run nuitka --standalone --enable-plugin=tk-inter ./GUI_Moveviewer.py --output-dir=./dist --output-filename=SCUFFLE_Editor --remove-output --windows-console-mode=disable --windows-icon-from-ico=.\Data\icon.ico --product-name=SCUFFLE_Editor --file-version=%1 --product-version=%1 --include-data-dir=.\Config=.\Config --include-data-dir=.\Data=.\Data 
move "./dist/GUI_Moveviewer.dist" "./dist/SCUFFLE_Editor"
rmdir /S /Q "./dist/SCUFFLE_Editor/Data/Scripts/Custom/"

cd ./dist
"C:\Program Files\WinRAR\winrar.exe" a -r -m5 -af ./SCUFFLE_VV_%1.rar ./SCUFFLE
"C:\Program Files\WinRAR\winrar.exe" a -ep -apSCUFFLE ./SCUFFLE_VV_%1.rar "./SCUFFLE_Editor/SCUFFLE_Editor.exe"
rmdir /S /Q "SCUFFLE"
rmdir /S /Q "SCUFFLE_Editor"
"C:\Program Files\WinRAR\winrar.exe" x ./SCUFFLE_VV_%1.rar


cd ..
