This is a forked version of https://github.com/CccT31/comp90024.

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
|   ├──── view.sh
|   └──── aurin_to_db.py                                 # Upload downloaded AURIN Json to couchdb
├── webapp/
|   ├──── public/
|   |     ├──── jsons/                                   # GeoJSON shapefiles
|   |     |     ├──── sa2.json
|   |     |     ├──── sa3.json
|   |     |     └──── sa4.json
|   |     ├──── javascripts/                             # Script files to run in the browser
|   |     |     └──── index.js
|   |     └──── ..
|   ├──── route/                                         # Server side scripts to redirect requests
|   |     ├──── db.js
|   |     └──── index.js
|   ├──── views/                                         # Pug templates that can be rendered into HTML
|   |     └──── index.pug
|   ├──── app.js                                         # The main script running on server
|   └──── ..
├── .gitattributes
├── .gitignore
├── LICENSE
└── README.md                                            <-- YOU ARE HERE
```

# Marks

- 35/40 (87.5%), after weighing each individual's contribution

- The report contains a very thorough user-guide that is easy to follow. Additionally, the system architecture is explained in excellent detail. However, the report does not contain a discussion on the advantages and disadvantages of using MRC in the context of twitter data analysis conducted in this project (although some aspects of this discussion are present in various sections).

  You showed a good working demonstration of the deployment of your cloud-based solution via Ansible. The structure of the playbook is well-setup for a dynamic deployment, with very little hard-coded variables. It was good to see Docker used to setup a CouchDB cluster. However, it would have been nice to see an ability to provision added resources in the playbook in order to enable dynamic horizontal scaling.
  It was also good idea to introduce separate security groups for the CouchDB intra-cluster communication, SSH access, and webapp HTTP(S) requests. Good job with achieving added automation via cloning the GitHub repo and retrieving the new instance IPs dynamically.
  The MapReduce functions were written very well - it was great to see custom reduce functions that extract tweets with minimum and maximum metric values.

  The harvester code is written cleanly and commented adequately. There are enough try/except statements at various points in the code in order to prevent untimely harvester termination. Very interesting usage of SenticNet and Hourglass and Emotions model to categorize four emotional aspects of a tweet. Interestingly, some of the example tweets with the minimum/maximum scores of these four metrics (and polarity) seem to have been miscategorized. It would have been great to see how a different language model would have performed. While you deployed multiple harvesters, these should have been deployed in separate Docker containers rather than running as scripts on the instances. Duplicate tweets are correctly taken care of via unique tweet ids. Great job at avoiding hard-coding the API credentials within the harvesters and instead passing in a token as an argument at harvester startup. Also, expediting the analysis by pre-process tweets before storing them into the database was a nice job.

  The webapp design is a little bit basic but quite functional. This is fine, since this subject is not HCI-focused. For geo-wise comparison, instead of the used having to compare two heat maps side-by-side, it would have been great to see plots of the correlation b/w the sentiment data extracted from Tweets and AURIN-derived data. The ability to conduct a temporal analysis of tweet sentiment was a great addition to the webapp.

  The Git repo is very-well structured, and has plenty of commits from all group members, indicating good teamwork. The README is well-written and contains the necessary information regarding project configuration to allow others to extend/reproduce your work. The presentation video showed all of the pertinent elements of the system in excellent detail. It was pleasing to see a presentation of all aspects of the project, from system architecture to Ansible deployment. Overall, this was great work and showed that all team members contributed to the project and worked well together.

  \- Prof. Richard O. Sinnott
