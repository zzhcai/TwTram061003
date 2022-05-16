# Summary

Cloud computing technologies make it simple for data analysis in a scalable manner. In this project, we examine the livability of Melbourne through the lens of Yarra Trams. A sentiment analysis of recent and past tweets (2014-2015) associated with trams in Melbourne, juxtaposed with AURIN statistics, may help shed some light on this topic. We use Ansible to automatically configure resources and deploy services on the Melbourne Research Cloud. Data are stored on virtual machines in CouchDB Docker containers, and several nodes across form a cluster that offers replication for fault tolerance. Following that, a map visualization is available for the public to view our latest, real-time analytical results.

More `README.md` can be found in `ansible/`, `harvester/`, and `webapp/`.

# Repo Structure

```
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
|   |           ├──── harvester/tasks/main.yaml          # Install harvester pip requirements
|   |           ├──── mount-volume/tasks/main.yaml       # Auto-mount volume
|   |           └──── webapp/tasks/main.yaml             # Install webapp apt dependencies
|   ├──── vars/
|   |     ├──── openstack.yaml                           # Instance vars for creation
|   |     └──── setup.yaml                               # Instance IPs
|   ├──── .gitignore
|   ├──── README.md
|   ├──── ansible.cfg                                    # Config: host_key_checking = False
|   ├──── cloud.key.pub                                  # SSH public key
|   ├──── main.yaml                                      # Ansible playbook
|   └──── run-mrc.sh
├── harvester/
|   ├──── shapes/                                        # GDA2020 Digital Boundary Files
|   |     └──── ..
|   ├──── README.md
|   ├──── methods.py
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
├── webapp/
|   ├──── public/
|   |     ├──── jsons/                                   # GeoJSON shapefiles
|   |     |     ├──── sa2.json
|   |     |     ├──── sa3.json
|   |     |     └──── sa4.json
|   |     └──── ..
|   └──── ..
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md                                            <-- YOU ARE HERE
```
