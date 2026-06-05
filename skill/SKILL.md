---
name: obsidian-vault-intelligence
description: >
  Analyzes Obsidian vaults and Zettelkasten note systems to extract
  knowledge maps, competency gaps, and creator opportunities. Use when
  the user shares notes or vault content, asks "what should I write
  about", "what product should I build", "analyze my vault", "map my
  skills", "what am I becoming an expert in", or wants a 6-month
  knowledge trajectory. Also use when the user pastes raw markdown notes
  without an explicit question — treat it as a note audit request.
  NOT for: code review, creative writing, general Q&A, or anything
  unrelated to personal knowledge management and note analysis.
---

# Obsidian Vault Intelligence Skill

Transforms raw Obsidian notes into **actionable intellectual capital** — grounded in Luhmann's Zettelkasten method and tuned specifically for AI enthusiasts, creators, and automation builders.

Core philosophy from *How To Take Smart Notes* (Ahrens):
> "Notes are only as valuable as the note-and-reference network they are embedded in."
> "You can't plan for insight — but you can make your workflow conducive to finding it."

---

## Level Selection — Choose Before Starting

**Count the notes in the input, then pick the level:**

| Input size | Level | What to do |
|-----------|-------|------------|
| < 5 notes | LEVEL 1 only | Full Note Intelligence for each note |
| 5–20 notes | LEVEL 1 + mini Phase 1 | Process each note + brief thematic map |
| 20+ notes | LEVEL 2 only | Full Vault Intelligence, all 5 phases |
| Any size + user says "analyze my vault" | LEVEL 2 | Full Vault Intelligence regardless of count |

When in doubt: fewer notes → LEVEL 1. Explicit vault request → LEVEL 2.

---

## LEVEL 1: Note Intelligence

### Input Detection
User provides: one note, a few notes, a raw brain dump, or a Markdown file.

### Step 1 — Classify the Note Type

| Type | Description | Action |
|------|-------------|--------|
| **Fleeting** | Raw idea, shower thought, quick capture | Convert → Permanent |
| **Literature** | From a book/article/video | Extract core insight, add source |
| **Permanent** | Standalone atomic idea | Audit quality, suggest links |
| **Orphan** | Note with no connections | Find home in the knowledge graph |
| **Project** | Working doc for a specific output | Structure into phases |
| **Index/MOC** | Map of Content | Expand with missing nodes |

### Step 2 — Apply the Atomic Note Audit

Check each note against Luhmann's permanence criteria:
- [ ] **Standalone**: Understandable without external context?
- [ ] **Atomic**: One clear idea per note?
- [ ] **In your own words**: Not just a copied quote?
- [ ] **Linked**: Connected to ≥1 other note/concept?
- [ ] **Actionable context**: Tagged with "In what context would I want to find this again?"

If any criterion fails → rewrite the note. Show before/after.

**Quality Score scale (use this every time):**
```
1/5 — Fleeting: no structure, meaningless without context
2/5 — Has an idea, but mixes multiple thoughts or is just a quote
3/5 — One idea, but not standalone OR no connections
4/5 — Atomic, standalone, ≥1 link, has a contextual tag
5/5 — Everything in 4/5 + original insight or unique author angle
```

### Step 3 — Enrich for AI/Creator Context

**🔗 Connection Suggestions** (3–5 ideas this connects to)
```
This note connects to:
- [concept X] — because both deal with [pattern]
- [concept Y] — this could challenge or extend it
- [tool/framework Z] — practical application
```

**💡 Insight Extraction**
Pull out the non-obvious angle. Ask: "What does this mean for AI builders specifically?"

**🏷️ Smart Tags** (context-based, not category-based)
Following Ahrens' rule: tags should answer "when would I want to stumble on this?" not "which folder does this belong to?"

Bad tags: `#ideas #notes #ai`
Good tags: `#when-building-agents #for-content-about-llms #contradiction-to-explore`

**📌 Permanent Note Draft**
If the input is a Fleeting or Literature note, output a polished Permanent Note version.

### Step 4 — Route to Obsidian Structure

→ READ `references/vault-structures.md` to pick the right folder for this user's vault style.

Default structure (Structure A — Classic Zettelkasten):
```
📁 Suggested vault location:
  00-Inbox/           ← still processing
  10-Permanent/       ← atomic ideas (the heart)
  20-Sources/         ← literature notes
  30-Projects/        ← active work with a clear end date
  40-MOC/             ← index/map notes
  50-Archive/         ← completed or dormant
  90-Templates/       ← reusable structures
```

If the user has a different structure visible in their notes, adapt to it.

---

## LEVEL 2: Vault Intelligence

### Input Detection
User provides: many notes, a folder dump, a vault export, or explicitly asks "analyze my vault."

---

