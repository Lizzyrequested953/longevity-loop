#!/usr/bin/env python3
"""Turn 01 — Biolearn baseline: does PhenoAge age-acceleration beat chronological
age at predicting the challenge outcome?

SCAFFOLD: the structure + metric are real; the two spots that need the actual
challenge dataset are marked `# TODO(you)`. It is honest by construction — it
computes a real Δ across seeds and refuses to invent numbers. Fill PROOF.md from
its printed output (report the null if the CIs overlap).

Docs: https://bio-learn.github.io/  ·  clocks via biolearn or pyaging.
"""
from __future__ import annotations

import json
import pathlib

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

OUT = pathlib.Path(__file__).parent / "results.json"
SEEDS = [0, 1, 2, 3, 4]


def load_challenge():
    """Return (meth_df, chrono_age: np.ndarray, outcome: np.ndarray[0/1]).

    TODO(you): wire the real Biomarkers-of-Aging Challenge data via Biolearn, e.g.

        from biolearn.data_library import DataLibrary
        data = DataLibrary().get("<challenge_dataset_id>").load()
        meth, meta = data.dnam, data.metadata
        return meth, meta["age"].values, (meta["outcome"] == 1).astype(int).values

    Until then this raises — we do NOT fabricate data.
    """
    raise NotImplementedError("Wire the Biolearn challenge dataset here (see docstring).")


def phenoage_acceleration(meth_df, chrono_age) -> np.ndarray:
    """PhenoAge age-acceleration = PhenoAge - chronological age.

    TODO(you): compute PhenoAge with Biolearn or pyaging, e.g.
        from biolearn.model_gallery import ModelGallery
        pheno = ModelGallery().get("PhenoAge").predict(meth_df)["predicted"].values
        return pheno - chrono_age
    """
    raise NotImplementedError("Compute PhenoAge via Biolearn/pyaging (see docstring).")


def _auc(x1d: np.ndarray, y: np.ndarray, seed: int) -> float:
    xtr, xte, ytr, yte = train_test_split(x1d.reshape(-1, 1), y, test_size=0.3,
                                          random_state=seed, stratify=y)
    clf = LogisticRegression(max_iter=1000).fit(xtr, ytr)
    return roc_auc_score(yte, clf.predict_proba(xte)[:, 1])


def main() -> int:
    meth, chrono, outcome = load_challenge()
    accel = phenoage_acceleration(meth, chrono)
    pheno_auc = np.array([_auc(accel, outcome, s) for s in SEEDS])
    chrono_auc = np.array([_auc(chrono, outcome, s) for s in SEEDS])
    delta = pheno_auc - chrono_auc
    result = {
        "metric": "outcome AUROC (5 seeds)",
        "phenoage_accel": {"mean": float(pheno_auc.mean()), "std": float(pheno_auc.std())},
        "chronological": {"mean": float(chrono_auc.mean()), "std": float(chrono_auc.std())},
        "delta_mean": float(delta.mean()), "delta_std": float(delta.std()),
        "verdict": "improves" if delta.mean() - delta.std() > 0 else "no improvement (null)",
    }
    OUT.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
    print("\nNow fill PROOF.md — report the verdict honestly, including a null.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
