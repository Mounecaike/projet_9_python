# 📚 LITRevu

Application Django permettant aux utilisateurs de publier ou de critiquer des livres, de suivre d’autres membres et de consulter un flux personnalisé.

Projet réalisé dans le cadre du parcours **Développeur d’application Python** (OpenClassrooms).

---

## 🚀 Fonctionnalités principales

- 🔐 Authentification : inscription, connexion, déconnexion  
- 🎟️ Création, modification et suppression de **tickets**  
- 📝 Création, modification et suppression de **reviews**  
- 📰 Flux d’actualités personnalisé (utilisateur + abonnements)  
- 👥 Système d’abonnement (follow / unfollow)  
- 🚫 Blocage et déblocage d’utilisateurs  
- 💬 Messages de confirmation et d’erreur clairs

---

## ⚙️ Installation

```bash
git clone https://github.com/<votre-nom-utilisateur>/LITRevu.git
cd LITRevu
python -m venv env
env\Scripts\activate  # sous Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Accès : http://127.0.0.1:8000
```
````
📁 Structure du projet
csharp
Copier le code
LITRevu/
├── accounts/   # Authentification utilisateur
├── posts/      # Tickets et critiques
├── follows/    # Abonnements et blocages
├── templates/  # Fichiers HTML
├── static/     # CSS
└── manage.py
````
## 🧠 Technologies
- Python 3.13
- Django 5.2
- SQLite
- HTML / CSS / Django templates
- Pillow (gestion des images)

## 💡 Bonnes pratiques
- Découpage logique par application (accounts, posts, follows)
- Sécurisation avec @login_required et @require_POST
- Gestion centralisée des messages (django.contrib.messages)
- Respect PEP8 & conventions Django
- Fichiers statiques configurés dans static/

### 👤 Auteur
- Jordan Lachaume
- Développeur d’application Python

## 📄 Licence
- Projet pédagogique — librement réutilisable à des fins d’apprentissage.