"""Reproduce actual tree membership and MSA architecture inspection without invented sites."""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    trees = json.loads((HERE / "trees-compact.json").read_text())
    result = {}
    for f, tree in trees.items():
        msa = json.loads((HERE / (f + "-msa.json")).read_text())["search"]["MSA_list"][
            "sequence_info"
        ]
        seqs = {x["persistent_id"]: x["sequence"] for x in msa}
        leaves = []
        for p, member in sorted(tree["leaves"].items()):
            assert p in seqs, (f, p)
            seq = seqs[p]
            leaves.append(
                {
                    "ptn": p,
                    **member,
                    "alignment_columns": len(seq),
                    "ungapped_length": sum(c.isalpha() for c in seq),
                    "occupied_columns": [
                        i + 1 for i, c in enumerate(seq) if c.isalpha()
                    ],
                }
            )
        result[f] = {
            "tree_leaves": len(leaves),
            "msa_sequences_including_ancestors": len(msa),
            "members": leaves,
        }
    met_h = result["PTHR45833"]["members"]
    canonical = next(x for x in met_h if x["uniprot"] == "P13009")
    alternate = next(x for x in met_h if x["uniprot"] == "Q748M7")
    assert canonical["ungapped_length"] == 1227
    assert alternate["ungapped_length"] == 605
    assert (
        len(set(canonical["occupied_columns"]) - set(alternate["occupied_columns"]))
        > 600
    )
    met_e = result["PTHR30519"]["members"]
    assert not any(x["uniprot"] in ["Q6F6Z8", "Q88JF1", "Q88E31"] for x in met_e)
    evidence = {
        "MetH_alignment_control": {
            "positive_accession": "P13009",
            "alternate_accession": "Q748M7",
            "canonical_residue_columns_not_occupied_by_alternate": len(
                set(canonical["occupied_columns"]) - set(alternate["occupied_columns"])
            ),
            "interpretation": "Different domain coverage agrees with official PF02219/PF02574 fusion architecture, but is not a target-negative assay or a residue discriminator.",
        },
        "MetE_target_tree_limit": "Exact MesD and isolated-domain targets are classified to the family by UniProt but absent from its downloaded tree/MSA. No PTN placement or aligned residue claim is invented for them.",
        "families": result,
    }
    (HERE / "phylogeny-and-msa.json").write_text(json.dumps(evidence, indent=2) + "\n")
    print(
        {
            f: (v["tree_leaves"], v["msa_sequences_including_ancestors"])
            for f, v in result.items()
        }
    )


if __name__ == "__main__":
    main()
