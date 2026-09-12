# ppgn-1 (Y38F2AR.7 / WBGene00021425 / UniProt G5EDB6) — research notes

Research journal for the AI GO-annotation review. Provenance is recorded inline as
`[PMID:xxxx "verbatim quote"]`. This is a **dark gene**: the deliverable is a precise,
defensible statement of what is and is not known.

## 1. Identity (verified from the UniProt record)

- UniProt **G5EDB6** (TrEMBL, unreviewed), *Caenorhabditis elegans*, NCBITaxon:6239.
- Gene symbol **ppgn-1**; ORF **Y38F2AR.7**; WormBase **WBGene00021425**; RefSeq NP_500191.3.
- Protein name (UniProt SubName): **Paraplegin**. 747 aa, 82.8 kDa.
- The *only* primary reference on the UniProt entry is an unpublished nucleotide-sequence
  submission: Yamanaka, Yamada-Inagawa, Nishizono, Ogura (2006), title "Paraplegin
  homologue in C. elegans" (EMBL AB257343 / BAE96353.1). No functional paper.
- Domain architecture (UniProt/InterPro): N-terminal **AAA+ ATPase** module
  (AAA+ core IPR003959; AAA_lid_3 IPR041569; SMART AAA domain 317–462) and C-terminal
  **peptidase M41** zinc-metallopeptidase module (IPR000642). Two predicted TM helices
  (Phobius: 111–133 and 225–245). N-terminal disordered/basic region 41–101 (matrix
  targeting/presequence-like). Cofactor Zn²⁺ (ARBA). SubCellular: Mitochondrion,
  multi-pass membrane protein.
- PANTHER classification: **PTHR43655** "ATP-DEPENDENT PROTEASE", subfamily
  **PTHR43655:SF8 PARAPLEGIN**. MEROPS peptidase clan/family **M41.A12**.
- Reactome (electronic, projected): R-CEL-8949664 "Processing of SMDT1";
  R-CEL-9837999 "Mitochondrial protein degradation".

**Bottom line on identity:** despite the surrounding project framing, ppgn-1 is NOT an
epidermal/innate-immune/wound gene. It is the *C. elegans* **paraplegin-subfamily
subunit of the mitochondrial m-AAA protease** — an ATP-dependent, membrane-embedded
zinc metalloprotease of the inner mitochondrial membrane. All curation below is against
that identity.

## 2. What the m-AAA protease family does (KNOWN — orthologue/family biology)

The family is well characterised in yeast, mouse and human; ppgn-1's GO annotations are
IBA/IEA propagations from these orthologues.

- m-AAA proteases are a conserved, membrane-bound, ATP-dependent proteolytic machine of
  the mitochondrial inner membrane that performs protein quality control:
  [PMID:16239145 "AAA proteases comprise a conserved family of membrane bound ATP-dependent proteases that ensures the quality control of mitochondrial inner-membrane proteins"].
- Human **paraplegin** (SPG7) is a bona fide subunit of this complex, and the complex is
  ATP-dependent: [PMID:16647881 "paraplegin, which is a conserved subunit of the ubiquitous and ATP-dependent m-AAA protease in mitochondria"]
  and [PMID:16647881 "The m-AAA protease carries out protein quality control in the inner membrane of the mitochondria"].
- The founding paper established paraplegin as a nuclear-encoded mitochondrial
  metalloprotease homologous to the yeast AAA ATPases with dual proteolytic + chaperone
  activity: [PMID:9635427 "Paraplegin is highly homologous to the yeast mitochondrial ATPases, AFG3, RCA1, and YME1, which have both proteolytic and chaperon-like activities at the inner mitochondrial membrane"]
  and localises to mitochondria: [PMID:9635427 "Immunofluorescence analysis and import experiments showed that Paraplegin localizes to mitochondria"].
- Besides bulk degradation, the m-AAA protease has a **regulated processing** role: it
  matures specific substrates. The conserved paradigm is maturation of the ribosomal
  protein MrpL32: [PMID:16239145 "The mitochondrial ribosomal protein MrpL32 is processed by the m-AAA protease, allowing its association with preassembled ribosomal particles and completion of ribosome assembly in close proximity to the inner membrane"].
  This dual degrade-vs-process behaviour is explicit in the literature:
  [PMID:21610694 "m-AAA proteases exert dual functions in the mitochondrial inner membrane: they mediate the processing of specific regulatory proteins and ensure protein quality control degrading misfolded polypeptides to peptides"].
- Loss of function is pleiotropic across organisms (respiration, mito morphology, axon
  degeneration): [PMID:16239145 "Inactivation of AAA proteases causes pleiotropic phenotypes in various organisms, including respiratory deficiencies, mitochondrial morphology defects, and axonal degeneration in hereditary spastic paraplegia (HSP)"].
- In mammals the physiological complex is a hetero-/homo-hexamer of paraplegin (SPG7)
  and/or AFG3L2 (WITH/FROM of the ppgn-1 IBA annotations lists human SPG7 = UniProtKB
  Q9UQ90 and AFG3L2 = UniProtKB Q9Y4W6, plus mouse Afg3l1/Afg3l2 and yeast Yta10/Yta12).

## 3. Bioinformatic verification for THIS protein (KNOWN — from ppgn-1 sequence)

