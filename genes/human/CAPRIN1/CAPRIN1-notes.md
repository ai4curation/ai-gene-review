# CAPRIN1 (Caprin-1, Q14444) — curation notes

Reviewed for the [Stress Granule Assembly Project](../../../projects/STRESS_GRANULES.md)
(issue 3953). CAPRIN1 is one of the nine candidate genes in that project's table that had
no local gene folder.

## Provider deep research

No `-deep-research-<provider>.md` file could be generated for this gene in the run that
created this folder: `just deep-research-perplexity human CAPRIN1` failed with
`Provider 'perplexity' not available. Available: claude_code`, and the `claude_code`
provider needs `agentapi`, which is not on PATH in this environment. Per the repository
rule that self-written content must never be named `-deep-research-<provider>.md`, the
literature synthesis below lives in this notes file instead. Everything here is taken
from the cached publications under `publications/` and from the curated UniProt record
`CAPRIN1-uniprot.txt`.

## What the protein is

Caprin-1 is a 709-residue, ubiquitously expressed cytoplasmic phosphoprotein with an
N-terminal coiled-coil/dimerisation region (UniProt `COILED 60..94`, `COILED 125..153`)
and a long C-terminal intrinsically disordered region (`REGION 524..709 /note="Disordered"`,
evidence `ECO:0000269|PubMed:31439799`) that carries the RGG motifs used for RNA binding.
A discrete G3BP1-binding region is annotated at residues 360-381
(`ECO:0000269|PubMed:17210633, ECO:0000269|PubMed:36279435`).

