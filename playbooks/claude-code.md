# Playbook: Claude Code

Reusable steps for setting up and running Claude Code on a real project. Distilled from the Kodree Claude Code course.

## Set up Claude Code on a repository

1. Clone the repository and open it in your editor (`code .` if the VS Code command is installed).
2. Establish a baseline: run the project's tests and lint so you know the starting state.
3. Run `/init` to draft a project `CLAUDE.md`. This works best once the codebase has enough structure to inspect — on an empty or trivial repo there's little for it to learn from.
4. Refine the drafted `CLAUDE.md` with project-specific rules and conventions.
5. Create `.claude/settings.json` with permission rules (allow / ask / deny) for the actions you want automated, gated, or blocked.
6. Verify with `/memory` (what's in memory/config) and `/permissions` (active rules).

## Two levels of CLAUDE.md

| File | Scope | Use for |
| --- | --- | --- |
| `~/.claude/CLAUDE.md` | All projects (global) | Personal preferences and defaults |
| `<repo>/CLAUDE.md` | One repository | Project conventions, rules, context |

Keep global preferences out of repo files, and keep project-specific rules out of the global file.

## Permission rules

`.claude/settings.json` supports three intents:

- **allow** — run automatically without asking.
- **ask** — prompt before running.
- **deny** — never run.

Verify the effective rules with `/permissions` after editing.

## Running tasks

- Tasks can run in the foreground or background.
- **Control+B** backgrounds a running task.

## Verify, don't assume

After changing configuration, confirm it took effect with `/memory` and `/permissions` rather than assuming.
