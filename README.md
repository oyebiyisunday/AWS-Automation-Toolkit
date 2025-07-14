# AWS Automation Toolkit: Python Solutions for Core Services

This repository provides a ready-to-use Python toolkit for automating key AWS services. Each module targets a core AWS offering, addressing real-world cloud engineering challenges with concise, scriptable solutions.

---

## Contents

### 1. S3 File Manager
- **Task:** Cloud file storage
- **Challenge:** Scalable organization & access control
- **Solution:** Scripted bucket operations  
  *Creates bucket → Uploads file → Lists buckets → Handles conflicts*

### 2. Lambda Invoker
- **Task:** Serverless code execution
- **Challenge:** Event-driven processing
- **Solution:** Direct function triggering  
  *Calls function → Passes payload → Decodes response → Handles missing functions*

### 3. DynamoDB CRUD
- **Task:** NoSQL data management
- **Challenge:** Low-latency schema-less access
- **Solution:** Key-value operations  
  *Creates items → Retrieves by key → Queries partitions*

### 4. CloudFormation Deployer
- **Task:** Infrastructure provisioning
- **Challenge:** Consistent environment setup
- **Solution:** Template-driven deployments  
  *Reads template → Launches stack → Handles IAM capabilities → Catches template errors*

### 5. IAM Role Builder
- **Task:** Secure access delegation
- **Challenge:** Service-to-service permissions
- **Solution:** Trust policy configuration  
  *Creates role → Attaches policies → Returns ARN*

### 6. SNS Broadcaster
- **Task:** Multi-channel notifications
- **Challenge:** Fan-out messaging
- **Solution:** Topic-based publishing  
  *Sends messages → Adds filtering attributes → Returns message ID*

### 7. SQS Processor
- **Task:** Decoupled messaging
- **Challenge:** Async workload handling
- **Solution:** Queue-based coordination  
  *Sends messages → Retrieves batches (long polling) → Deletes after processing*

### 8. Step Functions Orchestrator
- **Task:** Workflow coordination
- **Challenge:** Distributed state management
- **Solution:** State machine execution  
  *Starts workflows → Provides input → Uses unique execution names*

### 9. EC2 Provisioner
- **Task:** Virtual server deployment
- **Challenge:** On-demand compute
- **Solution:** Programmatic instance creation  
  *Launches instances → Applies security → Tags resources → Waits for running state*

### 10. RDS Monitor
- **Task:** Database management
- **Challenge:** SQL instance oversight
- **Solution:** Status reporting  
  *Lists instances → Shows status/engine → Identifies Multi-AZ deployments*

### 11. Kinesis Ingester
- **Task:** Streaming data collection
- **Challenge:** High-volume real-time intake
- **Solution:** Partitioned data writing  
  *Sends records → Uses shard keys → Handles throughput limits*

### 12. CloudWatch Metrics Publisher
- **Task:** Performance tracking
- **Challenge:** Custom monitoring
- **Solution:** Dimensional metric submission  
  *Publishes data → Adds context dimensions → Timestamps entries*

---

## Usage

Each toolkit module is designed for standalone usage or easy integration into your automation workflows.  
**Requirements:** Python 3.8+, [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), and AWS credentials.

```bash
pip install boto3
```

See the code examples in each module for usage patterns and extend as needed for your infrastructure.

---

## License

MIT License

---

*Crafted for reliability, scalability, and clarity in AWS automation.*
