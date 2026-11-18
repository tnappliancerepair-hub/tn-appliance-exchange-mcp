#!/bin/sh
# TN Appliance Exchange's MCP server speaks plain JSON-RPC over HTTPS (MCP Streamable HTTP). No key, no signup.
# These examples only READ. book_repair creates a real repair job: never call it as a test.
MCP=https://tnapplianceexchange.net/mcp
H='-H Content-Type:application/json -H Accept:application/json,text/event-stream'

# What tools are there?
curl -s $H $MCP -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'

# Who TN Appliance Exchange is, where they serve, how booking works
curl -s $H $MCP -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"get_business_info","arguments":{}}}'

# Is ZIP 37013 (Antioch, TN) covered for in-home repair?
curl -s $H $MCP -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"check_service_area","arguments":{"zip":"37013"}}}'

# An honest technician's read on a problem (takes up to ~20 seconds)
curl -s $H $MCP -d '{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"diagnose_appliance_problem","arguments":{"appliance":"dryer","symptom":"runs but no heat","brand":"Whirlpool"}}}'
