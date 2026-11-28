# FUS (P35637) — curation notes

Curated for the [Stress Granule Assembly Project](../../../projects/STRESS_GRANULES.md)
(issue 3953), which lists FUS as one of its 16 candidate genes. No provider
deep-research file was generated: the repo's `just deep-research` providers were
unavailable in this environment (`Provider 'perplexity' not available. Available:
claude_code`), so this file is the gene's research record. Everything below is cited to a
primary paper, the UniProt record, or a resolved database record.

## What FUS is

526-residue DNA/RNA-binding protein of the FET family (FUS/TLS, EWSR1, TAF15). Domain
layout from the UniProt record (P35637): an N-terminal QGSY-rich/low-complexity region
that MobiDB-lite calls disordered over residues 1–286, a single RRM (285–371), an
RGG-rich stretch, a RanBP2-type zinc finger (422–453), and a C-terminal PY-NLS inside the
disordered 444–526 segment. Classified in PANTHER PTHR23238 ("RNA BINDING PROTEIN"), with
InterPro signatures IPR000504 (RRM_dom), IPR034870 (TET_fam) and IPR001876 (Znf_RanBP2).

UniProt's own summary of its roles
[file:human/FUS/FUS-uniprot.txt "DNA/RNA-binding protein that plays a role in various cellular processes such as transcription regulation, RNA splicing, RNA transport, DNA repair and damage response"].

## Core activities, with evidence

**RNA binding.** The primary molecular function, carried by the RRM, RGG and RanBP2
zinc-finger regions. UniProt records a consensus
[file:human/FUS/FUS-uniprot.txt "Binds to ssRNA containing the consensus sequence 5'-AGGUAA-3'"].
Measured directly in vitro on unstructured single-stranded U40
[PMID:38070499 "in the absence of RNA, neither LCD nor RBD form droplets up to 15"] — the
same paper's EMSA and single-molecule work shows
[PMID:38070499 "while both LCD and RBD bind RNA, RBD drives RNA engagement and multivalent complex formation"].
CLIP-seq in mouse brain and human neural progenitors maps thousands of targets
[PMID:27378374 "TAF15 and FUS exhibit similar binding patterns in introns, are enriched in 3' untranslated regions and alter genes distinct from TDP-43"].

**Molecular condensate scaffold activity.** FUS is the archetypal phase-separating RBP
[PMID:38070499 "Fused in sarcoma (FUS) is an archetypal phase separating protein asymmetrically divided into a low complexity domain (LCD) and an RNA binding domain (RBD)"].
Reconstituted in vitro and in cells
[PMID:26317470 "We show that, in cells, FUS forms liquid compartments at sites of DNA damage and in the cytoplasm upon stress. We confirm this by reconstituting liquid FUS compartments in vitro."],
and the phase-separated state is a dynamic, disordered liquid rather than a static
structure
[PMID:26455390 "we find that FUS LC retains disordered secondary structure even in the liquid phase-separated state"].
The same assemblies bind the RNA Pol II CTD
[PMID:26455390 "This state directly binds the C-terminal domain of RNA polymerase II."],
which ties the condensate behaviour to the transcription role below. Phase separation is
switched off by transportin-1 binding the PY-NLS
[PMID:29677513 "We show that the importin karyopherin-β2/transportin-1 inhibits LLPS of FUS. This activity depends on tight binding of karyopherin-β2 to the C-terminal proline-tyrosine nuclear localization signal (PY-NLS) of FUS."]
and by phosphorylation of the fibril core
[PMID:28942918 "Phosphorylation of core-forming residues by DNA-dependent protein kinase blocks binding of soluble FUS-LC to FUS-LC hydrogels and dissolves phase-separated, liquid-like FUS-LC droplets."].

