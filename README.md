# Cloud Gaming Live Sessions & Server Registry (`cloudgame-db-sessions`)

Live status registry and directory of all 10 running Cloud Gaming runners, their active Cloudflare stream URLs, player counts, and latency statistics.

## Structure
- `data/servers.json`: Live registry of game runners and active tunnel URLs
- `schema/session_schema.json`: JSON Schema for game session records
- `scripts/register_server.py`: Dynamic server registration helper
