# How It Works

A detailed look at the skill's logic — for those who want to understand the mechanics or adapt it for their own use.

---

## Skill Architecture

```
Incoming request
       │
       ▼
┌──────────────────┐
│  Input Detector  │  ← Determines level: 1 or 2
└────────┬─────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
LEVEL 1    LEVEL 2
Note       Vault
Intel.     Intel.
    │         │
    │    ┌────┴──────────────────────────────┐
    │    │  Phase 1: Thematic Extraction     │
    │    │  Phase 2: Competency Map          │
    │    │  Phase 3: Opportunity Intelligence │
    │    │  Phase 4: Trajectory Forecast     │
    │    │  Phase 5: Vault Health            │
    │    └───────────────────────────────────┘
    │
┌───┴──────────────────────────┐
│  Step 1: Classify note type  │
│  Step 2: Atomic audit        │
│  Step 3: Enrich for AI/Creator│
│  Step 4: Route to vault      │
└──────────────────────────────┘
         │
         ▼
    Structured Output
```

---

## Where the Zettelkasten Logic Comes From

The skill implements three key principles from Luhmann:

### Principle 1: Atomicity
Luhmann stored exactly one idea per slip. The skill checks each note against 5 criteria and rewrites it if it isn't atomic.

**Why it matters:** atomic notes can be reused in different contexts. Note blocks cannot.

### Principle 2: Context Tags
Luhmann didn't ask "where does this go?" — he asked "when will I want to find this?" The skill generates the second type of tag.

**Example:**
- Bad tag: `#ai` (storage category)
- Good tag: `#when-building-rag-pipelines` (retrieval context)

### Principle 3: Compounding Through Connections
Vault value doesn't grow linearly with note count — it grows exponentially with connection count. The skill suggests connections on every analysis pass.

**Luhmann's math:** 90,000 notes × average connections = foundation for 58 books and 600 articles.

---

## Vault Intelligence Logic (Level 2)

### Phase 1: Thematic Extraction

The skill looks for:
- **Recurring concepts** — words/ideas appearing in 3+ notes
- **Clusters** — groups of concepts that frequently appear together
- **Trends** — topics whose density is growing
- **Lone wolves** — important ideas mentioned once, then dropped

This works even without explicit `[[links]]` — purely through semantic text analysis.

### Phase 2: Competency Map

The skill uses the taxonomy from `references/ai-creator-taxonomy.md` — a list of ~20 key skills for AI creators — and maps them against vault clusters.

**Depth scoring logic:**
- 1 note on topic → mention
- 3–5 notes → familiarity
- 5–10 notes → working knowledge
- 10+ notes with cross-references → expertise

### Phase 3: Opportunity Intelligence

Uses 15 patterns from `references/opportunity-patterns.md`. Each pattern is a signal in the vault pointing to a specific type of opportunity.

**Example pattern:** "Dense Cluster" — 5+ notes on one topic → suggests writing a definitive guide on exactly that topic.

### Phase 4: Trajectory Forecast

Forecast logic:
1. Find the strongest cluster → this is the current expertise signal
2. Find the fastest-growing cluster → this is where to invest
3. Find the critical gap → what needs to be learned next
4. Combine (1) + (3) → what the user becomes in 6 months
5. Match against archetypes → specific "who you're becoming" output

### Phase 5: Health Check

Evaluates vault structural health across 6 metrics:
- % of atomic notes
- Count of orphan notes (no links)
- Presence of MOC notes
- Fleeting → Permanent pipeline
- Tag quality (contextual vs categorical)
- Last activity date

---

## Why This Is Built for AI Enthusiasts

The skill adds an "AI Creator Lens" — three additional tests for each cluster:

**Build It Test:** can this knowledge cluster become a tool or agent?
→ Looks for "input → process → output" structures in notes

**Teach It Test:** is the knowledge deep enough to teach others?
→ Evaluates depth and uniqueness of angle

**Compound It Test:** which clusters create a rare combination?
→ Looks for intersections most people in the niche don't have

---

## Limitations

**What the skill does NOT do:**
- Does not read your vault directly (no Obsidian API integration — yet)
- Does not persist vault history between Claude sessions
- Does not replace your own work of creating connections

**What affects analysis quality:**
- More notes = more accurate patterns
- Dates on notes = more accurate trend detection
- Your own words (not quotes) = better understanding of your thinking

---

## Extending and Adapting

The skill is 4 files. You can edit any of them:

| File | What you can change |
|------|---------------------|
| `SKILL.md` | Analysis steps, output formats |
| `ai-creator-taxonomy.md` | Add your own niches and archetypes |
| `vault-structures.md` | Add structures for your specialization |
| `opportunity-patterns.md` | Add patterns from your own experience |
