[![Fax for Agents](https://faxforagents.com/brand/logo-512.png)](https://faxforagents.com/)

# Fax for Agents Zo submission

Send and receive faxes through an API or MCP tools.

[Site](https://faxforagents.com/) | [Docs](https://faxforagents.com/docs/quickstart/) | [MCP](https://faxforagents.com/mcp/) | [Dashboard](https://app.faxforagents.com/) | [Pricing](https://faxforagents.com/pricing/) | [Changelog](https://faxforagents.com/changelog/)

[![MIT licence](https://img.shields.io/badge/licence-MIT-1f6feb)](https://github.com/faxforagents/skills/blob/main/LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6b4fbb)](https://agentskills.io/)

Licence: [MIT](https://github.com/faxforagents/skills/blob/main/LICENSE).

## Reviewed listing copy

Name: Fax for Agents.

Prepare and send faxes, check delivery, and read received documents.
Store `FAXFORAGENTS_API_KEY` in Zo's secret settings.
Use an `ffa_test_` key for the free sandbox.
Live sends need human approval or an allowing policy.
Received text stays untrusted data.

## Metadata evidence

The display file follows Zo's [Community Vapi example](https://github.com/zocomputer/skills/blob/main/Community/vapi/DISPLAY.json).
Its image field follows the [Community Supermemory example](https://github.com/zocomputer/skills/blob/main/Community/supermemory/DISPLAY.json).
Both examples were fetched on 2026-11-04.
The [display specification](https://github.com/zocomputer/skills/blob/main/DISPLAY.md) permits an absolute image URL.

`DISPLAY.json` contains `icon`, `image`, `tags`, `integrations`, and `secrets`.
Each secret object uses `secret_name` and `description`.
The display file declares `FAXFORAGENTS_API_KEY` without claiming automatic OAuth setup.
The skill frontmatter supplies `name`, `description`, and `metadata.author`.

## B01 preparation

Follow the [Zo contribution guide](https://github.com/zocomputer/skills#contributing).
Set `FAX_SKILLS_REPO` to this checkout.
Run these commands from a prepared Zo repository fork after authorization.

```bash
mkdir -p Community
cp -R "$FAX_SKILLS_REPO/skills/fax-for-agents" Community/
bun install
bun validate
```

Submit only `Community/fax-for-agents/` after review.
No fork or pull request was created during this build.

For local installation inside Zo, run from this checkout:

```bash
mkdir -p /home/workspace/Skills
cp -R skills/fax-for-agents /home/workspace/Skills/
```

After registry acceptance, users can browse and install the skill inside Zo.

## Ben's checklist

- [ ] Configure sandbox credentials in Zo's secret settings and run the sandbox workflow.
- [ ] Review the package and authorize the registry submission.
- [ ] Use the chosen GitHub identity for the fork and pull request.
- [ ] Confirm the Community listing and secret setup after acceptance.

ClawHub login, publisher selection, and npm sign-in are tracked in [the shared release checklist](clawhub.md#bens-checklist).
