"""Register PMID:23433073 in the references list.

It is cited five times in the GO:0005096 row's supported_by but was not in
`references` - the repo validator does not require it, which is precisely why it needs a
guard: an unregistered reference has no `reference_review`, so the one paper that
reverses this review's headline verdict would carry no recorded judgement of its
citation quality.

The title is copied from publications/PMID_23433073.md frontmatter, never written from
memory.

Usage: uv run python patch_add_ref_23433073.py
"""

from __future__ import annotations

import pathlib

import yaml

HERE = pathlib.Path(__file__).parent
REVIEW = HERE.parent / "AGFG1-ai-review.yaml"
# Anchor on the directory holding BOTH genes/ and publications/. A walk that looks for
# `publications/` alone stops at genes/human/publications, which exists on main as a
# stray stub directory - a documented trap in this repo.
REPO = HERE
while REPO != REPO.parent and not (
    (REPO / "publications").is_dir() and (REPO / "genes").is_dir()
):
    REPO = REPO.parent
assert (REPO / "publications").is_dir() and (REPO / "genes").is_dir(), REPO
CACHE = REPO / "publications" / "PMID_23433073.md"
assert CACHE.exists(), CACHE

ANCHOR = """- id: PMID:25416956
  title: A proteome-scale map of the human interactome network."""

BLOCK = """- id: PMID:23433073
  title: Ancient complexity, opisthokont plasticity, and discovery of the 11th subfamily
    of Arf GAP proteins.
  reference_review:
    relevance: HIGH
    correctness: VERIFIED
    review_notes: >-
      The paper that reverses this review's verdict on GO:0005096, and it was nearly
      missed: it was fetched, judged to be a family-classification paper with nothing
      resting on it, deleted before the first commit, and came back only through the
      concurrent AGFG2 review. Full text available and read. It names three
      catalytically required ASAP3 positions with the statement that mutating any one
      severely impairs activity, reports that only 2 of 40 AGFG sequences retain the
      aspartate and that the AGFG consensus uniquely lacks the tryptophan, and concludes
      that the AGFG subfamily is predicted to have lost substantial GAP activity while
      explicitly warning that this must not be confused with loss of Arf binding. Every
      claim used from it was re-measured here on AGFG1's own sequence with GAP-competent
      positive controls, rather than transferred from the paper's consensus analysis or
      from the sibling review.
"""


def main() -> None:
    text = REVIEW.read_text()
    if "- id: PMID:23433073" in text:
        print("already registered; nothing to do")
        return

    # Title must match the cached frontmatter, not memory.
    fm = CACHE.read_text().split("---")[1]
    cached_title = " ".join(yaml.safe_load(fm)["title"].split())
    block_title = " ".join(yaml.safe_load(BLOCK)[0]["title"].split())
    assert block_title == cached_title, (
        f"title mismatch:\n  block:  {block_title}\n  cached: {cached_title}"
    )

    assert text.count(ANCHOR) == 1, f"anchor found {text.count(ANCHOR)} times"
    out = text.replace(ANCHOR, BLOCK.rstrip("\n") + "\n" + ANCHOR, 1)

    doc = yaml.safe_load(out)
    ids = [r["id"] for r in doc["references"]]
    assert ids.count("PMID:23433073") == 1, ids
    # Every PMID cited in a supported_by must now be registered.
    cited = set()

    def walk(n):
        if isinstance(n, dict):
            for k, v in n.items():
                if k in ("supported_by", "provenance") and isinstance(v, list):
                    for e in v:
                        if isinstance(e, dict) and str(e.get("reference_id", "")).startswith("PMID:"):
                            cited.add(e["reference_id"])
                else:
                    walk(v)
        elif isinstance(n, list):
            for e in n:
                walk(e)

    walk(doc)
    missing = sorted(cited - set(ids))
    assert not missing, f"cited but unregistered: {missing}"
    REVIEW.write_text(out)
    print(f"registered PMID:23433073; {len(ids)} references, 0 cited-but-unregistered")


if __name__ == "__main__":
    main()
