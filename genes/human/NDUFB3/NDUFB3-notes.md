# NDUFB3 (NADH dehydrogenase [ubiquinone] 1 beta subcomplex subunit 3) — review notes

UniProt: O43676 (NDUB3_HUMAN). HGNC:7698. Gene 4709. 98 aa, ~11.4 kDa.
Aliases: Complex I-B12 (CI-B12); NADH-ubiquinone oxidoreductase B12 subunit.

## Identity and biology (grounded in local files)

NDUFB3/B12 is a small nuclear-encoded **accessory ("supernumerary") subunit of
mitochondrial respiratory chain Complex I (NADH:ubiquinone oxidoreductase)**. It is a
genuine, stable subunit of the mature holoenzyme, located in the membrane arm on the
matrix side of the inner mitochondrial membrane, but it is **not catalytic**.

- Accessory, non-catalytic: UniProt FUNCTION — "Accessory subunit of the mitochondrial
  membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be
  involved in catalysis." [file:human/NDUFB3/NDUFB3-uniprot.txt]. Function ECO evidence is
  PMID:27626371.
- Complex I composition: "Complex I is composed of 45 different subunits."
  [file:human/NDUFB3/NDUFB3-uniprot.txt] (SUBUNIT; ECO from PMID:12611891 + PMID:27626371).
- Location: "Mitochondrion inner membrane ... Single-pass membrane protein ... Matrix
  side." [file:human/NDUFB3/NDUFB3-uniprot.txt]. UniProt FT annotates a single TRANSMEM
  helix at 66..88, consistent with a single-pass membrane-arm subunit.
- Family: "Belongs to the complex I NDUFB3 subunit family."
  [file:human/NDUFB3/NDUFB3-uniprot.txt].

## Complex I overall function (context, not NDUFB3's own catalytic MF)

- "Its main function is the transport of electrons from NADH to ubiquinone, which is
  accompanied by translocation of protons from the mitochondrial matrix to the
  intermembrane space." [PMID:9878551 abstract].
- "The multi-subunit NADH-ubiquinone oxidoreductase (complex I) is the first enzyme
  complex in the electron transport chain of mitochondria." [PMID:9425316 abstract].
- Reactome R-HSA-163217: net reaction NADH + Ubiquinone + 5H+(matrix) = NAD+ + Ubiquinol +
  4H+(IMS); FMN + 8 Fe-S clusters carry electrons. NDUFB3 (B12) is in the hydrophobic (HP)
  membrane arm.

## Accessory-subunit function evidence

- PMID:27626371 (Stroud et al., Nature 2016), systematic CRISPR knockouts + quantitative
  proteomics of every Complex I accessory subunit: "Bacterial and human complex I share
  14 core subunits that are essential for enzymatic function; however, the role and
  necessity of the remaining 31 human accessory subunits is unclear." "We show that 25
  subunits are strictly required for assembly of a functional complex." "loss of each
  subunit affects the stability of other subunits residing in the same structural module."
  This is the FUNCTION-supporting reference in UniProt and establishes accessory subunits
  (including NDUFB3) as structurally/assembly-required but non-catalytic.
- PMID:12611891 (Murray et al., JBC 2003): immunopurification of human Complex I and MS
  identification of subunits — "we can resolve and identify the human homologues of 42
  polypeptides detected so far in the more extensively studied beef heart complex I."
  Primary MS evidence for NDUFB3 complex membership (GOA IDA).
- PMID:28844695 (Guo et al., Cell 2017): cryo-EM of the human megacomplex
  I2III2IV2 — "reveals the precise assignment of individual subunits of human CI and CIII".
  Structural basis (ComplexPortal IDA/IPI) for NDUFB3 as an inner-membrane Complex I subunit
  and its supercomplex context.
- PMID:30030361 (Signes & Fernandez-Vizarra, review 2018): OXPHOS complexes contain core
  catalytic proteins plus "a large number of 'supernumerary' subunits that play essential
  roles in assembly, regulation and stability." Source of ComplexPortal pathway-level NAS
  BP annotations (aerobic respiration; ATP synthesis).

## PTM

- His methylation by METTL9: UniProt PTM — "Methylation at His residues by METTL9 enhances
  complex I-mediated mitochondrial respiration." (ECO from PMID:33563959, Davydova et al.,
  Nat Commun 2021). FT: Pros-methylhistidine at His-5, His-7, His-9 (in the N-terminal
  His-rich MAHEHGHEHGHHK motif). MUTAGEN 5..9 (HGHEH->RGHER) abolishes METTL9 methylation.
  Not a GO annotation in GOA but relevant to regulation of complex I respiration.

## Disease

- Mitochondrial complex I deficiency, nuclear type 25 (MC1DN25), MIM:618246, autosomal
  recessive. UniProt DISEASE. Variants: p.Trp22Arg (ARG-22; PMID:22499348, PMID:27091925)
  and 70-98 del (PMID:22499348). PMID:27091925: recurrent p.Trp22Arg causes "a distinctive
  facial appearance, short stature and a mild biochemical and clinical phenotype."
  Confirms NDUFB3 is functionally required for Complex I in vivo in humans.

## GO review conclusions

- Honest MF for NDUFB3 = **GO:0005198 structural molecule activity** (contributes to
  complex-level GO:0008137 NADH dehydrogenase (ubiquinone) activity via
  `contributes_to_molecular_function`, NOT direct `enables`).
- Complex membership: **part_of GO:0045271 respiratory chain complex I** (core CC), strongly
  supported (IDA/IPI/IBA/NAS/TAS).
- Core BP: **GO:0006120 mitochondrial electron transport, NADH to ubiquinone** and
  **GO:0032981 mitochondrial respiratory chain complex I assembly**.
- Location: **GO:0005743 mitochondrial inner membrane** (most specific; matrix side,
  single-pass).
- Over-annotations flagged (MARK_AS_OVER_ANNOTATED, not removed per policy — NAS/TAS,
  complex-level essence not wrong): direct `enables` GO:0008137 (x2, PMID:9878551 NAS,
  PMID:9425316 TAS) and inferred GO:1902600 proton transmembrane transport (IEA from
  GO:0008137) — NDUFB3 is non-catalytic and does not itself pump protons.
- Non-core context kept: GO:0009060 aerobic respiration and GO:0042776 PMF-driven ATP
  synthesis (pathway-level, downstream), GO:0005739 mitochondrion (generic vs inner
  membrane), GO:0022900 electron transport chain (generic parent of GO:0006120).
