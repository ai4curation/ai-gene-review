#!/usr/bin/env python3
"""Deterministic active-site and oxyanion-motif extractor for PANTHER:PTHR46118.

Parses the exact 1-indexed protein sequences and sequence versions from:
  1. All 11 in-repo `genes/*/*/*-uniprot.txt` records (`SQ` block + `DT` version) offline, and
  2. The 4 non-local PANTHER control members (`P75736`, `Q8ZQX0`, `Q57427`, `Q54QK2`)
     via `.cache/uniprot_seq/` (`SequenceCache`, which fetches from UniProt REST on a cold cache).

Emits:
  - `genes/human/ABHD11/ABHD11-bioinformatics/motif_table.tsv`
  - `genes/human/ABHD11/ABHD11-bioinformatics/RESULTS.md`
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[4]
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

from ai_gene_review.validation.family_residue_validator import SequenceCache  # noqa: E402

AA3 = {
    "A": "Ala",
    "C": "Cys",
    "D": "Asp",
    "E": "Glu",
    "F": "Phe",
    "G": "Gly",
    "H": "His",
    "I": "Ile",
    "K": "Lys",
    "L": "Leu",
    "M": "Met",
    "N": "Asn",
    "P": "Pro",
    "Q": "Gln",
    "R": "Arg",
    "S": "Ser",
    "T": "Thr",
    "V": "Val",
    "W": "Trp",
    "Y": "Tyr",
}


@dataclass(frozen=True)
class MemberSpec:
    accession: str
    gene: str
    organism: str
    subfamily: str
    uniprot_relpath: str | None
    status: str


MEMBERS: tuple[MemberSpec, ...] = (
    MemberSpec(
        "Q8NFV4",
        "ABHD11",
        "Homo sapiens",
        "PTHR46118:SF4",
        "genes/human/ABHD11/ABHD11-uniprot.txt",
        "Active glutaryl-lipoyl thioesterase / esterase",
    ),
    MemberSpec(
        "Q8K4F5",
        "Abhd11",
        "Mus musculus",
        "PTHR46118:SF4",
        "genes/mouse/Abhd11/Abhd11-uniprot.txt",
        "Active mitochondrial matrix ortholog",
    ),
    MemberSpec(
        "A0A8I6AS56",
        "Abhd11",
        "Rattus norvegicus",
        "PTHR46118:SF4",
        "genes/rat/Abhd11/Abhd11-uniprot.txt",
        "Active mitochondrial matrix ortholog",
    ),
    MemberSpec(
        "Q6DRD9",
        "abhd11",
        "Danio rerio",
        "PTHR46118:SF4",
        "genes/DANRE/abhd11/abhd11-uniprot.txt",
        "Active mitochondrial matrix ortholog",
    ),
    MemberSpec(
        "Q9W3R8",
        "CG2059",
        "Drosophila melanogaster",
        "PTHR46118:SF4",
        "genes/DROME/CG2059/CG2059-uniprot.txt",
        "Active serine carboxylesterase (`PTN000106319`)",
    ),
    MemberSpec(
        "Q9VGJ4",
        "CG14717",
        "Drosophila melanogaster",
        "PTHR46118:SF4",
        "genes/DROME/CG14717/CG14717-uniprot.txt",
        "Non-catalytic pseudoenzyme (`Ser->Gly120`, `PTN002451174`)",
    ),
    MemberSpec(
        "O45707",
        "abhd-11.2",
        "Caenorhabditis elegans",
        "PTHR46118:SF4",
        "genes/worm/abhd-11.2/abhd-11.2-uniprot.txt",
        "Active catalytic triad intact",
    ),
    MemberSpec(
        "O62202",
        "abhd-11.1",
        "Caenorhabditis elegans",
        "PTHR46118:SF3",
        "genes/worm/abhd-11.1/abhd-11.1-uniprot.txt",
        "Active triad intact (`Pro42` replaces oxyanion `His`, `-GLFG-` retained)",
    ),
    MemberSpec(
        "P53219",
        "IMO32",
        "Saccharomyces cerevisiae",
        "PTHR46118:SF4",
        "genes/yeast/IMO32/IMO32-uniprot.txt",
        "Active mitochondrial matrix alpha/beta-hydrolase",
    ),
    MemberSpec(
        "P53208",
        "EAT1",
        "Saccharomyces cerevisiae",
        "PTHR46118:SF4",
        "genes/yeast/EAT1/EAT1-uniprot.txt",
        "Active mitochondrial ethanol O-acetyltransferase / thioesterase / esterase",
    ),
    MemberSpec(
        "O94437",
        "SPAC22H12.03",
        "Schizosaccharomyces pombe",
        "PTHR46118:SF4",
        "genes/SCHPO/SPAC22H12.03/SPAC22H12.03-uniprot.txt",
        "Active mitochondrial alpha/beta-hydrolase",
    ),
    MemberSpec(
        "P75736",
        "ybfF",
        "Escherichia coli K-12",
        "PTHR46118:SF4",
        None,
        "Active bacterial cytoplasmic acyl-CoA/pNP esterase (no mitochondria)",
    ),
    MemberSpec(
        "Q8ZQX0",
        "ybfF",
        "Salmonella typhimurium LT2",
        "PTHR46118:SF4",
        None,
        "Bacterial cytoplasmic esterase (no mitochondria)",
    ),
    MemberSpec(
        "Q57427",
        "HI_0193",
        "Haemophilus influenzae Rd",
        "PTHR46118:SF4",
        None,
        "Bacterial cytoplasmic esterase (no mitochondria)",
    ),
    MemberSpec(
        "Q54QK2",
        "DDB_G0283799",
        "Dictyostelium discoideum",
        "PTHR46118:SF5",
        None,
        "Active catalytic triad intact",
    ),
)


def parse_uniprot_flatfile(path: Path) -> tuple[str, int]:
    """Parse canonical sequence and sequence version from a UniProt `.txt` file."""
    text = path.read_text(encoding="utf-8")
    sv_match = re.search(r"sequence version (\d+)\.", text)
    if not sv_match:
        raise ValueError(f"Missing sequence version line in {path}")
    sv = int(sv_match.group(1))
    sq_match = re.search(r"^SQ\s+SEQUENCE\s+(\d+)\s+AA;.*?\n(.*?)^//", text, re.M | re.S)
    if not sq_match:
        raise ValueError(f"Missing SQ sequence block in {path}")
    declared_len = int(sq_match.group(1))
    seq = re.sub(r"[^A-Z]", "", sq_match.group(2))
    if len(seq) != declared_len:
        raise ValueError(f"Sequence length mismatch in {path}: {len(seq)} != {declared_len}")
    return seq, sv


def load_cached_or_remote_sequence(
    cache: SequenceCache, accession: str
) -> tuple[str, int, str]:
    """Load sequence + version for non-local control accessions via SequenceCache (`.cache/uniprot_seq/`)."""
    seq = cache.get(accession)
    sv = cache.sequence_version(accession) or 1
    return seq, sv, f".cache/uniprot_seq/{accession}.seq"


def extract_member_motifs(spec: MemberSpec, seq: str, sv: int, source_label: str) -> dict[str, str | int]:
    """Deterministically extract 1-indexed oxyanion loop and catalytic triad motifs from `seq`."""
    # 1. Beta-5 nucleophilic elbow (GxSxG, or GxGxG in pseudoenzyme CG14717; Phe at -1 in EAT1)
    nuc_hits = list(re.finditer(r"G[HF][SG]MG[GA][KR]", seq))
    if len(nuc_hits) != 1:
        raise ValueError(f"{spec.accession}: expected 1 nucleophilic elbow match, got {len(nuc_hits)}")
    nuc_idx0 = nuc_hits[0].start() + 2
    nuc_pos = nuc_idx0 + 1
    nuc_aa = seq[nuc_idx0]
    nuc_win = seq[nuc_idx0 - 4 : nuc_idx0 + 5]

    # 2. Oxyanion-hole loop N-terminal to the nucleophilic elbow ([HP][GD]L[FLN][GL])
    oxy_hits = list(re.finditer(r"[HP][GD]L[FLN][GL]", seq[: nuc_idx0 - 40]))
    if len(oxy_hits) != 1:
        raise ValueError(f"{spec.accession}: expected 1 oxyanion motif match, got {len(oxy_hits)}")
    oxy_s0 = oxy_hits[0].start()
    oxy_start = oxy_s0 + 1
    oxy_end = oxy_s0 + 5
    oxy_5mer = seq[oxy_s0 : oxy_s0 + 5]
    oxy_10mer = seq[oxy_s0 - 3 : oxy_s0 + 7]
    oxy_10mer_range = f"{oxy_start - 3}-{oxy_10mer}-{oxy_end + 2}"

    # 3. Beta-6 charge-relay carboxylate (Asp or Glu) ~24-26 residues C-terminal to nucleophile
    acid_sub = seq[nuc_idx0 + 20 : nuc_idx0 + 30]
    acid_hits = list(re.finditer(r"[DE][IVMLN][STALP]P", acid_sub))
    if len(acid_hits) != 1:
        raise ValueError(f"{spec.accession}: expected 1 beta-6 acid match in {acid_sub}, got {len(acid_hits)}")
    acid_idx0 = nuc_idx0 + 20 + acid_hits[0].start()
    acid_pos = acid_idx0 + 1
    acid_aa = seq[acid_idx0]
    acid_win = seq[acid_idx0 - 4 : acid_idx0 + 5]

    # 4. Beta-8-alpha-F general-base histidine near C-terminus
    his_region_start0 = len(seq) - 36
    his_sub = seq[his_region_start0 : len(seq) - 12]
    his_hits = list(re.finditer(r"[GSND]H[WLFNC][IVL]", his_sub))
    if len(his_hits) != 1:
        raise ValueError(f"{spec.accession}: expected 1 general-base His match in {his_sub}, got {len(his_hits)}")
    his_idx0 = his_region_start0 + his_hits[0].start() + 1
    his_pos = his_idx0 + 1
    his_aa = seq[his_idx0]
    his_win = seq[his_idx0 - 4 : his_idx0 + 5]

    # Self-consistency assertions on 1-indexed slicing
    assert seq[oxy_start - 1 : oxy_end] == oxy_5mer
    assert seq[nuc_pos - 5 : nuc_pos + 4] == nuc_win and nuc_win[4] == nuc_aa
    assert seq[acid_pos - 5 : acid_pos + 4] == acid_win and acid_win[4] == acid_aa
    assert seq[his_pos - 5 : his_pos + 4] == his_win and his_win[4] == his_aa

    return {
        "accession": f"UniProtKB:{spec.accession}",
        "gene_symbol": spec.gene,
        "organism": spec.organism,
        "subfamily": spec.subfamily,
        "length": len(seq),
        "sequence_version": sv,
        "oxyanion_motif": f"{oxy_start}-{oxy_5mer}-{oxy_end}",
        "oxyanion_context": oxy_10mer_range,
        "nucleophile": f"{AA3[nuc_aa]}{nuc_pos}",
        "nucleophile_window": f"{nuc_pos - 4}-{nuc_win}-{nuc_pos + 4}",
        "nucleophile_9mer": nuc_win,
        "catalytic_acid": f"{AA3[acid_aa]}{acid_pos}",
        "catalytic_acid_window": f"{acid_pos - 4}-{acid_win}-{acid_pos + 4}",
        "catalytic_acid_9mer": acid_win,
        "general_base_his": f"{AA3[his_aa]}{his_pos}",
        "general_base_window": f"{his_pos - 4}-{his_win}-{his_pos + 4}",
        "general_base_9mer": his_win,
        "status": spec.status,
        "sequence_source": source_label,
    }


def verify_auxiliary_claims(seqs: dict[str, str]) -> None:
    """Verify cap-domain FT ACT_SITE homology residues and human Q8NFV4 crosswalk claims."""
    cap_checks = [
        ("Q8NFV4", 228, "D", "WRVNLDALT"),
        ("Q8K4F5", 229, "D", "WRLNLDTLA"),
        ("Q6DRD9", 238, "E", "WRINLESIS"),
        ("O94437", 190, "E", "FRVPIELIS"),
        ("P75736", 176, "P", "WRFNVPVLW"),
        ("Q9W3R8", 225, "H", "WACNAHVLR"),
        ("O45707", 220, "N", "WKININTID"),
    ]
    for acc, pos, expected_aa, expected_9mer in cap_checks:
        s = seqs[acc]
        assert s[pos - 1] == expected_aa, f"{acc}:{pos} expected {expected_aa}, got {s[pos - 1]}"
        assert s[pos - 6 : pos + 3] == expected_9mer, f"{acc}:{pos} window mismatch: {s[pos - 6 : pos + 3]}"

    # Verify O62202 residues 41..50 (`VPGLFGTKEN`) cited in SF3 oxyanion note
    assert seqs["O62202"][40:50] == "VPGLFGTKEN"
    # Verify Q8NFV4 nucleophilic 5-mer `130-GHSMG-134`
    assert seqs["Q8NFV4"][129:134] == "GHSMG"
    # Verify E. coli YbfF (P75736) helical-cap substrate-anchoring Arg123 and Tyr208 (PMID:18215690 abstract)
    assert seqs["P75736"][122] == "R", f"P75736:123 expected R, got {seqs['P75736'][122]}"
    assert seqs["P75736"][207] == "Y", f"P75736:208 expected Y, got {seqs['P75736'][207]}"


def render_results_md(rows: list[dict[str, str | int]]) -> str:
    """Render `RESULTS.md` deterministically from extracted sequence motif records."""
    table_lines = [
        "| Accession | Gene | Organism | Subfamily | Length (sv) | Oxyanion Motif | Nucleophile (1-based) | Beta-6 Acid (1-based) | General-Base His (1-based) | Status |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for r in rows:
        org_md = r["organism"]
        # Italicize species binomial while keeping strain suffixes upright
        for binomial in (
            "Homo sapiens",
            "Mus musculus",
            "Rattus norvegicus",
            "Danio rerio",
            "Drosophila melanogaster",
            "Caenorhabditis elegans",
            "Saccharomyces cerevisiae",
            "Schizosaccharomyces pombe",
            "Escherichia coli",
            "Salmonella typhimurium",
            "Haemophilus influenzae",
            "Dictyostelium discoideum",
        ):
            if str(org_md).startswith(binomial):
                org_md = f"*{binomial}*" + str(org_md)[len(binomial) :]
                break
        table_lines.append(
            f"| `{r['accession']}` | `{r['gene_symbol']}` | {org_md} | `{r['subfamily']}` | "
            f"{r['length']} (`sv={r['sequence_version']}`) | `{r['oxyanion_motif']}` | "
            f"`{r['nucleophile']}` (`{r['nucleophile_9mer']}`) | "
            f"`{r['catalytic_acid']}` (`{r['catalytic_acid_9mer']}`) | "
            f"`{r['general_base_his']}` (`{r['general_base_9mer']}`) | {r['status']} |"
        )

    table_block = "\n".join(table_lines)
    return f"""# PTHR46118 (PROTEIN ABHD11) Phylogeny, Active-Site Conservation, and Coordinate Crosswalk

