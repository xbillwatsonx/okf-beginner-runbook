# Open Knowledge Format Beginner Runbook

Date: 2026-06-27

Use this runbook when you want an AI agent, desktop AI app, command-line assistant, code assistant, or local AI harness to help you create a new Open Knowledge Format knowledge base or gradually turn an existing notes folder, reference vault, project archive, wiki, or second brain into an OKF-style knowledge base.

This guide is platform-neutral. It can be used with OpenClaw, Hermes, Hermes Desktop, Odysseus, VSCode-based agents, OpenCode, Local Codex, Gemini, Antigravity, or any other AI system that can read and write files with your permission.

## Beginner Quick-Start

1. Pick one small area of knowledge to organize first.
2. Tell the agent whether you are starting fresh or improving an existing folder.
3. Choose or approve one folder for the agent to inspect.
4. Ask your agent to inspect only that approved folder.
5. Have the agent summarize what it found before changing anything.
6. For an existing knowledge base, ask for a conversion plan before editing files.
7. Start with a small OKF folder structure or a light OKF wrapper around existing folders.
8. Create one Markdown file per concept when new files are needed.
9. Put YAML frontmatter at the top of every non-reserved Markdown file.
10. Make sure every non-reserved Markdown file has a non-empty `type` field.
11. Use `index.md` files to help people and agents discover what is in each folder.
12. Use `log.md` files to record meaningful changes over time.
13. Validate the folder before calling it finished.

## 1. What OKF Is

Open Knowledge Format, or OKF, is a simple way to organize knowledge as a folder of plain text files.

The files are ordinary Markdown files. Markdown is a plain text writing format that can use headings, bullet lists, links, tables, and code blocks. Most AI agents and many note apps can read it.

Each important idea, process, asset, rule, or reference gets its own `.md` file. At the top of each non-reserved Markdown file is a small metadata block called YAML frontmatter. YAML frontmatter is a few structured lines that help an agent quickly understand what the file is about.

The body of the file is normal Markdown. That means the knowledge stays readable by people while also being easy for AI agents to crawl, search, link, and update.

In plain English: OKF is a folder of linked notes with a small amount of structure at the top of each note.

## 1A. Optional Obsidian Viewing

You can open an OKF folder in Obsidian as a vault if you want a visual way to browse it.

Obsidian is a free Markdown viewer and note app. Point Obsidian at the OKF folder, and it can render the notes, links, and folder structure visually.

Obsidian is optional. The knowledge base still works as plain Markdown files without it.

## 2. What OKF Is Good For

OKF is useful when you want knowledge to be readable by humans and usable by AI agents.

Good uses include:

- personal second brain
- business knowledge base
- AI memory folder
- company playbooks
- product notes
- project documentation
- API documentation
- data definitions
- marketing asset library
- SOPs
- research vault
- agent operating manual
- customer support notes
- troubleshooting guides
- decision records
- prompt libraries
- internal training material

OKF is especially helpful when information is spread across notes, documents, folders, code comments, spreadsheets, meeting notes, or old project files and you want an agent to help make it navigable.

It can be used for a brand-new knowledge base, but it is just as useful for improving an existing one. For example, a folder like `REFERENCE-VAULT/` can be inspected, mapped, wrapped with `index.md` files, and gradually converted into OKF-style concept files without forcing a full rebuild on day one.

## 3. What OKF Is Not

OKF is not:

- a database
- a vector database
- a cloud service
- a proprietary app
- a replacement for domain-specific schemas
- a magic memory system
- a reason to dump every file into an agent context window
- a requirement to use Google Cloud
- a requirement to use Git
- a requirement to use any one AI assistant

OKF is a file format pattern, not a product. It gives your knowledge a shared shape so different tools and agents can understand it.

## 4. Before You Start

You need:

- an AI agent or app that can read and write local files
- a folder where the OKF knowledge base will live
- permission to inspect or modify that folder
- a small starting domain instead of everything at once

A domain is simply the area you want to organize. Examples:

- "our order process"
- "my AI prompts"
- "microgreens customer notes"
- "software project documentation"
- "marketing assets"
- "research on one topic"

Start small. A useful first OKF folder can have three to ten concept files.

## 5. First-Run Agent Behavior

The agent should not begin by creating files.

It should first ask whether you already have any of these:

- second brain
- reference vault
- notes folder
- Obsidian vault
- Google Drive folder available locally
- Git repository
- project folder
- existing knowledge base
- exported notes or documents

Then the agent should ask what you want to do:

