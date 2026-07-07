# hgh1 (SPAC26F1.12c) — S. pombe review notes

UniProt: Q10498 (HGH1_SCHPO), 356 aa, 41.3 kDa. PomBase: SPAC26F1.12c, standard name `hgh1`.
PomBase product: "eEF2 folding chaperone Hgh1". Characterisation status: **"biological role inferred"**
(i.e. the eEF2-chaperone role is inferred from the S. cerevisiae ortholog, not directly demonstrated in S. pombe).

## Identity / family (from UniProt + InterPro + PomBase)

- UniProt RecName (by similarity to S. cerevisiae P48362): "Co-chaperone protein HGH1 homolog".
- Belongs to the **HGH1 family** (UniProt SIMILARITY, ECO:0000305).
- InterPro architecture: IPR039717 (Hgh1), IPR007205 (Protein_HGH1_N / Pfam PF04063 DUF383),
  IPR007206 (Protein_HGH1_C / Pfam PF04064 DUF384), on an **ARM-type fold / ARM-like** scaffold
  (IPR011989 ARM-like, IPR016024 ARM-type_fold; Gene3D 1.25.10.10 "Leucine-rich Repeat Variant";
  SUPFAM SSF48371 "ARM repeat"). PANTHER PTHR13387 "PROTEIN HGH1 HOMOLOG".
- Orthologs (PomBase): human HGNC:24161 (**HGH1 / FAM203 / C21orf25**), S. cerevisiae **YGR187C (HGH1)**,
  S. japonicus SJAG_02014. eggNOG KOG2973 (Eukaryota).
- No signal peptide, no TM segment → soluble cytoplasmic protein (consistent with the family).

## What is KNOWN about the HGH1 family (chiefly from S. cerevisiae Hgh1)

Primary experimental characterization is in **budding yeast** Hgh1 (P48362):
[PMID:30876804 "Chaperone Function of Hgh1 in the Biogenesis of Eukaryotic Elongation Factor 2",
Mönkemeyer/Klaips/Balchin/Körner/Hartl/Bracher, Mol Cell 2019].
Abstract-only cache; key verbatim facts:
- "the highly conserved protein Hgh1 (FAM203 in humans) is a chaperone that cooperates with TRiC in
  eEF2 folding."
- "In the absence of Hgh1, a substantial fraction of newly synthesized eEF2 is degraded or aggregates."
- "Hgh1 is an armadillo repeat protein that binds to the dynamic central domain III of eEF2 via a
  bipartite interface."
- "Hgh1 binding recruits TRiC to the C-terminal eEF2 module and prevents unproductive interactions of
  domain III, allowing efficient folding of the N-terminal GTPase module."
- "eEF2 folding is completed upon dissociation of TRiC and Hgh1."

So the S. cerevisiae protein is a **dedicated co-chaperone/adaptor for eEF2 biogenesis**: it is not an
ATP-driven foldase itself, but an armadillo-repeat scaffold that (i) shields the dynamic domain III of
the nascent eEF2, and (ii) recruits the chaperonin TRiC/CCT (and, per UniProt SUBUNIT, potentially
Hsp90 via Cns1) to the client. It forms a ternary Hgh1–eEF2–TRiC complex. eEF2 (but not Hgh1) is
essential; Hgh1 loss reduces mature-eEF2 yield rather than abolishing translation.

## What is known SPECIFICALLY about S. pombe hgh1

- **No S. pombe-specific molecular study of hgh1.** All GO molecular-function/biological-process
  annotations in GOA are electronic ISO transfers from S. cerevisiae HGH1 (GO_REF:0000024,
  with/from SGD:S000003419), plus one IEA subcellular-location mapping and an ISS location.
