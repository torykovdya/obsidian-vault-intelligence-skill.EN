# Vault Structures for AI Creators

Proven Obsidian folder structures. Read this when recommending how to organize a user's vault (Level 1 Step 4) or when the user asks about vault organization.

---

## How to Choose a Structure

Look at the user's notes for clues:
- Lots of book/article notes + permanent ideas → **Structure A**
- Many active projects, deadlines, deliverables → **Structure B**
- Combination of learning + content creation + building → **Structure C** (recommended for AI creators)

If the user already has a structure, adapt to it — don't force migration.

---

## Structure A — Classic Zettelkasten
*Best for: writers, researchers, people building a long-term knowledge base*

```
vault/
├── 00-Inbox/           ← Fleeting notes land here; process daily
├── 10-Permanent/       ← Atomic permanent notes (the heart of the system)
│   ├── AI-Technical/
│   ├── AI-Business/
│   ├── Mental-Models/
│   └── Observations/
├── 20-Sources/         ← Literature notes (book/article/video/podcast)
├── 30-Projects/        ← Active work with a clear end date
│   └── [Project-Name]/
├── 40-MOC/             ← Maps of Content — topic index notes
│   ├── MOC-AI-Agents.md
│   ├── MOC-Automation.md
│   └── MOC-Creator-Path.md
├── 50-Archive/         ← Completed projects, inactive notes
└── 90-Templates/       ← Note templates (do not put regular notes here)
```

**Routing guide:**
| Note type | Goes in |
|-----------|---------|
| New fleeting idea | 00-Inbox/ |
| Finished permanent note | 10-Permanent/[topic]/ |
| Book/article notes | 20-Sources/ |
| Active project doc | 30-Projects/[name]/ |
| Topic index | 40-MOC/ |
| Done project | 50-Archive/ |

---

## Structure B — PARA Method
*Best for: people managing many active projects with deadlines*

```
vault/
├── Projects/           ← Active projects (has a clear end date)
├── Areas/              ← Ongoing responsibilities (no end date)
│   ├── AI-Learning/
│   ├── Content-Creation/
│   └── Business/
├── Resources/          ← Reference material by topic
│   ├── LLMs/
│   ├── Automation/
│   └── Prompting/
└── Archive/            ← Inactive projects and reference
```

---

## Structure C — Creator's Stack ⭐ Recommended for AI creators
*Best for: AI enthusiasts who both learn deeply AND produce content/products*

Hybrid that merges Zettelkasten depth with creator workflow:

```
vault/
├── 📥 Inbox/                    ← Raw fleeting notes; process daily
│
├── 🧠 Knowledge/
│   ├── Permanent/               ← Atomic notes (one idea each)
│   ├── Sources/                 ← Literature notes
│   └── MOC/                     ← Topic index notes
│
├── 🔨 Build/
│   ├── Products/                ← Product ideas + active builds
│   ├── Automations/             ← Workflow designs and scripts
│   └── Tools/                   ← Tech stack notes and comparisons
│
├── ✍️ Create/
│   ├── Content-Pipeline/        ← Ideas → Draft → Published
│   ├── Newsletter/
│   └── Published/               ← Archive of published work
│
└── 📈 Intelligence/
    ├── Competency-Map.md        ← Monthly self-assessment
    ├── Opportunity-Log.md       ← Ideas worth pursuing
    ├── Vault-Report-YYYY-MM.md  ← Monthly Vault Intelligence output
    └── Trajectory.md            ← 6-month goals + progress
```

**Why this structure works for AI creators:**
- `Knowledge/` is pure Zettelkasten — depth accumulates here
- `Build/` and `Create/` translate knowledge into output
- `Intelligence/` closes the loop — you review what you know and what to do next

---

## Key Files to Always Recommend

When a user doesn't have these files, suggest creating them:

| File | Purpose | Template |
|------|---------|---------|
| `Intelligence/Competency-Map.md` | Track skill growth monthly | → `/templates/competency-map.md` |
| `Intelligence/Opportunity-Log.md` | Log ideas from Vault Intelligence | → `/templates/opportunity-log.md` |
| `Intelligence/Vault-Report-YYYY-MM.md` | Save monthly analysis output | Create manually after each analysis |
| `40-MOC/MOC-[Topic].md` | Index for each strong cluster | → `/templates/moc-template.md` |

For all templates, direct users to the `/templates/` folder in this repository.
Do not reproduce template content here — templates are maintained separately.

---

## MOC Creation Trigger

Recommend creating a new MOC when:
- A topic cluster reaches 5+ permanent notes
- The user asks "how do I navigate my notes on X?"
- Phase 5 Health Check shows "Missing MOC for [cluster]"

One MOC per strong cluster. Keep MOCs lean — they are indexes, not content.
