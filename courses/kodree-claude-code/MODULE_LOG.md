# Kodree Claude Code — Module Log

Per-module notes. Reached **Part 25** of the course.

> **Note:** Parts 1–17 are captured together in one consolidated, topic-grouped backfill note (see **Units 1–17 (consolidated backfill)** below), assembled on 2026-07-23 from course content Daniel pasted. It is a topical summary of what the course covered, not separate per-part detail. Part 18 keeps its own detailed entry. From Part 19 onward, capture per unit.

## Backfill tracker (closed)

- [x] Parts 1–17 — covered together in the consolidated backfill note below (topical summary, not per-part detail).

Nothing is pending. Parts 18 onward were captured as they happened, so they are lesson entries rather than backfill. Use [templates/lesson-note.md](../../templates/lesson-note.md) if a deeper standalone note is useful.

## Lesson entries

Chronological, newest additions at the bottom.

## Units 1–17 (consolidated backfill)

_Assembled 2026-07-23 from pasted course content. Grouped by topic rather than by individual part. Facts here come only from that material._

### Sessions: starting, ending, and resuming
- A session always runs in a folder. On the computer a folder is just a container for files; a project is one folder holding all the files for a single piece of work (an app, a website, a tool). Whatever folder you start in becomes Claude's workspace for the whole session, so where you open it matters.
- Start a session by moving into the project folder, then launching Claude: `cd invoices` (go into the folder) then `claude` (start the session where the code lives).
- End a session with `/exit` (or the `Ctrl+D` shortcut). Claude Code shuts down cleanly and returns you to the normal terminal; the prompt changing from `>` back to `$` is the signal you've left Claude for your shell. `/exit` ends the conversation, not the work: approved changes are already saved in your files, and the session itself is saved so you can resume it.
- Continue the most recent session with `claude --continue` (short form `-c`); all the previous context comes back so you carry on mid-thought.
- Reopen an older session with `/resume` (inside Claude), which lists past sessions to choose from.
- Judgment call: resuming isn't always right. For an unrelated task, a clean session keeps things focused. A session that has wandered across many topics gets a cluttered memory that can muddy new answers; a fresh start often sharpens them. The skill is reading which situation you're in.

### Writing prompts
- A prompt is the instruction or question you send Claude, written in plain everyday language, like briefing a colleague. There's nothing to memorize.
- Be specific. A vague prompt leaves Claude guessing; a specific one names the place, the problem, and the result you want. Example: "improve the login page" (vague) vs. "On the login page, show a helpful error message when someone types the wrong password, instead of the page just reloading" (clear).

### The diff-and-approve loop
- When Claude is ready to edit, it shows the change first as a diff: your current version next to the proposed new one. Nothing is written yet; it's an offer, not a done deal.
- You accept, reject, or ask for a different approach. A proposal is a suggestion, and reviewing it is your job. Once you approve, Claude saves the change and often checks it did what you asked.
- A larger task (the same fix across many files) just runs this loop again, one reviewable step at a time. A big job is many small, visible steps in a row.

### Permission modes (matching the control to the job)
- Match the level of control to the work: tight control (ask-first or read-only) for important or unfamiliar work; looser control (auto-accept) for safe, repetitive work you're watching; the skip-everything mode stays parked for sandboxes and automated runs. Set it on purpose and change it as the work changes.

### Headless / one-shot mode
- For a quick, self-contained question you don't open a full session. Run `claude -p 'explain what this script does'`: the `-p` flag answers once, prints to the screen, and returns you to the terminal. This is also how Claude slots into scripts and automated jobs later.
- Pipe a file's contents into a one-shot with `|` (it feeds the left side's output into the right side): `cat error.log | claude -p 'explain what's causing this error'`.
- For another program to read the answer, request structured output with `--output-format json`: `claude -p "list the TODO comments in this file" --output-format json`. This is the doorway to automated workflows.
- Rule of thumb: one ask / one answer suits headless; anything you'll shape over several rounds belongs in a full session where Claude keeps the thread.

