# Before / After — Note Transformations

Six real examples of how the skill rewrites notes of different types and quality levels.

---

## Example 1: Fleeting → Permanent

### BEFORE (Fleeting Note)
```
GPT-4o is way faster than GPT-4. Should use it everywhere.
```

### AFTER (Permanent Note)
```markdown
# Latency vs Quality: when model speed matters more than accuracy

GPT-4o is faster than GPT-4 at comparable quality on most tasks.
This changes the architectural default: for real-time tasks (chatbots,
interactive agents) speed is a feature that outweighs a few percentage
points of accuracy.

Rule: try the faster model first. Upgrade only if quality is unacceptable.
Not the other way around.

Links: [[Model Selection Decision Tree]] | [[Agent UX Principles]]
Tags: #when-choosing-model #for-agent-architecture #latency-tradeoff
Source: personal experience, 2024-01
```

**What changed:** observation → decision-making principle with a concrete rule

---

## Example 2: Poor Literature Note → Good One

### BEFORE (copy-paste from an article)
```
"The key to effective prompting is to think of the model as a 
very smart but very literal interpreter of instructions. 
It will do exactly what you say, not what you mean."
— some article
```

### AFTER (Literature Note done right)
```markdown
# LLMs as literal interpreters, not mind readers

LLMs execute what is written, not what is meant.
This is the fundamental error in most prompts: we assume the model will
"get the context." It won't — it follows the instruction.

Practical implication: every prompt needs to be read through the eyes of
a literal executor. "Make this better" is a meaningless instruction.
"Rewrite to be 30% shorter without losing the key arguments" is precise.

Links: [[Precision in Prompt Instructions]] | [[Why Vague Prompts Fail]]
Tags: #mental-model-for-prompting #explains-prompt-failures
Source: [article title, author, link]
```

**What changed:** quote → original thought with a practical takeaway

---

## Example 3: Monolith Note → Atomic Split

### BEFORE (everything in one note)
```markdown
# Everything I Know About RAG

RAG stands for Retrieval Augmented Generation. The way it works: take
documents, split into chunks, create embeddings, put in a vector DB. Then
at query time search for similar chunks and feed them into the prompt.

Problem: chunking quality affects everything. Bad chunks = bad retrieval.
There are different strategies: fixed-size, semantic, hierarchical.

Another problem — hallucinations still happen even with RAG. Need evals.
Can use LLM-as-judge to evaluate answer quality.

Tools: LlamaIndex, LangChain, Chroma, Pinecone, Weaviate.
LlamaIndex feels cleaner for RAG than LangChain in my experience.
```

### AFTER (4 atomic notes)

**Note 1:**
```markdown
# RAG: How It Works

Retrieval Augmented Generation — an approach where an LLM receives
relevant context from an external knowledge base before generating a response.

Cycle: documents → chunks → embeddings → vector DB → query →
similar chunk search → chunks + question in prompt → answer.

Key point: the model doesn't "know" the documents — it "reads" them fresh each time.

Links: [[Embeddings Explained]] | [[Vector DB Comparison]]
Tags: #rag-fundamentals #for-explaining-rag-to-others
```

**Note 2:**
```markdown
# Chunking strategy determines the quality of the entire RAG pipeline

Chunking quality is the most underrated parameter in RAG.
Bad chunks → bad retrieval → bad answers, even with a great model.

Three main approaches:
- Fixed-size: simple, but breaks semantic boundaries
- Semantic: more complex, but chunks contain complete thoughts
- Hierarchical: document → sections → paragraphs, enables zooming

Rule: start with semantic chunking. Fixed-size only if speed is critical.

Links: [[RAG Pipeline Architecture]] | [[Semantic Splitting Libraries]]
Tags: #rag-deep-dive #chunking #when-building-rag
```

**Note 3:**
```markdown
# RAG reduces hallucinations but doesn't eliminate them

Common misconception: RAG = no hallucinations.
Reality: RAG reduces the probability, but the model can still generate
fabricated details on top of real context.

Solution: evals. Specifically — LLM-as-judge: another model checks
whether the answer is actually supported by the retrieved context.

Links: [[LLM-as-Judge Pattern]] | [[Evals Pipeline Design]]
Tags: #rag-limitations #hallucinations #when-building-production-rag
```

**Note 4:**
```markdown
# LlamaIndex vs LangChain for RAG: personal experience

LlamaIndex specializes in data ingestion and retrieval.
LangChain is general-purpose, but RAG isn't its core strength.

In practice: LlamaIndex requires less boilerplate for typical RAG tasks.
LangChain is better if RAG is part of a complex agentic pipeline.

Source: personal experience building [project]
Links: [[AI Framework Selection]] | [[RAG Pipeline Architecture]]
Tags: #framework-comparison #rag-tooling
```

**What changed:** 1 monolith → 4 notes, each findable and reusable independently

---

## Example 4: Orphan Note → Integrated

### BEFORE (orphan, zero links)
```markdown
# Second Brain

The second brain concept — offloading cognitive load to an external system.
Book by Tiago Forte.
```

### AFTER
```markdown
# The Second Brain as External Cognitive Infrastructure

Tiago Forte: a "second brain" is an external system for storing and processing
information that reduces cognitive load.

Core principle: the brain is built to generate ideas, not store them.
Storage is the system's job.

Difference from Zettelkasten: Forte's PARA method is project-oriented,
Zettelkasten is knowledge-oriented. They can be combined: PARA as folder
structure, Zettelkasten as note quality standard.

Links: [[Zettelkasten vs PARA]] | [[Cognitive Offloading]] | [[PKM Comparison]]
Tags: #pkm-foundations #for-explaining-note-systems #when-choosing-vault-structure
Source: Building a Second Brain — Tiago Forte
```

**What changed:** isolated fact → interconnected node with 3 links and clear context

---

## Example 5: Bad Tags → Smart Tags

### BEFORE
```
Tags: #ai #tools #useful #productivity #notes
```

### AFTER
```
Tags:
#when-evaluating-new-ai-tools          ← retrieval context
#for-article-comparing-llm-ides        ← future use case
#contradicts-my-earlier-take-on-X      ← intellectual tension
#requires-follow-up-research           ← open loop
```

**Rule:** good tags are small questions or situations, not categories.

---

## Example 6: Unstructured Project Note → Phased

### BEFORE
```markdown
# Want to build an automation to process incoming emails with Claude
need to think about this
```

### AFTER
```markdown
# Project: Email Intelligence Agent

**Problem:** 40% of incoming emails are routine — and automatable.
**Solution:** Claude reads emails, classifies them, drafts a reply.

## Phase 1 — MVP (2 weeks)
- [ ] Gmail API connection via n8n
- [ ] Classification prompt: urgent / important / routine / spam
- [ ] Draft reply for routine emails
- [ ] Test on last 50 emails

## Phase 2 — Expansion (month 2)
- [ ] Auto-send for approved templates
- [ ] Stats dashboard

## Resources
- [[Gmail API Setup]] | [[n8n Email Nodes]] | [[Claude API Pricing]]

## Status: planning
## Related notes: [[Email Management Patterns]] | [[AI Automation ROI]]
Tags: #active-project #n8n #claude-api #email-automation
```
