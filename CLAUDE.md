# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains Claude Code skills - self-contained utilities that extend Claude Code's capabilities. Each skill lives in `skills/<skill-name>/` with a `SKILL.md` manifest and implementation files.

## Skill Structure

Each skill must include:
- `SKILL.md` - YAML frontmatter with `name` and `description`, followed by usage documentation
- Implementation files (Python scripts, shell scripts, etc.)

The SKILL.md frontmatter format:
```yaml
---
name: skill-name
description: When to use this skill. Include trigger phrases and required environment variables.
---
```

## Running Skills

Skills are standalone utilities. Example for nano-banana-illustrator:
```bash
# Setup
pip install google-genai
export GOOGLE_API_KEY=your_key

# Generate image
python skills/nano-banana-illustrator/generate_image.py "A sunset over mountains" -o output.png
```

## Creating New Skills

1. Create directory: `skills/<skill-name>/`
2. Add `SKILL.md` with frontmatter describing when to invoke the skill
3. Add implementation files
4. Document dependencies and environment variables in SKILL.md