- create a new OKF knowledge base
- inspect an existing knowledge base first
- convert part of an existing folder into OKF
- add OKF structure to an existing project
- pause and only produce a proposed plan

The agent should wait for your answer before scanning or changing files.

## 5A. Existing Knowledge Base Conversion Path

Many users will not be starting from an empty folder. They may already have a reference vault, project archive, Obsidian vault, shared Drive export, internal wiki export, or a folder full of notes.

In that case, the agent should not assume the existing structure is wrong. The first goal is to understand it.

For an existing knowledge base, the agent should:

1. Ask which top-level folder to inspect.
2. Inspect only approved folders.
3. Summarize the current structure in plain English.
4. Identify useful existing patterns, such as `PROJECTS/`, `REFERENCE/`, `REPORTS/`, `SOPs/`, or `memory/`.
5. Identify what is already close to OKF, such as Markdown notes, index files, logs, or linked documents.
6. Identify what is missing, such as frontmatter, folder indexes, portable links, or smaller concept files.
7. Recommend the smallest safe conversion path.
8. Ask for approval before editing.

The safest conversion path is usually one of these:

- **Light wrapper**: Add `index.md` and `log.md` files around existing folders without moving anything.
- **Partial conversion**: Convert one approved folder or topic into OKF-style Markdown files.
- **New OKF layer**: Create a new OKF folder that links to important existing files instead of moving them.
- **Full migration**: Reorganize the existing knowledge base only after a clear plan, backup, and approval.
- **Plan only**: Produce a migration plan and make no file changes.

For a large existing folder, start with a map instead of a migration.

The agent can create a simple inventory like this:

```markdown
# Existing Knowledge Map

## Top-Level Areas

- `REFERENCE-VAULT/` - Long-term reference material.
- `PROJECTS/` - Active and historical project work.
- `REPORTS/` - Finished reports and audits.
- `memory/` - Chronological notes and session history.

## OKF Opportunities

- Add folder-level `index.md` files for discovery.
- Add `log.md` files to folders that change often.
- Convert high-value notes into one-concept Markdown files with frontmatter.
- Add portable links between related files.

## Do Not Touch Yet

- Private folders not approved by the user.
- Generated archives.
- Credentials, secrets, or account exports.
```

Then the agent can propose a small first improvement, such as:

- add a root `index.md`
- add a folder-level `index.md` to one approved area
- create `_templates/concept-template.md.tmpl`
- convert three existing notes into OKF concept files
- create a `log.md` entry explaining the change

This lets the user get OKF benefits without breaking a working system.

## 6. Safe Scanning Rules

The agent must not scan your whole computer by default.

The agent must ask where to look first.

Approved places may include:

- the current working folder
- a notes folder you approve
- a project folder you approve
- a Git repository you approve
- an export folder you approve
- a cloud-synced folder that is available locally and that you approve

The agent must not inspect sensitive folders unless you clearly approve.

Sensitive folders may include:

- tax records
- medical files
- password exports
- private family documents
- legal documents
- private customer data
- hidden system folders
- folders with secrets or credentials

Before modifying anything, the agent must summarize what it found.

Before editing existing files, the agent must either:

- create a backup, or
- confirm that the folder is already version-controlled and recoverable

Version-controlled means a tool such as Git is tracking file history so changes can be reviewed and undone.

The agent must not delete, overwrite, move, or rename existing files without explicit user approval.

## 7. Friendly Qualifying Questions

The agent should ask questions in normal language.

Use questions like these:

- What do you want this knowledge base to help you remember, organize, or do?
- Do you already have notes, documents, folders, an Obsidian vault, a Drive folder, a Git repo, or a second brain?
- Where is it located?
- Do you want to create something new or improve what you already have?
- What should be included first?
- Is anything private, sensitive, off limits, or not allowed to be touched?
- Will this be used by one person, a team, or the public?
- Should the agent only read the knowledge base, or should it also be allowed to create and update files?
- Where should the OKF folder live?
- Do you want simple folders, a connected wiki, or a mix of both?
- Do you want version history through Git, or should this stay as regular folders and files?
- Which AI agent, app, CLI, or harness are you using right now?

Examples of things to include first:

- business processes
- project notes
- product information
- customer notes
- code documentation
- marketing assets
- personal research
- recipes
- SOPs
- AI prompts
- tool instructions
- troubleshooting notes

## 8. Minimum Viable OKF Build

The first version should be small and working.

Create this starter structure unless the user requests something else:

