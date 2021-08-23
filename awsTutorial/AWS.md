binpack – Place tasks based on the least available amount of CPU or memory. This minimizes the number of instances in use.

random – Place tasks randomly.

spread – Place tasks evenly based on the specified value. Accepted values are attribute key-value pairs, instanceId, or host.

---

Enable DynamoDB Streams and set the value of StreamViewType to NEW_IMAGE. Use Kinesis Adapter in the application to consume streams from DynamoDB

---

default route limit per VPC is 200.
a subnet can only be associated with one route table at a time.
it is definitely possible to modify/edit the main route table.

---

Use the GetTraceSummaries API to get the list of trace IDs of the application and then retrieve the list of traces using BatchGetTraces API.

Use AWS Cognito Identity Pools then enable access to unauthenticated identities.

---

Step #1 Multiply the value of the provisioned RCU by 4 KB

```code
= 10 RCU x 4 KB

= 40

Step #2 To get the number of strong consistency requests, just divide the result of step 1 to 4 KB

Divide the Average Item Size by 4 KB since the scenario requires eventual consistency reads:

= 40 / 4 KB

= 10 strongly consistent reads requests

Step #3 To get the number of eventual consistency requests, just divide the result of step 1 to 2 KB

=40 / 2 KB

= 20 eventually consistent read requests
```

---

AppSync- search it

---

Execute an AWS Lambda function to make the API call triggered by the post-authentication event.

---

```code
// *****************************************
// function that returns a customer's record.
// Attempts to retrieve the record from the cache.
// If it is retrieved, the record is returned to the application.
// If the record is not retrieved from the cache, it is
//    retrieved from the database,
//    added to the cache, and
//    returned to the application
// *****************************************
get_customer(customer_id)

customer_record = cache.get(customer_id)
if (customer_record == null)

customer_record = db.query("SELECT * FROM Customers WHERE id == {0}", customer_id)
cache.set(customer_id, customer_record)

return customer_record
```

---

Using stage variables that can be configured, an API deployment stage
can interact with different backend endpoints. Users can use API Gateway stage variables to reference a single
AWS Lambda function with multiple versions and aliases

---

when your function returns an error, Lambda stops processing any data in the impacted shard and retries the entire batch of records. These records are continuously retried until they are successfully processed by Lambda or expired by the event source.

ref: https://aws.amazon.com/about-aws/whats-new/2019/11/aws-lambda-supports-failure-handling-features-for-kinesis-and-dynamodb-event-sources/?nc1=h_ls

---

configuration files are YAML- or JSON-formatted documents with a .config file extension that you place in a folder named .ebextensions and deploy in your application source bundle-
as the healthcheckurl.yaml file should be renamed to healthcheckurl.config file and placed in the .ebextensions directory to be picked up by Elastic Beanstalk.

---

A Developer is trying to deploy a serverless application using AWS CodeDeploy. The application was updated and needs to be redeployed.
What file does the Developer need to update to push that change through CodeDeploy?- appspec.yml

---

Cloud watch-
Standard resolution, with data having a one-minute granularity
High resolution, with data at a granularity of one second

---

Data at rest == KMS, audit== KMS

---

a global secondary index (GSI) is primarily used if you want to query over the entire table, across all partitions. GSI only supports eventual consistency and not strong consistency.

---

To return the number of write capacity units consumed by any of these operations, set the ReturnConsumedCapacity parameter to one of the following:

TOTAL — returns the total number of write capacity units consumed.

INDEXES — returns the total number of write capacity units consumed, with subtotals for the table and any secondary indexes that were affected by the operation.

NONE — no write capacity details are returned. (This is the default.)

You split shards to increase the capacity (and cost) of your stream. You merge shards to reduce the cost (and capacity) of your stream.

Data will be available within milliseconds to your Amazon Kinesis applications, and those applications will receive data records in the order they were generated.

You can also use metrics to determine which are your “hot” or “cold” shards, that is, shards that are receiving much more data, or much less data, than expected. You could then selectively split the hot shards to increase capacity for the hash keys that target those shards. Similarly, you could merge cold shards to make better use of their unused capacity.

---

API-
For the integration timeout, the range is from 50 milliseconds to 29 seconds for all integration types, including Lambda, Lambda proxy, HTTP, HTTP proxy, and AWS integrations.
the underlying Lambda function has been running for more than 29 seconds causing the API Gateway request to time out.

The API Gateway automatically enabled throttling in peak times which caused the HTTP 504 errors is incorrect because a large number of incoming requests will most likely produce an HTTP 502 or 429 error but not a 504 error

---

For Lambda functions that process Kinesis or DynamoDB streams, the number of shards is the unit of concurrency. If your stream has 100 active shards, there will be at most 100 Lambda function invocations running concurrently. This is because Lambda processes each shard’s events in sequence.

---

If you enable DynamoDB Streams on a table, you can associate the stream ARN with a Lambda function that you write. Immediately after an item in the table is modified, a new record appears in the table’s stream. AWS Lambda polls the stream and invokes your Lambda function synchronously when it detects new stream records.

---

Unlike standard queues, FIFO queues don’t introduce duplicate messages. FIFO queues help you avoid sending duplicates to a queue. If you retry the SendMessage action within the 5-minute deduplication interval, Amazon SQS doesn’t introduce any duplicates into the queue.

---

A Lambda authorizer is an API Gateway feature that uses a Lambda function to control access to your API. When a client makes a request to one of your API’s methods, API Gateway calls your Lambda authorizer, which takes the caller’s identity as input and returns an IAM policy as output.

There are two types of Lambda authorizers:

– A token-based Lambda authorizer (also called a TOKEN authorizer) receives the caller’s identity in a bearer token, such as a JSON Web Token (JWT) or an OAuth token or SAML.

– A request parameter-based Lambda authorizer (also called a REQUEST authorizer) receives the caller’s identity in a combination of headers, query string parameters, stageVariables, and $context variables

---

Cloudformation does not have the rollback feature :
A stack goes into the UPDATE_ROLLBACK_FAILED state when AWS CloudFormation cannot roll back all changes during an update

---

SAM uses CodeDeploy and rollbacks are possible

---

GenerateDataKey returns a plaintext and encrypted data key. Use the plain text key to encrypt the data then delete it

---
