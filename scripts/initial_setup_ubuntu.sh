#!/bin/bash

# Change hostname and take screenshot
sudo hostnamectl set-hostname VK521


# Install Apache Web Server and take screenshot
sudo apt update
sudo apt upgrade

sudo apt install python3

sudo apt install mariadb-server


sudo apt install openjdk-11-jdk

sudo apt install r-base

wget https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz
tar -xvzf spark-3.5.1-bin-hadoop3.tgz

mv spark-3.5.1-bin-hadoop3 spark

#!/bin/bash

# Define the environment variables
JAVA_HOME="export JAVA_HOME=/usr"
SPARK_HOME="export SPARK_HOME=/home/vagrant/spark"
PYSPARK_PYTHON="export PYSPARK_PYTHON=python3"
PATH_UPDATE="export PATH=\$PATH:\$SPARK_HOME/bin"

# File path to the .bashrc file
BASHRC_FILE="/home/vagrant/.bashrc"

# Function to add environment variables if they don't already exist
add_to_bashrc() {
    # Check if the environment variable is already in the .bashrc file
    if ! grep -Fxq "$1" "$BASHRC_FILE"; then
        echo "$1" >> "$BASHRC_FILE"
        echo "$1 added to .bashrc"
    else
        echo "$1 is already present in .bashrc"
    fi
}

# Add environment variables to .bashrc
add_to_bashrc "$JAVA_HOME"
add_to_bashrc "$SPARK_HOME"
add_to_bashrc "$PYSPARK_PYTHON"
add_to_bashrc "$PATH_UPDATE"

# Apply the changes
source ~/.bashrc

echo "Environment variables have been set and sourced."

# The first command is to set the user.name for each commmit
git config --global user.name MidhunSaiVinay
# The second command is to set the user.email for each commit
git config --global user.email midhunsaivinay@gmail.com
sudo apt-get update
sudo apt-get install apt-transport-https curl gnupg -yqq
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo -H gpg --no-default-keyring --keyring gnupg-ring:/etc/apt/trusted.gpg.d/scalasbt-release.gpg --import
sudo chmod 644 /etc/apt/trusted.gpg.d/scalasbt-release.gpg
sudo apt-get update
sudo apt-get install sbt



# Check if the SSH key already exists
if [ ! -f ~/.ssh/id_rsa ]; then
    ssh-keygen -t ed25519 -f ~/.ssh/id_rsa -N ""
    echo "SSH key generated for $SSH_KEY_EMAIL."

    # Start the ssh-agent in the background
    eval "$(ssh-agent -s)"

    # Add the SSH private key to the ssh-agent
    ssh-add ~/.ssh/id_rsa
    echo "SSH key added to ssh-agent."

    # Print the SSH public key (you will need to manually add it to GitHub)
    echo "Add the following SSH key to GitHub:"
    cat ~/.ssh/id_rsa.pub
else
    echo "SSH key already exists."
fi

# Instructions for adding SSH key to GitHub
echo -e "\nTo complete the setup, follow these steps:"
echo "1. Copy the above SSH key."
echo "2. Go to https://github.com/settings/keys."
echo "3. Click 'New SSH key', provide a title, and paste the key."