### Editor vs terminal
- The editor shares context the terminal can't. Claude's proposed change shows as a diff inside your code view, and the editor knows the file you have open and the lines you've highlighted, so you can point at "this function" without naming the file or pasting the lines.
- The terminal can't see your screen, so it leans on you to spell things out. Neither is better: the terminal shines for quick commands, one-shot jobs, and scripts; the editor shines when reading and shaping code in place. Many people keep both open and switch by task.

### Background commands
- Slow commands (a full build, a long test run, a dev server that stays up) don't need watching. Press `Ctrl+B` while a command runs to move it to the background; Claude hands the session back and the command keeps going. If you know a task will be slow, ask Claude to run it in the background from the start.
- A backgrounded command doesn't vanish: Claude gives each one an ID and monitors it, so you can ask how it's going or check its output any time without stopping it. `/bashes` lists everything running at once.

### Context and memory management
- Context is Claude's working memory, a limited amount held in mind at once. Once it's crammed (usually after a long, wandering session), answers can drift.
- `/context` shows how full that memory is. `/clear` empties the conversation but keeps you in the same session, giving a clean slate that often sharpens answers; you lose the old chat, so use it once that history stops pulling its weight.
- Three moves that get confused: `/clear` empties the conversation but keeps you in the session; `/exit` leaves Claude entirely; `claude --continue` reopens your last conversation (the opposite of a clean slate).

### Slash commands
- Inside a session, typed shortcuts starting with `/` handle quick admin, like keyboard shortcuts that save a trip to a menu. `/help` shows the full list.

### CLAUDE.md: the standing project note
- Claude has no memory across sessions: open it in a project and yesterday's conversation is gone. `CLAUDE.md` is a plain text file kept in the project that Claude reads automatically at the start of every session, before you type a word, so it already knows what you'd otherwise repeat.
- The bar for each line: is it stable, useful, and not already obvious from the code? Lines that fail that test dilute the ones that matter, and shorter, scannable files are followed more closely.
- Most of a good `CLAUDE.md` falls into three buckets. Commands: the build, test, run, and lint commands you use often. Conventions: how you like things done ("we use X, not Y"). Architecture: a short map of where the important pieces live so Claude's edits fit in.
- Make rules specific and actionable. "Write clean code" decides nothing; "Keep functions short — pull anything over 30 lines into its own function" names the move. Other examples: "Never edit migration files by hand, generate them with `npm run db:migrate`"; "Add a one-line comment above every exported function"; "Put shared logic in `utils/` instead of copying it between files".
- Drafting and tending: `/init` reads your codebase and drafts a `CLAUDE.md` (commands, conventions, structure) as a strong first draft to trim; without it, just ask "Create a CLAUDE.md for this project." Capture rules in the moment by starting a line with `#` and typing the rule — Claude saves it into your `CLAUDE.md` (asking which file). Over time, every correction becomes a rule.

### CLAUDE.md: where rules live (scope)
- Put a rule in the smallest place where it's true. Three locations: the project file (`CLAUDE.md` in the project folder) holds shared rules committed to the repo so every teammate's Claude reads them; your personal file (`~/.claude/CLAUDE.md` in your home folder) holds your own preferences and travels with you into every project, seen by nobody else; a nested file (`CLAUDE.md` in a subfolder) holds rules for one part of the project.
- Team agreements go in the project file; personal taste in your personal file. A nested `CLAUDE.md` isn't read at session start — Claude picks it up only when it works with a file in that folder — and its rules layer on top of what's loaded rather than replacing it.
- When unsure which rules are in play, run `/memory`: it lists every `CLAUDE.md` currently loaded and lets you open them to edit. It's the first check when Claude follows a rule you forgot or ignores one you expected, since often the file you had in mind simply wasn't loaded.

