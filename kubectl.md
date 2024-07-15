## kubectl reference

### Books and Github reference
- Kubernetes Patterns - Reusable Elements for Designing Cloud-Native Applications
Book: https://drive.google.com/drive/u/0/folders/1l4LxrtghKI8IpzVo1If6JuoihrPu3W8K
- GitHub Repo: https://github.com/k8spatterns

#### Imperative Command Examples
```kubectl create secret generic \
  app-secret --from-literal=DB_Host=mysql \
             --from-literal=DB_User=root
             --from-literal=DB_Password=password
```
`kubectl run nginx --image=nginx` Create an NGINX pod
`kubectl run nginx --image=nginx --dry-run=client -o yaml` Generate pod manifest yaml file; don't create it
`kubectl create deployment --image=nginx nginx` Create a deployment
`kubectl create deployment --image=nginx nginx --dry-run -o yaml` Generate deployment yaml; don't create it
`kubectl create deployment nginx --image=nginx --replicas=4` Generate deployment with 4 replicas
`kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml` Create a Service named redis-service of type ClusterIP to expose pod redis on port 6379
`kubectl expose pod nginx --port=80 --name nginx-service --type=NodePort --dry-run=client -o yaml` Create a Service named nginx of type NodePort to expose pod nginx's port 80 on port 30080 on the nodes
`kubectl taint nodes $node key=value:taint-effect` taint-effect (NoSchedule|PreferNoSchedule|NoExecute)
`kubectl taint nodes controlplane node-role.kubernetes.io/master:NoSchedule` Untaint node
`kubectl set image deployment/myapp nginx=nginx:1.9.1` Update deployment to set a different version of nginx
`kubectl rollout status deployment/myapp` Check status of rollout
`kubectl rollout history deployment/myapp` Check status of rollout
`kubectl rollout undo deployment/myapp` Rollback

#### Google Cloud resources you can create with Config Connector:
`kubectl get crds --selector cnrm.cloud.google.com/managed-by-kcc=true`

#### Get the cluster config view. 
`kubectl config view --raw --flatten > cluster.yaml` This gives you all of your config setup on your laptop, across all GCP accounts. The cluster.yaml produced from this command will be used to setup nethopper.

#### Get the External IPs of all the nodes
`kubectl get nodes -o wide --no-headers 2>/dev/null | awk '{print $7}'`

#### Rollout Restart all the apps in a namespace
`for app in $(kubectl get deployments -n $ns --no-headers --output=custom-columns="name:.metadata.name"); do kubectl rollout restart deploy/$app -n $ns; done`

#### Get the pods in Running Status
`kubectl get pods --all-namespaces --field-selector status.phase=Running`

#### Get the pods in Pending Status
`kubectl get pods --all-namespaces --field-selector status.phase=Pending`

#### Get the pods in a namespace
`kubectl get pods --all-namespaces --field-selector metadata.namespace=esx-i9-qa`

#### Get the Pending pods in a namespace
`kubectl get pods --all-namespaces --field-selector metadata.namespace=<ns>,status.phase=Pending`

#### Get the Pods for a Deployment
`kubectl get pods -n <ns> -l app=i9-document-api`

#### Get status reasons for unhealthy containers in a particular namespace
`kubectl get pods --all-namespaces --field-selector metadata.namespace=<ns>,status.phase=Pending --output=custom-columns="NAME:.metadata.name,STATUS:.status.phase,CONTAINERS:.status.containerStatuses[].name,STATE:.status.containerStatuses[].state"`

#### Get status reasons for unhealthy containers in a particular DEPLOYMENT
`kubectl get pods --all-namespaces --field-selector metadata.namespace=<ns>,status.phase=Pending -l app=i9-converter-service --output=custom-columns="NAME:.metadata.name,STATUS:.status.phase,CONTAINERS:.status.containerStatuses[].name,STATE:.status.containerStatuses[].state"`

