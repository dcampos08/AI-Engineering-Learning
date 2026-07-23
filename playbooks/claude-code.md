# Playbook: Claude Code

Reusable steps for setting up and running Claude Code on a real project. Distilled from the Kodree Claude Code course.

## Set up Claude Code on a repository

1. Clone the repository and open it in your editor (`code .` if the VS Code command is installed).
2. Establish a baseline: run the project's tests and lint so you know the starting state.
3. Run `/init` to draft a project `CLAUDE.md`. This works best once the codebase has enough structure to inspect — on an empty or trivial repo there's little for it to learn from.
4. Refine the drafted `CLAUDE.md` with project-specific rules and conventions.
5. Create `.claude/settings.json` with permission rules (allow / ask / deny) for the actions you want automated, gated, or blocked.
6. Verify with `/memory` (what's in memory/config) and `/permissions` (active rules).

## Where CLAUDE.md rules live

Put a rule in the smallest place where it's true.

| File | Scope | Use for |
| --- | --- | --- |
| `~/.claude/CLAUDE.md` | All projects (global, only you) | Personal preferences and defaults |
| `<repo>/CLAUDE.md` | One repository (shared via commit) | Project conventions, rules, context |
| `<subfolder>/CLAUDE.md` | One part of the project | Rules for that area only |

Keep global preferences out of repo files, and keep project-specific rules out of the global file. A nested (subfolder) `CLAUDE.md` isn't read at session start — Claude loads it only when working with a file in that folder, and its rules layer on top of what's already loaded. Run `/memory` to see which files are actually loaded.

## Write rules that get followed

- Cover the three buckets: **commands** (build/test/run/lint), **conventions** (how you like things done), **architecture** (where the important pieces live).
- Make each rule specific and actionable. "Keep functions short — pull anything over 30 lines into its own function" beats "write clean code".
- Trim aggressively. Every line competes for attention; short, scannable files are followed more closely. Drop anything obvious from the code or true only today.
- Capture rules in the moment: start a line with `#`, type the rule, and Claude saves it into a `CLAUDE.md` (asking which file).

## Keep out of CLAUDE.md

- **Secrets** (API keys, passwords) — the file gets committed and version control remembers; use environment variables.
- **Large documents** (style guides, API specs) — they bloat every session and go stale; leave them where they live and point Claude to them.
- Needs better served by a **hook** (automatic action on an event), a **skill** (a saved on-demand routine), or an **MCP connection** (access to an outside system).

## Permission rules

Permission rules decide what Claude may do without asking, using three intents:

- **allow** — run automatically without asking (safe/routine, e.g. tests, `git status`).
- **ask** — prompt before running (things to eyeball, e.g. pushing to the repo).
- **deny** — never run (irreversible or sensitive, e.g. reading a secrets file).

If an action is both allowed and denied, **deny wins**. Put shared rules in `.claude/settings.json` (committed, whole team) and personal tweaks in `.claude/settings.local.json` (stays on your machine). Verify the effective rules with `/permissions` after editing.

## Session and context management

- `claude --continue` (`-c`) reopens the most recent session with its context; `/resume` lists past sessions to pick an older one.
- Start a fresh session for an unrelated task. When a session's memory gets cluttered, `/clear` empties the conversation but keeps you in place, which often sharpens answers.
- `/context` shows how full the working memory is. Don't confuse `/clear` (empty, stay), `/exit` (leave), and `--continue` (reopen).

## Plan before executing

- On anything non-trivial, get the approach before the work: "Before you change anything, walk me through how you'd approach this."
- Read the plan, then push back on one point (a different approach, or an edge case it missed) and let it adjust before any code exists.
- Skip the plan step for basic edits like renaming a variable or fixing a typo.
- The reason to do this is cost: the approach is cheap to steer while it's still just a plan.

## Work a plan in Plan Mode

Enter Plan Mode with `Shift+Tab` (press until you reach it). Claude researches and proposes; it doesn't edit.

Read the plan against three questions:

1. Is the approach sound?
2. Are its assumptions right — the tools, the libraries, where things live?
3. Is anything missing?

Then take one of three moves:

| Move | What you do |
| --- | --- |
| Approve | Accept the plan and let it execute |
| Edit | Stay in Plan Mode and say what you want changed, the way you'd brief a colleague. Claude rewrites to match. Loop as many times as needed |
| Rethink | Send it back to reconsider the approach entirely |

The hard part is knowing when to stop looping. Approve too early and you miss mistakes that are cheap now and expensive later. Loop too long and you've spent the time you were trying to save, which was the point of using Claude Code at all.

## Choosing a model

- Three tiers: **Opus** (most capable, slowest, priciest), **Sonnet** (the sensible default for most real work), **Haiku** (fastest, cheapest, good for simple well-defined work).
- Match the tier to how much judgment the task needs — the more judgment required, the higher the tier; the more mechanical the task, the lower. Defaulting to Opus for everything "to be safe" just costs more and takes longer without a benefit.
- Switch mid-session with `/model <model name>` instead of starting a new session — move up when a task gets harder, down when it gets simpler.

## Running tasks

- Tasks can run in the foreground or background.
- **Control+B** backgrounds a running task; each gets an ID and is monitored. `/bashes` lists running background commands.

## Headless one-shot mode

- `claude -p '...'` answers a single question and exits — good for quick asks and for scripting.
- Pipe a file in: `cat error.log | claude -p 'explain this error'`.
- Add `--output-format json` when another program will read the answer. Multi-round work belongs in a full session.

## Output styles

- Match Claude's voice to the goal: **Default** to ship, **Explanatory** to learn a codebase, **Learning** to build your own skills (it leaves `TODO(human)` pieces for you).
- Set with `/config` → Output style, or `"outputStyle"` in `.claude/settings.local.json`. It applies from the next session or after `/clear`. Create custom ones with `/output-style:new`.

## Verify, don't assume

After changing configuration, confirm it took effect with `/memory` and `/permissions` rather than assuming.
