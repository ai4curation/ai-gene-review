"""Generate GENE-protnlm-predictions-review.yaml files from bench50 evaluation data.

Reads bench50_evaluation_results.csv and bench50_novel_review.csv,
maps assessments to the PredictionReview schema (COR/CNN/LSP/UNC/PLI/NPI/REP),
and writes one YAML per protein into the appropriate genes/ directory.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

PROJ_ROOT = Path(__file__).resolve().parent.parent.parent

GENE_MAP = {
    "A0A2I0M3K7": ("COLLI", "A0A2I0M3K7", "Columba livia", "NCBITaxon:8932"),
    "A0A2K5UJ34": ("MACFA", "A0A2K5UJ34", "Macaca fascicularis", "NCBITaxon:9541"),
    "A0A2U1PS28": ("ARTAN", "A0A2U1PS28", "Artemisia annua", "NCBITaxon:35608"),
    "A0A3B6GK97": ("WHEAT", "A0A3B6GK97", "Triticum aestivum", "NCBITaxon:4565"),
    "A0A3B6NKR6": ("WHEAT", "A0A3B6NKR6", "Triticum aestivum", "NCBITaxon:4565"),
    "A0A3B6RKV1": ("WHEAT", "A0A3B6RKV1", "Triticum aestivum", "NCBITaxon:4565"),
    "A0A8B6GS20": ("MYTGA", "A0A8B6GS20", "Mytilus galloprovincialis", "NCBITaxon:29158"),
    "A0A8C2TBA7": ("COTJA", "A0A8C2TBA7", "Coturnix japonica", "NCBITaxon:93934"),
    "A0A8C5FPT8": ("GADMO", "A0A8C5FPT8", "Gadus morhua", "NCBITaxon:8049"),
    "A0A8C9H4D2": ("9PRIM", "A0A8C9H4D2", "Piliocolobus tephrosceles", "NCBITaxon:591936"),
    "A0A8J0SCI2": ("XENTR", "A0A8J0SCI2", "Xenopus tropicalis", "NCBITaxon:8364"),
    "A0A8M9QG43": ("DANRE", "A0A8M9QG43", "Danio rerio", "NCBITaxon:7955"),
    "A0BFB4": ("PARTE", "A0BFB4", "Paramecium tetraurelia", "NCBITaxon:5888"),
    "C6T1A2": ("SOYBN", "C6T1A2", "Glycine max", "NCBITaxon:3847"),
    "D3VIU4": ("XENNA", "D3VIU4", "Xenorhabdus nematophila", "NCBITaxon:40576"),
    "F4JLB7": ("ARATH", "F4JLB7", "Arabidopsis thaliana", "NCBITaxon:3702"),
    "F6LAX4": ("WHEAT", "F6LAX4", "Triticum aestivum", "NCBITaxon:4565"),
    "Q6YYC5": ("ORYSJ", "Q6YYC5", "Oryza sativa subsp. japonica", "NCBITaxon:39947"),
    "Q9KZ33": ("STRCO", "Q9KZ33", "Streptomyces coelicolor", "NCBITaxon:1902"),
    # Batch 2: remaining 20 from bench50 with GO predictions in eval results
    "A0A061AL94": ("CAEEL", "A0A061AL94", "Caenorhabditis elegans", "NCBITaxon:6239"),
    "A0A1S3Y076": ("TOBAC", "A0A1S3Y076", "Nicotiana tabacum", "NCBITaxon:4097"),
    "A0A2G9RZF1": ("AQUCT", "A0A2G9RZF1", "Aquarana catesbeiana", "NCBITaxon:8400"),
    "A0A2R9CAF4": ("PANPA", "A0A2R9CAF4", "Pan paniscus", "NCBITaxon:9597"),
    "A0A674PKV4": ("TAKRU", "A0A674PKV4", "Takifugu rubripes", "NCBITaxon:31033"),
    "A0A6I8TLE4": ("AEDAE", "A0A6I8TLE4", "Aedes aegypti", "NCBITaxon:7159"),
    "A0A6I8W8A2": ("DROPS", "A0A6I8W8A2", "Drosophila pseudoobscura pseudoobscura", "NCBITaxon:46245"),
    "A0A8B6BFL6": ("MYTGA", "A0A8B6BFL6", "Mytilus galloprovincialis", "NCBITaxon:29158"),
    "A0A8B8L1Z3": ("ABRPR", "A0A8B8L1Z3", "Abrus precatorius", "NCBITaxon:3816"),
    "A0A8I3PI07": ("CANLF", "A0A8I3PI07", "Canis lupus familiaris", "NCBITaxon:9615"),
    "A2FPI7": ("TRIV3", "A2FPI7", "Trichomonas vaginalis", "NCBITaxon:412133"),
    "B7FXQ8": ("PHATC", "B7FXQ8", "Phaeodactylum tricornutum", "NCBITaxon:556484"),
    "B8BAB0": ("ORYSI", "B8BAB0", "Oryza sativa subsp. indica", "NCBITaxon:39946"),
    "E1BL04": ("BOVIN", "E1BL04", "Bos taurus", "NCBITaxon:9913"),
    "G1TUN6": ("RABIT", "G1TUN6", "Oryctolagus cuniculus", "NCBITaxon:9986"),
    "Q2U1U6": ("ASPOR", "Q2U1U6", "Aspergillus oryzae", "NCBITaxon:510516"),
    "Q8P365": ("XANCP", "Q8P365", "Xanthomonas campestris pv. campestris", "NCBITaxon:190485"),
    "Q9L243": ("STRCO", "Q9L243", "Streptomyces coelicolor", "NCBITaxon:100226"),
    "Q9RSY6": ("DEIRA", "Q9RSY6", "Deinococcus radiodurans", "NCBITaxon:243230"),
    "S0EDH7": ("GIBF5", "S0EDH7", "Gibberella fujikuroi", "NCBITaxon:1279085"),
    # Batch 3: remaining 11 with no GO predictions (name_only or subcellular-only)
    "A0A1S3BTE3": ("CUCME", "A0A1S3BTE3", "Cucumis melo", "NCBITaxon:3656"),
    "A0A2I4G8T1": ("JUGRE", "A0A2I4G8T1", "Juglans regia", "NCBITaxon:51240"),
    "A0A444Z7V7": ("ARAHY", "A0A444Z7V7", "Arachis hypogaea", "NCBITaxon:3818"),
    "A0A4W3GVU1": ("CALMI", "A0A4W3GVU1", "Callorhinchus milii", "NCBITaxon:7868"),
    "A0A804UIX9": ("MAIZE", "A0A804UIX9", "Zea mays", "NCBITaxon:4577"),
    "A0A8B8WEG2": ("BALMU", "A0A8B8WEG2", "Balaenoptera musculus", "NCBITaxon:9771"),
    "A0A8J1IYX6": ("XENTR", "A0A8J1IYX6", "Xenopus tropicalis", "NCBITaxon:8364"),
    "B4MAQ2": ("DROVI", "B4MAQ2", "Drosophila virilis", "NCBITaxon:7244"),
    "F6WPT1": ("XENTR", "F6WPT1", "Xenopus tropicalis", "NCBITaxon:8364"),
    "Q7NUH2": ("CHRVO", "Q7NUH2", "Chromobacterium violaceum", "NCBITaxon:243365"),
    "Q7VZI5": ("BORPE", "Q7VZI5", "Bordetella pertussis", "NCBITaxon:257313"),
}

PROTEIN_NAMES = {
    "A0A2I0M3K7": "TruB pseudouridine synthase family member 2 (TRUB2)",
    "A0A2K5UJ34": "Tetratricopeptide repeat domain 39C (TTC39C)",
    "A0A2U1PS28": "Translation factor GUF1 homolog, mitochondrial",
    "A0A3B6GK97": "Patatin (PNPLA domain-containing protein)",
    "A0A3B6NKR6": "GHMP kinase N-terminal domain-containing protein",
    "A0A3B6RKV1": "JmjC domain-containing protein",
    "A0A8B6GS20": "Myotubularin-related protein 9 (MTMR9)",
    "A0A8C2TBA7": "Peptidylglycine alpha-amidating monooxygenase (PAM)",
    "A0A8C5FPT8": "Rab-GAP TBC domain-containing protein (TBC1D14)",
    "A0A8C9H4D2": "Olfactomedin-like protein 2A (OLFML2A)",
    "A0A8J0SCI2": "Gastrula zinc finger protein XlCGF17.1-like",
    "A0A8M9QG43": "Auxilin (DnaJ homolog subfamily C member 6, dnajc6)",
    "A0BFB4": "Protein kinase domain-containing protein (uncharacterized)",
    "C6T1A2": "C2H2-Zn transcription factor (Glyma17g18110.1)",
    "D3VIU4": "Cystine transport protein FliY",
    "F4JLB7": "ROP-interactive CRIB motif-containing protein 7 (RIC7)",
    "F6LAX4": "Protein phosphatase 2A structural subunit (PP2A regulatory subunit A)",
    "Q6YYC5": "E3 ubiquitin-protein ligase Os08g0135400 (RGLG family)",
    "Q9KZ33": "Uncharacterized protein SCO7099 (ECF RNA polymerase sigma factor)",
    # Batch 2
    "A0A061AL94": "DNA replication licensing factor mcm-4",
    "A0A1S3Y076": "Proteinaceous RNase P 3",
    "A0A2G9RZF1": "CUB domain-containing protein (Neuropilin and tolloid-like protein 2)",
    "A0A2R9CAF4": "Sodium-independent sulfate anion transporter (STAS domain-containing protein)",
    "A0A674PKV4": "Growth arrest-specific protein 7a (F-BAR domain-containing protein)",
    "A0A6I8TLE4": "Ras GTPase-activating protein raskol",
    "A0A6I8W8A2": "Probable E3 ubiquitin-protein ligase HERC3",
    "A0A8B6BFL6": "Integrase_H2C2 domain-containing protein (reverse transcriptase)",
    "A0A8B8L1Z3": "J domain-containing protein (DnaJ homolog)",
    "A0A8I3PI07": "Metal transporter (uncharacterized)",
    "A2FPI7": "KilA-N domain-containing protein (uncharacterized)",
    "B7FXQ8": "Small heat shock protein (SHSP/Hsp20 domain-containing protein)",
    "B8BAB0": "POLYGALACTURONASE 1 (BURP domain-containing protein)",
    "E1BL04": "Xin actin binding repeat containing 2 (XIRP2)",
    "G1TUN6": "UBC core domain-containing protein (E2 ubiquitin-conjugating enzyme)",
    "Q2U1U6": "Glycoside hydrolase (uncharacterized protein)",
    "Q8P365": "Glutathione peroxidase (uncharacterized)",
    "Q9L243": "Secreted protein (5'-nucleotidase-like)",
    "Q9RSY6": "Small ribosomal subunit protein bS1",
    "S0EDH7": "Protein kinase domain-containing protein",
    # Batch 3
    "A0A1S3BTE3": "Mitogen-activated protein kinase 15",
    "A0A2I4G8T1": "UDP-glycosyltransferase 73C1",
    "A0A444Z7V7": "Cellulose synthase-like protein D3",
    "A0A4W3GVU1": "RRM domain-containing protein",
    "A0A804UIX9": "PGG domain-containing protein",
    "A0A8B8WEG2": "Protein kinase domain-containing protein (blue whale)",
    "A0A8J1IYX6": "Protein kinase domain-containing protein (Xenopus)",
    "B4MAQ2": "Importin N-terminal domain-containing protein",
    "F6WPT1": "ADP-ribosylation factor-like protein 1",
    "Q7NUH2": "HTH marR-type domain-containing protein",
    "Q7VZI5": "PrpF family protein",
}


def go_type(pred_label: str) -> str:
    """Determine GO term type from prediction label prefix."""
    if pred_label.startswith("F:"):
        return "GO_MF"
    elif pred_label.startswith("P:"):
        return "GO_BP"
    elif pred_label.startswith("C:"):
        return "GO_CC"
    return "GO_MF"


def strip_prefix(label: str) -> str:
    """Remove F:/P:/C: prefix from GO label."""
    if label and label[1:2] == ":":
        return label[2:]
    return label


def map_novel_assessment(assessment: str, accession: str, pred_id: str) -> tuple[str, int, str]:
    """Map bench50_novel_review assessment to schema (assessment, confidence, error_type)."""
    if assessment == "TRIVIALLY_DERIVABLE":
        return "CNN", 2, ""
    elif assessment == "PHMMER_TRANSFER_PLAUSIBLE":
        return "UNC", 1, ""
    elif assessment == "PHMMER_TRANSFER_DUBIOUS":
        if accession == "A0A2U1PS28":
            return "NPI", 0, "PARALOG_OVERANNOTATION"
        elif accession == "F6LAX4" and pred_id == "GO:1990405":
            return "NPI", 0, "PATHWAY_CONTEXT_IGNORED"
        return "NPI", 0, ""
    elif assessment == "MULTIDOMAIN_FALSE_POSITIVE":
        if accession == "A0A8B6GS20":
            return "PLI", 0, "PARALOG_OVERANNOTATION"
        elif accession == "D3VIU4":
            return "NPI", 0, "PATHWAY_CONTEXT_IGNORED"
        return "NPI", 0, "MULTIPLE_FUNCTIONS"
    elif assessment == "CROSS_KINGDOM_ERROR":
        return "NPI", 0, "PATHWAY_CONTEXT_IGNORED"
    return "UNC", 1, ""


def yaml_str(s: str) -> str:
    """Format a string for YAML, quoting if needed."""
    if not s:
        return "''"
    if any(c in s for c in ":#{}[]|>&*!%@`\"',"):
        escaped = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return s


def write_yaml(accession: str, predictions: list[dict], out_path: Path) -> None:
    """Write a PredictionReview YAML file."""
    org, gene, organism, taxon_id = GENE_MAP[accession]
    protein_name = PROTEIN_NAMES[accession]

    lines = []
    lines.append(f"id: {accession}")
    lines.append(f"gene_symbol: {gene}")
    lines.append("taxon:")
    lines.append(f"  id: {taxon_id}")
    lines.append(f"  label: {yaml_str(organism)}")
    lines.append("status: COMPLETE")

    n_correct = sum(1 for p in predictions if p["assessment"] in ("COR", "CNN", "LSP"))
    n_incorrect = sum(1 for p in predictions if p["assessment"] in ("PLI", "NPI", "REP"))
    n_uncertain = sum(1 for p in predictions if p["assessment"] == "UNC")
    lines.append(f"description: >-")
    if not predictions:
        lines.append(f"  ProtNLM2 made no predictions (GO or subcellular location) for")
        lines.append(f"  {protein_name}. The model returned only a protein name.")
    else:
        lines.append(f"  ProtNLM2 predicted {len(predictions)} GO term(s) for {protein_name}.")
        lines.append(f"  Assessment: {n_correct} correct (CNN/LSP), {n_uncertain} uncertain (UNC),")
        lines.append(f"  {n_incorrect} incorrect (NPI/PLI).")

    lines.append("source_documents:")
    lines.append(f"  - genes/{org}/{gene}/{gene}-uniprot.txt")
    lines.append(f"  - genes/{org}/{gene}/{gene}-goa.tsv")
    lines.append("predictions:")

    if not predictions:
        lines.append("  []")
    else:
        for pred in predictions:
            lines.append(f"  - source_method: ProtNLM2")
            lines.append(f"    source_version: UniProt 2024_06 pilot")
            lines.append(f"    predicted_term:")
            lines.append(f"      id: {pred['pred_id']}")
            lines.append(f"      label: {yaml_str(pred['pred_label'])}")
            lines.append(f"    predicted_term_type: {pred['term_type']}")
            lines.append(f"    review:")
            lines.append(f"      assessment: {pred['assessment']}")
            lines.append(f"      confidence_score: {pred['confidence']}")
            if pred.get("error_type"):
                lines.append(f"      error_type: {pred['error_type']}")
            summary = pred["summary"]
            lines.append(f"      summary: >-")
            for sline in wrap_text(summary, 76):
                lines.append(f"        {sline}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n")
    print(f"  Wrote {out_path}")


def wrap_text(text: str, width: int) -> list[str]:
    """Simple word-wrap for YAML block scalars."""
    words = text.split()
    result_lines = []
    current = []
    length = 0
    for w in words:
        if length + len(w) + 1 > width and current:
            result_lines.append(" ".join(current))
            current = [w]
            length = len(w)
        else:
            current.append(w)
            length += len(w) + 1
    if current:
        result_lines.append(" ".join(current))
    return result_lines


def main():
    proj_dir = Path(__file__).resolve().parent

    eval_results = {}
    with open(proj_dir / "bench50_evaluation_results.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            acc = row["accession"]
            if acc in GENE_MAP:
                eval_results.setdefault(acc, []).append(row)

    novel_reviews = {}
    with open(proj_dir / "bench50_novel_review.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row["accession"], row["pred_id"])
            novel_reviews[key] = row

    evidence_scores = {}
    with open(proj_dir / "evidence.tsv") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            acc = row["accession"]
            if acc in GENE_MAP:
                evidence_scores.setdefault(acc, {})[row["evidence_key"]] = row

    pred_evidence_map = {}
    subcell_predictions = {}
    with open(proj_dir / "predictions.tsv") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            acc = row["accession"]
            if acc in GENE_MAP:
                if row["pred_type"] == "GO":
                    pred_evidence_map[(acc, row["pred_id"])] = row.get("evidence_key", "")
                elif row["pred_type"] == "subcellular_location":
                    subcell_predictions.setdefault(acc, []).append(row)

    count = 0
    for accession in sorted(GENE_MAP.keys()):
        org, gene, organism, taxon_id = GENE_MAP[accession]
        eval_preds = eval_results.get(accession, [])

        predictions = []
        for ep in eval_preds:
            pred_id = ep["pred_id"]
            pred_label_raw = ep["pred_label"]
            pred_label = strip_prefix(pred_label_raw)
            term_type = go_type(pred_label_raw)
            match_cat = ep["match_category"]

            novel_key = (accession, pred_id)
            novel = novel_reviews.get(novel_key)

            if match_cat == "EXACT":
                assessment = "CNN"
                confidence = 2
                error_type = ""
                goa_match = ep.get("goa_match", "")
                goa_label = ep.get("goa_match_label", "")
                summary = (
                    f"ProtNLM2 predicted {pred_id} ({pred_label}), which matches "
                    f"existing GOA annotation {goa_match} ({goa_label}). "
                    f"Correct but not a novel prediction."
                )
            elif match_cat == "LESS_SPECIFIC":
                assessment = "LSP"
                confidence = 2
                error_type = ""
                goa_match = ep.get("goa_match", "")
                goa_label = ep.get("goa_match_label", "")
                summary = (
                    f"ProtNLM2 predicted {pred_id} ({pred_label}), which is less "
                    f"specific than existing GOA annotation {goa_match} ({goa_label}). "
                    f"Correct at a higher level but not informative."
                )
            elif match_cat == "MORE_SPECIFIC":
                assessment = "CNN"
                confidence = 2
                error_type = ""
                goa_match = ep.get("goa_match", "")
                goa_label = ep.get("goa_match_label", "")
                summary = (
                    f"ProtNLM2 predicted {pred_id} ({pred_label}), which is more "
                    f"specific than existing GOA annotation {goa_match} ({goa_label}). "
                    f"The prediction subsumes the existing annotation and is correct."
                )
            elif match_cat == "NO_OVERLAP":
                assessment = "UNC"
                confidence = 1
                error_type = ""
                summary = (
                    f"ProtNLM2 predicted {pred_id} ({pred_label}), which has no "
                    f"overlap with existing GOA annotations. Requires expert review "
                    f"to determine correctness."
                )
            elif novel:
                assessment, confidence, error_type = map_novel_assessment(
                    novel["assessment"], accession, pred_id
                )
                summary = novel["reasoning"]
            else:
                assessment = "UNC"
                confidence = 1
                error_type = ""
                summary = (
                    f"ProtNLM2 predicted {pred_id} ({pred_label}) with match category "
                    f"{match_cat}. Not in GOA; requires expert review."
                )

            ev_key = pred_evidence_map.get((accession, pred_id), "")
            model_score = ""
            if ev_key and accession in evidence_scores:
                ev_data = evidence_scores[accession].get(ev_key, {})
                model_score = ev_data.get("model_score", "")

            predictions.append({
                "pred_id": pred_id,
                "pred_label": pred_label,
                "term_type": term_type,
                "assessment": assessment,
                "confidence": confidence,
                "error_type": error_type,
                "summary": summary,
                "model_score": model_score,
            })

        SUBCELL_TO_GO = {
            "Nucleus": ("GO:0005634", "nucleus"),
            "Cytoplasm": ("GO:0005737", "cytoplasm"),
            "Mitochondrion": ("GO:0005739", "mitochondrion"),
            "Plastid": ("GO:0009536", "plastid"),
            "Chloroplast": ("GO:0009507", "chloroplast"),
            "Membrane": ("GO:0016020", "membrane"),
            "Secreted": ("GO:0005576", "extracellular region"),
        }
        for sp in subcell_predictions.get(accession, []):
            subcell_label = sp.get("pred_label", "")
            go_id, go_label = SUBCELL_TO_GO.get(subcell_label, ("", subcell_label))
            if not go_id:
                continue
            predictions.append({
                "pred_id": go_id,
                "pred_label": go_label,
                "term_type": "GO_CC",
                "assessment": "UNC",
                "confidence": 1,
                "error_type": "",
                "summary": (
                    f"ProtNLM2 predicted subcellular location '{subcell_label}', "
                    f"mapped to {go_id} ({go_label}). This is a subcellular "
                    f"location prediction rather than a direct GO term prediction."
                ),
                "model_score": "",
            })

        out_path = PROJ_ROOT / "genes" / org / gene / f"{gene}-protnlm-predictions-review.yaml"
        only_missing = "--only-missing" in sys.argv
        if only_missing and out_path.exists():
            continue
        write_yaml(accession, predictions, out_path)
        count += 1

    print(f"\nGenerated {count} prediction review files.")


if __name__ == "__main__":
    main()
