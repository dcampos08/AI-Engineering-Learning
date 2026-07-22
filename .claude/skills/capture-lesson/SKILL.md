---
name: capture-lesson
description: Append a structured lesson entry from rough course notes to the correct course MODULE_LOG.md. Manually invoked only.
disable-model-invocation: true
argument-hint: "[course, part/module, and rough notes]"
---

# Capture a course lesson

Take the rough notes the user supplied and append a single structured lesson entry to the correct course `MODULE_LOG.md`.

The user's input is:

$ARGUMENTS

## Rules

- Use `$ARGUMENTS` as the **only** source of facts. Do not add details, dates, links, results, or claims of understanding that are not present in that text.
- If a fact is not in `$ARGUMENTS`, leave it out. Never invent.
- Do not update, create, or touch any file other than the target `MODULE_LOG.md`.
- Do not commit or push.

## Steps

1. **Identify the course** from `$ARGUMENTS`.
   - For the Kodree course, the target file is `courses/kodree-claude-code/MODULE_LOG.md`.
   - For any other course, map it to `courses/<course-folder>/MODULE_LOG.md`. If you cannot confidently determine the folder, ask the user which file to use rather than guessing.

2. **Identify the module or part number** from `$ARGUMENTS` and use it in the entry heading.

3. **Build the entry.** Use the following sections, but only include a section when `$ARGUMENTS` actually provides information for it. Omit any section with no content.
   - `### What I learned`
   - `### What I did`
   - `### What confused me`
   - `### Commands or techniques`
   - `### Where I might use this`
   - `### Follow-up questions`

4. **Append** the entry to the end of the target `MODULE_LOG.md`. If the file does not exist yet, create it with a top-level `# <Course name> — Module Log` heading (use the course name, not the generic "Module Log"), then add the entry. Do not overwrite existing content.

5. **Reconcile the backfill tracker.** If the target `MODULE_LOG.md` has a backfill tracker and it contains an item for the part/module you just captured, mark that item as documented (change `[ ]` to `[x]` and note it points to the entry below). Leave every other pending backfill item exactly as it is. Do not invent notes for parts that remain pending.

## Entry format

Use a consistent heading in one of these two forms, matching the course's own terminology ("Part" or "Module"):

```
## Part <number>: <short descriptive title>
```
```
## Module <number>: <short descriptive title>
```

If `$ARGUMENTS` gives a title, use it. If no title is provided, write a concise title built **only** from the supplied notes — do not add topics the notes don't mention.

```
## Part <number>: <short descriptive title>

### What I learned
- ...

### Commands or techniques
- ...
```

(Include only the sections that have content.)

## Finish

After writing, tell the user exactly which file was changed (the full relative path). Do not report on or modify any other learning file.
