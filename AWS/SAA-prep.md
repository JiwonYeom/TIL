## Sample questions solutions

- The instance performs a normal shutdown and stops running; its status changes to stopping and then stopped.
- Any Amazon EBS volumes remain attached to the instance, and their data persists.
- Any data stored in the RAM of the host computer or the instance store volumes of the host computer is gone.
- In most cases, the instance is migrated to a new underlying host computer when it’s started.
- Storage gateway: enables on-premises applications to seamlessly use AWS cloud storage.
- Domain in SWF - special type of worker.
- Read replicas are only supported for InnoDB storage engine.
- CloudWatch free tier - 5 mins
- DB Parameter group : manage DB engine configuration. Container for engine configuration values. 
    - If dynamic parameter is changed and saved to the DB parameter group, it is applied immediately.
- Route 53 resource records : tell DNS how to route traffic for the domain
    - route traffic for certain domain to IP address of a host in your data center
    - route email for domain to a mail server
    - route traffic for a subdomain to the IP address of a different host
    - An Alias record can map one DNS name to another Amazon Route 53 DNS name.
    - An Amazon Route 53 CNAME record can point to any DNS record hosted anywhere.
- If using RDS Provisioned IOPS storage, you can scale throughput by specifying IOPS rate from 1000 to 10000
- ec2 placement group : logical grouping of instances within a single AZ. Recommended for applications that benefit from low network latency, high network throughput, or both.