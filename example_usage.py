from client import AgentConflictResolutionMergerClient
import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    merger = AgentConflictResolutionMergerClient()
    print("=== AGENT CONFLICT RESOLUTION MERGER ===")

    base = "Project: Autonomous Fleet\nStatus: Planning\nBudget: $50,000\nLead: Alice"
    agent_a = "Project: Autonomous Fleet\nStatus: In Progress\nBudget: $50,000\nLead: Alice" # Agent A updated status
    agent_b = "Project: Autonomous Fleet\nStatus: Planning\nBudget: $75,000\nLead: Alice"     # Agent B updated budget

    res = merger.merge_documents(base, agent_a, agent_b)
    print()
    print(f"Clean Auto-Merge: {res['clean_merge']} | Conflict Count: {res['conflicts_count']}")
    print("Merged Output (Both concurrent non-overlapping edits preserved):")
    for line in res['merged_text'].split("\n"):
        print("  " + line)

if __name__ == "__main__":
    main()