The old names in the record — "GPI-anchored protein p137", "membrane component chromosome
11 surface marker 1" — are historical and wrong. UniProt carries an explicit caution:
[UniProtKB:Q14444 CC CAUTION, "Was originally thought to be a GPI-anchored membrane
protein."]. There is no transmembrane segment, signal peptide or lipid-anchor feature in
the record. This matters for the review, because GOA still carries a `GO:0016020 membrane`
row from an NK-cell membrane-fraction proteomics screen (PMID:19946888).

Paralog: CAPRIN2/RNG140 (Q6IMN6). Rodent orthologs are called RNG105 (Caprin1); the
paralog RNG140 is Caprin2.

## Core molecular activities

**Selective mRNA binding through C-terminal RGG motifs.**
[PMID:17210633 "The carboxy-terminal region of Caprin-1 selectively bound mRNA for c-Myc
or cyclin D2, this binding being diminished by mutation of the three RGG motifs and
abolished by deletion of the RGG-rich region."] The curated UniProt FUNCTION adds the
neuronal targets: "In neuronal cells, directly binds to several mRNAs associated with RNA
granules, including BDNF, CAMK2A, CREB1, MAP2, NTRK2 mRNAs, as well as to GRIN1 and KPNB1
mRNAs, but not to rRNAs (PubMed:17210633)." The two human mRNA-interactome-capture screens
that annotate CAPRIN1 (PMID:22658674, PMID:22681889) are oligo(dT)-based poly(A)+ captures,
so their own evidence is mRNA-specific rather than generic RNA binding.

**Condensate scaffolding by the C-terminal IDR.**
[PMID:34074792 "Using the C-terminal IDR (607 to 709) of CAPRIN1, an RNA-binding protein
found in stress granules, P bodies, and messenger RNA transport granules, we have developed
and applied a variety of NMR methods for studies of condensed IDR states to provide insights
into interactions driving and modulating phase separation."] UniProt's DOMAIN block states
it directly: [UniProtKB:Q14444 CC DOMAIN, "The C-terminal disordered region undergoes
liquid-liquid phase separation (LLPS) for the formation of a membraneless compartment that
concentrates mRNAs with associated regulatory factors"].

**ATP as a modulator of that condensation, not a catalytic cofactor.**
[PMID:36040869 "Upon phase separation, CAPRIN1 molecules in the condensed phase are neutral
(ϕENS [Formula: see text] 0 mV), with ∼five molecules of ATP associated with each CAPRIN1
chain."] and [PMID:34074792 "We identify ATP interactions with CAPRIN1 that can enhance or
reduce phase separation."] CAPRIN1 has no Walker motif or nucleotide-binding fold; the ATP
association is a direct but low-specificity electrostatic/hydrotropic interaction that tunes
LLPS. Real binding, peripheral function — reviewed as `KEEP_AS_NON_CORE`.

**Phospho-dependent co-condensation with FMRP, and recruitment of the CCR4-NOT deadenylase.**
[PMID:31439799 "We found that different FMRP serine/threonine and CAPRIN1 tyrosine
phosphorylation patterns control phase separation propensity with RNA, including
subcompartmentalization, and tune deadenylation and translation rates in vitro."] UniProt
records the tyrosine kinase and the recruited enzyme: nine `MOD_RES ... Phosphotyrosine; by
EPHA4` sites (625, 636, 639, 651, 662, 665, 670) with evidence `ECO:0000269|PubMed:31439799`,
and [UniProtKB:Q14444 CC FUNCTION, "In these cytoplasmic ribonucleoprotein granules, CAPRIN1
mediates recruitment of CNOT7 deadenylase, leading to mRNA deadenylation and degradation"].
This is modelled as a production GO-CAM, `gomodel:63894f2500001378` ("FMR1 and CAPRIN1
undergo liquid-liquid phase separation following phosphorylation, leading to formation of
non-membrane-bounded organelle that prevent mRNA translation"), whose CAPRIN1 nodes are
`GO:0003729`, `GO:0140693` and `GO:0035591`.

## Role in stress granules

CAPRIN1 is one of the two mutually exclusive partners of the G3BP1 NTF2-like domain, and the
one that pushes the switch towards assembly.

- [PMID:17210633 "Caprin-1 exhibits a highly conserved motif, F(M/I/L)Q(D/E)Sx(I/L)D that
  binds to the NTF-2-like domain of G3BP-1."]
- [PMID:27022092 "Caprin1/USP10 binding to G3BP is mutually exclusive: Caprin binding
  promotes, but USP10 binding inhibits, SG formation."]
- [PMID:32302571 "Further regulation of SG assembly arises through positive or negative
  cooperativity by extrinsic G3BP1-binding factors that strengthen or weaken, respectively,
  the core SG network."]
- [PMID:17210633 "Overexpression of Caprin-1 induced the formation of cytoplasmic stress
  granules (SG). Its ability to bind RNA was required to induce SG formation but not
  necessarily its ability to enter SG."]

The mechanism is not simply "Caprin-1 glues G3BP1 together": the two halves of the protein
pull in opposite directions. [PMID:36279435 "The C-terminal domain of Caprin-1 underwent
spontaneous LLPS, whereas the N-terminal domain and GIM of Caprin-1 suppressed LLPS of
G3BP1."] The net cellular effect of full-length Caprin-1 is still positive, which is what
the five IDA `GO:0062029` rows record.

Disease genetics reinforce the SG role from the other direction. [PMID:35977029 "We validated
that NDD-related de novo variants in newly implicated and known NDD genes, such as CAPRIN1,
disrupt the interaction of the core SG network and interfere with SG formation."]

## Translation repression is selective, not global

This is the point most likely to be mis-annotated. Overexpression does inhibit bulk
synthesis, but loss of the protein does not:
[PMID:17210633 "However, cells lacking Caprin-1 exhibited no changes in global rates of
protein synthesis, suggesting that physiologically, the effects of Caprin-1 on translation
were limited to restricted subsets of mRNAs."] So `GO:0017148 negative regulation of
translation` is correct, but it is target-mRNA-selective repression inside condensates, not
a global shutdown, and the eIF2-alpha phosphorylation seen on overexpression in that paper
should not be read as CAPRIN1 being an ISR kinase activator.

## Neuronal mRNA transport (basis for the one NEW row)

The rodent ortholog RNG105 is the founding dendritic RNA-granule protein, and the knockout
shows the transport defect directly: [PMID:20861386 "Here, we demonstrate that RNG105
knock-out in mice reduces the dendritic localization of mRNAs for Na+/K+ ATPase (NKA)
subunit isoforms (i.e., α3, FXYD1, FXYD6, and FXYD7)."] Mouse Caprin1 (Q60865) accordingly
carries `GO:0008298 intracellular mRNA localization` by IMP from that paper (MGI), but human
CAPRIN1 has no row for it, even though Ensembl Compara (`GO_REF:0000107`) transferred the
neighbouring `GO:0050775` and `GO:0061003` rows from the same mouse gene.

Comparator check before proposing it (per the `NEW` rules in CLAUDE.md): a QuickGO query by
term id for `GO:0008298` in human returns 20 annotations and is non-empty, so a negative
result would have been meaningful — and it is positive. mRNA-transport RBPs in the same role
do carry the term: STAU1 and STAU2 (IBA), PUM2 (IEA), QKI (IDA, PMID:37379838), ZNF385A
(ISS), HNRNPAB (IEA). CAPRIN1 performs the work rather than merely being required for it: it
binds the cargo mRNAs itself and is the granule component that carries them. Proposed as a
`NEW` ISS row from the mouse IMP, not as an experimental human claim.

The human phenotype is consistent: [PMID:35979925 "CAPRIN1 encodes a ubiquitous protein that
regulates the transport and translation of neuronal mRNAs critical for synaptic plasticity,
as well as mRNAs encoding proteins important for cell proliferation and migration in multiple
cell types."] Two Mendelian disorders are recorded in UniProt — NEDLAAD from haploinsufficiency
(PMID:35979925) and CONDCAC from the aggregation-prone P512L allele
[PMID:36136249 "Indeed, overexpressed CAPRIN1P512L forms insoluble ubiquitinated aggregates,
sequestrating proteins associated with neurodegenerative disorders (ATXN2, GEMIN5, SNRNP200
and SNCA)."].

## Annotation decisions worth recording

- **`GO:0016020 membrane` (HDA, PMID:19946888) → REMOVE.** A crude NK-cell membrane-fraction
  proteome hit for a protein with no transmembrane segment, signal peptide or lipid anchor,
  on an entry whose name history is precisely a refuted GPI-anchor claim that UniProt
  cautions against. Keeping it revives the error.
- **`GO:0035591 signaling adaptor activity` (IDA, PMID:31439799) → MODIFY to `GO:0060090`
  molecular adaptor activity.** The adaptor claim is right — CAPRIN1 brings CNOT7 to the
  condensed mRNA — but GO:0035591 is defined as bringing molecules together *in a signaling
  pathway* ("The binding activity of a molecule that brings together two or more molecules in
  a signaling pathway"). Deadenylase recruitment to an mRNP condensate is RNA processing, not
  signal transduction. The replacement is the parent term with the signaling restriction
  dropped, so this is a generalising MODIFY, not a demotion of the curator's reading. The same
  term is used for CAPRIN1 and for FMR1 in `gomodel:63894f2500001378`, so this is an explicit
  argument with a modelling decision rather than a gap being filled.
- **`GO:0140677 molecular function activator activity` (IDA, PMID:32302570) → MODIFY to
  `GO:0140693`.** GO:0140677's own comment restricts it to a regulator that "directly
  interacts with the enzyme"; the target here is G3BP1's condensate-scaffold activity, not an
  enzyme. CAPRIN1 is one of the connecting nodes of the reconstituted SG protein-RNA network
  in that paper, which is condensate scaffolding, and the review accepts `GO:0140693` on three
  other IDA rows.
- **`GO:0043232 intracellular membraneless organelle` → TOO_GENERAL.** `GO:0010494` and
  `GO:0036464` are both asserted and both entail it; on its own the term does not say which
  condensate.
- **`GO:0000932 P-body` (ISS from rat Q5M9G3) → KEEP_AS_NON_CORE.** The rat row is an IDA
  from PMID:20516077, and PMID:34074792 independently describes CAPRIN1 as found in P-bodies.
  Supported, but peripheral to the stress-granule/transport-granule core.
- **The 14 bare `GO:0005515` rows → REMOVE**, per the repository protein-binding policy. The
  interactions themselves (G3BP1, FXR2, FMR1, DDX3X, GIGYF2) are real and are recorded in the
  notes and in the informative MF/BP rows; removal says the generic term carries no functional
  information, not that the interactions are false.
- The two `GO:0003723 RNA binding` HDA rows and the rat ISS row are MODIFYed to `GO:0003729
  mRNA binding`, because each row's own evidence is mRNA-specific (poly(A)+ interactome
  capture; the rat IDA shows mRNA binding). The IBA row stays `ACCEPT`: the PAINT node asserts
  RNA binding across a family that includes the *Drosophila* member, and mRNA specificity is
  not established at that depth.
