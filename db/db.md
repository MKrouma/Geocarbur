# Databse
Conception et implémentation de la base de données.

## Conception
Nous allons utiliser la méthode MERISE à savoir : 
- Modèle conceptuel;
- Modèle logique;
- Modèle physique.

### Modèle cocneptuel
Entité 1 : Station
Entité 2 : Ville
Relation  : n Station - 1 ville (n,1)

Propriétés station : nom, opérateur, shop, adresse, géometrie.
Propriétés ville : nom, superficie, population, pays.

## Implémentation
Utilise le code sql généré par dbdiagram. 

Créer la db
Ensuite, on crée la base de donnée `geocarbur_db`, on installe l'extension postgis depuis pgadmin. 

Populate la db
```
INSERT INTO public.villes(id, nom, superficie, population, pays)
VALUES (1, 'Abidjan', 12545, 5320000, 'Côte d"Ivoire');

INSERT INTO public.villes(id, nom, superficie, population, pays, created_at)
VALUES (2, 'Yamoussoukro', 35090, 500000, 'Côte d"Ivoire', '2025-03-12 21:00:00');
```

Change column name
```
ALTER TABLE public.stations
RENAME COLUMN geometrie TO geometry;
```

Stations avec des shops
```
SELECT *
FROM public.stations
WHERE shop=TRUE;
```


Jointure Stations & Ville 
```
select s.nom, v.nom 
from public.stations as s
inner join public.villes as v
on s.ville_id = v.id;
```

INSERT INTO villes (id, nom, superficie, population, pays, created_at)
VALUES (1, 'Abidjan', 2119, 6321017, 'Côte d"Ivoire', '2025-03-19');


To do 
- Ajouter ville_id dans la station table;
- Nettoyer la data avec les attributs de la stations
- Ingestion de la donnée depuis le PostGIS Bundle
- Faire quelques première requêtes spatiales (voir une station, trouver la station la plus proche etc avec les ST Functions.)