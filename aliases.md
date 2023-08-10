# SRE Terminal Aliases

### My Exports
export PS1="[\u@\h]\w$"
export REPOS=/home/repos
export project_id=codegarage-381602
export zone=us-east1
export zone=us-east1-b
export machine_type=n1-standard-1

### Linux aliases
alias ll="ls -lrt"
alias lla="ls -lart"
alias repos="cd $REPOS"
alias fhere="find . -name "
alias myip="curl http://ipecho.net/plain; echo "
alias du1='du -h -d 1 | sort -hr' # This shows the size of the current directory and its subdirectories in human-readable format
alias today='date +"%A, %B %d, %Y"' # This shows the current date in the format of "Day of the week, Month Day, Year"
alias weather='function _weather() { curl wttr.in/$1; }; _weather' # This shows the weather for your system location using the wttr.in service
alias ...='cd ../..' # This allows you to navigate up to two directory levels quickly.
alias c='clear' # This allows you to clear the terminal screen with a simple command.
alias h='history' # This allows you to view your command history quickly.
alias cp='cp -i' # This adds the -i flag to the cp command, which prompts for confirmation before overwriting an existing file.
alias rm='rm -i' # This adds the -i flag to the rm command, which prompts for confirmation before deleting a file.
alias mv='mv -i' # This adds the -i flag to the mv command, which prompts for confirmation before overwriting an existing file.
alias ..='cd ..' # This allows you to navigate up one directory level quickly
alias grep='grep --color=auto' # This is an alias for the grep --color=auto command, which highlights the search results
alias ports='netstat -a | grep -i "listen"' # This will show all open ports and the processes using them.
alias backup='tar -zcvf $(date +%Y%m%d).tar.gz *' # This creates a tarball of the current directory, compressed with gzip, with the filename in the format yyyymmdd.tar.gz.
alias path='echo -e ${PATH//:/\\n}' # This shows all directories in the PATH variable, one per line.
alias jsonpretty='function _jsonpretty() { python -m json.tool $1; }; _jsonpretty' # This pretty prints JSON file
alias rename='function _rename() { for i in *$1*; do mv "$i" "${i/$1/$2}"; done }; _rename' # This renames all files in the current directory containing a specific string with another string
alias ssh-keygen='function _ssh-keygen(){ ssh-keygen -t $1 -b $2 -C $3; }; _ssh-keygen' # This generates an ssh key with a specified encryption type, key size and comment
alias encrypt='function _encrypt() { openssl enc -aes-256-cbc -salt -in $1 -out $2; }; _encrypt' # This encrypts a file using AES-256 encryption

### terraform aliases
#### Basic Commands
alias ti='terraform init'
alias tp='terraform plan --var-file $1'
alias ta='terraform apply --auto-approve'
alias td='terraform destroy --auto-approve'
#### Interaction with State File
alias tsl='terraform state list'
alias tsr='terraform state rm $1'
alias tsh='terraform show'


### gcloud aliases
#### Config
alias gpl='gcloud projects list'
alias gcl='gcloud config list'
alias gccl='gcloud config configurations list'
alias gcca='gcloud config configurations activate $1'
#### Compute | Instances
alias gcil='gcloud compute instances list'
alias gcid='gcloud compute instances describe $1'
alias gcnl='gcloud compute networks list'
alias gcfrl='gcloud compute firewall-rules list'
alias gcsnl='gcloud compute networks subnets list --network $1'
#### Compute | Managed Instance Groups - MIG
alias gmigl='gcloud beta compute instance-groups managed list'
alias gmigd='gcloud beta compute instance-groups managed describe $1'
alias gmignp='gcloud beta compute instance-groups managed get-named-ports $1'
alias gmigli='gcloud beta compute instance-groups managed list-instances $1'
alias gmigrs='gcloud beta compute instance-groups managed resize $1 --size $2'
alias gssh='gcloud compute ssh --zone $zone $1  --project $project_id'

#### Services
alias gsl='gcloud services list'
alias gsla='gcloud services list --available'
#### GKE
alias gccll='gcloud container clusters list'
alias gcfmd='gcloud container fleet mesh describe'
alias gcfmeml='gcloud container fleet memberships list'
alias wrap_args='f(){ echo before "$@" after;  unset -f f; }; f'
#### IAM
alias gpfsa='f(){ gcloud projects get-iam-policy $1 --flatten="bindings[].members" --format="table(bindings.role)" --filter="bindings.members:$2";  unset -f f; }; f'

### kubectl aliases

#### This command is used a LOT both below and in daily life
alias k=kubectl

#### Execute a kubectl command against all namespaces
alias kca='_kca(){ kubectl "$@" --all-namespaces;  unset -f _kca; }; _kca'

#### Apply a YML file
alias kaf='kubectl apply -f'

#### Drop into an interactive terminal on a container
alias keti='kubectl exec -t -i'

#### Manage configuration quickly to switch contexts between local, dev ad staging.
alias kcuc='kubectl config use-context'
alias kcsc='kubectl config set-context'
alias kcdc='kubectl config delete-context'
alias kccc='kubectl config current-context'

