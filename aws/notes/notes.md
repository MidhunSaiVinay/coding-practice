# AWS Data Engineering
 ## Data lake architecture
![Data lake architecture diagram](images/data-lake-architecture.png)

## implementation

To create 
aws buckets for storage layer
There are landing zone clean zone and curtaled zone 
```bash
aws s3 mb s3://aws-dataengineering-clean-zone
aws s3 mb s3://aws-dataengineering-curated-zone
aws s3 mb s3://aws-dataengineering-landing-zone

```

