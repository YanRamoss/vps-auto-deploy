#!/bin/bash

source .env

cd $PUBLIC_DIRECTORY

git pull origin main

docker-compose build --no-cache

sleep 60

docker-compose up -d