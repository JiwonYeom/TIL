## Steps of replicating DB from on-premise to RDS
======= THIS PAGE MIGHT BE MIGRATED TO BLOG LATER =======

Please refer to [this](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.External.Repl.html) document for official guidelines. I will be discussing only tips I gained while I was doing this.

* You will have to set unique server id in your `/etc/my.cnf` file. Add the following part

```BASH
[mysqld]
log-bin=mysql-bin
server-id=1
```

* In the official document, step 6 (creating user and granting permission) could be confusing if you are a complete newbie in server and all (which is me!!), and I made a mistake by creating and granting permission to a dedicated user for replication in AWS RDS.

This might sound stupid, but I know some of the newcomers will be making same mistake as mine, so here goes.

User that is going to be used in the replication process should be made from the MASTER server, not SLAVE server.
This means the master server will *recognize* the user from that domain you assign. Which means:

```BASH
CREATE USER 'repl_user'@'mydomain.com' IDENTIFIED BY '<password>';
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'mydomain.com' IDENTIFIED BY '<password>';
```

You will have to run this
1. In your **master** server.
2. That *'mydomain.com'* part is host of RDS server. In other words, the **RDS hostname**, or its IP address. I don't know about others, but the term 'mydoman' can be confusing. I put literally my server's domain in first place.

Other parts are pretty straightforward, so you should be okay.

* In official document, step 8 can be ANOTHER confusing part. The `mymasterserver.mydomain.com` here, is **MASTER SERVER**'s domain. Since both step 6~7 and 8 says *mydomain.com*, I felt like it was very confusing for someone who tries this out for first time and have no server background like me.

* Once it successes on replication process, you should check it by `show slave status\G;` command.
The message that says *Slave running normally* does NOT guarantee that it is actually running.

If you see error messages in the status, you should stop the replication by

`CALL mysql.rds_stop_replication;`

and change settings(it could be at your master server OR your slave server), start it again by

`CALL mysql.rds_start_replication;`

* If it's running successfully, you should see no errors and instead see something like
```
Exec_Master_Log_Pos: 75456
Relay_Log_Space: 76280
...
Seconds_Behind_Master: 0
```
which is an indicator that your replication is running, showing gap with the master server.

* At your master server, you can also check if your DBs are connected well by commands like `show master status\G` or `show slave hosts\G`.
