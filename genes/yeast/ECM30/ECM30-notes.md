# ECM30 (YLR436C / Q06673) curation notes

Journal of research for the AI GO-annotation review. ECM30 is an **understudied ("dark")
gene**: SGD classifies it as a "protein of unknown function" with molecular_function and
biological_process annotated ND. The primary deliverable of this review is therefore an
honest, sharply-delimited `knowledge_gaps` section plus carefully-reasoned, evidence-limited
`description`/`core_functions`.

## Identity and family

- UniProt entry **HID1_YEAST / Q06673**, RecName "Protein ECM30", AltName "Extracellular
  mutant protein 30". Systematic name **YLR436C**, chromosome XII. 1274 aa, 145 kDa.
  [file:yeast/ECM30/ECM30-uniprot.txt]
- Gene name origin: **"ExtraCellular Mutant"** — the ECM series comes from the Lussier et al.
  1997 calcofluor-white / cell-surface transposon-mutagenesis screen
  [PMID:9335584 "screening transposon-mutagenized cells for altered sensitivity to calcofluor
  white"]. SGD attributes the ECM30 gene name to this paper. This paper is the source of
  UniProt's FUNCTION line ("Required to form the correct cell wall composition"
  {ECO:0000269|PubMed:9335584}). NOTE: the cached PMID_9335584 is **abstract-only**
  (`full_text_available: false`); the abstract reports 82 genes but does not name ECM30
  individually — the gene-specific data are in the full text, which I have not read. Per
  curation policy I do NOT remove/contradict this experimental cell-wall attribution.
- **Family = HID1 family** (UniProt "Belongs to the hid-1 family"; Pfam **PF12722 Hid1**;
  InterPro **IPR026705 HID1/Ecm30**; PANTHER **PTHR21575 "PROTEIN HID1"**).
  [file:yeast/ECM30/ECM30-uniprot.txt]
- MNEMONIC-COLLISION CAVEAT: UniProt's mnemonic "HID1_YEAST" reflects family membership, not
  a human-disease connection. ECM30 is the *S. cerevisiae* ortholog of metazoan HID1.
- **No paralog in S. cerevisiae.** SGD lists an empty paralogs array for ECM30
  [SGD backend locus S000004428, `paralogs: []`]. (The task brief's suggestion of a paralog
  "YKL215C" is NOT supported by SGD; YKL215C = OXP1, 5-oxoprolinase, unrelated.) ECM30 is the
  single-copy yeast member of PTHR21575. By contrast *S. pombe* has **three** HID1-family
  paralogs — hid1 (SPAP27G11.12 / O13776), hid2 (Q9HDV3), hid3 (Q9P7M6)
  [file:interpro/panther/PTHR21575/PTHR21575-entries.csv].

## PANTHER family membership (PTHR21575) — reviewed members

From `interpro/panther/PTHR21575/PTHR21575-entries.csv` (8 reviewed proteins, 4027 total,
7556 taxa):

| UniProt | Protein | Organism |
|---------|---------|----------|
| Q06673 | Protein ECM30 | S. cerevisiae |
| O13776 | Hid-1 family protein hid1 | S. pombe |
| Q9HDV3 | Hid-1 family protein hid2 | S. pombe |
| Q9P7M6 | Hid-1 family protein hid3 | S. pombe |
| Q8IV36 | Protein HID1 | Human |
| Q8R1F6 | Protein HID1 | Mouse |
| D4A0C3 | Protein HID1 | Rat |
| Q54JJ6 | Protein HID1 | Dictyostelium |

## Metazoan ortholog (human HID1, Q8IV36) — for orthology reasoning ONLY

