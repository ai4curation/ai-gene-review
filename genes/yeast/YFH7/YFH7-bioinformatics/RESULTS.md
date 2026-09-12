# YFH7 (P43591 / YFR007W) — bioinformatics analysis

**Target:** *Saccharomyces cerevisiae* YFH7 (UniProt P43591; ORF YFR007W; alias AIM12),
a 353-aa protein annotated as an "ATP-dependent kinase" (EC 2.7.1.-), with a solved
crystal structure (PDB **2GA8** at 1.77 Å, **2GAA** at 1.95 Å; Gueguen-Chaignon et al.
2008, PMID:18004758).

**Question addressed:** Is YFH7 a structurally intact, plausibly catalytically-competent
small-molecule (P-loop) kinase, what is its domain architecture, and how broadly is it
conserved?

## Methods (reproducible)

All steps are driven by the `justfile`; scripts read sequence/accession from
arguments (nothing gene-specific is hardcoded). Dependencies are managed with `uv`
(`pyproject.toml`).

| Step | Script | Input | Output |
|---|---|---|---|
| Motif scan (Walker A/B, composition) | `analyze_motifs.py` | `YFH7.fasta` | `results_motifs.json` |
| Domain architecture + orthology xrefs | `analyze_domains_orthology.py` | accession `P43591` (UniProt + InterPro REST) | `results_domains.json` |
| Taxonomic span (UniRef50/90 clusters) | `analyze_conservation.py` | accession `P43591` (UniProt REST) | `results_conservation.json` |
| PRK/URK/PANK family motif comparison | `compare_urk_motifs.py` | `YFH7.fasta` + controls | `results_urk_compare.json` |

Run with `just all` (motifs offline; domains/conservation need network access to the
public EBI/UniProt REST APIs). Control tests: `just test-controls`.

## Findings

### 1. Walker A / P-loop motif — present and canonical

The classic P-loop (Walker A) glycine-rich loop is detected at **residues 31–38,
`GSPGSGKS(T)`**, matching the `[AG]-x(4)-G-K-[ST]` consensus and exactly the position
reported for the ATP-binding site in UniProt (BINDING 31..39) and in the crystal
structure. This is the ATP β/γ-phosphate–binding loop of P-loop NTPases/kinases.

### 2. Walker B / catalytic acidic residue — candidate present

The Walker-B heuristic (hydrophobic strand ending in D/E) yields three candidates; the
one consistent with a P-loop-kinase catalytic Mg²⁺-coordinating aspartate lies within
the downstream `VILEG` block (see point 4). The heuristic is weak on its own, but its
best candidate co-locates with the family's diagnostic second block, consistent with an
intact catalytic scaffold. (Walker B position is not pinned to a single residue by
sequence alone — noted as a limitation.)

### 3. Domain architecture — P-loop NTPase fold with a ~100-residue insertion

From UniProt + InterPro cross-references (`results_domains.json`):

- **IPR027417** P-loop containing nucleoside triphosphate hydrolase (homologous
  superfamily), spanning **1–353**.
- **Gene3D 3.40.50.300** / **SUPFAM SSF52540** — P-loop NTPase fold. The SUPFAM fold is
  reported in **three discontinuous segments (22–54, 156–204, 233–349)**, leaving a gap
  at ~**55–155**. This ~101-residue stretch is the **"additional α/β domain of novel
  topology" / ~100-residue insertion** described in the crystal paper — the feature that
  distinguishes YFH7 from canonical family members.
- **PANTHER PTHR10285** "URIDINE KINASE" / nucleoside-kinase domain, spanning 12–322.
- **CDD cd00009 (AAA)** mapped to 9–105 (the N-terminal core lobe).
- UniProt similarity comment: *"Belongs to the YFH7 family."*

This is fully consistent with the crystal-structure conclusion that YFH7 adopts the
**PRK/URK/PANK** (phosphoribulokinase / uridine kinase / pantothenate kinase) fold with
core, lid, and NMPbind subdomains plus a family-atypical insertion.

### 4. PRK/URK/PANK family signature — two diagnostic blocks retained

Comparing YFH7 against a bona fide family member, *E. coli* uridine kinase (Udk,
P0A8F4), both proteins carry the two diagnostic sequence blocks
(`results_urk_compare.json`):

