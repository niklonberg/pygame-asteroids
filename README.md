# pygame-asteroids
a simple asteroids game made with pygame.

if on windows and using WSL, requires VcXsrv to be installed
with that done:
turn on xlaunch

run
source venv/bin/activate

then run
export DISPLAY=:0 (or save it in your .zshrc .bashrc file whatever you are using, otherwise you need to run this command every time)
"The export DISPLAY=:0 command sets up communication between your Linux programs (running in WSL) and the Windows display system through VcXsrv."

then run
python3 main.py to start the game

# extension ideas

Add a scoring system  
Implement multiple lives and respawning  
Add an explosion effect for the asteroids  
Add acceleration to the player movement  
Make the objects wrap around the screen instead of disappearing  
Add a background image  
Create different weapon types  
Make the asteroids lumpy instead of perfectly round  
Make the ship have a triangular hit box instead of a circular one  
Add a shield power-up  
Add a speed power-up  
Add bombs that can be dropped  
