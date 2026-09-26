# ACADM (MCAD) review notes

UniProt: P11310 | HGNC:89 | EC 1.3.8.7 | Medium-chain specific acyl-CoA dehydrogenase, mitochondrial.

## Core biology

MCAD catalyzes the first (rate-committed) step of each cycle of mitochondrial fatty acid
beta-oxidation for medium-chain acyl-CoA esters: the FAD-dependent alpha,beta-dehydrogenation
of a saturated acyl-CoA to the corresponding trans-2-enoyl-CoA, with electrons passed to the
electron-transfer flavoprotein (ETF).

- "Medium-chain specific acyl-CoA dehydrogenase is one of the acyl-CoA dehydrogenases that
  catalyze the first step of mitochondrial fatty acid beta-oxidation (FAO), breaking down fatty
  acids into acetyl-CoA and allowing the production of energy from fats" [UniProt P11310 FUNCTION].
- "The first step of FAO consists in the proR-proR stereospecific alpha, beta-dehydrogenation of
  fatty acyl-CoA thioesters using the electron transfer flavoprotein (ETF) as their physiologic
  electron acceptor, resulting in the formation of trans-2-enoyl-CoA ((2E)-enoyl-CoA)" [UniProt P11310].
- Substrate preference C6-C12 (optimum hexanoyl/octanoyl-CoA), can extend to C14/C16:
  KM values 175 uM butyryl-CoA, 15 uM hexanoyl-CoA, 3.4 uM octanoyl-CoA [UniProt P11310 BIOPHYSICOCHEMICAL PROPERTIES, PMID:8823175].
- [PMID:19224950 "MCAD is a member of the acyl-CoA dehydrogenase (ACAD) family of flavoproteins, which catalyzes the first step of the mitochondrial β-oxidation of medium-chain fatty acids"].

## Catalysis, active site, FAD

