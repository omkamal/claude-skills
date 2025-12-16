# Claude Skills

A collection of custom skills for Claude Code that extend its capabilities with specialized tools and workflows.

## Installation

### Quick Install (Recommended)

Add this repository as a Claude Code plugin marketplace:

```bash
/plugin marketplace add omkamal/claude-skills
```

Then install skills interactively:

```bash
/plugin
```

Select "Browse and install plugins" and choose the skills you want.

### Direct Install

Install a specific skill directly:

```bash
/plugin install nano-banana-illustrator@claude-skills
```

### Manual Installation

For personal use, copy a skill folder to your local skills directory:

```bash
cp -r skills/nano-banana-illustrator ~/.claude/skills/
```

For project-wide use, copy to your project's `.claude/skills/` directory and commit to git.

## Available Skills

| Skill | Description |
|-------|-------------|
| **nano-banana-illustrator** | Generate images using Google's Gemini Image API. Supports multiple models (pro/flash) and aspect ratios. |

## Creating New Skills

1. Create a new directory under `skills/`:
   ```bash
   mkdir skills/my-skill-name
   ```

2. Add a `SKILL.md` file with YAML frontmatter:
   ```yaml
   ---
   name: my-skill-name
   description: When to use this skill. Include trigger phrases and required env vars.
   ---

   # My Skill Name

   Instructions and documentation for the skill...
   ```

3. Add your implementation files (Python, shell scripts, etc.)

4. Document any dependencies and environment variables in the SKILL.md

## Skill Structure

```
skills/
└── skill-name/
    ├── SKILL.md          # Required: manifest with frontmatter + documentation
    └── implementation.*  # Your skill's code
```

### SKILL.md Format

The `SKILL.md` file requires YAML frontmatter with:

- **name**: Unique identifier (lowercase, hyphens for spaces)
- **description**: Complete description including when to use and required setup

The markdown body contains instructions Claude follows when the skill is active.

## Requirements

- [Claude Code](https://claude.ai/code) CLI
- Skill-specific dependencies (documented in each skill's SKILL.md)

## License

Apache 2.0 - See [LICENSE](LICENSE) for details.
