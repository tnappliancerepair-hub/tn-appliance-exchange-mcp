"""Is a ZIP covered for in-home appliance repair by TN Appliance Exchange?

Python 3.8+, standard library only:  python3 check_zip.py 37013
"""
import json
import sys
import urllib.request

MCP_URL = "https://tnapplianceexchange.net/mcp"


def call(method, params, req_id=1):
    body = json.dumps({"jsonrpc": "2.0", "id": req_id, "method": method, "params": params}).encode()
    req = urllib.request.Request(MCP_URL, data=body, headers={
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "User-Agent": "tn-appliance-mcp-example/1.0 (+https://github.com/tnappliancerepair-hub/tn-appliance-exchange-mcp)",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def main():
    zip_code = sys.argv[1] if len(sys.argv) > 1 else "37013"
    call("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                        "clientInfo": {"name": "check-zip-example", "version": "1.0"}})
    res = call("tools/call", {"name": "check_service_area", "arguments": {"zip": zip_code}}, 2)
    data = json.loads(res["result"]["content"][0]["text"])
    print(data.get("message") or data)


if __name__ == "__main__":
    main()
