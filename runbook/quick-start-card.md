# OKF Quick-Start Card

OKF is a plain Markdown folder pattern that helps people and agents organize linked knowledge with simple frontmatter.

## Beginner Flow

1. Pick a domain.
2. Tell the agent what you already have.
3. Approve one folder for inspection.
4. Let the agent summarize and propose a structure.
5. Let the agent build only after approval.

Optional: open the OKF folder in Obsidian as a free visual Markdown vault.

## Minimum Folder Structure

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

## Frontmatter Template

```yaml
---
type: Playbook
title: Example Title
description: A short plain-language summary.
tags: [example, starter]
timestamp: 2026-07-01T00:00:00Z
---
```

## Reserved Files

- `index.md` = discovery
- `log.md` = history

Reserved files do not need frontmatter. Other `.md` files need frontmatter with a non-empty `type`.

## Copy-Paste Prompts

- `prompts/build-or-inspect-okf-knowledge-base.md` - Start a new OKF build or inspect an existing folder.
- `prompts/convert-existing-knowledge-base-to-okf.md` - Convert an existing knowledge base gradually.
- `prompts/validate-okf-knowledge-base.md` - Check an OKF folder before calling it complete.
- `prompts/repair-okf-knowledge-base.md` - Inspect and recommend repairs for an OKF folder.

## Validator

From the repo root:

```bash
python3 validate-okf.py starter-kit/okf-knowledge-base
```

For the full explanation, read [the beginner runbook](okf-beginner-runbook.md).
