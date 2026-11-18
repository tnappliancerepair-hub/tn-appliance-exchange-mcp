// Ask TN Appliance Exchange's MCP server for an honest technician's read on an appliance problem.
// Node 18+ (built-in fetch), no packages:  node diagnose.mjs dryer "runs but no heat" Whirlpool
const MCP_URL = 'https://tnapplianceexchange.net/mcp';

async function call(method, params, id = 1) {
  const r = await fetch(MCP_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Accept: 'application/json, text/event-stream' },
    body: JSON.stringify({ jsonrpc: '2.0', id, method, params }),
  });
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.json();
}

const [appliance = 'dryer', symptom = 'runs but no heat', brand = ''] = process.argv.slice(2);
await call('initialize', { protocolVersion: '2025-06-18', capabilities: {}, clientInfo: { name: 'diagnose-example', version: '1.0' } });
const res = await call('tools/call', { name: 'diagnose_appliance_problem', arguments: { appliance, symptom, brand } }, 2);
const data = JSON.parse(res.result.content[0].text);
console.log(data.safety + '\n');
console.log(data.diagnosis);
