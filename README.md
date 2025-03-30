# Geocarbur
Geocarbur est une plateforme de visualisation et d'analyse des stations de carburant dans la ville d'Abidjan.

## Fonctionnalités
- Informations sur les stations;
- Cartographie des stations;
- Station la plus proche (distance, temps);
- Calcul d'itinéraire.

## Workflow
- Collecte de données (ok);
- Nettoyage de données (ok);
- Conception de la base de données (ok);
- Implémentation de la BD (ok);
- Developpement du backend;
- Développement du frontend.


## Backend
```
python3 -m venv .venv
.venv\Scripts\activate.bat
python -c "import sys;print(sys.executable)"
pip install flask
pip freeze > requirements.txt
flask --app app run (flask run)
```