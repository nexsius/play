if exist "dest\tool.exe" (
   REN "dest\tool.exe" "launcher.exe"
)
COPY src\*  dest\ /Y
DEL /F /Q src\*.* 
dest\launcher.exe

