# GKE-and-Sample-App

## What is GKE?
Google Container Engine(GKE) is a Management and orchestration system for Containers. It is a container platform which Kubernetes can manage, in short, it is a hosted Kubernetes. Goal of GKE is to increase the productivity of devops teams by hiding the complexity of setting up the k8s cluster, overlay network, etc by simple user interface

## How to create cluster using GKE?
Set the zone in which you want to try out the example.  
    `gcloud config set compute/zone us-west1-a`
 
Create the cluster using following command  
    ```gcloud container --project <project-name> clusters create <cluster-name> --machine-type n1-standard-2 --image-type "CONTAINER_VM" --disk-size "50" --num-nodes 2 --network default --enable-cloud-logging --no-enable-cloud-monitoring```

To verify if cluster is up, check  
    `kubectl get node`

## How to deploy sample application?

1. Create services,  
    `kubectl create -f mysql-service.yaml`  
    `kubectl create -f testapp-service.yaml`

2. Create deployments,  
    `kubectl create -f mysql-deployment.yaml`  
    `kubectl create -f testapp-deployment.yaml`