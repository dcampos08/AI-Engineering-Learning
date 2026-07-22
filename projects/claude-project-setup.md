# Project: Set up Claude Code on a real project

Write-up of the Kodree assignment "Set up Claude Code on a real project."

## Goal

Configure Claude Code inside a real repository and complete a full contribute-to-upstream workflow, from cloning through opening a pull request.

## Status

**Done** — assignment completed. Specific dates, repository names, and the PR link are not recorded here yet; add them if/when appropriate (and only if non-sensitive).

## What I did

### Environment
- Installed and configured the VS Code `code .` command.
- Installed nvm, Node.js, and npm.

### Repository setup
- Cloned a GitHub repository.
- Created and switched to a feature branch.
- Established a working baseline by running the project's tests and lint before changing anything.

### Project workflow
- Used `npm install`, `npm test`, `npm run lint`, and `npm run dev`.
- Confirmed that `package.json` defines what the npm commands run.
- Noted that Node can discover test files by convention, e.g. `tests/users.test.js`.

### Claude Code configuration
- Used Claude Code inside the real repository.
- Ran `/init` to draft a project `CLAUDE.md`, then refined it.
- Created `.claude/settings.json` with allow, ask, and deny permission rules.
- Verified configuration with `/memory` and `/permissions`.
- Practiced foreground and background tasks with Control+B.

### Git and GitHub
- Used `git status`, `git add`, `git diff --cached`, `git commit`, and `git push`.
- Opened a pull request from my fork to the original course repository.

## What I learned

- `/init` is most useful once a codebase has enough structure to inspect.
- `~/.claude/CLAUDE.md` is global across projects; a repository `CLAUDE.md` is project-specific.
- Establishing a green baseline first makes it clear what your own changes affect.

## Links

_To add (only if non-sensitive): repository, branch, and pull request URLs._

## Related

- [playbooks/claude-code.md](../playbooks/claude-code.md)
- [playbooks/git-and-github.md](../playbooks/git-and-github.md)
- [courses/kodree-claude-code/MODULE_LOG.md](../courses/kodree-claude-code/MODULE_LOG.md)
