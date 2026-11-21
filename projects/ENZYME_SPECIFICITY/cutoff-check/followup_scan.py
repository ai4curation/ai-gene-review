"""Follow-up on the UNDECIDED rows the cutoff check placed below their family's cutoff.

The evaluation scores a row against the NCBIfam models that carry its EC or GO term.
A BTC there can mean only "not this family", so for each flagged row this script also
scores the protein against the sister model that matters and scans the whole KT2440
proteome with each model, to see whether another KT2440 protein is the dedicated
enzyme. Nothing is hand-entered: scores come from pyhmmer, the proteome from UniProt.

    uv run python projects/ENZYME_SPECIFICITY/cutoff-check/followup_scan.py

Writes followup.yaml next to this script.
"""

from __future__ import annotations

import urllib.request
from pathlib import Path

import pyhmmer
import yaml

from ai_gene_review.validation.enzyme_family_cutoff import NCBIfam

HERE = Path(__file__).parent
CACHE = Path(".cache")
PROTEOME = "UP000000556"  # Pseudomonas putida KT2440 reference proteome

# Each case names the flagged protein, the models to score, and the controls whose own
# family each model should pass. Models are chosen by name and role, not by EC/GO.
CASES = [
    {
        "gene": "ptxD",
        "protein": "Q88HI1",
        "question": "GhrA was the only target model; is ptxD inside the GhrB family it resembles?",
        "models": ["NF011938.0", "NF012013.0"],
        "controls": {"P37666": "E. coli GhrB", "P75913": "E. coli GhrA"},
    },
    {
        "gene": "PP_4638",
        "protein": "Q88E30",
        "question": "Does another KT2440 protein pass the canonical MetF models?",
        "models": ["TIGR00676.1", "TIGR00677.1", "NF006950.0"],
        "controls": {},
    },
]


def fetch(url: str, path: Path) -> Path:
    """Download once into the cache."""
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review"})
        with urllib.request.urlopen(req, timeout=300) as fh:
            path.write_bytes(fh.read())
    return path


def accession(name: str | bytes) -> str:
    """UniProt accession from a FASTA id such as tr|Q88HI1|Q88HI1_PSEPK."""
    text = name if isinstance(name, str) else name.decode()
    return text.split("|")[1] if "|" in text else text


def search(
    hmm: pyhmmer.plan7.HMM, block: pyhmmer.easel.DigitalSequenceBlock
) -> dict[str, float]:
    """Bit score of every sequence with a positive score, filters off as in the check."""
    hits = next(
        pyhmmer.hmmsearch(
            [hmm],
            block,
            E=1e6,
            domE=1e6,
            Z=len(block),
            bias_filter=False,
            F1=1.0,
            F2=1.0,
            F3=1.0,
        )
    )
    return {accession(h.name): round(h.score, 1) for h in hits if h.score > 0}


def main() -> None:
    """Score each case's protein, controls and the KT2440 proteome against its models."""
    db = NCBIfam(CACHE / "ncbifam")
    alphabet = pyhmmer.easel.Alphabet.amino()
    proteome_path = fetch(
        f"https://rest.uniprot.org/uniprotkb/stream?query=proteome:{PROTEOME}&format=fasta",
        CACHE / "proteomes" / f"{PROTEOME}.fasta",
    )
    with pyhmmer.easel.SequenceFile(
        proteome_path, digital=True, alphabet=alphabet
    ) as fh:
        proteome = fh.read_block()
    families = {f.accession: f for f in db.families}

    results = {"ncbifam_release": db.release(), "proteome": PROTEOME, "cases": []}
    for case in CASES:
        control_block = pyhmmer.easel.DigitalSequenceBlock(alphabet)
        for acc in case["controls"]:
            fasta = fetch(
                f"https://rest.uniprot.org/uniprotkb/{acc}.fasta",
                CACHE / "proteomes" / f"{acc}.fasta",
            )
            with pyhmmer.easel.SequenceFile(
                fasta, digital=True, alphabet=alphabet
            ) as fh:
                control_block.extend(fh.read_block())
        models = []
        for model in case["models"]:
            with pyhmmer.plan7.HMMFile(db.hmm_path(families[model])) as fh:
                hmm = fh.read()
            tc = round(hmm.cutoffs.trusted[0], 1)
            in_proteome = search(hmm, proteome)
            control_scores = search(hmm, control_block)
            ranked = sorted(in_proteome.items(), key=lambda kv: -kv[1])
            models.append(
                {
                    "model": f"{model} {families[model].product_name}",
                    "trusted_cutoff": tc,
                    "flagged_protein_score": in_proteome.get(case["protein"]),
                    "kt2440_above_tc": [a for a, s in ranked if s >= tc],
                    "kt2440_top_hits": [
                        {"accession": a, "score": s} for a, s in ranked[:3]
                    ],
                    "controls": {
                        f"{acc} {label}": control_scores.get(acc)
                        for acc, label in case["controls"].items()
                    },
                }
            )
        results["cases"].append(
            {k: case[k] for k in ("gene", "protein", "question")} | {"models": models}
        )

    (HERE / "followup.yaml").write_text(
        yaml.safe_dump(results, sort_keys=False, width=120)
    )
    print(yaml.safe_dump(results, sort_keys=False, width=120))


if __name__ == "__main__":
    main()
