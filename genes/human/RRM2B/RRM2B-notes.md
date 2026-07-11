# RRM2B (p53R2) review notes

UniProtKB: Q7LG56 (RIR2B_HUMAN). Gene: RRM2B / P53R2. 351 aa. EC 1.17.4.1.

## Core biology (grounded in UniProt + cached PMIDs)

RRM2B encodes the **p53-inducible small subunit of ribonucleotide reductase (p53R2)**.
It is a paralog of the cell-cycle-regulated small subunit RRM2, but unlike RRM2 it is
**induced by p53/TP53 in response to DNA damage** and is present in resting/quiescent cells
[PMID:10716435, PMID:11517226]. Together with the large catalytic subunit RRM1 it forms an
active **ribonucleotide reductase (RNR)** that reduces ribonucleoside diphosphates (NDPs) to
2'-deoxyribonucleoside diphosphates (dNDPs) — the rate-limiting de novo step in dNTP supply
for DNA synthesis and repair [PMID:11517226, PMID:16376858].

- EC 1.17.4.1 / RHEA:23252: "a 2'-deoxyribonucleoside 5'-diphosphate + [thioredoxin]-disulfide
  + H2O = a ribonucleoside 5'-diphosphate + [thioredoxin]-dithiol" (UniProt CATALYTIC ACTIVITY).
- Cofactor: binds 2 iron ions per subunit; contains a **diiron-tyrosyl free radical** center
  required for catalysis [PMID:19728742 (crystal structure); PMID:11517226 (iron-tyrosyl radical)].
  UniProt Fe-binding residues: 100, 131, 134, 194, 228, 231; ACT_SITE 138.

## Subcellular location

RNR is a **cytosolic** process. Pontarin et al. [PMID:18997010] used three independent methods
and found R1/R2/p53R2 reside in the cytosol, arguing against the earlier nuclear-translocation
model and supporting a primary function of p53R2 for mtDNA replication. The earlier reports
described translocation cytoplasm->nucleus after DNA damage [PMID:11719458, PMID:12615712];
UniProt SUBCELLULAR LOCATION: "Cytoplasm. Nucleus. Note=Translocates from cytoplasm to nucleus
in response to DNA damage." HPA IDA supports cytosol + nucleoplasm.
Treat cytosol as the core location; nucleus/nucleoplasm/cytoplasm accepted as observed locations.
Mitochondrion IEA (GO_REF:0000108, inferred from GO:0006264) is not a documented physical
localization of the protein — RNR is cytosolic and supplies dNTPs that are imported into
mitochondria; mark over-annotated.

## Disease / physiology

- **MTDPS8A/8B** (mitochondrial DNA depletion syndrome 8, encephalomyopathic +/- tubulopathy):
  RRM2B mutations cause severe mtDNA depletion; Rrm2b-/- mouse recapitulates this. p53R2 has a
  crucial role in dNTP supply for mtDNA synthesis, distinct from DNA repair [PMID:17486094].
- **PEOA5**: autosomal dominant progressive external ophthalmoplegia with multiple mtDNA
  deletions [PMID:19664747].
- **RCDFRD**: rod-cone dystrophy, deafness, Fanconi renal dysfunction [PMID:32827185].
These establish the physiological role: providing dNTPs for **mitochondrial DNA replication/
synthesis** in post-mitotic/quiescent tissues (skeletal muscle high expression).

## Annotation review reasoning

- **MF GO:0004748** (ribonucleoside-diphosphate reductase activity, thioredoxin disulfide as
  acceptor): CORE. Direct IDA [PMID:16376858 catalytic activity; PMID:12615712], IBA, ISS, IEA
  all agree. Accept.
- **GO:0016491 oxidoreductase activity** (IEA, InterPro): correct but far too general given the
  specific GO:0004748 is present -> MARK_AS_OVER_ANNOTATED (parent of the specific term).
- **BP dNTP synthesis**: GO:0009263 (deoxyribonucleotide biosynthetic process), GO:0009265
  (2'-deoxyribonucleotide biosynthetic process), GO:0009185 (ribonucleoside diphosphate metabolic
  process) — all correct core/near-core process terms for RNR. Accept the specific ones; the
  ComplexPortal IDA on 0009265 and 0009185 are supported by PMID:16376858. GO:0009185 is somewhat
  general (metabolic vs biosynthetic) but correct.
- **DNA repair GO:0006281 / GO:0000731 (DNA synthesis involved in DNA repair)**: supported by
  IDA [PMID:11719458] and the p53-checkpoint literature. Accept as core/near-core (supplies dNTPs
  for repair). NAS on 0000731 from PMID:10716435 accepted.
- **GO:0006264 mitochondrial DNA replication** (IMP PMID:17486094; IEA): supported — p53R2 supplies
  dNTPs for mtDNA synthesis; loss causes mtDNA depletion. Accept (KEEP_AS_NON_CORE style: it is the
  in vivo physiological consequence; RRM2B itself doesn't replicate DNA but supplies precursors).
  Keep as core process — this is arguably the most important physiological role.
- **Cell-cycle regulation terms**: GO:1901992 (positive regulation of mitotic cell cycle phase
  transition, IEA/ARBA), GO:0010971 (positive regulation of G2/M transition, IDA PMID:10716435),
  GO:0070318 (positive regulation of G0 to G1 transition, IDA PMID:11517226 / IEA). PMID:10716435
  shows p53R2 induction causes G2/M arrest (a checkpoint), which is not the same as "positive
  regulation of G2/M transition". These are indirect/over-interpreted -> MARK_AS_OVER_ANNOTATED.
  GO:0070318 IDA is cited to PMID:11517226 which is an in-vitro RNR activity paper about resting
  cells; does not directly demonstrate positive regulation of G0->G1 -> MARK_AS_OVER_ANNOTATED.
- **GO:0014075 response to amine** (IEA from rat ortholog, GO_REF:0000107): weakly supported,
  electronic transfer from a rat paralog; peripheral -> MARK_AS_OVER_ANNOTATED.
- **protein binding GO:0005515 (IPI)**: bare, uninformative. 12615712 = TP53 (functional/regulatory),
  19015526 = ATM/MDM2 (regulation of p53R2 stability). Per policy do NOT REMOVE bare protein-binding
  IPIs -> MARK_AS_OVER_ANNOTATED (keep the functional context in reason).
- **identical protein binding GO:0042802 (IPI)**: RNR small subunits form homodimers (structural
  ferritin-like fold; UniProt INTERACTION lists Q7LG56-Q7LG56). Large-scale screens (25416956,
  25502805, 31515488). Uninformative for function -> MARK_AS_OVER_ANNOTATED.
- **Cytosol/cytoplasm/nucleus/nucleoplasm**: cytosol (IBA/IDA/TAS/HPA) core; others accepted as
  observed locations. Mitochondrion IEA over-annotated (see above).

## core_functions (author-supplied, strictly validated)

- MF: GO:0004748.
- Process: GO:0009263 (deoxyribonucleotide biosynthetic process) — the de novo dNTP supply role.
- Process: GO:0006264 (mitochondrial DNA replication) — the key physiological role (dNTP supply
  for mtDNA synthesis; disease-defining).
- Location: GO:0005829 (cytosol).
</content>
