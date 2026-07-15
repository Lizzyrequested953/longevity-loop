#!/usr/bin/env python3
"""Turn 02 — does fine-tuning an open bio-FM beat a frozen-embedding linear probe
at predicting age?

SCAFFOLD: the frozen-probe baseline + the metric are real and runnable once you
wire an age-labeled single-cell matrix (`# TODO(you)`); the fine-tune arm is a
Modal stub. It refuses to fabricate data or scores. Fill PROOF.md from the output
(report the null if fine-tuning doesn't beat the probe).

Baseline (laptop): bio-FM embeddings -> linear probe.
Fine-tune (GPU):  LoRA/full fine-tune via Modal.
"""
from __future__ import annotations

import json
import pathlib

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import KFold

OUT = pathlib.Path(__file__).parent / "results.json"
SEEDS = [0, 1, 2]


def load_aging_cells():
    """Return (X_expr: np.ndarray[n_cells, n_genes], age: np.ndarray[n_cells]).

    TODO(you): pull an age-labeled slice via CELLxGENE Census, e.g.
        import cellxgene_census
        with cellxgene_census.open_soma() as c:
            adata = cellxgene_census.get_anndata(
                c, "Homo sapiens",
                obs_value_filter="tissue_general=='blood' and development_stage_ontology_term_id!=''")
        return adata.X.toarray(), adata.obs["age"].astype(float).values
    We do NOT fabricate cells.
    """
    raise NotImplementedError("Wire an age-labeled single-cell matrix (see docstring).")


def embed_frozen(X):
    """Frozen bio-FM embeddings (Geneformer/scGPT), no gradient.

    TODO(you): tokenize + encode with a pretrained checkpoint, e.g. Geneformer's
    EmbExtractor or scGPT's embed API; return [n_cells, d]. As a cheap stand-in you
    may start with log1p + PCA to get the pipeline green, then swap in the real FM.
    """
    raise NotImplementedError("Return frozen bio-FM embeddings (see docstring).")


def frozen_probe_mae(emb, age) -> np.ndarray:
    """5-fold Ridge probe on frozen embeddings -> MAE per seed."""
    maes = []
    for seed in SEEDS:
        kf = KFold(n_splits=5, shuffle=True, random_state=seed)
        fold = [mean_absolute_error(age[te], Ridge().fit(emb[tr], age[tr]).predict(emb[te]))
                for tr, te in kf.split(emb)]
        maes.append(float(np.mean(fold)))
    return np.array(maes)


# --- fine-tune arm (Modal GPU) — stub; implement when the baseline is green ---
# import modal
# app = modal.App("longevity-turn02")
# @app.function(gpu="A10G", timeout=3600)
# def train(...):  # LoRA/full fine-tune of the bio-FM head for age regression
#     ...           # return held-out MAE per seed on the SAME folds as the probe


def main() -> int:
    X, age = load_aging_cells()
    emb = embed_frozen(X)
    probe = frozen_probe_mae(emb, age)
    result = {
        "metric": "age MAE (years), 5-fold x 3 seeds",
        "frozen_probe": {"mean": float(probe.mean()), "std": float(probe.std())},
        "finetuned": "TODO: run `modal run finetune.py::train`, then paste MAE here",
        "verdict": "fill after both arms run (overlap ⇒ null: fine-tuning didn't beat the probe)",
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
