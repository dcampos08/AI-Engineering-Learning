# Glossary

Terms and definitions collected while learning. Keep entries short and in my own words. Add terms as they come up.

## Git and GitHub

- **Original repository** — the canonical upstream repo owned by its maintainer(s).
- **Fork** — a personal copy of another repository hosted under your own account. Lets you make changes and propose them back via pull request.
- **Local clone** — a copy of a repository downloaded to your machine with `git clone`.
- **Branch** — a movable pointer to a line of commits, used to develop changes in isolation from the main line.
- **Feature branch** — a branch created for a specific piece of work, kept separate until it's ready to merge.
- **Pull request (PR)** — a proposal to merge changes from one branch (often on a fork) into another repository or branch, with review and discussion.
- **`git status`** — shows the working tree state: staged, unstaged, and untracked changes.
- **`git add`** — stages changes for the next commit.
- **`git diff` (no arguments)** — shows unstaged changes to tracked files only. New untracked files don't appear until staged; use `git status` to see them, or `git add` then `git diff --cached`.
- **`git diff --cached`** — shows the changes that are staged (about to be committed).
- **`git commit`** — records staged changes as a new commit.
- **`git push`** — uploads local commits to a remote repository.

## Node and npm

- **nvm** — Node Version Manager; installs and switches between Node.js versions.
- **Node.js** — a JavaScript runtime that runs JS outside the browser.
- **npm** — Node's package manager; installs dependencies and runs scripts.
- **`package.json`** — the manifest that defines a project's dependencies and the scripts that npm commands (`test`, `lint`, `dev`, etc.) run.
- **`npm install`** — installs the dependencies listed in `package.json`.
- **Test file discovery** — Node/test runners can automatically find test files by convention, such as `tests/users.test.js`.
- **Working baseline** — running tests and lint before changing a project, so you know the starting state is green before you touch anything.

## Claude Code

- **`~/.claude/CLAUDE.md`** — the user-level (global) instructions that apply across all projects.
- **Repository `CLAUDE.md`** — project-level instructions that apply only within that repo. Complements the global file.
- **`/init`** — drafts a project `CLAUDE.md` by inspecting the codebase. Most useful once a codebase has enough structure to inspect.
- **`.claude/settings.json`** — project configuration, including permission rules.
- **Permission rules (allow / ask / deny)** — control which actions Claude Code can take automatically, must ask about, or is blocked from.
- **`/memory`** — command to view and verify what Claude Code has in memory / configuration.
- **`/permissions`** — command to view and verify the active permission rules.
- **Foreground vs background tasks** — Claude Code can run tasks in the foreground or background; Control+B backgrounds a running task.

_Add AI/ML terms (evaluation, RAG, agents, MLOps, etc.) here as they're learned._
