@echo off
::iterations
set iter=20
:loop

::Put your command here 

set /a iter=iter-1
if %iter%==0 goto exitloop
goto loop
:exitloop
pause