#!/bin/bash

source .env

cd $PUBLIC_DIRECTORY

git pull origin main

docker-compose up -d --build