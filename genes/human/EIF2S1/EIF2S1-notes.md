# EIF2S1 (eIF2α, UniProt P05198) — curation notes

Reviewed for the [Integrated Stress Response project](../../../projects/INTEGRATED_STRESS_RESPONSE.md)
(issue #3951), which lists EIF2S1 as the central missing hub of the pathway.

`just deep-research` is unavailable in this environment (no provider API keys), so
these notes are assembled from the cached UniProt flat file and the cached
publications rather than from a generated `-deep-research-*.md` file.

## What the protein is

315-aa alpha subunit of the heterotrimeric eukaryotic translation initiation
factor 2 (eIF2 = α/EIF2S1 + β/EIF2S2 + γ/EIF2S3). Domain architecture is an
N-terminal S1/OB nucleic-acid-binding fold (PROSITE PS50126, residues 17–88),
a middle helical domain and a C-terminal αβ domain
[file:human/EIF2S1/EIF2S1-uniprot.txt "DOMAIN 17..88 /note=\"S1 motif\""].
PANTHER family PTHR10602 (subfamily SF0). Protein existence level 1, with 31 PDB
entries including cryo-EM structures of eIF2 bound to eIF2B and to 43S/48S
complexes.

Naming caution worth carrying into the review: the HGNC synonym `EIF2A` is shared
with the unrelated gene *EIF2A*
[file:human/EIF2S1/EIF2S1-uniprot.txt "This gene should not be confused with EIF2A, with which it shares the alias EIF2A."].
Several older GOA rows for this entry are keyed to the `EIF2A` alias era.

## Core biochemistry

eIF2 delivers Met-tRNAi to the 40S subunit as a GTP-dependent ternary complex, is
part of the 43S/48S pre-initiation complex, and is released as eIF2–GDP after
start-codon recognition and GTP hydrolysis
[file:human/EIF2S1/EIF2S1-uniprot.txt "Member of the eIF2 complex that functions in the early steps of protein synthesis by forming a ternary complex with GTP and initiator tRNA"].
Recycling requires eIF2B-catalysed GDP→GTP exchange.

Functional reconstitution: adding purified eIF2 (plus eIF2B) to HeLa extracts
stimulated translation of capped, uncapped and EMCV-IRES reporters
[PMID:16289705 "eIF2 (eukaryotic translation initiation factor 2) and eIF2B augmented translation of capped, uncapped and encephalomyocarditis virus-internal ribosome entry site-promoted mRNAs."].
This single paper is the IDA source for four GOA rows: generic, cap-dependent and
IRES-mediated translation initiation factor activity, plus translational
initiation.

Complex membership is experimentally established in human cells — eIF2γ pulls
down endogenous eIF2α and eIF2β
[PMID:23063529 "The GTP-binding γ-subunit (eIF2γ) forms the core of the heterotrimeric eIF2 complex"],
assembly needs the dedicated chaperone CDC123
[PMID:35031321 "Unlike its archaeal counterpart, eukaryotic IF2 requires the dedicated assembly factor Cdc123 to form the heterotrimeric complex (14)."],
and α-less or β-less dimers are non-functional
[PMID:35031321 "Thus, dimeric eIF2 complexes lacking α or β do not provide eIF2 function in vivo."].

eIF2 associates with 80S ribosomes and polysomes, and that association depends on
ABCF1/ABC50
[PMID:17894550 "Expression of a mutant of ABC50 in which both sites are mutated to alanine markedly decreased the association of eIF2 with 80S ribosomal and polysomal fractions."].

## The ISR: eIF2α Ser52 is the convergence point

All four eIF2α kinases (HRI/EIF2AK1, PKR/EIF2AK2, PERK/EIF2AK3, GCN2/EIF2AK4)
phosphorylate the same serine — numbered Ser52 in the UniProt sequence (which
includes Met1) and Ser51 in the literature
[PMID:38340717 "Responding to different stresses, these kinases all phosphorylate EIF2 on serine 51 of the EIF2α subunit to inhibit global protein synthesis."].
Phosphorylation converts eIF2 from eIF2B substrate to eIF2B inhibitor:

- [file:human/EIF2S1/EIF2S1-uniprot.txt "Activity is regulated by phosphorylation at Ser-49 and Ser-52, which stabilizes the eIF2/GDP/eIF2B complex and prevents the eIF2B-mediated exchange of GDP for GTP, thereby preventing the formation of the 43S pre-initiation complex (43S PIC)"]
- [PMID:31048492 "These structures explain how phosphorylated eIF2 dominantly inhibits the nucleotide exchange activity of eIF2B."]
- [PMID:31048492 "The unphosphorylated and phosphorylated forms of eIF2 bind to eIF2B in completely different manners: the nucleotide exchange-active and -inactive modes, respectively."]

The downstream consequence is selective uORF-mediated translation of ATF4, ATF5,
DDIT3/CHOP and PPP1R15A/GADD34
[file:human/EIF2S1/EIF2S1-uniprot.txt "This results in the global attenuation of 5' cap-dependent protein synthesis and concomitant translation of ISR-specific mRNAs that contain a short upstream open reading frame (uORF) in their 5' UTR, such as ATF4, ATF5, DDIT3/CHOP and PPP1R15A/GADD34"],
with the GADD34 uORF mechanism worked out directly
[PMID:19131336 "and directs translation of GADD34 during eIF2α phosphorylation."].
Dephosphorylation is by PP1 holoenzymes recruited by GADD34 or CReP
[PMID:26095357 "As the stress declines, the GADD34 protein, by recruiting the ser/thr protein phosphatase 1 (PP1), facilitates the dephosphorylation of phospho-eIF2α, restoring normal protein synthesis (Connor et al."].

### Ontology gap found during this review

The GEF-inhibitor step above — the actual mechanism of the ISR — has no molecular
function annotation on human EIF2S1. The term exists
(`GO:1990624` guanyl nucleotide exchange factor inhibitor activity, "Binds to and
stops, prevents or reduces the activity of a guanyl nucleotide exchange factor"),
and the comparator check settles the question in favour of adding it rather than
against: PomBase has already annotated the *S. pombe* ortholog tif211
(UniProtKB:P56286, eIF2α) to `GO:1990624` with TAS from PMID:31048492
(QuickGO, 2026-10-29; 31 annotations on the term, the rest being MON1 and
Ensembl projections of it). The Kashiwagi structures that PomBase cites contain
the *human* eIF2α chain (PDB 6K71, 6K72, chain K = P05198 1-315), so the human
annotation is better grounded than the pombe one it was transferred to. Added as
a `NEW` row.

## Branch-specific ISR roles with human experimental evidence

**HRI branch / mitochondrial stress.** The DELE1–HRI relay converges on eIF2α
[PMID:32132707 "that HRI is the eIF2α kinase that is necessary and sufficient for this relay."],
[PMID:32132706 "eIF2α phosphorylation is mediated by the four eIF2α kinases GCN2, HRI, PERK and PKR, which are activated by diverse types of cellular stress6."].

**Mitophagy.** This is the one place where eIF2α has a location-dependent
function of its own rather than acting as a kinase substrate. Iron chelation
(DFP) drives phospho-eIF2α onto mitochondria, and tethering phosphomimetic
eIF2α to the mitochondrial outer membrane is sufficient to trigger
PINK1/PRKN-independent mitophagy:

- [PMID:38340717 "HRI activation results in accumulation of phosphorylated EIF2 on mitochondria, and we show that this localization is sufficient to trigger mitophagy."]
- [PMID:38340717 "Taken together, these results indicate that phosphorylation and mitochondrial localization of EIF2α are necessary and sufficient to trigger mitophagy."]
- [PMID:38340717 "We observed clear colocalization of p-EIF2α with the mitochondrial OM marker TOM20 in DFP-treated samples as opposed to control or Tg-treated samples (Figure 4C)."]

The ER-marker control that `projects/ORGANELLES.md` asks for was run by the
authors and was negative
[PMID:38340717 "Analysis of the subcellular fractions with an ER marker showed no evidence of ER enrichment of p-EIF2α upon DFP treatment (Figure S4C)."],
so the mitochondrial fraction is not MAM contamination. Even so the review keeps
the root `GO:0005739` mitochondrion rather than adding
`GO:0005741` mitochondrial outer membrane: this is stress-triggered recruitment of
a soluble cytosolic protein to the organelle surface, which the organelle policy
explicitly says is not an outer-membrane location. Note also that peroxisomal
tethering of phospho-eIF2α did *not* trigger pexophagy
[PMID:38340717 "These results suggest that some feature of mitochondria, in addition to pEIF2α targeting, is required for organellar degradation."],
i.e. the mitochondrial localization is specific, not a generic tethering artefact.

**PERK branch / ER stress.** eIF2α is the PERK substrate that routes ER stress to
QRICH1 and ATF4
[PMID:33384352 "We identified QRICH1 as a key effector of the PERK-eIF2α axis of the UPR."],
and the PERK–eIF2α axis also drives respiratory supercomplex assembly
[PMID:31023583 "The PERK-eIF2α-ATF4 axis increases supercomplex assembly factor 1 (SCAF1 or COX7A2L), promoting SCs and enhanced mitochondrial respiration."].
An independent IMP comes from a rotenone neurotoxicity study where eIF2α knockdown
was protective
[PMID:18508033 "An eIF2alpha siRNA significantly reduced rotenone cytotoxicity."],
in a setting the authors characterised as ER stress
[PMID:18508033 "Rotenone also induced endoplasmic reticulum (ER) stress which was evident by an increase in phosphorylation of PERK, PKR, and eIF2alpha as well as the expression of GRP78."].

**Stress granules.** Phospho-eIF2α is the canonical trigger, and eIF2α itself is a
constituent of the stalled 48S complexes that make up the granule
[PMID:18032499 "In uninfected cells, the phosphorylation of eIF2alpha induces the formation of stress granules, aggregates of stalled translation complexes that prevent the translation of mRNAs."],
[PMID:30258011 "Examination of the known SG factors, such as dsRNA adenosine deaminase 1 (ADAR1), Caprin1, cytoplasmic polyadenylation element-binding protein (CPEB), eIF2α, 4E-binding protein 1 (4EBP1), dsRNA-dependent protein kinase (PKR), and Staufen1, at 8 h postinfection (hpi) surprisingly revealed their presence in punctate structures and colocalization with the VM ( Fig."].
Treated as non-core: the granule is a consequence of the translation-attenuation
function rather than a separate activity.

## Annotation-review judgements worth recording

- **25 bare `GO:0005515` rows.** Removed per the protein-binding policy. Two
  groups deserve a note. (i) EIF2S2 (P20042) and EIF2S3 (P41091) partners: the
  informative claim is `GO:0005850` eIF2 complex, which the entry already carries
  with IDA/IPI. (ii) Kinase and phosphatase partners (PKR P19525, PERK Q9Z2B5,
  PPP1CA P62136): here eIF2α is the *substrate*. Removal says nothing about the
  interactions being false.
- **15 Reactome TAS `GO:0005829` cytosol rows.** All kept — cytosol is where
  initiation happens and it is also supported by HPA IDA (GO_REF:0000052).
- **Rat-projected rows** (GO_REF:0000107 from UniProtKB:P68101): `GO:0097451`
  glial limiting end-foot and `GO:2000676` positive regulation of type B
  pancreatic cell apoptotic process are flagged as over-annotated. Both are
  single-ortholog Ensembl Compara projections of highly specific claims; the
  pancreatic-apoptosis one in particular describes a PERK→CHOP outcome rather
  than something eIF2α does. `GO:0034605` cellular response to heat,
  `GO:1904373` response to kainic acid and `GO:1990737` response to
  manganese-induced ER stress are kept non-core: eIF2α genuinely does get
  phosphorylated in these settings, but they are contexts, not functions.
- **`GO:0005634` nucleus** (projected from mouse) is flagged as over-annotated.
  There is one incidental human immunofluorescence observation of nuclear signal
  [PMID:30258011 "The eIF2α protein appeared to be present in both the nucleus and the cytoplasm and showed cytoplasmic accumulation and localization in the VM in infected cells, which appeared to be specific based on the location at identical sites of the punctate structures of the endogenous protein and the VM ( Fig."],
  but no nuclear function is known, so the row is not removed outright.
- **`GO:0016020` membrane (HDA)** and **`GO:0070062` extracellular exosome (HDA)**
  are flagged as over-annotated: both are whole-fraction proteomics hits for an
  abundant cytosolic protein, and the membrane paper says as much about its own
  non-integral hits
  [PMID:19946888 "The remaining species were largely involved in cellular processes and molecular functions that could be predicted to be transiently associated with membranes."].
- **`GO:0045202` synapse (`is_active_in`, projected)** is kept non-core.
  eIF2α-dependent translational control in neurons is real, but the row is a
  projection and names a cellular context rather than a distinct activity.
- `GO:0003676` nucleic acid binding, `GO:0005737` cytoplasm and `GO:0006446`
  regulation of translational initiation are marked `TOO_GENERAL`: each is a
  strict ancestor of a more specific term accepted elsewhere in this review
  (`GO:0003723`, `GO:0005829`, `GO:0032057` respectively).

## Open questions

- Does unphosphorylated eIF2α have any function on mitochondria, or is the
  mitochondrial pool entirely the phospho-form? PMID:38340717 reports total eIF2α
  in the mitochondrial fraction is unchanged by DFP, so the recruited species is
  specifically phospho-eIF2α.
- The `GO:0160297` IRES-mediated translation initiation factor activity row rests
  on one EMCV-IRES reporter in HeLa extract. Whether eIF2 dependence generalises
  across IRES types (type 1/2 vs HCV-like, which can bypass eIF2) is not settled
  by that experiment.
- Ser49 phosphorylation is annotated only by similarity to *Drosophila*
  (UniProtKB:P83268); no human assay distinguishes Ser49 from Ser52 contributions.
