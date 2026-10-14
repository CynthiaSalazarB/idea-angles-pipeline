# Idea Angles Pipeline sync agent

Two-way sync between the local SQLite idea store (canonical) and the Notion **Idea Bank**.
The News Dashboard sync moved to its own repo, [news-digest](https://github.com/CynthiaSalazarB/news-digest), on 2026-10-14.

## Idea Bank (Phase 2b)

A Notion database with these properties (one-time manual setup; connect your integration to it):

| Property | Type | Options / notes |
|----------|------|-----------------|
| Title | title | Working title from angles agent |
| Idea ID | rich_text | Idea Angles Pipeline UUID — required for pull sync |
| Brand fit % | number | 0–100 advisory score (not a gate) |
| Brand fit note | rich_text | One-line why |
| Lane | select | Your brand lanes (e.g. `Build`, `Create`, `Reflect`) |
| Status | select | `Inbox`, `Approved`, `Rejected`, `Edit requested` |
| Source | select | `cli_capture`, `telegram` |
| Angles | rich_text | Formatted angle summary |
| Synced | date | Last push time |

```powershell
# Push angled ideas to Notion (or: python orchestrator.py --steps ideas-push)
python -m agents.sync_agent.run ideas push

# Pull Approved/Rejected status from Notion (or: --steps ideas-pull)
python -m agents.sync_agent.run ideas pull
```

Requires `NOTION_IDEA_BANK_DATABASE_ID` in `.env`.

### Remote capture drain (GCP Telegram bot)

The VM's SQLite is a **capture inbox, never canonical** — local `data/cynthia.db` is the one true ideas store (future notes/embedding/memory modules index it). Drain the inbox whenever you like:

```powershell
# 1. Fetch a copy of the VM's DB
gcloud compute scp <vm-name>:~/idea-angles-pipeline/data/cynthia.db data/remote/cynthia-vm.db

# 2. Merge it into the local DB (upsert by UUID, newer updated_at wins, idempotent)
python -m agents.sync_agent.run ideas pull-remote --from data/remote/cynthia-vm.db
```

Strictly one-way: local never pushes ideas back to the VM. Re-running is always safe.

