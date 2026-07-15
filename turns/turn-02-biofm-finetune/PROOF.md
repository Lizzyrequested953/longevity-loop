# PROOF — Turn 02 (fill after running both arms)

> Status: **scaffolded, not yet run.** No result claimed. Fill with real numbers (including a null)
> to flip this turn to `done` in `data/turns.yml`.

## Hypothesis
Fine-tuning an open bio-FM (Geneformer/scGPT) beats a frozen-embedding linear probe at age prediction.

## Metric
Held-out age MAE (years), 5-fold × 3 seeds, on the SAME split scheme as the frozen probe.

## Result
- Frozen probe MAE: `TBD ± TBD`
- Fine-tuned MAE: `TBD ± TBD`
- **Verdict:** `TBD` — fine-tuning wins / **no improvement (null)** ← overlap = null, report it.
- Modal GPU cost for the fine-tune: `$TBD`

## Threats to validity
- Batch effects across datasets/donors; leakage if normalization saw the test fold.
- Single tissue/dataset; not a search over FMs or hyperparameters.
- Computed on public single-cell data only — **no clinical/therapeutic claim**.

## Reproduce
```bash
cd turns/turn-02-biofm-finetune
pip install -r requirements.txt
python finetune.py                 # frozen-probe baseline
modal run finetune.py::train       # fine-tune arm (GPU)
```

## Compounded into Turn 03
`TBD` — the pipeline + comparable metric that seeds the next, harder question.
