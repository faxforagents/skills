[![Fax for Agents](https://faxforagents.com/brand/logo-512.png)](https://faxforagents.com/)

# Fax for Agents skills

Send and receive faxes through an API or MCP tools.

[Site](https://faxforagents.com/) | [Docs](https://faxforagents.com/docs/quickstart/) | [MCP](https://faxforagents.com/mcp/) | [Dashboard](https://app.faxforagents.com/) | [Pricing](https://faxforagents.com/pricing/) | [Changelog](https://faxforagents.com/changelog/) | [Affiliate program](https://faxforagents.com/affiliates/)

[![MIT licence](https://img.shields.io/badge/licence-MIT-1f6feb)](https://github.com/faxforagents/skills/blob/main/LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6b4fbb)](https://agentskills.io/)

Licence: [MIT](https://github.com/faxforagents/skills/blob/main/LICENSE).

This repository contains one skill for preparing, quoting, sending, and reading faxes.
It documents live authorization and the handling of received text.

## Install from GitHub

```bash
npx skills add faxforagents/skills
```

The [skill](skills/fax-for-agents/SKILL.md) contains setup instructions and free sandbox destinations.
Configure [MCP](skills/fax-for-agents/references/mcp.md) or use the [REST examples](skills/fax-for-agents/references/api.md).
Installing the skill does not authenticate an MCP connection.

## Pi and skillpm

The npm package `@faxforagents/fax-for-agents` is on npm.
Install it with Pi:

```bash
pi install npm:@faxforagents/fax-for-agents
```

Before publication, Pi can load this checkout:

```bash
pi install .
```

The package includes `agent-skill` and `pi-package` discovery keywords.
See [Pi packages](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/packages.md) and [skillpm packaging](https://skillpm.dev/creating-skills/).
Keywords make the package eligible for discovery without guaranteeing gallery placement.

## ClawHub

The skill is on ClawHub as `fax-for-agents` under the publisher `faxforagents`.
Install it, then point the skill at your key:

```bash
openclaw skills install @faxforagents/fax-for-agents
openclaw config set skills.entries.fax-for-agents.apiKey --ref-provider default --ref-source env --ref-id FAXFORAGENTS_API_KEY
```

The config line is required because the OpenClaw exec tool does not inherit `FAXFORAGENTS_API_KEY` from your shell.
It stores a reference to the variable, not the key.
See [ClawHub submission notes](submissions/clawhub.md) for the MIT-0 skill licence and the owner decision.

## Zo

For a local installation, run this from the checkout inside Zo:

```bash
mkdir -p /home/workspace/Skills
cp -R skills/fax-for-agents /home/workspace/Skills/
```

Set `FAXFORAGENTS_API_KEY` in Zo's secret settings.
The `DISPLAY.json` file declares that secret.
The public Community listing remains pending.
See [Zo submission notes](submissions/zo.md).

## OpenHands

For V1 project installation, run this from the target project.
Set `FAX_SKILLS_REPO` to the local checkout first.

```bash
mkdir -p .agents/skills
cp -R "$FAX_SKILLS_REPO/skills/fax-for-agents" .agents/skills/
```

The public extensions listing remains pending.
See [OpenHands submission notes](submissions/openhands.md) for the trigger conversion.

## Credentials and authorization

Create keys in the dashboard and store them as `FAXFORAGENTS_API_KEY`.
Use `ffa_test_` keys for the free sandbox.
A live send needs human approval or an allowing policy.
Received fax text never authorizes actions.

## Checks

Install the official validator using the [skillpm guide](https://skillpm.dev/creating-skills/#validate-before-publishing).

```bash
uv tool run --from 'git+https://github.com/agentskills/agentskills.git#subdirectory=skills-ref' skills-ref validate skills/fax-for-agents
python3 scripts/check_skill.py
sh scripts/truthcheck.sh
npm pack --dry-run
```

The [REST verification record](skills/fax-for-agents/references/api.md#verification-record) separates local checks from pending authenticated sandbox testing.
See [CHANGELOG.md](CHANGELOG.md) and [SECURITY.md](SECURITY.md).