| Block | YFH7 | *E. coli* Udk |
|---|---|---|
| Walker A P-loop `[AG]x₄GK[ST]` | `GSPGSGKS` @ 31 | `GASASGKS` @ 15 |
| URK second block `[IV][IV][IL]EG` | `VILEG` @ 263 | `IILEG` @ 115 |

Retention of **both** blocks indicates the small-molecule-kinase catalytic scaffold is
intact — i.e. YFH7 is not an obviously degenerate pseudokinase at the level of these
family fingerprints. (This is evidence for structural competence, not proof of in-vivo
catalysis or of any particular substrate.)

### 5. Orthology / conservation — ancient fold, budding-yeast-restricted protein

Two layers must be distinguished:

- **The fold/domain is ancient and pan-eukaryotic.** YFH7 belongs to eggNOG
  **KOG2702** (a eukaryotic orthologous group), OrthoDB group at the **Eukaryota**
  level (`...at2759`), has an InParanoid record, and maps to PANTHER **PTHR10285**
  (uridine-kinase family) — all indicating the P-loop kinase family it sits in is
  deeply conserved across eukaryotes (and, via the URK family, into bacteria).
- **The specific YFH7 protein is lineage-restricted.** Its **UniRef50 cluster (≥50 %
  identity) has a common taxon of *Saccharomycetaceae*** (23 members: *Saccharomyces*,
  *Vanderwaltozyma polyspora*, *Saccharomyces eubayanus/pastorianus*, etc.), and the
  UniRef90 cluster narrows to *Saccharomyces* sensu stricto (`results_conservation.json`).
  For comparison, the control protein **actin (ACT1, P60010) has a UniRef50 common taxon
  of *Eukaryota* (434 members)** — the expected signature of a broadly conserved protein.

**Interpretation:** YFH7 is a **budding-yeast-specific member of an ancient P-loop
small-molecule-kinase family**. This matches the crystal paper's description of a
"yeast-specific protein showing weak similarity" to the PRK/URK/PANK subfamily, with a
lineage-specific insertion. The specific in-vivo substrate is not determinable from
sequence/structure alone.

## Overall assessment

YFH7 is a **structurally intact P-loop (PRK/URK/PANK-fold) ATP-dependent small-molecule
kinase** with a canonical Walker A P-loop, retained family diagnostic blocks, and a
lineage-specific ~100-residue insertion. The evidence supports classifying it as a
**catalytically-plausible small-molecule kinase** (`kinase activity`; more specifically
consistent with a phosphotransferase acting on a small-molecule hydroxyl acceptor), but
**the physiological substrate is unknown** — the crystallographers could only conclude
"new substrate specificity," and no substrate has since been identified from sequence,
structure, or the analyses here. This is an **MF/BP substrate gap**, not a fold or
family-membership uncertainty.

## Checklist

- [x] Scripts do not use hardcoded inputs or outputs (sequence/accession are CLI args;
      verified by running on control sequences).
- [x] Scripts tested on at least one other input:
      - `analyze_motifs.py` / `compare_urk_motifs.py`: positive control *E. coli* Udk
        (P-loop + URK block detected) and negative control yeast histone H4 (neither
        detected).
      - `analyze_conservation.py`: control actin ACT1 (P60010) → Eukaryota-wide cluster,
        correctly contrasting with YFH7's yeast-restricted cluster.
- [x] Analyses completed as expected (all `just` steps run cleanly).
- [x] Direct results of the scripts are in the folder (`results_*.json`).
- [x] Summary includes provenance and justification; uncertainty (substrate identity,
      exact Walker B residue) is stated explicitly.
- [?] Walker B catalytic residue is a heuristic candidate only, not pinned to a single
      residue by sequence alone (would need structure-based residue mapping from PDB 2GA8).

## Data provenance / tools

- UniProt REST (`rest.uniprot.org`) — entry P43591, UniRef50/90 clusters.
- InterPro REST (`www.ebi.ac.uk/interpro`) — domain-to-protein mapping.
- Reference family member: *E. coli* uridine kinase Udk (P0A8F4).
- Control proteins: yeast actin ACT1 (P60010), yeast histone H4 (P02309).
- Structural/functional context: Gueguen-Chaignon et al. 2008, *Proteins* 71:804–812
  (PMID:18004758; PDB 2GA8, 2GAA).
- biopython 1.87, requests 2.34 (see `pyproject.toml` / `uv.lock`).
