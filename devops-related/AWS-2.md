#### VPC


#### Route53
Provides Domain / DNS related services + health check if needed.

Steps to switch name server with existing Domain
1. Create Hosted Zone in Route53. Enter domain that you own.
2. Confirm 2 records generated after Hosted Zone creation. (NS, SOA)
3. Go visit your Domain provider. In settings, change the name server with data provided by Route53 NS record
4. Check if it has changed well with some sort of DNS Lookup service
5. Add A record, which is your Host (server). Enter your IP.
6. Wait until DNS caching updates. If it doesn't show up for too long (it WILL take time, but usually a day or two should be enough.) if your settings were right with DNS Lookup or flush your cache (PC, browser, etc).
