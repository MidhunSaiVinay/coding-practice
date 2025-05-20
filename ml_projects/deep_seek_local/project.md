1. In a shell script, use gcloud commands to create your VM instance, for example:
    ```bash
   
    # Create the VM instance
    gcloud compute instances create instance-20250126-20250126-170147 \
        --project=uber-etl-447800 \
        --zone=us-central1-c \
        --machine-type=g2-standard-12 \
        --network-interface=network-tier=PREMIUM,stack-type=IPV4_ONLY,subnet=default \
        --metadata=^,@^ssh-keys=mkasa1:ecdsa-sha2-nistp256\ AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKjIMRr7QH6MGlvIFLEcx3W14WK0\+A5kKihWyFDsROrwRpMlMSwLMAUYQpVTm/nN8TjBO1NYx08lkqv4eORcZsg=\ google-ssh\ \{\"userName\":\"mkasa1@hawk.iit.edu\",\"expireOn\":\"2025-01-26T16:46:13\+0000\"\} \
        --maintenance-policy=TERMINATE \
        --provisioning-model=STANDARD \
        --service-account=980691811171-compute@developer.gserviceaccount.com \
        --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/trace.append \
        --accelerator=count=1,type=nvidia-l4 \
        --create-disk=auto-delete=yes,boot=yes,device-name=instance-20250126-164048,image=projects/debian-cloud/global/images/debian-12-bookworm-v20250113,mode=rw,size=280,type=pd-balanced \
        --no-shielded-secure-boot \
        --shielded-vtpm \
        --shielded-integrity-monitoring \
        --labels=goog-ec-src=vm_add-gcloud \
        --reservation-affinity=any

    # Connect to VM and install Ollama
    gcloud compute ssh instance-20250126-20250126-170147 --zone=us-central1-c --project=uber-etl-447800 -- \
    'curl -fsSL https://ollama.com/install.sh | sh && ollama run deepseek-r1'
    ```
