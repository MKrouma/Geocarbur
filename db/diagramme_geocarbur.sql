CREATE TABLE "stations" (
  "id" integer PRIMARY KEY,
  "nom" varchar,
  "operateur" varchar,
  "shop" bool,
  "adresse" varchar,
  "geometry" geometry,
  "ville_id" integer,
  "created_at" timestamp
);

CREATE TABLE "villes" (
  "id" integer PRIMARY KEY,
  "nom" varchar,
  "superficie" integer,
  "population" integer,
  "pays" varchar,
  "created_at" timestamp
);

ALTER TABLE "stations" ADD FOREIGN KEY ("ville_id") REFERENCES "villes" ("id");
