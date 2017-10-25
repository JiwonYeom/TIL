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
