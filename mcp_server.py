import sys, json
from client import AgentConflictResolutionMergerClient
sys.stdout.reconfigure(encoding='utf-8')

def handle_mcp():
    merger = AgentConflictResolutionMergerClient()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps({"status": "ready", "skill": "genpark-agent-conflict-resolution-merger-skill"}))
        return
    req = json.loads(sys.stdin.read() or "{}")
    base = req.get("base_text", "")
    a = req.get("agent_a_text", "")
    b = req.get("agent_b_text", "")
    res = merger.merge_documents(base, a, b)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    handle_mcp()
