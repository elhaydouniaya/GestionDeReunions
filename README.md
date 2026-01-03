# Gestion des Réunions TP - Odoo

Ce projet est un module Odoo conçu pour pour la gestion simplifiée des réunions. Il permet de planifier des réunions, d'assigner des responsables, de définir des lieux et de suivre le statut de chaque session.

## Fonctionnalités

- **Gestion des Réunions** : Création, modification et suppression de réunions.
- **Détails de la Réunion** : Sujet, Responsable, Date et Heure, Lieu.
- **Suivi de Statut** : Brouillon, Planifiée, Terminée, Annulée.
- **Ordre du Jour** : Champ texte pour détailler les points à aborder.

## Structure du Projet

```text
.
├── addons/
│   └── tp_gestion_reunions/    # Dossier du module Odoo
├── rapport.pdf                 # Rapport du projet
└── README.md                   # Ce fichier
```

## Installation avec Docker

1. Clonez ce dépôt.
2. Assurez-vous d'avoir Docker et Docker Compose installés.
3. Lancez les conteneurs :
   ```bash
   docker-compose up -d
   ```
4. Accédez à Odoo via `http://localhost:8069`.
5. Connectez-vous avec `admin` / `admin`.
6. Allez dans **Applications**, recherchez "TP - Gestion des Réunions" et installez-le.

## Auteur
- Aya Elhaydouni
