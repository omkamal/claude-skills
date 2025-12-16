# Claude Skills

A collection of custom skills for [Claude Code](https://claude.ai/code) that extend its capabilities with specialized tools and workflows.

## What are Skills?

Skills are self-contained utilities that Claude Code loads automatically when relevant. When you install a skill, Claude gains new capabilities - like generating images, manipulating documents, or integrating with external APIs - without any manual intervention.

## Installation

### Prerequisites

1. Install [Claude Code CLI](https://claude.ai/code)
2. Ensure you have an active Claude Code session

### Method 1: Plugin Marketplace (Recommended)

**Step 1:** Add this repository as a marketplace:

```bash
/plugin marketplace add omkamal/claude-skills
```

**Step 2:** Browse and install skills interactively:

```bash
/plugin
```

Select **"Browse and install plugins"** → **"claude-skills"** → Choose your skill → **"Install now"**

### Method 2: Direct Install

Install a specific skill in one command:

```bash
/plugin install nano-banana-illustrator@claude-skills
```

### Method 3: Manual Installation

**Personal use** (available in all your projects):
```bash
git clone https://github.com/omkamal/claude-skills.git
cp -r claude-skills/skills/nano-banana-illustrator ~/.claude/skills/
```

**Project-wide** (shared with team via git):
```bash
mkdir -p .claude/skills
cp -r claude-skills/skills/nano-banana-illustrator .claude/skills/
git add .claude/skills
git commit -m "Add nano-banana-illustrator skill"
```

## Using Skills in Claude Code

Once installed, skills activate automatically based on context. Simply describe what you want:

```
"Generate an image of a sunset over mountains"
"Create a portrait illustration of a robot"
"Make a cinematic wide shot of a forest"
```

Claude will recognize the intent and use the appropriate skill.

## Available Skills

### nano-banana-illustrator

Generate images using Google's Gemini Image API (Nano Banana).

**Setup:**
```bash
pip install google-genai
export GOOGLE_API_KEY=your_api_key_here
```

**Features:**
- **Models**: `pro` (high quality, 4K) or `flash` (fast generation)
- **Aspect Ratios**: landscape (16:9), portrait (9:16), square (1:1), cinematic (21:9)
- **Image Editing**: Pass reference images for style transfer or editing

**CLI Usage:**
```bash
# Basic generation
python generate_image.py "A sunset over mountains" -o sunset.png

# Portrait mode with flash model
python generate_image.py "A robot" -o robot.png -a portrait -m flash

# With reference image
python generate_image.py "Make this image more colorful" -i reference.jpg -o output.png
```

**In Claude Code:**
```
"Generate a landscape image of a cyberpunk city at night"
"Create a square profile picture of a friendly AI assistant"
```

## Managing Plugins

```bash
# List installed plugins
/plugin

# Update marketplace
/plugin marketplace update claude-skills

# Remove a plugin
/plugin uninstall nano-banana-illustrator

# Remove marketplace
/plugin marketplace remove claude-skills
```

## Creating New Skills

1. Create a directory under `skills/`:
   ```bash
   mkdir skills/my-skill-name
   ```

2. Add `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: my-skill-name
   description: When to use this skill. Include trigger phrases and required env vars.
   ---

   # My Skill Name

   Instructions Claude follows when using this skill...

   ## Usage
   Examples and guidelines...
   ```

3. Add implementation files (Python, shell scripts, etc.)

4. Update `.claude-plugin/marketplace.json` to include your skill:
   ```json
   {
     "name": "my-skill-name",
     "source": "./skills/my-skill-name",
     "description": "Brief description",
     "version": "1.0.0"
   }
   ```

## Repository Structure

```
claude-skills/
├── .claude-plugin/
│   └── marketplace.json    # Plugin marketplace configuration
├── skills/
│   └── nano-banana-illustrator/
│       ├── SKILL.md        # Skill manifest and documentation
│       └── generate_image.py
├── CLAUDE.md               # Claude Code guidance
├── LICENSE                 # Apache 2.0
└── README.md
```

## Contributing

1. Fork this repository
2. Create your skill in `skills/your-skill-name/`
3. Add a `SKILL.md` with proper frontmatter
4. Update `marketplace.json`
5. Submit a pull request

## License

Apache 2.0 - See [LICENSE](LICENSE) for details.

## Author

Omar Kamal Hosney
