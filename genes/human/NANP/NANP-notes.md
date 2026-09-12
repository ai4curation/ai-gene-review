# NANP (Q8TBE9) — Gene Review Notes

## Identity

- **Gene symbol:** NANP (HGNC:16140); synonyms C20orf147, HDHD4.
- **Protein:** N-acylneuraminate-9-phosphatase (EC 3.1.3.29); also called
  N-acetylneuraminate-9-phosphate phosphatase (Neu5Ac-9-Pase), Haloacid
  dehalogenase-like hydrolase domain-containing protein 4 (HDHD4).
- **UniProt:** Q8TBE9, 248 aa, human, chromosome 20p11.
  [file:human/NANP/NANP-uniprot.txt "RecName: Full=N-acylneuraminate-9-phosphatase"]
- **Evidence level:** PE 1 (evidence at protein level).

## Core molecular function

NANP catalyzes the third (dephosphorylation) step of the de novo sialic acid
(N-acetylneuraminate, Neu5Ac) biosynthetic pathway: it hydrolyzes
N-acetylneuraminate-9-phosphate (Neu5Ac-9-P) to free N-acetylneuraminate
(sialic acid) plus inorganic phosphate.

[file:human/NANP/NANP-uniprot.txt "Reaction=N-acetylneuraminate 9-phosphate + H2O = N-acetylneuraminate +"]

Reaction: Neu5Ac-9-P + H2O -> Neu5Ac + phosphate (Rhea:80839; EC 3.1.3.29).

The enzyme is a member of the **HAD-like (haloacid dehalogenase) hydrolase
superfamily, NANP family**.
[file:human/NANP/NANP-uniprot.txt "Belongs to the HAD-like hydrolase superfamily. NANP family."]

It also acts on the second physiological substrate,
**N-glycoloylneuraminate 9-phosphate (KDN/Neu5Gc-9-P)**:
[file:human/NANP/NANP-uniprot.txt "Can also use"]
"N-glycoloylneuraminate 9-phosphate as substrate (PubMed:14235556)".
[file:human/NANP/NANP-uniprot.txt "Reaction=N-glycoloylneuraminate 9-phosphate + H2O = N-"]

### Cofactor and mechanism

