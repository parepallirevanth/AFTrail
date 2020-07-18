#sudo apt-get update
cd $(dirname $0)
cd ../
#comment
#rebuild Dockerfiles and runing
sudo docker-compose up -d --build
