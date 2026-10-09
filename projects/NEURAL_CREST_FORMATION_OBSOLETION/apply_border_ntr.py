"""Re-point border-specifier reviews from GO:0014029 to the proposed
'neural plate border formation' term (NTR), as part of the
NEURAL_CREST_FORMATION_OBSOLETION proposal.

For each listed review:
  * NEW rows on GO:0014029 are re-pointed to {id: NTR, label: neural plate border formation};
  * ACCEPT rows on GO:0014029 (GOA-sourced) become MODIFY with the NTR (plus any
    extra replacement given) as proposed_replacement_terms;
  * a core function that lists GO:0014029 drops it (core-function ids must be
    real GO terms) and states the border role in its description;
  * a proposed_new_terms entry is added, supported by that core function's quotes.

Edits are textual so the rest of each file keeps its formatting. Run from the
repo root; validate afterwards with `just validate <org> <gene>`.
"""
import json
import re
import sys
import pathlib
import yaml

NTR_LABEL = "neural plate border formation"
DEFINITION = (
    "The formation of the neural plate border, the region of ectoderm at the boundary "
    "between the neural plate and the non-neural ectoderm that is competent to give rise to "
    "neural crest, preplacodal ectoderm, dorsal neural tube and epidermis."
)
JUSTIFICATION = (
    "GO has no term for the neural plate border. GO:0014029 neural crest formation is "
    "defined as forming this ectodermal region but is placed under epithelial to mesenchymal "
    "transition, so border specifiers end up annotated to an EMT term. The border is conserved "
    "in chordates without neural crest (amphioxus, tunicates), so it cannot be a part of "
    "neural crest formation. See projects/NEURAL_CREST_FORMATION_OBSOLETION.md."
)
REASON_SUFFIX = (
    " GO:0014029 is proposed for obsoletion (projects/NEURAL_CREST_FORMATION_OBSOLETION.md): "
    "its definition describes forming the neural plate border region while its placement is under "
    "epithelial to mesenchymal transition. This gene's role is border formation, captured by the "
    "proposed term 'neural plate border formation' (NTR)."
)

GENES = {
    # path: extra replacement ids for MODIFY rows
    "genes/XENLA/gbx2/gbx2-ai-review.yaml": [],
    "genes/human/MSX1/MSX1-ai-review.yaml": [],
    "genes/human/PAX7/PAX7-ai-review.yaml": [],
    "genes/human/TFAP2A/TFAP2A-ai-review.yaml": [],
    "genes/human/TFAP2C/TFAP2C-ai-review.yaml": [],
    "genes/XENLA/pax3-a/pax3-a-ai-review.yaml": [("GO:0014034", "neural crest cell fate commitment")],
    "genes/XENLA/zic1/zic1-ai-review.yaml": [("GO:0014034", "neural crest cell fate commitment")],
}


def quotes_for(doc):
    for cf in doc.get("core_functions") or []:
        if any(t.get("id") == "GO:0014029" for t in cf.get("directly_involved_in") or []):
            return [s for s in cf.get("supported_by") or [] if str(s.get("reference_id", "")).startswith("PMID:")][:2]
    return []


def main(root):
    root = pathlib.Path(root)
    only = set(sys.argv[2:])
    for rel, extra in GENES.items():
        if only and not any(o in rel for o in only):
            continue
        path = root / rel
        text = path.read_text()
        doc = yaml.safe_load(text)
        quotes = quotes_for(doc)

        # 1. NEW rows: re-point the term
        text, n_new = re.subn(
            r"(- term:\n(\s+)id: )GO:0014029\n(\s+)label: neural crest formation\n((?:(?!\n- term:)[\s\S])*?action: NEW)",
            lambda m: f"{m.group(1)}NTR\n{m.group(3)}label: {NTR_LABEL}\n{m.group(4)}",
            text,
        )

        # 2. ACCEPT rows on GO:0014029 -> MODIFY with NTR replacement
        def to_modify(m):
            block = m.group(0)
            if "action: ACCEPT" not in block:
                return block
            ind = re.search(r"\n(\s+)action: ACCEPT", block).group(1)
            repl = f"{ind}proposed_replacement_terms:\n{ind}- id: NTR\n{ind}  label: {NTR_LABEL}\n"
            for i, l in extra:
                repl += f"{ind}- id: {i}\n{ind}  label: {l}\n"
            block = block.replace(f"{ind}action: ACCEPT", f"{ind}action: MODIFY", 1)
            # rewrite the reason as a quoted scalar (parsed value + suffix), robust to any style
            rm = re.search(rf"\n{ind}reason: .*?(?=\n{ind}[a-z_]+:)", block, re.S)
            if rm:
                parsed = yaml.safe_load("reason: " + block[rm.start() + 1 + len(ind) + len("reason: "):rm.end()].replace("\n" + ind + "  ", "\n  ")) or {}
                reason = (parsed.get("reason") or "").strip()
                new = f"\n{ind}reason: " + json.dumps(reason + REASON_SUFFIX, ensure_ascii=False)
                block = block[: rm.start()] + new + block[rm.end():]
            # insert replacement terms right after the reason block
            rm2 = re.search(rf"\n{ind}reason: .*?(?=\n{ind}[a-z_]+:)", block, re.S)
            pos = rm2.end() + 1
            block = block[:pos] + repl + block[pos:]
            return block

        text, n_acc = re.subn(
            r"- term:\n\s+id: GO:0014029\n[\s\S]*?(?=\n- term:|\n[a-z_]+:)", to_modify, text
        )

        # 3. core function: drop GO:0014029 from directly_involved_in
        cf_pat = re.compile(r"(\n(\s*)directly_involved_in:\n)(\2- id: GO:0014029\n\2  label: neural crest formation\n)")
        m = cf_pat.search(text)
        if m:
            ind = m.group(2)
            rest = text[m.end():]
            # if no other list item follows, drop the key as well
            if not re.match(rf"{ind}- id: ", rest):
                text = text[: m.start()] + "\n" + text[m.end():]
            else:
                text = text[: m.end(1)] + text[m.end():]

        # 4. proposed_new_terms entry
        entry = {
            "proposed_name": NTR_LABEL,
            "proposed_definition": DEFINITION,
            "justification": JUSTIFICATION,
            "proposed_parent": {"id": "GO:0007398", "label": "ectoderm development"},
            "supported_by": [{"reference_id": q["reference_id"], "supporting_text": q["supporting_text"]} for q in quotes],
        }
        dumped = yaml.safe_dump([entry], sort_keys=False, width=100, allow_unicode=True)
        if re.search(r"^proposed_new_terms: \[\]\s*$", text, re.M):
            text = re.sub(r"^proposed_new_terms: \[\]\s*$", "proposed_new_terms:\n" + dumped.rstrip("\n"), text, count=1, flags=re.M)
        elif re.search(r"^proposed_new_terms:\s*$", text, re.M) and NTR_LABEL not in text.split("proposed_new_terms:")[1][:3000]:
            text = re.sub(r"^proposed_new_terms:\s*\n", "proposed_new_terms:\n" + dumped, text, count=1, flags=re.M)
        elif "proposed_new_terms" not in text:
            text = text.rstrip("\n") + "\nproposed_new_terms:\n" + dumped

        path.write_text(text)
        print(f"{rel}: NEW re-pointed {n_new}, ACCEPT rows scanned {n_acc}, quotes {len(quotes)}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
