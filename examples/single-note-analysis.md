# Example: Single Note Analysis

A real walkthrough of how the skill analyzes and improves a raw note.

---

## Input Note (Fleeting Note — raw)

```
agents are interesting
saw that langchain and autogen do something similar
need to look into this more
maybe write an article
```

---

## Skill Output

---

### 🔍 Note Analysis

**Type:** Fleeting Note
**Quality:** 1/5
**Status:** Needs rewriting before filing

**Issues:**
- ❌ Not standalone — "interesting" carries no meaning without context
- ❌ Not atomic — mixes: observation, tool list, TODO, and article idea
- ❌ No source — where did this observation come from?
- ❌ No connections
- ❌ No specifics — "something similar" — similar how, exactly?

---

### 📝 Permanent Note Version

The skill splits one fleeting note into three atomic notes:

**Note 1:**
```markdown
# LangChain and AutoGen solve the same problem with different architectures

LangChain builds agents through chains of calls (chains).
AutoGen uses multi-agent dialogues between models.
Same goal (autonomous task execution), fundamentally different design:
orchestration vs. negotiation.

Links: [[AI Agent Architectures]] | [[LLM Orchestration Patterns]]
Tags: #when-comparing-agent-frameworks #for-article-about-agents
```

**Note 2:**
```markdown
# Fragmented agent framework market signals an immature paradigm

When a market hasn't settled, many frameworks emerge with similar goals
(LangChain, AutoGen, CrewAI, LlamaIndex Agents...).
This is a normal early phase: experimentation first, consolidation later.

Analogy: before React, there were 10+ MVC frameworks for JS.

Links: [[Technology Adoption Curve]] | [[Framework Wars Pattern]]
Tags: #when-thinking-about-ai-ecosystem #market-timing
```

**Note 3 (Project Note — filed separately):**
```markdown
# Article idea: Comparing agent frameworks for practitioners

Problem: most comparisons are theoretical.
Angle: "I ran X, Y, Z on the same task — here's what actually worked"
Audience: developers who want to know where to start

Status: idea
Needs: define a test task, run both frameworks on it
```

---

### 🔗 Suggested Connections

- `[[ReAct Pattern]]` — both frameworks implement ReAct, but differently
- `[[Tool Use in LLMs]]` — agents = LLM + tools, worth linking
- `[[When to Use Agents vs Simple Pipelines]]` — the counterargument, needed for completeness
- `[[AI Ecosystem Map]]` — if you have an ecosystem map, add this observation there

---

### 🏷️ Smart Tags

```
#when-comparing-agent-frameworks
#for-article-about-ai-agents
#ecosystem-observation
#market-timing
```

---

### 💡 Insight for AI Creators

Your observation "they do something similar" is actually a signal of market immaturity. When many frameworks solve one problem differently, it means the niche hasn't crystallized — and **comparative content is currently scarce**. People are searching for "which one wins." You could be the person who gives an honest answer based on real use.

---

### 📁 Vault Location

```
00-Inbox/          ← delete the original fleeting note
10-Permanent/AI-Technical/agent-frameworks-comparison.md
10-Permanent/AI-Technical/framework-wars-pattern.md
20-Projects/article-agent-frameworks-comparison.md
```

---

## Before / After

| Before | After |
|--------|-------|
| 4 lines, 1 note | 3 atomic notes + 1 project note |
| Quality: 1/5 | Quality: 4/5 |
| Connections: 0 | Connections: 4 |
| Tags: 0 | Tags: 4 contextual |
| Next action: unclear | Next action: specific and clear |

---

## What to Do With This Output

1. Create three new files in Obsidian using the templates above
2. Delete the original fleeting note from Inbox
3. Open `20-Projects/article-agent-frameworks-comparison.md` and plan the first step
4. Add the article idea to `Intelligence/Opportunity-Log.md`
