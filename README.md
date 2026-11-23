# hello-toto

Petit serveur web Python qui affiche **hello toto** au centre de la page. Il écoute sur toutes les interfaces réseau et utilise uniquement la bibliothèque standard de Python : aucune dépendance à installer.

## Prérequis

- Python 3
- Le port `8081` disponible sur la machine

## Démarrer le serveur

Depuis le dossier du projet, lancez :

```bash
python3 server.py
```

Le terminal indique les adresses d’accès locale et réseau. Pour ouvrir le site sur le même ordinateur, rendez-vous sur <http://localhost:8081>.

Pour arrêter le serveur, revenez au terminal et appuyez sur `Ctrl+C`.

## Utiliser depuis un autre appareil

Connectez l’autre appareil au même réseau local que l’ordinateur qui héberge le serveur, puis ouvrez dans son navigateur l’adresse LAN affichée au démarrage, par exemple `http://192.168.1.42:8081` (remplacez l’adresse par celle indiquée dans votre terminal).

Si la page ne s’ouvre pas, vérifiez que les appareils sont sur le même réseau et que le pare-feu de l’ordinateur autorise les connexions entrantes sur le port `8081`.

## Démarrer en arrière-plan (Linux/macOS)

```bash
nohup python3 server.py > server.log 2>&1 &
echo $! > server.pid
```

Consultez `server.log` pour retrouver l’adresse LAN annoncée. Pour arrêter ce processus :

```bash
kill "$(cat server.pid)"
rm server.pid
```

## Vérification rapide

Avec `curl`, vérifiez que le serveur répond et renvoie la page :

```bash
curl -i http://localhost:8081/
```

Une réponse `200 OK` indique que la page est accessible. Le serveur sert la page à `/` et `/index.html`.