**Self-assembly / homo-oligomerisation.** UniProt:
[file:human/FUS/FUS-uniprot.txt "Self-oligomerizes (via N-terminal region) (PubMed:25453086). Oligomerization is essential for chromatin binding (PubMed:25453086)."]
The N-terminal region responsible is mapped
[PMID:25453086 "The N-terminal QGSY (glutamine-glycine-serine-tyrosine)-rich region (amino acids 1-164) mediates FUS self-assembly in the nucleus of mammalian cells and the self-assembly is essential for its chromatin binding and transcription activation."].

**Chromatin binding and transcription coupling.** Self-assembled FUS occupies active
chromatin
[PMID:25453086 "we found that a significant portion of nuclear FUS was bound to active chromatin and that the ALS mutations dramatically decreased FUS chromatin binding ability"],
and chromatin binding is separable from splicing regulation
[PMID:25453086 "Functionally, the chromatin binding is required for FUS transcription activation, but not for alternative splicing regulation."].
SAFB1 is the tether
[PMID:27731383 "depletion of SAFB1 reduced FUS's localization to chromatin-bound fraction and splicing activity, suggesting SAFB1 could tether FUS to chromatin compartment thorough N-terminal DNA-binding motif"].
FUS also bridges the polymerase to U1 snRNP
[PMID:26124092 "our data lead to a model that FUS functions in coupling transcription to splicing via mediating an interaction between RNAP II and U1 snRNP"],
and is required for splicing in the coupled reaction
[PMID:26124092 "we found that FUS must be present during the transcription reaction in order for splicing to occur"].
As a coactivator it works on the androgen receptor
[PMID:21909421 "Data from ectopic overexpression and \"knock-down\" approaches demonstrated that AR transcriptional activity was enhanced by FUS."],
recruited to a specific enhancer
[PMID:21909421 "Chromatin immunoprecipitation experiments showed that FUS was recruited to ARE III of the enhancer region of the PSA gene."].
FUS is also reported on the repressive side of ligand-dependent transcription
[PMID:27731383 "They coordinately regulated the alternative splicing and repressed AR -mediated transcription in vitro."],
which is why the family-level `transcription coregulator activity` (GO:0003712) term is
not redundant with `transcription coactivator activity`.

**Alternative-splicing regulation, including autoregulation.** Both GOA rows for
`regulation of RNA splicing` rest on alternative-splicing assays: an E1A minigene
[PMID:27731383 "To investigate the interplay between FUS and SAFB1 in the alternative splicing, we performed splicing assays using E1A mini-gene construct in HEK293."]
and the FUS-dependent alternative splicing tested in
[PMID:25453086 "Functionally, the chromatin binding is required for FUS transcription activation, but not for alternative splicing regulation."].
The best-characterised single event is FUS's own exon 7
[PMID:24204307 "We demonstrated that FUS is a repressor of exon 7 splicing and that the exon 7-skipped splice variant is subject to nonsense-mediated decay (NMD)."].

**Pri-miRNA processing.** Not currently annotated for FUS beyond a bare protein-binding
row with DROSHA. The mechanism is co-transcriptional recruitment of the microprocessor
[PMID:23232809 "We also show that FUS/TLS is recruited to chromatin at sites of their transcription and binds the corresponding pri-microRNAs. Moreover, FUS/TLS depletion leads to decreased Drosha level at the same chromatin loci."]
with a functional readout
[PMID:23232809 "Limited FUS/TLS depletion leads to a reduced microRNA biogenesis"].
Comparator check (QuickGO, `goId=GO:0031053&taxonId=9606`, exact usage, 59 annotations):
the same-role cofactors that promote Drosha-mediated processing without being the nuclease
carry `GO:0031053 primary miRNA processing` `involved_in` — DDX5 (IMP), SRRT (IMP),
SRSF3 (IMP), HNRNPA2B1 (IDA), METTL3 (IDA) — alongside DROSHA and DGCR8 themselves. The
regulation term `GO:2000636` has only two human annotations (BMP4, TGFB1, both IDA), so
`GO:0031053` is the convention here, not the regulation branch.

