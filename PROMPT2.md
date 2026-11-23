# Prompt

Écris un script Python autonome nommé `server.py` qui démarre un serveur web local sur le port `8080`. Utilise uniquement la bibliothèque standard de Python : aucune dépendance externe (par exemple Flask ou FastAPI).

## Exigences

- Le serveur sert une page HTML complète avec le CSS intégré, sans fichier ni ressource externe.
- La page affiche uniquement le texte visible `hello zuzu`, centré horizontalement et verticalement dans la fenêtre. Utilise Flexbox ou CSS Grid et adapte la mise en page à la taille de l’écran.
- Le serveur écoute sur toutes les interfaces réseau (`0.0.0.0`) afin d’être accessible depuis les autres appareils du réseau local, sur le port `8080`.
- Au démarrage, affiche clairement `http://localhost:8080` pour l’accès depuis cet ordinateur ainsi que l’adresse LAN de cet ordinateur au format `http://<adresse-IP-LAN>:8080`, déterminée avec la bibliothèque standard.
- Indique brièvement que l’adresse LAN est à ouvrir depuis un appareil connecté au même réseau et que le pare-feu peut devoir autoriser les connexions entrantes sur le port `8080`.
- L’arrêt avec `Ctrl+C` est géré proprement : le serveur se ferme sans traceback ni message d’erreur.

Fournis le contenu complet de `server.py`, prêt à être exécuté avec `python3 server.py`.