Title: IPRoute2 Basic
Date: 2016-08-04 10:00
Category: Linux


### ip link

Show link layer interface information

```
ip link
```

```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:fc:a7:ea brd ff:ff:ff:ff:ff:ff
```

To get statistics about how an interface is communicating, you can query statistics from each interface by passing the -s option to the link subcommand:

```
ip -s link show ens33
```

```
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:fc:a7:ea brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast   
    1060924019 724744   0       0       0       0       
    TX: bytes  packets  errors  dropped carrier collsns 
    12143852   195148   0       0       0       0 
```

### ip addr

get an overview of the addresses attached to each interface


```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:fc:a7:ea brd ff:ff:ff:ff:ff:ff
    inet 192.168.138.128/24 brd 192.168.138.255 scope global dynamic ens33
       valid_lft 1425sec preferred_lft 1425sec
    inet6 fe80::1856:a02b:4c91:cea6/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:34:a4:7b:20 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:34ff:fea4:7b20/64 scope link 
       valid_lft forever preferred_lft forever
5: veth78282f4@if4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default 
    link/ether b2:42:c4:47:0c:16 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet6 fe80::b042:c4ff:fe47:c16/64 scope link 
       valid_lft forever preferred_lft forever
```

To get a specific interface, you can use this syntax:

```
ip addr show eth0
```

### ip route

The routing table contains kernel information about the paths to other network locations. We can print off the current routing table by typing:

```
ip route
```

```
default via 192.168.138.2 dev ens33  proto static  metric 100 
169.254.0.0/16 dev docker0  scope link  metric 1000 
172.17.0.0/16 dev docker0  proto kernel  scope link  src 172.17.0.1 
192.168.138.0/24 dev ens33  proto kernel  scope link  src 192.168.138.128  metric 100
```

## How To Configure Network Interfaces and Addresses

### Config interface

```
ip link set eth1 up
ip link set eth1 down
```

You can also use the ip link subcommand to set attributes about the interface. For instance, if you would like to change the multicast flag on or off for your interface, you can type:

```
ip link set eth1 multicast on
ip link set eth1 multicast off
```

You can adjust the mtu and package queue length like this:

```
ip link set eth1 mtu 1500
ip link set eth1 txqueuelen 1000
```

If the interface you are configuring is down, you can adjust the interface name and the arp flag associated with the device:

```
ip link set eth1 name eth10
ip link set eth1 arp on
```

To adjust the addresses associated with the interfaces, we again use the `ip addr` subcommand.

We can add an address to a device by typing:

```
ip addr add ip_address/net_prefix brd + dev interface
```


The `brd +` portion of the command automatically sets the broadcast address. Multiple addresses can be added to each interface without a problem.

We can get rid of addresses with the inverse operation. To delete a specific address associated with an interface, you can use it like this:

```
ip addr del ip_address/net_prefix dev interface
```

Optionally, you can omit the address, and the first listed address associated with that interface will be deleted.

You can also adjust the routing of the server, using the `ip route [add | change | replace | delete ]` syntax, but we won't be covering this here, because most people will will not be adjusting this on a regular basis


## Additional Capabilities of IPRoute2
IPRoute2 has some additional capabilities that we will not be able to discuss in-depth in this guide. Instead, we will talk about what these are and what situations you may find them useful.

The idea of IP routing rules is difficult to talk about because it is very situation dependent. Basically, you can decide on how to route traffic based on a number of fields, including target address, source address, routing protocol, packet size, etc.

We access this functionality by using the ip rule subcommand. The basic querying follows the general pattern of the other subcommands:

```
ip rule show
0:  from all lookup local 
32766:  from all lookup main 
32767:  from all lookup default
```

These three routing rules are the default rules configured by the kernel. The first line matches any traffic and is used to route high priority traffic. The second line is the main rule that handles normal routing. The last one is an empty rule that is used for post-processing if the rules above didn't match the packet.

Routing rules, as configured by the IPRoute2 software, are stored in a routing policy database, where the policy is selected by matching against sets of rules. We can add or delete rules using the appropriate actions. You should not do this without knowing what you are doing however. Look at the man pages and search for ip rule for more information.

```
man ip         # search for "ip rule"
```
Another thing that we'll discuss briefly is the handling of arp information through these tools. The subcommand that deals with this information is called ip neigh.

```
ip neigh
107.170.58.1 dev eth0 lladdr 00:00:5e:00:01:68 DELAY
```

By default, this should at least list your gateway. Arp is a protocol used to gather information about physical devices accessible through the local network.

Basically, an arp request is broadcast over the local network whenever an IP address needs to be reached. The matching IP address responds and then the local computer knows where to send information to that IP address. This information is cached on the local system for some time (typically about 15 minutes) to avoid having to query during follow up communication.
