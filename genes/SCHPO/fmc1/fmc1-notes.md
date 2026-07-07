# fmc1 (SPAC1486.11) — S. pombe — review notes

Journal for the AI GO-annotation review of the *S. pombe* gene **fmc1**
(systematic name SPAC1486.11; synonym *new3*; UniProt **G2TRM0**, FMC1_SCHPO).
"Formation of Mitochondrial Complexes protein 1" — a putative mitochondrial
F1-ATP-synthase assembly factor. This is an understudied ("dark") gene: UniProt
lists it as *Evidence at transcript level* (PE 2), and there is **no direct
experimental characterization of the fission-yeast protein**. All GO annotations
are electronic/phylogenetic (IBA, IEA) or ND.

## Identity confirmation (from fmc1-uniprot.txt)

- `ID   FMC1_SCHPO ... 104 AA`; `AC   G2TRM0`.
- `DE   RecName: Full=ATP synthase assembly factor fmc1, mitochondrial;`
  `AltName: Full=Formation of mitochondrial complexes protein 1;`
  `Flags: Precursor;`
- `GN   Name=fmc1; Synonyms=new3; ORFNames=SPAC1486.11;`
- `OX   NCBI_TaxID=284812` (S. pombe 972 / ATCC 24843).
- Function (by similarity, ECO:0000250): "Needed for the assembly of the
  mitochondrial F1-F0 complex at high temperature."
- Subcellular location (by similarity): Mitochondrion.
- SIMILARITY: "Belongs to the FMC1 family." (ECO:0000305)
- Features: `TRANSIT 1..?  /note="Mitochondrion" /evidence=ECO:0000255`;
  `CHAIN ?..104`. So it carries a predicted N-terminal mitochondrial transit
  peptide (mito targeting is sequence-predicted, not experimentally mapped).
- Domain/family cross-refs: InterPro **IPR039196 (Fmc1)**; PANTHER **PTHR28015**
  ("ATP SYNTHASE ASSEMBLY FACTOR FMC1, MITOCHONDRIAL"); Pfam **PF13233
  (Complex1_LYR_2)** — i.e. it belongs to the LYR-motif protein (LYRM)
  superfamily. PomBase SPAC1486.11 → fmc1.
- `PE   2: Evidence at transcript level` — no protein-level experimental
  evidence recorded in UniProt for the pombe protein.

Domain reasoning (inline): 104-aa, small, matrix-soluble-type protein with a
single Complex1_LYR_2 (LYR-motif) module and a predicted mito transit peptide.
The LYRM family members typically act as small accessory/assembly factors of
OXPHOS complexes rather than as enzymes; they have no catalytic domain. This is
fully consistent with an accessory assembly-factor / chaperone-like role and
argues *against* any catalytic (enzyme) molecular function.

## Existing GO annotations (from fmc1-goa.tsv)

1. GO:0005759 mitochondrial matrix — IBA (is_active_in) — GO_REF:0000033
   (PANTHER PTN001997425 | SGD:S000001360).
2. GO:0033615 mitochondrial proton-transporting ATP synthase complex assembly —
   IBA (involved_in) — GO_REF:0000033 (same PANTHER/SGD source).
3. GO:0005739 mitochondrion — IEA (located_in) — GO_REF:0000044
   (UniProtKB-SubCell SL-0173).
4. GO:0033615 (again) — IEA (involved_in) — GO_REF:0000002 (InterPro:IPR039196).
5. GO:0003674 molecular_function (root) — ND — GO_REF:0000015 (PomBase). This is
   the "no biological data available" root-term placeholder: MF is genuinely
   dark for this protein.

The IBA source is SGD:S000001360 = *S. cerevisiae* FMC1 (the founding, and only
directly-characterized, family member). So the pombe annotations propagate
budding-yeast biology through the PANTHER tree (PTN001997425).

## Family biology — established in S. cerevisiae (NOT in pombe)

Founding paper, **PMID:11096112** (Lefebvre-Legendre et al. 2001, J Biol Chem
276:6789-6796) — *S. cerevisiae* FMC1. Cached abstract (publications/PMID_11096112.md);
full_text_available: false (abstract-only). Verbatim quotes available:
- "We have identified a yeast nuclear gene (FMC1) that is required at elevated
  temperatures (37 degrees C) for the formation/stability of the F(1) sector of
  the mitochondrial ATP synthase."
