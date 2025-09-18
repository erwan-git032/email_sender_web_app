# Email Sender Web App

Cette application Flask permet d’envoyer des emails avec pièce jointe via Gmail, en toute sécurité grâce à l’utilisation d’un mot de passe d’application et de variables d’environnement.

## Fonctionnalités

- Envoi d’email via une interface web simple
- Ajout de pièce jointe (fichiers)
- Sécurité : email et mot de passe d’application stockés dans un fichier `.env` ou des variables d’environnement
- Messages de succès ou d’erreur affichés à l’utilisateur

## Installation

1. Clonez le projet ou téléchargez les fichiers.
2. Installez les dépendances Python :
   ```
   pip install -r requirements.txt
   ```
3. Créez un mot de passe d’application Gmail ([voir la documentation Google](https://support.google.com/mail/answer/185833?hl=fr)).
4. Configurez le fichier `.env` à la racine du projet :
   ```
   GMAIL_SENDER_EMAIL=VOTRE_ADRESSE_GMAIL
   GMAIL_APP_PASSWORD=VOTRE_MOT_DE_PASSE_APPLICATION
   ```
5. Lancer l’application :

```bash
python app.py
```

Accès à l’application : [http://localhost:5000](http://localhost:5000)

## Technologies utilisées

* Python 3.11
* Flask
* smtplib
* Jinja2 (templates HTML)
* HTML, CSS
*python-dotenv


## Utilisation

1. Lancez l’application :
   ```
   python app.py
   ```
2. Ouvrez votre navigateur à l’adresse [http://127.0.0.1:5000](http://127.0.0.1:5000)
3. Remplissez le formulaire, ajoutez une pièce jointe si besoin, et envoyez votre email.

## Sécurité

- **Ne partagez jamais votre mot de passe d’application.**
- Utilisez toujours des variables d’environnement ou un fichier `.env` (jamais en clair dans le code).
- L’email d’envoi est aussi stocké dans le fichier `.env` pour plus de flexibilité et de sécurité.

## Dépendances

Voir `requirements.txt`.

## Structure du projet

```
email_sender/
│
├── app.py
├── email_utils.py
├── requirements.txt
├── .env
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── uploads/
└── README.md
```

## Auteur
Axel ATAYI
GitHub : [https://github.com/erwan-git032](https://github.com/erwan-git032)


