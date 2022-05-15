# Datasets

- `./shapes` = GDA2020 Digital Boundary Files:

  - Statistical Areas Level 2 - 2021 - Shapefile (48.33 MB)
  - Statistical Areas Level 3 - 2021 - Shapefile (34.31 MB)
  - Statistical Areas Level 4 - 2021 - Shapefile (28.45 MB)

  https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files#downloads-for-gda2020-digital-boundary-files

# Run on VM

- Install `pip` dependencies:

  ```
  pip install -r requirements.txt
  ```

- Sync views

  ```
  chmod +x view.sh
  ./view.sh
  ```

- Add `/home/ubuntu/twitter-melb.json` into CouchDB (no hang up):

  ```
  chmod +x upload_hist.sh
  ./upload_hist.sh
  ```

- Twitter search + streaming (no hang up):

  ```
  export bearer=<your-twitter-app-bearer-token>
  chmod +x search_by_*.sh stream_by_*.sh
  ./search_by_destination.sh
  ./search_by_landmark.sh
  ./stream_by_destination.sh
  ./stream_by_landmark.sh
  ```