```text
okf-knowledge-base/
  index.md
  log.md
  getting-started.md
  domains/
    index.md
  playbooks/
    index.md
  references/
    index.md
  projects/
    index.md
  prompts/
    index.md
  _templates/
    concept-template.md.tmpl
    index-template.md.tmpl
    log-entry-template.md.tmpl
```

Then create three to ten starter concept files based on the user's chosen domain.

`getting-started.md` is a non-reserved OKF concept file, so it needs frontmatter:

```markdown
---
type: Guide
title: Getting Started
description: Basic instructions for using and maintaining this OKF knowledge base.
tags: [guide, maintenance]
timestamp: 2026-06-27T00:00:00Z
---

# Getting Started

Use `index.md` files to navigate the knowledge base. Add one concept per Markdown file. Update `log.md` after meaningful changes.
```

The files in `_templates/` use `.md.tmpl` so they are inert templates, not OKF concept files. If a template uses the plain `.md` extension instead, it must include frontmatter and a non-empty `type`, such as `type: Template`.

Good first concept files might include:

- one overview file
- one glossary term
- one playbook
- one reference note
- one troubleshooting guide
- one project note
- one prompt or agent instruction

Keep the first build boring and usable. It is better to have eight clear files than eighty confusing files.

## 9. File Naming Rules

Use:

- lowercase file names
- hyphens instead of spaces
- clear names
- one concept per file
- folders only when they make discovery easier

Avoid:

- giant files
- vague names like `misc.md`
- file names that only make sense to one person
- machine-specific names
- deeply nested folder structures

Good names:

- `customer-intake.md`
- `weekly-content-process.md`
- `stripe-checkout-troubleshooting.md`
- `seed-inventory-reference.md`
- `qwen-tts-preset.md`

Weak names:

- `notes.md`
- `misc.md`
- `stuff.md`
- `new-final-final.md`
- `things-to-remember.md`

## 10. Frontmatter Rules

Every non-reserved `.md` file must begin with YAML frontmatter.

Non-reserved means any Markdown file that is not named `index.md` or `log.md`.

That includes files such as `README.md`, guide files, template files, reference files, project files, prompt files, and playbooks if they use the `.md` extension.

Use this basic format:

```yaml
---
type: Playbook
title: Example Playbook
description: A plain-language summary of what this file explains.
tags: [example, starter]
timestamp: 2026-06-27T00:00:00Z
---
```

The `type` field is required.

The `type` field must:

- sit at the root of the YAML frontmatter
- be present in every non-reserved `.md` file
- contain a short, useful value
- not be empty

Optional fields may include:

- `title`
- `description`
- `resource`
- `tags`
- `timestamp`

The body after the frontmatter can use normal Markdown headings, paragraphs, lists, tables, links, and code blocks.

Do not indent the opening or closing `---` lines.

Do not add characters after the `---` lines.

Do not use other frontmatter dividers such as long dashed lines.

## 11. Recommended Concept Types

OKF does not force a fixed taxonomy. A taxonomy is a set of official categories. You do not need one at the beginning.

Starter type values can include:

- Playbook
- SOP
- Project
- Reference
- Prompt
- Decision
- Metric
- API
- Schema
- Dataset
- Tool
- ContactNote
- ResearchNote
- TroubleshootingGuide
- GlossaryTerm

Choose names that are easy to understand. You can rename or refine them later.

Agents and tools should tolerate unknown types. A new type should not break the knowledge base.

## 12. Internal Linking Rules

Use standard Markdown links.

Good examples:

```markdown
[Order process](../playbooks/order-process.md)
[Customer intake](./customer-intake.md)
[Products](/references/products.md)
```

Avoid machine-specific paths:

```text
C:\Users\Name\Documents\folder\file.md
/home/name/private-folder/file.md
```

Links should stay portable if the OKF folder is moved to another computer, app, repository, or AI environment.

Bundle-relative links start with `/` and point from the root of the OKF folder. Relative links such as `./file.md` or `../folder/file.md` are also acceptable.

Use the surrounding sentence to explain what the link means. The link itself does not need a special machine-readable relationship type.

For quality control, report broken internal links.

Do not treat broken links as fatal OKF conformance errors. OKF consumers must tolerate broken links because some links may point to planned or not-yet-written knowledge.

Mark intentional missing targets as planned.

## 13. Reserved Files

Two file names have special meaning in OKF.

### `index.md`

Use `index.md` for directory discovery.

It should describe what is inside a folder and link to the most important child files.

