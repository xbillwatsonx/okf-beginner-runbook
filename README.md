# OKF Beginner Runbook for Local Agentic Tools

Build or inspect an Open Knowledge Format knowledge base with any file-capable AI agent, CLI, desktop app, or local harness.

This package helps a person or AI agent create, inspect, or gradually convert a knowledge base into an Open Knowledge Format style structure.

## What This Does

Use this runbook with your agent. The agent asks qualifying questions about your setup and how you want to move forward. Then the agent can build a new knowledge base or modify your existing one to follow Google's OKF format and rules.

If your agent or tool supports editable operating instructions, the runbook can help it add approved guidance there so you and your agent know how to use the knowledge base moving forward.

## Highlights

- Compatible with existing agentic harnesses, CLIs, coding tools, and desktop AI apps.
- Works in local, cloud, or mixed environments.
- Can be opened in Obsidian as an optional visual Markdown vault.
- Can create a new OKF knowledge base from scratch.
- Can modify an existing knowledge base.
- User-friendly.
- Non-technical.
- Agent asks qualifying questions before implementing.
- Completely open source and free under the MIT License.

It is designed to work as a plain downloaded folder. Git is optional.

## What Is Included

- `runbook/okf-beginner-runbook.md` - The full beginner-friendly implementation runbook.
- `runbook/quick-start-card.md` - A one-page condensed OKF starter card.
- `starter-kit/okf-knowledge-base/` - A small OKF starter bundle you can copy and adapt.
- `prompts/` - Copy-paste prompts for agents and AI tools.
- `examples/` - Small examples of OKF-style files.
- `validate-okf.py` - A tiny dependency-free Python validator for basic OKF checks.
- `ABOUT.md` - Project background and purpose.
- `CONTACT.md` - How to ask questions or suggest improvements.
- `PRIVACY.md` - Plain privacy note for this static open-source project.
- `CHANGELOG.md` - Package history.
- `LICENSE` - MIT License.

## Quick Start

1. Open `runbook/quick-start-card.md`.
2. Read the one-page starter card, then open `runbook/okf-beginner-runbook.md` for detail.
3. Copy `starter-kit/okf-knowledge-base/` to the place where you want your knowledge base.
4. Use one of the prompts in `prompts/` with an AI agent that can read and write files.
5. Validate the result before calling it complete:

```bash
python3 validate-okf.py starter-kit/okf-knowledge-base
```

## Important Note

The OKF starter bundle is inside:

```text
starter-kit/okf-knowledge-base/
```

The surrounding project files, such as this `README.md`, are distribution materials. They are not part of the starter OKF knowledge base unless you intentionally copy them into one.

## Recommended Workflow

1. Start with a small knowledge domain.
2. Inspect only approved folders.
3. Preserve useful existing structure.
4. Add a light OKF wrapper before attempting a full migration.
5. Optionally open the folder in Obsidian for visual browsing.
6. Validate non-reserved Markdown files inside the OKF bundle.

## Project Info

- [About](ABOUT.md)
- [Contact](CONTACT.md)
- [Privacy](PRIVACY.md)
