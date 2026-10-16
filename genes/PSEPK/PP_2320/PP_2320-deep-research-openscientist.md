---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-01T00:43:44.372824'
end_time: '2026-09-01T01:01:24.711884'
duration_seconds: 1060.34
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: PP_2320
  gene_symbol: PP_2320
  uniprot_accession: Q88KH0
  protein_description: 'RecName: Full=L,D-TPase catalytic domain-containing protein
    {ECO:0000259|PROSITE:PS52029};'
  gene_info: OrderedLocusNames=PP_2320 {ECO:0000313|EMBL:AAN67933.1};
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the YkuD family.
  protein_domains: LD-transpeptidase. (IPR050979); LD_TPept_cat_dom. (IPR005490);
    LysM. (IPR018392); Transpep_catalytic_dom. (IPR038063); YkuD (PF03734)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: PP_2320-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: PP_2320-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88KH0
- **Protein Description:** RecName: Full=L,D-TPase catalytic domain-containing protein {ECO:0000259|PROSITE:PS52029};
- **Gene Information:** OrderedLocusNames=PP_2320 {ECO:0000313|EMBL:AAN67933.1};
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the YkuD family.
- **Key Domains:** LD-transpeptidase. (IPR050979); LD_TPept_cat_dom. (IPR005490); LysM. (IPR018392); Transpep_catalytic_dom. (IPR038063); YkuD (PF03734)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PP_2320" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PP_2320' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PP_2320** (gene ID: PP_2320, UniProt: Q88KH0) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation of PP_2320 (Q88KH0), a YkuD-family L,D-transpeptidase of *Pseudomonas putida* KT2440

**Gene:** PP_2320 (OrderedLocusName; EMBL AAN67933.1) · **UniProt:** Q88KH0 · **Organism:** *Pseudomonas putida* KT2440 (ATCC 47054 / DSM 6125 / NCIMB 11950) · **Protein:** L,D-transpeptidase (YkuD family), 325 aa

---

## Summary

**PP_2320 (UniProt Q88KH0) is a periplasmic, Sec-secreted cysteine-active-site L,D-transpeptidase (LDT) of the YkuD family whose primary function is to covalently anchor the major outer-membrane lipoprotein OprI to the peptidoglycan (PG) sacculus, thereby tethering the outer membrane to the cell wall and maintaining envelope integrity.** The enzyme catalyzes an L,D-transpeptidation reaction: its catalytic cysteine (Cys209) attacks a donor PG peptide stem to form a thioacyl-enzyme intermediate, which is then resolved by the ε-amino group of a C-terminal lysine of OprI (Lys83 in the experimentally characterized ortholog), forming an amide (isopeptide) bond that links OprI — and hence the outer membrane — to the cell wall. This is a **protein-anchoring** transpeptidation, mechanistically distinct from the 3-3 (*meso*-DAP–*meso*-DAP) peptidoglycan cross-linking performed by other LDTs.

This functional assignment rests on three converging lines of evidence. First, sequence and domain analysis confirms PP_2320 is a *bona fide* LDT: it carries an intact catalytic Cys209/His207 dyad within the diagnostic YkuD "S-H-G-C" motif, an N-terminal Sec signal peptide directing it to the periplasm, a LysM peptidoglycan-binding module, and the full YkuD catalytic domain (Pfam PF03734). Second, comparative genomics establishes PP_2320 as the reciprocal-best-hit ortholog (76.3% amino-acid identity) of *Pseudomonas aeruginosa* PA2854/LdtPae2 — the enzyme experimentally proven, both *in vivo* and by *in vitro* reconstitution with solved crystal structures, to perform exactly this OprI-to-peptidoglycan anchoring reaction. Third, the substrate is conserved in *P. putida*: OprI is encoded in the same genome (PP_2322, Q88KG8), and its C-terminal acceptor lysine (Lys83) is conserved between the two species, supporting direct transfer of the PA2854 substrate specificity to PP_2320.

