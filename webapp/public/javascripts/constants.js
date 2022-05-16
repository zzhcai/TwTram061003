webapp = {
  server: "http://172.26.130.6:5984/",
  db: "historic_melb",
  mel_db: "melb_db",
  view_avg: "sa_sum_count",
  view_max: "max_id",
  view_min: "min_id",
  view_sum: "sum_count",
  view_sa_max: "sa_max_id",
  view_sa_min: "sa_min_id",
  geoJSON: (n) => `/jsons/${n}.json`,
  sa2gl: {
    sa2: 3,
    sa3: 2,
    sa4: 1,
    all: 0,
  },
  viewURL(design, view, sa) {
    return `${this.server}${this.db}/_design/${design}/_view/${view}?group_level=${this.sa2gl[sa]}`;
  },
  hisViewURL(design) {
    return `${this.server}${this.db}/_design/${design}/_view/sa_sum_count`;
  },
  melViewURL(design, view) {
    return `${this.server}${this.mel_db}/_design/${design}/_view/${view}`;
  },
};