- Catalytic base is Glu (Glu376 in mature numbering = Glu401 in precursor used by UniProt FT ACT_SITE 401).
  [PMID:1970566 "Glutamic acid 376, which has been proposed by Powell and Thorpe ... as an essential
  residue and the proton-abstracting base at the active site of the enzyme, was mutated to glutamine"];
  the Gln376 mutant "is devoid of activity (less than 0.02% that of wild type)".
- The position of the catalytic Glu determines chain-length specificity: MCAD has Glu376 on loop JK;
  LCAD/IVD have Glu255 on helix G. [PMID:8823175 "The catalytically essential glutamate residue that
  initiates catalysis by abstracting the substrate alpha-hydrogen as H+ is located at position 376
  (mature MCADH numbering) on loop JK in medium chain acyl-CoA dehydrogenase (MCADH)"].
- FAD is the bound cofactor; the WT enzyme "is a yellow protein due to the content of stoichiometric FAD"
  [PMID:1970566]. UniProt COFACTOR: FAD. Each subunit contains 1 mol FAD [PMID:3597357].

## Oligomeric state and location

- Soluble homotetramer. [PMID:3597357 "indicating a homotetrameric structure"] (native MW ~178,000;
  subunit ~44,000). UniProt SUBUNIT: "Homotetramer". Maier et al. confirm recombinant human MCAD elutes
  as a tetramer: [PMID:19224950 "Wild-type MCAD was eluted in the tetrameric form with an almost
  negligible amount of aggregates"].
- Mitochondrial matrix. [UniProt P11310 SUBCELLULAR LOCATION "Mitochondrion matrix" ECO:...PubMed:16020546].
  N.B. PMID:16020546 is the ACAD9 paper; it reports MCAD localization context only indirectly. UniProt
  cites PubMed:16020546 for the matrix location of MCAD. Mature protein after cleavage of a 25-aa transit peptide.
- GOA also has a "mitochondrial membrane" IDA (PMID:16020546) and a sperm-nucleus HDA (PMID:21630459) and
  an "axon" IDA (PMID:21237683). The axon call reflects neuronal expression: [PMID:21237683 "MCAD in the
  molecular layer and axons of specific neurons"]. The nucleus HDA is from a sperm-nucleus proteome whose
  isolation explicitly removed mitochondria; for a matrix FAO enzyme this is best treated as contaminant /
  non-core. [PMID:21630459 "sperm nuclei were obtained through CTAB treatment and isolated to over 99.9%
  purity without any tail fragments, acrosome or mitochondria"].

## ETF as physiological electron acceptor

- MCAD donates electrons to ETF; structure of the human ETF.MCAD complex solved.
  [UniProt P11310 "ETF is the electron acceptor that transfers electrons to the main mitochondrial
  respiratory chain via ETF-ubiquinone oxidoreductase" ECO:...PubMed:15159392, PubMed:25416781].
- METTL20/ETFbeta-KMT methylation of ETFbeta reduces electron transfer FROM MCAD; this is a regulatory
  observation about ETFbeta, used by GOA to support MCAD's FAO process annotation.
  [PMID:25416781 "METTL20-mediated methylation of ETFβ in vitro reduced its ability to receive electrons
  from the medium chain acyl-CoA dehydrogenase and the glutaryl-CoA dehydrogenase"].

## Disease (MCAD deficiency, ACADMD; MIM 201450)

- Most common inherited FAO disorder; common mutation c.985A>G (K304E precursor numbering; K329E by mature
  pre-cleavage convention used in older papers). [PMID:2393404 "A single A to G nucleotide replacement which
  resulted in lysine329-to-glutamic acid329 substitution of the MCAD protein was identified in all cultures
  ... this point mutation was present in 91% (31 of 34) of mutant MCAD alleles"].
- Mechanism is protein misfolding / impaired tetramer assembly with loss of function.
  [PMID:1902818 "mutant MCAD, which was demonstrated to be inactive, probably because of the inability to
  form active tetrameric MCAD"]; [PMID:19224950 "results substantiate the hypothesis of protein misfolding
  with loss-of-function being the common molecular basis in MCADD"].

## Physiology: carnitine, exercise

- MCADD patients accumulate octanoylcarnitine; they can upregulate carnitine biosynthesis during exercise.
  [PMID:16972171 "Our results suggest that MCADD patients are able to increase carnitine biosynthesis during
  exercise to compensate for carnitine losses"]. This is an indirect, secondary metabolic consequence of
  MCAD deficiency (acylcarnitine handling), NOT evidence that MCAD itself carries out carnitine biosynthesis;
  the IMP carnitine-process annotations (GO:0045329 carnitine biosynthetic process, GO:0019254 carnitine
  metabolic process CoA-linked) are downstream/indirect and should be demoted from core.

## Annotation strategy summary

- Core MF: GO:0070991 medium-chain fatty acyl-CoA dehydrogenase activity (strong EXP/IDA support).
- Core BP: GO:0006635 fatty acid beta-oxidation / GO:0033539 FAO using acyl-CoA dehydrogenase;
  GO:0051793 medium-chain fatty acid catabolic process; GO:0051791 medium-chain fatty acid metabolic process.
- Core CC: GO:0005759 mitochondrial matrix.
- Cofactor: GO:0050660 FAD binding (correct; supported by FAD content).
- General parents kept non-core/accept: GO:0003995 acyl-CoA dehydrogenase activity,
  GO:0016627 oxidoreductase activity acting on CH-CH.
- MODIFY/over-annotation candidates:
  - GO:0004466 long-chain fatty acyl-CoA dehydrogenase activity (IEA, RHEA C14/C16): MCAD's primary
    specificity is medium-chain; C14/C16 are weak secondary substrates. MARK_AS_OVER_ANNOTATED (the
    Rhea-derived "long-chain" specific MF overstates specificity; better term is the medium-chain one).
  - GO:0016937 short-chain fatty acyl-CoA dehydrogenase activity (IEA, RHEA pentanoyl/C5): butyryl-CoA
    KM is very high (175 uM, poor substrate); this is a separate enzyme's specialty (SCAD). MARK_AS_OVER_ANNOTATED.
  - GO:0005978 glycogen biosynthetic process (IEA Ensembl ortholog): no mechanistic link; REMOVE.
  - GO:0006111 regulation of gluconeogenesis (IEA Ensembl ortholog): indirect at best; MARK_AS_OVER_ANNOTATED.
  - GO:0019254 / GO:0045329 carnitine processes (IMP PMID:16972171): indirect patient physiology;
    KEEP_AS_NON_CORE (do not REMOVE experimental IMP).
  - GO:0005634 nucleus (HDA sperm nucleus): non-core/contaminant; MARK_AS_OVER_ANNOTATED.
  - GO:0030424 axon (IDA): neuronal expression of a mito enzyme; KEEP_AS_NON_CORE.
  - GO:0031966 mitochondrial membrane (IDA PMID:16020546): MCAD is a soluble matrix protein; keep as
    non-core/over-annotated (matrix is the precise term).
  - GO:0042802 identical protein binding (IDA): captures homotetramer; do not endorse as core MF
    (uninformative). MARK_AS_OVER_ANNOTATED but note it reflects real tetramerization.
- GO:0005737 cytoplasm (IBA) and GO:0005739 mitochondrion (various): correct but general; matrix is precise.


## 2026-09-26 substantive re-review

This section supersedes conflicting interpretations in the earlier notes, while preserving
that earlier record. All 50 original GOA assertions, including their terms, qualifiers,
evidence codes and original references, remain unchanged. The final revised actions are 38 ACCEPT,
6 KEEP_AS_NON_CORE, 4 UNDECIDED, 1 MARK_AS_OVER_ANNOTATED and 1 MODIFY. No new annotation is proposed.

### Identity, baseline and research access

ACADM is the HGNC-approved human symbol (HGNC:89; UniProt P11310; aliases MCAD,
MCADH and ACAD1), checked against the [HGNC-provided NCBI gene record](https://www.ncbi.nlm.nih.gov/gene/000034).
The baseline review matches main commit `21121fc735d20bcb2dbf8328aa82d5da30185e5e`,
Git blob `9e3c0f399451c3b041c58b61aa6f66ee064c28e4`. An open-PR search found no overlapping
ACADM PR before editing. This was a substantive re-review of an existing COMPLETE file,
not a new seeded review.

A genuine default Falcon attempt with the prescribed perplexity-lite fallback ran alongside
publication caching. Both provider commands failed before reaching a research provider:
`uvx` could not fetch `deep-research-client[cyberian]==0.2.7rc1` from PyPI because DNS lookup
failed, returning code 2 for each provider and wrapper code 1. The attempt used writable
process-local UV tool/cache directories. No provider report was produced, and no manual
text was labeled as provider output. All 13 cited publications were already cached;
`fetch-gene-pmids` completed 13/13 without replacing source files. This manual source review
uses those caches plus the primary-source reads identified below. No machine source was edited.

### Catalysis and substrate-range corrections

The single core function is FAD-dependent, ETF-coupled acyl-CoA dehydrogenation in the
mitochondrial matrix. FAD binding remains a valid annotation but is a component of that
catalytic mechanism, not an independent core function. Human liver enzyme purification
identifies the octanoyl-CoA product, ETF use, one FAD per subunit and homotetrameric structure
[PMID:3597357]. Recombinant human enzyme mutagenesis establishes the catalytic glutamate
and FAD content [PMID:1970566]. The reaction is the first step of a beta-oxidation cycle;
the earlier description as a rate-committed step was not justified by these sources.

The C14/C16 long-chain reactions in the unchanged human UniProt record have explicit
Rhea assignments, RHEA:47316/RHEA:43448, and human-literature provenance. Their existence is
compatible with a C6/C8 activity optimum [PMID:8823175; PMID:21237683]. These activities are
retained as non-core rather than rejected from the protein's name. The earlier high-Km
argument was incorrect: the curated record lists C8 3.4, C14 2.3 and C16 1.6 micromolar;
Km alone does not establish turnover or catalytic efficiency. The original full kinetic
panel was not independently re-extracted.

The RHEA:43456 pentanoyl-CoA reaction is assigned in human UniProt by similarity to rat
Acadm P08503, whose identity was checked in UniProt. GO:0016937 covers substrates with
fewer than six carbons and is not exclusive to the protein named SCAD. Retain this
secondary activity with its orthology limitation; neither butyryl-CoA kinetics nor an
activity optimum directly measures human C5 turnover. The underlying rat C5 assay remains
unrecovered. Broad acyl-CoA dehydrogenase/oxidoreductase terms describe the core chemistry
and are accepted rather than demoted solely for their breadth.

### Localization: positive evidence and remaining uncertainty

The earlier statement that PMID:16020546 contains only indirect MCAD context is withdrawn.
The [author-uploaded full primary article](https://www.researchgate.net/publication/7723299_Human_Acyl-CoA_Dehydrogenase-9_Plays_a_Novel_Role_in_the_Mitochondrial_-Oxidation_of_Unsaturated_Fatty_Acids)
was inspected at Figure 5 and the submitochondrial localization results. It directly tests
MCAD in fractionated human muscle mitochondria and detects it in both matrix and membrane
fractions. The authors interpret the membrane signal as loose association or nonspecific
adherence typical of matrix ACADs. Matrix is accepted as core and membrane association is
retained as non-core, without claiming an integral or stable membrane-resident protein.
The local PMID cache remains abstract-only; primary full-text access is not relabeled as
complete local caching.

The [primary ACAD10/11 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3073726/)
includes MCAD comparator activity and immunostaining data in sections 3.7/3.8. Its axon
observation is retained as non-core [PMID:21237683]. The staining does not by itself resolve
every molecule to mitochondria or define an axon-specific molecular function. General
mitochondrion annotations correctly describe the core compartment. Cytoplasm is compatible
but less informative and is refined to matrix, without asserting that the PAINT inference
is biologically false.

The sperm-nucleus source reports extensive removal of mitochondrial and other non-nuclear
structures [PMID:21630459; [publisher record](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/pmic.201000799)].
The full ACADM-specific identification/supplement was not recovered. The earlier confident
contamination claim is withdrawn; the nucleus HDA remains UNDECIDED. The MitoCoP main article
was inspected [PMID:34800366], but its individual ACADM supplementary entry was not re-extracted;
mitochondrion is accepted with curator deference and independent targeted evidence.

### Propagation and carnitine-process scope

All 19 electronic/phylogenetic assertions have source-entity assessments. PAINT inference
is evaluated as ancestral-node propagation, not as pairwise donor counting; no reconstructed
tree or IBD placement is claimed. The underlying ARBA predicates were not inspected and
are explicitly UNRESOLVED even where independent human evidence supports the annotation.
InterPro domain/site compatibility is distinguished from experimental proof of chemistry.
Rhea and EC mappings are checked against the unchanged curated catalytic record.

The Ensembl process transfers identify mouse Acadm P45952 / ENSMUSP00000072483 / MGI:87867.
Their exact term-specific donor evidence chain for glycogen biosynthesis, regulation of
gluconeogenesis and CoA-linked carnitine metabolism was not recovered. QuickGO retrieval
failed on DNS and MGI page access was incomplete; no matching ACADM/Acadm entry was found
in the local GO-CAM index. The mouse identity is corroborated by the
[Reactome ortholog reaction](https://reactome.org/content/detail/R-MMU-49491).
These three assertions are UNDECIDED rather than rejected as spurious transfers. A mouse
knockout article read as a lead ([primary article](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.0010023))
was not established as the donor source and is not substituted for that missing chain.

The [patient exercise study](https://pubmed.ncbi.nlm.nih.gov/16972171/)
measures carnitine-related plasma/urine changes and infers compensatory biosynthesis. Its
full text was not recovered. The CoA-linked carnitine and carnitine-biosynthesis IMP
assertions therefore remain UNDECIDED: the abstract alone does not show ACADM performing
a step in these processes. The FAO annotation is retained using independent human enzyme
evidence; increased octanoylcarnitine is not relabeled as directly quantified successful
MCAD flux. No additional process is proposed from metabolic necessity alone.

### Source-specific qualifications and numbering

All 13 PMID references received manual source-scope assessments. VERIFIED refers to
citation identity and the support explicitly described, not to complete full-text access
or resolution of every annotation. PMID:25416781 supplies ETF-dependent electron-transfer
evidence, but its locally recovered text lacks complete assay methods. PMID:1731887 supports
a mitochondrial location by a traceable statement. PMID:2393404 establishes a human disease
variant, not a purified-enzyme assay. Reactome expression-event location is the location of
the mature protein, not the site of transcription or translation.

The earlier variant numbering is reversed: c.985A>G is precursor p.Lys329Glu, conventionally
K304E after removal of the 25-residue targeting peptide. Likewise, mature Glu376 corresponds
to precursor Glu401. PMID:1902818 describes tetramer failure as a probable explanation for
variant inactivity. Full-text PMID:19224950 shows variant-dependent differences in assembly,
stability and kinetics, including variants with preserved tetramer assembly; it does not
justify assigning one identical mechanism to all missense alleles. Identical-protein binding
is retained as non-core based on measured wild-type homotetramers.

### Verification

The draft preserves all original source fields across 50 annotations and adds no NEW rows.
Initial `just validate human ACADM` passes without warnings or errors. History and rendered
HTML are generated from the final draft; an independent annotation review is requested before
publication. No Git state or shared project tracker was changed by this task.


### Independent review and recovered mouse donor provenance

Independent annotation review by the sibling annotation-reviewer found stale reference
findings concerning sperm-nucleus contamination, inferred exercise flux, probable tetramer
failure and a generic MitoCoP quote. These reviewer-authored statements were corrected to
match the source-scoped judgments above. Variant heterogeneity and cohort-specific allele
frequency were also clarified. IBA source-entity blocks retain the PTN ancestral node, as
the annotation-reviewer skill specifies, rather than templated extant-descendant lists.

The earlier unresolved-donor paragraph is superseded by a newly accessible
[MGI comparative Acadm graph](https://www.informatics.jax.org/homology/GOGraph/Acadm),
generated 2023-03-10. It explicitly lists mouse IMP evidence from PMID:18459129 / MGI:4412440
for all three disputed process annotations. The present web footer is newer than that
snapshot; no current GOA export or exact current Ensembl evidence selection is claimed.
The [primary PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/18459129/) was independently
verified. The sibling reviewer could additionally inspect methods/results through page 10
of an [author thesis chapter reproducing the study](https://pure.rug.nl/ws/portalfiles/portal/14546957/05c5.pdf).
Subsequent PDF requests timed out for both reviewers; the discussion was not read and no
complete full-paper access is claimed.

The source establishes stress-dependent metabolic effects. De novo G6P formation decreases
by about 20% during the LPS-induced acute phase response, while fasting alone has no such
reduction. G6P partitioning shifts toward glycogen. The glycogen-biosynthesis assertion is
therefore MARK_AS_OVER_ANNOTATED as a process-role overstatement; regulation of gluconeogenesis
is retained as a contextual non-core role. The partial methods/results include carnitine
pool assays; carnitine-process participation remains UNDECIDED because an unresolved
mechanism is not settled by altered metabolites. These are source-based judgments, not
an assertion that the mouse ortholog was misidentified.

Normal caching of the newly required PMID failed DNS (0/1 publications, no artifact), both
in the parent's canonical request and in an overlapping temporary-output probe initiated
before the parent's pending request was known. Neither source cache was fabricated. The
bibliographic entry is retained honestly; final publication must stay a draft until this
missing cache can be recovered normally. There are now 14 cited PMIDs, of which the original
13 remain cached and unchanged. Initial validation passed before adding the newly identified
source; the final validation report must be interpreted with this cache limitation.

Final targeted validation passes with one reference warning: `Could not fetch reference: PMID:18459129`. Rendering completes successfully. This operational limitation remains explicit; there are no schema, ontology, quotation or source-assertion errors.

Final independent signoff found no remaining blocking biological concern across all 50 rows, core functions, reference findings and notes. The missing PMID cache remains the publication limitation.
