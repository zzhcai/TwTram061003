# Summary

COMP90024 Cluster and Cloud Computing - 2022 Semester 1 - Project 2: Melbourne the Most Liveable City...?

# Repo Structure

```
├── TwitterHarvester/
|   ├──── shapes/                                        # GDA2020 Digital Boundary Files
|   |     └──── ..
|   ├──── README.md
|   ├──── methods.py
|   ├──── requirements.txt
|   ├──── search.py                                      # Twitter search
|   ├──── search_by_destination.sh
|   ├──── search_by_landmark.sh
|   ├──── stream.py                                      # Twitter streaming
|   ├──── stream_by_destination.sh
|   ├──── stream_by_landmark.sh
|   ├──── upload_hist.py                                 # Adding historic tweets to database
|   ├──── upload_hist.sh
|   ├──── view.py                                        # Sync CouchDB views
|   └──── view.sh
├── ansible/
|   ├──── roles/
|   |     ├──── openstack/
|   |     |     ├──── common/tasks/main.yaml
|   |     |     ├──── images/tasks/main.yaml
|   |     |     ├──── instance/tasks/main.yaml
|   |     |     ├──── key/tasks/main.yaml
|   |     |     ├──── security-group/tasks/main.yaml
|   |     |     ├──── volume-snapshot/tasks/main.yaml
|   |     |     └──── volume/tasks/main.yaml
|   |     └──── setup/
|   |           ├──── couch/
|   |           |     ├──── tasks/main.yaml              # Setup CouchDB containers and clusters
|   |           |     └──── templates/main.yaml          # Docke-compose template
|   |           ├──── docker/tasks/main.yaml             # Install Docker dependencies
|   |           ├──── git/tasks/main.yaml                # Pull code
|   |           ├──── mount-volume/tasks/main.yaml       # Auto-mount volume
|   |           └──── webapp/tasks/main.yaml             # Install webapp dependencies
|   ├──── vars/
|   |     ├──── openstack.yaml                           # Instance vars for creation
|   |     └──── setup.yaml                               # Instance IPs
|   ├──── .gitignore
|   ├──── README.md
|   ├──── ansible.cfg                                    # Config: host_key_checking = False
|   ├──── cloud.key.pub                                  # SSH public key
|   ├──── main.yaml                                      # Ansible playbook
|   └──── run-mrc.sh
├── webapp/
|   └──── ..
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md                                            <-- YOU ARE HERE
```
