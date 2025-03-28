#!/bin/bash

source .env

cd $PUBLIC_DIRECTORY

git pull origin main

docker-compose down -v

sleep 5

docker-compose up -d --build