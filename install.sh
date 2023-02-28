#!/bin/sh

sudo apt update
sudo apt install -y python3
mkdir ~/.deploy
echo "alias env_generator='python3 ~/.deploy/env_generator/index.py'" >> ~/.bashrc
cp -r ~/env_generator ~/.deploy
cd ~
source .bashrc
sudo rm -rf ~/env_generator