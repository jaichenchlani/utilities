#!/bin/bash

# Config Values used in Bash Scripts across the repository
# Any default values used across automation should be coded here.

# Timeout setting in seconds
default_timeout=1
wait_for_key_press_flag="true"

# kubectl commands
ns=observability

# Get external IPs for all the nodes
# Original command, not working when moved to work laptop..
kubectl_get_node_external_ips_obsolete="kubectl get nodes -o jsonpath=\"{.items[*].status.addresses[?(@.type=='ExternalIP')].address}\""
# Switched to this...
kubectl_get_node_external_ips="kubectl get nodes --no-headers -o wide | awk {'print \$7'}"

# Get external IP for a particular service
# Set the variable app, before using the command in your script
kubectl_get_svc_external_ip="kubectl get svc --no-headers --field-selector=metadata.name=\$app | awk '{print \$4}'"