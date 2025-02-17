ssh -i "stock_vm.pem" ubuntu@ec2-18-225-255-25.us-east-2.compute.amazonaws.com
sudo apt update
sudo apt install -y openjdk-11-jdk
cd /opt
sudo wget https://downloads.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
tar -xvzf kafka_2.13-3.9.0.tgz