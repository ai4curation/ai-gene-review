# GMPS (human) — curation notes

UniProtKB: P49915 (GUAA_HUMAN). HGNC:4378. Gene ID 8833. 693 aa, chromosome 3.

## Core function

GMPS is **GMP synthase [glutamine-hydrolyzing]** (GMP synthetase; EC 6.3.5.2), the
enzyme catalysing the **final, committed step of de novo guanine-nucleotide
biosynthesis**: the ATP-dependent amination of xanthosine-5'-monophosphate (XMP)
to guanosine-5'-monophosphate (GMP), using the amide nitrogen of L-glutamine.

Reaction (UniProt CATALYTIC ACTIVITY, Rhea:11680):
`XMP + L-glutamine + ATP + H2O = GMP + L-glutamate + AMP + diphosphate + 2 H(+)`
[file:human/GMPS/GMPS-uniprot.txt: "Reaction=XMP + L-glutamine + ATP + H2O = GMP + L-glutamate + AMP + diphosphate + 2 H(+)"]

It acts immediately downstream of IMP dehydrogenase (IMPDH1/2), which oxidises IMP
to XMP; GMPS then aminates XMP to GMP. UniProt PATHWAY: "Purine metabolism; GMP
biosynthesis; GMP from XMP (L-Gln route): step 1/1."

Two-domain architecture (UniProt features):
- Glutamine amidotransferase type-1 (GATase) domain, res 27–216 (ACT_SITE Cys104,
  His190, Glu192) — hydrolyses glutamine to release ammonia.
- GMPS ATP-PPase domain, res 217–435 (ATP binding 244–250) — adenylates XMP, then the
  ammonia attacks the adenyl-XMP intermediate to form GMP.
[UniProt FUNCTION: "Catalyzes the conversion of xanthine monophosphate (XMP) to GMP in
the presence of glutamine and ATP through an adenyl-XMP intermediate."]

Cofactor: Mg2+ required (essential activator beyond ATP chelation)
[PMID:7706277 abstract, "Magnesium ion is required for enzyme activity, and the
requirement is beyond levels needed for ATP chelation."].

## Key primary literature (cached; both abstract-only)

- **PMID:8089153** (Hirst, Haliday, Nakamura, Lou 1994, JBC) — purification to
  homogeneity, cDNA cloning, functional expression; complements an *E. coli* guaA
  mutant. Establishes FUNCTION, CATALYTIC ACTIVITY, and cytosolic localization. This is
  the UniProt EC evidence (ECO:0000269|PubMed:8089153).
- **PMID:7706277** (Nakamura & Lou 1995, JBC) — biochemical/kinetic characterization:
  Mg2+ requirement, sigmoidal XMP kinetics (Hill 1.48), decoyinine inhibition. GOA has
  this as the EXP evidence for GO:0003922 (via Reactome).

## Structure / quaternary state

- Crystal structure PMID:23816837 (Welin et al. 2013, PDB 2VXO/2VPI): reports GMPS is a
  **homodimer** (UniProt SUBUNIT: "Homodimer"). Note the earlier kinetic paper
  (PMID:7706277) reported the enzyme behaves as a **monomer** in solution during
  catalysis; Reactome R-HSA-73792 still describes GMPS as a monomer. Oligomeric state is
  thus debated but not central to the MF/BP annotations. Reactome R-HSA-9748957
  ("GMPS dimer transforms 6TXMP to 6TGMP") uses the dimer description for the
  thiopurine-activation reaction.

## Moonlighting / non-core

- GMPS has a reported nuclear moonlighting role in **USP7 (HAUSP)-mediated
  deubiquitination that stabilizes p53** (and in Drosophila, USP7-dependent regulation of
  histone H2B / epigenetic silencing). No GOA line covers this, so it appears only in the
  top-level `description` and is treated as **non-core**. Not annotated here (no term in
  GOA to review).

## Disease / clinical

- No common Mendelian disease. UniProt DISEASE note: recurrent chromosomal translocation
  t(3;11)(q25;q23) fusing KMT2A/MLL1 with GMPS in treatment-related AML
  (PMID:11110714) — a gene-fusion partner event, not an enzymatic-function annotation.
- Pharmacology: activates thiopurine prodrugs (azathioprine / 6-mercaptopurine →
  6-thioGMP; Reactome R-HSA-9748957, R-HSA-9748787). DrugBank links Azathioprine,
  L-Glutamine, Glutamic acid.

## GOA review summary

18 GOA lines. All are consistent with the single, well-supported function (GMP synthase)
+ cytosolic localization + de novo GMP/purine biosynthesis. No wrong-branch or
contradicted annotations.

Notable citation issue: **PMID:8081953** is the `original_reference_id` for the
`GO:0003921 GMP synthase activity` IDA line (assigned by MGI). The cached record for
PMID:8081953 is "Enhanced in vitro growth of glomerular cells derived from rats with
immune-mediated mesangial injury" (Harendza et al. 1993, Exp Nephrol) — a paper with
**no relation to GMP synthase**. This is a wrong-identifier / transposed-PMID citation.
The annotated *function* (GMP synthase activity for GMPS) is nonetheless correct and
independently supported (PMID:8089153, IBA), so the annotation is ACCEPTed while the
reference is flagged WRONG_IDENTIFIER in `reference_review`. (The correct MGI-style
reference is almost certainly PMID:8089153, the GMP synthetase cloning paper.)

Broader BP terms (GO:0006164 purine nucleotide biosynthetic process; GO:0009168 purine
ribonucleoside monophosphate biosynthetic process; GO:0009113 purine nucleobase
biosynthetic process) are all correct parents of the GMP biosynthesis role — kept but
noted as broader / non-core relative to GO:0006177 GMP biosynthetic process.
