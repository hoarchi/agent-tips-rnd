# External Research Agent and Skill Survey

Captured: 2026-05-31

This survey records external precedents for `agent-rnd-phd`. It is not an
installation plan. Sources are design references and risk signals.

## Summary Judgment

No surveyed tool should be adopted as an unquestioned research authority.
The useful pattern is modular:

- use literature agents for source discovery and citation-grounded synthesis
- use benchmark harnesses for measurement
- use autonomous experiment loops only inside strong budget, security, and
  reproducibility boundaries
- use a claim ledger to prevent paper prose from outrunning evidence

## Sources Reviewed

| Source | Type | Useful pattern | Main risk | Adoption stance |
|---|---|---|---|---|
| OpenAI Skills | Agent skill format | Versioned folders with instructions, references, scripts, and assets | Skill text can steer agents strongly; needs review | Use format for our own skill |
| OpenAI Deep Research | Hosted research model/API | Browsing, synthesis, citations, internal file/MCP search | Citations and scope still need verification | Use as literature scout, not final authority |
| Future-House PaperQA | Scientific RAG | Literature QA with citations; metadata/retraction-oriented workflows | Domain is papers, not drawing QA experiments | Candidate subtool for literature review |
| Stanford STORM | Knowledge curation | Multi-perspective outline and long cited report generation | Report quality is not equivalent to peer-reviewed research | Use for survey outlines |
| GPT Researcher | Web research agent | Broad web/local report generation | Breadth can mask weak source quality | Use for early scouting only |
| Agent Laboratory | Research assistant framework | Literature review, experimentation, report writing stages | Generated research still needs human and benchmark gates | Use as workflow precedent |
| Sakana AI Scientist v2 | Autonomous scientific discovery | End-to-end ideation/experiments/manuscript; tree search | Code execution and fabricated/weak results are serious risks | Study, do not run by default |
| AutoResearchClaw | Multi-agent research pipeline | Structured debate, self-healing executor, verifiable reports, HITL modes | Very broad autonomy; new and needs audit | Borrow stage design cautiously |
| ARIS / Auto Claude Code Research in Sleep | Markdown skill suite | Overnight research loops, critic model, anti-hallucination checks | Overnight autonomy can amplify bad assumptions | Borrow critic/review patterns |
| ai-research-skills | Skill collection | Research design, literature triage, manuscript skills | Community project; must inspect before installation | Strong structural inspiration |
| research-hub | MCP/CLI workflow | Zotero/Obsidian/NotebookLM, DOI/arXiv verification, paper clusters | Tooling overhead and external account dependency | Possible later integration |

## Source Notes

### OpenAI Skills

OpenAI's public skills catalog describes skills as folders of instructions,
scripts, and resources that agents can discover and use for specific tasks.
This supports our choice to include `SKILL.md`, `references`-style docs,
templates, schemas, and scripts in one package.

Source: https://github.com/openai/skills

### OpenAI Deep Research

The API documentation positions deep research models for browsing, data
analysis, web search, remote MCP, and file search over internal data, with
inline citations in final answers. This is useful for literature scouting and
source collection, but final claims still require your own source gate and
experiment gate.

Source: https://platform.openai.com/docs/guides/deep-research

### PaperQA

PaperQA is explicitly a retrieval-augmented agent for scientific literature QA
with citations. It is a good fit for answering questions over papers and
checking scientific context, but it does not replace our drawing QA benchmark.

Sources:

- https://github.com/Future-House/paper-qa
- https://arxiv.org/abs/2312.07559

### STORM

STORM generates full-length reports with citations using multi-perspective
knowledge curation. It is useful for literature-map drafts and outline
generation, especially when we need breadth before choosing a precise
hypothesis.

Source: https://github.com/stanford-oval/storm

### GPT Researcher

GPT Researcher is useful for broad report generation across web/local sources.
Treat it as a scouting tool. It should not be trusted for final literature
claims without source verification and source-tier labeling.

Source: https://github.com/assafelovic/gpt-researcher

### Agent Laboratory

Agent Laboratory presents a staged autonomous research assistant spanning
literature review, experimentation, and report writing. The structure is useful,
but our agent must keep stronger gates around benchmark design, sensitive data,
and claim ledgers.

Source: https://github.com/SamuelSchmidgall/AgentLaboratory

### AI Scientist v2

AI Scientist v2 is an end-to-end autonomous scientific discovery system. It is
important as a frontier precedent, but this agent should not default to fully
autonomous code execution or paper generation. The lesson is not "let the agent
write a paper"; the lesson is to separate ideation, experiment execution,
review, and artifact traceability.

Sources:

- https://github.com/SakanaAI/AI-Scientist-v2
- https://arxiv.org/abs/2504.08066

### AutoResearchClaw

AutoResearchClaw reports a multi-agent research pipeline with structured debate,
self-healing execution, verifiable reporting, human-in-the-loop modes, and
cross-run evolution. These are relevant patterns, but the project is new and
should be audited before adoption.

Sources:

- https://github.com/aiming-lab/AutoResearchClaw
- https://arxiv.org/abs/2605.20025

### ARIS

ARIS-style Markdown skills emphasize overnight research loops, paper review,
revision, and anti-hallucination checks such as DBLP/CrossRef verification.
This supports our decision to include skeptical review and source gates.

Source: https://github.com/Unimposing-electroscope363/Auto-claude-code-research-in-sleep

### ai-research-skills and research-hub

The community `ai-research-skills` ecosystem demonstrates that research work
benefits from multiple narrow skills rather than a single mega-prompt.
`research-hub` suggests a concrete literature workflow around Zotero,
Obsidian, NotebookLM, DOI/arXiv verification, and clusters.

Sources:

- https://github.com/WenyuChiou/ai-research-skills
- https://glama.ai/mcp/servers/WenyuChiou/research-hub

## Design Decisions Imported Into agent-rnd-phd

1. Use a Codex-compatible skill entrypoint, but keep research protocols in
   separate files to avoid one giant prompt.
2. Add source reliability tiers.
3. Require benchmark definitions before performance claims.
4. Keep a claim ledger for manuscript writing.
5. Add skeptical review as a mandatory stage.
6. Allow multi-agent roles, but make the workflow executable sequentially.
7. Treat external autonomous paper systems as precedents, not authorities.

