import json
import time

def register_server(server_id, stream_url, status='online', latency_ms=20):
    with open('data/servers.json', 'r') as f:
        servers = json.load(f)
    for s in servers:
        if s['id'] == server_id:
            s['stream_url'] = stream_url
            s['status'] = status
            s['latency_ms'] = latency_ms
            s['last_ping'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
            break
    with open('data/servers.json', 'w') as f:
        json.dump(servers, f, indent=2)
    print(f'Registered server {server_id} -> {stream_url}')
