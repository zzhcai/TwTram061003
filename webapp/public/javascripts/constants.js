webapp = {
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
  aurindb: {
    sa2: ['sa2_emotion_14_db', 'sa2_income_14_db'],
    sa3: ['sa3_mental_14_db', 'sa3_abs_population_14_db', 'sa3_travel_16_db'],
    sa4: ['sa4_population_14_db'],
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
  aurinDBURL(db) {
    return `${this.server}${db}/_all_docs?include_docs=true`;
  },
};
