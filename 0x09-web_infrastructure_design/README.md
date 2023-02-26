# :shell: 0x09 - Web Infrastructure :shell:

In this project I will be whiteboarding various web infrastructure.

## :running: Getting Started

* [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) - Operating system reqd.

## :warning: Prerequisites

* Must have `git` installed

* Must have repository cloned


```
$ sudo apt-get install git
```
## :List Of Tasks: Tasks

0-Simple_web_stack 1.What is a server Servers are physical machines (as hardwares), virtual machines or softwares (computer programs) that serve or provide functionality to other programs or devices called “clients”. 2.What is the role of the domain name The role of the domain name is to replace complex IP addresses numbers into easily understandable names so humans can remember and communicate them in a better way. What type of DNS record www is in www.foobar.com DNS record of www belongs to a A record of the www.foobar.com because it goes directly ti the IP address What is the role of the web server Web servers are what make Web hosting What is the role of the application server The application server is the intermediary between browser-based databases and back-end databases and legacy systems. What is the role of the database The role of the database is to make the information gathered organized so it can be easily accessed, managed and updated What is the server using to communicate with the computer of the user requesting the website The server is using the HTTP (Hypertext Transfer Protocol), which enables the transfer of resource and data, such as HTML documents between the server and the client.

Issues with the simple web infrastructure

One of the issues of having a simple web infrastructure, has to do with the SPOF (Single Point of Failure) where if component of the system fails, there is no backup that can support the continuity of the functionality of the system, bringing the whole system to a collapse by being unable to operate.
Also, whenever some structure or node in the system needs to be repaired, the whole system has to be shut down, while the maintenance is done. Then, client requests cannot be attended during this period of time.
Overload of traffic can be a risk to the server capacity. This, because there is no possibility to scale the service with additional servers as backup. Leading to a possible breakdown of the web page and client requests, as traffic surpasess servers capacity.
1-distributed_web_infrastructure For additional element, why you are adding it?

The new configuration is composed of two master-servers and one slave-servers. As the master-servers are going to be working based on a Active-Active set up, their configuration must be identical, therefore we need to add every additional element as the simple web infrastructure we had in the previous point. The load is going to be managed through a load-balancer, which distributes the queries according to a Robin-Round algorithm. Finally an additional server will be needed to serve a replica or slave server, helping to unload the masters servers reading queries.

What distribution algorithm your load balancer is configured with and how it works

Our load-balancer is using a Round Robin algorithm distribution. Meaning the queries requested are distributed to every server sequentially one after another. And after sending the request to the last server, the algorithm startarts from the first server. This will bring on average and approximately, to a server load distribution of 50% on each of the two servers configuration. Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both

Our load-balancer is enabling an Active-Active set up.

The Active-Active cluster is typically made up of at least two nodes, both activaley running the same type of services at the same time. Their purpose is to achieve load balancing by distributing tasks to different servers in order to prevent overload. As there are more than one servers (nodes) available to severe, the service time and process throughput can have improvements. How a database Primary-Replica (Master-Slave) cluster works

A database Primary-Replica (Master-Replica) is a mechanism which enables data of one database server (the master) to be replicated or to be copied to one or more computers or database servers (the slaves), in order all users share the same level of information. This process leads to a distributed database in which users can quickly access data without interfering with each other.

The database replication process can either be synchronous or asynchronous. In the first one, the replication process is done from the client server to the model server and then replicated to all the replica servers before the client is notified about the data replication. This method of replication may take longer to verify, however all data was copied before proceeding.

As in the asynchronous replication process, replication is done by sending data from the client to the model server, followed by a confirmation order to the client, who finally gives permission of copying to the replicas at an unspecified or monitored pace (Lutkevich, 2020) What is the difference between the primary node and the replica node in regard to the application.

One of the main differences between the primary node and the replica node, regarding the application, is that the primary database is regarded as the authoritative source, while the replica database is synchronized to it. The primary node serves as the keeper of information, here the “real” data is kept, then writing only happens here. On the other hand, reading only occurs in the replica or slave node. This architecture purpose is due to safeguard site reliability. In case a site receives a lot of traffic, a replica node prevents overloading of the master node with reading and writing requests. This eases the load of the entire system preventing it to collapse

2-secured_For every additional element, why you are adding it

3 Firewalls: The first Firewall checks the rules after receiving the requests and could deny following requests. The second firewall is working in the server to prevent someone hacking depending of the requests, and the third firewall acts as a circuit-level firewalls, inspect the transaction of the information. SSL certificate: 1 SSL certificate: is added to secure https protocols and encrypt communication. Then, the ‘plain text’ won’t be easy accessed or viewed by a third person, making the protocol communication and data transfer form the browser and web server more secure and_monitored_weWhat are firewalls for

Firewalls is a network security device that monitors network traffic, it can be understood as a division or “wall” between a private network and public network which limits and blocks network traffic based on a set of security rules in the hardware or software by analyzing data packets that request entry to the network. Additionally, firewalls are used to allow remote access to a private network through secure authentication (Beal, 1996)

Why is the traffic served over HTTPS

HTTPS stands for HyperText Transfer Protocol Secure, and the traffic is served in order to bring protection by using the secure port 443, which encrypts outgoing information. Then it is more difficult to spy or get access to the site’s information.

What monitoring is used for

Monitoring is practice used for quality control. As Peter Ducker said, “What can’t be measured, it can’t be improved”. Then, monitoring not only helps to make sure to maintain high quality levels, keeping the established standards and consistency, but also to help in the continuous improvement of the resources performance.

The way data monitoring is performed, relies on checking new data against predefined rules and metrics. If data quality anomalies are detected, an alert is sent in order to give information about the metrics and rules violation, so data can be checked (Informatica, 2021).

3 monitoring clients: 2 monitoring deployed in each master-server, and one monitoring client for the load balancer. This will help understand the metrics of the performance of the resources according to the users requests. The information gathered will help us improve users’ experience and make decisions on the future whether to scale up the web infrastructure system.

How the monitoring tool is collecting data

IT monitoring is composed of three parts: 1) Fundation; 2) Software, and 3) Interpretation in order to function.

Foundation: Are related to the infrastructure at its lowest layer of the software stack. This includes physical and virtual devices, such as servers, CPUs and VMs. Software: The software is the monitoring section which analyzes what is happening in the devices (physical or virtual machines) in terms of CPU usage, load, memory, and running count. Interpretation: Here is where collected data is turned into metrics and are presented through graphs or data charts (mostly on GUI dashboard). This is often integrated with tools of data visualization to help better understand and do data analytics of performance (Gillis, 2020). Explain what to do if you want to monitor your web server QPS

Queries per second is a measure of the rate of traffic going in a particular server serving a Web domain. It is an important metric to monitor, because it can help you decide whether to scale the server in order to cope with the demand of usage, and resource requirement so the web page won’t collapse in the future with overload server request.

Issues with the secured and monitored web infrastructureb_infrastructure