#### Get the container status for a particular pod
`kubectl get pod  i9-converter-service-6c7b47df64-ftxxd -n <ns> --output=custom-columns="NAME:.metadata.name,STATUS:.status.phase,CONTAINERS:.status.containerStatuses[].name,STATE:.status.containerStatuses[].state"`

#### Get total number of pods
`kubectl get pods --all-namespaces --no-headers --field-selector metadata.namespace=<ns> --output=custom-columns="NAME:.metadata.name" | wc -l`

#### Create an NGINX Pod
`kubectl run nginx --image=nginx`

#### Generate POD Manifest YAML file (-o yaml). Don't create it(--dry-run)
`kubectl run nginx --image=nginx --dry-run=client -o yaml`

#### Create a deployment
`kubectl create deployment --image=nginx nginx`
`kubectl create deployment web-server --image=gcr.io/engaged-reducer-318105/sre-demo:v1`

#### Expose the deployment via a service
`kubectl expose deployment web-server --type LoadBalancer --port 80 --target-port 80`

#### Generate Deployment YAML file (-o yaml). Don't create it(--dry-run)
`kubectl create deployment --image=nginx nginx --dry-run=client -o yaml`

#### Generate Deployment YAML file (-o yaml). Don't create it(--dry-run) with 4 Replicas (--replicas=4)
`kubectl create deployment --image=nginx nginx --dry-run=client -o yaml > nginx-deployment.yaml`

#### kubectl context management
ns=observability
`kubectl config set-context $(kubectl config current-context) --namespace=$ns` Set a namespace as the default namespace
`kubectl config set-context --current --namespace sample` Just update the default namespace in the current cluster context
`kubectl config get-contexts` Describe one or many contexts
`kubectl config use-contexts` Set the current-context in a kubeconfig file

#### Expose a Deployment
`kubectl expose deployment hello-world --type=NodePort --name=example-service`

#### nginx is just the example; could be any deployment
**Create Objects:**
```
kubectl apply -f nginx.yaml (declarative)
kubectl run --image=nginx nginx
kubectl create deployment --image=nginx nginx
kubectl expose deployment nginx --port 80
```

```
Update Objects:
kubectl apply -f nginx.yaml (declarative)
kubectl edit deployment nginx
kubectl scale deployment nginx --replicas=5
kubectl set image deployment nginx nginx=nginx:1.18
```

#### Imperative: Create a service redis-service exposing a pod
`kubectl expose pod redis --port 6379 --type ClusterIP --name redis-service`

#### Taint and Tolerance
`kubectl taint nodes $node key=value:taint-effect`
- taint-effect : NoSchedule | PreferNoSchedule | NoExecute(existing pods will be evicted)

#### Get the nodes in the default pool
`kubectl get nodes -l cloud.google.com/gke-nodepool=default-pool`

#### Drain all the nodes in default pool
```
for node in $(kubectl get nodes -l cloud.google.com/gke-nodepool=default-pool -o=name); do
  kubectl drain --force --ignore-daemonsets --delete-emptydir-data --grace-period=10 "$node";
done
```

#### Istio Injection
`kubectl label namespace default istio-injection=enabled`

#### Delete ALL resources in a Namespace
```
ns=monitoring
kubectl delete all --all -n $ns
```

#### Get Containers running in all Pods - All Namespaces
`kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{@.metadata.name}{"\n"}{@.metadata.namespace}{"\n"}{@.spec.nodeName}{"\n"}{@.spec.containers[*].name}{"\n"}{@.spec.containers[*].image}{"\n"}{@.spec.containers[*].resources.requests.cpu}{"\n"}{@.spec.containers[*].resources.requests.memory}{"\n"}{@.spec.containers[*].resources.limits.cpu}{"\n"}{@.spec.containers[*].resources.limits.memory}{"\n"}{end}'`

