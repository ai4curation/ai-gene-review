"""Fetch ProtNLM2 predictions from the UniProt REST API and produce TSV files.

Replaces parse_protnlm_xml.py for reproducibility — anyone can re-fetch from the
live API without needing the pre-release XML.

Produces the same 3 TSV files as the XML parser:
  - entries.tsv: one row per entry (accession, protein name, name type, prediction counts)
  - predictions.tsv: one row per prediction (GO term, function comment, subcellular location)
  - evidence.tsv: one row per evidence block (model score, match provenance)

Usage:
    # Fetch all public entries (from FTP accession list) — ~45 min at 10 req/s
    python fetch_protnlm_api.py

    # Fetch specific accessions from a file (one per line)
    python fetch_protnlm_api.py --accessions accessions.txt

    # Convert existing JSONL to TSVs without fetching
    python fetch_protnlm_api.py --convert-only

    # Resume an interrupted fetch (skips accessions already in JSONL)
    python fetch_protnlm_api.py --resume
"""

from __future__ import annotations

import argparse
import csv
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

API_BASE = "https://rest.uniprot.org/uniprotkb/protnlm"
FTP_ACCESSION_LIST = "https://ftp.ebi.ac.uk/pub/contrib/UniProt/ProtNLM2/List_of_UniProt_accessions_that_have_ProtNLM2_annotations.tsv"
REQUESTS_PER_SECOND = 10
MAX_RETRIES = 3


def fetch_accession_list() -> list[str]:
    """Download the FTP accession list (a TSV with Entry as the first column)."""
    print(f"Downloading accession list from {FTP_ACCESSION_LIST}...")
    req = urllib.request.Request(FTP_ACCESSION_LIST)
    with urllib.request.urlopen(req, timeout=30) as resp:
        lines = resp.read().decode().strip().split("\n")
    # First line is header: "Entry\tEntry Name\tOrganism (ID)\t..."
    accessions = []
    for line in lines[1:]:
        parts = line.strip().split("\t")
        if parts and parts[0]:
            accessions.append(parts[0])
    print(f"  {len(accessions)} accessions")
    return accessions


def load_accession_file(path: str) -> list[str]:
    """Load accessions from a file — handles both plain lists and TSV (first column)."""
    accessions = []
    with open(path) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            # Skip header line (heuristic: first field contains a space or is "Entry")
            if i == 0 and (parts[0] == "Entry" or " " in parts[0]):
                continue
            accessions.append(parts[0])
    return accessions


def fetch_one(accession: str) -> dict | None:
    url = f"{API_BASE}/{accession}"
    for attempt in range(MAX_RETRIES):
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code == 429:
                wait = 2 ** (attempt + 1)
                print(f"  Rate limited on {accession}, waiting {wait}s...")
                time.sleep(wait)
                continue
            raise
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError):
            if attempt < MAX_RETRIES - 1:
                time.sleep(2 ** (attempt + 1))
                continue
            raise
    return None


def fetch_all(accessions: list[str], jsonl_path: Path, resume: bool = False) -> None:
    done = set()
    if resume and jsonl_path.exists():
        with open(jsonl_path) as f:
            for line in f:
                obj = json.loads(line)
                done.add(obj["primaryAccession"])
        print(f"Resuming: {len(done)} already fetched")

    remaining = [a for a in accessions if a not in done]
    print(f"Fetching {len(remaining)} entries from {API_BASE}/...")

    mode = "a" if resume and jsonl_path.exists() else "w"
    interval = 1.0 / REQUESTS_PER_SECOND
    errors = []

    with open(jsonl_path, mode) as f:
        for i, acc in enumerate(remaining):
            start = time.monotonic()
            data = fetch_one(acc)
            if data is None:
                errors.append(acc)
            else:
                f.write(json.dumps(data) + "\n")

            if (i + 1) % 500 == 0:
                print(f"  {i + 1}/{len(remaining)} fetched ({len(errors)} errors)")
            elapsed = time.monotonic() - start
            if elapsed < interval:
                time.sleep(interval - elapsed)

    print(f"Done: {len(remaining) - len(errors)} fetched, {len(errors)} errors")
    if errors:
        err_path = jsonl_path.parent / "fetch_errors.txt"
        with open(err_path, "w") as f:
            f.write("\n".join(errors) + "\n")
        print(f"  Error accessions written to {err_path}")


def extract_evidence(evidences: list[dict] | None) -> dict:
    """Extract evidence properties from an inline evidence array."""
    if not evidences:
        return {}
    ev = evidences[0]
    props = {p["key"]: p["value"] for p in ev.get("properties", [])}
    return {
        "eco_type": ev.get("evidenceCode", ""),
        "source_db": ev.get("source", ""),
        "source_id": ev.get("id", ""),
        "model_score": props.get("model_score", ""),
        "match_text": props.get("string_match_text", ""),
        "match_location": props.get("string_match_location", ""),
        "match_type": props.get("string_match_type", ""),
        "phmmer_accession": props.get("phmmer_accession", ""),
        "phmmer_score": props.get("phmmer_score", ""),
        "tmalign_accession": props.get("tmalign_accession", ""),
        "tmalign_score1": props.get("tmalign_score_chain_1", ""),
        "tmalign_score2": props.get("tmalign_score_chain_2", ""),
    }


