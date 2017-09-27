## VPN network basics

#### Customer Gateway & Amazon VPC
Amazon VPC allows creation of customer gateway through it VPN Connection settings.

Here are overall setting steps for cases of Windows server(as customer gateway) & AWS VPC connection

Basically, There are 2 sides : AWS and your data center.
These two networks get connected through VPN connection, which could be said a secure connection that can even connect to private subnet.

Please refer to first figure you see in [this](http://docs.aws.amazon.com/ko_kr/AmazonVPC/latest/NetworkAdminGuide/Introduction.html) page.

Most likely, two tunnels will be made, which are VPN connections. Generally two or more is needed so that it can prevent complete failure. (If one fails, network can use another tunnel)

In AWS, VPN connection setting allows you to prepare both VPG(Virtual Private Gateway) and Customer Gateway. You just need to know the IP address of your Data Center's to-be gateway.

In my case, I tried it with Windows Server 2012.

Unfortunately I didn't succeed, even though I followed all the steps in [here](http://docs.aws.amazon.com/ko_kr/AmazonVPC/latest/NetworkAdminGuide/customer-gateway-windows-2012.html).
Vitrual Connection didn't get Up'ed. I guess it was some problem in the settings, but since the setting's quite complicated and you should have sufficient knowledge of IP, Private IP, Subnet, CIDR and etc, it wasn't so easy.
