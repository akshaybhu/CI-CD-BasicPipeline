#!/bin/bash

BASE_DIR="/home/ec2-user/CI-CD-BasicPipeline"

if [ ! -d "$BASE_DIR" ]; then
    echo "Verify the correct repo name!!"
else
    cd "$BASE_DIR" || exit
    git pull --rebase upstream main
    git push origin main
    sudo service nginx restart
fi
