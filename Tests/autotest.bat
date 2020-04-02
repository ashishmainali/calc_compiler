@echo off
set loopcount=18
:loop
if %loopcount% GEQ 10 goto nextloop
echo python3 ..\Template\hmwk_02.py Test-0%loopcount%.txt - ..\Results\0%loopcount%.txt
python3 ..\Template\hmwk_02.py Test-0%loopcount%.txt > ..\Results\0%loopcount%.txt
dos2unix ..\Results\0%loopcount%.txt ..\Results\0%loopcount%.txt
diff ..\Results\Test-0%loopcount%_results.txt ..\Results\0%loopcount%.txt
set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop

:nextloop
echo python3 ..\Template\hmwk_02.py Test-%loopcount%.txt - ..\Results\%loopcount%.txt
python3 ..\Template\hmwk_02.py Test-%loopcount%.txt > ..\Results\%loopcount%.txt
dos2unix ..\Results\%loopcount%.txt ..\Results\%loopcount%.txt
diff ..\Results\Test-%loopcount%_results.txt ..\Results\%loopcount%.txt
set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop
:exitloop
pause