def convert_jsonl_to_tsvs(jsonl_path: Path, out_dir: Path) -> None:
    """Convert JSONL of API responses to the 3 TSV files."""
    entries_f = open(out_dir / "entries.tsv", "w", newline="")
    preds_f = open(out_dir / "predictions.tsv", "w", newline="")
    evid_f = open(out_dir / "evidence.tsv", "w", newline="")

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
    with open(jsonl_path) as f:
        for line in f:
            data = json.loads(line)
            acc = data["primaryAccession"]
            count += 1

            # Protein name
            desc = data.get("proteinDescription", {})
            rec = desc.get("recommendedName")
            sub = desc.get("submissionNames", [{}])
            if rec:
                pname = rec["fullName"]["value"]
                ntype = "recommended"
                name_evidences = rec["fullName"].get("evidences", [])
            elif sub and sub[0].get("fullName"):
                pname = sub[0]["fullName"]["value"]
                ntype = "submitted"
                name_evidences = sub[0]["fullName"].get("evidences", [])
            else:
                pname = ""
                ntype = "none"
                name_evidences = []

            ev_key = 0

            # Name evidence
            for ev_obj in name_evidences:
                ev_key += 1
                props = {p["key"]: p["value"] for p in ev_obj.get("properties", [])}
                vw.writerow([
                    acc, ev_key, ev_obj.get("evidenceCode", ""),
                    ev_obj.get("source", ""), ev_obj.get("id", ""),
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

            # GO terms
            xrefs = data.get("uniProtKBCrossReferences", [])
            go_xrefs = [x for x in xrefs if x.get("database") == "GO"]
            for go in go_xrefs:
                go_id = go["id"]
                go_term = ""
                for p in go.get("properties", []):
                    if p["key"] == "GoTerm":
                        go_term = p["value"]
                evidences = go.get("evidences", [])
                ev_keys = []
                for ev_obj in evidences:
                    ev_key += 1
                    ev_keys.append(str(ev_key))
                    props = {p["key"]: p["value"] for p in ev_obj.get("properties", [])}
                    vw.writerow([
                        acc, ev_key, ev_obj.get("evidenceCode", ""),
                        ev_obj.get("source", ""), ev_obj.get("id", ""),
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
                pw.writerow([acc, "GO", go_id, go_term, ",".join(ev_keys) if ev_keys else ""])

            # Comments (function, subcellular location)
            n_func = 0
            n_subcell = 0
            for comment in data.get("comments", []):
                ctype = comment.get("commentType", "")
                if ctype == "FUNCTION":
                    for text_obj in comment.get("texts", []):
                        evidences = text_obj.get("evidences", [])
                        ev_keys = []
                        for ev_obj in evidences:
                            ev_key += 1
                            ev_keys.append(str(ev_key))
                            props = {p["key"]: p["value"] for p in ev_obj.get("properties", [])}
                            vw.writerow([
                                acc, ev_key, ev_obj.get("evidenceCode", ""),
                                ev_obj.get("source", ""), ev_obj.get("id", ""),
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
                        pw.writerow([acc, "function", "", text_obj.get("value", ""),
                                     ",".join(ev_keys) if ev_keys else ""])
                        n_func += 1
                elif ctype == "SUBCELLULAR LOCATION":
                    for subloc in comment.get("subcellularLocations", []):
                        loc = subloc.get("location", {})
                        evidences = loc.get("evidences", [])
                        ev_keys = []
                        for ev_obj in evidences:
                            ev_key += 1
                            ev_keys.append(str(ev_key))
                            props = {p["key"]: p["value"] for p in ev_obj.get("properties", [])}
                            vw.writerow([
                                acc, ev_key, ev_obj.get("evidenceCode", ""),
                                ev_obj.get("source", ""), ev_obj.get("id", ""),
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
                        pw.writerow([acc, "subcellular_location", "", loc.get("value", ""),
                                     ",".join(ev_keys) if ev_keys else ""])
                        n_subcell += 1

            ew.writerow([acc, pname, ntype, len(go_xrefs), n_func, n_subcell, ev_key])

    entries_f.close()
    preds_f.close()
    evid_f.close()
    print(f"Converted {count} entries -> {out_dir}")


def main():
    parser = argparse.ArgumentParser(description="Fetch ProtNLM2 predictions from UniProt REST API")
    parser.add_argument("--accessions", help="File with accessions (one per line). Default: FTP list")
    parser.add_argument("--convert-only", action="store_true", help="Convert existing JSONL, skip fetching")
    parser.add_argument("--resume", action="store_true", help="Resume interrupted fetch")
    parser.add_argument("--out-dir", default=str(Path(__file__).parent), help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = out_dir / "protnlm_api.jsonl"

    if not args.convert_only:
        if args.accessions:
            accessions = load_accession_file(args.accessions)
        else:
            accessions = fetch_accession_list()
        fetch_all(accessions, jsonl_path, resume=args.resume)

    if not jsonl_path.exists():
        print(f"Error: {jsonl_path} not found. Run fetch first.")
        return

    convert_jsonl_to_tsvs(jsonl_path, out_dir)


if __name__ == "__main__":
    main()