Example:

```markdown
# Playbooks

- [Customer intake](customer-intake.md) - How to receive and organize new customer requests.
- [Weekly content process](weekly-content-process.md) - How to create and review weekly content.
```

`index.md` should help a person or agent decide what to open next.

Do not use `index.md` as a concept file.

Do not add YAML frontmatter to normal `index.md` files. They are reserved discovery files, not concept documents. Exception: the bundle-root `index.md` may include frontmatter only to declare the target OKF version, such as `okf_version: "0.1"`, if the user wants explicit version metadata.

Optional bundle-root `index.md` example:

```markdown
---
okf_version: "0.1"
---

# OKF Knowledge Base

This index helps people and agents discover the main areas of the bundle.
```

### `log.md`

Use `log.md` for chronological change history.

It should record meaningful updates, migrations, imports, structure changes, and validation notes.

Put the newest date section at the top.

Example:

```markdown
# Directory Update Log

## 2026-06-27

- **Initialization**: Created the first OKF folder structure.
- **Creation**: Added starter playbook and reference files.
- **Validation**: Checked frontmatter and internal links.
```

Do not use `log.md` as a concept file.

Do not add YAML frontmatter to `log.md`. It is a reserved history file, not a concept document.

## 14. Agent Ingestion Strategy

The agent must not load the whole OKF folder into context at once.

The agent should:

1. Read the root `index.md`.
2. Follow only relevant links.
3. Open folder-level `index.md` files as needed.
4. Read only the concept files needed for the current task.
5. Use `log.md` to understand recent changes.
6. Ask before making broad edits.

This keeps the agent focused and prevents wasting context on unrelated files.

## 15. Build Procedure

Use this workflow when asking an agent to build a new OKF knowledge base, improve an existing OKF knowledge base, or gradually convert an existing non-OKF knowledge base into OKF-style structure.

### Step 1: Ask the first-run questions

The agent asks what the user already has, where it is, what should be included first, and what is off limits.

### Step 2: Inspect only approved folders

The agent checks only the folders the user approved.

### Step 3: Summarize what exists

Before changing anything, the agent reports:

- what folders it inspected
- what file types it found
- whether an OKF-like structure already exists
- whether the current folder already has a useful structure worth preserving
- which parts could be wrapped with OKF files without moving anything
- whether there are sensitive-looking areas to avoid
- whether there is Git history or another backup

### Step 4: Recommend one path

The agent recommends one of these:

- new OKF folder
- light OKF wrapper around existing files
- partial conversion
- full migration
- planning only

For an existing folder, the agent should prefer a light wrapper or partial conversion first unless the user clearly asks for a full migration.

### Step 5: Propose a folder structure

The agent shows the planned folder tree before creating it.

### Step 6: Show three sample files

The agent shows examples of:

- one concept file
- one `index.md`
- one `log.md` entry

### Step 7: Ask for approval

The agent asks before creating or modifying files.

### Step 8: Create the folder structure

The agent creates only approved folders and files.

### Step 9: Create starter files

The agent creates three to ten starter concept files based on the chosen domain. If converting an existing folder, the agent may instead create three to ten OKF-style files that summarize, link to, or carefully refactor approved existing notes.

### Step 10: Validate the result

The agent checks frontmatter, reserved files, links, file size, naming, and privacy boundaries.

### Step 11: Generate a user guide

The agent adds a short `getting-started.md` guide explaining how to add files, link concepts, update indexes, and run validation. Because `getting-started.md` is a non-reserved Markdown file, it must include YAML frontmatter and a non-empty `type`.

## 16. Validation Rules

The agent must validate before declaring the OKF bundle complete.

Validation must check:

- every non-reserved `.md` file has YAML frontmatter
- YAML frontmatter starts and ends with triple dashes on their own lines
- every non-reserved `.md` file has a non-empty root-level `type`
- reserved `index.md` files are used for discovery
- reserved `log.md` files are used for change history
- links are portable
- broken internal links are reported for quality control
- intentional missing targets are clearly marked as planned
- no giant catch-all file was created
- no machine-specific file paths were used
- no sensitive folders were included by accident
- files are small enough for agent retrieval

If an official validator or project validator is available in the user's environment, use it.

This starter repo also includes a tiny dependency-free validator script. From the repo root, run:

```bash
python3 validate-okf.py starter-kit/okf-knowledge-base
```

If not, use this simple validation checklist:

