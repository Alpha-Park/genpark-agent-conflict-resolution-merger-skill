import sys, difflib
sys.stdout.reconfigure(encoding='utf-8')

class AgentConflictResolutionMergerClient:
    """
    3-Way differential merge engine for concurrent multi-agent outputs.
    Compares common base with Agent A and Agent B modifications,
    resolves non-overlapping edits automatically, and isolates conflicting spans.
    """
    def __init__(self):
        pass

    def merge_documents(self, base_text, agent_a_text, agent_b_text):
        base_lines = base_text.splitlines()
        a_lines = agent_a_text.splitlines()
        b_lines = agent_b_text.splitlines()

        merged_lines = []
        conflicts = []
        max_len = max(len(base_lines), len(a_lines), len(b_lines))

        for i in range(max_len):
            base_l = base_lines[i] if i < len(base_lines) else None
            a_l = a_lines[i] if i < len(a_lines) else None
            b_l = b_lines[i] if i < len(b_lines) else None

            # Case 1: Both agents made identical modifications or identical omissions
            if a_l == b_l:
                if a_l is not None:
                    merged_lines.append(a_l)
            # Case 2: Only Agent B changed the line
            elif a_l == base_l:
                if b_l is not None:
                    merged_lines.append(b_l)
            # Case 3: Only Agent A changed the line
            elif b_l == base_l:
                if a_l is not None:
                    merged_lines.append(a_l)
            # Case 4: True concurrent conflict
            else:
                conflicts.append({
                    "line_number": i + 1,
                    "base_content": base_l,
                    "agent_a_content": a_l,
                    "agent_b_content": b_l
                })
                merged_lines.append(f"<<<<<<< AGENT_A (Line {i+1})")
                if a_l is not None: merged_lines.append(a_l)
                merged_lines.append("=======")
                if b_l is not None: merged_lines.append(b_l)
                merged_lines.append(f">>>>>>> AGENT_B")

        clean_merge = (len(conflicts) == 0)

        return {
            "status": "success",
            "clean_merge": clean_merge,
            "conflicts_count": len(conflicts),
            "conflicts": conflicts,
            "total_merged_lines": len(merged_lines),
            "merged_text": "\n".join(merged_lines)
        }