- Requires **Mg2+** as cofactor.
  [file:human/NANP/NANP-uniprot.txt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420;"]
- Crystal structures (PDB 2W4M, 4KNV, 4KNW) show a HAD Rossmann-like core with a
  Mg2+ ion and phosphate bound in the active site; Mg2+-coordinating residues at
  Asp12, Asp14, Asp189 (BINDING annotations).
  [file:human/NANP/NANP-uniprot.txt "/ligand=\"Mg(2+)\""]
- Inhibited by calcium, vanadate, sodium orthovanadate and phosphonate — hallmarks
  of a HAD-superfamily aspartate-nucleophile phosphatase.
  [file:human/NANP/NANP-uniprot.txt "Inhibited by calcium (PubMed:16237198). Inhibited"]

## Pathway placement

De novo sialic acid biosynthesis (five enzymatic steps to CMP-sialic acid):
GNE (UDP-GlcNAc 2-epimerase/ManNAc kinase) -> NANS (Neu5Ac-9-P synthase) ->
**NANP (Neu5Ac-9-P phosphatase, this gene)** -> CMAS (CMP-Neu5Ac synthetase) ->
sialyltransferases.

UniProt pathway: "Amino-sugar metabolism; N-acetylneuraminate biosynthesis."
[file:human/NANP/NANP-uniprot.txt "PATHWAY: Amino-sugar metabolism; N-acetylneuraminate biosynthesis."]

Willems et al. 2019 describe NANP as the third enzyme:
[PMID:31121216 "NANP is the third enzyme in sialic acid biosynthesis"] and note it
[PMID:31121216 "dephosphorylates sialic acid 9-phosphate to free sialic acid"].

## Key papers (all cached abstract-only; full_text_available: false)

- **PMID:14235556** (Jourdian et al. 1964, JBC) — original isolation of "sialic acid
  9-phosphatase" from human erythrocytes; UniProt FUNCTION/CATALYTIC ACTIVITY
  reference. Not in publications cache.
- **PMID:16237198** (Maliekal et al. 2006, Glycobiology) — **identified the gene**
  encoding Neu5Ac-9-Pase. Purified >1000-fold from rat liver, showed Mg2+ dependence
  and vanadate/Ca2+ inhibition placing it in the HAD family; identified HDHD4 by
  MS; recombinant human protein was >230-fold more efficient on Neu5Ac-9-P than its
  next-best substrate. Basis of the IDA annotations to GO:0050124
  (N-acylneuraminate-9-phosphatase activity) and GO:0046380 (N-acetylneuraminate
  biosynthetic process).
  [PMID:16237198 "The recombinant enzyme displayed a"] ...
  [PMID:16237198 ">230-fold higher catalytic efficiency on Neu5Ac-9-phosphate than on its second"]
- **PMID:23747226** (Kim et al. 2013, BMCL) — designed a phosphonate inhibitor of
  HDHD4; solved structures with Mg2+ and phosphate (PDB 4KNV/4KNW). Confirms
  catalytic activity, Km ~47 uM for Neu5Ac-9-P, Mg2+ cofactor, active-site basic
  residues K141/R104/R72. IDA reference for GO:0050124.
  [PMID:23747226 "inhibits"] ...
  [PMID:23747226 "the native substrate"]
- **PMID:31121216** (Willems et al. 2019, BBA Gen Subj) — **knockout study**. In two
  human cell lines, NANP KO did NOT abolish cell-surface sialylation or CMP-sialic
  acid levels (unlike GNE, NANS, CMAS KO), even though Neu5Ac-9-P substrate
  accumulated. Concludes NANP activity is **not essential** for de novo sialic acid
  production and that an alternative/bypassing phosphatase exists. IMP reference for
  GO:0006055 (CMP-N-acetylneuraminate biosynthetic process).
  [PMID:31121216 "was\nlargely unaffected in NANP (N-acylneuraminate-9-phosphatase) KO"] (note: wraps)
  [PMID:31121216 "NANP activity is not essential for"]

## Annotation review reasoning

### Core (ACCEPT)
- **GO:0050124 N-acylneuraminate-9-phosphatase activity** — three annotations
  (IDA PMID:16237198, IDA PMID:23747226, IBA GO_REF:0000033). This IS the enzyme's
  characterized catalytic activity. ACCEPT the experimental (IDA) ones as core; IBA
  is consistent. The IEA (GO_REF:0000120, from RHEA/EC mapping) is also correct but
  redundant — ACCEPT/KEEP.
- **GO:0046380 N-acetylneuraminate biosynthetic process** — IDA PMID:16237198 and
  IBA GO_REF:0000033. Correct direct BP; the free Neu5Ac product is the immediate
  output of NANP. ACCEPT.
- **GO:0005829 cytosol** — TAS Reactome. NANP is a soluble cytosolic HAD phosphatase
  (no TM/signal). Consistent. ACCEPT.

### Non-core but correct
- **GO:0006055 CMP-N-acetylneuraminate biosynthetic process** — IMP PMID:31121216.
  NANP contributes upstream of CMP-Neu5Ac formation, but the KO paper shows NANP is
  dispensable for CMP-sialic acid production (a bypass exists). The annotation
  reflects the pathway context tested (CMP-sialic acid readout), so it is defensible
  as an experimental annotation, but it is one step removed from NANP's direct
  product (free Neu5Ac, not CMP-Neu5Ac). KEEP_AS_NON_CORE. Do NOT REMOVE (IMP).
- **GO:0006054 N-acetylneuraminate metabolic process** — IEA ARBA. Correct but a
  parent of the more specific GO:0046380 already annotated. Redundant generalization.
  KEEP_AS_NON_CORE.

### Over-annotation / generic
- **GO:0016787 hydrolase activity** — IEA InterPro (IPR011950). True but maximally
  generic; the specific GO:0050124 is the informative term. MARK_AS_OVER_ANNOTATED.

### Likely wrong IEA
- **GO:0006045 N-acetylglucosamine biosynthetic process** — IEA from UniPathway
  UPA00630 mapping. UPA00630 is "N-acetylneuraminate biosynthesis" (the sialic acid
  pathway), NOT GlcNAc biosynthesis. NANP does not make GlcNAc; GlcNAc is upstream
  substrate territory. This is a UniPathway->GO mapping artifact. The correct BP is
  N-acetylneuraminate biosynthesis (already covered by GO:0046380). MODIFY to
  GO:0046380. (IEA, so MODIFY/REMOVE both permissible; MODIFY preferred to preserve
  the intended pathway meaning.)

## Core function summary (for core_functions)

1. **MF: GO:0050124 N-acylneuraminate-9-phosphatase activity** — dephosphorylates
   Neu5Ac-9-P (and Neu5Gc/KDN-9-P) to free sialic acid + Pi; Mg2+-dependent HAD
   phosphatase.
   - directly_involved_in: GO:0046380 N-acetylneuraminate biosynthetic process
   - location: GO:0005829 cytosol
2. **MF: GO:0000287 magnesium ion binding** — obligate Mg2+ cofactor at the HAD
   active site (Asp12/Asp14/Asp189).
</content>