#### Get Containers running in all Pods - Specified Namespace
`kubectl get pods -n $ns -o jsonpath='{range .items[*]}{@.metadata.name}{"\n"}{@.metadata.namespace}{"\n"}{@.spec.nodeName}{"\n"}{@.spec.containers[*].name}{"\n"}{@.spec.containers[*].image}{"\n"}{@.spec.containers[*].resources.requests.cpu}{"\n"}{@.spec.containers[*].resources.requests.memory}{"\n"}{@.spec.containers[*].resources.limits.cpu}{"\n"}{@.spec.containers[*].resources.limits.memory}{"\n"}{end}'`

#### Get Containers running in A Pod - Specified Namespace
`kubectl get pods -n $ns --field-selector metadata.name=$pod -o jsonpath='{range .items[*]}{@.metadata.name}{"\n"}{@.metadata.namespace}{"\n"}{@.spec.nodeName}{"\n"}{@.spec.containers[*].name}{"\n"}{@.spec.containers[*].image}{"\n"}{@.spec.containers[*].resources.requests.cpu}{"\n"}{@.spec.containers[*].resources.requests.memory}{"\n"}{@.spec.containers[*].resources.limits.cpu}{"\n"}{@.spec.containers[*].resources.limits.memory}{"\n"}{end}'`

#### Loop through to get the containers...
`for i in 0 1; do kubectl get pods -n $ns --no-headers -o=custom-columns=container:.spec.containers[$i].name,pod:.metadata.name,namespace:.metadata.namespace,node:.spec.nodeName,cpu_request:.spec.containers[$i].resources.requests.cpu,memory_request:.spec.containers[$i].resources.requests.memory,cpu_limit:.spec.containers[$i].resources.limits.cpu,memory_limit:.spec.containers[$i].resources.limits.memory; done`

#### Get Deployments Custom Columns
`kubectl get deployment --all-namespaces -o=custom-columns=app:.metadata.name,namespace:.metadata.namespace,env:.metadata.labels.environment,version:.metadata.labels.version,replicas:.status.availableReplicas,cpu_request:.spec.template.spec.containers[0].resources.requests.cpu,memory_request:.spec.template.spec.containers[0].resources.requests.memory,cpu_limit:.spec.template.spec.containers[0].resources.limits.cpu,memory_limit:.spec.template.spec.containers[0].resources.limits.memory`

#### Get deployments Custom Columns
`kubectl get deployment -n $ns -o=custom-columns=app:.metadata.name,namespace:.metadata.namespace,env:.metadata.labels.environment,version:.metadata.labels.version,replicas:.status.availableReplicas,cpu_request:.spec.template.spec.containers[0].resources.requests.cpu,memory_request:.spec.template.spec.containers[0].resources.requests.memory,cpu_limit:.spec.template.spec.containers[0].resources.limits.cpu,memory_limit:.spec.template.spec.containers[0].resources.limits.memory`

#### Get HPA Custom Columns
`kubectl get hpa --all-namespaces -o=custom-columns=app:.metadata.name,namespace:.metadata.namespace,hpa_min_replicas:.spec.minReplicas,hpa_max_replicas:.spec.maxReplicas,hpa_target_cpu_threshold:.spec.targetCPUUtilizationPercentage,hpa_current_cpu_percent:.status.currentCPUUtilizationPercentage,hpa_current_replicas:.status.currentReplicas,hpa_desired_replicas:.status.desiredReplicas,hpa_last_scale_time:.status.lastScaleTime`

#### Get ConfigMap (for Java Options)
`kubectl get configmap --all-namespaces -o custom-columns=app:.metadata.name,namespace:.metadata.namespace,java_options:.data._JAVA_OPTIONS`

#### Get Virtual Services
`kubectl get vs --all-namespaces --output=custom-columns="NAME:.metadata.name,NAMESPACE:.metadata.namespace,GATEWAYS:.spec.gateways[*],HOSTS:.spec.hosts[*],URI:.spec.http[*].match[*].uri,ROUTE:.spec.http[*].route[*].destination.host"`