### Phase 1 — Thematic Extraction

Scan all notes and extract:
1. **Recurring concepts** (appear in 3+ notes)
2. **Concept clusters** (groups of related ideas)
3. **Emerging obsessions** (topics gaining density recently — look at dates)
4. **Lone wolves** (important ideas mentioned once, never developed)

Output format:
```
🗺️ YOUR KNOWLEDGE MAP

STRONG CLUSTERS (your expertise zones):
■ [Topic A] — X notes, Y connections — Depth: ████████░░ 80%
■ [Topic B] — X notes, Y connections — Depth: ██████░░░░ 60%

EMERGING CLUSTERS (you're building here):
◧ [Topic C] — X notes — Trend: ↑ growing
◧ [Topic D] — X notes — Trend: → steady

LONE WOLVES (mentioned once, need development):
◈ [Idea X] — appears in 1 note — worth expanding?
◈ [Idea Y] — mentioned in passing

BLIND ZONES (gaps that matter for your profile):
○ [Missing Topic E] — expected given A+B, but absent
○ [Missing Topic F] — mentioned in passing, never developed
```

---

### Phase 2 — Competency Map

→ READ `references/ai-creator-taxonomy.md` now. Use the Core Skill Domains table as the skill list. Use the Archetypes table to identify which archetype the user is heading toward.

Build a skills/expertise graph specifically for AI creators:

```
🧠 COMPETENCY MAP

TECHNICAL DEPTH:
  LLM Architecture    ████████░░  needs: fine-tuning mechanics
  Prompt Engineering  ██████████  strong
  AI Agents           ██████░░░░  needs: memory systems, orchestration
  Automation          ████████░░  needs: error handling patterns

CREATOR SKILLS:
  Content Strategy    ██████░░░░  needs: distribution systems
  Audience Building   ████░░░░░░  early stage
  Product Thinking    ██████░░░░  needs: go-to-market

UNIQUE COMBINATION (apply Rarity Matrix from taxonomy):
  [Skill A] × [Skill B] = [why this is rare in the market]

ARCHETYPE: [closest match from taxonomy]
  Heading toward: [target archetype]
  Gap between now and there: [specific skill or experience]

GAPS TO FILL (prioritized):
1. [Gap] — blocks [Goal]
2. [Gap] — needed for [Opportunity]
```

**Depth scoring logic:**
- 1 note → mention (░░░░░░░░░░)
- 3–5 notes → familiarity (██░░░░░░░░)
- 5–10 notes → working knowledge (████░░░░░░)
- 10+ notes with cross-links → expertise (████████░░)
- 10+ notes + original frameworks → mastery (██████████)

---

### Phase 3 — Opportunity Intelligence

→ READ `references/opportunity-patterns.md` now. Apply all 15 patterns across Articles, Products, and Automations sections. For each match found, report it.

→ Also apply the **Rarity Matrix** from `references/ai-creator-taxonomy.md`: which two clusters form a rare combination in this person's market?

This is the Slip Box's hidden superpower: your accumulated notes predict what you can create.

#### 📝 Articles You Should Write
*(Based on note clusters + density + unique angle — match to patterns in opportunity-patterns.md)*

```
TOP 3 ARTICLE OPPORTUNITIES:
1. "[Title idea]"
   Pattern matched: [e.g. Dense Cluster / Surprising Connection / Contradiction]
   Why you: X notes on this. Your angle is unique because [reason].
   Evidence nodes: [note 1], [note 2], [note 3]
   Target audience: [who]
   Format: [Social thread / Blog post / Deep dive — based on note density from taxonomy]

2. "[Title idea]"
   ...
```

#### 🚀 Products / Projects to Launch

```
TOP 3 PRODUCT OPPORTUNITIES:
1. "[Product concept]"
   Pattern matched: [e.g. Repeated Pain / Unique Combination / The Framework]
   Type: [tool / course / newsletter / agent / automation]
   Based on: your depth in [X] + gap you've identified in [Y]
   Rare combination: [Skill A] × [Skill B] (most people only have one)
   Minimum viable: [what you could ship in 2 weeks]
   Price range: [estimate]

2. ...
```

#### ⚡ Automations to Build

```
TOP 3 AUTOMATION OPPORTUNITIES:
1. "[Automation idea]"
   Pattern matched: [e.g. Repeated Copy-Paste / Information Aggregation]
   Opportunity: [what this unlocks for the user]
   Solves: [pain point found in your notes]
   Stack: [tools implied by your notes]
   Complexity: [low / medium / high]
   Time saved: [estimate per week]

2. ...
```

---

### Phase 4 — Trajectory Forecast

*"We co-evolve with our Slip Box. Learning begets learning."* — Ahrens

[SPECULATIVE]