**DNA binding and homologous pairing.** GOA has the downstream process row but no DNA
binding molecular function at all. The biochemistry is explicit
[PMID:10567410 "hPOMp75/TLS binds both single- and double-stranded DNAs and mediates annealing of complementary DNA strands. More important, it promotes the uptake of a single-stranded oligonucleotide into a homologous superhelical DNA to form a D-loop."],
and is ATP-independent
[PMID:10567410 "DNA annealing and D-loop formation catalyzed by hPOMp75/TLS require Mg(2+) and are ATP-independent."].
The oncogenic fusion loses it
[PMID:10567410 "Interestingly, the oncogenic fusion form TLS-CHOP is not able to promote DNA pairing."].
UniProt reads the same paper as a repair role
[file:human/FUS/FUS-uniprot.txt "Plays a role in DNA repair mechanisms by promoting D-loop formation and homologous recombination during DNA double-strand break repair (PubMed:10567410)."].

## Localisation

Nucleus, in a punctate pattern
[file:human/FUS/FUS-uniprot.txt "Note=Displays a punctate pattern inside the nucleus and is excluded from nucleoli."].
The 24 `nucleoplasm` TAS rows all come from Reactome spliceosome and
cleavage/polyadenylation events; FUS really is a listed participant — the participant
query for `R-HSA-72103` ("Formation of pre-mRNPs") and `R-HSA-9970141` ("Core CPA complex
binds capped pre-mRNA") both return `UniProt:P35637 FUS`. The four SynGO-derived synaptic
rows (glutamatergic synapse, GABA-ergic synapse, pre- and postsynaptic cytosol) are
Ensembl Compara projections from mouse Fus (P56959); UniProt carries the matching
neuronal role only by similarity
[file:human/FUS/FUS-uniprot.txt "In neuronal cells, plays crucial roles in dendritic spine formation and stability, RNA transport, mRNA stability and synaptic homeostasis (By similarity)."].

## The stress-granule question — and why this review does not annotate it

This is the project-relevant finding, and it goes the opposite way from the project page's
framing of FUS as a stress-granule RBP.

GOA carries **no** stress-granule annotation for FUS, and the literature says that is
correct for the wild-type protein:

- Endogenous FUS is not required for stress-granule formation
  [PMID:23092511 "We also demonstrate that endogenous TDP-43 and FUS do not have overlapping functions in this cellular process as SG initiation and assembly occur normally in the absence of FUS."].
- Recruitment of FUS into stress granules requires cytoplasmic mislocalisation, i.e. an
  ALS mutation or an engineered NLS defect
  [PMID:22563080 "We determined the requirements for SG recruitment of FUS and TDP-43 and found that cytoplasmic mislocalization is a common prerequisite for SG recruitment of FUS and TDP-43."],
  and the responsible region is the RGG zinc-finger RNA-binding domain
  [PMID:22563080 "For FUS, the arginine-glycine-glycine zinc finger domain, which is the protein's main RNA binding domain, is most important for SG recruitment, whereas the glycine-rich domain and RNA recognition motif (RRM) domain have a minor contribution and the glutamine-rich domain is dispensable."].
- Stated as a mutant-specific phenotype
  [PMID:24090136 "Since only the mutants, but not the endogenous wild-type FUS, are associated with stress granules under most of the stress conditions reported to date, the relationship between FUS and stress granules represents a mutant-specific phenotype and thus may be of significance in mutant-induced pathogenesis."],
  with the mutant's effect being to perturb granule dynamics rather than to build granules
  [PMID:24090136 "We found that expression of mutant-FUS delays the assembly of stress granules."].

The comparator check runs the other way and still supports the decision. Same-role
comparators *do* carry the location term — TIA1 `GO:0010494` IDA (PMID:8576255,
PMID:21984414), ATXN2 `GO:0010494` IDA (PMID:17392519), TARDBP `GO:0010494` IEA — so the
absence on FUS is not a term-level convention that would hide a real gap. It is a
gene-level judgement, and it matches the papers. So: no `NEW` row for
`GO:0010494 cytoplasmic stress granule`, no `NEW` row for
`GO:0034063 cytoplasmic stress granule assembly`, and the open biological question
(whether endogenous wild-type FUS ever enters granules under a stress that has not been
tested) is recorded as a knowledge gap with a matching suggested experiment instead.

Patel et al.'s abstract does state that FUS forms liquid compartments "in the cytoplasm
upon stress" [PMID:26317470], but it does not call them stress granules, the entry is
abstract-only in our cache, and much of that paper's cell work uses tagged/mutant
constructs. That is not enough to overturn the three papers above.

## Things this review changes in GOA

1. `GO:0048255 mRNA stabilization` (IDA, PMID:27378374, MGI) is the wrong direction. The
   paper's own count is
   [PMID:27378374 "We identified 299 and 330 genes that were highly stabilized (increased half-life), as well as 132 and 44 genes that were highly destabilized (decreased half-life) upon loss of TAF15 and FUS, respectively"]
   — losing FUS *stabilised* 330 transcripts and destabilised only 44, so FUS predominantly
   destabilises its targets, and the validated subset moved not at all
   [PMID:27378374 "FUS depletion did not appear to have an effect on mRNA stability of these transcripts"].
   Recorded as `MODIFY` to `GO:0043488 regulation of mRNA stability` plus a `WRONG_TERM`
   source defect against MGI.
2. `GO:1990000 amyloid fibril formation` (two rows) is marked over-annotated. Both cited
   papers explicitly separate what they measured from pathogenic amyloid
   [PMID:28942918 "Unlike pathogenic amyloid fibrils, FUS-LC fibrils lack hydrophobic interactions within the core and are not polymorphic at the molecular structural level."]
   and
   [PMID:22579281 "Unlike pathogenic fibers, the LC sequence-based polymers described here are dynamic and accommodate heterotypic polymerization."],
   and the GO definition is about "insoluble fibrous protein aggregates". The biologically
   meaningful content is already carried by `GO:0140693` and `GO:0140694`.
3. Two `NEW` molecular-function rows for DNA binding (`GO:0003697` single-stranded,
   `GO:0003690` double-stranded), both from PMID:10567410 — GOA has the HR-repair process
   row from that paper but no DNA-binding function from it.
4. One `NEW` process row, `GO:0031053 primary miRNA processing` (IMP, PMID:23232809), per
   the comparator check above.
5. Both `regulation of RNA splicing` rows `MODIFY` to
   `GO:0000381 regulation of alternative mRNA splicing, via spliceosome`, which is what
   each row's own assay measured.
6. The 56 bare `GO:0005515 protein binding` rows are removed per the repository's
   protein-binding policy. Removal does not dispute any interaction; the informative
   content of two of them is recovered as the new pri-miRNA-processing row (DROSHA) and in
   the chromatin-binding reasons (SAFB1).

## Disease context (not annotated as function)

ALS6 with or without FTD, caused by variants clustered in the PY-NLS
[file:human/FUS/FUS-uniprot.txt "The disease is caused by variants affecting the gene represented in this entry."];
also hereditary essential tremor 4, and recurrent translocations producing FUS-DDIT3
(myxoid liposarcoma), FUS-ERG (AML) and FUS-ATF1 (angiomatoid fibrous histiocytoma). The
original cloning of FUS was as the FUS-DDIT3 fusion partner
[PMID:8510758 "Fusion of CHOP to a novel RNA-binding protein in human myxoid liposarcoma."].
Disease mechanisms (cytoplasmic mislocalisation, inclusion formation, gain-of-toxicity in
granule dynamics) are deliberately kept out of the annotation set.
