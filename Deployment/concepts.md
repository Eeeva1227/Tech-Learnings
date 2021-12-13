# The monolith
Changes to one tiny part of the application required a whole redeployment that had to be carefully planned.

# Microservice-based architectures


# Virtual Machines
As the number of applications grew, so did the complexity of managing all of these dependecies. Each machine had to be carefully configured to run all our applications, and that was incredibly hard to manage.

This problem is solved with **Virtual Machines(VM)**. Each application could have its own operating system, baked with the exact dependencies it needed.

# Docker
As our systems became more complex and the number of applications and services we had to run started to grow, even VM were a bit too heavyweight. It was not viable to run an entire OS for each small(or micro) servive we had to deploy.

That's when container technologies like `Docker` started to become popular.

We can package our services in a container that will run on the same host OS but still with enough isolation that we don't need to worry about one container affecting the others.

VM and containers are different things yet serve the same purpose in many ways. It provides an isolated and consistent environment to run our applications.