- "Fmc1p is a soluble protein located in the mitochondrial matrix."
- "instead of being incorporated into a functional F(1) oligomer, they form
  large aggregates in the mitochondrial matrix." (of alpha/beta-F1 subunits)
- "the absence of Fmc1p can be efficiently compensated for by increasing the
  expression of Atp12p."
- "unlike Atp12p and Atp11p, Fmc1p is not required in normal growth conditions
  (28--30 degrees C)."
- "We propose that Fmc1p is required for the proper folding/stability or
  functioning of Atp12p in heat stress conditions."

So the mechanistic model (in budding yeast): Fmc1p is a matrix accessory factor
that stabilizes/assists the dedicated F1 assembly chaperone **Atp12p** (human
ATPAF2), which in turn chaperones folding/assembly of the F1 α3β3 head of ATP
synthase (Complex V). Fmc1p is conditionally required (heat stress) and
dispensable at normal temperature.

Human ortholog: **FMC1 / C7orf55** (OMIM 620766, "Formation Of Mitochondrial
Complex V Assembly Factor 1 Homolog"); member of the LYR-motif protein
superfamily; linked to Complex V (ATP synthase) assembly and interacting with
the ATP12/ATPAF2 axis (WebSearch, GeneCards/OMIM; PMC4381221 on LYR proteins
interacting with mitochondrial complexes). This corroborates conservation of the
assembly-factor role across fungi and humans.

## KNOWN vs NOT-KNOWN for S. pombe fmc1 specifically

KNOWN (defensible by orthology + domain, not by pombe experiments):
- It is a member of the FMC1 family (UniProt SIMILARITY; InterPro IPR039196;
  PANTHER PTHR28015). High-confidence family assignment.
- By orthology it is expected to localize to the mitochondrion / matrix
  (predicted transit peptide + IBA to matrix from the S. cerevisiae ortholog).
- By orthology it is expected to participate in mitochondrial F1Fo ATP synthase
  (Complex V) assembly, most plausibly as a chaperone-like accessory factor
  acting via the Atp12/ATPAF2 F1-assembly chaperone.

NOT KNOWN (genuine gaps for the pombe protein):
- No experimental data on the pombe protein at all (PE 2, transcript-level). No
  IDA/IMP/IPI/IGI annotations exist.
- Its specific molecular activity is undefined (MF is ND). Whether it acts as a
  protein-folding chaperone, as an adaptor that stabilizes a partner chaperone
  (Atp12/ATPAF2 ortholog), or in some other capacity has not been shown in pombe.
- Whether the fission-yeast protein is, like budding yeast, only *conditionally*
  (heat-stress) required, or has a broader role, is unknown.
- No pombe interaction partner has been demonstrated (does an Atp12/ATPAF2
  ortholog exist in pombe and does fmc1 act on it?). BioGRID lists 1 interaction
  (unverified here).
- No loss-of-function phenotype (respiratory competence, growth on non-fermentable
  carbon source, temperature sensitivity of ATP synthase assembly) has been
  reported for pombe fmc1.

## Planned review actions

- GO:0005759 mitochondrial matrix (IBA): KEEP_AS_NON_CORE / accept-ish. Matrix
  localization is orthology-supported (S. cerevisiae Fmc1p is a soluble matrix
  protein) and is the actual site of F1 assembly. Reasonable IBA; keep.
- GO:0033615 ATP synthase complex assembly (IBA): ACCEPT as the core process.
  Best-supported functional statement, matches family and the founding paper.
- GO:0005739 mitochondrion (IEA, SubCell): KEEP_AS_NON_CORE — correct but less
  specific than the matrix (IBA) term; general parent.
- GO:0033615 (IEA, InterPro): ACCEPT — redundant with the IBA but independently
  domain-supported (IPR039196). Consistent.
- GO:0003674 molecular_function root (ND): KEEP_AS_NON_CORE — honest placeholder;
  MF genuinely dark. Do not remove (ND root reflects the real state).

core_functions MF: use GO:0044183 "protein folding chaperone"
(def: "Binding to a protein or a protein-containing complex to assist the protein
folding process") — NON-ATP-dependent (Fmc1 has no ATPase; so NOT GO:0140662).
This is the most defensible MF given the founding-paper mechanism (assists
folding/stability of the F1 assembly machinery), framed as inferred by orthology.
BP: GO:0033615. Location: GO:0005759.
