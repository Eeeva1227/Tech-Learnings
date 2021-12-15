# Introduction to Kubernetes
After our application is packaged in a container image somewhere, we need a way to actually run it, and that's where a system like Kubernetes will help us.

kubernetes takes a group of machines and expose them to use as if it was a single thing. 

If we have dozens of replicas of an application running, Kubernetes can load balance the traffic between these replicas.

# Kubernetes Architecture

## Kubernetes Cluster
- The **master** node
- **Worker** nodes

### The workers
The worker nodes are where our applications actually run. Multiple applications can run on the same node, and the same application can have multiple replicas spread across different nodes.

### The master
Changes to our desired state(usually in the form of `yaml` manifest files) are sent to the master that will then decide what it needs to do. It compares the current state with the desired state, and makes the necessary changes to always make sure we have what we want.

# Introduction to `Kubectl` 
`kubectl` is the Kubernetes CLI, and it is the main interface with Kubernetes.

There are two main ways to use `kubectl`:
- Declarative way
- Imperative way