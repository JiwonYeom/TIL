## PacktPub eBook Learning AWS Quick Skim
#### Cloud service models
* Iaas (Infrastructure as a Service) - Users deploy & run their own apps on a service that they can control provision processing, storage, network resources. Traditional in-premise, virtual server provisioning.
* Paas (Platform as a Service) - service provider takes control of most services. Customer takes leverage of these to build their apps, focusing on app functions
* Saas (Software as a Service) - Typically third-party providers provides subscribe-based services to their users. Customers focus on content management and customize provided service

##### Designing Cloud Application
* Multi-tier architecture
* UI tier, app/business tier, data tier. OR commonly web server, app server, database
* Usually supports auto-scaling & load balancing
Implements master-slave DB model

##### Multi-tenacy
* cost saving by infra sharing & efficiency in managing single instance of application across multiple customers / tenants.
* This is a complex design.
* Issue in a tenant can lead to issues in other tenants
share-nothing to share-everything

##### Designing for Failure
* Assume that things will fail.
* Assume that hardware will fail. Cloud Data center outages. Database failure. Transaction exceeded. etc.
Minimize human / manual intervention. Ex) Use AWS CloudFormation to install,configure,start application.
Key principles
* Do not store app state on your servers. You will lose them. Sessions should never be stored to local file systems.
* Logging should always be stored in a centralized location (ex. DB or third-party logging service)
* Log records should contain additional cloud-specific info (instance ID, region, AZ, tenant ID...etc) Include application-specific sequence of calls or requests if possible. Use tools for viewing, searching, and filtering logs for big logs.
* If a request fails on server (5xx error), you should try cloud provider's SDK features for retry logics. You should log the retry attempts too. If retry attempts are too many, consider reviewing infrastructure size.

#### AWS Components, Cost Model, Application Development Environments
* Optimizing cloud infrastructure costs
    * Choose right size for EC2 (size, type, available network bandwidth)
    * Turn off unused instances
    * Use Auto Scaling
    * Use reserved instances - can help save 50-60% or higher on our instance costs.
    * Use spot instances - you can set maximum price that is much lower than regular on-demand price, and when Amazon has extra capacity, they can provide you. This means your instance will be terminated when it becomes unavailable, but building a correct fail-over will prevent your service from being affected.
    * Use S3 storage class - RRS(Reduced Redundancy Storage) option in S3 can reduce cost by storing non-critical and easily restorable data at lower levels of redundancy than standard option. It stores data in multiple facilities and on multiple devices, but replicated fewer times (99.99% durability)
    * Amazon glacier can be used for storing backups and archiving old data.
    * DB costs - Caching and read replicas can reduce the capacity needed for DB instance. Use spare local RAM cache in your app server or Amazon ElastiCache. Amazon SQS can be another option, that will buffer writes that exceed your provisioned capacity.

#### Designing for and Implementing Scalability
* Defining scalability objectives - To achieve scalability, your application architecture must be scalable in order to leverage the services provided by AWS cloud.
    * Application should respond proportionally.
    * Operationally efficient &cost-effective.
* Designing scalable application architectures
    * Use appropriate AWS PaaS services
    * Use scale-put approach - this allows you to distribute application components, partition your data, and follow a service-oriented design strategy.
    * Implement loosely coupled components. - SQS ensures app will perform in sitaution of high concurrency, unpredictable loads, and/or load spikes. Make your components stateless as possible.
    * Implement asynch processing - ensure you include enough logs for troubleshooting. Also, AWS Kinesis data streams can help you create asynch pipelines
* Leveraging AWS infrastructure services for scalability
    * CloudFront to distribute content - static contents should be delivered through CloudFront CDN
    * AWS ELB to scale.
    * AWS CloudWatch to implement auto scaling
    * Scaling data services
    * Scaling proactively - keep track of traffic patterns or events and use that information to proactively plan scaling.
    
#### Designing for and implementing High Availability
* Define availability objectives - Things are to fail at some point. Set a clear object to keep.
* Nature of failures
    * VPC for high availability
        * carefully select your primary site and DR site. Primary site to closest towards your customers, and DR to the closes region or different country.
        * Set up network topology.
        * Public facing servers -> public subnet. DB server & other app servers -> private subnet
        choose different sets of IP addresses across different regions (multi-region deployment)
        * Appropriate routing table and ACL should be defined
        Define primary & secondary tunnels.
        * Set up gateway servers and NAT, to act as gatekeepers. Gateway --> public subnet. NAT–>private subnet.
    * ELB & Route53
        * Instance availability - never run a single instance in a production enviroinment. Run multiple EC2 instances and put ELB in front.
    * Zonal availability / availability zone redundancy  - Very important to run your application stack in more than one zone. But makesure component level dependencies across zones could lead to latencies / failures.  
    * Regional availability / regional redundancy - ELB and Route 53 supports single application across multiple regions.
    * High availability for application & data layer
        * AWS OpsWorks provide a good recovery mechanism. Auto healing -> if layer/instance becomes unhealthy, OpsWorks terminates the instance and starts a new one.
        * Cold starts from preconfigured images / warm start from scaled down instances in a secondary region
        * Stateless & micro-service oriented architecture can help. In this design service failure is contained / isolated to that service while the rest of your application service runs normally.
        * User / session information should be stored in central location such as ElastiCache & distribute it across multi AZ
        * Rigorous implementation of exception handling code
