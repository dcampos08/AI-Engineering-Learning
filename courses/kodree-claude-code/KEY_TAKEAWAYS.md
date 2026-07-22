# Kodree Claude Code — Key Takeaways

Distilled lessons from the course so far (through Part 18). These are verified takeaways, not a summary of undocumented modules.

## Workflow discipline

- **Establish a baseline before changing anything.** Run tests and lint first so you know the project starts green and can attribute any breakage to your changes.
- **`package.json` is the source of truth for commands.** What `npm test`, `npm run lint`, and `npm run dev` actually do is defined there.
- **Use feature branches.** Do work on a branch created and switched to for that task, not on the main line.

## Git and GitHub

- Know the four distinct things: original repository, fork, local clone, and branch. They are not interchangeable.
- The core loop: `git status` → `git add` → `git diff --cached` (review what's staged) → `git commit` → `git push`.
- Contributing back to an upstream project goes through a pull request from your fork to the original repo.

## Claude Code configuration

- **Two levels of `CLAUDE.md`:** `~/.claude/CLAUDE.md` applies globally across all projects; a repository `CLAUDE.md` applies to just that project. Use each for the right scope.
- **`/init` inspects the codebase to draft a project `CLAUDE.md`,** so it's most useful once the codebase has enough structure to inspect.
- **`.claude/settings.json` controls permissions** with allow, ask, and deny rules.
- **Verify configuration** with `/memory` and `/permissions` rather than assuming it took effect.
- **Foreground vs background tasks** — Control+B backgrounds a running task.

## Promoted to playbooks

- [Claude Code playbook](../../playbooks/claude-code.md)
- [Git and GitHub playbook](../../playbooks/git-and-github.md)
