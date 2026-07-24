---
name: synthesize-learning
description: Review the latest active-course MODULE_LOG.md entries, propose a plan for promoting genuinely reusable learning into the repo's durable files, and apply only what the user approves. Manually invoked only.
disable-model-invocation: true
---

# Synthesize recent course notes

Periodically turn recent course notes into durable, reusable capability. Read the newest entries in the active course log, decide what is genuinely worth promoting, and propose a plan. Make no edits until the user approves.

## Hard rules

- **First pass makes no edits.** Only read, analyze, and present a plan. Wait for explicit approval before touching any file.
- **After approval, make only the changes the user approved.** If they approve part of the plan, do only that part.
- **Do not invent facts.** Every proposed change must trace to something actually written in the course notes or already in the repo. If a fact is not there, leave it out.
- **Do not recommend updating every file.** Most passes touch only one or two files. If nothing is worth promoting, say so and propose no changes.
- **Never raise a SKILLS_MATRIX.md score without concrete evidence.** A score change needs a specific evidence statement, per the repo's maintenance rules. Watching or discussing material is not evidence.
- **Distinguish guided practice from independent ability.** Following a course walkthrough once is guided practice. A score reflecting real skill needs repeated, independent application. Call out which one the notes actually support.
- Do not commit or push.

## Steps

1. **Find the active course.** Check [LEARNING_HUB.md](../../../LEARNING_HUB.md) for the current focus. If ambiguous, ask which course to synthesize rather than guessing.

2. **Read the latest log entries.** Open that course's `MODULE_LOG.md` and read the most recent entries (roughly the last few parts/modules, or everything added since the previous synthesis). Note anything marked confusing or unresolved — that is usually not yet reusable capability.

3. **Identify genuinely reusable or important learning.** Separate:
   - **Reusable techniques** — worth a playbook or a KEY_TAKEAWAYS entry.
   - **Terminology** — worth a GLOSSARY definition.
   - **Status or focus changes** — worth a LEARNING_HUB update.
   - **Demonstrated skill with evidence** — possibly worth a SKILLS_MATRIX change.
   - **Completed, verifiable work** — possibly worth a PORTFOLIO entry.
   - **One-off details** that belong only in the log and should not be promoted.

4. **Consider (do not assume) updates to these files.** For each, decide whether the notes justify a change and skip the ones that do not:
   - The active course's `KEY_TAKEAWAYS.md` — for the Kodree course this is `courses/kodree-Codex/KEY_TAKEAWAYS.md`. Each course keeps its own `KEY_TAKEAWAYS.md` inside its own `courses/<course-folder>/` directory; there is no repo-root takeaways file.
   - `playbooks/`
   - `GLOSSARY.md`
   - `LEARNING_HUB.md`
   - `SKILLS_MATRIX.md`
   - `PORTFOLIO.md`

5. **Present a concise proposed update plan.** For each proposed change list: the file, what would be added or changed, and the specific note it comes from. For any SKILLS_MATRIX change, state the evidence and whether it reflects independent ability or only guided practice. List files you deliberately chose not to touch, briefly. Then stop and ask for approval.

6. **After approval, apply only the approved changes.** Follow the repo's writing and accuracy rules. Then report exactly which files changed.

## Finish

Report the full relative path of every file you changed and nothing you did not. Do not commit or push.
