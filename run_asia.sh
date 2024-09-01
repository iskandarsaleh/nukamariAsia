#!/bin/bash
sudo docker image build -t asia/nginx .
sudo docker container run -d -p 8085:80 asia/nginx
