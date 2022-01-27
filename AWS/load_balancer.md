# Load balancers in AWS
- ALB
- ELB

A sudden spike in access will cause the web service to slow down and cause errors.

A load balancer like ALB distributes the load on such web services and improves their stability and high availability.


## ALB
ALB, Application Load Balancer is a part of the system called AWS.

Elastic Load Balancing automatically distributes your incoming traffic acrros multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones.

It monitors the health of its registered targets, and routes traffic only to the healthy targets.

Elastic Load Balancing supports the following load balancers: **Application Load Balancers**, **Network Load Balancers**, **Gateway Load Balancers**, and **Classic Load Balancers**.


## ALB components
A load balancer serves as the single point of contact for clients.

*The load balancer distributes incoming application traffic across multiple targets.* 

### Listener
A *listener* checks for connection requests from clients, using the protocol and port that you configure. The rules that you define for a listener determine how the load balancer routes requests to its registered targets.

Each rule consists of a priority, one or more actions, and one or more conditions. 
When the condition for a rule are met, then its actions re performed. 
You must define a default rule for each listener, and you can optionally define additional rules.

### Target group
Each *target group* routes requests to one or more registered targets, such as EC2 instances, using the protocol and port number that you specify. You can register a target with multiple target groups.
