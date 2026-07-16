# 🧬♻️ longevity-loop — an AI-native compounding loop for aging science

<div align="center">

[![CI](https://img.shields.io/github/actions/workflow/status/wjlgatech/longevity-loop/ci.yml?style=flat-square&label=loop%20check)](https://github.com/wjlgatech/longevity-loop/actions)
[![Last Updated](https://img.shields.io/github/last-commit/wjlgatech/longevity-loop?style=flat-square&label=last%20turn)](https://github.com/wjlgatech/longevity-loop/commits/main)
[![License](https://img.shields.io/github/license/wjlgatech/longevity-loop?style=flat-square)](LICENSE)

🛠️ **Method & tooling: [FM-os](https://github.com/wjlgatech/FM-os)** — the SLM/foundation-model-ops hub and the closed-loop machinery this project runs on. longevity-loop is FM-os applied to a real mission.

A solo builder's public, self-improving loop for AI × longevity: pick a falsifiable question → analyze open aging data → score on a public verifier → write it up honestly → share → let the artifact recruit people, feedback, and funding → repeat, harder. Built in public, verified not vibed.

**North star:** climb a credibility-gated, code-only leaderboard (the [Biomarkers of Aging Challenge](https://www.longevityprize.com/prize/biomarker) on the open Biolearn platform) — real signal in aging science with **no wet lab**.

</div>

---

> Not medical advice. Computational results on public data are labeled as such and kept strictly separate from any wet-lab/therapeutic claim (which requires independent validation). No evidence ⇒ no claim.

---

<h2 id="the-loop">♻️ The Loop (one turn of the flywheel)</h2>

Each turn is falsifiable and ends in a shared, verifiable artifact. No evidence ⇒ no claim.

| # | Stage | What happens |
|--:|---|---|
| 1 | **QUESTION** | State one falsifiable question + the metric that settles it (and the null you'd accept). |
| 2 | **DATA** | Pull an OPEN aging dataset (CELLxGENE, Tabula Muris Senis, GEO, GTEx, the Biomarkers challenge set). |
| 3 | **MODEL** | Analyze / fine-tune an open bio-FM (pyaging, Geneformer, scGPT) — cheaply, reproducibly. |
| 4 | **VERIFY** | Score on a public verifier — the Biolearn leaderboard or a held-out benchmark. No evidence ⇒ no claim. |
| 5 | **WRITE-UP** | Honest report: result AND the null/failure, threats-to-validity, a reproduce command. |
| 6 | **SHARE** | Build in public — repo + thread + explainer; route to the human hubs (VitaDAO, LBF, Foresight). |
| 7 | **COMPOUND** | The artifact recruits feedback, collaborators, and funding → they unlock the next, harder question. |

> ⑦ COMPOUND feeds back into ① — each turn adds data, a tool, or a connection, so the next question is bigger.

---

<h2 id="turns">📓 Turns Log</h2>

Every turn of the loop, logged honestly. `done` requires a PROOF (result incl. the null + a reproduce command).

| Turn | Question | Stage | Status |
|---|---|---|:--|
| [turn-01-biolearn-baseline](turns/turn-01-biolearn-baseline) | Motivated by Levine's Systems Age (2025): does cross-clock DISAGREEMENT (heterogeneity across a clock panel) add predictive signal over the best single clock on the Biomarkers-of-Aging open data? | VERIFY | 🧩 scaffolded |
| [turn-02-biofm-finetune](turns/turn-02-biofm-finetune) | Does fine-tuning an open single-cell FM beat a frozen-embedding linear probe at predicting age? | MODEL | 🧩 scaffolded |

---

<h2 id="frontier">🛰️ Frontier Radar</h2>

The frontier groundbreakers' most recent deep works — verified, with a link + a real quote. Refreshed weekly by [`scripts/track.py`](scripts/track.py) (arXiv + GitHub).

- **Alex Zhavoronkov** — [The End of Aging Clocks: Training Foundation Models to Reason in Aging and Longevity](https://www.biorxiv.org/content/10.64898/2026.03.28.714980v1) _(2026)_
  Longevity-LLM v0.1 (fine-tuned Qwen3-14B) hit 4.34-yr MAE epigenetic-age prediction (beating Horvath) across methylation/proteomics/clinical/RNA, and handled multiple longevity tasks.
  > "These results demonstrate that a single modestly sized LLM can match or replace purpose-built aging clocks across data modalities."
  → _Future:_ Interim report from Insilico's Multi-Modal AI Gym for Science (MMAI) — foundation models for drug discovery + aging.
- **Morgan Levine** — [Systems Age: one blood methylation test quantifying aging across 11 physiological systems](https://www.nature.com/articles/s43587-025-00958-3) _(2025)_
  DNA-methylation clocks that score aging separately per system (heart, lung, brain, immune…) from one blood draw, beating global clocks at system-relevant disease prediction.
  > "most epigenetic clocks provide a single age estimate, overlooking within-person variation."
  → _Future:_ System-specific clocks usable clinically to track how interventions shift aging in individual organ systems.
- **Tony Wyss-Coray** — [Plasma proteomic signatures of cellular aging predict human disease](https://pubmed.ncbi.nlm.nih.gov/42297981/) _(2026)_
  From >7,000 plasma proteins in 60,542 people, ML models estimate biological age of 40+ cell types, linking cell-type-specific aging to disease and mortality.
  > "Aging is asynchronous across cells and organs."
  → _Future:_ Cell-type-resolved plasma proteomic clocks as clinical biomarkers from a single blood test.
- **Vadim Gladyshev** — [Mammalian aging involves genome-wide splicing degeneration leading to functional decline](https://www.biorxiv.org/content/10.64898/2026.06.26.734787v1) _(2026)_
  Integrative mouse/human analysis shows aging systematically loses RNA-splicing fidelity ('splicing degeneration'), rising with age but alleviated by calorie restriction or rapamycin — a proposed new hallmark.
  > "aging is characterized by systematic deterioration of the fidelity of RNA splicing, here termed splicing degeneration"
  → _Future:_ Splicing degeneration as 'a promising target for aging interventions acting to reverse' it.
- **João Pedro de Magalhães** — [Translational toolkit for reproducible, cross-study profiling of human ageing hallmarks](https://www.biorxiv.org/content/10.64898/2026.04.20.719545v1) _(2026)_
  A validated assay toolkit to simultaneously quantify 8+ ageing hallmarks (senescence, immune ageing, mTOR, autophagy, genomic instability…) in clinically accessible human blood and tissue.
  > "a validated, high-resolution toolkit for the simultaneous quantification of multiple ageing hallmarks in clinically accessible human samples"
  → _Future:_ Standardize hallmark measurement to overcome methodological heterogeneity and translate into human clinical studies.
- **Peter Fedichev** — [A Minimal Model Explains Aging Regimes and Guides Intervention Strategies](https://www.biorxiv.org/content/10.1101/2025.08.25.671954v1) _(2025)_
  Reduces aging physiology to three variables (resilience, entropic damage, regulatory noise), yielding two regimes: linear damage-driven aging in stable species like humans vs intrinsic instability in mice/flies.
  > "In stable species, including humans, aging is driven by linear damage accumulation that gradually erodes resilience"
  → _Future:_ A three-level intervention roadmap: target dynamic hallmarks, reduce physiological noise, slow/reverse entropic damage.
- **Jacob Kimmel** — [In silico design of epigenetic reprogramming payloads](https://openreview.net/forum?id=kPQ6NKVAiT) _(2025)_
  NewLimit's generative model (protein-foundation-model transfer learning) designs transcription-factor reprogramming payloads from sparse sampling of the combinatorial TF space, in a lab-in-the-loop.
  > "Through diverse epigenetic codes, human cells execute distinct programs from a common genome"
  → _Future:_ Run the model lab-in-the-loop to design reprogramming interventions far faster than pure experiments.
- **George Church** — [Replacement as an aging intervention (Nature Aging Perspective)](https://pubmed.ncbi.nlm.nih.gov/40341243/) _(2025)_
  Argues replacing aged cells/tissues/organs is an underappreciated, near-term-feasible strategy where drug interventions have not yet proven durable in humans.
  > "there is a lack of interventions conclusively shown to attenuate the processes of aging in humans"
  → _Future:_ Develop replacement-based interventions (cell/tissue/organ) alongside reprogramming and gene therapy.
- **Steve Horvath** — [Epigenetic ageing clocks: statistical methods and emerging computational challenges](https://www.nature.com/articles/s41576-024-00807-w) _(2025)_
  Nature Reviews Genetics review (Teschendorff & Horvath) on the statistical foundations of epigenetic clocks and open problems in interpretation, cell-type heterogeneity, and single-cell methods.
  > "many computational and statistical challenges remain that limit our understanding, interpretation and application of epigenetic clocks"
  → _Future:_ Interpretable clocks built at cell-type and single-cell resolution to make epigenetic age causally + clinically meaningful.
- **Matt Kaeberlein** — [Exercise and Weekly Sirolimus (Rapamycin) in Older Adults: RAPA-EX-01 RCT](https://onlinelibrary.wiley.com/doi/10.1002/jcsm.70274) _(2026)_
  RCT (40 adults, 65-85) found once-weekly 6 mg rapamycin did NOT boost — and may have slightly blunted — functional gains from a 13-week exercise program, with more adverse events. A clean, useful negative result.
  > "did not enhance, and in sensitivity analyses, it may have modestly attenuated short-term functional improvements from a home exercise programme"
  → _Future:_ Test alternative rapamycin dosing/timing (e.g. mTORC1 cycling) before combining with exercise in older adults.

**🕸️ Congregational view:** the field as a spatiotemporal knowledge graph (modeled after [getzep/graphiti](https://github.com/getzep/graphiti)) — **[open the field graph →](https://wjlgatech.github.io/longevity-loop/graph.html)**.

**Reflections — what else could be important?** _(synthesis, not claims)_

- Clocks are collapsing into foundation models: Zhavoronkov's Longevity-LLM replacing purpose-built clocks + Kimmel's protein-FM reprogramming design → the field's own 'FM-ops' moment. A unified multimodal aging FM is the obvious open target.
- Aging is resolving from one number to many: Systems Age (11 systems), Wyss-Coray (40+ cell types), Gladyshev (splicing as a new hallmark). The gap: a shared, cell/system-resolved BENCHMARK so these aren't incomparable — a natural longevity-loop contribution.
- Negative results are becoming first-class (Kaeberlein's rapamycin+exercise null). An open registry of honest longevity nulls would be high-trust signal and is exactly the no-evidence⇒No discipline the field needs.
- Correlation ≠ cause is the recurring caveat (Horvath): the frontier wants INTERPRETABLE, causal clocks. A loop turn probing whether an intervention moves a clock in a held-out, pre-registered way is more valuable than a new clock.
- The data wall is inverting in biology (multiomic tokens > internet-text tokens): the scarce input is now well-curated, standardized human hallmark data (de Magalhães' toolkit) — curation, not compute, is the bottleneck to attack.
- Two camps to bridge: 'repair/replace damage' (Church, Fedichev's entropic damage) vs 'reprogram/rejuvenate' (Kimmel, Levine). A model that predicts which regime a given tissue is in could route interventions — an unclaimed synthesis.

---

<h2 id="90-day-roadmap">🗺️ 90-Day Roadmap</h2>

Three tracks every week — full weekly plan in **[docs/ROADMAP.md](docs/ROADMAP.md)**:

- 🧠 Knowledge — ramp on aging biology fast; verify every claim against a primary paper (TRUE = evidenced).
- 🛠️ Tooling — each week ships runnable, gated code (the loop); cheap fine-tunes on Tinker/Modal.
- 🤝 Connections — build in public; reach the hubs + people with an artifact in hand, never empty-handed. In Act II this is the bridge: the credential network (Genentech, Yale/Levine, Georgia Tech) turns computation into bench access, then a raise.

### Phase 1 — Foundation & First Signal · _Days 1–30_
Stand up the loop, ramp on aging biology, ship the first VERIFIABLE result.

**GATE 1 — public repo live · ≥1 leaderboard submission · first grant application in · 5 researcher touches.**

### Phase 2 — Differentiated Result & Momentum · _Days 31–60_
A genuine finding on OPEN data + an adopted open tool + a real collaborator.

**GATE 2 — a reproducible finding write-up · an open tool with ≥1 external user · 1 named collaborator · a micro-grant funded OR strong grant progress.**

### Phase 3 — Credibility & Leverage · _Days 61–90_
Convert signal into a preprint, non-dilutive funding, and a deliberate fork in the road.

**GATE 3 — a preprint OR top-decile leaderboard · non-dilutive funding · a named collaborator · a lab partnership lined up for Act II.**

### Act II — Wet-lab validation & spin-out · _Days 91–180 (Months 4–6)_
Sequenced bridge: convert the computational finding + your credential network (Genentech, Yale/Levine orbit, Georgia Tech) into a lab-validated result, then an incorporated, fundable company. Full-time, raise-ready.

**GATE 4 — a lab-validated (or cleanly null) finding · a co-authored preprint · an incorporated entity + a wet-lab co-founder · age1 acceptance OR a pre-seed raise underway.**

**Signal ladder** (each rung recruits the next):

1. Public repo + honest launch thread
2. First open-leaderboard submission (code-only, credibility-gated)
3. A reproduced aging clock + a shipped open tool
4. A fine-tuned bio-FM finding on open data (research-loop write-up)
5. A named academic/industry collaborator
6. Non-dilutive micro-grant (VitaDAO / Foresight)
7. A preprint or top-decile leaderboard finish
8. A lab partnership (dry+wet): your computation earns bench access + co-authorship
9. A wet-lab-validated (or cleanly null) finding with the partner lab
10. An incorporated company + a wet-lab co-founder from the network
11. age1 acceptance or a pre-seed raise — the sequenced fork taken: build the company

---

<h2 id="execution">✅ Roadmap Execution</h2>

**5/16 done (31%).** Each execution is a checkbox with a before→after eval; a box only ticks with a real result (`done` requires a non-pending before AND after — no evidence ⇒ not done, gated in CI).

- [x] **E1** (P1 · Foundation) — Stand up the AI-native loop (repo + self-audit + gated `make check`)
- [x] **E2** (P1 · Foundation) — Map the field into a verified knowledge base
- [x] **E3** (P1 · Foundation) — Ship the build-in-public surface (README + live dashboard)
- [x] **E4** (P1 · Foundation) — Follow the frontier: radar + live tracker + field graph
- [x] **E5** (P1 · Foundation) — Scaffold the first two loop turns (runnable, honest, PROOF-gated)
- [ ] **E6** (P1 · First Signal) — Run Turn 01 — Systems-Age heterogeneity test on the Biomarkers-of-Aging data
- [ ] **E7** (P1 · First Signal) — First public leaderboard submission (Biolearn / Biomarkers Challenge)
- [ ] **E8** (P2 · Momentum) — Run Turn 02 — fine-tune an open bio-FM vs a frozen probe (age prediction)
- [ ] **E9** (P2 · Momentum) — Ship an open tool a lab actually adopts
- [ ] **E10** (P2 · Momentum) — Secure 1 named academic/industry collaborator
- [ ] **E11** (P3 · Leverage) — Close a non-dilutive micro-grant (VitaDAO / Foresight)
- [ ] **E12** (P3 · Leverage) — Preprint OR top-decile leaderboard finish
- [ ] **E13** (P4 · Wet-lab bridge) — Secure a lab partnership — computation-for-bench (Yale/Levine orbit or Genentech-alum PI)
- [ ] **E14** (P4 · Wet-lab bridge) — First real wet-lab validation (or clean null) of a computational hypothesis, run with the partner lab
- [ ] **E15** (P4 · Spin-out) — Incorporate the entity + recruit a wet-lab co-founder from the network
- [ ] **E16** (P4 · Spin-out) — age1 acceptance OR a pre-seed raise underway (dilutive, full-time)

### Eval reports — before → after

| Execution | Metric | Before | After |
|---|---|---|---|
| ✅ E1 | loop self-audit /100 | n/a (no repo) | 100 (9 principles, gated in CI) |
| ✅ E2 | curated, URL-verified entries | 0 | ~75 (16 researchers, 16 startups, 26 tools, 17 ecosystem) |
| ✅ E3 | public live artifacts | none | public repo + GitHub Pages dashboard + generated README |
| ✅ E4 | frontier signal | 0 tracked | 10 verified recent works + weekly arXiv/GitHub tracker + 60-node bi-temporal graph |
| ✅ E5 | runnable loop turns | 0 | 2 scaffolded (Turn 01 Biolearn/Systems-Age; Turn 02 bio-FM fine-tune) |
| ⬜ E6 | outcome AUROC Δ (best single clock vs +cross-clock heterogeneity), 5 seeds | pending | pending |
| ⬜ E7 | public leaderboard rank / percentile | not entered | pending |
| ⬜ E8 | held-out age MAE, frozen probe vs fine-tuned | pending | pending |
| ⬜ E9 | external users / adopters | 0 | pending |
| ⬜ E10 | named collaborators | 0 | pending |
| ⬜ E11 | non-dilutive funding secured | $0 | pending |
| ⬜ E12 | preprint posted / leaderboard percentile | none | pending |
| ⬜ E13 | lab partnerships with bench access | 0 | pending |
| ⬜ E14 | dry→wet validated (or null) findings | 0 | pending |
| ⬜ E15 | incorporated entity + wet-lab co-founder | none | pending |
| ⬜ E16 | accelerator / pre-seed capital | $0 | pending |

---

<h2 id="people">🧠 Researchers</h2>

🤖 = AI-forward · 💬 = active in the open community (good first contacts).

- **[João Pedro de Magalhães](https://x.com/jpsenescence)** 🤖💬 — University of Birmingham: HAGR aging databases; computational biogerontology
- **[Alex Zhavoronkov](https://x.com/biogerontology)** 🤖💬 — Insilico Medicine: deep-learning aging clocks + generative AI drug discovery
- **[Peter Fedichev](https://x.com/fedichev)** 🤖💬 — Gero: physics/AI dynamical models of aging
- **[Jacob Kimmel](https://x.com/jacobkimmel)** 🤖💬 — NewLimit (fmr Calico): ML-designed reprogramming payloads; bio foundation models
- **[Morgan Levine](https://x.com/DrMorganLevine)** 🤖💬 — Altos Labs (fmr Yale): epigenetic aging clocks (PhenoAge)
- **[Tony Wyss-Coray](https://x.com/wysscoray)** 🤖💬 — Stanford: plasma-proteomic organ aging clocks
- **[Vadim Gladyshev](https://gladyshevlab.bwh.harvard.edu)** 🤖 — Harvard Medical School: mouse + single-cell (scAge) aging clocks
- **[George Church](https://x.com/geochurch)** 🤖💬 — Harvard / Wyss Institute: gene-therapy longevity; synthetic biology
- **[Nir Barzilai](https://x.com/NirBarzilaiMD)** 💬 — Albert Einstein College of Medicine: centenarian genetics; TAME metformin trial
- **[Matt Kaeberlein](https://x.com/mkaeberlein)** 💬 — Optispan (fmr U. Washington): rapamycin geroscience; Dog Aging Project
- **[David Sinclair](https://x.com/davidasinclair)** 💬 — Harvard Medical School: information theory of aging; reprogramming; sirtuins
- **[Eric Verdin](https://x.com/EricVerdin)** 💬 — Buck Institute: geroscience; ketone bodies; immune aging
- **[Andrew Steele](https://x.com/statto)** 💬 — Independent (author of 'Ageless'): longevity science communication
- **[Charles Brenner](https://x.com/CharlesMBrenner)** 💬 — City of Hope: NAD+ metabolism; vocal longevity-hype skeptic (a good reality check)
- **[Joe Betts-LaCroix](https://x.com/bettslacroix)** 💬 — Retro Biosciences: reprogramming + autophagy longevity company
- **[Kristen Fortney](https://bioagelabs.com)** 🤖 — BioAge Labs: ML on longitudinal human data for aging drug discovery

---

<h2 id="startups">🏢 Startups & Labs</h2>

🤖 = AI-native platform.

- **[NewLimit](https://www.newlimit.com)** 🤖 — AI-guided epigenetic reprogramming to restore youthful cell function _(well-funded-private)_
- **[Retro Biosciences](https://www.retro.bio)** 🤖 — reverse cellular aging (reprogramming, autophagy) + AI protein design _(well-funded-private)_
- **[Gero](https://www.gero.ai)** 🤖 — physics-based AI modeling of aging + generative molecule design _(well-funded-private)_
- **[Shift Bioscience](https://shiftbioscience.com)** 🤖 — AI 'virtual cell' for safe single-gene cellular reprogramming _(early)_
- **[BioAge Labs](https://www.bioagelabs.com)** 🤖 — aging-biology multi-omics ML platform (metabolic disease) _(public)_
- **[Insilico Medicine](https://insilico.com)** 🤖 — generative AI drug discovery (PandaOmics, Chemistry42) + clinical pipeline _(public)_
- **[Altos Labs](https://www.altoslabs.com)**  — cellular rejuvenation via partial reprogramming (+ growing computation arm) _(well-funded-private)_
- **[Calico Life Sciences](https://www.calicolabs.com)**  — basic biology of aging → age-related-disease medicines _(well-funded-private)_
- **[Recursion](https://www.recursion.com)** 🤖 — AI drug discovery via cellular imaging (Recursion OS; merged Exscientia) _(public)_
- **[Isomorphic Labs](https://www.isomorphiclabs.com)** 🤖 — AI drug design built on AlphaFold _(well-funded-private)_
- **[Cellarity](https://cellarity.com)** 🤖 — AI on single-cell transcriptomics to design cell-state-correcting medicines _(well-funded-private)_
- **[Xaira Therapeutics](https://xaira.com)** 🤖 — AI-native drug discovery on David Baker's generative protein models _(well-funded-private)_
- **[Rubedo Life Sciences](https://www.rubedolife.com)** 🤖 — AI-driven senolytics discovery (ALEMBIC platform) _(well-funded-private)_
- **[Gordian Biotechnology](https://www.gordian.bio)**  — high-throughput in-vivo pooled screening (Mosaic) for diseases of aging _(early)_
- **[Loyal](https://loyal.com)**  — canine longevity — lifespan-extension drugs for dogs _(well-funded-private)_
- **[Centenara Labs](https://www.centenara.com)**  — hallmarks-of-aging therapeutics portfolio (fmr Rejuveron) _(well-funded-private)_

---

<h2 id="stack">🛠️ The Buildable Stack (open, code-only)</h2>

### Models
- **[Geneformer](https://huggingface.co/ctheodoris/Geneformer)** — Transformer on ~30-104M single-cell transcriptomes; fine-tune for cell-type / perturbation / aging tasks.
- **[scGPT](https://github.com/bowang-lab/scGPT)** — GPT-style single-cell foundation model; fine-tune for annotation, integration, perturbation prediction.
- **[ESM-2](https://github.com/facebookresearch/esm)** — Protein LM (8M-650M) that runs on a laptop; embeddings for variant-effect on longevity genes.
- **[TxGNN](https://github.com/mims-harvard/TxGNN)** — GNN over a drug/disease knowledge graph for zero-shot repurposing; rank candidate longevity interventions.
- **[AltumAge](https://github.com/rsinghlab/AltumAge)** — Deep pan-tissue methylation clock (MLP over ~20k CpGs) to fine-tune/benchmark vs ElasticNet clocks.

### Tools
- **[AlphaFold](https://github.com/google-deepmind/alphafold)** — Structure prediction; usually query the precomputed AlphaFold DB rather than run locally.
- **[scanpy](https://github.com/scverse/scanpy)** — Standard single-cell preprocessing (QC/clustering/DE) before any aging model.
- **[CZ CELLxGENE Census](https://github.com/chanzuckerberg/cellxgene-census)** — API to slice ~33M+ standardized cells by tissue/age/disease in seconds — fastest cohort pull.
- **[pyaging](https://github.com/rsinghlab/pyaging)** — PyTorch package bundling 50+ aging clocks with one API — score biological age on a laptop.
- **[Biolearn](https://bio-learn.github.io/)** — Open standardized platform for the Biomarkers of Aging Challenge — the code-only leaderboard to compete on.

### Clocks
- **[scAge](https://github.com/alex-trapp/scAge)** — Epigenetic age from sparse single-cell methylation — detect cell-level aging + rejuvenation.
- **[DunedinPACE](https://github.com/danbelsky/DunedinPACE)** — Pace-of-aging (rate, not age) from 450k/EPIC — a strong intervention outcome variable.

### Datasets
- **[Tabula Muris Senis](https://registry.opendata.aws/tabula-muris-senis/)** — Mouse aging cell atlas (~500k cells, 18 organs) — the go-to open single-cell aging benchmark.
- **[GTEx Portal](https://gtexportal.org/)** — Human multi-tissue expression with donor age; expression matrices download freely (genotypes gated).
- **[NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/)** — Largest public expression/epigenomics archive; search 'age'-flagged series to build custom aging sets.
- **[Human Cell Atlas](https://data.humancellatlas.org/)** — Open multi-omic reference maps (70M+ cells) for age-stratified tissue baselines.
- **[HAGR (GenAge / CellAge)](https://genomics.senescence.info/)** — Curated aging/senescence gene sets (GenAge 307, CellAge 866) — priors / feature filters.
- **[UK Biobank](https://www.ukbiobank.ac.uk/use-our-data/apply-for-access/)** — 500k multi-omic + health cohort — ACCESS-GATED (application/fee/cloud-only), not laptop-downloadable.

### Benchmarks
- **[Biomarkers of Aging Challenge](https://www.longevityprize.com/prize/biomarker)** — Open competition + curated dataset (methylation/proteomics/outcomes, 500+ people) — the North-Star code-only leaderboard.
- **[Open Problems in Single-Cell](https://github.com/openproblems-bio/openproblems)** — Community benchmarking harness (tasks/datasets/metrics) to fairly evaluate a model vs baselines.
- **[LAB-Bench](https://github.com/Future-House/LAB-Bench)** — 2,457-question benchmark for LLMs on biology research tasks (literature, sequences, DBs).
- **[BixBench](https://github.com/Future-House/BixBench)** — Benchmark for LLM agents on real computational-biology analysis workflows.

---

<h2 id="ecosystem">🤝 Funding & Community</h2>

✅ = realistically open to a solo/independent builder.

- **[Biomarkers of Aging Challenge / Longevity Prize](https://www.longevityprize.com/prize/biomarker)** ✅ _grant_ — Open, code-only competition + curated dataset (Biolearn) — the IDEAL first credibility-gated signal, no wet lab.
- **[VitaDAO / VitaLabs](https://www.vitadao.com/)** ✅ _community_ — DeSci collective; fast fellowship grants (~$65K), light application, active Discord — most accessible funding+community on-ramp.
- **[Foresight Institute — Longevity Grants](https://foresight.org/engage/grants/)** ✅ _grant_ — Monthly-deadline frontier grants (AI-for-science + longevity), unusually open to non-traditional applicants.
- **[Foresight Fellowship](https://foresight.org/engage/fellowship/)** ✅ _fellowship_ — Year-long fellowship; mentorship + intros to funders/senior scientists; global, independent-friendly.
- **[Longevity Biotech Fellowship (LBF)](https://longbiofellowship.org/)** ✅ _fellowship_ — The main 'how do I get into longevity biotech' front door (ODLB merged in); cohort + retreat + community.
- **[age1](https://age1.com/)** ✅ _accelerator_ — Laura Deming's longevity accelerator (~$500K, 4-mo). Dilutive — the premier founder on-ramp; apply with a public track record.
- **[Impetus Longevity Grants (Norn Group)](https://impetusgrants.org/)** 🔒 _grant_ — Fast $10K-$500K aging-science grants (~3-4 wk decisions) — PI/lab-gated; partner into a lab to access.
- **[Hevolution Foundation](https://hevolution.com/grants)** 🔒 _grant_ — Large geroscience funder ($300-500K/yr); institutional/PI-gated — a funder to partner toward.
- **[XPRIZE Healthspan](https://www.xprize.org/prizes/healthspan)** 🔒 _grant_ — $101M team competition (restore function 10-20 yrs). Team/clinical — highest-leverage as a rallying point + network.
- **[NIA (NIH)](https://www.nia.nih.gov/research/grants-funding)** 🔒 _grant_ — Largest US non-dilutive aging funder; SBIR/STTR is the realistic founder path once incorporated.
- **[Astera Institute (Rejuvenome)](https://astera.org/)** 🔒 _grant_ — Runs the open ~$70M combinatorial mouse-lifespan dataset — build on it as open data; grants are relationship-driven.
- **[Vitalist Bay / Vitalism](https://vitalistbay.com/)** ✅ _community_ — Longevity pop-up city — the highest-density in-person gathering of the frontier/independent crowd.
- **[Aging Research & Drug Discovery (ARDD)](https://agingpharma.org/)** ✅ _conference_ — The top translational-geroscience conference (Copenhagen) — where the serious science+investor crowd is.
- **[Longevity Summit Dublin](https://longevitysummitdublin.com/)** ✅ _conference_ — Rejuvenation-biotech heavy (de Grey/O'Dea); researchers + advocates + investors.
- **[Longevity Marketcap (Nathan Cheng)](https://longevitymarketcap.com/)** ✅ _media_ — Most-read industry newsletter; Cheng is a hub node (LBF, Vitalism, Healthspan Capital) — engage to map who's who.
- **[Lifespan.io](https://lifespan.io/)** ✅ _media_ — Advocacy + news non-profit — a place to get build-in-public work amplified to an engaged audience.
- **[Longevity.Technology](https://longevity.technology/)** ✅ _media_ — Daily industry/investment newsletter — track funding rounds + deal-flow signals.

---

<h2 id="build-in-public">📣 Build in public</h2>

This repo IS the artifact: every turn commits data, a result, or a connection. Follow the commits, open an issue with a paper/dataset/collaborator, or PR an entry to `data/*.yml`.

<sub>Generated from <code>data/*.yml</code> by <code>scripts/build.py</code> — do not edit by hand. A sibling of <a href="https://github.com/wjlgatech/FM-os">FM-os</a>.</sub>