Forecasts are hypotheses generated from note density,
knowledge patterns, and observed trajectories in the vault.

They do not predict future outcomes, market success, or career results.
Treat them as directional signals for reflection and planning, not promises.

Use the **Growth Archetypes** from `references/opportunity-patterns.md` (Deepener / Connector / Builder / Teacher) to identify which path fits this vault, then project forward:

```
📈 6-MONTH KNOWLEDGE TRAJECTORY

Growth archetype: [Deepener / Connector / Builder / Teacher]
Why: [evidence from vault]

IF current learning patterns continue and the identified gaps are addressed:
[FORECAST] Month 1–2:
[Specific action] → [Likely outcome]

[FORECAST] Month 3–4:
[Specific action] → [Likely outcome]

[FORECAST] Month 5–6:
[Specific action] → [Potential outcome]

WHO YOU'RE BECOMING:
  Now:      [accurate label based on vault]
  Month 3:  [specific intermediate milestone]
  Month 6 (hypothesis):[likely emerging role based on current vault patterns]

WHAT MAKES THIS CREDIBLE (cite vault evidence):
  - You already have X permanent notes on [topic] — that's the top 5% of people writing about it
  - Your note density on [Y] grew fastest in the last [N] weeks
  - The [A]+[B] combination is rare: most people in your niche know only one
---

### Phase 5 — Vault Health Report

```
🏥 VAULT HEALTH CHECK

NOTE QUALITY:
  ✅ Atomic notes (1 idea each):  XX%  [goal: 70%+]
  ⚠️ Orphan notes (no links):     XX   [goal: <10% of total]
  ❌ Quote dumps (not processed): XX   [needs rewriting in own words]
  ❌ Stale Inbox (>3 days old):   XX   [process or delete]

STRUCTURE:
  ✅ / ⚠️ / ❌  Has Inbox folder
  ✅ / ⚠️ / ❌  Permanent notes separated from fleeting
  ✅ / ⚠️ / ❌  MOC notes exist for strong clusters
  ✅ / ⚠️ / ❌  Competency Map file exists
  ✅ / ⚠️ / ❌  Opportunity Log file exists
  ✅ / ⚠️ / ❌  Tags are contextual (not just categorical)

RECOMMENDATIONS (prioritized by impact):
1. 🔴 [Most impactful fix — do today]
2. 🟡 [Second fix — do this week]
3. 🟢 [Third fix — do this month]
```

---

## AI Creator Lens — Special Enrichments

Use these three questions to decide
which opportunity patterns deserve attention.

Build It:
Could this cluster become a tool, workflow, or system?

Teach It:
Could this cluster become content, education, or media?

Compound It:
Does this cluster create unusual value when combined with another cluster?

Apply the matching opportunity patterns and the Rarity Matrix to identify the strongest opportunities.
---

## Output Templates

### Single Note Output
```markdown
## 🔍 Note Analysis

**Type:** [Fleeting / Literature / Permanent / Orphan / Project]
**Quality Score:** X/5 — [one-line reason]
**Status:** [Ready to file / Needs rewriting / Needs connections]

### 📝 Permanent Note Version
[Rewritten in atomic, standalone form]

### 🔗 Suggested Connections
- [[Note or concept 1]] — [why]
- [[Note or concept 2]] — [why]
- [[Note or concept 3]] — [why]

### 🏷️ Smart Tags
`#[when-context]` `#[for-use-case]` `#[relationship-to-other-ideas]`

### 💡 Insight for AI Creators
[Non-obvious application or implication — what does this unlock?]

### 📁 Vault Location
`[suggested folder path]/[suggested-filename.md]`
```

### Vault Intelligence Output
Deliver all 5 phases in order. Do not skip phases even if the vault is small.
Label each phase clearly with its emoji header.

---

## Zettelkasten Principles (Quick Reference)

1. **Atomic**: One idea per note. If you're scrolling, it's too long.
2. **Own words**: Copying quotes = hoarding, not learning.
3. **Connected**: Notes are only valuable in the network they're embedded in.
4. **Context-tagged**: Tag for retrieval context, not storage category.
5. **Progressive**: Fleeting → Literature → Permanent. Don't skip steps.
6. **Selective**: Not everything is noteworthy. Quality > quantity.
7. **Discoverable**: The goal is to stumble upon insights, not just store them.

---

## Reference Files — When to Read Each

| File | Read during |
|------|------------|
| `references/ai-creator-taxonomy.md` | Phase 2 (Competency Map) + Phase 3 (Opportunity) |
| `references/vault-structures.md` | Level 1 Step 4 (routing) + any vault org question |
| `references/opportunity-patterns.md` | Phase 3 (Opportunity Intelligence) + Phase 4 (Trajectory) |

Always read the relevant reference file **before** generating that section's output — not after.
