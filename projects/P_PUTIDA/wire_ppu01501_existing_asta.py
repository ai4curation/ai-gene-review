#!/usr/bin/env python3
"""Wire Asta provenance into existing ppu01501 reviews."""

from __future__ import annotations

from pathlib import Path

import yaml


SPECIES = "PSEPK"
ROOT = Path("genes") / SPECIES

ASTA_SUPPORT = {
    "oprD": "- **Protein Description:** SubName: Full=Basic-amino-acid specific porin OprD {ECO:0000313|EMBL:AAN66830.1}; EC=3.4.21.- {ECO:0000313|EMBL:AAN66830.1};",
    "ftsI": "- **Protein Description:** RecName: Full=Peptidoglycan D,D-transpeptidase FtsI {ECO:0000256|HAMAP-Rule:MF_02080}; EC=3.4.16.4 {ECO:0000256|HAMAP-Rule:MF_02080}; AltName: Full=Penicillin-binding protein 3 {ECO:0000256|HAMAP-Rule:MF_02080}; Short=PBP-3 {ECO:0000256|HAMAP-Rule:MF_02080};",
    "nagZ": "- **Protein Description:** RecName: Full=Beta-hexosaminidase {ECO:0000256|HAMAP-Rule:MF_00364}; EC=3.2.1.52 {ECO:0000256|HAMAP-Rule:MF_00364}; AltName: Full=Beta-N-acetylhexosaminidase {ECO:0000256|HAMAP-Rule:MF_00364}; AltName: Full=N-acetyl-beta-glucosaminidase {ECO:0000256|HAMAP-Rule:MF_00364};",
    "mexB": "- **Protein Description:** RecName: Full=Efflux pump membrane transporter {ECO:0000256|RuleBase:RU364070};",
    "mrdA-I": "- **Protein Description:** RecName: Full=Peptidoglycan D,D-transpeptidase MrdA {ECO:0000256|HAMAP-Rule:MF_02081}; EC=3.4.16.4 {ECO:0000256|HAMAP-Rule:MF_02081}; AltName: Full=Penicillin-binding protein 2 {ECO:0000256|HAMAP-Rule:MF_02081}; Short=PBP-2 {ECO:0000256|HAMAP-Rule:MF_02081};",
    "mrdA-II": "- **Protein Description:** RecName: Full=Peptidoglycan D,D-transpeptidase MrdA {ECO:0000256|HAMAP-Rule:MF_02081}; EC=3.4.16.4 {ECO:0000256|HAMAP-Rule:MF_02081}; AltName: Full=Penicillin-binding protein 2 {ECO:0000256|HAMAP-Rule:MF_02081}; Short=PBP-2 {ECO:0000256|HAMAP-Rule:MF_02081};",
}


def main() -> None:
    for gene, text in ASTA_SUPPORT.items():
        path = ROOT / gene / f"{gene}-ai-review.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        ref_id = f"file:{SPECIES}/{gene}/{gene}-deep-research-asta.md"
        refs = data.setdefault("references", [])
        if not any(ref.get("id") == ref_id for ref in refs):
            refs.append(
                {
                    "id": ref_id,
                    "title": f"Asta retrieval report for {gene}",
                    "findings": [
                        {
                            "statement": "Used as lightweight first-pass identity and functional context for the beta-lactam-resistance batch.",
                            "supporting_text": text,
                        }
                    ],
                }
            )

        annotations = data.get("existing_annotations") or []
        if not annotations:
            continue
        review = annotations[0].setdefault("review", {})
        supported_by = review.setdefault("supported_by", [])
        if not any(item.get("reference_id") == ref_id for item in supported_by):
            supported_by.append({"reference_id": ref_id, "supporting_text": text})

        path.write_text(yaml.safe_dump(data, sort_keys=False, width=100), encoding="utf-8")
        print(f"wired {gene}")


if __name__ == "__main__":
    main()
