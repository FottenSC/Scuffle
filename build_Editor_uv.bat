cd ./dist
rmdir /S /Q "SCUFFLE_Editor" 
del /Q "SCUFFLE_Editor_VV_%1.rar"
cd ..
uv run nuitka --standalone --enable-plugin=tk-inter ./GUI_Moveviewer.py --output-dir=./dist --output-filename=SCUFFLE_Editor --remove-output --windows-console-mode=disable --windows-icon-from-ico=.\Data\icon.ico --product-name=SCUFFLE_Editor --file-version=%1 --product-version=%1 --include-data-dir=.\Config=.\Config --include-data-dir=.\Data=.\Data 
move "./dist/GUI_Moveviewer.dist" "./dist/SCUFFLE_Editor"
rmdir /S /Q "./dist/SCUFFLE_Editor/Data/Scripts/Custom/"

cd ./dist
"C:\Program Files\WinRAR\winrar.exe" a -r -m5 -af ./SCUFFLE_Editor_VV_%1.rar ./SCUFFLE_Editor
cd ..