#!/bin/bash

# git clone git@github.com:theronj60/project-red-rock.git /home/flask_app

sudo apt install nginx

# sudo nano /etc/nginx/sites-enabled/flask_app # create this

echo "server {
    listen 80;
    server_name 192.0.2.0;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}" > /etc/nginx/sites-enabled/flask_app

sudo unlink /etc/nginx/sites-enabled/default

sudo nginx -s reload

sudo apt update && sudo apt upgrade

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update

sudo apt install python3.11

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 110 &&\
	sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 100

# node and npm through nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
# restart terminal
nvm install --lts

# yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update
sudo apt-get install yarn
yarn --version

echo "Please run sudo update-alternatives --config python3 select version"

echo "Then check version then run sudo apt install python3-pip"
