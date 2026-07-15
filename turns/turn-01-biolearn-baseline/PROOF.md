# PROOF — Turn 01 (fill after running `baseline.py`)

> Status: **scaffolded, not yet run.** No result is claimed. Filling this file (with real numbers,
> including a null if that's the outcome) is what flips the turn to `done` in `data/turns.yml`.

## Hypothesis
PhenoAge age-acceleration predicts the challenge outcome better than chronological age.

## Metric
Outcome AUROC on a held-out 30% split, mean ± std over 5 seeds; Δ = PhenoAge − chronological.

## Result
- PhenoAge accel AUROC: `TBD ± TBD`
- Chronological AUROC: `TBD ± TBD`
- **Δ (mean ± std):** `TBD`
- **Verdict:** `TBD` — improves / **no improvement (null)** ← report honestly, overlap = null.

## Threats to validity
- Single dataset / split scheme; leakage if any preprocessing saw the test split.
- Computed on public data only — **no wet-lab / clinical claim** is made.
- Clock choice (PhenoAge) is one of many; not a search over clocks.

## Reproduce
```bash
cd turns/turn-01-biolearn-baseline
pip install -r requirements.txt
python baseline.py    # writes results.json
```

## Compounded into Turn 02
`TBD` — what this turn taught (a feature, a data quirk, a contact) that seeds the next question.
