# Research notes: *S. pombe* ahk1 (SPAC7D4.03c / UniProt O14260)

## Summary of task
AI GO-annotation review of the understudied fission-yeast gene **ahk1** (PomBase standard
name; systematic name **SPAC7D4.03c**; UniProt **O14260**, entry name YFP3_SCHPO). This is a
"dark gene": PomBase characterisation status is **"biological role inferred"** and all of its
functional GO annotations are transferred by orthology (ISO), not experimentally determined in
*S. pombe*.

## Identity / naming (verified)
- PomBase gene page reports `name: ahk1`, `product: "MAP kinase cascade scaffold protein Ahk1"`,
  `characterisation_status: "biological role inferred"`, `deletion_viability: viable`,
  `taxonomic_distribution: fungi only` (PomBase JSON API, gene SPAC7D4.03c, latest dataset).
- UniProt O14260 (YFP3_SCHPO): `RecName: Full=UPF0592 membrane protein C7D4.03c`; 886 aa;
  `PE 3: Inferred from homology`. Belongs to the **UPF0592 family** (`-!- SIMILARITY`, ECO:0000305).
- InterPro/domain content: **Pfam PF08578 = DUF1765**; **PANTHER PTHR37988** ("UPF0592 MEMBRANE
  PROTEIN C7D4.03C"); InterPro **IPR013887 (UPF0592)**. (from ahk1-uniprot.txt DR lines and
  PomBase interpro_matches).

## Domain / topology reasoning (from ahk1-uniprot.txt)
- Predicted **multi-pass membrane protein**: three TRANSMEM helices at 277–297, 374–394, 400–420
  (all ECO:0000255, i.e. sequence-model predicted, not experimentally confirmed).
- SUBCELLULAR LOCATION: `Membrane; Multi-pass membrane protein` (ECO:0000305, inferred).
- A predicted disordered / low-complexity region at ~87–112 (MobiDB-lite).
- The single defining domain is DUF1765 (domain of unknown function); no catalytic motif, no
  recognizable kinase/phosphatase/enzymatic signature. Consistent with a non-catalytic
  scaffold/adaptor-type role rather than an enzyme.

## The orthology basis for the functional annotations (KEY)
Both functional GO annotations on S. pombe ahk1 are **ISO** (inferred from sequence orthology),
with-from **SGD:S000002231**:
- GO:0005078 "MAP kinase scaffold activity" — ISO, GO_REF:0000024, with SGD:S000002231.
- GO:0000165 "MAPK cascade" — ISO, PMID:26787842, with SGD:S000002231.
- PomBase `ortholog_annotations` lists **YDL073W** (*S. cerevisiae* AHK1) as ortholog via
  **InterPro:IPR013887** (the UPF0592 family), and **SJAG_04503** (*S. japonicus*) via
  PMID:21511999. PomBase orthogroup `SOG_0639`. (Note the curated `orthologs` list is empty; the
  cross-species relationship is captured as an InterPro-family-based ortholog_annotation, i.e. it
  is a domain-family/homology call, not a 1:1 syntenic ortholog assertion.)

*S. cerevisiae* AHK1 (YDL073W, SGD:S000002231) is a **Verified ORF** described by SGD as
"Scaffold protein in the HKR1 sub-branch of the Hog1p-signaling pathway; physically interacts with
the cytoplasmic domain of Hkr1p, and with Sho1p, Pbs2p, and Ste11p; prevents cross-talk signaling
from Hkr1p of the osmotic stress MAPK cascade to the Kss1p MAPK cascade; non-essential"
(yeastgenome.org locus S000002231).

