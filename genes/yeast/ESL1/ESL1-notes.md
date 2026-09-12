# ESL1 (YIL151C, P40456) — curation notes

Journal of research for the AI GO-annotation review of *Saccharomyces cerevisiae* ESL1.
All assertions carry inline provenance. Where a claim is about the paralog ESL2 or the
ESL1/ESL2 pair jointly, that is stated explicitly.

## Identity and domain architecture (from UniProt P40456 + primary literature)

- Standard name **ESL1** = "EST/SMG-like protein 1"; systematic name **YIL151C**; SGD:S000001413.
  1118 aa, 128.7 kDa. UniProt evidence level 1 (protein level). [UniProt P40456]
- Named by Lai et al. 2013, which is the ONLY dedicated functional study of this gene.
  ESL = "EST/SMG-like". The paralog is **ESL2 = YKR096W** (>70% similarity to ESL1 along
  the entire polypeptide). [PMID:23893744 "the previously uncharacterized yeast open
  reading frames Yil151c and Ykr096w, share >70% similarity with each other along their
  entire polypeptide sequence"]

### Domains
- **PIN (PilT N-terminus) endonuclease domain**, C-terminal. UniProt annotates a PINc
  domain at residues **947–1087** (ECO:0000255, sequence-analysis). InterPro IPR002716
  (PIN_dom); Pfam PF13638 (PIN_4); SMART SM00670 (PINc). [UniProt P40456]
- **14-3-3-like "Est-one-homology" (EOH) domain**, central. Not given explicit FT
  coordinates in UniProt, but described by the primary paper. [PMID:23893744 "these two
  proteins also share extensive similarity ... with human hEST1A/B and Drosophila and
  Caenohabditis elegans SMG5/6 proteins ... encompassed the region corresponding to the
  14-3-3–like Est-one-homology domain (45–51% similarity ...) and the C-terminal PIN
  endonuclease domain (49–53% similarity ...)"]
- The four acidic catalytic residues of the PIN domain are **conserved** in Esl1/Esl2.
  The ESL1 "nuclease-dead" allele used in the paper carries **D952N and E982Q** (two
  substitutions); the ESL2 nuclease-dead allele carries a single D1123N substitution.
  [PMID:23893744 "complete conservation of four critical D/E residues required for
  nuclease activity of the PIN-domain proteins"; "The esl1-nd mutant carries two amino
  acid substitutions (D952N and E982Q) while the esl2-nd mutant carries a single amino
  acid substitution (D1123N)"]
- InterPro family assignment: **IPR045153 Est1/Ebs1-like**; PANTHER PTHR15696 (SMG-7 /
  telomerase-binding protein EST1A family). [UniProt P40456 DR lines]
- N-terminal ~1–119 region is disordered (MobiDB-lite); phosphoserines at S170 and S190
  from large-scale phosphoproteomics. [UniProt P40456 FT lines; ECO:0007744|PubMed:18407956]

### IMPORTANT: the task brief's "GRAM/VASt lipid-transfer domain" description is WRONG
The UniProt record and the primary literature both establish ESL1 as a **PIN-domain +
14-3-3-like (EOH) protein of the Est1/SMG family** — there is no GRAM domain, no VASt
domain, and no evidence for lipid binding or lipid transfer. I proceeded on the basis of
the actual UniProt/primary-literature evidence, not the brief's mischaracterization.

## What is KNOWN about ESL1 (experimental, from Lai et al. 2013, PMID:23893744)

All functional data come from a single paper studying esl1Δ, esl2Δ single mutants and
esl1Δ esl2Δ double mutants (and nuclease-dead alleles). Most phenotypes are reported for
the *pair* and are stronger in the double mutant, indicating **functional redundancy**
between ESL1 and ESL2. ESL1-specific single-mutant results are called out below.

1. **NOT NMD; NOT telomere maintenance.** Despite structural orthology to metazoan
   hEST1A/B (SMG5/6), esl1Δ, esl2Δ and esl1Δ esl2Δ mutants have wild-type telomere
   length, normal senescence/ALT kinetics (with est2Δ), normal subtelomeric silencing
   (5-FOA), no TERRA accumulation, and no accumulation of NMD substrates (ade2-1;
   unspliced pre-CYH2). [PMID:23893744 "Esl1 and Esl2 were not involved in
   nonsense-mediated mRNA decay or telomere maintenance pathways"; "ESL1 and ESL2 do not
   seem to have NMD-related functions"; "Esl1 and Esl2 are not required for
   telomerase-dependent or alternative telomere maintenance mechanisms"]
   → This directly REFUTES the IBA-propagated NMD (GO:0000184), telomerase holoenzyme
     complex (GO:0005697), telomeric DNA binding (GO:0042162), and telomerase RNA binding
     (GO:0070034) annotations for this yeast gene.

2. **Environment-sensing adaptive gene expression.** esl1Δ esl2Δ deregulate ~50–53
   transcripts (≥2-fold) — hexose transporters (HXT3/6/7), hexokinase HXK1, MAL genes,
   JEN1, glycogen genes (GPH1, PGM2), and one-carbon/glycine-regulon genes (GCV1/2/3,
   SHM2, ADE17) — in the direction *opposite* to the environmentally appropriate
   response. [PMID:23893744 "absence of Esl1 and Esl2 led to more than two-fold
   deregulation of ∼50 transcripts, most of which were expressed inversely to the
   appropriate metabolic response to environmental nutrient supply"; "esl1Δ esl2Δ double
   mutants may have a defect in adapting the expression of hexose and one-carbon
   metabolism genes to environmentally appropriate requirements"]

3. **Genetic interaction with the Rim101 pH-sensing pathway.** esl1Δ esl2Δ is synthetic
   sick with rim8Δ and dfg16Δ (the arrestin-like adaptor and GPCR of the Rim101 pathway),
   and ESL2 interacts with RIM9/RIM13/RIM20 in an independent screen — supporting a role
   parallel to Rim101 in environmental adaptation. [PMID:23893744 "esl1Δ esl2Δ double
   mutants were synthetic sick with null mutations for Rim8 and Dfg16, which form the
   environmental-sensing complex of the Rim101 pH response gene expression pathway"]

4. **Genome-stability / stress phenotypes (pair; some nuclease-dependent).** esl1Δ esl2Δ
   show elevated mitochondrial-genome instability (petite formation) and altered
   sensitivity to genotoxins (better on bleomycin/HU, worse on adriamycin). Bleomycin
   resistance is phenocopied by nuclease-dead alleles, implicating the PIN catalytic
   residues in *this* phenotype. [PMID:23893744 "ESL1 and ESL2 contribute to maintenance
   of mitochondrial genome stability"; "the nuclease-dead mutants phenocopied the
   bleomycin sensitivity of the esl1Δ or esl2Δ mutants"]

5. **Synthetic interaction with trf4Δ** (TRAMP-complex poly(A) polymerase); esl1Δ esl2Δ
   deregulate neighboring CUTs/SUTs — but this CUT/SUT change is **nuclease-independent**
   and not directly coupled to the coding-gene changes. [PMID:23893744 "loss of Esl1 and
   of Esl2 lead to impaired genetic fitness with trf4Δ, rim8Δ, and dfg16Δ"; "these
   changes in transcript levels were again independent of Esl1 and Esl2 nuclease domain
   integrity"]

### ESL1-specific vs pair
- Single-mutant SGA hits attributed to **esl1Δ alone**: synthetic sick with FUS3, DAL81,
  SNX4, and synthetic lethal with TRF4. [PMID:23893744 Table 2]
- Telomere/NMD assays and drug-sensitivity trends were tested on esl1Δ single mutants and
  were negative/weaker than the double mutant. The transcriptome (microarray) and most
  synthetic-sick tetrad validations were done on the **double** mutant, so the ~50-gene
  expression signature is a *joint* ESL1+ESL2 phenotype, not proven ESL1-alone.

## What is NOT known (knowledge gaps)
- **Direct molecular activity of ESL1 is undetermined.** The PIN domain has intact
  catalytic residues, but no biochemical assay of Esl1 (or Esl2) endoribonuclease
  activity has been reported; the key transcriptome phenotype is *largely
  nuclease-independent*. So RNA-endonuclease activity is domain-*suggestive* but unproven
  for ESL1. [PMID:23893744 "all other PIN domain-containing proteins characterized to
  date exert ribonuclease activity in vitro and/or in vivo"; "Esl1 and Esl2 may regulate
  the expression of the altered transcripts in a largely nuclease-independent manner"]
- **Direct RNA/DNA/protein substrates and partners of ESL1 are unknown.** The only
  reported physical interaction motivating the study is a two-hybrid hit with Mdt1/Pin4
  (Uetz et al. 2000, via the paper); no direct target of the EOH or PIN domain is
  established. [PMID:23893744 "a large-scale two-hybrid screen (Uetz et al. 2000) had
  found it to interact with two uncharacterized ... open reading frames"]
- **Mechanism linking ESL1 to nutrient/pH-adaptive gene expression is unknown** —
  whether it acts on mRNA stability, transcription, or the Rim101 axis, and whether the
  EOH 14-3-3-like domain mediates a regulatory protein-protein interaction (as in
  metazoan SMG5/6→UPF1) is undetermined. [PMID:23893744 "provide a basis for future
  investigations into the detailed mechanisms by which they exert this function"]
- **Redundancy vs ESL2 and ESL1-specific role.** Almost all phenotypes are stronger in
  esl1Δ esl2Δ; the individual, non-redundant contribution of ESL1 is not resolved.
- **Subcellular localization of Esl1 protein not experimentally reported** (no CC data in
  UniProt beyond ND; metazoan orthologs are nucleocytoplasmic but this was not tested for
  Esl1).

## Existing GOA annotations — assessment summary
| GO term | aspect | evidence | verdict |
|---|---|---|---|
| GO:0000184 NMD | BP | IBA | REMOVE — directly refuted for this yeast gene (PMID:23893744) |
| GO:0005697 telomerase holoenzyme complex | CC | IBA | REMOVE — refuted (no telomere role) |
| GO:0042162 telomeric repeat DNA binding | MF | IBA | REMOVE — refuted (no telomere role) |
| GO:0070034 telomerase RNA binding | MF | IBA | REMOVE — refuted (no telomere role) |
| GO:0003674 molecular_function (root) | MF | ND | KEEP_AS_NON_CORE (ND placeholder) |
| GO:0005575 cellular_component (root) | CC | ND | KEEP_AS_NON_CORE (ND placeholder) |
| GO:0008150 biological_process (root) | BP | ND | KEEP_AS_NON_CORE (ND placeholder) |

The four IBA annotations are phylogenetic propagations from the metazoan SMG5/6 / EST1A
clade. Lai et al. 2013 experimentally tested exactly these two functions (NMD and
telomere maintenance) in the yeast proteins and found them absent. This is a textbook
case where experimental data in the target species overrides an IBA propagation. Note the
NMD IBA even lists SGD:S000002614 (EBS1) among the with/from set — EBS1, not ESL1, is the
yeast SMG7 ortholog with NMD links; ESL1's inclusion in the tree does not reflect yeast
NMD function.

## Deep research (falcon)
`ESL1-deep-research-falcon.md` was generated (Edison, 21 citations, ~29 min). It is
**literature-limited**: falcon could NOT access the key functional paper (Lai et al. 2013)
and therefore relies on domain/family inference (PIN + TPR-like/EOH, Est1/Ebs1-like
family) and on the paralogs Est1/Ebs1. It correctly flags ESL1 as poorly characterized and
notes the mammalian ESL1 = E-selectin ligand 1 (GLG1) name clash (irrelevant to yeast
YIL151C). It does not contradict this review; because it lacked the primary paper, its
inferential telomere/NMD framing is superseded by the direct experimental exclusion of
those functions in Lai et al. 2013, which I read in full. No falcon-only claims were
imported into the review.

## References consulted
- PMID:23893744 — Lai et al. 2013, G3. Primary functional study (full text cached). HIGH.
- UniProt P40456 (ESL1_YEAST) — domain architecture, family, PTMs.
- ESL1-goa.tsv — GOA annotation set.
- ESL1-deep-research-falcon.md — provider deep research (literature-limited; see above).
