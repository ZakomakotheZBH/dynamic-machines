@echo off
setx PATH "%PATH%;%CD%"
assoc .zewpolbin=ZewpolBinFile
ftype ZewpolBinFile=python.exe "%CD%\dmc.py" "%%1"
echo .zewpolbin files are now registered!
