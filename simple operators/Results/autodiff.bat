@echo off
set loopcount=18
:loop
if %loopcount% GEQ 10 goto nextloop
diff ..\Results\Test-0%loopcount%_results.txt ..\Results\0%loopcount%.txt
set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop

:nextloop
diff ..\Results\Test-%loopcount%_results.txt ..\Results\%loopcount%.txt
set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop
:exitloop
pause
