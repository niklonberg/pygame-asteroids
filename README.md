# pygame-asteroids
a simple asteroids game made with pygame.

if on windows and using WSL, requires VcXsrv to be installed
with that done:
turn on xlaunch

run
source venv/bin/activate

then run
export DISPLAY=:0
"The export DISPLAY=:0 command sets up communication between your Linux programs (running in WSL) and the Windows display system through VcXsrv."

then run
python3 main.py to start the game