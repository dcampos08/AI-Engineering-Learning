# Playbook: Git and GitHub

Reusable Git and GitHub workflow. Mostly distilled from the Kodree Claude Code course; the clone-vs-checkout section came from working through a course exercise where the repo turned out to be cloned already.

## Four things that are not the same

| Thing | What it is |
| --- | --- |
| Original repository | The canonical upstream repo owned by the maintainer |
| Fork | Your personal copy of that repo on your account |
| Local clone | A copy on your machine (`git clone`), created once |
| Branch | A line of commits within a repo, for isolated work |

## Do I already have this repo? (clone vs. checkout)

Cloning and checking out are different operations, and the exercise instructions that say "clone the repo" assume you don't have it yet.

- `git clone` is the one-time download that creates the folder. You do it once per repo.
- `git checkout` switches which version of the files is sitting in that folder. Same folder, contents rewritten in place. It downloads nothing.
- `git pull` is what actually gets you an updated copy from the remote.

Before cloning anything, check whether you already have it:

```bash
ls ~/Claude                   # or wherever you keep projects
cd <folder>
git remote -v                 # prints the URL this folder was cloned from
```

If `git remote -v` prints the repo's URL, that folder is already a clone of it. Then orient and switch:

```bash
git status                    # current branch, and what's changed
git branch -a                 # local and remote branches
git checkout <branch>         # switch to an existing branch
git checkout -b <branch>      # create a new branch and switch to it
git pull                      # now bring in the remote's newer commits
```

## Contribute-to-upstream workflow

1. **Fork** the original repository to your account.
2. **Clone** your fork locally.
3. **Baseline:** run tests and lint before changing anything.
4. **Branch:** create and switch to a feature branch for your work.
5. Make changes.
6. **Stage and review:** `git add`, then `git diff --cached` to see exactly what's staged.
7. **Commit:** `git commit`.
8. **Push:** `git push` to your fork.
9. **Open a pull request** from your fork's branch to the original repository.

## The core local loop

```bash
git status            # what changed
git add <paths>       # stage
git diff --cached     # review what's staged
git commit            # record
git push              # upload to remote
```

## Reading history

Ask Claude to do git archaeology when you need to understand how the code got the way it is, not just what changed now — it searches past commits and their diffs and explains the answer.

## Habits

- Check `git status` often to stay oriented.
- Remember that plain `git diff` shows only unstaged changes to tracked files — new untracked files won't show up there. Use `git status` to see them, or `git add` then `git diff --cached`.
- Review `git diff --cached` before every commit — commit what you meant to, nothing extra.
- Keep work on feature branches, not the main line.
- Establish a green baseline before you start so you can tell what your changes broke or fixed.