The enzyme operates extracytoplasmically, in the periplasm at the peptidoglycan layer, within the cell-wall biogenesis / peptidoglycan-maturation pathway, and performs a non-redundant structural role in envelope architecture. Because PP_2320 has not itself been the subject of a dedicated experimental study, this report is explicit that the assignment is a high-confidence orthology-based inference rather than a direct experimental demonstration in *P. putida*.

---

## Gene/Protein Identity Verification

All mandatory identity checks passed:

| Verification item | Result |
|---|---|
| UniProt accession | Q88KH0 |
| Gene / locus | PP_2320 (OrderedLocusName), *Pseudomonas putida* KT2440 |
| Protein length | 325 aa |
| Protein description | L,D-transpeptidase catalytic domain-containing protein |
| Organism | *Pseudomonas putida* KT2440 — confirmed |
| Family | YkuD family — confirmed (Pfam PF03734) |
| Key domains | LysM (IPR018392) + YkuD/LD_TPept_cat_dom (IPR005490, PF03734) — confirmed |

The gene symbol, organism, family, and domain architecture from UniProt are internally consistent and consistent with the literature identified. PP_2320 is an ordered-locus identifier unique to *P. putida* KT2440, so there is no gene-symbol ambiguity. The characterized literature describes the correct protein family (YkuD LDTs) and, critically, the experimentally characterized ortholog PA2854 in the closely related *P. aeruginosa*. No conflicting literature for a different gene under the same symbol was encountered.

---

## Molecular Identity and Domain Architecture

Direct analysis of the UniProt Q88KH0 sequence and InterPro/CDD annotation gives the architecture (N→C):

| Region (residues) | Feature | Source |
|---|---|---|
| 1–25 | **Sec signal peptide** (cleaved; no lipobox — mature protein has only one Cys) | UniProt feature |
| 40–86 | **LysM domain** (peptidoglycan-binding module; IPR018392) | InterPro/CDD |
| 98–233 | **YkuD / L,D-transpeptidase catalytic domain** (Pfam PF03734; PROSITE PS52029; Gene3D 2.40.440.10; SUPFAM SSF141523) | InterPro |
| Cys209 (in **S-H-G-C** motif) | **Catalytic nucleophile**, paired with general-base **His207** | Sequence analysis |

The protein contains a **single cysteine (Cys209)**, located in the diagnostic YkuD "SHGC" motif (…GIGMRT**SHGC**FRM…). This is the canonical **Cys/His catalytic dyad** of L,D-transpeptidases — a chemistry mechanistically distinct from the Ser-based D,D-transpeptidases (penicillin-binding proteins, PBPs). The **LysM + YkuD** architecture places PP_2320 in the **lipoprotein-anchoring LDT clade** (equivalent to *E. coli* LdtA/LdtB/LdtC = ErfK/YbiS/YcfS), as opposed to the Ig-domain–containing 3-3 cross-linking clade (LdtD/LdtE).

---

## Key Findings

### Finding 1 — PP_2320 is a Sec-secreted YkuD-family L,D-transpeptidase with an intact catalytic Cys209–His207 dyad

PP_2320 encodes a 325-amino-acid protein with the hallmark architecture of an active L,D-transpeptidase. It has an N-terminal Sec signal peptide (residues 1–25, cleavage before Leu26) with **no lipobox** — indeed the entire protein contains only one cysteine — indicating the mature protein is exported as a soluble periplasmic enzyme rather than being lipid-anchored. The YkuD catalytic domain (residues ~98–233) is assigned by Pfam (PF03734), PROSITE (PS52029), Gene3D (2.40.440.10), and SUPFAM (SSF141523).

