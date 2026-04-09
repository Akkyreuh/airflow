Q1 : 

LocalExecutor : 
Execute toutes les taches dans un processus en local, sur la même machine.
Bien pour un environnement de dev

CeleryExecutor : 
Répartie les tâches sur les différent workers
Bon pour de la "petite" prod

KubernetesExecutor : Créé un pod par tâche. C'est parfait pour les besoins de scalabilité de la prod // pour s'appliquer sur les services duppliqués
Bon pour de la production multi service, qui nécessite kubernetes

Q2 : 

Avec ./dags:/opt/airflow/dags : 

Le dossier local est reproduit dans le conteneur. Quand on modifie le le fichier de notre dag, ça envoie les modifications sur airflow et quand on déclenche le dag ça a pris les modifications en compte

Sans mapping il faudrait re build l'image a chaques fois

En théorie les workers n'auraient pas la même version du dag s'il y a eu des modifs et ce serait le bordel

Q3 : 

cathcup = true ferait que l'airflow va rattraper toutes les executions du dag (1 par jours manquant)

l'idempotence permet de ne pas avoir à duppliquer les entrées du même jours qui contiennent les mêmes valeurs

Q4

Déjà si on utilisait UTC théoriquement on pourrait avoir els bonnes heures en faisant un mapping mais justement ça deviendrait trop problématique lorsqu'on change d'heure
-> En plus ça pourrait causer une dupplication // un prélèvement de donnée en moins selon quel changement d'heure on fait 

