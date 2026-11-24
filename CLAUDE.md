# Project instructions

## Standing rule
- Show every change as a diff before editing. Apply it only after approval.
- Never post content to Instagram or YouTube without the user's explicit approval for that specific video.
- Content comes from the user's content calendar. The calendar runs in 28-day cycles.

## Agent roles (enforced)
Delegate by role. Do not do a role's work in the main agent when a subagent exists for it.

| Role | Agent | Model | Allowed actions |
|------|-------|-------|-----------------|
| Research | `researcher` | claude-haiku-5-5 | Read, search, fetch. No edits. |
| Implementation | `implementer` | claude-sonnet-5-5 | Edit, write, run commands in scope. |
| Review | `reviewer` | claude-opus-5-5 | Read and inspect only. No edits. |

## Enforcement
- Anything that changes files goes to `implementer`.
- Every change passes through `reviewer` before it is reported as done.
- `reviewer` never edits. If it finds problems, it reports them and the implementer fixes them.
- An agent does not approve its own work.
- Report test and command output as it actually appeared. Do not claim success without it.
