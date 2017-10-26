## AWS FAQ S3 summaries
Studying for AWS Certified SAA. Summaries on parts that I didn't know + likely important. Possibly messy since it's for my own study!

* Largest object that can be uploaded as single PUT is 5gb. If larger than 100mb, consider using multipart.

* storage classes S3 offer :
    - S3 standard : general purpose & frequently accessed.
    - S3 standard-infrequent access : long-lived but less frequently accessed
    - Glacier : long-erm arcive

* read-after-write consistency for PUTS of new objects & eventual consistency for overwrite PUTs & DELETEs

* If traffic suddenly spikes does not affect pricing and service. 

* S3 SLA provides service credit if monthly uptime percentage is below

* Default bucket limit for AWS account - 100 bucket

* regions  
    * Near customers, data centers, AWS resources
    * remote from other operations for geographic redundanc + DR
    * address specific legal requirements
    * reduce storage costs.

* COPY request + within S3 Region ==> no Data transfer charge

* Controlling access to data : 
    - IAM
    - bucket policy
    - ACL
    - query string authentication

* Data access auditing is supported (optional)

* Options for encrypting : SSE-S3, SSE-C, SSE-KMS, or a client library such as the Amazon S3 Encryption Client.

* VPC Endpoint for S3 : logical entity withiin VPC that allows connectivity only to S3. Routes requests to S4 and responses back to VPC.

* Amazon Macie: AI-powered security service. Machine-learning. 

* Durability
    - Standard - IA : 99.999999999% durability
    - Amazon S3 Standard & Standard - IA redundantly stores objects on multiple devices across multiple facilities.

* S3 checksums : Content-MD5 checksum & cyclic redundancy checks (CRCs)

* Versioning - preserves existing objects for every PUT, POST, COPY, DELETE operation.

* Lifecycle rule setting + versioning alllows rollback for S3.

* Versioning charges :every version of an object stored / requested.

* Retrieval option for objects in Amazon Glacier : Expedited, Standard, Bulk retrievals

* Retrieve 10 GB Glacider per month for free.

* S3 event notifications : 
    - set up triggers to perform actions including transcoding media files when they are uploaded
    - processing data files when they become available
    - synchronizing Amazon S3 objects with other data stores
    - set up event notifications based on object name prefixes and suffixes

#### Storage Management