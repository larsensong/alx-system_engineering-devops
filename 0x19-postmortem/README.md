My first postmortem
Between EAT 6 AM  and EAT 12 PM on the 5th of April 2023  there was a six-hour outage on one of my web  servers.

About 50% of users that used our services during the outage were impacted since all of the web server's services were unavailable but the load balancer was still sending half of the user traffic to the server.

The main reason for the problem is a memory overload brought on by the server's memory and cache not being frequently purged. Additionally, the installation of the new Datadog agent overloaded the server to the point of failure.


                    Timeline was on 5th April 2023
6:05 AM   EAT - On the server, I was attempting to install the updated datadog agent.In addition, I tried to merge immediately to the main data log.

8:20 AM EAT - I tried restarting the server after finishing the settings since I saw that it was becoming less responsive.

10:30 AM EAT -  The server was still showing as being active throughout the lengthy reboot process.I thought it was a local problem because the datadog site report indicated that the server was still operational.

11:10 AM EAT -  In response to my request for assistance on Slack, a peer advised that I try login in from a new device before deleting the stored host and rebooting the server.

11: 40 AM -I followed the advice and tried to log in using a different machine, but it didn't appear to work. I then made the decision to delete the virtual machine and restart the procedure

12:00 PM EAT - The datalog was updated and the services were restored.


                    
 
The cause and solution
The issue was primarily caused by an unexpected memory overflow on the impacted server. 
Adding even another data log to the server caused a crash that rendered it irrecoverable without addressing the initial memory issues.
When colleagues were consulted, they advised trying to connect to the server from a different workstation, but it did not work. 
I choose to terminate the virtual machine and restart the server in order to solve the issue. 
The load balancer quickly started routing user traffic to the freshly built web server.

			Preventive and corrective strategies

Use bash or puppet scripts to automate the creation of new servers in the event that any existing ones fail.
Set up a mechanism to notify you if a server fails and is unrecoverable so that you may replace it as soon as possible.
Reduce the amount of time required to set up a new server.




How to prevent server crush
Increase the amount of useable server memory

Server upgrade and restart scheduling

Server cache and memory clearing automation
  
How to manage user traffic in the event of a crash


My server is routinely upgraded.
Make sure I'm backing up user info.
Server availability monitoring is automated using a load balancer.
Set up a caching plugin.
User files should be compressed.
Load balancing depending on availability is requested.

