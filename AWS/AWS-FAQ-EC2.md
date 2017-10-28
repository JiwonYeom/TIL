## AWS FAQ EC2 summaries
Studying for AWS Certified SAA. Summaries on parts that I didn't know + likely important. Possibly messy since it's for my own study!

* if you want to run 20+ instances, complete the request form

* RunInstances API / DescribeInstances API / TerminateInstances API

* EBS boot partition --> `StopInstances` API to release resources but preserve data. `StartIncetances` to restart.

* local instance storage is temporary, but if this is used as a clone, it could be useful

* typically less than 10 mins to run. Dependent to size of AMI, number of instances, how recently that AMI was launched.

* EC2 is joint with S3 for instance with root devices backed by local instance storage.Load their AMIs into S3, and move them between S3 and EC2. 

* Sending email from EC2 -> default limits exist. Else, request by form.

* Supported OS : Amazon Linux, Ubuntu, Windows, Red Hat Linux, SUSE Linux, Fedora, Debian, EntOS, Gentoo Linux, Oracle Linux, Free BSD

* EC2 uses ECC memory

* EC2 billing starts when EC2 initiates the boot sequence of AMI instance.

* EC2 billing ends when the instance terminates. (shutdown -h") / instance failure

* When YOU stop the instance, hourly usage / data transfer fee  does not change. But EBS volume storages WILL be charged.

* Billable EC2 instance hours : any time your instances are in a "running" state. Billing starts when instance trnasitions into running state.

* When two instances in different AZ communicate, if data is transferred BETWEEN two instances, charged as Out & In.

* Prices include tax? No.

* 5 families of EC2 instances :
    * General Purpose : have memory to CPU ratios suitable for most general purpose applications and come with fixed performance (M4 and M3 instances) or burstable performance (T2)
        * M4,M3,T2
    * Compute Optimized : (C4 and C3 instances) have proportionally more CPU resources than memory (RAM) and are well suited for scale out compute-intensive applications and High Performance Computing (HPC) workloads
        * C4,C3   
    * Memory Optimized :  Memory Optimized Instances (R3 and R4 instances) offer larger memory sizes for memory-intensive applications, including database and memory caching application
        * R3,R4
    * GPU : (P2) take advantage of the parallel processing capabilities of NVIDIA Tesla GPUs for high performance parallel computing /  (G3) offer high-performance 3D graphics capabilities for applications using OpenGL and DirectX
        * P2,G3
    * Storage Optimized instances :  I3 and I2 instances that provide very high, low latency, I/O capacity using SSD-based local instance storage for I/O-intensive applications and D2, Dense-storage instances, that provide high storage density and sequential I/O performance for data warehousing, Hadoop and other data-intensive applications
        8 I3,I2,D2

* M1 M3 comparison?
    * M3 : more consistence, SSD-based instance storage, higher I/O, less expensive. Recommended for genera purpose, balance of compute, memory, network resources.
    * M1 for more disk storage

* EC2 Compute Unit
    * Amount of CPU that is allocated to a particular instance. ECU provides relative measure of the integer processing power of an EC2 instance.

* Getting historyof all EC2API calls made on my account for security analysis & operational troubleshootings : turnon `CloudTrail` in AWS console.

* 5 EIP per region. To increase, make special request.

* Configureing reverse DNS record for EIP : fill out form. Notethat DNS record must exist BEFORE they create the reverse DNS record.
> Reverse DNS record : opposite of DNS. maps IP to a domain name. https://www.itworld.com/article/2833006/networking/how-to-setup-reverse-dns-and-ptr-records.html

* Can I make sure I'm in the same AZ as another dev? Currently not supported. One AZ name in two AWS customer accounts may relate to different physical AZ

* transfer data between AZ using public IP --> twice for Regional Data Transfer + public IP? : no. Regional Data Transfer rates once even if both conditions apply

* Networking Capabilities : `SR-IOV`

* Enhanced networking could be useful when high packet-per-second performance, low latency networking

* How to enable : launch HVM AMI. 
    * R4, X1, I3, P2, G3, m4.16xlarge instances provide Elastic Network Adapter (ENA) interface.
    * C3, C4, R3, I2, M4, D2 : Intel® 82599g Virtual Function Interface
    * Amazon Linnux AMI includes both of these drivers by default. 
    * If not included, download & install. 
    * **Enhanced networking is only supported in Amazon VPC**

* No additional fee for enhanced networking.

##### EBS

* EBS volume : SSD backed(transactional) / HDD backed (intensive)

* When using ebs as a root partition, set the Delete On Terminate to "N" to persist.

* EBS snapshots are only available through EC2 APIs

* No need to unmount volumes to take snapshot. But this might exclude local caches. Cleanly detach the volume in order to prevent it.

* Snapshots are given unique identifier.

* shared snapshots no extra charge, cpy of another user's shared volume -> EBS charge

* EBS offers encryption of data volumes and snapshots

* IOPS volume - IOPS maximum 50:1 size. Min 100 IOPS, max 20000 IOPS

* EBS volume to other instance in another AZ : snapshot ->create volume

##### CloudWatch

* Minimum time interval granularity : 1 minute

* disable monitoring -> metrics data can be retrieved as far as 2 weeks. After that data won't be available is the monitoring was diabled.

* terminated EC2 instance or deleted ELB can be accessed

* Custom metric can provide data at at granularity of one second

* Custom metric cane be either standard or high resolution.

* High resolution custom metrics are NOT priced differently from standartd metrics.

* Availabled statistics : retrieve, graph, set alarms.... Average, Sum, Minimum, Maximum, Sample Count. 

* CloudWatch Logs Agent sends data every 5 mins by default

* CloudWatch Logs Agent formats in any text based common log data / JSON-formatted logs

##### Auto Scaling

* Auto scaling speed for upping / downing can be customized.

* Delete auto scaling group -> instances wil be terminated & group will be deleted.

##### ELB

* Classic load balancer : routes based on appliation / network level information. Ideal for simple load ballancig between multiple EC2

* Application load balancer : based on advanced application level information. Microservices, container-based architectures...

##### ETC

* non-production, can be interrupted : spot instance



