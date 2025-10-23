# 📦 Modèle de dépôt — enseignement-section-inf-module-template

Ce dépôt sert de **modèle standard** pour tous les modules ICT de la section INF.

Il automatise la génération de la documentation, la publication web et la synchronisation FTP.  
Avant toute utilisation, suivez attentivement les étapes ci-dessous.

Une fois la mise en place du projet faite, ces deux documents vous aideront à construire votre cours :

- [🔗 Cheatsheet Markdown](aide-memoire/cheatsheet.md)
- [🔗 Cheatsheet en-têtes](aide-memoire/tardis.md)

---

## ⚙️ Étapes initiales de création du module

1. **Créer un nouveau dépôt** à partir de ce template.  
   Respecter la convention de nommage :  
   `I###-Libellé-du-module` ou `C###-Libellé-du-module`  
   Exemple :  
   - `I182-Implementer-la-securite-systeme` (module école)  
   - `C109-Exploiter-et-surveiller-des-services-dans-le-cloud-public` (module inter-entreprise)

2. **Ajouter la variable d’environnement `ICT_MODULE`** dans votre dépôt.  
   - Exemple de valeur : `182`  
   - Cette variable est indispensable pour que les GitHub Actions fonctionnent.

3. **Demander à la section** de préparer votre structure FTP sur :  
   👉 `ftp://enseignement.section-inf.ch`

---

## 🌍 Variables d’environnement à définir dans votre dépôt

| **Nom** | **Rôle** | **Exemple** |
|----------|-----------|-------------|
| `ICT_MODULE` | Définit le numéro du module ICT utilisé dans le menu de navigation du site | `182` |

> ⚠️ Cette variable est **obligatoire**.  
> Sans elle, les workflows GitHub échoueront dès la phase de build.

---

## 🏗️ Variables d’environnement déjà configurées au niveau de l’organisation

Ces variables sont gérées globalement par la section INF.

> 🛈 Si votre dépôt vient d’être créé, **demandez à la section** d’ajouter votre dépôt au *scope* de ces variables.

*(Aucune variable organisationnelle publique spécifique n’est requise pour l’instant.)*

---

## 🔐 Secrets organisationnels déjà configurés

| **Nom du secret** | **Rôle** |
|--------------------|----------|
| `FTP_USERNAME` | Nom d’utilisateur FTP pour `enseignement.section-inf.ch` |
| `FTP_PASSWORD` | Mot de passe associé au compte FTP |

> 🛈 Si votre dépôt est nouveau, **demandez à la section** d’inclure votre dépôt dans le *scope* de ces secrets.  
> Sans cela, la synchronisation FTP échouera.

---

## 🧱 Préparation du serveur FTP `enseignement.section-inf.ch`

Ces opérations sont **manuelles** et effectuées par la section INF lors de la mise en place d’un nouveau module.

1. Ajouter le module à `index.php` et le mettre **actif** (un module peut être présent mais temporairement masqué).  
2. Ajouter une photo `numero_de_module.png` (348×192 px) dans le dossier `/images`.  
3. Créer un dossier du module dans `/moduleICT` :
   ```
   /moduleICT/<numéro_du_module>/
   ```
4. Créer les sous-dossiers suivants :
   ```
   /cours
   /presentations
   /exercices
   /tardis
   ```
5. Dans chacun de ces sous-dossiers, créer un fichier JSON vide :
   | **Dossier** | **Fichier à créer** |
   |--------------|---------------------|
   | `cours` | `.ftp-sync-support.json` |
   | `presentations` | `.ftp-sync-slidedeck.json` |
   | `exercices` | `.ftp-sync-exercices.json` |
   | `tardis` | `.ftp-sync-ui.json` |

> Ces fichiers de synchronisation sont utilisés par les GitHub Actions.  
> Ils permettent de ne synchroniser que le **delta des modifications**.  
> Sans ces fichiers initiaux, la première exécution peut échouer.

---

## ✅ Bonnes pratiques

- Ne modifiez **jamais** les noms de variables (`ICT_MODULE`, `FTP_USERNAME`, etc.).  
- Vérifiez vos **droits de dépôt** avant d’activer les workflows.  
- Si une GitHub Action échoue avec  
  `❌ ICT_MODULE non défini`,  
  allez dans :  
  [`Settings → Actions → Variables`](./settings/secrets/actions)

---

**Responsable du modèle :** Section INF – École Technique des Métiers de Lausanne  
**Référence interne :** TARDIS — Teaching And Resources Development for Integrated Sequences  
