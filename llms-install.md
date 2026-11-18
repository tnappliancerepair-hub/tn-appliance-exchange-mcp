# Installing the TN Appliance Exchange MCP server

This is a **remote** MCP server. There is nothing to clone, build or install, and no API key.

- URL: `https://tnapplianceexchange.net/mcp`
- Transport: Streamable HTTP
- Auth: none

## Cline

Add this to `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "tn-appliance-exchange": {
      "type": "streamableHttp",
      "url": "https://tnapplianceexchange.net/mcp",
      "disabled": false
    }
  }
}
```

If your Cline version only runs local (stdio) servers, use the mcp-remote bridge (needs Node 18+):

```json
{
  "mcpServers": {
    "tn-appliance-exchange": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://tnapplianceexchange.net/mcp"]
    }
  }
}
```

## Check it works

Ask: "Is ZIP 37013 covered for appliance repair?" The assistant should call `check_service_area`.

## Rules

- `book_repair` creates a real repair job. Call it only after the person agrees to book AND to be texted. Never as a test.
- Lead with the safety line the diagnosis returns; gas, refrigerant and electrical-hazard problems are pro-only.
- Don't promise an appointment time.