#### List all contexts
alias kcgc='kubectl config get-contexts'

#### General aliases
alias kdel='kubectl delete'
alias kdelf='kubectl delete -f'

#### Pod management.
alias kgp='kubectl get pods'
alias kgpa='kubectl get pods --all-namespaces'
alias kgpw='kgp --watch'
alias kgpwide='kgp -o wide'
alias kep='kubectl edit pods'
alias kdp='kubectl describe pods'
alias kdelp='kubectl delete pods'
alias kgpall='kubectl get pods --all-namespaces -o wide'

#### get pod by label: kgpl "app=myapp" -n myns
alias kgpl='kgp -l'

#### get pod by namespace: kgpn kube-system"
alias kgpn='kgp -n'

#### Service management.
alias kgs='kubectl get svc'
alias kgsa='kubectl get svc --all-namespaces'
alias kgsw='kgs --watch'
alias kgswide='kgs -o wide'
alias kes='kubectl edit svc'
alias kds='kubectl describe svc'
alias kdels='kubectl delete svc'

#### Ingress management
alias kgi='kubectl get ingress'
alias kgia='kubectl get ingress --all-namespaces'
alias kei='kubectl edit ingress'
alias kdi='kubectl describe ingress'
alias kdeli='kubectl delete ingress'

#### Namespace management
alias kgns='kubectl get namespaces'
alias kens='kubectl edit namespace'
alias kdns='kubectl describe namespace'
alias kdelns='kubectl delete namespace'
alias kcn='kubectl config set-context --current --namespace'

#### ConfigMap management
alias kgcm='kubectl get configmaps'
alias kgcma='kubectl get configmaps --all-namespaces'
alias kecm='kubectl edit configmap'
alias kdcm='kubectl describe configmap'
alias kdelcm='kubectl delete configmap'

#### Secret management
alias kgsec='kubectl get secret'
alias kgseca='kubectl get secret --all-namespaces'
alias kdsec='kubectl describe secret'
alias kdelsec='kubectl delete secret'

#### Deployment management.
alias kgd='kubectl get deployment'
alias kgda='kubectl get deployment --all-namespaces'
alias kgdw='kgd --watch'
alias kgdwide='kgd -o wide'
alias ked='kubectl edit deployment'
alias kdd='kubectl describe deployment'
alias kdeld='kubectl delete deployment'
alias ksd='kubectl scale deployment'
alias krsd='kubectl rollout status deployment'

#### Rollout management.
alias kgrs='kubectl get replicaset'
alias kdrs='kubectl describe replicaset'
alias kers='kubectl edit replicaset'
alias krh='kubectl rollout history'
alias kru='kubectl rollout undo'

#### Statefulset management.
alias kgss='kubectl get statefulset'
alias kgssa='kubectl get statefulset --all-namespaces'
alias kgssw='kgss --watch'
alias kgsswide='kgss -o wide'
alias kess='kubectl edit statefulset'
alias kdss='kubectl describe statefulset'
alias kdelss='kubectl delete statefulset'
alias ksss='kubectl scale statefulset'
alias krsss='kubectl rollout status statefulset'

#### Port forwarding
alias kpf="kubectl port-forward"

#### Tools for accessing all information
alias kga='kubectl get all'
alias kgaa='kubectl get all --all-namespaces'

#### Logs
alias kl='kubectl logs'
alias kl1h='kubectl logs --since 1h'
alias kl1m='kubectl logs --since 1m'
alias kl1s='kubectl logs --since 1s'
alias klf='kubectl logs -f'
alias klf1h='kubectl logs --since 1h -f'
alias klf1m='kubectl logs --since 1m -f'
alias klf1s='kubectl logs --since 1s -f'

#### File copy
alias kcp='kubectl cp'

#### Node Management
alias kgno='kubectl get nodes'
alias keno='kubectl edit node'
alias kdno='kubectl describe node'
alias kdelno='kubectl delete node'
alias kgnoeips="kubectl get nodes -o wide --no-headers | awk {'print $7'}"

#### PVC management.
alias kgpvc='kubectl get pvc'
alias kgpvca='kubectl get pvc --all-namespaces'
alias kgpvcw='kgpvc --watch'
alias kepvc='kubectl edit pvc'
alias kdpvc='kubectl describe pvc'
alias kdelpvc='kubectl delete pvc'

#### Service account management.
alias kdsa="kubectl describe sa"
alias kdelsa="kubectl delete sa"

#### DaemonSet management.
alias kgds='kubectl get daemonset'
alias kgdsw='kgds --watch'
alias keds='kubectl edit daemonset'
alias kdds='kubectl describe daemonset'
alias kdelds='kubectl delete daemonset'

#### CronJob management.
alias kgcj='kubectl get cronjob'
alias kecj='kubectl edit cronjob'
alias kdcj='kubectl describe cronjob'
alias kdelcj='kubectl delete cronjob'

#### Job management.
alias kgj='kubectl get job'
alias kej='kubectl edit job'
alias kdj='kubectl describe job'
alias kdelj='kubectl delete job'