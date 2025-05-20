sudo apt update
sudo apt install git
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate

git clone https://github.com/deepseek-ai/DeepSeek-V3.git
cd DeepSeek-V3/inference
pip install -r requirements.txt

curl -fsSL https://ollama.com/install.sh | sh
