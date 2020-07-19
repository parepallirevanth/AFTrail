#sudo apt-get update
cd $(dirname $0)
cd ../
#rebuild Dockerfiles and runing
sudo docker-compose up -d --build