#### Get all the apps in a namespace
`kubectl get deployment -n $ns -o  jsonpath='{.items[*].metadata.labels.app}'`

#### Get the App Version
`kubectl get deployment --selector=app=$app -n $n -o  jsonpath='{.items[*].metadata.labels.version}'`
`kubectl get deployment -l app=$app -n $n -o  jsonpath='{.items[*].metadata.labels.version --output=custom-columns="NAME:.metadata.name,IMAGE:.spec.containers[*].image”`
`kubectl get deployment -l app=$app -n $n --output=custom-columns=“VERSION:.metadata.labels.version”`

#### Get ALL pods for a Deployment
`kubectl get pods -n $ns -l app=$app`
`kubectl get pods -n $ns -l app=$app --no-headers | wc -l | tr -d ' '`

#### Get RUNNING Status pods for a Deployment
`kubectl get pods -n $ns -l app=$app --field-selector status.phase=Running`
`kubectl get pods -n $ns -l app=$app --field-selector status.phase=Running --no-headers --ignore-not-found=true | wc -l | tr -d ' '`

#### Get PENDING Status pods for a Deployment
`kubectl get pods -n $ns -l app=$app --field-selector status.phase=Pending`
`kubectl get pods -n $ns -l app=$app --field-selector status.phase=Pending --no-headers --ignore-not-found=true | wc -l | tr -d ' '`

#### Get ALL pods across ALL Namespaces
`kubectl get pods --all-namespaces`
`kubectl get pods --all-namespaces --no-headers --ignore-not-found=true | wc -l | tr -d ' '`

#### Get RUNNING Status pods across ALL Namespaces
`kubectl get pods --all-namespaces --field-selector status.phase=Running`
`kubectl get pods --all-namespaces --field-selector status.phase=Running --no-headers --ignore-not-found=true | wc -l | tr -d ' '`

#### Get PENDING Status pods across ALL Namespaces
`kubectl get pods --all-namespaces --field-selector status.phase=Pending`
`kubectl get pods --all-namespaces --field-selector status.phase=Pending --no-headers --ignore-not-found=true| wc -l | tr -d ' '`

#### Get SUCCEEDED Status pods across ALL Namespaces
`kubectl get pods --all-namespaces --field-selector status.phase=Succeeded`
`kubectl get pods --all-namespaces --field-selector status.phase=Succeeded --no-headers --ignore-not-found=true| wc -l | tr -d ' '`

#### Get FAILED Status pods across ALL Namespaces
`kubectl get pods --all-namespaces --field-selector status.phase=Failed`
`kubectl get pods --all-namespaces --field-selector status.phase=Failed --no-headers --ignore-not-found=true| wc -l | tr -d ' '`

#### Get ALL pods for a Namespace
`kubectl get pods --all-namespaces --field-selector metadata.namespace=$ns`
`kubectl get pods --all-namespaces --field-selector metadata.namespace=$ns --no-headers --ignore-not-found=true| wc -l | tr -d ' '`

#### Get RUNNING Status pods for a Namespace
`kubectl get pods --all-namespaces --field-selector metadata.namespace=$ns,status.phase=Running`
`kubectl get pods --all-namespaces --field-selector metadata.namespace=$ns,status.phase=Running --no-headers --ignore-not-found=true | wc -l | tr -d ' '`

#### Get PENDING Status pods for a Namespace
`kubectl get pods --all-namespaces --field-selector metadata.namespace=$ns,status.phase=Pending`
`kubectl get pods --all-namespaces --field-selector metadata.namespace=$ns,status.phase=Pending --no-headers --ignore-not-found=true | wc -l | tr -d ' '`

#### Get FAILED Status pods for a Namespace
`kubectl get pods --all-namespaces --field-selector metadata.namespace=$ns,status.phase=Failed`
`kubectl get pods --all-namespaces --field-selector metadata.namespace=$ns,status.phase=Failed --no-headers --ignore-not-found=true | wc -l | tr -d ' '`

