## AWS FAQ S3 summaries
Studying for AWS Certified SAA. Summaries on parts that I didn't know + likely important. Possibly messy since it's for my own study!

- You are still responsible for managing database settings
- customers can run up to 40 RDS DB instances by default. Up to 10 can be Oracle / SQL Server DBs 
- Multi-AZ Failover : RDS flips the canonical name record(CNAME) for DB instance to point at the standby. The standby gets prototed to become new primary.
Failovers comlete within 1/2 mins. Can be affected by large uncommitted transactions.
- Standbys will be provisioned in different AZ in a same REGION
- Read Replica
    - Scale beyond compute or I/O capacity of a single DB instance for read-heavy database worloads.
    - Serving traffic  while the source DB instance is unavailable. 
    - Business reporting / data warehousing scenario
- RDS does not allow direct host access to DB instance via Telnet, SSH, or Windows remote desktop connection
- For DB instance, maximum size of associated storage capacity is 6TB