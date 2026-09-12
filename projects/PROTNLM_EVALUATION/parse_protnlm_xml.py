"""Parse ProtNLM2 post-processed XML into TSV files for analysis.

Produces:
  - entries.tsv: one row per entry (accession, protein name, name type, prediction counts)
  - predictions.tsv: one row per prediction element (GO term, function comment, subcellular location)
  - evidence.tsv: one row per evidence block (model score, match provenance)
"""

import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = "http://uniprot.org/uniprot"

def ns(tag: str) -> str:
    return f"{{{NS}}}{tag}"


def parse_xml(xml_path: str, out_dir: str) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    entries_f = open(out / "entries.tsv", "w", newline="")
    preds_f = open(out / "predictions.tsv", "w", newline="")
    evid_f = open(out / "evidence.tsv", "w", newline="")

    ew = csv.writer(entries_f, delimiter="\t")
    pw = csv.writer(preds_f, delimiter="\t")
    vw = csv.writer(evid_f, delimiter="\t")

    ew.writerow(["accession", "protein_name", "name_type", "n_go", "n_function", "n_subcell", "n_evidence"])
    pw.writerow(["accession", "pred_type", "pred_id", "pred_label", "evidence_key"])
    vw.writerow([
        "accession", "evidence_key", "eco_type", "source_db", "source_id",
        "model_score", "match_text", "match_location", "match_type",
        "phmmer_accession", "phmmer_score",
        "tmalign_accession", "tmalign_score1", "tmalign_score2",
    ])

    count = 0
    for event, elem in ET.iterparse(xml_path, events=("end",)):
        if elem.tag != ns("entry"):
            continue
        count += 1

        acc = elem.find(ns("accession")).text

        # Protein name
        rec = elem.find(f".//{ns('recommendedName')}/{ns('fullName')}")
        sub = elem.find(f".//{ns('submittedName')}/{ns('fullName')}")
        if rec is not None:
            pname, ntype = rec.text, "recommended"
        elif sub is not None:
            pname, ntype = sub.text, "submitted"
        else:
            pname, ntype = "", "none"

        # GO terms
        gos = elem.findall(f"{ns('dbReference')}[@type='GO']")
        for go in gos:
            go_id = go.get("id")
            term_prop = go.find(f"{ns('property')}[@type='term']")
            label = term_prop.get("value", "") if term_prop is not None else ""
            ev_key = go.get("evidence", "")
            pw.writerow([acc, "GO", go_id, label, ev_key])

        # Comments (function, subcellular location)
        n_func = 0
        n_subcell = 0
        for comment in elem.findall(ns("comment")):
            ctype = comment.get("type", "")
            if ctype == "function":
                text_el = comment.find(ns("text"))
                if text_el is not None:
                    ev_key = text_el.get("evidence", "")
                    pw.writerow([acc, "function", "", text_el.text or "", ev_key])
                    n_func += 1
            elif ctype == "subcellular location":
                for loc in comment.findall(f".//{ns('location')}"):
                    ev_key = loc.get("evidence", "")
                    pw.writerow([acc, "subcellular_location", "", loc.text or "", ev_key])
                    n_subcell += 1

        # Evidence blocks
        evidences = elem.findall(ns("evidence"))
        for ev in evidences:
            key = ev.get("key", "")
            eco = ev.get("type", "")
            src = ev.find(ns("source"))
            if src is None:
                continue
            db = src.find(ns("dbReference"))
            if db is None:
                continue
            props = {p.get("type"): p.get("value") for p in db.findall(ns("property"))}
            vw.writerow([
                acc, key, eco,
                db.get("type", ""), db.get("id", ""),
                props.get("model_score", ""),
                props.get("string_match_text", ""),
                props.get("string_match_location", ""),
                props.get("string_match_type", ""),
                props.get("phmmer_accession", ""),
                props.get("phmmer_score", ""),
                props.get("tmalign_accession", ""),
                props.get("tmalign_score_chain_1", ""),
                props.get("tmalign_score_chain_2", ""),
            ])

        ew.writerow([acc, pname, ntype, len(gos), n_func, n_subcell, len(evidences)])
        elem.clear()

    entries_f.close()
    preds_f.close()
    evid_f.close()
    print(f"Parsed {count} entries -> {out}")


if __name__ == "__main__":
    xml_path = sys.argv[1] if len(sys.argv) > 1 else str(Path.home() / "Downloads/post-processed-2026_02_28k.xml")
    out_dir = sys.argv[2] if len(sys.argv) > 2 else str(Path(__file__).parent)
    parse_xml(xml_path, out_dir)