#### Get SUCCEEDED Status pods for a Namespace
`kubectl get pods --all-namespaces --field-selector metadata.namespace=$ns,status.phase=Succeeded`
`kubectl get pods --all-namespaces --field-selector metadata.namespace=$ns,status.phase=Succeeded --no-headers --ignore-not-found=true | wc -l | tr -d ' '`

#### Get Pod Image
`kubectl get pods -o wide  -n $ns --output=custom-columns="NAME:.metadata.name,IMAGE:.spec.containers[*].image"`

#### Get Deployment Images
`kubectl get deployments --all-namespaces --output=custom-columns="KIND:.kind,NAME:.metadata.name,Namespace:.metadata.namespace,IMAGE:.spec.template.spec.containers[*].image"`

#### Get CronJob Images
`kubectl get cronjobs --all-namespaces --output=custom-columns="KIND:.kind,NAME:.metadata.name,Namespace:.metadata.namespace,IMAGE:spec.jobTemplate.spec.template.spec.containers[*].image"`

#### Get status reasons for unhealthy containers in a particular namespace
`kubectl get pods --all-namespaces --field-selector metadata.namespace=esx-i9-qa,status.phase=Pending --output=custom-columns="NAME:.metadata.name,STATUS:.status.phase,CONTAINERS:.status.containerStatuses[*].name,STATE:.status.containerStatuses[*].state"`

#### Get status reasons for unhealthy containers in a particular DEPLOYMENT
`kubectl get pods --all-namespaces --field-selector metadata.namespace=esx-i9-qa,status.phase=Pending -l app=i9-converter-service --output=custom-columns="NAME:.metadata.name,STATUS:.status.phase,CONTAINERS:.status.containerStatuses[*].name,STATE:.status.containerStatuses[*].state"`

#### Get the container status for a particular pod
`kubectl get pod  i9-converter-service-6c7b47df64-ftxxd -n esx-i9-qa --output=custom-columns="NAME:.metadata.name,STATUS:.status.phase,CONTAINERS:.status.containerStatuses[*].name,STATE:.status.containerStatuses[*].state"`

#### Get total number of pods
`kubectl get pods --all-namespaces --no-headers --field-selector metadata.namespace=esx-i9-prd --output=custom-columns="NAME:.metadata.name" | wc -l`
`kubectl get pod i9-converter-service-6c7b47df64-fxzkg -n esx-i9-qa --output=custom-columns=“NAME:.metadata.name,CONTAINERS:.status.containerStatuses[*].name,STATE:.status.containerStatuses[*].state"`

#### describe pod
`kubectl describe pod i9-converter-service-6c7b47df64-fxzkg -n esx-i9-qa | grep Events: -A 10`

#### Get virtual services
`kubectl get vs --all-namespaces --output=custom-columns="NAME:.metadata.name,NAMESPACE:.metadata.namespace,GATEWAYS:.spec.gateways[*],HOSTS:.spec.hosts[*],URI:.spec.http[*].match[*].uri,ROUTE:.spec.http[*].route[*].destination.host"`

#### Get all the pods that are not 1.9.5
`kubectl get pods -o wide  --all-namespaces --output=custom-columns="NAME:.metadata.name,SPACE:.metadata.namespace,IMAGE:.spec.containers[*].image" | grep istio | sed /1.9.5/d`

#### Disable PRD West Gateway
`kubectl scale deployment --replicas=0 ilb-gateway-api-ext-prd -n istio-system`
`kubectl scale deployment --replicas=0 ilb-gateway-ui-prd -n istio-system `

#### Enable UAT East Gateway
`kubectl scale deployment --replicas=1 istio-ilbgateway-esportal-ui-pub-uat -n istio-system `

#### Get HPA
`kubectl get hpa -n es-portal-dev`

#### Important Flags:
```
--all-namespaces
—show-labels
```

