# GGCT (gamma-glutamylcyclotransferase) review notes

UniProt: O75223 (GGCT_HUMAN). Synonyms: C7orf24, CRF21. HGNC:21705. 188 aa cytosolic
protein. EC 4.3.2.9 (lyase). Human, NCBITaxon:9606.

## Core biochemistry (γ-glutamyl cycle)

GGCT is the gamma-glutamylcyclotransferase of the γ-glutamyl cycle / glutathione turnover.
It acts on the γ-glutamyl-amino acids produced by GGT1 (γ-glutamyl transpeptidase), converting
an (L-γ-glutamyl)-L-amino acid to **5-oxo-L-proline (pyroglutamate) + the free L-amino acid**
by intramolecular cyclization. The 5-oxoproline is subsequently reconverted to glutamate by
OPLAH (5-oxoprolinase), closing the cycle and recycling glutamate for glutathione (GSH) synthesis.

- UniProt CATALYTIC ACTIVITY (RHEA:20505, EC 4.3.2.9):
  "Reaction=an alpha-(gamma-L-glutamyl)-L-amino acid = 5-oxo-L-proline + an L-alpha-amino acid"
  [file:human/GGCT/GGCT-uniprot.txt].
- UniProt FUNCTION: "Catalyzes the formation of 5-oxoproline from gamma-glutamyl dipeptides and
  may play a significant role in glutathione homeostasis (PubMed:18515354)."
  [file:human/GGCT/GGCT-uniprot.txt].

### Enzymatic identification and structure (PMID:18515354, Oakley et al. 2008, JBC)
The definitive functional identification. C7orf24 identified as GGCT; recombinant enzyme
crystallized at 1.7 Å; homodimer of ~21-kDa (20,994-Da) subunits; active-site Glu98 acts as
general acid/base (E98A/E98Q abolish activity without altering fold). This is the source of the
IDA gamma-glutamylcyclotransferase-activity annotation and one IDA homodimer annotation.
- [PMID:18515354 "catalyzes the formation of 5-oxoproline (pyroglutamic acid) from gamma-glutamyl dipeptides and potentially plays a significant role in glutathione homeostasis"]
- [PMID:18515354 "The enzyme is a dimer of 20,994-Da subunits"]
- [PMID:18515354 "Mutation of Glu(98) to Ala or Gln completely inactivates the enzyme without altering the overall fold"]
- full_text_available: false (abstract cached); the abstract already states catalytic activity and dimer.

### Crystal structure (PMID:17932939, Bae et al. 2008, Proteins)
Structural-genomics crystal structure of "Homo sapiens protein LOC79017" (= GGCT). Cached record
is abstract-only (no body text). UniProt attributes the SUBUNIT=Homodimer assertion partly to this
paper (ECO:0000305|PubMed:17932939). Source of one IDA protein-homodimerization annotation.
- UniProt SUBUNIT: "Homodimer." {ECO:0000305|PubMed:17932939, ECO:0000305|PubMed:18515354}
  [file:human/GGCT/GGCT-uniprot.txt].

## Location

Cytosolic enzyme.
- UniProt DR GO: "GO:0005829; C:cytosol; IDA:UniProtKB" [file:human/GGCT/GGCT-uniprot.txt].
- Reactome R-HSA-1247922 ("GGCT transforms gGluCys to OPRO") places the reaction in cytosol; source
  of the TAS cytosol annotation.
- PMID:16765912 purified the 21-kDa protein (CRF21 = GGCT) from the **cytosolic fraction** of U937
  cells — supports cytosol IDA.
  [PMID:16765912 "a 21-kDa cytochrome c-releasing factor that appears in the cytosolic fraction"]

## Cytochrome c release / apoptosis (PMID:16765912, Masuda et al. 2006, BBRC)
Independent of the enzymology, GGCT was purified as "cytochrome c-releasing factor 21" (CRF21):
overexpression in HeLa induced release of cytochrome c from mitochondria and apoptosis; it was
induced by geranylgeraniol (GGO) in U937 leukemia cells. This is the basis of the
GO:0001836 (release of cytochrome c from mitochondria) IMP annotation.
- [PMID:16765912 "Overexpression of CRF21 in HeLa cells induced the release of cytochrome c from mitochondria, with subsequent apoptosis"]
- full_text_available: false (abstract cached).
- Assessment: This is an experimental (IMP) annotation and is retained, but it is an
  overexpression/context-specific pro-apoptotic phenotype, not the core γ-glutamyl-cycle enzyme
  function, so it is kept as NON_CORE. Do NOT REMOVE (experimental annotation).

## Exosome (PMID:19056867, Gonzales et al. 2009, JASN)
Large-scale LC-MS/MS proteomics of human **urinary exosomes**; GGCT was one of 1132 proteins
detected. This is high-throughput mass-spec detection (HDA), typical of an abundant cytosolic
enzyme captured in exosome preparations, not evidence of a functional extracellular/exosomal role.
Marked as over-annotation (cytosol is the physiological location).
- [PMID:19056867 "the analysis identified 1132 proteins unambiguously"]
- full_text_available: false (abstract cached).

## Cancer-associated antigen context
GGCT (C7orf24) has been studied as a cancer-associated / proliferation marker antigen, but its
core molecular function remains gamma-glutamylcyclotransferase activity in the γ-glutamyl cycle.
Not annotated as core; noted for completeness (UniProt AltName reflects the CRF21 apoptosis name;
the C7orf24 "cancer marker" framing is mentioned in PMID:18515354 intro).
- [PMID:18515354 "The hypothetical protein C7orf24 has been implicated as a cancer marker with a potential role in cell proliferation"]

## Core function summary
- MF: gamma-glutamylcyclotransferase activity (GO:0003839) — verified current label via OLS.
- BP: glutathione catabolic process (GO:0006751) — GGCT breaks down γ-glutamyl dipeptides in the
  glutathione recycling arm of the γ-glutamyl cycle (also fits glutathione metabolic process
  GO:0006749; catabolic is the more specific correct branch). Not glutathione *biosynthetic*
  (GO:0006750) — GGCT does not synthesize GSH.
- CC: cytosol (GO:0005829).

## Action tally
- ACCEPT: GO:0003839 IBA, GO:0003839 IEA, GO:0003839 IDA, GO:0005829 TAS, GO:0005829 IDA (5)
- KEEP_AS_NON_CORE: GO:0001836 IMP, GO:0042803 IDA x2 (3)
- MARK_AS_OVER_ANNOTATED: GO:0070062 HDA exosome (1)
</content>
</invoke>
