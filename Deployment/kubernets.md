# Introduction to Kubernetes
After our application is packaged in a container image somewhere, we need a way to actually run it, and that's where a system like Kubernetes will help us.

kubernetes takes a group of machines and expose them to use as if it was a single thing. 

If we have dozens of replicas of an application running, Kubernetes can load balance the traffic between these replicas.

# Kubernetes Architecture

## Kubernetes Cluster
A Kubernetes cluster consisits of a master and several worker nodes.
- The **master** node
- **Worker** nodes

### The workers
The worker nodes are where our applications actually run. Multiple applications can run on the same node, and the same application can have multiple replicas spread across different nodes.

### The master
Changes to our desired state(usually in the form of `yaml` manifest files) are sent to the master that will then decide what it needs to do. It compares the current state with the desired state, and makes the necessary changes to always make sure we have what we want.

# Introduction to `Kubectl` 
`kubectl` is the Kubernetes CLI, and it is the main interface with Kubernetes.
`kubectl` is connected to the cluster's master nodes.
Interacting with Kubernetes by sending commands to master nodes through `kubectl`.

There are two main ways to use `kubectl`:
- Declarative way *via manifest files*
- Imperative way *via specific orders*

# Pods
Pods are where our applications run. **It's the basic building block and the atomic unit of scheduling in Kubernetes**.
Each pod will include one or more containers and every time we run a container in Kubernetes, it will be inside a pod.

## Multi-Container Pods
Multiple containers can run inside a single pod. Pod is a way to group containers that cooperate to do something.
When we run more than one container in a single pod, it's usually to support the primary application.

## Interaction with Running Pods
`kubectl apply -f <pod_yaml_file>`n applies the manifest file.

`kubectl port-forward <pod_name> --address 0.0.0.0 3000:80` sends requests from `localhost:3000` to the container's port 80.

### Streaming logs
`kubectl logs --follow nginx` where `--follow` tells kubectl to keep streaming the logs live, instead of just printing and exiting.

### Executing commands
`kubectl exec nginx -- ls`

### Killing pods
`kubectl delete pod <pod_name>`
`kubectl delete -f <pod_yaml_file>`

When a pod dies, Kubernetes will NOT automatically reschedule it.

# Deployments
- Used to scale our applications by increasing/decreasing the number of replicas we have running.
- Handles the rollout of new versions of our application
