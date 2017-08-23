## Subnet Mask

How to make and locate subnets - credits to [this](https://www.youtube.com/watch?v=Ct4PU6CyvTQ&t=435s) course

#### CIDR : Classless Inter-Domaining Routing

#### class C example

##### 1) how to make?

**a.** how many subnets? --> subnets can only be made in even numbers. If odd number, make even number that contains it.

**b.** borrow bits from the network part ( xxxxxxxx.xxxxxxxx.xxxxxxxx.10000000). Depending on the number of division. (ex) 2 division - 1 bit, 4 division - 2 bits, 8 division - 3bits...)

**c.** each subnet will have 2^(rest of host bits) -2

**d.** set ranges

ex) divide into 3 subnets
```
192.168.1.0
subnet 1 - 192.168.1.0 ~ 192.168.1.63
subnet 2 - 192.168.1.64 ~ 192.168.1.127
subnet 3 - 192.168.1.128 ~ 192.168.1.191
subnet 4 - 192.168.1.192 ~ 192.168.1.255
```

#### 2) how to position?

**a.** Identify mask bits (/n), and find its class

**b.** Find out the remainder bits without class determining bits (8, 16, 24)

**c.** Find out how many blocks (block size) of each subnet

**d.** find out each range of subnets

**e.** locate where the given IP is

**f.** find out network Id and Broadcast Id

ex) 192.168.225.212/27
```
a. 27 --> class C
b. remainder is 3 bits.
c. each subnet carries 32 bits and 30 hosts
d. range is:
subnet 1 - 192.168.255.0 ~ 192.168.255.31
subnet 2 - 192.168.255.32 ~ 192.168.255.63
subnet 3 - 192.168.255.64 ~ 192.168.255.95
subnet 4 - 192.168.255.96 ~ 192.168.255.127
subnet 5 - 192.168.255.128 ~ 192.168.255.159
subnet 6 - 192.168.255.160 ~ 192.168.255.191
subnet 7 - 192.168.255.192 ~ 192.168.255.223
subnet 8 - 192.168.255.224 ~ 192.168.255.255
e. the given Ip locates at subnet 7
f. network ID : 192.168.255.192/27 , Broadcast Id: 192.168.255.223/27
```
