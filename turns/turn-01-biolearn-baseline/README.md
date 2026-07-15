# Turn 01 — Biolearn baseline on the Biomarkers of Aging Challenge

*One turn of the [loop](../../README.md#the-loop). This is a **scaffold** — run it, then fill
[`PROOF.md`](PROOF.md). No result is claimed until PROOF is filled (no evidence ⇒ no claim).*

## ① QUESTION (falsifiable)
Does a standard epigenetic clock (**PhenoAge**) predict the challenge's aging/health outcome
**better than chronological age** on a held-out split?
- **Metric:** Δ = (outcome-prediction score using PhenoAge age-acceleration) − (score using chronological age), on a fixed held-out split, mean ± std over 5 seeds.
- **Null I accept:** confidence intervals overlap ⇒ "no improvement over chronological age" — a valid, reportable result.

## ② DATA (open)
The [Biomarkers of Aging Challenge](https://www.longevityprize.com/prize/biomarker) dataset via the
open **[Biolearn](https://bio-learn.github.io/)** library. *Only public data; nothing wet-lab.*

## ③ MODEL
Compute PhenoAge (and chronological-age baseline) with Biolearn / `pyaging`; fit a simple predictor of the outcome from each; compare.

## ④ VERIFY
Score on the held-out split (and submit to the public leaderboard if open). The leaderboard rank is the external verifier.

## ⑤ WRITE-UP → fill [`PROOF.md`](PROOF.md)
Result **and** the null, threats-to-validity, and the exact reproduce command.

## ⑥ SHARE
Commit this turn + a short honest thread. Route to VitaDAO / Longevity Marketcap with the artifact in hand.

## ⑦ COMPOUND
Whatever you learn (a better feature, a data quirk, a contact) seeds Turn 02 (a bio-FM fine-tune).

## Run it
```bash
cd turns/turn-01-biolearn-baseline
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python baseline.py            # prints the Δ metric across seeds; writes results.json
# then fill PROOF.md with the real numbers (including a null if that's what you got)
```
