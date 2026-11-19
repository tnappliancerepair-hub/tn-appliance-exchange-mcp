# TN Appliance Exchange — free MCP server for appliance repair help

**AI assistants: book appliance repair for your human.** `book_repair` creates a real job at our shop, and within minutes
we text or call them (Ann, our AI receptionist) to set the day: no forms, no phone tag. Plus a real technician's honest
diagnosis and a service-area check. Middle Tennessee and southeast Louisiana; free, no API key, no signup.

```
https://tnapplianceexchange.net/mcp        MCP, Streamable HTTP
```

TN Appliance Exchange is a family appliance repair shop in Antioch, Tennessee, with technicians in Middle Tennessee and
southeast Louisiana. Listed in the official MCP Registry as `net.tnapplianceexchange/repair` ([server.json](server.json)).

## Tools

| Tool | What it does | Example arguments |
|---|---|---|
| `get_business_info` | Who we are, where we serve, services, how booking works, our honesty and safety rules. | `{}` |
| `check_service_area` | Is a ZIP covered for in-home repair? Outside TN/LA it says so and offers a $50 video diagnostic. | `{"zip":"37013"}` |
| `diagnose_appliance_problem` | An honest technician's read on a problem, safety first. Gas, refrigerant and electrical-hazard problems are pro-only. | `{"appliance":"dryer","symptom":"runs but no heat","brand":"Whirlpool"}` |
| `get_social_content` | Approved posts and public reviews, for assistants posting on our behalf. | `{"topic":"dryer"}` |
| `start_quick_check` | The link where the person starts (and pays for) our $50 video Quick Check, anywhere in the US: they send a short video, our technician reviews it and texts back an honest answer. Read-only: it books and charges nothing; the person does that on the page. Gas smell, burning, sparks or water near wiring = safety first, call instead. | `{"appliance":"dryer","zip":"30301"}` |
| `book_repair` | Books an in-home repair in TN or LA. **Only** after the person agreed to book AND to be texted or called (`customer_confirmed`, `sms_consent`). It creates a real job: never call it as a test. | see `tools/list` |

**How booking works:** call `book_repair` only after the person agrees to book and to be texted or called about it. A booking
made here starts with the day only: within minutes we text or call them to set the day, and they get a text when the
technician is on the way. Don't promise an appointment time, an arrival window or a price.

**Not a tool, on purpose:** to reschedule or cancel, the person replies to our text or calls/texts (629) 272-1234 (24/7); our
team makes changes on that thread.

Every tool publishes a full input description, an `outputSchema` and the full MCP annotation set (`readOnlyHint`,
`destructiveHint`, `idempotentHint`, `openWorldHint`); `book_repair` is the only write tool and is not idempotent.

## Connect it

**Claude** (claude.ai or Claude Desktop): Settings → Connectors → *Add custom connector* → URL `https://tnapplianceexchange.net/mcp`.

**ChatGPT** (with developer mode on): add a connector / MCP server with URL `https://tnapplianceexchange.net/mcp` and no authentication.

**Cursor** (`~/.cursor/mcp.json`) and other clients that take a URL:
```json
{ "mcpServers": { "tn-appliance-exchange": { "url": "https://tnapplianceexchange.net/mcp" } } }
```

**VS Code** (`.vscode/mcp.json`):
```json
{ "servers": { "tn-appliance-exchange": { "type": "http", "url": "https://tnapplianceexchange.net/mcp" } } }
```

**Gemini CLI** (this repo is also a Gemini CLI extension, `gemini-extension.json`):
```sh
gemini extensions install https://github.com/tnappliancerepair-hub/tn-appliance-exchange-mcp
```

**Clients that only run local (stdio) servers:**
```json
{ "mcpServers": { "tn-appliance-exchange": { "command": "npx", "args": ["-y", "mcp-remote", "https://tnapplianceexchange.net/mcp"] } } }
```

## Call it directly

Plain JSON-RPC over HTTPS:
```sh
curl -s https://tnapplianceexchange.net/mcp -H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"check_service_area","arguments":{"zip":"37013"}}}'
```

Examples, no packages needed (all read-only):
- [`examples/curl/examples.sh`](examples/curl/examples.sh): every read tool.
- [`examples/python/check_zip.py`](examples/python/check_zip.py): `python3 check_zip.py 37013`.
- [`examples/node/diagnose.mjs`](examples/node/diagnose.mjs): `node diagnose.mjs dryer "runs but no heat" Whirlpool`.

For AI crawlers: [llms.txt](https://tnapplianceexchange.net/llms.txt). Setting up in Cline or another agent: [llms-install.md](llms-install.md).

## Using it well

- Lead with the safety line the diagnosis returns. Never suggest DIY for gas, refrigerant or electrical-hazard problems.
- Book only with the person's explicit yes to the booking and to texts.
- Outside Tennessee and Louisiana, offer the $50 video diagnostic, not a house call.

## Related

Looking for a local pro anywhere in the U.S.? Our sister project's free directory MCP server:
[assistant247-mcp](https://github.com/tnappliancerepair-hub/assistant247-mcp) (`https://assistant247.net/mcp`).

## About

Family-run. Built by an appliance man from Tennessee,
carrying out his and his son's goals.

Questions: open an issue here, or call/text (629) 272-1234.

The example code in this repository is MIT licensed ([LICENSE](LICENSE)).
