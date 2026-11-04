# Tessl registry

Source: [Publish and update](https://docs.tessl.io/creating-skills-and-plugins/publish-and-update), read on 2026-11-04.

Tessl publishes skills through its CLI. A publication is private by default.
Public visibility needs an approval request and a later publication with public visibility.
Automatic linting and quality reviews run on every publication.

## Package

The canonical skill directory `skills/fax-for-agents` is the package. No plugin manifest is needed for one skill.

## Commands

```bash
tessl skill publish ./skills/fax-for-agents --workspace faxforagents --dry-run
tessl skill publish ./skills/fax-for-agents --workspace faxforagents
```

After approval:

```bash
tessl skill publish ./skills/fax-for-agents --workspace faxforagents --public --bump patch
```

## Steps only Ben can do

- Sign in to Tessl and confirm the `faxforagents` workspace exists under his account.
- Open the registry item, choose Actions, then Make Public, and confirm the request.
- Confirm whether a public release can be made private again before relying on it.
