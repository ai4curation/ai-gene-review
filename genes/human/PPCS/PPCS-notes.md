# PPCS (human, Q9HAB8) — gene review notes

## Identity

- Gene: **PPCS** (HGNC:25686); synonym **COAB**. UniProt **Q9HAB8** (PPCS_HUMAN), 311 aa.
- Name: **Phosphopantothenate--cysteine ligase** (RecName); AltName **Phosphopantothenoylcysteine synthetase / PPC synthetase**. EC **6.3.2.51**.
  [file:human/PPCS/PPCS-uniprot.txt "RecName: Full=Phosphopantothenate--cysteine ligase"], [file:human/PPCS/PPCS-uniprot.txt "AltName: Full=Phosphopantothenoylcysteine synthetase"]
- Evidence at protein level (PE 1). Two isoforms by alternative splicing (isoform 2 = Q9HAB8-2, VSP_045796 lacks residues 1-173).

## Function (core)

- **Second step of CoA biosynthesis from vitamin B5 (pantothenate).** Conjugates L-cysteine to 4'-phosphopantothenate to form 4-phosphopantothenoylcysteine.
  [file:human/PPCS/PPCS-uniprot.txt "Catalyzes the second step in the biosynthesis of coenzyme A"], [PMID:29754768 "Phosphopantothenoylcysteine synthetase (PPCS) catalyzes the second step of the pathway during which phosphopantothenate reacts with ATP and cysteine to form phosphopantothenoylcysteine."]
- **Prefers ATP over CTP** as the nucleotide cosubstrate (mammalian enzyme differs from the CTP-dependent bacterial CoaB).
  [file:human/PPCS/PPCS-uniprot.txt "Has a preference for ATP over CTP as"], [reactome:R-HSA-196753 "Mammalian PPCS prefers ATP to CTP, unlike the E. coli ortholog"]
- Two catalytic-activity entries in UniProt: ATP-dependent (RHEA:25156, canonical for EC 6.3.2.51) and CTP-dependent (RHEA:19397). Both give N-[(R)-4-phosphopantothenoyl]-L-cysteine + NMP + diphosphate + H+.
- Pathway: **Cofactor biosynthesis; coenzyme A biosynthesis; CoA from (R)-pantothenate: step 2/5** (UniPathway UPA00241, UER00353).
  [file:human/PPCS/PPCS-uniprot.txt "coenzyme A biosynthesis; CoA from (R)-"]

### Direct experimental support

- **PMID:11923312 (Daugherty et al. 2002, J Biol Chem)** — reconstituted the human CoA pathway; PPCS overexpressed/purified and activity verified. Basis for the IDA on GO:0004632 and GO:0015937. Abstract-only cache (`full_text_available: false`).
  [PMID:11923312 "The individual human enzymes were overexpressed in E. coli and purified, and the corresponding activities were experimentally verified."], [PMID:11923312 "the entire pathway from phosphopantothenate to CoA was successfully reconstituted in vitro using a mixture of purified recombinant enzymes"]
- **PMID:12906824 (Manoj et al. 2003, Structure)** — 2.3 Å crystal structure of human PPCS; homodimer. Cited in UniProt RN [9] (FUNCTION, HOMODIMERIZATION). Not separately in GOA but underpins the homodimer/catalytic-complex annotations. (Referenced via UniProt; cache not present, title taken verbatim from UniProt reference record.)

## Structure / subunit

- **Homodimer**; active site at the dimer interface. CoaB-like fold (Gene3D 3.40.50.10300; SUPFAM SSF102645).
  [file:human/PPCS/PPCS-uniprot.txt "SUBUNIT: Homodimer."]
- Self-interaction also captured in the HuRI binary interactome map (PMID:32296183, IntAct) → GO:0042802 identical protein binding.

## Localization

- **Cytosol** (Reactome TAS, R-HSA-196753). CoA pathway steps occur in cytosol / mitochondrial intermembrane space.
  [reactome:R-HSA-196753 "is catalyzed by cytosolic phosphopantothenate-cysteine ligase (PPCS aka Phosphopantothenoylcysteine synthase or PPC synthase)"]
- IBA nucleus (GO:0005634) is an ancestral phylogenetic call not supported by the human data → marked over-annotated.

## Disease

- **CMD2C = dilated cardiomyopathy, autosomal recessive** (MIM:618189), caused by biallelic PPCS variants (107-111del, A180P, E233V), which reduce/abolish ligase activity and decrease protein abundance and cellular CoA.
  [file:human/PPCS/PPCS-uniprot.txt "A form of\nCC       dilated cardiomyopathy"] (paraphrase; see UniProt DISEASE block), [PMID:29754768 "biallelic mutations in PPCS, linking CoA synthesis with a cardiac phenotype"], [PMID:29754768 "Biochemical analysis revealed a decrease in CoA levels in fibroblasts of all affected individuals."]
- Pantethine (a PPCS-independent CoA source) proposed as targeted treatment.
  [PMID:29754768 "CoA biosynthesis can occur with pantethine as a source independent from PPCS, suggesting pantethine as targeted treatment"]

## Annotation review decisions (summary)

- **ACCEPT (core MF):** GO:0004632 phosphopantothenate--cysteine ligase activity — IDA (11923312), IMP (29754768), IEA, IBA.
- **ACCEPT (core BP):** GO:0015937 coenzyme A biosynthetic process — IDA, IMP, NAS, IEA, IBA.
- **ACCEPT (core CC):** GO:0005829 cytosol — TAS Reactome.
- **ACCEPT (MF, catalysis-linked):** GO:0042803 protein homodimerization activity — IMP (obligate homodimer, active site at interface).
- **KEEP_AS_NON_CORE:** GO:0005737 cytoplasm (IBA, general vs cytosol); GO:0042802 identical protein binding (IPI HuRI, = homodimer); GO:1902494 catalytic complex (IPI, homodimer); GO:0003015 heart process (IMP, disease phenotype, downstream of CoA loss).
- **MARK_AS_OVER_ANNOTATED:** GO:0005634 nucleus (IBA, wrong compartment for human enzyme); GO:0006085 acetyl-CoA biosynthetic process (IMP, downstream of the CoA pool, not a direct PPCS role — accurate term is GO:0015937). Neither REMOVED (nucleus is IBA and defensibly over-annotated, but per policy over-annotation is preferred; acetyl-CoA is IMP/experimental so never REMOVE).

## Core function IDs (author-supplied, branch-validated)

- GO:0004632 phosphopantothenate--cysteine ligase activity (MF; acid-amino acid ligase branch) — verified current label + MF-branch via local go.db.
- GO:0042803 protein homodimerization activity (MF) — verified.
- Supporting: directly_involved_in GO:0015937 (BP); location GO:0005829 cytosol (CC).

## Provenance / caveats

- Publications PMID_11923312 and PMID_29754768 are **abstract-only** in the local cache (`full_text_available: false`; the latter's Full Text section is empty). All PMID `supporting_text` quotes above and in the review YAML are verbatim from the cached abstracts.
- GO term labels for all core_functions and reviewed terms confirmed current against local `~/.data/oaklib/go.db` (2026-07 build).
- `just validate human PPCS` → ✓ Valid.
