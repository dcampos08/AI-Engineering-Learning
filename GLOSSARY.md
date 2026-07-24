# Glossary

Terms and definitions collected while learning. Keep entries short and in my own words. Add terms as they come up.

## Git and GitHub

- **Original repository** — the canonical upstream repo owned by its maintainer(s).
- **Fork** — a personal copy of another repository hosted under your own account. Lets you make changes and propose them back via pull request.
- **Local clone** — a copy of a repository downloaded to your machine with `git clone`.
- **`git clone`** — the one-time download that creates the local folder. You clone a given repo once; after that you never clone it again unless you delete the folder.
- **`git checkout`** — switches which version of the files is in your working folder, by pointing the repo at a different branch or commit. It downloads nothing and creates no new folder; it rewrites the contents of the folder you're already in. (`git switch` is the newer, narrower command for the branch-switching case.)
- **`git pull`** — fetches new commits from the remote and merges them into your current branch. This, not `checkout`, is what gets you an updated copy of someone else's work.
- **`git fetch`** — downloads new commits from the remote without changing your working files. `git pull` is roughly `fetch` plus merge.
- **Remote** — the hosted repository your local clone is linked to (usually on GitHub), named `origin` by default. `git remote -v` prints its URL, which is how you confirm what a local folder is a clone of.
- **Branch** — a movable pointer to a line of commits, used to develop changes in isolation from the main line.
- **Feature branch** — a branch created for a specific piece of work, kept separate until it's ready to merge.
- **Pull request (PR)** — a proposal to merge changes from one branch (often on a fork) into another repository or branch, with review and discussion.
- **`git status`** — shows the working tree state: staged, unstaged, and untracked changes.
- **`git add`** — stages changes for the next commit.
- **`git diff` (no arguments)** — shows unstaged changes to tracked files only. New untracked files don't appear until staged; use `git status` to see them, or `git add` then `git diff --cached`.
- **`git diff --cached`** — shows the changes that are staged (about to be committed).
- **`git commit`** — records staged changes as a new commit.
- **`git push`** — uploads local commits to a remote repository.
- **Git archaeology** — using Claude to search past commits and their diffs to answer how the code got the way it is.

## Node and npm

- **nvm** — Node Version Manager; installs and switches between Node.js versions.
- **Node.js** — a JavaScript runtime that runs JS outside the browser.
- **npm** — Node's package manager; installs dependencies and runs scripts.
- **`package.json`** — the manifest that defines a project's dependencies and the scripts that npm commands (`test`, `lint`, `dev`, etc.) run.
- **`npm install`** — installs the dependencies listed in `package.json`.
- **Test file discovery** — Node/test runners can automatically find test files by convention, such as `tests/users.test.js`.
- **Working baseline** — running tests and lint before changing a project, so you know the starting state is green before you touch anything.

## Claude Code — general concepts

- **Session** — one conversation with Claude Code, running in the folder you started it in. That folder is Claude's workspace for the whole session. Claude saves sessions on exit so they can be resumed.
- **Prompt** — a message you send Claude: an instruction or question, written in plain everyday language.
- **Diff** — the side-by-side view of your current file next to Claude's proposed change, shown before anything is written. You accept, reject, or ask for a different approach.

## Claude Code — planning

- **Plan Mode** — a mode where Claude researches and proposes an approach instead of editing files. Nothing is written while you're in it. Reach it by pressing `Shift+Tab` until the mode indicator shows it.
- **Plan** — the written approach Claude produces in Plan Mode. It can look convincing and still be wrong, so reading it critically is your job, not a formality.
- **The three moves on a plan** — approve it, edit it, or send it back to rethink the approach. Editing means staying in Plan Mode and describing what you want; Claude rewrites the plan to match, as many times as you need.

## Claude Code — sessions

