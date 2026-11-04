[![Fax for Agents](https://faxforagents.com/brand/logo-512.png)](https://faxforagents.com/)

# Fax for Agents ClawHub submission

Send and receive faxes through an API or MCP tools.

[Site](https://faxforagents.com/) | [Docs](https://faxforagents.com/docs/quickstart/) | [MCP](https://faxforagents.com/mcp/) | [Dashboard](https://app.faxforagents.com/) | [Pricing](https://faxforagents.com/pricing/) | [Changelog](https://faxforagents.com/changelog/)

[![MIT licence](https://img.shields.io/badge/licence-MIT-1f6feb)](https://github.com/faxforagents/skills/blob/main/LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6b4fbb)](https://agentskills.io/)

Licence: [MIT](https://github.com/faxforagents/skills/blob/main/LICENSE).

## Reviewed listing copy

Name: Fax for Agents.
Slug: `fax-for-agents`.
Category: `communication`.
Topics: `fax,api`.

Prepare documents, quote fax costs, check delivery, and read received faxes.
Live sends need human approval or an allowing policy.
Use an `ffa_test_` API key for the free sandbox.
Live sends use a paid Fax for Agents account.

## Release status

The package is prepared locally and has not been published.
The [ClawHub format](https://github.com/openclaw/clawhub/blob/main/docs/skill-format.md#license) requires MIT-0 for published skills.
This repository and package retain MIT as requested.
Do not publish this artifact unchanged to ClawHub.
Ben must resolve the licence conflict before publication.
No alternate licence grant is included here.

Runtime requirements are declared under `metadata.openclaw`.
`FAXFORAGENTS_API_KEY` is required for REST and stdio, while hosted OAuth uses client authentication.
Tool scopes and network permissions appear in the skill body.
Portable trigger phrases remain under `metadata.triggers`.

## B01 commands

These are preparation and future publication commands, not a record of execution.
Run them from this repository after resolving the licence conflict.

```bash
skills-ref validate skills/fax-for-agents
npm pack --dry-run
npm i -g clawhub
clawhub login
clawhub whoami
clawhub skill publish ./skills/fax-for-agents --slug fax-for-agents --name "Fax for Agents" --categories communication --topics fax,api --dry-run
clawhub skill publish ./skills/fax-for-agents --slug fax-for-agents --name "Fax for Agents" --categories communication --topics fax,api
```

Add `--owner faxforagents` only after Ben confirms authority over that ClawHub owner.
Wait until security checks finish and the release becomes installable.
See the [publishing quickstart](https://docs.openclaw.ai/clawhub/quickstart).

## npm distribution

Install the official Python validator on `PATH` before using skillpm.
The [skillpm guide](https://skillpm.dev/creating-skills/) documents this isolated installation:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install 'git+https://github.com/agentskills/agentskills.git#subdirectory=skills-ref'
skills-ref validate skills/fax-for-agents
```

Keep `.venv/` out of version control.
Sign in as the authorized npm publisher before running B01's publication command.

```bash
npm login
skillpm publish --access public
pi install npm:@faxforagents/fax-for-agents
```

The npm package retains MIT.
Check Pi and skillpm discovery after publication.

## Ben's checklist

- [ ] Resolve ClawHub's MIT-0 requirement before publishing any ClawHub artifact.
- [ ] Sign in with `clawhub login` and confirm identity with `clawhub whoami`.
- [ ] Choose the publisher owner and confirm organization authority.
- [ ] Sign in to npm and confirm scope ownership and authentication requirements.
- [ ] Supply a sandbox key and complete the documented smoke test.
- [ ] Review the dry run before authorizing publication.
- [ ] Wait for ClawHub security checks and verify installation.
- [ ] Confirm Pi and skillpm discovery after npm publication.

## Later directory submission

The [awesome OpenClaw list](https://github.com/VoltAgent/awesome-openclaw-skills/blob/main/CONTRIBUTING.md) requires publication and real community usage.
Do not submit a new skill immediately after publication.
Require passing ClawHub tests and clean security status first.
The proposed description is eight words:

Send and receive faxes through Fax for Agents.
