# Manual deep research: human ELAVL2

Date: 2026-07-18

## Scope and provenance

Falcon deep research was attempted and returned HTTP 402. Its configured
Perplexity-lite fallback returned HTTP 401 because quota was unavailable. No
provider-named output was retained. This manual synthesis uses the reviewed
UniProtKB Q12926 record, the current GOA file, the local Reactome event, cached
primary publications, and targeted PubMed/PMC searches.

## Protein identity and architecture

ELAVL2 (HuB/Hel-N1) is a 359-residue neural ELAV-family RNA-binding protein.
The reviewed UniProt record assigns three RNA-recognition motifs (RRMs), at
residues 39-117, 125-205, and 276-354, and records two splice isoforms. Isoform
2 lacks residues 239-251 in the hinge between RRM2 and RRM3. The record describes
brain-enriched, neural-specific expression and states that the protein binds
target-mRNA 3'-UTRs, while noting that its GAAA-motif preference and several
targets are transferred from mouse [file:human/ELAVL2/ELAVL2-uniprot.txt
"RNA-binding protein that binds to the 3' untranslated region"].

## Direct RNA-binding specificity

The original human Hel-N1 study cloned the protein and directly tested binding
to the Id transcript. The abstract states that Hel-N1 [PMID:8158249 "can bind to
the 3' untranslated region (3' UTR) of Id mRNA, a transcript that"]. This is
direct support for mRNA 3'-UTR binding, but the paper does not demonstrate direct
control of DNA-templated transcription; Id is merely the protein encoded by the
bound mRNA.

A second human study selected RNA targets for Hel-N1 and Hel-N2 from randomized
and naturally derived 3'-UTR libraries. It found that [PMID:7972035
"combinatorial libraries yielded (A+U)-rich consensus sequences for both Hel-N1"]
and selected a subset of natural 3'-UTRs bound by Hel-N1. This directly supports
the more specific mRNA 3'-UTR AU-rich-region-binding activity.

An independent ELAV-family analysis explicitly includes Hel-N1 among the four
human family members and summarizes that [PMID:10710437 "include HuC, HuD,
Hel-N1 and HuR. These proteins bind to AU-rich elements in the"]. Its full text
further reports that Hel-N1 recognizes U-rich motifs including AUUUG, GUUUUU,
and AUUUA. This corroborates the direct Hel-N1 selection experiments without
claiming that the HuC/HuD measurements in that paper were ELAVL2 assays.

Two orthogonal mRNA-interactome capture studies independently assigned ELAVL2 as
an RNA-binding protein in human HeLa and HEK293 cells (GOA HDA annotations from
PMID:22658674 and PMID:22681889). Their abstracts describe UV-crosslinking plus
poly(A)-RNA purification and the resulting biochemical mRNA-bound proteomes.
They corroborate direct RNA association but do not establish ELAVL2 sequence or
target specificity.

## Alternative splicing and 3'-UTR length control

Reduction of ELAVL2 in primary human neurons followed by RNA-seq identified
ELAVL2-dependent expression and splicing networks. The cached abstract reports
[PMID:27260404 "spliced genes resulting from haploinsufficient levels of ELAVL2."]
The perturbation supports regulation of alternative mRNA splicing in human
neurons. The network enrichment for neurodevelopmental, synaptic, and
autism-associated genes is useful context, but it should not be converted into
direct annotations for every downstream neuronal process.

A later primary study gives direct human-neuron evidence for alternative
polyadenylation/3'-UTR-length control. Combined HuB/HuC/HuD expression globally
lengthened 3'-UTRs in HEK293T cells, while acute neuronal HuB depletion had the
strongest individual effect. The abstract states [PMID:37862432 "Depleting
ELAVL2 in WT neurons led to global shortening of 3'UTR"]. The full text reports
that HuB loss greatly decreased 3'-UTR length, whereas HuC loss had a smaller
trend and HuD loss had no detectable effect in that assay. This supports mRNA
alternative polyadenylation as a core ELAVL2-controlled process.

The same study links ELAVL2-dependent long 3'-UTRs to endogenous dsRNA, tonic
type-I-interferon signaling, and antiviral resistance. These are experimentally
supported downstream phenotypes, but the mechanistic core remains ELAVL2's
control of neuronal RNA processing. Broad immune-process annotations would risk
turning an RNA-processing mechanism into downstream over-annotation.

## RNP and protein interactions

InterPro transfers ribonucleoprotein-complex membership from the ELAV/Hu family.
This is consistent with ELAVL2 binding RNA and with the reviewed UniProt record's
experimentally supported interaction with IGF2BP1. PMID:17289661 describes the
composition of IMP1/IGF2BP1 RNP granules, but its locally available abstract does
not name ELAVL2. The GOA row and UniProt record identify IGF2BP1 as the partner;
the generic GO molecular-function term protein binding adds little information.

PMID:36950384 is a neuronal interaction-proteomics study. GOA/IntAct maps the
ELAVL2 interaction row to DYRK1A, and UniProt records three IntAct experiments.
The paper establishes a quality-controlled neuronal PPI network, but its main
text does not explain the functional consequence of the ELAVL2-DYRK1A pair.
Generic protein binding is therefore over-annotated rather than a core molecular
function.

The Reactome event R-HSA-9921507 describes nuclear dengue-virus NS5 binding to
spliceosome components CD2BP2 and DDX23. Its local summary does not name ELAVL2
or expose the evidence for assigning ELAVL2 to the nucleoplasm. Nucleoplasmic
localization is biologically plausible for an alternative-splicing regulator,
but this specific pathway-derived record is retained only as non-core.

## Synthesis and curation boundaries

The strongest ELAVL2-specific molecular evidence supports AU-/U-rich mRNA
3'-UTR binding. Human perturbation experiments additionally establish regulation
of alternative splicing and distal poly(A)-site use/3'-UTR length. Phylogenetic
IBA evidence supports a protein-RNA adaptor activity, and the RNP-complex IEA is
consistent with the biochemical role.

The following claims are deliberately excluded from the core:

- direct regulation of DNA-templated transcription;
- a specific biochemical consequence of DYRK1A or IGF2BP1 binding;
- direct control of every neurodevelopmental, synaptic, immune, or antiviral
  pathway enriched downstream of ELAVL2 perturbation;
- isoform-specific functions, because neither human isoform has been compared in
  the decisive RNA-processing assays;
- direct mRNA stabilization as an ELAVL2-specific in-vivo activity, because the
  strongest local evidence for stability is family-level or transferred from
  mouse.

## Curation-ready conclusions

1. Accept mRNA 3'-UTR AU-rich-region binding, mRNA 3'-UTR binding, RNA binding,
   protein-RNA adaptor activity, and ribonucleoprotein-complex membership.
2. Modify broad nucleic-acid binding to the experimentally supported AU-rich
   mRNA 3'-UTR-binding term.
3. Mark both generic protein-binding annotations as over-annotated while
   preserving the underlying interaction evidence.
4. Keep the Reactome nucleoplasm location as non-core because the local event
   does not expose ELAVL2-specific evidence.
5. Modify regulation of DNA-templated transcription to post-transcriptional
   regulation of gene expression.
6. Add regulation of alternative mRNA splicing, via spliceosome, and mRNA
   alternative polyadenylation from direct human perturbation studies.
