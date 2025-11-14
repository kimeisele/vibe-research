# 🔄 Auto-Sync Setup: vibe-agency → vibe-research

## Zweck

Dieses Setup synchronisiert automatisch Code-Änderungen von `vibe-agency` (Haupt-Repo mit ausführbarem Code) nach `vibe-research` (Test & Validierung Repo).

## Was wird synchronisiert?

- ✅ `agency_os/` - Komplette Agent-Struktur, Knowledge Bases, State Machines
- ✅ `core_orchestrator.py` - Workflow-Engine (falls vorhanden)
- ✅ `handlers/` - Phase Handler (planning, coding, qa, etc.)
- ✅ `vibe-cli.py` - CLI Updates
- ✅ `requirements.txt` - Merged Dependencies

## Setup in `vibe-agency` Repo

### Schritt 1: Trigger-Workflow erstellen

Erstelle diese Datei in `vibe-agency`:

**`.github/workflows/trigger-research-sync.yml`**

```yaml
name: Trigger Research Sync

on:
  push:
    branches:
      - main
      - develop
    paths:
      - 'agency_os/**'
      - 'core_orchestrator.py'
      - 'handlers/**'
      - 'vibe-cli.py'

  workflow_dispatch:

jobs:
  trigger-sync:
    runs-on: ubuntu-latest

    steps:
      - name: Trigger vibe-research sync
        run: |
          curl -X POST \
            -H "Accept: application/vnd.github.v3+json" \
            -H "Authorization: token ${{ secrets.RESEARCH_SYNC_TOKEN }}" \
            https://api.github.com/repos/kimeisele/vibe-research/dispatches \
            -d '{"event_type":"sync-to-research"}'
```

### Schritt 2: GitHub Token erstellen

1. Gehe zu GitHub Settings → Developer Settings → Personal Access Tokens
2. Erstelle Token mit Scope: `repo` (Full control of private repositories)
3. In `vibe-agency` Repo Settings → Secrets → Actions
4. Erstelle Secret: `RESEARCH_SYNC_TOKEN` mit dem Token

### Schritt 3: Testen

```bash
# Im vibe-agency Repo
git add .github/workflows/trigger-research-sync.yml
git commit -m "Add auto-sync to vibe-research"
git push

# Check Actions Tab für Status
```

---

## Manueller Sync (Fallback)

Falls automatischer Sync nicht funktioniert, verwende das manuelle Script:

```bash
# Im vibe-research Repo
./scripts/manual-sync-from-vibe-agency.sh
```

Oder GitHub Actions manuell triggern:

1. Gehe zu `vibe-research` → Actions
2. Wähle "Sync from vibe-agency"
3. Click "Run workflow"
4. Wähle Branch aus `vibe-agency` (default: main)

---

## Wie es funktioniert

```
┌─────────────────┐
│  vibe-agency    │
│  (Haupt-Repo)   │
└────────┬────────┘
         │ push/merge
         │
         ▼
┌─────────────────────────────┐
│ GitHub Action               │
│ trigger-research-sync.yml   │
└────────┬────────────────────┘
         │ repository_dispatch
         │
         ▼
┌─────────────────────────────┐
│  vibe-research              │
│  sync-from-vibe-agency.yml  │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ 1. Clone vibe-agency        │
│ 2. Copy agency_os/          │
│ 3. Copy Python files        │
│ 4. Commit & Push            │
└─────────────────────────────┘
```

---

## Vorteile

✅ **Automatisch** - Kein manuelles Copy-Paste
✅ **Selektiv** - Nur relevante Files werden synced
✅ **Versioniert** - Jeder Sync ist ein Git Commit
✅ **Transparent** - Sync-Historie in GitHub Actions
✅ **Fallback** - Manueller Trigger wenn nötig

---

## Troubleshooting

### Sync funktioniert nicht?

1. **Check Permissions:**
   ```bash
   # Prüfe ob Token gültig ist
   curl -H "Authorization: token YOUR_TOKEN" \
     https://api.github.com/repos/kimeisele/vibe-research
   ```

2. **Check Workflow Logs:**
   - `vibe-agency` → Actions → "Trigger Research Sync"
   - `vibe-research` → Actions → "Sync from vibe-agency"

3. **Manueller Fallback:**
   ```bash
   cd /path/to/vibe-research
   ./scripts/manual-sync-from-vibe-agency.sh
   ```

### File-Konflikte?

Der Sync überschreibt immer mit vibe-agency Version. Falls du lokale Änderungen in vibe-research hast:

```bash
# Sichere lokale Änderungen
git stash

# Warte auf Sync

# Re-apply lokale Änderungen
git stash pop
```

---

## Status

- ✅ Workflow in `vibe-research` erstellt
- ⏳ Workflow in `vibe-agency` muss erstellt werden
- ⏳ GitHub Token muss erstellt werden
- ⏳ Erster Sync muss getestet werden
