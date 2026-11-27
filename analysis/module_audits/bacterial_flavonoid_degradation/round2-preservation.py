"""Check round-2 annotations, withdrawals and source bytes against published head."""

from pathlib import Path
from collections import Counter
import hashlib
import json
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[3]
AUDIT = Path(__file__).resolve().parent
HEAD = "ed4fa345048677c168a8fe4beb8a6b9c53c7edf6"


def git_bytes(path):
    return subprocess.check_output(["git", "show", f"{HEAD}:{path}"], cwd=ROOT)


def payloads(d):
    return [
        {k: v for k, v in row.items() if k != "review"}
        for row in d["existing_annotations"]
    ]


def counts(reviews):
    rows = [a for d in reviews for a in d["existing_annotations"]]
    return dict(
        rows=len(rows),
        actions=dict(sorted(Counter(a["review"]["action"] for a in rows).items())),
        active_NEW=sum(
            a["review"]["action"] == "NEW" and not a.get("retired") for a in rows
        ),
        retired=sum(bool(a.get("retired")) for a in rows),
    )


def main():
    prior = json.loads((AUDIT / "round1-preservation.json").read_text())
    paths = sorted(prior["current_review_sha256"])
    protected = set(prior["protected_sha256"])
    old_reviews = []
    new_reviews = []
    reviews = {}
    changes = []
    tracked = set(
        subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", HEAD], cwd=ROOT, text=True
        ).splitlines()
    )
    for path in paths:
        old = yaml.safe_load(git_bytes(path))
        new = yaml.safe_load((ROOT / path).read_text())
        assert payloads(old) == payloads(new), path
        old_reviews.append(old)
        new_reviews.append(new)
        for i, (a, b) in enumerate(
            zip(old["existing_annotations"], new["existing_annotations"])
        ):
            if a["review"]["action"] != b["review"]["action"]:
                assert (
                    a.get("retired")
                    and b.get("retired")
                    and a["term"]["id"] == "GO:0046275"
                )
                assert (a["review"]["action"], b["review"]["action"]) == (
                    "MARK_AS_OVER_ANNOTATED",
                    "REMOVE",
                )
                changes.append(
                    dict(
                        path=path,
                        row_index=i,
                        term=b["term"]["id"],
                        action="REMOVE",
                        retired=True,
                    )
                )
        folder = str(Path(path).parent) + "/"
        protected.update(
            p
            for p in tracked
            if p.startswith(folder)
            and any(
                x in p
                for x in [
                    "-uniprot.",
                    "-goa.",
                    "-deep-research",
                    "-citations.",
                    "-hypotheses/",
                ]
            )
        )
        for ref in old.get("references", []):
            if ref["id"].startswith("PMID:"):
                p = "publications/" + ref["id"].replace(":", "_") + ".md"
                if p in tracked:
                    protected.add(p)
        reviews[path] = dict(
            rows=len(payloads(new)),
            ordered_payloads_unchanged=True,
            sha256=hashlib.sha256((ROOT / path).read_bytes()).hexdigest(),
        )
    assert len(changes) == 9
    assert counts(old_reviews)["active_NEW"] == counts(new_reviews)["active_NEW"] == 7
    assert counts(old_reviews)["retired"] == counts(new_reviews)["retired"] == 9
    source_hashes = {}
    for p in sorted(protected):
        data = (ROOT / p).read_bytes()
        assert data == git_bytes(p), p
        source_hashes[p] = hashlib.sha256(data).hexdigest()
    unchanged = [
        "modules/bacterial_flavonoid_degradation.yaml",
        "modules/bacterial_flavonoid_degradation-source-analysis/check_module.py",
    ]
    for p in unchanged:
        assert (ROOT / p).read_bytes() == git_bytes(p), p
    new_sources = [
        "publications/PMID_16321959.md",
        "publications/PMID_17275835.md",
        "analysis/module_audits/bacterial_flavonoid_degradation/round2-evidence/Q89GB7.json",
        "analysis/module_audits/bacterial_flavonoid_degradation/round2-evidence/P04335.json",
    ]
    result = dict(
        status="PASS",
        reviewed_head=HEAD,
        panel_reviews=len(paths),
        before=counts(old_reviews),
        after=counts(new_reviews),
        rows_added=0,
        rows_deleted=0,
        original_payloads_and_order_preserved=True,
        newly_retired_rows=0,
        withdrawal_action_changes=changes,
        broad_hydrolase_core_members=[
            "HERSS/Hsero_1004",
            "PSEPK/PP_3195",
            "BRADU/bll6428",
        ],
        specific_reaction_terms_relocated_to_questions=2,
        module_and_checker_unchanged=True,
        protected_source_count=len(source_hashes),
        protected_sha256=source_hashes,
        current_reviews=reviews,
        newly_fetched_sources_sha256={
            p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in new_sources
        },
    )
    (AUDIT / "round2-preservation.yaml").write_text(
        yaml.safe_dump(result, sort_keys=False)
    )
    print(
        {
            k: v
            for k, v in result.items()
            if k
            not in [
                "protected_sha256",
                "current_reviews",
                "withdrawal_action_changes",
                "newly_fetched_sources_sha256",
            ]
        }
    )


if __name__ == "__main__":
    main()