The sole cysteine, **Cys209**, sits within the diagnostic YkuD "S-H-G-C" motif and constitutes the catalytic nucleophile, paired with the general-base histidine **His207** to form the canonical Cys/His dyad shared by all L,D-transpeptidases. InterPro assigns the full complement of LDT signatures (IPR005490, IPR038063, IPR050979) plus a **LysM** peptidoglycan-binding module (IPR018392). The presence of the family is directly supported: "*Some bacterial peptidoglycans also contain 3-3 cross-links that are formed by another class of enzymes called L,D-transpeptidases which contain a YkuD catalytic domain*" [PMID: 38006948](https://pubmed.ncbi.nlm.nih.gov/38006948/). The intact (non-degenerate) catalytic motif indicates PP_2320 is very likely an enzymatically active LDT rather than a pseudo-enzyme.

### Finding 2 — Reaction class: L,D-transpeptidation of the peptidoglycan stem, with protein or muropeptide acceptors

At the family level, YkuD L,D-transpeptidases operate by a defined mechanism: they cleave the *meso*-DAP(position 3)–D-Ala(position 4) bond of a tetrapeptide donor stem, form a covalent thioacyl-enzyme intermediate on the catalytic cysteine, and transfer the *meso*-DAP(3) carbonyl to an acceptor amine. Two physiological acceptor classes are documented in γ-proteobacteria: (i) the side-chain amine of *meso*-DAP in an acceptor PG stem, generating **3-3 cross-links**; or (ii) the C-terminal lysine of a **lipoprotein** (classically Braun's lipoprotein, Lpp), producing a covalent outer-membrane–PG tether.

This duality is directly documented: in *E. coli*, "*Ldt(fm) homologues are responsible for the attachment of the Braun lipoprotein to murein, indicating that evolutionarily related domains have been tailored to use muropeptides or proteins as acyl acceptors in the L,D-transpeptidation reaction*" [PMID: 17369299](https://pubmed.ncbi.nlm.nih.gov/17369299/). PP_2320 carries the conserved catalytic Cys209 and the complete YkuD domain required for either reaction; the orthology and substrate analyses below (Findings 4–8) resolve it firmly into the **protein-anchoring** (lipoprotein-acceptor) subclass.

### Finding 3 — Localization and pathway: a periplasmic cell-envelope enzyme acting independently of penicillin-binding proteins

The cleaved N-terminal Sec signal peptide without a lipobox indicates the mature enzyme is exported to the **periplasm**, precisely where the PG sacculus resides. UniProt GO assignments are consistent: cellular component "extracellular region" (GO:0005576, reflecting export beyond the cytoplasm); molecular function "peptidoglycan L,D-transpeptidase activity" (GO:0071972); and biological processes "cell wall organization" (GO:0071555), "peptidoglycan-protein cross-linking" (GO:0018104), and "regulation of cell shape" (GO:0008360). UniProt PATHWAY: "Cell wall biogenesis; peptidoglycan biosynthesis."

Functionally, L,D-transpeptidases use Cys-based chemistry **independent of the D,D-transpeptidase PBPs** and are therefore intrinsically insensitive to most β-lactams: "*Penicillin-binding proteins (PBPs) synthesize essential 4-3 cross-links in PG and are inhibited by β-lactam antibiotics*" [PMID: 30275297](https://pubmed.ncbi.nlm.nih.gov/30275297/). This contrast frames the PBP-independent pathway in which PP_2320 acts. As an anchoring (not cross-linking) LDT, PP_2320's main contribution is to envelope integrity via OM tethering rather than to β-lactam bypass per se.

### Finding 4 — PP_2320 is the *P. putida* ortholog (76% identity) of PA2854, the OprI-anchoring L,D-transpeptidase

A Needleman–Wunsch global alignment between PP_2320/Q88KH0 (325 aa) and *P. aeruginosa* PAO1 PA2854/Q9HZZ0 (323 aa) yields **245/321 identical positions = 76.3% identity** (75.4% over the full PP_2320 length). The two proteins share an identical domain architecture (Sec signal → LysM PG-binding domain → YkuD catalytic domain) and a single catalytic cysteine in the SHGC motif (Cys209 in PP_2320; Cys207 in PA2854).

PA2854 is experimentally characterized: El-Araby et al. (2026) identified it as the catalyst that covalently tethers OprI to peptidoglycan in live *P. aeruginosa*: "*We document that the gene product of PA2854 is the catalyst that performs this transformation between the cell wall and the outer-membrane lipoprotein OprI in live [P. aeruginosa]*" [PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/). The **LysM** accessory domain (rather than Ig-like) places both proteins in the lipoprotein-anchoring LDT clade, distinct from the Ig-domain 3-3 cross-linking clade. The broader family context — "*l,d-transpeptidases (LDTs), which are dispensable for growth in most bacterial species and whose physiological functions remain elusive*" [PMID: 37255442](https://pubmed.ncbi.nlm.nih.gov/37255442/) — underscores that individual paralogs carry specialized functions best defined through the closest characterized ortholog.

### Finding 5 — Reciprocal-best-hit orthology confirms PP_2320 ↔ PA2854; *P. putida* KT2440 has only two LDTs

A genome-wide survey (Pfam PF03734) finds exactly **two** L,D-transpeptidases in *P. putida* KT2440: **PP_2320** (325 aa) and **PP_1451** (184 aa). *P. aeruginosa* PAO1 has three: PA3756 (166 aa), PA2854 (323 aa), and PA0732 (347 aa). Pairwise identities resolve the orthology unambiguously:

| Query | vs PA3756 (166 aa) | vs **PA2854 (323 aa, LdtPae2, OprI anchor)** | vs PA0732 (347 aa) |
|---|---|---|---|
| **PP_2320** | 46.4% | **76.3%** ⭐ | 30.9% |
| PP_1451 | 66.3% ⭐ | 43.7% | 42.9% |

PP_2320 best-matches PA2854 at 76.3%, and PA2854 best-matches PP_2320 (over PP_1451 at 43.7%) — a clean **reciprocal best hit**. PP_2320 is therefore the dedicated ortholog of the experimentally characterized OprI-anchoring enzyme and the **only long, LysM-containing (lipoprotein-anchoring-clade) LDT in *P. putida***. PP_1451 is instead the reciprocal ortholog of PA3756 (66.3%), while PA0732 has no *P. putida* ortholog above ~30%. The two *P. putida* LDTs thus likely divide labor: PP_2320 = OprI anchoring; PP_1451 = a cross-linking/other LDT. This assignment is consistent with the experimentally validated PA2854 function [PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/).

### Finding 6 — The OprI substrate lipoprotein is encoded in *P. putida* KT2440 (PP_2322), near the PP_2320 gene

For the anchoring function to operate, the substrate must be present. UniProt confirms *P. putida* KT2440 encodes OprI: **Q88KG8, gene *oprI* = PP_2322, 83 aa, "Major outer membrane lipoprotein"** (the *Pseudomonas* analog of Braun's lipoprotein/Lpp), plus the peptidoglycan-associated lipoprotein Pal/OprL (PP_1223). The anchoring enzyme PP_2320 and its substrate *oprI* (PP_2322) map to the **same local genomic region** (PP_2319 uncharacterized 106 aa; PP_2320 LDT; PP_2321; PP_2322 *oprI*). This proximity is suggestive of a functional relationship but is **not** conserved in *P. aeruginosa* (where PA2854 lies distant from *oprI*, PA0973), so it is corroborative rather than a defined operon.

### Finding 7 — Precise reaction: PP_2320 links the ε-amino group of OprI Lys83 to the peptidoglycan peptide stem, non-redundantly for envelope integrity

The definitive mechanistic detail comes from the *P. aeruginosa* studies. El-Araby et al. (2026, *J. Am. Chem. Soc.*) reconstituted the reaction *in vitro* with purified recombinant PA2854, OprI, and synthetic peptidoglycan, and confirmed it in live cells, documenting attachment of the **side-chain ε-amino group of Lys83 of OprI** to the **peptide stem of peptidoglycan** [PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/). The enzyme turns over both non-cross-linked and cross-linked peptidoglycan as substrate. X-ray structures were solved for trimeric OprI (2.1 Å) and PA2854 (2.63 Å; three domains that bind both PG and OprI). The anchoring is **non-redundant**: "*anchoring of the outer membrane to the cell wall catalyzed by PA2854 does not appear to be a redundant reaction*" [PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/), and its loss yields a weakened envelope prone to disruption.

The companion study (Hugonneau-Beaufet et al., 2023) assigned the three *P. aeruginosa* LDTs by gene inactivation: "*the three P. aeruginosa LDTs catalyze peptidoglycan cross-linking (LdtPae1), the anchoring of lipoprotein OprI to the peptidoglycan (LdtPae2), and the hydrolysis of the resulting peptidoglycan-OprI amide bond (LdtPae3)*" [PMID: 37255442](https://pubmed.ncbi.nlm.nih.gov/37255442/). This places OprI anchoring specifically with **LdtPae2 = PA2854**, the ortholog of PP_2320 — establishing it as the anchoring enzyme, not the cross-linker or the hydrolase. The same study demonstrated the pathway's physiological importance: "*deletion of each of the ldt genes impaired biofilm formation and potentiated the bactericidal activity of EDTA*" [PMID: 37255442](https://pubmed.ncbi.nlm.nih.gov/37255442/), with anchoring dynamically controlled by opposing LdtPae2/LdtPae3 activities and increasing in biofilm growth.

### Finding 8 — The OprI acceptor lysine (Lys83) is conserved in *P. putida*, supporting substrate-specificity transfer

Substrate conservation completes the inference chain. *P. putida* KT2440 OprI (PP_2322, Q88KG8) is 83 aa and terminates in **Lys83** (…ANERALRMLDKASR-**K**); *P. aeruginosa* OprI (P11221) is likewise 83 aa terminating in **Lys83** (…ANERALRMLEKASR-**K**), with identical lysine positions (6, 25, 51, 61, 79, 83) and a conserved N-terminal lipobox cysteine (residue 20). Because the ε-amino group of OprI Lys83 is the experimentally demonstrated acyl acceptor in *P. aeruginosa* [PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/), and this C-terminal acceptor lysine is conserved in the *P. putida* substrate, the substrate specificity of the reaction is expected to transfer directly to PP_2320.

---

## Mechanistic Model / Interpretation

Integrating all eight findings produces a coherent model. PP_2320 is synthesized with an N-terminal Sec signal peptide, exported across the inner membrane, and released as a soluble periplasmic protein. Its LysM domain engages the peptidoglycan sacculus and positions the YkuD catalytic domain for reaction. The catalytic Cys209, activated by the general-base His207, attacks the *meso*-DAP–D-Ala peptide bond of a tetrapeptide PG stem, releasing the terminal D-Ala and forming a thioacyl-enzyme intermediate. The activated *meso*-DAP carbonyl is then transferred to the acceptor — the ε-amino group of Lys83 at the C-terminus of the outer-membrane lipoprotein OprI — forming a covalent amide (isopeptide) bond that tethers the outer membrane to the cell wall.

```
        OUTER MEMBRANE
   ┌─────────────────────────────┐
   │  OprI (PP_2322, lipoprotein) │  N-term lipobox Cys → OM lipid anchor
   │        …Lys83–NH2 (ε)        │─────────┐
   └─────────────────────────────┘         │  covalent amide (isopeptide) bond
                                            │  formed by PP_2320
        PERIPLASM                           ▼
   ┌─────────────────────────────────────────────────┐
   │  PP_2320 (Q88KH0)  Sec-exported LDT              │
   │   [LysM PG-binding] + [YkuD  Cys209/His207]      │
   │        │ acyl-donor: PG meso-DAP stem            │
   │        ▼                                         │
   │  PEPTIDOGLYCAN  ...–meso-DAP(3)–|–D-Ala(4)        │
   │                     (D-Ala released)             │
   └─────────────────────────────────────────────────┘
        INNER MEMBRANE
```

**Reaction:**
> PG donor stem (…–mDAP³–D-Ala⁴) + OprI(Lys-ε-NH₂) → PG–mDAP³–(ε)Lys-OprI amide + D-Ala⁴

This model differs importantly from the "textbook" LDT function of forming 3-3 peptidoglycan cross-links. PP_2320 belongs to the **protein-anchoring** subclass, using a lipoprotein rather than a muropeptide as the acyl acceptor; the LysM (rather than Ig-like) accessory domain is the structural signature of this clade. The reaction is part of a dynamic, reversible system: in *P. aeruginosa*, anchoring by LdtPae2 is counteracted by the hydrolase LdtPae3, allowing tuning of OM–PG connectivity by growth state (notably increasing in biofilms). Whether *P. putida* possesses a dedicated LdtPae3-type hydrolase is unresolved — its second LDT, PP_1451, is the short LdtPae1-clade ortholog, not an LdtPae3 ortholog.

Physiologically this is a **structural, envelope-stabilizing** role, not a metabolic or signaling one. It parallels the classic Braun's lipoprotein–PG system of *E. coli* and analogous β-barrel and inner-membrane-protein tethers documented across Gram-negatives, all of which maintain the outer membrane as an impermeable barrier and preserve envelope mechanical integrity.

### Confidence assessment

| Claim | Evidence type | Confidence |
|---|---|---|
| PP_2320 is an active LDT (Cys/His dyad, YkuD domain) | Direct sequence/domain analysis | Very high |
| PP_2320 is periplasmic (Sec signal, no lipobox) | Sequence analysis + GO | High |
| PP_2320 catalyzes L,D-transpeptidation | Family enzymology + domain | Very high |
| PP_2320 anchors OprI to PG (specific function) | Orthology (76.3% RBH) to experimentally proven PA2854 | High (inferred) |
| Acceptor = OprI Lys83 ε-amino; donor = PG stem | Experimental in ortholog + substrate conservation | High (inferred) |
| Non-redundant envelope role | Experimental in ortholog | Moderate–high (inferred) |

---

## Evidence Base

| PMID | Title (abbreviated) | Role in this report |
|---|---|---|
| [42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/) | *Outer Membrane–Peptidoglycan Anchoring in [Pseudomonas]* | **Keystone.** Experimentally proves PA2854 (76.3% ortholog of PP_2320) anchors OprI Lys83 ε-amino to the PG stem; provides crystal structures and demonstrates non-redundancy. Basis for Findings 4–8. |
| [37255442](https://pubmed.ncbi.nlm.nih.gov/37255442/) | *Characterization of P. aeruginosa l,d-Transpeptidases…biofilm* | Assigns the three *P. aeruginosa* LDTs by gene inactivation; identifies LdtPae2 (=PA2854) as the OprI anchoring enzyme and documents biofilm/EDTA phenotypes. Supports Findings 4 and 7. |
| [17369299](https://pubmed.ncbi.nlm.nih.gov/17369299/) | *Identification of the L,D-transpeptidases…Braun lipoprotein to E. coli PG* | Establishes that YkuD LDTs can use either muropeptides or lipoproteins as acyl acceptors — the mechanistic precedent for protein anchoring. Supports Finding 2. |
| [38006948](https://pubmed.ncbi.nlm.nih.gov/38006948/) | *Unusual 1-3 PG cross-links…YkuD domains* | Confirms that YkuD-domain enzymes are L,D-transpeptidases acting on peptidoglycan. Supports Findings 1–2. |
| [30275297](https://pubmed.ncbi.nlm.nih.gov/30275297/) | *Copper inhibits PG LD-transpeptidases…bypass of PBPs* | Frames the PBP-independent (β-lactam-insensitive) nature of the LDT pathway. Supports Finding 3. |
| [40681671](https://pubmed.ncbi.nlm.nih.gov/40681671/) | *An inner membrane protein covalently attached to PG in Dickeya dadantii* | Broader context: LDTs anchor diverse proteins (not only Lpp) to PG in γ-proteobacteria; anchoring sequences are portable. |
| [33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/) | *DpaA Detaches Braun's Lipoprotein from Peptidoglycan* | Context for the reversible/dynamic nature of lipoprotein-PG anchoring (hydrolase counterpart). |
| [33139883](https://pubmed.ncbi.nlm.nih.gov/33139883/) / [33139884](https://pubmed.ncbi.nlm.nih.gov/33139884/) | *β-Barrel proteins tether the OM…* | Context: covalent OM–PG tethering is a widespread envelope-integrity strategy. |
| [23123904](https://pubmed.ncbi.nlm.nih.gov/23123904/) | *Role of P. aeruginosa PG-associated OM proteins in vesicle formation* | Shows OprI tethers OM to PG and influences OM vesicle formation, corroborating OprI's structural anchoring role. |

The evidence base is unusually strong for a "hypothetical" locus because a very recent high-resolution study ([PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/)) directly characterized the close ortholog PA2854, combined with an earlier genetic study ([PMID: 37255442](https://pubmed.ncbi.nlm.nih.gov/37255442/)) that assigned OprI anchoring to that same enzyme. No reviewed paper contradicts the functional assignment. The principal caveat is that all direct experimental data are from *P. aeruginosa*; transfer to *P. putida* is by orthology and substrate conservation.

---

## Supported and Refuted Hypotheses

**Supported**
- PP_2320 is a catalytically competent YkuD/L,D-transpeptidase (intact Cys209/His207 dyad). *(Sequence/InterPro)*
- PP_2320 is the OprI-anchoring LDT of *P. putida* (ortholog of PA2854/LdtPae2, 76.3% reciprocal best hit). *(Orthology + transferred experiment)*
- The reaction links a PG peptide stem to the ε-amino group of an OprI C-terminal Lys; the enzyme is periplasmic; its role is OM–PG tethering / envelope integrity. *(El-Araby 2026; Hugonneau-Beaufet 2023)*

**Refuted / de-prioritized**
- PP_2320 is **not** best assigned as a PG **3-3 cross-linker** (that clade carries Ig-like, not LysM, domains; the *P. putida* cross-linking role more likely falls to PP_1451).
- PP_2320 is **not** the OprI-**detaching** hydrolase (LdtPae3/DpaA-type).

---

## Limitations and Knowledge Gaps

1. **No direct experimental study of PP_2320 itself** exists; the functional assignment is a high-confidence orthology-based inference (76.3% RBH to experimentally characterized PA2854/LdtPae2) plus domain architecture — not direct proof in *P. putida*.
2. **In vivo confirmation of OprI anchoring in *P. putida* is lacking.** It remains formally unproven that *P. putida* OprI is covalently attached to PG, or that PP_2320 is responsible in this organism.
3. **Acceptor promiscuity not excluded.** LDTs can accept multiple substrates; PP_2320 could in principle also anchor other periplasmic/OM proteins (as OutB is anchored in *Dickeya* [PMID: 40681671](https://pubmed.ncbi.nlm.nih.gov/40681671/)) or contribute minor 3-3 cross-linking.
4. **No identified hydrolase counterpart in *P. putida*.** PA0732/LdtPae3 has no clear *P. putida* ortholog above ~30%; how (or whether) *P. putida* reverses OprI anchoring is unknown.
5. **Structural inference only.** PP_2320's own structure is undetermined; domain boundaries and the LysM assignment rest on bioinformatic prediction and homology to PA2854.
6. **Genomic adjacency of PP_2320 and *oprI* is not conserved** in *P. aeruginosa*, so the proximity should not be over-interpreted as regulatory coupling.

---

## Proposed Follow-up Experiments / Actions

1. **Muropeptide / PG–protein linkage analysis in *P. putida* KT2440.** Isolate PG sacculi and use LC-MS/MS to detect OprI-Lys83–PG amide adducts directly, in wild-type versus a ΔPP_2320 deletion mutant. This is the single most decisive experiment.
2. **Construct a PP_2320 deletion (and catalytic Cys209→Ala) mutant** and assay for: loss of covalent OprI–PG linkage; envelope-integrity phenotypes (EDTA/detergent/antibiotic sensitivity, OM blebbing/vesiculation); and biofilm formation. Complementation with wild-type but not Cys209Ala confirms catalytic dependence.
3. **In vitro reconstitution** with purified recombinant PP_2320, *P. putida* OprI (PP_2322), and native/synthetic PG, mirroring the PA2854 assay [PMID: 42100858](https://pubmed.ncbi.nlm.nih.gov/42100858/), to demonstrate direct catalysis and measure kinetics/specificity.
4. **Test acceptor promiscuity.** Screen whether PP_2320 can anchor other periplasmic proteins (e.g., an engineered PG-anchoring reporter, as for OutB in *Dickeya* [PMID: 40681671](https://pubmed.ncbi.nlm.nih.gov/40681671/)) and quantify any residual 3-3 cross-linking.
5. **Search for a hydrolase counterpart** that reverses OprI anchoring (functional analog of LdtPae3/DpaA [PMID: 33947763](https://pubmed.ncbi.nlm.nih.gov/33947763/)); test whether anchoring is dynamically regulated with growth phase/biofilm.
6. **Experimental structure determination** (X-ray or cryo-EM) of PP_2320, ideally as a covalent complex with OprI and a PG-stem mimic.

---

## Conclusion

PP_2320 (Q88KH0) of *Pseudomonas putida* KT2440 is a periplasmic, Sec-secreted YkuD-family L,D-transpeptidase with an intact Cys209/His207 catalytic dyad and a LysM peptidoglycan-binding domain. Its primary function is to covalently anchor the major outer-membrane lipoprotein OprI to the peptidoglycan sacculus by transpeptidation — joining a peptidoglycan *meso*-DAP peptide stem (acyl donor) to the ε-amino group of OprI Lys83 (acyl acceptor) — thereby tethering the outer membrane to the cell wall and maintaining envelope integrity. This assignment is grounded in strong reciprocal-best-hit orthology (76.3% identity) to the experimentally validated *P. aeruginosa* enzyme PA2854/LdtPae2, together with conservation of the OprI substrate and its acceptor lysine in *P. putida*. Direct experimental confirmation in *P. putida* remains the key outstanding step.

---

## References

- El-Araby AM, *et al.* **Outer Membrane–Peptidoglycan Anchoring in *Pseudomonas aeruginosa*.** *J Am Chem Soc.* 2026. PMID **42100858**.
- Hugonneau-Beaufet I, *et al.* **Characterization of *Pseudomonas aeruginosa* l,d-Transpeptidases and Evaluation of Their Role in Peptidoglycan Adaptation to Biofilm Growth.** *Microbiol Spectr.* 2023. PMID **37255442**.
- Magnet S, *et al.* **Identification of the L,D-transpeptidases responsible for attachment of the Braun lipoprotein to *Escherichia coli* peptidoglycan.** *J Bacteriol.* 2007. PMID **17369299**.
- Peters K, *et al.* **Copper inhibits peptidoglycan LD-transpeptidases suppressing β-lactam resistance due to bypass of penicillin-binding proteins.** *PNAS* 2018. PMID **30275297**.
- Alamán-Zárate MG, *et al.* **Unusual 1-3 peptidoglycan cross-links in Acetobacteraceae are made by L,D-transpeptidases with a catalytic domain distantly related to YkuD domains.** 2024. PMID **38006948**.
- **An inner membrane protein is covalently attached to peptidoglycan in the γ-proteobacterium *Dickeya dadantii*.** 2025. PMID **40681671**.
- Winkle M, *et al.* **DpaA Detaches Braun's Lipoprotein from Peptidoglycan.** *mBio* 2021. PMID **33947763**.
- (Databases) UniProt Q88KH0; Q88KG8 (OprI, PP_2322); InterPro IPR005490 / IPR018392 / IPR050979; Pfam PF03734.


## Artifacts

- [OpenScientist final report](PP_2320-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](PP_2320-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:38006948
2. PMID:17369299
3. PMID:30275297
4. PMID:42100858
5. PMID:37255442
6. PMID:40681671
7. PMID:33947763