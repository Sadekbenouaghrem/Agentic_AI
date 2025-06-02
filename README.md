# 🤖 Agentic AI – Autonomous Web Agents with Django

Un projet Django complet combinant des agents autonomes, l'API OpenAI, REST/GraphQL, Celery & Redis pour la génération et la gestion de tâches IA. Conçu pour des applications web intelligentes, sécurisées et extensibles.

---

## 🛠️ Fonctionnalités principales

- **Modèles Django** : `Agent`, `Task`, `Interaction` avec relations explicites (ForeignKey, ManyToMany), validations et contraintes.
- **API REST sécurisée** : Django REST Framework + JWT OAuth2 + permissions par rôle.
- **Schéma GraphQL** : Types, queries, mutations (avec Graphene-Django).
- **Interface web** : Templates HTML + Tailwind CSS (agent list, task list, task detail, création).
- **Sécurité** : CORS, CSRF, CSP, nettoyage des entrées.
- **Traitement asynchrone** : Celery + Redis pour les tâches IA autonomes.
- **Intégration OpenAI** : Utilisation de l'API AutoGPT pour générer et enregistrer des réponses dans `Interaction`.

---

## 🚀 Installation rapide

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-utilisateur/agentic-ai.git
cd agentic-ai

python -m venv venv
source venv/bin/activate  # ou `venv\Scripts\activate` sous Windows

pip install -r requirements.txt

SECRET_KEY=your-secret-key
DEBUG=True
OPENAI_API_KEY=your-openai-key

python manage.py migrate
python manage.py runserver

celery -A agentic_ai worker --loglevel=info
agentic_ai/
│
├── agent/               # App principale (modèles, vues, urls, templates)
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tasks.py         # Tâches Celery (avec OpenAI)
│   ├── graphql/         # Schéma GraphQL
│   └── templates/       # Templates HTML
│
├── agentic_ai/          # Réglages Django (settings.py, urls.py)
├── manage.py
├── requirements.txt
└── README.md

