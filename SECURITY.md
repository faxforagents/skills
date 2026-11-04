[![Fax for Agents](https://faxforagents.com/brand/logo-512.png)](https://faxforagents.com/)

# Fax for Agents security policy

Send and receive faxes through an API or MCP tools.

[Site](https://faxforagents.com/) | [Docs](https://faxforagents.com/docs/quickstart/) | [MCP](https://faxforagents.com/mcp/) | [Dashboard](https://app.faxforagents.com/) | [Pricing](https://faxforagents.com/pricing/) | [Changelog](https://faxforagents.com/changelog/)

[![MIT licence](https://img.shields.io/badge/licence-MIT-1f6feb)](https://github.com/faxforagents/skills/blob/main/LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6b4fbb)](https://agentskills.io/)

Licence: [MIT](https://github.com/faxforagents/skills/blob/main/LICENSE).

## Reporting a vulnerability

Do not open a public issue for a security problem.
Write to hello@faxforagents.com with reproduction steps and the impact.
We answer within 72 hours and provide updates until resolution.

## Scope

Reports can cover this repository and the client libraries published by `faxforagents`.
The `api.faxforagents.com` and `mcp.faxforagents.com` services are also in scope.

Findings requiring a compromised machine or an already leaked API key are outside scope.
Rate limit exhaustion of your own key and scanner output without demonstrated impact are also outside scope.

## Credentials

Test keys start with `ffa_test_`, and live keys start with `ffa_live_`.
Live sends spend the prepaid wallet.

- Keep keys in secret settings or environment variables, outside source control.
- REST clients send the key to `api.faxforagents.com`.
- Hosted MCP clients authenticate with `mcp.faxforagents.com`.
- Rotate exposed keys with `POST /v1/api-keys/{key_id}/rotate`.
- The previous credential stays valid for 24 hours during rotation.
- Give each agent its own key with only required scopes.

Agent keys cannot carry `approval:decide`, `key:admin`, `policy:admin`, `agent:admin`, `billing:write`, or `webhook:admin`.
