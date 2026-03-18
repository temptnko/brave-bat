#!/bin/bash
#updating system
apt -y update && apt -y upgrade

#installing python3 and libraries
#---------------------------------
apt install python3-venv

python3 -m venv myenv

source myenv/bin/activate

pip install pyautogui selenium webdriver-manager
#--------------------------------

#making the words to search
echo "angry-birds, jeans, GANT, VPN, 
Quantum, Fungi, Asteroid, Cryptocurrency, 
Bioluminescence, Ecosystem, Blockchain, 
Kaleidoscope, Tesseract, Nanotechnology, 
Mindfulness, Symbiosis, Photovoltaic, Augmented, 
Fractal, Luminance, Cryptocurrency, Hologram, 
Epigenetics, Metaverse" > search.txt

#brave installation
#------------------------------------
apt install -y curl

curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg

curl -fsSLo /etc/apt/sources.list.d/brave-browser-release.sources https://brave-browser-apt-release.s3.brave.com/brave-browser.sources

apt update

apt install -y brave-browser
#----------------------------------

#link wallet database
rm -rf ~/.config/BraveSoftware/Brave-Browser/BraveWallet/*

cp ~/bat/1.0.227 ~/.config/BraveSoftware/Brave-Browser/BraveWallet/
#-------------------------------------------
#giving permissions
chmod +x bat.py

#launching the .py script
python3 bat.py