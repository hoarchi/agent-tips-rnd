# Templates

Reusable formats for this R&D agent. Two kinds live here:

1. **Markdown workflow templates** — the research-loop artifacts the agent
   leaves behind (brief → hypothesis → benchmark → experiment → ledger →
   review → manuscript plan).
2. **DOCX deliverable formats** — JSON spec + Python generator pairs that emit
   submission-grade Word documents:
   - **연구노트 (research note)** — Korean R&D lab-notebook format with a
     configurable company/author/reviewer signature line.
   - **논문 (manuscript)** — academic paper, IMRaD, Korean or English.

Both DOCX formats follow the same architecture: a JSON spec carries the
content, a generator under `scripts/` turns it into a `.docx`. Edit the JSON,
never the generated Word file.

---

## 1. Markdown workflow templates

| Template | Stage | Schema (machine-checkable JSON) |
|---|---|---|
| `research-brief.md` | Intake | `schemas/research_question.schema.json` |
| `literature-matrix.md` | Landscape | `schemas/source_record.schema.json` |
| `hypothesis-card.md` | Question framing | — |
| `benchmark-card.md` | Benchmark design | `schemas/benchmark_card.schema.json`, `benchmark_item.schema.json` |
| `experiment-card.md` | Experiment | `schemas/experiment_card.schema.json` |
| `claim-ledger.md` | Evidence ledger | `schemas/claim_ledger.schema.json` |
| `peer-review-report.md` | Skeptical review | — |
| `manuscript-plan.md` | Paper planning | — |

`manuscript-plan.md` is the *planning* skeleton (working title, target venue,
contribution candidates, claim boundaries). The *full paper body* is produced by
the manuscript DOCX generator below — plan first, then draft.

---

## 2. 연구노트 (research note) — DOCX

Three ways to use it — pick whichever fits:

1. **Open the prebuilt DOCX** `templates/research-note-template.docx` directly in
   Word and fill it in. (Rendered from the empty spec — no tools needed.)
2. **Edit the JSON spec** `templates/research-note.json` and generate a DOCX.
3. Both: generate once, then keep editing the JSON and regenerating.

- **Prebuilt DOCX:** `templates/research-note-template.docx`
- **Spec template:** `templates/research-note.json` (an emptied, fill-in
  skeleton — copy it and write your own note)
- **Generator:** `scripts/create_research_note_docx.py`

### Build

```bash
python scripts/create_research_note_docx.py \
  --input  programs/<program_id>/research-notes/<YYMMDD>/research-note-spec.json \
  --output programs/<program_id>/research-notes/<YYMMDD>/연구노트_<YYMMDD>.docx
```

`--sample` is **optional**: a `.docx` whose styles (fonts, table styles) are
reused. If omitted, a blank document is used — so the command above works with
nothing but the JSON. Pass `--sample <any existing note>.docx` only if you want
to inherit a specific document's styles. Write the spec under the owning
program's `research-notes/{YYMMDD}/` folder.

### Spec fields

| Field | Meaning |
|---|---|
| `title` / `subtitle` | `연구노트` + English program subtitle |
| `project_name` | Korean formal project name (과제명) |
| `researcher`, `date`, `research_type`, `research_storage` | Header KV table. Date as `YYYY.MM.DD` |
| `purpose` / `summary` | `[연구목적]` / `[연구내용]` blue box |
| `sections[]` | `{heading, paragraphs[], bullets[], tables[]}` |
| `paragraphs[]` | string, or `{text, dash, first_line_twips}` — `dash:true` prints a leading `-` |
| `bullets[]` | `{lead, body}` — `lead` is bolded; rendered as `List Paragraph` |
| `tables[]` | `{headers, rows, widths_twips}` (section-level or top-level) |
| `footer_company/author/reviewer` | Signature line |

### Style rules (enforced by the generator — see also `SKILL.md`)

- **Brief nominal endings only.** Use `확장함 / 필요함 / 확인함 / 것임 / 아님 /
  금지`. Narrative endings (`하였다 / 했다 / 되었다 / 한다 / 것이다 / 있다`)
  are **rejected** at build time. Write in report-bullet style from the start.
- **One date only.** Any full date in the body/header/footer that differs from
  the spec `date` is rejected.
- **Footer** is a single signature line driven by the spec
  `footer_company / footer_author / footer_reviewer` fields: `페이지 PAGE /
  NUMPAGES YYYY. MM. DD {회사} 작성자 : … / 검토자 : …`. Do not add a second
  internal-use line.
- Body paragraphs use first-line indent; list items carry no manual hyphen.

The default 7-section flow (연구 질문 → 방법 → 결과 → 실패 유형 → 응용 관점 →
결론 → 다음 계획, + 요약 표) is reflected in `research-note.json`. Add, remove,
or rename sections freely — the generator renders whatever the spec contains.

---

## 3. 논문 (manuscript) — DOCX

- **Prebuilt DOCX:** `templates/manuscript-template.docx` (open in Word to see
  the layout)
- **Spec template:** `templates/manuscript.json`
- **Generator:** `scripts/create_manuscript_docx.py`

### Build

```bash
python scripts/create_manuscript_docx.py \
  --input  <program>/manuscripts/<name>/manuscript.json \
  --output <program>/manuscripts/<name>/manuscript.docx \
  [--sample style-carrier.docx]   # optional; blank document if omitted
```

`--sample` is **optional** here (unlike the research note). Relative `image`
paths in figures resolve against the spec file's folder.

### Spec fields

| Field | Meaning |
|---|---|
| `title` / `subtitle` | Centered title block |
| `authors[]` | `{name, mark}` — `mark` is the affiliation/corresponding superscript (e.g. `"1*"`) |
| `affiliations[]`, `corresponding` | Centered lines under authors |
| `abstract` (+ `abstract_secondary`) | Bordered abstract box; secondary box for a 국문/영문 second abstract |
| `keywords[]` | Italic keyword line |
| `sections[]` | `{heading, level?, paragraphs[], bullets[], equations[], figures[], tables[], sections[]}` — `sections[]` nests subsections |
| `heading` numbering | Level inferred from the leading number depth: `2` → H1, `2.1` → H2, `2.1.3` → H3 (or set `level` explicitly) |
| `paragraphs[]` | string, or `{text, no_indent}` — narrative prose, justified, **no** brief-ending rule |
| `figures[]` | `{caption, image?, width_in?, placeholder?}` — embeds the image if present, else a labeled placeholder box; auto-numbered `Figure N` |
| `tables[]` | `{caption?, headers, rows, widths_twips}` — auto-numbered `Table N` |
| `equations[]` | string or `{text, number}` — centered, optional `(n)` number |
| `references[]` | strings — rendered as a hanging-indent `[n]` list |
| `*_label` fields | `abstract_label`, `keywords_label`, `references_label`, `figure_label_prefix`, `table_label_prefix` — switch to Korean (`초록`, `그림`, `표`) for KCI/국내 학회 |

### Notes

- Default fonts: Times New Roman (latin) + Malgun Gothic (Hangul). Works for
  English-only, Korean-only, or mixed manuscripts — the generator does not care
  which language the headings and body are in.
- Plan with `manuscript-plan.md` and the claim ledger first. **Every
  quantitative claim in the manuscript must already exist in the claim ledger**
  (Claim Gate in `SKILL.md`). The generator does not check this — the agent must.
- Suggested home for drafts: `programs/{program_id}/manuscripts/{name}/`.

---

## Dependencies

Both DOCX generators need `python-docx`:

```bash
python -m pip install python-docx
```
