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
| [turn-01-biolearn-baseline](turns/turn-01-biolearn-baseline) | Does a standard epigenetic clock (e.g. PhenoAge) predict the challenge outcome better than chronological age on a held-out split? | VERIFY | 🧩 scaffolded |

---

<h2 id="90-day-roadmap">🗺️ 90-Day Roadmap</h2>

Three tracks every week — full weekly plan in **[docs/ROADMAP.md](docs/ROADMAP.md)**:

- 🧠 Knowledge — ramp on aging biology fast; verify every claim against a primary paper (TRUE = evidenced).
- 🛠️ Tooling — each week ships runnable, gated code (the loop); cheap fine-tunes on Tinker/Modal.
- 🤝 Connections — build in public; reach the hubs + people with an artifact in hand, never empty-handed.

### Phase 1 — Foundation & First Signal · _Days 1–30_
Stand up the loop, ramp on aging biology, ship the first VERIFIABLE result.

**GATE 1 — public repo live · ≥1 leaderboard submission · first grant application in · 5 researcher touches.**

### Phase 2 — Differentiated Result & Momentum · _Days 31–60_
A genuine finding on OPEN data + an adopted open tool + a real collaborator.

**GATE 2 — a reproducible finding write-up · an open tool with ≥1 external user · 1 named collaborator · a micro-grant funded OR strong grant progress.**

### Phase 3 — Credibility & Leverage · _Days 61–90_
Convert signal into a preprint, non-dilutive funding, and a deliberate fork in the road.

**GATE 3 — a preprint OR top-decile leaderboard · non-dilutive funding · a named collaborator · a clear next-90 plan.**

**Signal ladder** (each rung recruits the next):

1. Public repo + honest launch thread
2. First open-leaderboard submission (code-only, credibility-gated)
3. A reproduced aging clock + a shipped open tool
4. A fine-tuned bio-FM finding on open data (research-loop write-up)
5. A named academic/industry collaborator
6. Non-dilutive micro-grant (VitaDAO / Foresight)
7. A preprint or top-decile leaderboard finish
8. A talk/podcast + a company-or-lab decision

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