- **`/exit`** — closes Claude Code cleanly and returns you to your normal terminal. Ends the conversation, not the work; approved changes are already saved. `Ctrl+D` does the same.
- **`claude --continue` / `-c`** — reopens your most recent session with its context intact, so you carry on mid-thought. (Launched from the shell, but it's about re-entering a session.)
- **`/resume`** — lists your past sessions so you can reopen a specific earlier one (not just the last).
- **`/help`** — shows the full list of slash commands available inside a session.
- **`Ctrl+B`** — moves a running command to the background so the session frees up while the command keeps going.
- **`/bashes`** — lists the background commands currently running. Each backgrounded command gets an ID and is monitored, so you can check its output without stopping it.

## Claude Code — command line

- **Headless / one-shot mode** — running Claude for a single self-contained question that prints one answer and returns you to the terminal. Also how Claude fits into scripts and automation.
- **`claude -p '...'`** — the `-p` flag runs a one-shot prompt: Claude answers once and exits.
- **Pipe (`|`)** — feeds one command's output into the next. Example: `cat error.log | claude -p 'explain this error'` sends the file's contents into a one-shot question.
- **`--output-format json`** — makes a one-shot answer come back as structured JSON that another program can parse. The doorway to automated workflows.

## Claude Code — context and memory

- **Context** — Claude's working memory, a limited amount held in mind at once. When it fills up (often after a long, wandering session), answers can drift.
- **`/context`** — shows how full the current context is.
- **`/clear`** — empties the conversation but keeps you in the same session (a clean slate). You lose the old chat. Distinct from `/exit` (leaves entirely) and `claude --continue` (reopens the last conversation).
- **`/compact`** — summarizes the session, keeping key state (decisions, file paths, what's left) while dropping the noise, instead of wiping it entirely like `/clear`. Proactive alternative to waiting for auto-compact.

## Claude Code — configuration

- **`~/.claude/CLAUDE.md`** — the user-level (global/personal) instructions that apply across all your projects and are seen only by you.
- **Repository `CLAUDE.md`** — project-level instructions committed to the repo, so every teammate's Claude reads the same rules. Complements the global file.
- **Nested `CLAUDE.md`** — a `CLAUDE.md` inside a subfolder, holding rules for that one part of the project. Not read at session start; Claude picks it up only when it works with a file in that folder, and its rules layer on top of what's already loaded. Guideline: put a rule in the smallest place where it's true.
- **`/init`** — drafts a project `CLAUDE.md` by inspecting the codebase. Most useful once a codebase has enough structure to inspect.
- **`#` rule shortcut** — start a line with `#` and type a rule; Claude saves it into a `CLAUDE.md` (asking which file). Turns an in-the-moment correction into a lasting rule.
- **`.claude/settings.json`** — shared project configuration, committed to the repo (including permission rules), so the whole team shares the same guardrails.
- **`.claude/settings.local.json`** — local configuration that stays on your machine for personal tweaks.
- **Permission rules (allow / ask / deny)** — control which actions Claude Code can take automatically, must ask about, or is blocked from. If an action is both allowed and denied, **deny wins**. Deny is the hard block; deny anything irreversible or sensitive.
- **`/memory`** — lists every `CLAUDE.md` currently loaded and lets you open them to edit. First check when a rule is or isn't being followed.
- **`/permissions`** — shows and edits the active permission rules.
- **Foreground vs background tasks** — Claude Code can run tasks in the foreground or background; `Ctrl+B` backgrounds a running task.

## Claude Code — output styles

- **Output style** — how Claude talks to you while it works (same underlying Claude). Loads when a session starts, so a change applies next session or right after `/clear`; then stays with the project.
- **Default** — quick and to the point; makes the change and moves on. Best when you know what you want.
- **Explanatory** — does the work and explains its choices with short "Insights". Best for understanding an unfamiliar codebase.
- **Learning** — hands-on; explains as it goes and leaves small pieces for you to write, marked `TODO(human)`. Best for building your own skills.
- **`/config`** — menu where you set the output style (Output style → choose one). Can also be set with `"outputStyle": "..."` in `.claude/settings.local.json`.
- **`/output-style:new`** — creates a custom output style from a description of the voice you want.

## Claude Code — models

- **Opus / Sonnet / Haiku** — the three model tiers. Opus is the most capable but slowest and priciest. Haiku is the fastest and cheapest, and shines on simpler, well-defined work. Sonnet sits in between and handles most real work well — the sensible default.
- **`/model <model name>`** — switches models mid-session. Move up the tier when a task needs more judgment, and down when it's mechanical.
- **Opusplan** — a built-in hybrid mode: Opus plans, then Sonnet executes the plan. Start with `claude --model opusplan` or pick it from the `/model` list.

## Claude Code — beyond CLAUDE.md (introduced, covered later)

- **Hook** — an automatic action that fires on an event, often to block something (e.g. stopping a commit that contains a secret before it's saved).
- **Skill** — a saved set of steps Claude can run on demand, the same way every time (e.g. a "scaffold a new API endpoint our way" routine triggered by name).
- **MCP connection** — plugs Claude into an outside system so it can read or act there (e.g. fetching a customer's record from your database).

_Add AI/ML terms (evaluation, RAG, agents, MLOps, etc.) here as they're learned._
