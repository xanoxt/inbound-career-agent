# TOOLING — configuring the search provider

> This pack is **model-agnostic**: it runs on any tool-using agent (Claude Code, open-weights setups, etc.). The only external dependency is a **web-search provider** for playbooks `01-market-sense` and `05-conversation-prep`. Configure at least one before those run.

---

## Providers

| Provider | Cost | Needs | When |
|---|---|---|---|
| **Tavily** (default) | Free tier 1000 searches/mo | `TAVILY_API_KEY` | Start here — ample for one person |
| **DeepSeek websearch MCP** | Pay-as-you-go (very cheap) | `DEEPSEEK_API_KEY` + balance | Cheaper scaling / second provider |

Selection + fallback rule lives in `AgentContract.xml` (`tool id="search"`): default Tavily; on quota exhaustion or error, fall back to DeepSeek; **never scrape** as a workaround — report to the user instead.

## 1. Tavily (default)

1. Get an API key at **tavily.com** (free tier = 1000 searches/month).
2. Expose the key to the agent as the env var **`TAVILY_API_KEY`**.
3. Two integration styles — pick what your agent supports:
   - **MCP server** (cleanest for Claude Code): add Tavily's MCP server to `.mcp.json` (template below).
   - **Direct API**: the agent calls Tavily's REST search endpoint with the key from env.

## 2. DeepSeek websearch MCP (optional scaling)

1. Repo: **https://github.com/lyumeng/websearch-deepseek**
2. Get a DeepSeek API key; ensure you have a balance.
3. Expose as **`DEEPSEEK_API_KEY`**.
4. Add the MCP server to `.mcp.json` (template below).

## Claude Code `.mcp.json` template

> Template only — confirm exact `command`/`args`/transport from each project's README before relying on it.

```json
{
  "mcpServers": {
    "tavily": {
      "command": "npx",
      "args": ["-y", "tavily-mcp"],
      "env": { "TAVILY_API_KEY": "<your-key>" }
    },
    "deepseek-websearch": {
      "command": "npx",
      "args": ["-y", "websearch-deepseek"],
      "env": { "DEEPSEEK_API_KEY": "<your-key>" }
    }
  }
}
```

Place at the project root (or user-level config per your tool). Only one provider is required; include both if you want automatic fallback.

## Security

- Keys go in env / a secret store — **never in the repo**. `.gitignore` already excludes `.env`, `.env.*`, `*.key`.
- For Claude Code, the agent reads keys from the MCP server env / your shell — don't paste keys into playbook files.

## Open-weights setups

If the user later moves to a local/open-weights model: the pack itself is unchanged (plain MD/XML). The search provider is still cloud-based (Tavily or DeepSeek), so ensure the runtime can reach it. Everything else (playbooks, rituals, file-io) is local and model-agnostic.

## Troubleshooting

- **No search results / quota hit:** switch provider (DeepSeek), or wait for the monthly reset. Don't scrape.
- **MCP server not found by the agent:** confirm `.mcp.json` location and that the package name matches the project's current README.
- **Green-path user has no provider configured:** playbooks 01/05 will degrade gracefully — they should report "search not configured; set a provider per TOOLING.md" rather than fail silently.
