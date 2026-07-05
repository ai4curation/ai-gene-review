# ILT1 (YDR090C / Q03193) — curation notes

Journal-style notes for the AI GO-annotation review of the *S. cerevisiae* dark gene **ILT1**.
Standard name ILT1 = "Ionic Liquid Tolerance 1"; systematic name **YDR090C**; UniProt **Q03193**;
SGD **S000002497**. SGD qualifier: **Verified** ORF.

## Identity / provenance

- ILT1 is the SGD standard name assigned in 2018 by Higgins et al.
  [PMID:30045857 "we identified SGE1 ... and a previously uncharacterized gene that we named ionic
  liquid tolerance 1 (ILT1), which encodes a predicted membrane protein"].
- SGD one-line description: "Protein of unknown function; deletion confers sensitivity to cationic
  compounds; green fluorescent protein (GFP)-fusion protein localizes to the plasma membrane."
- UniProt name: "Uncharacterized membrane protein YDR090C". Evidence level PE 1 (protein level).

## Sequence / domain reasoning (inline, from UniProt Q03193 record)

- 310 aa multi-pass membrane protein. UniProt models 6 TRANSMEM helices (topology from
  PubMed:12524434 / PubMed:16847258 C-terminal reporter-fusion topology studies); Higgins 2018
  cite a 7-transmembrane-helix prediction [PMID:30045857 "ILT1 encodes a membrane protein with
  seven transmembrane helices"]. Either way it is a polytopic ~6–7 TM integral membrane protein.
- **PQ-loop repeats**: UniProt annotates two PQ-loop domains (residues 5..69 and 138..194). Pfam
  PF04193 (PQ-loop), InterPro IPR006603 (PQ-loop_rpt), SMART SM00679 (CTNS, ×2). The PQ-loop /
  "MtN3/saliva" fold is a duplicated 3-TM unit typical of SWEET-like and PQ-loop transporters/
  sensors (e.g. cystinosin/CTNS, PQLC2, SWEETs, lysosomal amino-acid transporters).
- InterPro family **IPR051415 = LAAT-1** (Lysosomal/Vacuolar Amino Acid Transporter 1).
- PANTHER: family **PTHR16201** ("SEVEN TRANSMEMBRANE PROTEIN 1-RELATED" / LAAT-1);
  subfamily **PTHR16201:SF37** = "PQ-LOOP REPEAT-CONTAINING PROTEIN".

## Family / orthology reasoning — the key nuance for the IBA annotations

The GOA file carries four IBA (GO_Central / PAINT) annotations propagated from PTHR16201:
- GO:0005774 vacuolar membrane (C)
- GO:0015174 basic amino acid transmembrane transporter activity (F)
- GO:0034488 basic amino acid transmembrane export from vacuole (P)
- GO:0080144 intracellular amino acid homeostasis (P)

Inspecting the PANTHER PAINT table (`interpro/panther/PTHR16201/PTHR16201-paint.tsv`), these IBD
seeds are the **characterized members of *other* subfamilies**, not ILT1's own clade:
- SGD:S000005452 = **YPQ1** (YOL092W) — vacuolar membrane **lysine** exporter
- SGD:S000002760 = **YPQ2** (YDR352W) — vacuolar membrane **arginine** exporter
- SGD:S000000351 = **RTC2/YPQ3** (YBR147W) — putative vacuolar cationic-amino-acid transporter
- WB:WBGene00021546 = *C. elegans* **LAAT-1** (lysosomal cationic amino acid transporter)
- UniProtKB:Q6ZP29 = human **PQLC2/LAAT1** (lysosomal cationic amino acid transporter)
- PomBase:SPAC17C9.10 (S. pombe)

**ILT1 is NOT a PAINT seed** (it is uncharacterized). It sits in subfamily **SF37**, whose only two
members are ILT1 (Q03193) and the *S. pombe* SPAC2E12.03c (Q10227) — **both uncharacterized**
(`PTHR16201-entries.csv`). So the specific "vacuolar basic amino acid export" function attached to
ILT1 by IBA is inherited from the distantly related YPQ/PQLC2 subfamilies, i.e. it is a
family-level (paralog) inference, not evidence that ILT1 itself does this.

Two concrete conflicts with the family-level IBA inference:
1. **Location.** ILT1 is experimentally at the **plasma membrane**, not the vacuolar membrane:
   - Huh et al. GFP localization (IDA:SGD; UniProt SUBCELLULAR LOCATION "Cell membrane
     {ECO:0000269|PubMed:14562095}").
   - Higgins et al. Ilt1-GFP [PMID:30045857 "both Sge1PLL-GFP and Ilt1-GFP fusion proteins
     localized to the plasma membrane"]. So the IBA GO:0005774 *vacuolar membrane* term conflicts
     with two independent experimental plasma-membrane localizations.
2. **Process.** The only characterized phenotype is **cationic-toxin tolerance** at the cell
   surface, not intracellular/vacuolar amino-acid homeostasis.

Therefore the IBA amino-acid-transport terms are best treated as **over-annotations / uncertain
paralog inferences** for ILT1: the *fold* (PQ-loop) is consistent with a small-molecule
transporter/sensor, but the *substrate* (basic amino acids) and *site* (vacuole) are not
supported for ILT1 and are in fact contradicted (location).

## Experimental knowledge (KNOWN) — all from Higgins et al. 2018 (PMID:30045857, full text)

- **Deletion phenotype:** `ydr090cΔ` shows reduced growth at a subtoxic 31 mM [C2C1im]Cl (imidazolium
  ionic liquid) [PMID:30045857 "only ydr090cΔ displayed reduced growth in medium with a subtoxic
  31 mM [C2C1im]Cl concentration compared to medium without IIL"]. Basis for the standard-name
  assignment ILT1.
- **Complementation / gain of function:** plasmid ILT1 rescues the `ilt1Δ` growth defect in
  [C2C1im]Cl in the BY (S288c-derived) background [PMID:30045857 "The BY ilt1Δ strain transformed
  with the empty control vector grew significantly slower than the deletion strain complemented
  with the ILT1 sequence"]; extra copies increase tolerance.
- **Broader cationic-toxin tolerance:** `ilt1Δ` is sensitive to the cationic dye crystal violet
  (CV) and to [C4C1im]Cl [PMID:30045857 "ILT1 functions in tolerance to a range of cationic toxins
  in the BY strain background"].
- **Localization:** Ilt1-GFP at the plasma membrane [PMID:30045857 "both Sge1PLL-GFP and Ilt1-GFP
  fusion proteins localized to the plasma membrane"].
- **Independent of SGE1:** ILT1 acts independently of the SGE1 efflux pump [PMID:30045857 "This
  indicated that sge1PLL function does not require ILT1 for IIL tolerance in the BY strain
  background"].
- **Strain-specific effect:** no ILT1 requirement in the 378 background (which carries the tolerant
  SGE1PLL allele) [PMID:30045857 "no significant differences in cell growth were seen between 378
  ilt1Δ/ilt1Δ mutants ... suggesting that ILT1 has strain-specific functions"].
- **PTMs (UniProt large-scale):** Phospho-Ser229 (PubMed:17330950, 19779198); predicted N-glyco at
  N251, N259.

## NOT known / knowledge gaps

- **Molecular function is unknown.** No transport activity, substrate, or mechanism has been
  measured for Ilt1. It is plausibly a PQ-loop transporter/permease or a transport-associated /
  regulatory membrane protein, but there is no direct biochemical assay. The IBA MF term (basic
  amino acid transporter) is a family inference from a *different* subfamily and is not supported.
- **The relevant substrate/transported species (if any) is unknown** — whether Ilt1 exports the
  ionic-liquid cation, imports something protective, or acts indirectly (e.g. modulating another
  transporter or membrane property) has not been determined.
- **The direct biological role beyond cationic-toxin tolerance is unknown.** Ionic liquids are
  synthetic xenobiotics; the *native* physiological function of ILT1 (its selective advantage in
  the wild) is not established. No growth phenotype other than cationic-compound sensitivity is
  documented.
- **No physical interactors / pathway** are functionally established (BioGRID lists high-throughput
  interactions only).

## Curation plan (summary)

- Location: keep **plasma membrane** (IDA, PMID:30045857) as core CC; keep generic "membrane" IEA.
- The IBA **vacuolar membrane** (GO:0005774) location conflicts with two experimental PM
  localizations → MARK_AS_OVER_ANNOTATED / REMOVE-leaning; treat as non-core paralog inference.
- IBA MF (basic amino acid transporter, GO:0015174) and IBA BP (vacuolar basic amino acid export
  GO:0034488; intracellular amino acid homeostasis GO:0080144) are unsupported paralog inferences
  for ILT1's subfamily → MARK_AS_OVER_ANNOTATED (uncertain; do not assert; document in
  knowledge_gaps).
- ND MF/BP (GO:0003674 / GO:0008150): experimental data now support at least a BP
  (cationic-compound / xenobiotic tolerance) → the BP-ND is superseded; MF remains genuinely
  unknown.
- core_functions: minimal — CC plasma membrane; BP response to xenobiotic/toxic cationic compound
  (defensible from deletion phenotype). MF left as a knowledge gap.

## Falcon deep-research cross-check (2026-07-05)

Ran `just deep-research-falcon yeast ILT1` (Edison; 24.7 min). The report
(`ILT1-deep-research-falcon.md`) independently reaches the same core conclusion: YDR090C/ILT1 is a
PQ-loop family member that is **distinct from the characterized Ypq1-3 vacuolar transporters**, and
any transport/substrate assignment is **"inference rather than direct evidence"**. It adds useful
family context (3+1+3 alternating-access fold from cystinosin structures; PQLC2/LAAT-1 lysosomal
cationic-amino-acid exporters; Ypq2 nitrogen-regulated vacuolar arginine export) — all consistent
with my paralog-over-annotation reasoning for the IBA terms. Two caveats: (1) the report leans
toward a "vacuolar transporter" prediction based purely on homology, which conflicts with the two
experimental plasma-membrane localizations for Ilt1 — I weight the direct evidence higher; (2) the
report did NOT surface the Higgins et al. 2018 primary experimental paper and instead mentions an
unverifiable "Reed et al. 2019 Yarrowia lipolytica" study for the ILT1 name — likely a spurious
citation. I have NOT used that claim; the review's functional/phenotypic claims are all anchored to
the verified Higgins et al. 2018 full text (PMID:30045857).
