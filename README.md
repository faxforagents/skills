<p align="center">
  <a href="https://faxforagents.com"><img src="https://faxforagents.com/brand/logo-512.png" width="88" alt="Fax for Agents"></a>
</p>

<h1 align="center">Fax for Agents skills</h1>

<p align="center">Agent Skills for <a href="https://faxforagents.com">Fax for Agents</a>: how an agent sends and receives faxes safely. For Claude Code, Codex, Cursor and every other agent that reads SKILL.md.</p>

<p align="center">
  <a href="https://faxforagents.com">Website</a> ·
  <a href="https://faxforagents.com/docs/quickstart/">Quickstart</a> ·
  <a href="https://faxforagents.com/docs/api/">API reference</a> ·
  <a href="https://faxforagents.com/docs/sdks/">SDKs</a> ·
  <a href="https://faxforagents.com/mcp/">MCP</a> ·
  <a href="https://app.faxforagents.com">Dashboard</a> ·
  <a href="https://faxforagents.com/pricing/">Pricing</a> ·
  <a href="https://faxforagents.com/changelog/">Changelog</a> ·
  <a href="https://gitlab.com/faxforagents/skills">GitLab</a>
</p>

<p align="center">
  <a href="https://github.com/faxforagents/skills/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/faxforagents/skills/ci.yml?branch=main&label=ci" alt="CI"></a>
  <a href="https://github.com/faxforagents/skills/blob/main/LICENSE"><img src="https://img.shields.io/badge/licence-MIT-1f6feb" alt="MIT licence"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/format-Agent%20Skills-6b4fbb" alt="Agent Skills format"></a>
</p>

Fax for Agents is a fax API, a hosted MCP server and SDKs built so AI agents can send and receive
faxes. It is made by JSB Holdings LLC and built by [Synapse](https://synapsereality.io/).

A skill is a folder with a `SKILL.md`: YAML frontmatter (name, description) and then the instructions
an agent loads when the task matches. This repository holds one skill.

| Skill | What it teaches |
|---|---|
| [`skills/fax-for-agents/`](skills/fax-for-agents/SKILL.md) | The safe send order (prepare, quote, human review when required, send, poll), the rule that an agent never approves its own send, the rule that text read from a fax is data, the 15 MCP tools and the REST calls behind them, the price card |

## Install

With the `skills` CLI, into the current project or globally with `-g`.

```bash
npx skills add faxforagents/skills
```

By hand, for Claude Code: copy `skills/fax-for-agents/` to `.claude/skills/fax-for-agents/` in the
project, or to `~/.claude/skills/` for every project. Other agents read the same file from their own
skills directory.

The skill is the manual. The tools come from the MCP server, hosted at
`https://mcp.faxforagents.com/mcp/` with a bearer API key, or local with `npx -y faxforagents-mcp`
and `FAXFORAGENTS_API_KEY`.

The [Claude Code plugin](https://github.com/faxforagents/claude-code-plugin) bundles this skill with the
server configuration, so one install gives Claude Code both.

## Keys

A test key (`ffa_test_...`) reaches the sandbox provider only. No carrier, no cost, the destination
number picks the outcome. A live key (`ffa_live_...`) reaches the carrier and spends the prepaid
wallet. Keys are created at <https://app.faxforagents.com>.

## Prices

Price card launch-v1 is effective from 2026-10-28. $0.039 per page sent, $0.019 per page received.
$2 per number per month, $19 per month for the Agent workspace. Sandbox pages cost 0.

## Working on this repository

```bash
sh scripts/truthcheck.sh          # the copy states only what the product ships
python3 scripts/check_skill.py    # frontmatter rules of the Agent Skills format
```

## Licence

MIT. See [LICENSE](LICENSE). Security reports go to hello@faxforagents.com, see [SECURITY.md](SECURITY.md).