- **Deletion phenotype (S. pombe): viable, normal cell morphology** (PomBase deletion_viability = viable;
  FYPO:0002060 "viable vegetative cell population", FYPO:0002177 "viable vegetative cell with normal cell
  morphology"). This is consistent with the non-essential co-chaperone role seen in budding yeast.
- A broad set of high-throughput **stress phenotypes** are recorded from genome-wide screens (e.g.
  sensitivity to hydroxyurea, lithium, several antifungals; resistance to caffeine, brefeldin A, diamide,
  bleomycin, etc.). These are pleiotropic HT-screen signals and are not, on their own, evidence of a
  specific molecular function; I do not build core_functions on them.

## Domain reasoning (inline, no external bioinformatics agent)

- The Q10498 sequence is 356 aa with the two-part HGH1 Pfam signature (PF04063 N + PF04064 C) mapped by
  InterPro, sitting on an all-α ARM/HEAT-like solenoid (SUPFAM ARM repeat; Gene3D 1.25.10.10). Armadillo
  solenoids are classic **protein–protein interaction scaffolds**, which fits the "adaptor that clamps a
  client and recruits chaperonins" mechanism established for the ortholog.
- No nucleotide-binding (Walker/P-loop) or catalytic motifs are annotated → consistent with a
  **non-catalytic, non-ATP-dependent co-chaperone** (hence MF GO:0044183 "protein folding chaperone",
  NOT GO:0140662 "ATP-dependent protein folding chaperone").
- Length and family membership match the S. cerevisiae ortholog (Sc Hgh1 ~394 aa); orthology is
  unambiguous (single-copy KOG2973; reciprocal PomBase ortholog calls), so ISO transfer of the eEF2
  co-chaperone role is biologically well-motivated even though not directly tested in S. pombe.

## Annotation-by-annotation plan (GOA has 6 rows; several are duplicates/overlaps)

1. GO:0005737 cytoplasm, IEA, GO_REF:0000044 (SubCell mapping). Cytoplasmic localization is expected for
   this soluble family; ACCEPT (location, non-core).
2. GO:0044183 protein folding chaperone, ISO, GO_REF:0000024 (from SGD). This is the correct MF for the
   ortholog's mechanism (co-chaperone/adaptor, non-ATP). KEEP — core molecular function (transferred).
   (Appears twice in GOA — duplicate ISO row.)
3. GO:0051083 'de novo' cotranslational protein folding, ISO, GO_REF:0000024. Matches the co-translational
   eEF2-folding role. KEEP — core biological process (transferred).
4. GO:0005737 cytoplasm, ISS, GO_REF:0000024 (from UniProt P48362). Redundant with #1 but well-supported;
   ACCEPT (location).
5. GO:0005634 nucleus, ISO, GO_REF:0000024 (is_active_in). **Questionable.** eEF2 folding is a
   cytoplasmic/co-translational process; the ortholog is described as cytosolic. A nuclear "is_active_in"
   for a cytoplasmic co-chaperone is not supported by the mechanism and looks like an over-broad ISO
   transfer (SGD high-throughput localization). MARK_AS_OVER_ANNOTATED (or KEEP_AS_NON_CORE at most).
6. GO:0005737 cytoplasm, ISO, is_active_in, GO_REF:0000024. Consistent with the site of action; ACCEPT
   (location, non-core; cytoplasm is where the eEF2/TRiC folding happens).

## Knowledge gaps (the honest core deliverable)

- **Molecular activity in S. pombe is inferred, not measured.** No study has shown fission-yeast Hgh1
  binds eEF2 (ef2 = tef1/tef2 products in S. pombe) or TRiC, or affects eEF2 folding/levels.
- **Biological role / phenotype:** deletion is viable with normal morphology; the physiological
  consequence of losing hgh1 in S. pombe (e.g. eEF2 abundance, translation elongation fidelity, stress
  fitness) has not been dissected. The HT stress phenotypes are unexplained mechanistically.
- **Nuclear pool:** whether hgh1 has any genuine nuclear function (vs. an ISO artifact) is unknown.
- Family-level: whether HGH1 proteins have clients beyond eEF2 is not established.

## Deep research (falcon / Edison Scientific)

Falcon deep research completed (~21 min; `hgh1-deep-research-falcon.md`, 12 citations). It
independently corroborates the review: HGH1 as a dedicated eEF2 co-chaperone that binds eEF2
domain III co-translationally, recruits TRiC/CCT (incl. Cct6) and links to a Cns1–Hsp90 network;
hgh1Δ reduces total eEF2 by ~30–35% with increased insoluble eEF2; localization is cytoplasmic
by inference, "explicit localization experiments were not identified in the retrieved evidence".
The report is centered on the S. cerevisiae ortholog and explicitly notes S. pombe hgh1 function
is inferred. Some falcon citations use Edison-internal keys (e.g. yang2026, fulton2024, engler2025)
that are not verified PMIDs; the review therefore anchors all `supporting_text` only to the
independently verified PMID:30876804. The perplexity-lite fallback failed (API 401/quota).

## References to cite
- PMID:30876804 — primary S. cerevisiae Hgh1/eEF2 mechanism (HIGH relevance; the basis for the ISO transfer).
- GO_REF:0000024 — ISO transfer method (already present).
- GO_REF:0000044 — SubCell location mapping (already present).
- file: bioinformatics not needed; UniProt/InterPro domain evidence cited inline.