### The single primary reference (abstract-only in cache)
[PMID:26787842 "Scaffold Protein Ahk1, Which Associates with Hkr1, Sho1, Ste11, and Pbs2,
Inhibits Cross Talk Signaling from the Hkr1 Osmosensor to the Kss1 Mitogen-Activated Protein
Kinase."] is entirely about the **budding-yeast (*S. cerevisiae*)** Ahk1:
- [PMID:26787842 "Here, using a mass spectrometric method, we identified a protein, termed Ahk1
  (Associated with Hkr1), that binds to Hkr1-cyto."]
- [PMID:26787842 "In addition to Hkr1-cyto binding, Ahk1 also bound to other signaling molecules
  in the HKR1 subbranch, including Sho1, Ste11, and Pbs2."]
- [PMID:26787842 "Thus, Ahk1 is a scaffold protein in the HKR1 subbranch and prevents incorrect
  signal flow from Hkr1 to Kss1."]
- [PMID:26787842 "In the budding yeast Saccharomyces cerevisiae, osmostress activates the Hog1
  mitogen-activated protein kinase (MAPK), which regulates diverse osmoadaptive responses."]

This paper does NOT assay the *S. pombe* protein. Cache marks `full_text_available: false`
(abstract only). The paper is the experimental basis for the *S. cerevisiae* annotation that is
then transferred to *S. pombe* by ISO.

## What phenotype data exist for *S. pombe* ahk1 (all from genome-wide / high-throughput screens)
17 single-locus (ahk1Δ) phenotypes are recorded in PomBase, all from systematic screens
(no gene-focused study). References and phenotype highlights:
- PMID:20473289 — genome-wide deletion set (Kim et al.). ahk1Δ **viable**.
- PMID:23697806 — cell-cycle/cell-shape genome-wide resource.
- PMID:28410370 — systematic screen of sexual-reproduction morphology (identifies mating/shmoo
  abnormalities): **abnormal shmoo morphology (FYPO:0000357)**, **shmoo formation at cell side
  (FYPO:0006011)**, **promiscuous mating (FYPO:0006014)**.
- PMID:34250083 — chronological lifespan barcode screen: **loss of viability in stationary phase
  (FYPO:0000245)** (ageing-associated).
- PMID:35820914 — yeast-ageing protease study.
- PMID:37787768 — broad phenomics/machine-learning functional profiling: stress sensitivities and
  resistances — sensitive to caffeine (FYPO:0000097), cycloheximide (FYPO:0000104), hydroxyurea
  (FYPO:0000088), tunicamycin (FYPO:0001457), KCl+SDS (FYPO:0007924); resistant to MMS
  (FYPO:0000725), vanadate (FYPO:0000830), lithium (FYPO:0001583), LiCl+SDS (FYPO:0009085),
  MgCl2+SDS (FYPO:0009087).

Interpretation: the deletion phenotype fingerprint (osmotic/salt/cell-wall-stress, caffeine,
mating/shmoo abnormalities) is broadly **consistent with** a role in stress-responsive signaling,
which fits the orthology-based MAPK-scaffold assignment. But NONE of these screens establishes a
molecular mechanism, a direct binding partner, or a specific, non-redundant place in the Sty1/Spc1
(Hog1-like) SAPK pathway for the *S. pombe* protein.

## KNOWN vs NOT-KNOWN
KNOWN (or well-supported):
- Fungal-only protein of the UPF0592/DUF1765 family; large (886 aa); predicted multi-pass membrane
  protein with a disordered region. (UniProt, InterPro, PANTHER.)
- Non-essential (ahk1Δ viable). (PMID:20473289.)
- Deletion perturbs stress responses and sexual-reproduction morphology in genome-wide screens.
- Its *S. cerevisiae* homolog (AHK1/YDL073W) is an experimentally validated scaffold in the HKR1
  sub-branch of the Hog1 osmostress MAPK pathway. (PMID:26787842.)

NOT KNOWN (the deliverable knowledge gaps):
- Whether *S. pombe* ahk1 actually functions as a MAPK scaffold, or is a scaffold at all — this is
  purely an orthology transfer via the shared UPF0592 domain family (IPR013887), never tested in
  *S. pombe*.
- Its direct binding partners in *S. pombe* (does it bind Sty1/Spc1, Wis1, Win1/Wak1, Sho1-like
  components, or the Wsc1/Mtl2 osmosensors?). Unknown.
- Whether it has any specific, non-redundant role in the Sty1/Spc1 SAPK pathway (the pombe
  osmostress core is Wis1→Sty1; there is no exact Hkr1/Kss1 cross-talk architecture in pombe, so
  the budding-yeast "prevents Hkr1→Kss1 cross-talk" role may not map directly).
- Its precise molecular activity (DUF1765 has no assigned biochemical function).
- Its subcellular localization in *S. pombe* (membrane prediction only; not experimentally shown).

## Curation reasoning for the annotation actions
- GO:0005078 MAP kinase scaffold activity (ISO): the only molecular-function annotation, and it is
  more informative than "protein binding". It is orthology-based and unproven in pombe, so KEEP but
  flag as inferred/non-core with an explicit knowledge gap; not REMOVE (it is a reasonable,
  curator-made ISO transfer from a verified budding-yeast scaffold, and PomBase is reliable).
- GO:0000165 MAPK cascade (ISO): same reasoning; a plausible, orthology-based process assignment;
  keep as non-core, flag as inferred.
- GO:0016020 membrane (IEA, UniProtKB-SubCell): supported by predicted TM helices; accept as a
  low-resolution, prediction-based localization (non-core).
- GO:0005575 cellular_component (ND, GO_REF:0000015): root "unknown" placeholder; standard
  PomBase practice; keep as-is (represents absence of specific CC knowledge).

## Provenance sources used
- genes/SCHPO/ahk1/ahk1-uniprot.txt (UniProt O14260)
- genes/SCHPO/ahk1/ahk1-goa.tsv (QuickGO GOA)
- publications/PMID_26787842.md (abstract-only)
- PomBase JSON API for SPAC7D4.03c (name/product/status/phenotypes/orthologs/InterPro)
- OLS (FYPO + GO term labels/definitions)
- SGD locus S000002231 (S. cerevisiae AHK1 = YDL073W)

## Deep research note
`scripts/deep_research_wrapper.py SCHPO SPAC7D4.03c falcon --fallback perplexity-lite` was run in
the foreground twice; it hung (exit 124 / 550s timeout) after emitting only the
"Using SPAC7D4.03c as gene symbol" line, producing no report. Per project policy, no
`-deep-research-*.md` file was fabricated; this review is grounded in UniProt + GOA + PomBase +
the cached publication, all with explicit provenance above.
