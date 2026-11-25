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
| Review | `reviewer` | claude-opus-5-5 | Read and inspect only. No edits. |

## Enforcement
- Changes to files are made by the main agent, after the user approves the diff.
- Sonnet (claude-sonnet-5-5) is called only when the user asks for it, for edits or implementation work.
- Every change passes through `reviewer` before it is reported as done.
- `reviewer` never edits. If it finds problems, it reports them and the main agent fixes them, or Sonnet if the user asks.
- An agent does not approve its own work.
- Report test and command output as it actually appeared. Do not claim success without it.