Generated deterministically by `genes/human/ABHD11/ABHD11-bioinformatics/extract_motifs.py` (with full machine-readable coordinates in `genes/human/ABHD11/ABHD11-bioinformatics/motif_table.tsv`). **Sequence-provenance boundary**: the 11 in-scope eukaryotic rows are parsed completely offline directly from the committed `genes/<species>/<gene>/<gene>-uniprot.txt` `SQ` blocks and `DT` sequence-version lines, whereas the 4 out-of-scope PANTHER control rows (`P75736`, `Q8ZQX0`, `Q57427`, `Q54QK2`) have no local `genes/` directory and resolve via `.cache/uniprot_seq/` (`SequenceCache`, requiring network access to UniProt REST on a fresh checkout if `.cache/uniprot_seq/` is unpopulated).

## 1. PANTHER 19.0 Family and Subfamily Architecture (`PANTHER:PTHR46118`)

- **Official family name**: `PROTEIN ABHD11` (`PANTHER:PTHR46118`)
- **Subfamilies**:
  - `PANTHER:PTHR46118:SF4` (`PROTEIN ABHD11`, clade node `PANTHER:PTN008704070` at `LUCA`): Trans-kingdom subfamily spanning both eukaryotic mitochondrial orthologs/paralogs (`PTN002919262` `Eukaryota` -> `PTN000106239` `Unikonts`) and bacterial cytoplasmic esterases (`PTN008704081` `Eubacteria`: *Escherichia coli* K-12 `ybfF` `UniProtKB:P75736`, *Salmonella enterica* serovar Typhimurium LT2 `ybfF` `UniProtKB:Q8ZQX0`, and *Haemophilus influenzae* `HI_0193` `UniProtKB:Q57427`).
  - `PANTHER:PTHR46118:SF3` (`AB HYDROLASE-1 DOMAIN-CONTAINING PROTEIN`, clade node `PANTHER:PTN002251067` at `Caenorhabditis`): Nematode lineage-specific duplicate `abhd-11.1` (`UniProtKB:O62202`), sister to `SF4` `abhd-11.2` (`UniProtKB:O45707`) below nematode duplication `PANTHER:PTN002251066`.
  - `PANTHER:PTHR46118:SF5` (`AB HYDROLASE-1 DOMAIN-CONTAINING PROTEIN`, clade node `PANTHER:PTN000862953` at `Dictyostelium`): Amoebozoan duplicate `DDB_G0283799` (`UniProtKB:Q54QK2`), sister to `SF4` `DDB_G0278415` (`UniProtKB:Q54Y48`) below amoebozoan duplication `PANTHER:PTN002251098`.