### CLAUDE.md: what does NOT belong in it
- No secrets. An API key or password in the project file gets committed and shared, and version control remembers, so it spreads further and lasts longer than you'd want. Use an environment variable instead.
- No big documents. Pasting a long style guide, API spec, or design doc bloats every session and goes stale when the real doc changes. Leave the document where it lives and point Claude to it.
- `CLAUDE.md` is one tool, not the whole toolbox. Some needs have a purpose-built home (each covered later in the course): a hook is an automatic action that fires on an event, often to block something (like stopping a commit that contains a secret); a skill is a saved set of steps Claude runs on demand the same way every time (like a "scaffold a new API endpoint our way" routine); an MCP connection plugs Claude into an outside system to read or act there (like fetching a customer's record from your database).

### Permissions (allow / ask / deny)
- Permissions govern what Claude may do without checking with you (distinct from `CLAUDE.md`, which is about how you like things done). Like a key card: some doors open any time, some need sign-off, some stay locked.
- Three answers to any command, edit, or read: Allow (go ahead, don't ask — for safe routine things like running tests or `git status`); Ask (check first, every time — for things you want to eyeball, like pushing to the repo); Deny (never — for the dangerous or sensitive, like reading a secrets file). If something is both allowed and denied, deny wins.
- Rules live in a settings file, and where you put them decides who gets them: the shared `.claude/settings.json` is committed to the repo so the whole team shares the guardrails; the local `.claude/settings.local.json` stays on your machine for personal tweaks.
- The deny list is the safety net / hard block: deny anything irreversible or sensitive, and a denied action is stopped outright. `/permissions` opens the full list and lets you change it; the common move is adding an allow rule for a safe command you keep approving (like your test command) so the prompts fall away.

### Output styles
- Output styles change how Claude talks to you while it works (same Claude, same skills). Default is quick and to the point (best when you know what you want). Explanatory does the work and explains its choices with short "Insights" (best for understanding an unfamiliar codebase). Learning is hands-on: it explains as it goes and leaves small pieces for you to write yourself, marked `TODO(human)` (best when the goal is building your own skills).
- The styles aren't just flavors: Explanatory and Learning are longer by design and Learning pauses to hand you code, so pick the style for your goal, not your mood.
- Set it with `/config` → Output style → choose one, or add `"outputStyle": "Explanatory"` to `.claude/settings.local.json`. The voice loads when a session starts, so a change applies in your next session or right after `/clear`, not mid-turn, and then stays with the project until you change it. Create your own with `/output-style:new` when you keep wishing for the same voice.

## Part 18

### What I learned
- The difference between an original repository, fork, clone, and branch.
- A project `CLAUDE.md` gives Claude repository-specific guidance.
- `/init` drafts `CLAUDE.md` by inspecting an existing codebase.

### What I did
- Installed the project dependencies.
- Ran tests and lint.
- Created Claude permission rules.
- Committed my changes and opened a pull request.

### What confused me
- Why `git diff` did not initially show my new files.

## Part 19: Plan then execute

### What I learned
- The course pushes a plan-then-execute mindset: have Claude research and lay out its approach before it makes a batch of changes.
- Not every task needs a plan step. For something basic like renaming a variable or fixing a typo, planning is overkill.
- Steering the approach while it's still cheap to steer is the whole point. The back-and-forth happens before a single change exists.

### Commands or techniques
- Ask Claude: "Before you change anything, walk me through how you'd approach this."
- Read the plan, then push back on one point (a different approach, or an edge case it missed) and watch it adjust, all before any code exists.

### What confused me
- Nothing major. This was a fairly basic module.

## Part 20: Entering and reading a plan in plan mode

### What I learned
- In Plan Mode, Claude researches and proposes instead of editing. The course called this a safety net in action.
- A plan can look convincing and still be wrong, so reading it critically is my job.

### Commands or techniques
- Start a new session in Plan Mode by pressing `Shift+Tab` until you reach it.
- Review a plan against three questions: (1) Is the approach sound? (2) Are its assumptions right — the tools, the libraries, where things live? (3) Is anything missing?

## Part 21: Approving, editing and looping on a plan

### What I learned
- A plan gives you three moves: approve it, edit it, or send it back to rethink the approach.
- To change a plan, stay in plan mode and tell Claude what you want the same way you'd brief a colleague. Claude rewrites the plan to match, and you can loop as many times as you need.
- The hard part of looping isn't doing it, it's knowing when to stop. Approve too early and you may miss mistakes; take too long and you lose the time savings that were the point of using Claude Code.

### What I did
- Worked an exercise that instructed me to clone a repo used in the course. I found I already had it cloned and only needed to check it out.

### What confused me
- Git mechanics. The plan-mode material made sense; the repo handling did not fully click.
- How to tell whether I already have a repo cloned.
- What `checkout` actually means. My assumption was that it makes an updated local copy.

### Follow-up questions
- How do I check whether a repo is already cloned on my machine?
- What does `git checkout` do, precisely?

## Part 22: Model tradeoffs: Opus vs. Sonnet vs. Haiku

### What I learned
- The lesson covered the different Anthropic models (as of 7/23/26). Opus is the most capable, but is the slowest and priciest. Haiku is the fastest and cheapest, and shines on simpler, well-defined work. Sonnet sits in between and handles most real work well — it's the sensible default.
- The common trap is reaching for Opus on everything to be safe, which just means paying more (especially at scale) and waiting longer for work that didn't need it.
- The more judgment a task demands, the further up the model tier you should reach; the more mechanical the task, the further down.

### What I did
- Ran an exercise comparing Haiku vs. Sonnet on summarizing a line of code, and found the responses roughly similar.

### Follow-up questions
- How do you monitor model performance over time and make the determination to switch models, to ensure the right model is being used for the right task?

## Part 22: Switching models mid-session

### What I learned
- You can switch models mid-session by typing `/model` followed by the name of the model.
- The recommendation is to switch up or down within a session depending on the difficulty of the task at hand.

### Commands or techniques
- `/model <model name>` — switch models mid-session.

## Part 23: The opusplan hybrid

### What I learned
- Opusplan is a built-in hybrid that uses Opus to plan (the part that needs the most reasoning), then hands off to Sonnet to execute the plan (the part that needs steady work).
- This setup uses the strong model where it matters and the faster, cheaper model for the bulk of the work.

### Commands or techniques
- Start a session with `claude --model opusplan`, or pick opusplan from the `/model` list.

## Part 24: Managing Context and Cost Across the Loop

### What I learned
- Context is a resource: everything Claude knows in a session lives in a fixed-sized window, and every new message carries a lot with it, so cluttered sessions cost more per turn and, past a point, get less sharp.
- Managing context is described as the last habit of working with intent.
- Reading big files and long outputs fill the window the fastest, which is why feeding Claude only what the task needs keeps a session lean.
- Claude does auto-compact when the window nearly fills, but waiting for that is the worst case, since it strikes mid-moment when you don't choose it. Better to manage as you go.

### Commands or techniques
- `/context` — shows how full the window is and what is taking space.
- `/clear` — wipes the conversation to zero; use when switching to unrelated work.
- `/compact` — summarizes the session, keeping key state (decisions, file paths, what's left) while dropping the noise.

### Follow-up questions
- Better understand how Claude chooses what to keep when `/compact` runs, and whether I'd have a say in that within a session.

## Part 25: How Claude works with your repo: status, diffs, history

### What I learned
- The lesson covered reading changes, writing commit messages, drafting pull request descriptions, reviewing code, and untangling conflicts.
- Claude reads your repo on demand: asking "what have I changed?" runs the equivalent of `git status` and `git diff` and explains the changes in plain English.
- Claude can do git archaeology — searching past commits and their diffs to answer how the code got the way it is.

### What I did
- Forked the course-provided repo (mate-academy/git-playground-task1) and cloned it.
- Made a few edits, then created a `notes.md` file predicting what I changed from memory.
- Had Claude summarize what I changed and compared the results against my prediction.
- Had Claude commit the changes onto a new branch called `read-repo` and create a PR against the main repo.

### What confused me
- The git mechanics overall: cloning, forking, committing changes, and creating PRs. Still fuzzy on what I'm actually doing during these steps.
- Using VSCode: having to look across Terminal screens caused mechanical issues. Would like a shortcut to make this easier.

### Follow-up questions
- Is there a shortcut to make it easier to work across Terminal screens in VSCode?
