# Project instructions

## Standing rule
- Show every change as a diff before editing. Apply it only after approval.
- Never post content to Instagram or YouTube without the user's explicit approval for that specific video.
- Content comes from the user's content calendar. The calendar runs in 28-day cycles.

## Agent roles (enforced)
Research and review are delegated by role. The main agent does file changes itself.

| Role | Agent | Model | Allowed actions |
|------|-------|-------|-----------------|
| Research | `researcher` | claude-haiku-5-5 | Read, search, fetch. No edits. |
| Implementation | main agent (no subagent) | — | Edit, write, run commands in scope, only after the user approves the diff. |
| Review | `reviewer` | claude-opus-5-5 | Read and inspect only. No edits. |

## Enforcement
- Anything that changes files is done by the main agent, after the user approves the diff.
- Before any Edit or Write, show the full diff in the chat and wait for the user's approval. This applies to files in the repo and to new files outside the repo.
- Every change passes through `reviewer` before it is reported as done.
- `reviewer` never edits. If it finds problems, it reports them and the main agent fixes them.
- An agent does not approve its own work.
- Report test and command output as it actually appeared. Do not claim success without it.