## 2. Verified 1-Based Catalytic Triad and Oxyanion-Hole Alignment Across PTHR46118 Members

Sequence alignment against *Escherichia coli* K-12 YbfF (`UniProtKB:P75736`, 254 aa, `sv=1`)—whose 1.1-A and 1.68-A crystal structures (`PDB:3BF7`, `PMID:18215690`, cached abstract-only in-repo) describe an alpha/beta-hydrolase domain with a `Ser-His-Asp-Ser` catalytic tetrad (whose sequence-derived canonical alpha/beta-hydrolase charge-relay triad positions in `P75736` are nucleophilic `Ser89`, `beta-6` `Asp113`, and `His234`, alongside oxyanion loop `23-HGLFG-27`) plus helical-cap substrate-anchoring residues `Arg123` and `Tyr208`—together with experimentally mapped active-site features of yeast Eat1 (`UniProtKB:P53208`, `FT ACT_SITE 115 / 139 / 302`) and human ABHD11 (`UniProtKB:Q8NFV4`, `sv=2`, 306 aa, `FT ACT_SITE 132 / 287`), identifies the canonical alpha/beta-hydrolase oxyanion loop (`beta-3`–`alpha-A`, `64-HGLFG-68` within `61-VFLHGLFGSK-70` in `Q8NFV4`) and catalytic triad at `beta-5` (`GxSxG` nucleophilic elbow; `GFSMG` in `EAT1`), `beta-6` (`Asp`/`Glu` charge-relay acid), and the `beta-8`–`alpha-F` loop (`His` general base), shown below with symmetric `[-4,+4]` 9-aa flanking windows:

{table_block}

- **Note on *C. elegans* `abhd-11.1` (`UniProtKB:O62202`, `PTHR46118:SF3`) oxyanion-loop variation**: At residues `41-VPGLFGTKEN-50` (`39-ILVPGLFGTK-48`), `abhd-11.1` retains the core `-GLFG-` oxyanion-loop backbone (`42-PGLFG-46`, where the backbone amide NH contributes to the oxyanion hole) alongside the complete `Ser114`–`Asp140`–`His267` charge-relay triad, although the canonical N-terminal histidine of `-HGLFG-` (`52-HGLFG-56` in sister paralog `abhd-11.2` `O45707`) is substituted by `Pro42`.
- **Note on `beta-6` triad acid vs cap-domain `FT ACT_SITE` homology call**: UniProt `Q8NFV4` (`FT ACT_SITE 228`, `Asp228` in `223-WRVNLDALT-231`), `Q8K4F5` (`229`, `Asp229` in `224-WRLNLDTLA-232`), `Q6DRD9` (`238`, `Glu238` in `233-WRINLESIS-241`), and `O94437` (`190`, `Glu190` in `185-FRVPIELIS-193`) carry an automated `ECO:0000250` homology projection in the cap/core linker region, whereas family-wide sequence alignment with *E. coli* YbfF (`UniProtKB:P75736` `Asp113`, `PDB:3BF7`, `PMID:18215690`) and *S. cerevisiae* Eat1 (`FT ACT_SITE 139`) identifies the conserved `beta-6` aspartate/glutamate (`Asp156` in human `Q8NFV4`, `Asp113` in `P75736`, `Asp139` in `P53208`, `Glu176` in `P53219`) as the conserved triad carboxylate; the `FT ACT_SITE 228`-aligned position is non-acidic in *E. coli* YbfF (`Pro176` in `171-WRFNVPVLW-179`), *Drosophila* `CG2059` (`His225` in `220-WACNAHVLR-228`), and *C. elegans* `abhd-11.2` (`Asn220` in `215-WKININTID-223`).

