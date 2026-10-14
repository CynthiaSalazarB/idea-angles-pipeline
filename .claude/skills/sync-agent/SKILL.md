---
name: sync-agent
description: Run Idea Angles Pipeline Notion sync for the Idea Bank. Use when pushing or pulling ideas to Notion, draining VM captures, fixing sync errors, or configuring NOTION_API_KEY and the Idea Bank database ID.
---

# Sync Agent (Idea Bank)

The News Dashboard sync moved to the news-digest repo on 2026-10-14.

## Commands

```powershell
.venv\Scripts\Activate.ps1
python -m agents.sync_agent.run ideas push
python -m agents.sync_agent.run ideas pull
python -m agents.sync_agent.run ideas push --dry-run

# Drain GCP Telegram-bot captures into the canonical local DB (one-way, idempotent)
gcloud compute scp <vm-name>:~/idea-angles-pipeline/data/cynthia.db data/remote/cynthia-vm.db
python -m agents.sync_agent.run ideas pull-remote --from data/remote/cynthia-vm.db
```

Requires `NOTION_IDEA_BANK_DATABASE_ID` in `.env`.

Schema: [agents/sync_agent/README.md](../../agents/sync_agent/README.md).

## Troubleshooting

- **401 / invalid token**: use the **Internal Integration Token** from [notion.so/my-integrations](https://www.notion.so/my-integrations), starts with `secret_` or `ntn_`. MCP OAuth does not replace it for Python sync.
- **401 / unauthorized**: integration not connected to the Idea Bank database.

## Related

- [agents/sync_agent/README.md](../../agents/sync_agent/README.md)
