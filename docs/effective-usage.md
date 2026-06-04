# How to Use Obsidian Vault Intelligence Effectively

> The tool is only as good as your input. This guide shows you how to get maximum value.

---

## Principle #1: Garbage In, Garbage Out — But Start Anyway

Claude analyzes what you give it. Better-structured notes yield more precise analysis. But even messy notes are valid raw material. Don't wait for a perfect vault.

---

## Use Case Scenarios

### 🔸 Scenario A: Breaking Down a Single Note

**When to use:** you just wrote a note and want to improve it

**How to prompt:**
```
Here's a note from my Obsidian vault. Please analyze it:
- What type of note is this?
- How atomic is it?
- Rewrite it as a Permanent Note
- Suggest connections to other concepts
- What smart tags should I add?

--- NOTE ---
[your note text]
```

**What you get:** rewritten note, 3–5 connections, smart tags, vault location

---

### 🔸 Scenario B: Processing a Batch of Notes

**When to use:** 10–50 unprocessed notes have piled up in your Inbox

**How to prompt:**
```
Here are my unprocessed notes from my Inbox folder.
For each one:
1. Identify the type (Fleeting / Literature / Permanent)
2. Rate quality on a scale of 1–5
3. Rewrite the worthy ones as Permanent Notes
4. For the rest, tell me what to do with them

--- NOTES ---
[note 1]
---
[note 2]
---
[note 3]
```

**Pro tip:** include the date of each note — Claude will identify trends more accurately

---

### 🔸 Scenario C: Cluster Analysis

**When to use:** you want to understand how deep your knowledge is on a specific topic

**How to prompt:**
```
Here are all my notes on [AI agents / prompt engineering / automation].
Build a map of this topic:
- What do I know well?
- Where are the gaps?
- What content or product could I create from this?

--- NOTES ON TOPIC ---
[all notes on the topic]
```

---

### 🔸 Scenario D: Full Vault Intelligence

**When to use:** monthly strategic review

**How to export your vault:**

*Method 1 — manually (for smaller vaults, up to ~30 notes):*
1. Open your vault folder in Finder / File Explorer
2. Select the `.md` files you want to analyze — e.g. everything in `10-Permanent/`
3. Open each file and paste the contents into a single text document
4. Send that document to Claude

> ⚠️ Obsidian does not have a "Export to PDF" option for the whole vault. Use one of the methods below instead.

*Method 2 — terminal:*
```bash
# Collect all .md files from vault into one file
find ~/ObsidianVault -name "*.md" -exec cat {} \; > vault-export.txt
```

*Method 3 — Python script (in /examples):*
```bash
python3 examples/export-vault.py ~/ObsidianVault > vault-export.txt
```

**How to prompt:**
```
Here is an export of my Obsidian vault from the past 3 months.
Please run a full Vault Intelligence analysis:
1. Knowledge map (clusters, blind zones)
2. Competency map
3. Top 3 articles I can write
4. Top 3 products / automations
5. 6-month forecast

[vault content]
```

---

## How to Prepare Notes for Better Analysis

### Minimal prep (2 minutes)
Add to the top of each note:
```
Date: 2024-01-15
Topic: AI Agents
Type: fleeting / literature / permanent
```

### Optimal prep (5 minutes per batch)
The note structure Claude analyzes most effectively:
```markdown
# Title (one idea)

## The Idea
[core point in 1-3 sentences, in your own words]

## Source
[where the idea came from: book / video / personal experience]

## Connections
- similar to [[another idea]]
- contradicts [[a third idea]]

## Application
[how this can be used]

Tags: #prompt-engineering #when-building-agents
Date: 2024-01-15
```

---

## Power Prompts

### Find what to write about right now
```
Here are my notes. I need an article or post idea I can write this week.
Look for: a dense knowledge cluster + my unique angle + a topic people care about.
Give me the top 3 ideas with an explanation of why I specifically should write each one.

[notes]
```

### Discover your blind zones
```
I work in [AI automation / LLM content / etc.].
Here are my notes. What important things am I NOT studying?
What should be in my vault but isn't?
What am I missing that my peers likely know?

[notes]
```

### Plan your learning for the next month
```
Here are my current notes and knowledge level.
Build a 4-week learning plan:
- What to study (specific, not abstract)
- In what order (what unlocks what)
- How it feeds back into my vault
- What opportunities it unlocks

[notes + current context]
```

### Turn your vault into a product
```
I want to create a [course / tool / service / newsletter].
Here are my notes. What existing knowledge can I package right now?
- What's the minimum viable product I could build in 2 weeks?
- Which specific notes does it draw from?
- Who needs this?

[notes]
```

---

## Common Mistakes

### ❌ "My notes aren't ready / they're a mess"
**Reality:** messy notes are normal input. The skill was built for exactly this. Send them as-is.

### ❌ Sending one note at a time indefinitely
**Better:** collect 20–30 notes and send together. Patterns only emerge from mass.

### ❌ Ignoring suggested connections
**Important:** when Claude suggests `[[link to concept X]]` — create that note in Obsidian. That's how the graph grows.

### ❌ Not returning to the analysis
**Better:** run Vault Intelligence monthly. Compare competency maps. Watch yourself grow.

### ❌ Copying others' notes into your vault
**Zettelkasten principle:** only your own words. Copying is an illusion of knowledge, not knowledge.

---

## Recommended Working Rhythm

```
DAILY (5–10 min)
└── Process Inbox: fleeting notes → permanent notes
    Prompt: "Rewrite these as Permanent Notes"

WEEKLY (15–20 min)
└── Cluster review for the week
    Prompt: "What did I learn this week? What connections?"

MONTHLY (30–45 min)
└── Full Vault Intelligence
    Prompt: full vault analysis, update competency map

QUARTERLY (1–2 hours)
└── Strategic review
    Prompt: "What changed in 3 months? What should I build next?"
```

---

## Obsidian Integration

### Useful plugins
- **Dataview** — SQL-style queries to your vault, helps collect notes by topic
- **Templater** — automate note templates
- **Graph Analysis** — visualize connections
- **Smart Connections** — AI-powered similar note search

### Collect notes by tag (Dataview query)
```dataview
LIST
FROM #ai-agents
SORT file.mtime DESC
```

---

## Progress Metrics

Track monthly:

| Metric | How to measure |
|--------|---------------|
| Permanent Notes | File count in `/10-Permanent/` |
| Avg connections per note | Claude estimates during analysis |
| Active clusters | Topics with 5+ notes |
| Orphan notes | Notes with zero links |
| New notes/week | Log in `Intelligence/Trajectory.md` |

> Luhmann wrote 6 permanent notes per day. Your goal isn't 6 — it's consistency. Even 3 notes per week is 150 permanent ideas in a year.

---

## Next Step

1. Install the skill (file in `/releases`)
2. Open Obsidian, copy your 10 most recent notes
3. Send to Claude using the Scenario B prompt above
4. Create `Intelligence/Competency-Map.md` in your vault using the analysis output
5. Repeat in one month and compare

Your vault is your intellectual capital. The skill just makes it visible.