```text
[ ] Did I inspect only approved folders?
[ ] Did I avoid private or sensitive folders?
[ ] Does every non-reserved .md file start with YAML frontmatter?
[ ] Does every non-reserved .md file have a non-empty type field?
[ ] Are index.md files used only for discovery?
[ ] Are log.md files used only for change history?
[ ] Do internal links use portable Markdown links?
[ ] Are broken internal links reported?
[ ] Are intentional missing targets clearly marked as planned?
[ ] Are files small and focused?
[ ] Are file names lowercase and clear?
[ ] Did I update the folder index after adding important files?
[ ] Did I add a log entry for meaningful changes?
```

## 17. Maintenance Routine

Use a small routine so the knowledge base stays useful.

### Daily or per project

- Add new notes as separate concept files.
- Link related files.
- Update folder `index.md` when new important files are added.
- Add a short `log.md` entry for meaningful changes.

### Weekly

- Check broken links.
- Merge duplicates.
- Add missing descriptions.
- Review recent `log.md` entries.
- Look for important concepts that should have their own file.

### Monthly

- Archive stale files.
- Refine concept types.
- Clean up folder structure.
- Validate the whole bundle.
- Review whether the folder is still easy for a person to understand.

## 18. Beginner Copy-Paste Agent Prompt

Copy this into your agent:

```text
Help me build or inspect an Open Knowledge Format knowledge base. First, ask me whether I already have a notes folder, second brain, vault, Drive folder, Git repo, or knowledge base. Ask where it is and whether I want to create a new OKF folder, modify an existing one, or only inspect and plan. Do not scan my whole computer. Only inspect folders I approve. Before changing anything, summarize what you found and show me your proposed structure. Do not delete, overwrite, move, or rename files unless I approve. Use OKF-style Markdown files with YAML frontmatter. Make one file per concept when creating new concept files. Use type as the required frontmatter field in every non-reserved .md file. Use index.md for discovery and log.md for change history. Validate the folder before calling it complete.
```

## 19. Troubleshooting

### Broken links

Ask the agent to list broken links and their source files. Fix the target path or create the missing concept file if the missing page should exist.

### Missing frontmatter

Add a YAML frontmatter block at the top of the concept file. Make sure it begins and ends with `---` on their own lines.

### Malformed YAML

YAML is picky about spacing. Keep it simple. If a field breaks, ask the agent to rewrite the frontmatter using the starter format in this runbook.

### Files that are too large

Split the file into smaller concept files. Add links between the files and update the folder `index.md`.

### Too many folders

Flatten the structure. Use fewer folders and better `index.md` files.

### Too few links

Ask the agent to find related concepts and add useful Markdown links. Do not add links just for decoration.

### Confusing file names

Rename only with approval. Use lowercase, hyphens, and clear terms.

### Duplicate concepts

Merge duplicates only after reviewing both files. Preserve any unique information and add a `log.md` entry.

### Agent loading too much context

Tell the agent to start from the root `index.md`, follow only relevant links, and open only the files needed for the task.

### Accidental private information

Stop. Ask the agent to identify the affected files. Remove or redact the private information with approval. Add a log entry only if it is safe to mention the cleanup without exposing the private details.

### Old notes that do not fit the structure

Do not force everything into OKF at once. Keep old notes in a separate folder, then convert the most useful ones one at a time.

## 20. Final Deliverables Checklist

Use this list to confirm the OKF starter bundle is complete.

### Setup checklist

```text
[ ] User chose a small starting domain.
[ ] User approved the folder to inspect.
[ ] Agent summarized existing files before making changes.
[ ] Agent confirmed backup or version history before modifying existing files.
[ ] Agent proposed a structure.
[ ] User approved file creation or edits.
```

### Safe scanning checklist

```text
[ ] Agent did not scan the whole computer.
[ ] Agent inspected only approved folders.
[ ] Agent avoided sensitive folders.
[ ] Agent did not move, rename, delete, or overwrite files without approval.
```

### Default folder template

```text
okf-knowledge-base/
  index.md
  log.md
  getting-started.md
  domains/
    index.md
  playbooks/
    index.md
  references/
    index.md
  projects/
    index.md
  prompts/
    index.md
  _templates/
    concept-template.md.tmpl
    index-template.md.tmpl
    log-entry-template.md.tmpl
```

### Sample OKF concept file

