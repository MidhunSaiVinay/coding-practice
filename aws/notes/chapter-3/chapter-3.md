# AWS Data Engineers Toolkit

## Table of Contents
- [Amazon Database Migration Service](#amazon-database-migration-service)
- [Amazon Kinesis for Streaming Data Ingestion](#amazon-kinesis-for-streaming-data-ingestion)
  - [Kinesis Data Firehose](#kinesis-data-firehose)
  - [Kinesis Data Streams](#kinesis-data-streams)
  - [Kinesis Data Analytics](#kinesis-data-analytics)
  - [Kinesis Video Streams](#kinesis-video-streams)
- [Amazon Kinesis Agent](#amazon-kinesis-agent)
- [Amazon Kinesis Firehose](#amazon-kinesis-firehose)
- [Amazon Kinesis Data Streams](#amazon-kinesis-data-streams)
- [Amazon Kinesis Data Analytics](#amazon-kinesis-data-analytics)
- [Amazon Kinesis Video Streams](#amazon-kinesis-video-streams)
- [Amazon MSK for Streaming Data](#amazon-msk-for-streaming-data)
- [Amazon AppFlow for SaaS Data Integration](#amazon-appflow-for-saas-data-integration)
- [AWS Transfer Family](#aws-transfer-family)
- [AWS DataSync for Multi-Source Ingestion](#aws-datasync-for-multi-source-ingestion)
- [AWS Snow Family for Large Data Transfers](#aws-snow-family-for-large-data-transfers)
- [AWS Glue for Data Ingestion](#aws-glue-for-data-ingestion)
- [AWS Lambda for Data Transformation](#aws-lambda-for-data-transformation)
- [AWS Glue ETL Components](#aws-glue-etl-components)
- [AWS Glue DataBrew](#aws-glue-databrew)
- [AWS Glue Data Catalog](#aws-glue-data-catalog)
- [AWS Glue Crawlers](#aws-glue-crawlers)
- [Amazon EMR for Big Data Processing](#amazon-emr-for-big-data-processing)
- [AWS Glue Workflows](#aws-glue-workflows)
- [AWS Step Functions for Complex Workflows](#aws-step-functions-for-complex-workflows)
- [Amazon Managed Workflows for Apache Airflow (MWAA)](#amazon-managed-workflows-for-apache-airflow-mwaa)
- [Amazon Athena for SQL Analytics](#amazon-athena-for-sql-analytics)
- [Amazon Redshift for Data Warehousing](#amazon-redshift-for-data-warehousing)
- [Amazon QuickSight for Data Visualization](#amazon-quicksight-for-data-visualization)

## Amazon Database Migration Service

AWS Database Migration Service (DMS) helps migrate databases with minimal downtime:

* Database engine migrations (Oracle → Aurora PostgreSQL)
* Same-engine replication (on-premises → AWS)
* Database to S3 data lake integration

**Key Features:**

1. **Data Lake Integration**
    * Continuous database replication to S3
    * Full initial load + ongoing updates
    * Supported formats: CSV, Parquet

2. **Change Data Capture (CDC)**
    * Tracks database modifications (Insert/Update/Delete)
    * Adds operation tracking column
    * Example format:
      ```
      Operation, ID, Data...
      I, 1001, "New record"
      U, 1001, "Updated data"
      D, 1001, "Deleted"
      ```

3. **Point-in-Time Recovery**
    * Creates database snapshots
    * Applies CDC updates incrementally
    * Scheduled update jobs

**Deployment Options:**
* Provisioned: Manual instance sizing
* Serverless: Automatic resource management

**Best Used For:**
* Database engine migrations
* Data lake synchronization

**Limitations:**
* May impact source database performance

## Amazon Kinesis for Streaming Data Ingestion

Amazon Kinesis is a managed service for real-time data stream ingestion and processing. It supports various streaming data types including:

* Log files
* Website clickstreams
* IoT data
* Video and audio streams

**Core Kinesis Services:**

### Kinesis Data Firehose

* Ingests streaming data
* Buffers data for configured period
* Writes to targets like:
  * Amazon S3
  * Redshift
  * OpenSearch Service
  * Splunk

### Kinesis Data Streams

* Real-time data stream ingestion
* Custom application processing
* Low latency processing

### Kinesis Data Analytics

* Reads from streaming sources
* Analyzes using:
  * SQL statements
  * Apache Flink code

### Kinesis Video Streams

* Processes video/audio streams
* Handles time-serialized data:
  * Thermal imagery
  * RADAR data

**Additional Tool:**
* Kinesis Agent: Utility for packaging and sending data to Kinesis services

## Amazon Kinesis Agent

Kinesis Agent is a pre-built tool for streaming file data to Kinesis services:

**Key Features:**
* Monitors specified files for changes
* Buffers data (1 sec - 15 min)
* Handles file rotation and checkpointing
* Automatic retries on failure
* JSON conversion capability

**Common Use Cases:**
* Web server log streaming
* Log file analysis
* Real-time event monitoring

**Best For:**
* File-based data streaming
* Log file monitoring
* Near real-time analytics

**Not Recommended For:**
* Direct application events (use KPL/SDK instead)
* IoT device data streaming

## Amazon Kinesis Firehose

Kinesis Firehose is a managed service for streaming data ingestion and delivery:

**Key Features:**
* Near real-time data ingestion
* Automatic data buffering
* Built-in data transformation
* Multiple delivery targets

**Buffer Configuration:**
* Time-based: 1-15 minutes
* Size-based: 1-128 MB
* Triggers on first limit reached

**Data Transformation Options:**
* Convert to Parquet/ORC
* Custom Lambda transformations
* Dynamic partitioning for S3
* Payload-based partitioning

**Common Use Cases:**
* Web clickstream analysis
* Log file streaming
* Data lake/warehouse ingestion

**Best Used For:**
* Buffered streaming delivery
* S3/Redshift/OpenSearch targets
* Third-party service integration

**Not Recommended For:**
* Low-latency processing
* Custom delivery targets
* Direct stream processing

## Amazon Kinesis Data Streams

Kinesis Data Streams provides real-time data streaming with sub-second latency:

**Key Features:**
* ~70ms data availability latency
* Terabyte-scale data ingestion
* Multiple consumer support
* Real-time data processing

**Input Options:**
* Kinesis Agent (for log files)
* AWS SDK (lowest latency)
* Kinesis Producer Library (KPL)
    * High throughput
    * Enhanced monitoring
    * KCL integration

**Consumer Options:**
* Other Kinesis services
* AWS Lambda functions
* EC2 server clusters with KCL
    * Automated load balancing
    * Failure handling
    * Processing checkpoints
    * Shard management

**Capacity Modes:**
* Provisioned: Manual shard management
* On-Demand: Automatic scaling

**Best Used For:**
* Real-time processing needs
* Custom processing applications
* High-availability clusters

**Not Recommended For:**
* Simple data delivery workflows
* Apache Kafka migrations (use MSK)

## Amazon Kinesis Data Analytics

Kinesis Data Analytics enables real-time stream processing using Apache Flink:

**Key Features:**
* Apache Flink application support
* Real-time metric extraction
* Rolling time window analysis
* SQL query capability

**Common Use Cases:**
* E-commerce clickstream analysis
* Real-time sales metrics
* Promotional impact tracking
* Time-based aggregations

**Processing Options:**
* SQL queries
* Custom Flink applications
* Built-in analytical functions
* Time-based windowing

**Best Used For:**
* Rolling metric calculations
* Time-series analysis
* Existing Flink applications
* Stream-to-stream processing

**Not Recommended For:**
* Simple data delivery
* Batch processing
* Static data analysis

## Amazon Kinesis Video Streams

Kinesis Video Streams manages video and time-series data ingestion at scale:

**Key Features:**
* Automatic infrastructure scaling
* Live and on-demand playback
* Computer vision integration
* Multi-source ingestion

**Common Use Cases:**
* Video doorbell systems
* Security camera feeds
* Baby monitors
* RADAR data processing
* Thermal imagery analysis

**Core Capabilities:**
* Real-time streaming
* API service integration
* Video analytics support
* Millions of concurrent sources

**Best Used For:**
* Streaming media applications
* Live video processing
* Time-series data analysis
* IoT camera integration

**Not Recommended For:**
* Static file storage
* Basic data streaming
* Non-time-series data

## Amazon MSK for Streaming Data

Amazon MSK is AWS's managed Apache Kafka service offering:

**Key Features:**
* Automated cluster management
* Multi-AZ deployment
* Automatic component replacement
* OS/application updates
* AWS service integration

**Deployment Options:**
1. **Provisioned Clusters**
    * Manual capacity planning
    * Specified compute/storage

2. **Serverless Clusters**
    * Automatic scaling
    * Best for variable workloads
    * Pay-per-use pricing

**Best Used For:**
* Existing Kafka migrations
* Open-source requirements
* Third-party integrations
* Cross-platform compatibility

**Not Recommended For:**
* New AWS-native solutions
* Simple streaming needs
* AWS-only deployments

## Amazon AppFlow for SaaS Data Integration

Amazon AppFlow enables automated data flows between SaaS applications and AWS services:

**Key Features:**
* 50+ pre-built connectors
* Scheduled or event-triggered flows
* Basic data transformations
* Secure data transfer

**Common Sources:**
* Salesforce
* Google Analytics
* ServiceNow
* Slack
* GitHub
* LinkedIn

**Destination Options:**
* Amazon S3
* Amazon Redshift
* Amazon EventBridge
* Supported SaaS platforms

**Data Operations:**
* Field filtering
* Data masking
* Field validation
* Basic calculations

**Best Used For:**
* SaaS data integration
* Automated workflows
* Simple transformations
* Scheduled data sync

**Not Recommended For:**
* Complex transformations
* Unsupported sources
* Custom protocols

## AWS Transfer Family

AWS Transfer Family provides managed file transfer services using common protocols (FTP, SFTP, FTPS, AS2):

**Key Features:**
* Direct S3 integration
* Multiple protocol support
* Identity management
* Automated scaling

**Common Use Cases:**
* MLS file transfers
* EDI data exchange
* Partner data ingestion
* Legacy system integration

**Core Benefits:**
* Minimal migration effort
* Immediate S3 availability
* Managed infrastructure
* Existing protocol support

**Best Used For:**
* Legacy protocol requirements
* Partner data exchange
* Direct S3 integration
* Regulated data transfers

**Not Recommended For:**
* Multi-cloud requirements
* Cost-sensitive workloads
* Modern API integrations

## AWS DataSync for Multi-Source Ingestion

AWS DataSync enables efficient data transfer from on-premises and multi-cloud sources:

**Key Features:**
* High-performance data transfer
* Support for multiple protocols:
    * NFS
    * SMB
    * S3-compatible systems
    * HDFS
* Multi-cloud support:
    * Azure Blob Storage
    * Google Cloud Storage

**Target Options:**
* Amazon S3
* Amazon EFS

**Common Use Cases:**
* End-of-day transaction syncing
* Historical data migration
* On-premises data lake transfer
* Multi-cloud data consolidation

**Best Used For:**
* Network-based data transfers
* Compatible storage systems
* Regular data syncing
* Cross-cloud migration

**Not Recommended For:**
* Very large datasets (use Snow Family)
* Incompatible storage systems
* Real-time data streaming

## AWS Snow Family for Large Data Transfers

AWS Snow Family offers secure, physical devices for large-scale data transfer and edge computing:

**Available Devices:**
* Snowcone: 8-14TB storage, 2 vCPU, 4GB RAM
* Snowball Edge:
    * Compute-optimized: 28TB SSD, optional NVIDIA GPU
    * Storage-optimized: 210TB SSD

**Key Features:**
* Ruggedized hardware design
* TPM security modules
* Data encryption at rest
* Edge computing capability
* Local network transfer

**Common Use Cases:**
* Large dataset migration
* Remote location data transfer
* Edge computing deployments
* Factory IoT processing

**Best Used For:**
* Very large data volumes
* Poor network connectivity
* Remote processing needs
* Secure data transfer

**Not Recommended For:**
* Small datasets
* Good network availability
* Real-time requirements
* Frequent small transfers

## AWS Glue for Data Ingestion

AWS Glue provides serverless Apache Spark-based data ingestion and transformation:

**Key Features:**
* Built-in source connectors
* AWS Marketplace connectors
* Apache Spark environment
* Serverless operation

**Connector Types:**
1. **Built-in Connectors**
    * Amazon RDS
    * Amazon Redshift
    * Amazon DocumentDB
    * MongoDB/Atlas
    * JDBC sources

2. **AWS Marketplace Connectors**
    * AWS-provided (free)
      * Google BigQuery
    * Third-party (subscription)
      * CData Salesforce

**Best Used For:**
* Custom ETL workflows
* Complex data transformations
* Unsupported data sources
* Spark-based processing

**Not Recommended For:**
* Simple data transfers
* Supported AWS services
* Real-time streaming
* Cost-sensitive ingestion

## AWS Lambda for Data Transformation

AWS Lambda enables serverless code execution for light data transformations:

**Key Features:**
* 1ms billing increments
* Up to 15 minutes runtime
* Maximum 10GB memory
* Massive parallel scaling
* Multiple language support

**Common Data Use Cases:**
* CSV file validation
* Stream processing
* ZIP file extraction
* XML parsing
* Parquet conversion

**Scaling Capabilities:**
* Auto-scaling to thousands/second
* Default 1,000 concurrent limit
* Increasable to tens of thousands
* Per-region quota management

**Best Used For:**
* Light data transformation
* File validation
* Stream processing
* Parallel workloads

**Not Recommended For:**
* Long-running processes
* Heavy computational tasks
* Large file processing
* Cost-sensitive workloads

## AWS Glue ETL Components

AWS Glue offers serverless data processing through multiple engines:

**Processing Engines:**
1. **Glue Spark**
    * Distributed processing
    * In-memory computation
    * Multi-node clusters
    * Supports existing Spark code
    * Optional Glue ETL libraries

2. **Glue Python Shell**
    * Single-node processing
    * Python-based tasks
    * Smaller dataset processing
    * Data science workloads

**Key Capabilities:**
* Serverless operation
* Data Processing Unit (DPU) based
* S3 data integration
* Glue Data Catalog support
* Spark Streaming support

**Development Options:**
* Direct Spark code writing
* GUI-based Glue Studio
* Visual ETL editor
* Code generation

**Best Used For:**
* Large dataset processing
* Complex ETL workflows
* Data transformations
* Stream processing

**Not Recommended For:**
* Simple data moves
* Cost-sensitive workloads
* Real-time requirements

## AWS Glue DataBrew

AWS Glue DataBrew is a visual data preparation tool with serverless architecture:

**Key Features:**
* 250+ built-in transformations
* No-code data preparation
* Visual recipe creation
* Data profiling capabilities
* Data quality monitoring

**Common Transformations:**
* Data formatting
* PII data obfuscation
* Column operations
* Timezone conversions
* Outlier detection/removal

**Core Capabilities:**
* Profile job execution
* PII detection
* Data masking
* Encryption options
* Hash generation

**Best Used For:**
* Data analyst workflows
* Data scientist preparation
* Data cleaning tasks
* Visual transformation needs

**Not Recommended For:**
* Complex ETL requirements
* Custom transformation logic
* Code-first approaches

## AWS Glue Data Catalog

AWS Glue Data Catalog provides a unified metadata repository compatible with Apache Hive metastore:

**Key Features:**
* Unified metadata repository
* Hive metastore compatibility
* Automatic schema inference
* Table/database organization
* S3 data integration

**Core Components:**
1. **Databases**
    * Logical groupings
    * Namespace containers
    * Multiple table collections

2. **Tables**
    * Schema definitions
    * Column metadata
    * Data type information
    * S3 location references
    * File format details

**AWS Service Integration:**
* Amazon Athena
* Amazon EMR
* AWS Glue ETL
* Amazon Redshift Spectrum

**Best Used For:**
* Data lake organization
* SQL query enablement
* ETL job references
* Cross-service metadata sharing

**Not Recommended For:**
* Business metadata management
* Document management
* Non-technical catalogs

## AWS Glue Crawlers

AWS Glue Crawlers automatically discover and catalog data source metadata:

**Key Features:**
* Automatic schema inference
* Multiple source support
* Classifier-based detection
* Scheduled execution
* Incremental updates

**Common Sources:**
* Amazon S3
* Database tables
* Data streams
* Local files

**Core Functions:**
1. **Schema Detection**
    * Column names
    * Data types
    * File formats
    * Data patterns

2. **Metadata Management**
    * Automatic catalog updates
    * Database creation
    * Table registration
    * Schema evolution

**Best Used For:**
* Automated cataloging
* Schema discovery
* Data lake organization
* Format detection

**Not Recommended For:**
* Real-time updates
* Custom schema needs
* Small data volumes

## Amazon EMR for Big Data Processing

Amazon EMR offers managed big data processing with multiple deployment options:

**Key Features:**
* Multiple processing engines support
* Auto-scaling capabilities
* Managed infrastructure
* Multiple deployment modes

**Deployment Options:**

1. **EMR Provisioned (EC2)**
    * Full cluster control
    * Custom instance selection
    * Multiple application support
    * Detailed configuration
    * Lowest cost option

2. **EMR on EKS**
    * Container-based deployment
    * Existing EKS integration
    * Spark workload focus
    * Container orchestration

3. **EMR Serverless**
    * Spark/Hive support
    * No instance management
    * CPU/memory limits
    * Optional warm pools
    * Per-job billing

**Cluster Components (EC2):**
* Master node (required)
* Core nodes (1+ required)
* Task nodes (optional)

**Best Used For:**
* Complex big data processing
* Multi-application needs
* Performance optimization
* Cost-sensitive workloads

**Comparison with Glue:**
* More configuration control
* Lower processing costs
* Broader application support
* Requires more expertise

## AWS Glue Workflows

AWS Glue Workflows orchestrates Glue components for data pipeline management:

**Key Features:**
* Sequential step execution
* State information sharing
* Visual workflow builder
* Glue component integration
* Automated dependencies

**Supported Components:**
* Glue Crawlers
* Glue ETL Jobs (Spark/Python)
* State tracking between steps

**Common Workflow Pattern:**
1. Crawler catalogs raw data
2. ETL job transforms data
3. Crawler updates catalog

**Key Capabilities:**
* State information passing
* Dependency management
* Visual orchestration
* Status monitoring
* Error handling

**Best Used For:**
* Glue-only pipelines
* Sequential processing
* Data lake workflows
* Catalog management

**Limitations:**
* Glue components only
* No external service integration
* Basic orchestration needs

## AWS Step Functions for Complex Workflows

AWS Step Functions provides serverless orchestration for complex data pipelines:

**Key Features:**
* 220+ AWS service integrations
* Serverless architecture
* Visual workflow builder
* JSON-based state machines
* Usage-based pricing

**Workflow Definition:**
* Amazon States Language (ASL)
* JSON-based definitions
* Visual Studio interface
* Drag-and-drop creation
* State machine structure

**State Types:**
* Task execution
* Choice branching
* Wait states
* Loop controls
* Parallel execution

**Triggering Options:**
* Amazon EventBridge
* API Gateway
* AWS CodePipeline
* IoT Rules Engine
* Direct API calls

**Best Used For:**
* Complex workflows
* Multi-service orchestration
* Visual pipeline design
* Event-driven processes

**Not Recommended For:**
* Simple sequential tasks
* Single-service workflows
* Cost-sensitive operations

## Amazon Managed Workflows for Apache Airflow (MWAA)

Amazon MWAA provides managed Apache Airflow for workflow orchestration:

**Key Components:**
1. **Scheduler**
    * Multithreaded Python process
    * Task scheduling control
    * Execution management

2. **Worker/Executor**
    * Task execution
    * Auto-scaling capability
    * VPC integration
    * Configurable worker limits

3. **Meta-database**
    * Task status tracking
    * Service account operation
    * Environment-specific instance

4. **Web Server**
    * Web-based monitoring
    * Task execution interface
    * Service account operation

**Core Features:**
* Automated Airflow deployment
* Automatic scaling
* VPC networking
* Environment isolation
* Python-based workflows

**Environment Sizing:**
* Small/Medium/Large options
* Fixed core environment cost
* Storage-based charging
* Worker usage billing

**Best Used For:**
* Existing Airflow migrations
* Complex workflow orchestration
* Teams with Airflow experience
* Multi-cloud integrations

**Not Recommended For:**
* Cost-sensitive workloads
* Simple sequential tasks
* Serverless requirements

## Amazon Athena for SQL Analytics

Amazon Athena provides serverless SQL querying for data lakes:

**Key Features:**
* Serverless architecture
* Standard SQL support
* Direct S3 data querying
* Glue Data Catalog integration
* Multiple connection options

**Query Interfaces:**
* AWS Management Console
* JDBC driver support
* ODBC driver support
* API integration

**Federated Query Capabilities:**
* DynamoDB connectivity
* RDS database access
* CloudWatch Logs querying
* Cross-source joins

**Athena for Apache Spark:**
* Jupyter notebook integration
* Spark job execution
* Interactive data analysis
* Console-based development

**Best Used For:**
* Data lake exploration
* SQL-based analytics
* Ad-hoc querying
* Multi-source analysis

**Not Recommended For:**
* Transactional workloads
* Real-time queries
* Complex transformations

## Amazon Redshift for Data Warehousing

Amazon Redshift provides cloud-based data warehousing optimized for OLAP workloads:

**Core Components:**
1. **Leader Node**
    * Query planning/optimization
    * Client connections (JDBC/ODBC)
    * Query distribution
    * Results aggregation

2. **Compute Nodes**
    * Parallel query execution
    * Local data processing
    * Data storage management
    * Query optimization

**Storage Options:**
* Local SSD cache
* Redshift Managed Storage (RMS)
* S3 via Redshift Spectrum

**Redshift Spectrum Features:**
* External S3 data querying
* Glue Data Catalog integration
* Serverless compute layer
* Multiple format support:
    * JSON
    * CSV
    * Parquet

**Best Used For:**
* Complex analytical queries
* Large dataset processing
* Regular reporting needs
* Multi-table joins

**Not Recommended For:**
* Transactional processing
* Real-time queries
* Small datasets
* Simple analytics

## Amazon QuickSight for Data Visualization

Amazon QuickSight is a serverless business intelligence service for creating interactive data visualizations:

**Key Features:**
* Interactive dashboards
* Drill-down capabilities
* Multi-source data integration
* Serverless architecture
* User-based pricing

**User Types:**
1. **Authors**
    * Create visualizations
    * Configure data sources
    * Design dashboards
    * Set up analyses

2. **Readers**
    * View dashboards
    * Apply filters
    * Drill into details
    * Export data

**Data Source Integration:**
* Amazon S3
* Amazon Athena
* Amazon Redshift
* RDS databases
* Third-party sources

**Common Use Cases:**
* Sales analytics
* Business reporting
* KPI monitoring
* Performance tracking
* Trend analysis

**Best Used For:**
* Business intelligence
* Interactive reporting
* Data exploration
* Visual analytics

**Not Recommended For:**
* Static reporting
* Complex calculations
* Raw data analysis
* Small data volumes