## 3. Human `ABHD11` (`UniProtKB:Q8NFV4`) Sequence Version and Isoform Coordinate Crosswalk

- **`Q8NFV4` `sv=1` (historical 315-aa canonical precursor used in `PMID:32792488` and `PMID:40664791`)**: Contained a 9-residue N-terminal translation-initiation extension (`SEQUENCE CAUTION` in `ABHD11-uniprot.txt`); oxyanion motif at `73-HGLFG-77`, catalytic nucleophile numbered `Ser141`, `beta-6` acid `Asp165`, and catalytic histidine `His296` (`S141A` and `H296A` mutants in `PMID:32792488` and `PMID:40664791`).
- **`Q8NFV4` `sv=2` (current 306-aa canonical isoform 1 `Q8NFV4-1`)**: 9-aa N-terminal artifact trimmed (`-9` shift relative to `sv=1`); oxyanion motif at `64-HGLFG-68` (`61-VFLHGLFGSK-70`) and catalytic triad at `Ser132` (`130-GHSMG-134`), `Asp156` (`152-LIAVDISPV-160`), and `His287` (`283-PNAGHWIHA-291`) (`FT ACT_SITE 132`, `FT ACT_SITE 287`, `FT MUTAGEN 132`, `FT MUTAGEN 287` in `ABHD11-uniprot.txt`).
- **`Q8NFV4-4` (`sv=2` 299-aa isoform 4; historically 308-aa isoform 2/D lacking `VAR_SEQ 42..48`, `-7` shift relative to `Q8NFV4-1`)**: Lacks 7 residues in the N-terminal presequence/disordered region (`57-HGLFG-61`, `Ser125`, `Asp149`, `His280` in `sv=2`; `Ser134`, `His289` in historical 308-aa numbering). Used as the yeast two-hybrid ORF clone in HuRI (`PMID:32296183`).
- **Recombinant mature human ABHD11 (`residues 37..306` of `sv=2` / `46..315` of `sv=1`, 270 aa used in `PMID:32579589`)**: Lacks the 36-aa N-terminal mitochondrial transit peptide (`-36` shift relative to `Q8NFV4-1` `sv=2`), numbering the oxyanion motif `28-HGLFG-32`, nucleophile `Ser96`, `beta-6` acid `Asp120`, and histidine `His251`.
"""


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    repo_root = out_dir.parents[3]
    seq_cache = SequenceCache(repo_root / ".cache" / "uniprot_seq")

    rows: list[dict[str, str | int]] = []
    seqs: dict[str, str] = {}

    for spec in MEMBERS:
        if spec.uniprot_relpath is not None:
            seq, sv = parse_uniprot_flatfile(repo_root / spec.uniprot_relpath)
            source_label = spec.uniprot_relpath
        else:
            seq, sv, source_label = load_cached_or_remote_sequence(seq_cache, spec.accession)
        seqs[spec.accession] = seq
        rows.append(extract_member_motifs(spec, seq, sv, source_label))

    verify_auxiliary_claims(seqs)

    tsv_fields = [
        "accession",
        "gene_symbol",
        "organism",
        "subfamily",
        "length",
        "sequence_version",
        "oxyanion_motif",
        "oxyanion_context",
        "nucleophile",
        "nucleophile_window",
        "catalytic_acid",
        "catalytic_acid_window",
        "general_base_his",
        "general_base_window",
        "status",
        "sequence_source",
    ]
    tsv_path = out_dir / "motif_table.tsv"
    with tsv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=tsv_fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    results_path = out_dir / "RESULTS.md"
    results_path.write_text(render_results_md(rows), encoding="utf-8")
    print(f"Wrote {len(rows)} verified member rows to {tsv_path.relative_to(repo_root)} and {results_path.relative_to(repo_root)}")


if __name__ == "__main__":
    main()