```markdown
---
type: Playbook
title: Customer Intake
description: Steps for receiving and organizing a new customer request.
tags: [customers, intake, operations]
timestamp: 2026-06-27T00:00:00Z
---

# Purpose

Use this playbook when a new customer sends a request.

# Steps

1. Record the customer's name and request.
2. Confirm what they need.
3. Link any related notes or project files.
4. Add the next action to the active task list.

# Related

- [Customer notes](../references/customer-notes.md)
```

### Sample `index.md`

```markdown
# Playbooks

This folder contains repeatable procedures.

- [Customer intake](customer-intake.md) - Steps for receiving and organizing a new customer request.
- [Weekly review](weekly-review.md) - A simple review routine for keeping the knowledge base current.
```

### Sample `log.md`

```markdown
# Directory Update Log

## 2026-06-27

- **Initialization**: Created the first OKF starter structure.
- **Creation**: Added customer intake and weekly review playbooks.
- **Validation**: Checked required frontmatter, reserved files, and internal links.
```

### Validation checklist

```text
[ ] Every non-reserved .md file has frontmatter.
[ ] Every non-reserved .md file has a non-empty type field.
[ ] index.md files describe folders and point to important children.
[ ] log.md files record meaningful history.
[ ] Internal links are portable.
[ ] No machine-specific paths are used for internal links.
[ ] No sensitive folders or private files were included by accident.
[ ] No giant catch-all files were created.
```

### Maintenance routine

```text
Daily or per project:
- Add one concept per file.
- Link related files.
- Update index.md when useful.

Weekly:
- Check links.
- Merge duplicates.
- Add missing descriptions.

Monthly:
- Archive stale files.
- Refine concept types.
- Validate the bundle.
```

### Reusable agent prompt

```text
Help me build or inspect an Open Knowledge Format knowledge base. First, ask me whether I already have a notes folder, second brain, vault, Drive folder, Git repo, or knowledge base. Ask where it is and whether I want to create a new OKF folder, modify an existing one, or only inspect and plan. Do not scan my whole computer. Only inspect folders I approve. Before changing anything, summarize what you found and show me your proposed structure. Do not delete, overwrite, move, or rename files unless I approve. Use OKF-style Markdown files with YAML frontmatter. Make one file per concept when creating new concept files. Use type as the required frontmatter field in every non-reserved .md file. Use index.md for discovery and log.md for change history. Validate the folder before calling it complete.
```

### Troubleshooting guide

If something feels messy, do not rebuild everything. Ask the agent for a small repair plan:

```text
Inspect this Open Knowledge Format knowledge base and recommend the smallest safe repair plan. Do not change anything yet. Report missing frontmatter, empty type fields, broken links, confusing file names, duplicate concepts, giant files, weak index.md files, missing log entries, machine-specific paths, and possible privacy issues. Then ask for approval before making any edits.
```

## Inspection Notes

Sources used:

- Google Cloud OKF announcement: <https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing>
- Official OKF v0.1 draft specification: <https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md>
- Andrej Karpathy's LLM Wiki pattern: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>
- Marie Haynes OKF overview: <https://www.mariehaynes.com/okf/>
- Optional video page reviewed for context: <https://www.youtube.com/watch?v=esYAIA6lU-s>

Key source notes:

- Google's OKF announcement frames OKF as an open, vendor-neutral, human-friendly and agent-friendly format made of Markdown files with YAML frontmatter.
- The official OKF spec says the required field is `type`, that only `index.md` and `log.md` are reserved Markdown filenames, that reserved files should not have frontmatter or be used as concept documents, that `log.md` entries are newest first, that broken links are tolerated by OKF consumers, and that OKF does not prescribe a fixed taxonomy or storage system.
- Karpathy's LLM Wiki pattern emphasizes a persistent, compounding wiki that agents maintain through indexing, logging, cross-linking, and periodic linting instead of re-discovering raw documents every time.
- Marie Haynes' overview adds a beginner-friendly business framing: each concept becomes a Markdown file, frontmatter works like an index card, and agents should use the structure to find the right knowledge instead of stuffing everything into context.

Assumptions made:

- The audience is non-technical or lightly technical.
- The runbook should favor safe behavior over aggressive migration.
- The first OKF build should be small enough for a beginner to inspect by hand.
- The runbook should not depend on Git, even though Git is useful when available.
- The runbook should work for private/local folders as well as team or public knowledge bases.

Human review recommended before publishing:

- Confirm whether the starter folder names match the target audience.
- Decide whether to include a tiny validator script in a future technical appendix.
- Decide whether to mention Git more strongly for team use.
- Re-check the official OKF spec before publishing publicly, because OKF v0.1 is marked as a draft and may change.
