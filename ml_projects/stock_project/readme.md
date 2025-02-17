## Overview
This guide outlines how to build a free-tier real-time stock market data pipeline using Kafka, Snowflake, Airflow, Prometheus, and Grafana. Steps include environment setup, code, security considerations, and references to official documentation.

---

## 1. Choose a Free-Tier Cloud VM
- AWS Free Tier EC2: [AWS EC2 Docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- GCP Free Tier Compute VM: [GCP Compute Docs](https://cloud.google.com/compute/docs)

Provision a small VM (e.g., t2.micro on AWS or e2-micro on GCP) to host Kafka, Airflow, Prometheus, and Grafana.

---

## 2. Install and Configure Kafka
1. Download Kafka: [Kafka Docs](https://kafka.apache.org/documentation/)  
2. Run ZooKeeper and Kafka in separate terminal sessions:
    ```bash
    # Start ZooKeeper (default configs)
    bin/zookeeper-server-start.sh config/zookeeper.properties
    # Start Kafka
    bin/kafka-server-start.sh config/server.properties
    ```
3. Configure security (SASL or TLS) using [Kafka Security](https://kafka.apache.org/documentation/#security).

---

## 3. Python Producer to Fetch Stock Data
Use the Yahoo Finance API (via [yfinance](https://pypi.org/project/yfinance/)) to fetch real-time prices, then push to Kafka:
```python
import yfinance as yf
from kafka import KafkaProducer
import json

producer = KafkaProducer(
     bootstrap_servers='YOUR_VM_PUBLIC_IP:9092',
     security_protocol='SASL_PLAINTEXT' # or 'SSL' if configured
)

def fetch_and_send_stock_data(ticker='AAPL'):
     data = yf.download(ticker, period='1d', interval='1m')
     latest = data.tail(1).to_dict('records')[0]
     producer.send('stock_topic', json.dumps(latest).encode('utf-8'))

if __name__ == "__main__":
     fetch_and_send_stock_data()
```
Use IAM roles or service accounts to limit privileges on the VM.

---

## 4. Snowflake Setup and Consumer
1. Sign up for a [Snowflake trial](https://www.snowflake.com/free-trials/) (free-tier credits).
2. Install Snowflake Python connector:
    ```bash
    pip install snowflake-connector-python
    ```
3. Consume messages from Kafka and insert into Snowflake:
    ```python
    from kafka import KafkaConsumer
    import snowflake.connector
    import json

    consumer = KafkaConsumer('stock_topic', bootstrap_servers='YOUR_VM_PUBLIC_IP:9092')
    conn = snowflake.connector.connect(user='SNOWFLAKE_USER', password='SNOWFLAKE_PASS', account='SNOWFLAKE_ACCT')

    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS STOCK_PRICES (SYMBOL STRING, DATETIME TIMESTAMP, PRICE FLOAT)")

    for msg in consumer:
         record = json.loads(msg.value.decode('utf-8'))
         symbol = 'AAPL'
         dt = record['Date']
         price = record['Close']
         insert_sql = f"INSERT INTO STOCK_PRICES VALUES ('{symbol}', '{dt}', {price})"
         cursor.execute(insert_sql)
    ```

---

## 5. Configure Airflow DAG
Install Airflow on the same free-tier VM:
```bash
pip install apache-airflow
airflow db init
airflow users create --username admin --password admin --role Admin --email admin@example.com
airflow webserver -p 8080
airflow scheduler
```
A simple DAG for daily ingestion:
```python
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def fetch_stock_data():
     # Reuse producer code here
     pass

dag = DAG('stock_ingestion', start_date=datetime(2023,1,1), schedule_interval='0 9 * * 1-5')
ingest_task = PythonOperator(task_id='fetch_data', python_callable=fetch_stock_data, dag=dag)
```
Schedule daily or at specific market times.

---

## 6. Snowflake Trend Analysis
Use SQL queries for quick insights:
```sql
-- Top 5 daily closing prices
SELECT SYMBOL, MAX(PRICE) AS MAX_PRICE, DATE(DATETIME) AS TRADE_DATE
FROM STOCK_PRICES
GROUP BY SYMBOL, DATE(DATETIME)
ORDER BY MAX_PRICE DESC
LIMIT 5;

-- Moving average example
SELECT 
  SYMBOL, 
  DATETIME, 
  AVG(PRICE) OVER(ORDER BY DATETIME ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS MA5
FROM STOCK_PRICES;
```
Reference [Snowflake Docs](https://docs.snowflake.com/).

---

## 7. Dashboard with Free Tools
- [Google Looker Studio](https://lookerstudio.google.com/) for connecting to Snowflake.  
- [Streamlit](https://docs.streamlit.io/) for quick interactive dashboards on the same VM.

---

## 8. Monitoring with Prometheus & Grafana
Set up Prometheus and Grafana on the VM:
```bash
# Docker approach (if resources allow)
docker run -d --name prometheus -p 9090:9090 prom/prometheus
docker run -d --name grafana -p 3000:3000 grafana/grafana
```
In Prometheus config, scrape Kafka and VM metrics:
```
scrape_configs:
  - job_name: 'kafka'
     static_configs:
        - targets: ['localhost:9092']
```
Use [Grafana Docs](https://grafana.com/docs/grafana/latest/) for dashboards.

---

## 9. Security Highlights
- Use IAM roles or service accounts to restrict VM access.
- Configure Snowflake RBAC to limit data access.
- Enable Kafka SASL/TLS for secure data transfer.
- Limit inbound firewall rules for SSH/Kafka ports.

---

## 10. Automated Cloud Infrastructure from CLI
You can provision or tear down the entire environment on demand using a simple bash script and AWS CLI. Below is an example snippet to start and stop a free-tier EC2 instance (adjust parameters as needed):
```bash
#!/usr/bin/env bash

# Create EC2 instance
INSTANCE_ID=$(aws ec2 run-instances \
  --image-id ami-0c02fb55956c7d316 \
  --count 1 \
  --instance-type t2.micro \
  --key-name YOUR_KEY_PAIR \
  --security-group-ids YOUR_SG_ID \
  --subnet-id YOUR_SUBNET_ID \
  --query 'Instances[0].InstanceId' \
  --output text)

echo "Created instance with ID: $INSTANCE_ID"

# Wait until instance is running
aws ec2 wait instance-running --instance-ids $INSTANCE_ID

# Run setup commands remotely (e.g., install Kafka, Airflow, etc.) via SSH or remote scripts
# ...

# After you're done, terminate the instance:
# aws ec2 terminate-instances --instance-ids $INSTANCE_ID
# echo "Terminated instance $INSTANCE_ID"
```
Run the script to bring up resources only when needed, keeping costs minimal.

---

## References
- [AWS Free Tier](https://aws.amazon.com/free/)  
- [GCP Free Tier](https://cloud.google.com/free)  
- [Apache Kafka](https://kafka.apache.org/documentation/)  
- [Snowflake](https://docs.snowflake.com/)  
- [Apache Airflow](https://airflow.apache.org/docs/)  
- [Prometheus](https://prometheus.io/docs/introduction/overview/)  
- [Grafana](https://grafana.com/docs/grafana/latest/)  
- [YFinance](https://pypi.org/project/yfinance/)
