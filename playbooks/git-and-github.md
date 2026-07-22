# Playbook: Git and GitHub

Reusable Git and GitHub workflow, distilled from the Kodree Claude Code course.

## Four things that are not the same

| Thing | What it is |
| --- | --- |
| Original repository | The canonical upstream repo owned by the maintainer |
| Fork | Your personal copy of that repo on your account |
| Local clone | A copy on your machine (`git clone`) |
| Branch | A line of commits within a repo, for isolated work |

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

## Habits

- Check `git status` often to stay oriented.
- Remember that plain `git diff` shows only unstaged changes to tracked files — new untracked files won't show up there. Use `git status` to see them, or `git add` then `git diff --cached`.
- Review `git diff --cached` before every commit — commit what you meant to, nothing extra.
- Keep work on feature branches, not the main line.
- Establish a green baseline before you start so you can tell what your changes broke or fixed.
