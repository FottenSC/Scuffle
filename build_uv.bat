del /F /Q "./dist/SCUFFLE" 
uv run nuitka --standalone --enable-plugin=tk-inter ./GUI_Main.py --output-dir=./dist --output-filename=SCUFFLE --remove-output --windows-console-mode=disable --windows-icon-from-ico=.\Data\icon.ico --product-name=SCUFFLE --file-version=%1 --product-version=%1 --include-data-dir=.\Config=.\Config --include-data-dir=.\Data=.\Data 
move "./dist/GUI_Main.dist" "./dist/SCUFFLE"
PAUSE