To guard against propagating enzyme annotations onto a possible pseudoenzyme, I scanned
the ppgn-1 sequence itself (see `ppgn-1-bioinformatics/`, reproducible
`analyze_motifs.py`). All three catalytic motifs are intact and correctly ordered:

- Walker A / P-loop **GPPGCGKT** at 325 (ATP binding).
- Walker B **IIYIDE** at 380 (Mg-ATP hydrolysis).
- **HExxH** zinc-binding catalytic motif **HEAGH** at 555, within the M41 domain,
  followed downstream by an acidic residue (…MLEHT**D**) — a complete FtsH-type Zn²⁺
  active site.

Interpretation: ppgn-1 is a **catalytically competent** m-AAA protease at the sequence
level, not a degenerate pseudoenzyme. This supports the enzymatic GO terms for this
specific protein, not merely by family membership. See
`file:worm/ppgn-1/ppgn-1-bioinformatics/RESULTS.md`.

## 4. C. elegans context — and the paralog trap (NOT-known for ppgn-1)

- *C. elegans* has (at least) two m-AAA protease subunit genes: the well-studied
  **spg-7** (WBGene00004978; the AFG3L2-type subunit, and the gene whose RNAi is the
  canonical trigger of the mitochondrial unfolded-protein response, UPR^mt, and of
  detoxification/immune gene induction — WormBase/literature summaries) and the
  understudied **ppgn-1** (paraplegin subfamily, this gene).
- **Crucial curation caveat:** the large *C. elegans* mitochondrial-protease functional
  literature (UPR^mt, drug resistance, detoxification, pathogen resistance) is about
  **spg-7**, NOT ppgn-1. None of it can be attributed to ppgn-1. The GOA annotations for
  ppgn-1 are correctly all IBA/IEA (no experimental evidence code), reflecting this.
- WITH/FROM of the ppgn-1 IBA annotations includes WB:WBGene00004978 (spg-7) as a
  co-orthologue in the PANTHER tree, i.e. the two worm genes are placed together in the
  m-AAA clade.

## 5. Explicit KNOWN vs NOT-known ledger for ppgn-1

KNOWN (high confidence, from orthology + domain/motif evidence):
- Encodes a paraplegin-subfamily m-AAA protease subunit (AAA+ ATPase + M41 Zn-peptidase).
- Retains intact ATP-binding (Walker A), ATP-hydrolysis (Walker B) and Zn-peptidase
  (HExxH) catalytic motifs → catalytically competent in principle.
- Predicted mitochondrial, integral inner-membrane (two TM helices), matrix-facing
  catalytic domains — the canonical m-AAA topology.
- Family function: ATP-dependent proteolytic quality control + regulated processing of
  inner-membrane / matrix substrates.

NOT KNOWN (the real gaps for ppgn-1 specifically):
- **No** *C. elegans* experimental characterisation of ppgn-1: no mutant/RNAi phenotype,
  no localisation, no biochemistry has been reported for this gene (all GO evidence is
  IBA/IEA; the only UniProt reference is an unpublished sequence submission).
- **Substrates unknown**: which inner-membrane proteins ppgn-1 degrades or matures in the
  worm is undetermined (no worm equivalent of the MrpL32 result attributed to ppgn-1).
- **Complex composition unknown**: whether ppgn-1 assembles with the AFG3L2-type subunit
  spg-7 into a hetero-hexamer, forms a homo-oligomer, or is catalytically redundant with
  spg-7 is untested.
- **Physiological role unknown**: whether ppgn-1 (as opposed to spg-7) contributes to
  UPR^mt, respiration, mitochondrial morphology, fertility, longevity, stress/pathogen
  responses, or is functionally dispensable, is unknown.
- **Regulation unknown**: expression, tissue distribution (Bgee: "Expressed in germ line
  and 4 other cell types" — coarse, electronic), and conditions under which it acts are
  uncharacterised.

## 6. Annotation-review plan (summary)

All 10 GOA annotations are IBA/IEA and are consistent with a catalytically competent
paraplegin-subfamily m-AAA protease; none is contradicted, so none is REMOVEd.
- Core, well-supported family propagations → ACCEPT: mitochondrial protein processing
  (IBA), m-AAA complex (IBA), metalloendopeptidase activity (IBA + IEA), ATP-dependent
  peptidase activity (IEA), ATP binding (IEA), ATP hydrolysis activity (IEA).
- Correct but non-specific / non-core → KEEP_AS_NON_CORE with a note: proteolysis
  (GO:0006508, generic parent of the specific processing/QC role), mitochondrion
  (GO:0005739, generic parent of inner membrane), membrane (GO:0016020, generic parent
  of inner membrane).
- The persistent uncertainty (no worm data) is captured in `knowledge_gaps`, not by
  down-grading correct family propagations.

## 7. Deep research status

`just deep-research-falcon worm ppgn-1 --fallback perplexity-lite` was run FOREGROUND and
retried. Falcon timed out at the 600 s server limit on both attempts; the perplexity-lite
fallback returned HTTP 401 (account quota exhausted). No `-deep-research-*.md` file was
produced. Per repo policy I did not fabricate one. This review therefore rests on the
UniProt/InterPro record, the GOA evidence codes, the primary m-AAA/paraplegin literature
cited above (PubMed-verified, cached in `publications/`), and the reproducible sequence
analysis in `ppgn-1-bioinformatics/`.