- Human HID1 FUNCTION (UniProt Q8IV36): "Plays a role in the biogenesis of large dense core
  vesicles (LDCVs) at the trans-Golgi network; necessary for the proper sorting of cargo into
  LDCVs and is required for proper regulated exocytosis (also known as regulated secretory
  pathway)." {ECO:0000269|PubMed:37751424}
  [https://rest.uniprot.org/uniprotkb/Q8IV36.txt]
- Human HID1 localization: Cytoplasm; Golgi apparatus, trans-Golgi network membrane
  (lipid-anchor); "Shuttles between the cytosol and the Golgi apparatus."
  [https://rest.uniprot.org/uniprotkb/Q8IV36.txt]
- Human HID1 experimental GO (QuickGO, Q8IV36): IDA to Golgi trans cisterna (GO:0000138),
  Golgi medial cisterna (GO:0005797), Golgi apparatus (GO:0005794), cytosol (GO:0005829);
  IMP/ISS to dense core granule biogenesis (GO:0061110); IBA to secretory granule maturation
  (GO:0061792) and Golgi organization (GO:0007030). [QuickGO annotation search Q8IV36]
- KEY CAVEAT for propagation: LDCVs / regulated dense-core secretory granules are a
  **metazoan/neuroendocrine** feature. *S. cerevisiae* has no regulated dense-core secretory
  pathway, so the metazoan-specific processes/compartments of HID1 do NOT transfer wholesale.
  The conserved element is more plausibly a general Golgi-associated membrane-trafficking role.

## What is KNOWN about ECM30 (evidence-anchored)

1. **Subcellular localization: cytoplasm** (cytosolic), from GFP-fusion high-throughput
   analysis [PMID:14562095 (Huh et al. global GFP localization); GOA HDA GO:0005737]. UniProt
   SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:14562095}. Consistent with the human
   ortholog's cytosol↔Golgi shuttling (peripheral, not integral membrane).
2. **Cell-wall phenotype** (source of the gene name): ecm30 mutants show altered calcofluor-
   white sensitivity and abnormal relative levels of mannose and glucose [PMID:9335584; SGD
   description "may play a role in cell wall biosynthesis, mutants have abormal relative
   levels of mannose and glucose"].
3. **Gap1p (general amino acid permease) sorting and transport defects** in ecm30 mutants
   [SGD locus description, S000004428: "have Gap1p sorting and transport defects"]. This is a
   membrane-cargo intracellular-sorting phenotype (Gap1 traffics TGN → endosome → vacuole vs
   plasma membrane depending on nitrogen source). I could not resolve a single primary PMID
   naming ECM30 for this Gap1 defect from public search; recording it as an SGD-curated
   free-text phenotype, not asserting a specific citation.
4. **Genetic interaction network centered on membrane trafficking** (SGD interaction_details,
   BioGRID; n=87 genetic partners). Notable, functionally coherent hits:
   - **GET pathway**: GET1 (Phenotypic Suppression), GET2 (Negative Genetic + Phenotypic
     Suppression), GET3 (Phenotypic Suppression) — tail-anchored membrane-protein insertion
     at the ER.
   - **Golgi/secretory**: ARL1 (Phenotypic Enhancement; Golgi Arf-like GTPase), SEC14
     (Synthetic Growth Defect; TGN PI/PC transfer protein), SEC26 & SEC28 (Negative Genetic;
     COPI coatomer subunits).
   - **Vacuolar/endosomal sorting**: VPS1 (dynamin), VPS9, VPS17 (retromer).
5. **Physical interactions** (SGD/BioGRID, n=30 physical partners; mostly single-method
   high-throughput AC-MS). Trafficking-relevant: **LAA1** (Affinity Capture-MS; TGN AP-1
   clathrin-adaptor-associated / AP-3 accessory), **VAM6/VPS39** (Affinity Capture-MS; HOPS
   tethering complex, vacuole fusion), **UBP15** (AC-MS + AC-Western; ubiquitin protease).
   Many other AC-MS hits (histones HHT1/HHT2/HTB1/HTB2, RNA-binding CAF20/PUF2/PUF3/DHH1,
   Pol II RPO21) are typical abundant-protein / RNA-tethered background for a large 145 kDa
   cytosolic protein and are not treated as functional.
6. **Post-translational modification**: phosphoserine at Ser635 and Ser1065 (large-scale
   phosphoproteomics) [UniProt MOD_RES; PMID:17330950, PMID:18407956, PMID:19779198]. Ser1065
   is a mitotic/Cdk1-context site (Holt et al.). Regulatory significance unknown.
7. **Sequence architecture**: 1274 aa, HID1 α-solenoid-type fold (Pfam Hid1 ×2 across the
   protein), multiple internal disordered/low-complexity stretches (MobiDB-lite regions at
   ~23-42, 405-439, 494-517, 803-842, 1100-1149). No transmembrane domain, no signal peptide,
   no catalytic-domain signature → consistent with a peripheral/cytosolic scaffold rather than
   an enzyme or integral membrane protein. [file:yeast/ECM30/ECM30-uniprot.txt]

## What is NOT known (the real gaps)

- **Molecular function (MF-dark).** No biochemical activity assigned; SGD/UniProt MF = ND.
  The HID1 fold has no catalytic assignment in any organism. Whether ECM30 acts as a
  membrane-trafficking scaffold/adaptor (like human HID1 at the TGN) is inferred, not shown.
- **Direct molecular partners.** No validated, specific binding partner defines its activity;
  the AC-MS hits are unfiltered high-throughput. The mechanistic link to LAA1/GET/ARL1 is
  genetic/HT-physical, not a defined complex.
- **Biological role / mechanism of the cell-wall phenotype.** Why an ecm30 null perturbs
  cell-wall mannose/glucose and calcofluor sensitivity is unexplained — likely indirect via
  mis-sorting of cell-wall-biosynthetic cargo (cf. Gap1 mis-sorting), but this is a
  hypothesis, not established.
- **Whether the metazoan HID1 Golgi/secretory role is conserved in yeast.** ECM30 localizes
  to cytoplasm in the one HT study; it has no experimental Golgi localization in yeast. The
  IBA Golgi-cisterna/Golgi-organization annotations derive from metazoan orthologs performing
  a process (regulated dense-core secretion) that S. cerevisiae lacks.
- **Redundancy / genetic buffering.** ECM30 is non-essential and single-copy in S. cerevisiae
  (no paralog), yet the null is only modestly sick — implies functional buffering by parallel
  trafficking pathways rather than a dedicated paralog.

## GO annotation review plan (existing_annotations, 9 total)

| # | term | evid | source | plan |
|---|------|------|--------|------|
| 1 | GO:0005829 cytosol | IBA | GO_REF:0000033 (PANTHER PTN000491103) | ACCEPT (KEEP_AS_NON_CORE): cytosolic localization is consistent with HT GFP data & human ortholog cytosol pool. |
| 2 | GO:0016020 membrane | IBA | GO_REF:0000033 | MARK_AS_OVER_ANNOTATED: uninformative root-ish CC; ECM30 has no TM and is peripheral at best; propagated from membrane-associated metazoan HID1. |
| 3 | GO:0007030 Golgi organization | IBA | GO_REF:0000033 | MARK_AS_OVER_ANNOTATED: metazoan-HID1-derived; no yeast evidence ECM30 organizes the Golgi; yeast lacks the regulated-secretion context. |
| 4 | GO:0000138 Golgi trans cisterna | IBA | GO_REF:0000033 | MARK_AS_OVER_ANNOTATED: from human HID1 IDA at TGN; ECM30 localizes cytoplasm in yeast, no yeast Golgi-cisterna evidence. |
| 5 | GO:0005797 Golgi medial cisterna | IBA | GO_REF:0000033 | MARK_AS_OVER_ANNOTATED: same as #4; overly specific metazoan compartment. |
| 6 | GO:0005737 cytoplasm | IEA | GO_REF:0000044 (UniProt SubCell) | ACCEPT/KEEP_AS_NON_CORE: matches HDA + UniProt SUBCELLULAR LOCATION. |
| 7 | GO:0005737 cytoplasm | HDA | PMID:14562095 | ACCEPT (best-supported localization; experimental HT GFP). |
| 8 | GO:0003674 molecular_function | ND | GO_REF:0000015 | ACCEPT: correctly records MF-dark status (root ND). |
| 9 | GO:0008150 biological_process | ND | GO_REF:0000015 | ACCEPT: correctly records BP-dark status (root ND). |

Rationale for the Golgi IBA calls: I am NOT removing an experimental annotation. These are
**IBA electronic** inferences over-propagated from metazoan HID1 (dense-core-vesicle
biogenesis at the TGN), a process absent in S. cerevisiae. Per CLAUDE.md, over-propagated
IEA/IBA inferences that can be argued against on biological grounds are legitimate
MARK_AS_OVER_ANNOTATED / MODIFY candidates. I keep cytosol/cytoplasm (supported) and record
the honest dark-gene status via the ND roots and the knowledge_gaps section.

## Deep research status

Automated deep research did not yield a provider file. Falcon (Edison) timed out at 600s
on the initial run and again on a single retry (the shared Edison endpoint was saturated by
many concurrent sibling jobs at the time); the perplexity-lite fallback returned HTTP 401
(quota exhausted). No `-deep-research-{provider}.md` file was produced. This review is
therefore grounded directly in primary/curated sources: the UniProt record (Q06673), the
GOA TSV, cached publications (PMID:9335584, PMID:14562095, and the phosphoproteomics PMIDs),
the SGD locus record (S000004428: description, phenotypes, interactions, empty paralog list),
the PANTHER PTHR21575 family membership file, QuickGO annotations for the human ortholog HID1
(Q8IV36), and the human HID1 UniProt FUNCTION/localization. All assertions above carry inline
provenance. Per project policy, no self-authored content is named as a provider deep-research
file.
