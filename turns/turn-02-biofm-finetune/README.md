# Turn 02 — Fine-tune an open bio-FM on an aging task

*One turn of the [loop](../../README.md#the-loop). **Scaffold** — run it, then fill
[`PROOF.md`](PROOF.md). No result claimed until PROOF is filled. Seeds from Turn 01.*

## ① QUESTION (falsifiable)
Does **fine-tuning** an open single-cell foundation model (Geneformer or scGPT) on an aging
dataset beat a **frozen-embedding linear probe** at predicting cell/donor age?
- **Metric:** held-out age MAE (or age-group AUROC), fine-tuned vs frozen-probe, mean ± std over 3 seeds.
- **Null I accept:** CIs overlap ⇒ "fine-tuning doesn't beat a linear probe here" — reportable, and a genuinely useful negative result for the field.

## ② DATA (open)
Age-labeled single-cell data via **[CZ CELLxGENE Census](https://github.com/chanzuckerberg/cellxgene-census)**
or **[Tabula Muris Senis](https://registry.opendata.aws/tabula-muris-senis/)**. Public only.

## ③ MODEL — where the compute goes
- **Frozen baseline:** extract Geneformer/scGPT embeddings → linear/logistic probe (laptop-fine).
- **Fine-tune:** LoRA/full fine-tune on a cheap GPU via **[Modal](https://modal.com)** (serverless GPU;
  bio-FMs are HF/PyTorch, not LLM-LoRA, so Tinker doesn't apply here — Tinker is for the LLM turns).

## ④ VERIFY
Held-out split, fixed seeds; compare against the frozen probe AND Turn 01's clock baseline. Report on the same held-out scheme so turns are comparable.

## ⑤ WRITE-UP → fill [`PROOF.md`](PROOF.md)
Result + the null, threats (batch effects, leakage, single dataset), reproduce command + the Modal run cost.

## ⑥ SHARE
Commit the turn + a short thread; if it's a clean result (or a clean null), that's a shippable open finding — route to a collaborator from `data/people.yml`.

## ⑦ COMPOUND
A working fine-tune pipeline + a comparable metric seeds Turn 03 (a real hypothesis on a target/intervention, or a leaderboard climb).

## Run it
```bash
cd turns/turn-02-biofm-finetune
pip install -r requirements.txt
python finetune.py           # frozen-probe baseline (laptop); prints metric + writes results.json
# for the fine-tune arm on a GPU:  modal run finetune.py::train   (see TODO hooks)
```
