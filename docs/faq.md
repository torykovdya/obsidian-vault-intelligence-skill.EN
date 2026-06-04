# FAQ

---

**Q: Does the skill work with notes in languages other than English?**

Yes — Claude understands and processes notes in any language natively. You can ask for the output in a different language than the notes themselves.

---

**Q: How many notes do I need for a meaningful Vault Intelligence analysis?**

Minimum: 20–30 notes to see patterns. Optimal: 50+. The more notes, the more accurate your competency map and trajectory forecast. But start with what you have.

---

**Q: Can I use this with Notion, Roam Research, or Logseq?**

Yes. The skill works with any text in Markdown format or even plain text. Just export your notes and paste them in. "Obsidian" is the target audience, not a hard requirement.

---

**Q: Does Claude retain my notes between sessions?**

No. Every session starts fresh. This means: save analysis results back into Obsidian. Create a file like `Intelligence/Vault-Report-2024-01.md` and paste the key insights from each monthly analysis.

---

**Q: How often should I run Vault Intelligence?**

Recommended rhythm:
- Daily: process Inbox (5 min)
- Weekly: analyze the week's notes (15 min)
- Monthly: full Vault Intelligence (30–45 min)
- Quarterly: strategic review (1–2 hours)

---

**Q: The skill suggests product ideas — how much should I trust them?**

The skill builds recommendations from your actual knowledge (your notes), not random suggestions. These are inferences from your own knowledge graph. Treat them as starting points for your own judgment, not directives.

---

**Q: Can I modify the skill for my own niche?**

Yes, and it's encouraged. The four files in `/skill/` are fully editable. Add your own patterns to `opportunity-patterns.md`, your own niches to `ai-creator-taxonomy.md`. See [docs/how-it-works.md](how-it-works.md) for details.

---

**Q: Is there an Obsidian plugin for this?**

Not yet — it's on the roadmap. The plan is a plugin that automatically exports your vault and sends it to Claude on a schedule.

---

**Q: Why should tags be contextual rather than categorical?**

Categorical tags (`#ai`, `#productivity`) answer the archivist's question: "where does this go?" Contextual tags (`#when-building-agents`, `#contradicts-my-belief-about-X`) answer the researcher's question: "when will I want to stumble on this again?"

Luhmann's point: the goal of the system isn't storage — it's creating the conditions for insights. An archive is dead. A knowledge graph is alive.

---

**Q: What should I do with orphan notes (no links)?**

Three options:
1. **Find a connection** — ask Claude: "what could this note connect to?"
2. **Develop it** — an orphan note often signals the start of a new cluster
3. **Delete it** — if no connection surfaces after a month, the idea probably wasn't significant

---

**Q: Does this only work for AI-related topics?**

No. The AI Creator Lens is an optional enrichment layer. The core analysis works for any domain: software development, marketing, research, creative writing. Replace the taxonomy in `ai-creator-taxonomy.md` with your own domain's skill map.

---

**Q: My vault is huge (1000+ notes). What's the best approach?**

Use the `export-vault.py` script with filters:
```bash
# Last 90 days only
python3 export-vault.py ~/Vault --days 90 > recent.txt

# Permanent notes folder only
python3 export-vault.py ~/Vault --folder "10-Permanent" > permanent.txt

# Stats first to understand your vault
python3 export-vault.py ~/Vault --stats
```

Then analyze in thematic batches rather than all at once.

---

**Q: How do I install the skill?**

Copy the contents of `skill/SKILL.md` from this repository. This is the instruction file for Claude — paste it into the System Prompt field or at the start of your conversation. The files in `skill/references/` don't need to be pasted manually; the skill references them automatically during analysis.

---

**Q: How can I contribute to the project?**

Read `CONTRIBUTING.md` in the root of the repository. We're especially looking for:
- New patterns for `skill/references/opportunity-patterns.md` — if you've spotted a recurring vault signal that isn't covered by the current 15 patterns
- Vault structure templates for specific niches (marketing, science, software development)
- Real analysis examples from real vaults (with your permission)

All changes via Pull Request. Discussions in Issues.
