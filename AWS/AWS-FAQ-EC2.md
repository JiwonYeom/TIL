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



