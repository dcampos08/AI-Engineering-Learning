# Kodree Claude Code — Key Takeaways

Distilled lessons from the course so far (through Part 19). These are verified takeaways, not a summary of undocumented modules.

## Workflow discipline

- **Establish a baseline before changing anything.** Run tests and lint first so you know the project starts green and can attribute any breakage to your changes.
- **`package.json` is the source of truth for commands.** What `npm test`, `npm run lint`, and `npm run dev` actually do is defined there.
- **Use feature branches.** Do work on a branch created and switched to for that task, not on the main line.
- **Plan before executing on anything non-trivial.** Have Claude lay out its approach first, push back on one point, then let it work. Trivial edits like a rename or a typo fix don't need it.

## Git and GitHub

- Know the four distinct things: original repository, fork, local clone, and branch. They are not interchangeable.
- The core loop: `git status` → `git add` → `git diff --cached` (review what's staged) → `git commit` → `git push`.
- Contributing back to an upstream project goes through a pull request from your fork to the original repo.

## Sessions and context

- A session runs in the folder you open it in, so where you start Claude decides what it can work on.
- Approved edits are real and persist; exiting never loses your work, and sessions are saved so you can resume.
- Match the re-entry to the task: `claude --continue` (`-c`) to carry on the last session, `/resume` to pick an older one, a fresh session when the task is unrelated. When a session's memory gets cluttered, `/clear` (or a new session) often sharpens answers.
- Keep `/clear` (empty but stay), `/exit` (leave), and `--continue` (reopen) straight — they're easy to confuse.

## Prompts and the edit loop

- Specific prompts beat vague ones: name the place, the problem, and the result you want.
- Claude proposes a diff and writes nothing until you approve. Reviewing the diff is the real work; a big change is just many small reviewable steps.

## CLAUDE.md discipline

- `CLAUDE.md` is the standing note Claude reads at the start of every session; it's how you avoid re-explaining the project each time.
- Fill it with the three buckets — **commands, conventions, architecture** — and nothing that's obvious from the code or true only today.
- Make rules specific and actionable ("pull anything over 30 lines into its own function"), not vague ("write clean code"). Trim aggressively: every extra line dilutes the rules that matter.
- **Put a rule in the smallest place where it's true:** personal file (`~/.claude/CLAUDE.md`) for your taste, project file for team agreements, nested files for one corner of the codebase. Use `/memory` to see what's actually loaded.
- Keep secrets and large documents out — secrets belong in environment variables, big docs stay where they live with a pointer. Some needs want a hook, skill, or MCP instead of a rule.

## Permissions

- Permissions decide what Claude may do without asking: **allow** (safe/routine), **ask** (eyeball first), **deny** (never). If both allow and deny apply, **deny wins**.
- Shared rules go in `.claude/settings.json` (committed); personal ones in `.claude/settings.local.json`. Deny anything irreversible or sensitive; allow the safe commands you keep approving so the prompts fall away. `/permissions` shows and edits them.

## Working style choices

- **Headless one-shot mode** (`claude -p`) answers a single question and exits; pipe files in with `|` and request `--output-format json` when a program will read the result. Multi-round work belongs in a full session.
- **Editor vs terminal:** the editor sees your open file and selection (so "this function" works); the terminal is better for quick commands and scripts. Background slow commands with `Ctrl+B` and check them with `/bashes`.
- **Output styles** match Claude's voice to your goal: Default to ship, Explanatory to learn a codebase, Learning to build your own skills. The wrong style has a real cost (length, and Learning pausing to hand you code).

## Claude Code configuration

- **Two levels of `CLAUDE.md`:** `~/.claude/CLAUDE.md` applies globally across all projects; a repository `CLAUDE.md` applies to just that project. Use each for the right scope.
- **`/init` inspects the codebase to draft a project `CLAUDE.md`,** so it's most useful once the codebase has enough structure to inspect.
- **`.claude/settings.json` controls permissions** with allow, ask, and deny rules.
- **Verify configuration** with `/memory` and `/permissions` rather than assuming it took effect.
- **Foreground vs background tasks** — Control+B backgrounds a running task.

## Promoted to playbooks

- [Claude Code playbook](../../playbooks/claude-code.md)
- [Git and GitHub playbook](../../playbooks/git-and-github.md)
