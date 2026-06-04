# 🧠 Obsidian Vault Intelligence — Claude Skill

> *Transforms your notes into intellectual capital. Built on Niklas Luhmann's Zettelkasten method, tuned for AI enthusiasts, creators, and automation builders.*

---

## What This Is

**Obsidian Vault Intelligence** is a Claude skill that analyzes your Obsidian vault and answers the questions most AI tools ignore:

| Question | What the skill does |
|----------|---------------------|
| What am I actually becoming an expert in? | Builds a competency map from your notes |
| Which topics am I underexploring? | Finds blind zones and knowledge gaps |
| What articles should I write? | Generates ideas from your existing knowledge clusters |
| What product should I launch? | Finds unique intersections of your skills |
| What automations should I build? | Identifies "manual pain" patterns in your vault |
| Who will I be in 6 months? | Projects your knowledge trajectory |

---

## Two Operating Modes

```
┌─────────────────────────────────────────────────────┐
│  LEVEL 1: Note Intelligence                          │
│  Input: 1–10 notes                                   │
│  Output: Audit, rewritten Permanent Notes,           │
│  connections, smart tags, vault routing              │
├─────────────────────────────────────────────────────┤
│  LEVEL 2: Vault Intelligence                         │
│  Input: full vault or large dump                     │
│  Output: Knowledge map, competency map,              │
│  opportunities (articles/products/automations),      │
│  6-month forecast, vault health check                │
└─────────────────────────────────────────────────────┘
```

---

## Quick Start

### 1. Install the skill

Download `skill/SKILL.md` from this repository. This is the main skill file — paste its contents into the System Prompt field or load it as a skill in Claude's interface (if your version supports skills).

**Quick start:** copy the contents of `skill/SKILL.md` and paste it at the beginning of any Claude conversation about your notes.

### 2. First analysis (5 minutes)

Copy 5–10 notes from Obsidian and send to Claude:

```
Here are some notes from my Obsidian vault. Please analyze them:
1. What type is each note?
2. How can they be improved?
3. What do they reveal about my interests and expertise?

[paste your notes]
```

### 3. Full vault analysis (20–30 minutes)

Export your vault to text and send:

```
Here is my full Obsidian vault (or a section of it).
Run a Vault Intelligence analysis: knowledge map, competency map,
opportunities, and a 6-month growth forecast.

[paste vault content]
```

---

## Repository Structure

```
obsidian-vault-intelligence/
│
├── README.md                          ← you are here
├── CHANGELOG.md                       ← version history
├── CONTRIBUTING.md
├── LICENSE
│
├── skill/                             ← skill source files
│   ├── SKILL.md                       ← main file (Claude instructions)
│   └── references/
│       ├── ai-creator-taxonomy.md     ← AI niche taxonomy and archetypes
│       ├── vault-structures.md        ← vault structures + MOC templates
│       └── opportunity-patterns.md   ← 15 patterns for finding opportunities
│
├── docs/
│   ├── how-it-works.md               ← detailed logic explanation
│   ├── effective-usage.md            ← how to get maximum value
│   ├── zettelkasten-primer.md        ← Zettelkasten fundamentals
│   └── faq.md                        ← frequently asked questions
│
├── examples/
│   ├── single-note-analysis.md       ← before/after single note breakdown
│   ├── vault-intelligence-sample.md  ← full vault analysis example output
│   └── before-after-notes.md         ← 6 note transformation examples
│
├── templates/                         ← Obsidian templates
│   ├── permanent-note.md
│   ├── literature-note.md
│   ├── moc-template.md
│   ├── competency-map.md
│   └── opportunity-log.md
│
└── assets/
    └── vault-structure-diagram.png
```

---

## Philosophy

This skill is built on three principles from Sönke Ahrens' *How To Take Smart Notes*:

**1. Notes are only as valuable as the network they're embedded in**
> A single note is a fact. A linked note is knowledge. A thousand linked notes is intellectual capital.

**2. You can't plan for insight — but you can make your workflow conducive to finding it**
> The Zettelkasten is not an archive. It's an environment where ideas collide and generate new ones.

**3. Your notes predict what you can create**
> Luhmann wrote 58 books and 600 articles — alone, without the internet, without assistants. Not because he was a genius, but because his system showed him what he already knew.

---

## Who This Is For

- 🤖 **AI enthusiasts** — track how your expertise in LLMs, agents, and prompting grows
- ✍️ **Content creators** — find article topics hiding inside your own notes
- ⚡ **Automation builders** — surface automation patterns directly from your vault
- 🚀 **Indie makers** — discover your niche at the intersection of your knowledge
- 📚 **Knowledge networkers** — build a second brain that actively works for you

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). We especially welcome:
- New patterns for `opportunity-patterns.md`
- Vault structure templates for specific niches
- Real analysis examples (with permission)

---

## License

MIT — use, modify, distribute freely.

---

<p align="center">
  Built on the ideas of <a href="https://niklas-luhmann-archiv.de/">Niklas Luhmann</a> and the <a href="https://obsidian.md">Obsidian</a> ecosystem<br>
  Inspired by <em>How To Take Smart Notes</em> — Sönke Ahrens
</p>
