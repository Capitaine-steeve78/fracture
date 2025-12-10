@echo off
setlocal

set BASE=%~dp0

"%BASE%FractureEnv\Scripts\python.exe" "%BASE%fracture.py" %1

endlocal
