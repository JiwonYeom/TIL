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