#### Basic commands
```
kubectl get ns
kubectl get deployments --namespace es-portal-prd
kubectl get deployments --namespace es-portal-prd | awk '{print $1}' 	
kubectl get services --namespace es-portal-prd
kubectl get pods --namespace es-portal-prd
kubectl get nodes | awk '{print $1}' 
```

#### Search by Labels:
`kubectl get deployments --all-namespaces -l app=audit-api`
`kubectl get deployments --all-namespaces -l 'app in (audit-api,user-api)'`

#### Get the Node Capacity and Allocatable Resources
`kubectl describe node $node | grep Allocatable -B 7 -A 6`

#### Get the Node Requests and Limits
`kubectl describe node $node | grep 'Allocated resources:' -A 5`

#### Get Max number of pods a node can schedule
`kubectl describe node $node | grep pods: | head -1 | awk 'BEGIN { FS = "[ :,}()]+" } { printf "%d", $3 } '`

#### Get Non-terminated pods running on a node
`kubectl describe node $node | grep "Non-terminated Pods:" | head -1 | awk 'BEGIN { FS = "[ :,}()]+" } { printf “%d”, $3 } '`

#### Get all the pods running on a Node
`kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=$node | awk 'BEGIN { FS = "[ :,}()]+" }{ printf “%d”, $3 } '`
`kubectl get pods --all-namespaces -o wide --field-selector spec.nodeName=$node | awk '{print $1,$2,$3,$4,$5,$6,$7,$8,$9}'`
$1: Namespace
$2: Name of the Pod’{}
$4: Status
$5: Restarts
$6: Age
$7: IP

#### Get the node description in a json format
`kubectl get node $node -o json`

#### Get the deployment description in a json format
`kubectl get deployment $d --namespace $ns -o json`

#### Get Image name for a namespace-deployment combination
`temp=$(kubectl describe deployment $d --namespace $ns | grep Image: | awk 'BEGIN { FS = "[ :,}()/@]+" } { printf "%s %s %s %s",$3,$4,$5,substr($8,1,12) } ')`
project=$(echo $temp | awk '{printf "%s/%s",$1,$2}')
repository=$(echo $temp | awk '{print $3}')
sha=$(echo $temp | awk '{print $4}')

#### Get the Deployment version
`version=$(kubectl describe deployment $d --namespace $ns | grep version= | head -1 | awk 'BEGIN { FS = "[ :,}()/@]+" } { printf "%s", substr($2,9) } ')`
`kubectl get pods -l 'environment in (production, qa)'`

#### Kubectl jsonpath examples:
`kubectl get pods -n es-portal-dev -l app=audit-api -o=jsonpath='{.items[0].spec.containers[0].resources}'`
`kubectl get pods -n es-portal-dev -l app=audit-api -o=jsonpath='{.items[0].status.conditions}'`
`kubectl get pods -n es-portal-dev -l app=audit-api -o=jsonpath='{.items[0].apiVersion}'`
`Kubectl custom-columns example`
`kubectl get pods --all-namespaces --no-headers=true -o=custom-columns=NAME:.metadata.name`

#### Explain command gives you good information about the commands.
`kubectl explain pods`
`kubectl explain pods.spec.containers`

#### Run an interactive shell within the pod
`kubectl exec monolith --stdin --tty -c monolith /bin/sh`

#### Scale a deployment
`kubectl scale deployment hello --replicas=3`

#### Get replicasets
`kubectl get replicaset`

#### Kubectl Rolling Update Commands
```
kubectl rollout history deployment/hello
kubectl rollout pause deployment/hello
kubectl rollout resume deployment/hello
kubectl rollout status deployment/hello
kubectl rollout undo deployment/hello
```

#### Log in to a GKE POD
`export FORTIO_POD=$(kubectl get pods -l app=fortio -o 'jsonpath={.items[0].metadata.name}')`
`kubectl exec "$FORTIO_POD" -c fortio -- /usr/bin/fortio curl -quiet http://httpbin:8000/get`