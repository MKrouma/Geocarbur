CREATE TABLE "stations" (
  "id" integer PRIMARY KEY,
  "nom" varchar,
  "operateur" varchar,
  "shop" bool,
  "adresse" varchar,
  "geometrie" geom,
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

ALTER TABLE "stations" ADD FOREIGN KEY ("id") REFERENCES "villes" ("id");
