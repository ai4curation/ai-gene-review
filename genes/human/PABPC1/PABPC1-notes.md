# PABPC1 (P11940) — curation notes

Created for the [stress granule project](../../../projects/STRESS_GRANULES.md) (issue 3953),
which lists PABPC1 among the unreviewed RNA-binding recruits of stress granules.

No external deep-research provider was reachable in this environment (no Perplexity,
OpenAI, Falcon or Asta credentials), so there is no `PABPC1-deep-research-*.md` file.
These notes are my own synthesis from the cached publications, the UniProt record and
the GOA table, with provenance for every assertion.

## Summary of what the protein is

PABPC1 is the major cytoplasmic poly(A)-binding protein: four tandem RRMs (residues
11-89, 99-175, 191-268, 294-370), a proline-rich linker, and a C-terminal MLLE/PABC
peptide-binding domain (542-619) [file:genes/human/PABPC1/PABPC1-uniprot.txt
"DOMAIN 542..619 /note=\"PABC\""]. The N-terminal RRM array is the poly(A)-binding
module: the first cDNA paper already showed "The N terminal part, highly homologous to
the yeast poly(A) binding protein, is sufficient for poly(A) binding activity"
[PMID:2885805]. Binding is A-selective and high-affinity — "the hPABP selects
oligo(rA)-rich sequences and it binds oligo(rA)25 with an apparent Kd of 7 nM", about
100-fold tighter than unrelated RNA [PMID:7908267].

It is extraordinarily abundant: "growing HeLa cells contain a surprisingly high number
of approximately 8 x 10(6) PABP molecules per cell, which corresponds to an
intracellular concentration of about 4 microM", roughly a three-fold excess over
cytoplasmic poly(A) binding sites [PMID:7908267]. That abundance matters for curation:
PABPC1 turns up in many whole-fraction proteomes (membrane, focal adhesion,
extracellular exosome, purified spliceosome) where there is no evidence it does any
work.

## Core activity 1: poly(A) binding that drives closed-loop translation initiation

PABPC1 bridges the 3' poly(A) tail to the cap-binding complex through eIF4G: "The
PABP-eIF4G interaction brings about the circularization of the mRNA by joining its 5'
and 3' termini, thereby stimulating mRNA translation" [PMID:11997512]. The contact is
structurally defined and allosterically coupled to RNA: the crystal structure of
poly(A)11·PABP(1-190)·eIF4G(178-203) shows "eIF4G interacts with the RRM2 domain of
PABP", and "this interaction is allosterically regulated by poly(A) binding to PABP"
[PMID:23041282].

Two dedicated regulators tune the activity in opposite directions. Paip1 binds with 1:1
stoichiometry and "an apparent K(d) of 1.9 nM" through two motifs, PAM1 and PAM2
[PMID:11997512]; Paip2 and its homolog Paip2B "inhibit translation of capped and
polyadenylated mRNAs both in vitro and in vivo by displacing PABP from the poly(A)
tail" [PMID:16804161].

The MLLE/PABC domain is a peptide-binding module, not an RNA-binding one: "In protein
synthesis, the PABC domain of PABP functions to recruit several translation factors
possessing the PABP-interacting motif 2 (PAM2) to the mRNA poly(A) tail"
[PMID:14685257]. The PAM2 clients catalogued in UniProt include PAIP1, PAIP2, PAIP2B,
eRF3a/eRF3b (GSPT1/GSPT2), LARP1, LARP4, LARP4B, ataxin-2, HELZ, PAN3 and the GW182
proteins TNRC6A/B/C. This is why ~60% of PABPC1's GOA rows are bare `protein binding`:
GO has no term for the activity that unifies them (see "Ontology gap" below).

## Core activity 2: protecting the poly(A) tail, and setting mRNA fate at termination

PABPC1 shields long tails from the uridylation that marks mRNA for decay: "PABPC1
antagonizes uridylation of polyadenylated mRNAs, contributing to the specificity for
short A-tails" [PMID:25480299]. In the c-fos mCRD system it is part of a five-protein
bridging complex (Unr/CSDE1, PABP, PAIP1, hnRNP D, NSAP1/SYNCRIP) whose overexpression
"stabilized mCRD-containing mRNA by impeding deadenylation" [PMID:11051545]; that
complex is the referent of `GO:0106002` and of ComplexPortal CPX-1076.

At the stop codon PABPC1 is an NMD antagonist. It "inhibits the interaction between
eRF3 and Upf1 in vitro and prevents NMD in cells when positioned in proximity to the
termination codon" [PMID:18447585]; the authors propose that mRNAs with long 3' UTRs
that nonetheless escape NMD "have evolved to concentrate NMD-inhibiting factors, such
as PABP, in spatial proximity of the termination codon" [PMID:18447585]. The eRF3
contact is through the C-terminus: "the last 39 C-terminal amino acids of PABP contain
the interface that interacts with eRF3" [PMID:12489690].

The deadenylation story is genuinely two-sided, and GOA reflects that with
opposite-sign rows. PABPC1 recruits PAN3 (and so the PAN2-PAN3 deadenylase) and the
Tob/CCR4-NOT machinery through the same MLLE surface, which is the basis of the
`positive regulation of ... poly(A) tail shortening` ISS rows transferred from yeast
Pab1 (UniProtKB:P29341); it simultaneously protects the tail as above. Both claims are
kept in this review, in different contexts, rather than one being removed.

## Stress granules and other granules

PABPC1 is the canonical stress-granule marker. It is "generally a diffuse cytoplasmic
protein" that "can be found in discrete foci such as stress and neuronal granules"
[PMID:21940797], and DDX3X-dependent stressors "direct DDX3 with eIF4E and PABP1 into
SGs, but not to processing bodies" [PMID:21883093]. Granule recruitment is not merely
passive: knocking down DDX3X "interfered with SG assembly, led to nuclear accumulation
of PABP1 and reduced cell viability following stress" [PMID:21883093]. UniProt records
direct interactions with both nucleators, "Interacts with G3BP1 and G3BP2"
[file:genes/human/PABPC1/PABPC1-uniprot.txt "Interacts with G3BP1 and G3BP2"], which is
how the gene connects to the G3BP1/G3BP2 module this project is building.

It is also a component of other cytoplasmic RNP granules that are *not* stress
granules: Staufen transport granules, where "Ribosomes and proteins involved in the
control of protein synthesis (PABP1 and FMRP) were present in purified hStaufen
complexes" [PMID:15121898], and IMP1/IGF2BP1 granules, which "consisted of IMPs, 40 S
ribosomal subunits, shuttling heterologous nuclear RNPs, poly(A)-binding proteins, and
mRNAs" and which "lacked eIF4E, eIF4G, and 60 S ribosomal subunits, indicating that
embodied mRNAs are not translated" [PMID:17289661]. So `cytoplasmic ribonucleoprotein
granule` is carrying real, distinct information here rather than being a redundant
parent of `cytoplasmic stress granule`.

A caution on the stress-granule row qualified `is_active_in` (the PANTHER IBA row):
stress granules are "sites of translational silencing" [PMID:21883093], so asserting
that PABPC1's activity *occurs* there is not the same as saying it is located there.
This review keeps the location and flags the qualifier.

## Nucleocytoplasmic shuttling: real, but conditional

PABPC1 shuttles: nuclear accumulation follows transcription inhibition, the minimal
shuttling unit is the first two RRMs, and shuttling was confirmed by heterokaryon
fusion [PMID:9582337]. But at steady state the protein is cytoplasmic — confocal
immunofluorescence "reveals that it is localized exclusively to the cytoplasm"
[PMID:7908267]. The mechanism of relocalisation is a block in mRNA export, not a
nuclear function: "perturbations that block mRNA export recapitulate PABP
relocalisation", supporting "a model in which nuclear export of PABPs is dependent on
ongoing mRNA export" [PMID:21940797]. Rotavirus NSP3 produces the same end state by
evicting PABP from eIF4G, and nuclear accumulation then requires the RoXaN LD domain
acting as a nuclear export signal [PMID:18799579]. The `nucleus` rows are therefore
kept as non-core rather than accepted as a site of function.

The same reasoning is why the two splicing-related rows are marked over-annotated.
PABPC1 was detected by mass spectrometry in affinity-purified native C complex
[PMID:11991638], and UniProt records "Identified in the spliceosome C complex"
[file:genes/human/PABPC1/PABPC1-uniprot.txt "Identified in the spliceosome C complex"].
But nothing in that work, or anywhere else I could find, assays a contribution of
PABPC1 to splicing; an abundant poly(A)-tail-binding protein co-purifying with a
spliceosome assembled on a polyadenylated substrate is the expected passenger. Note
also that UniProt's FUNCTION line asserts regulation of "pre-mRNA splicing" citing
PubMed:11051545, PubMed:17212783 and PubMed:25480299 — none of which is about splicing;
that is recorded as a source defect in the review.

## Virus interactions

PABPC1 is a recurrent viral target, and UniProt summarises the strategies: "Many
viruses shutoff host mRNA translational machinery by inhibiting cellular PABPC1
activity using different mechanisms. Picornaviruses, caliciviruses or lentiviruses
encode proteases that cleave PABPC1 ... Rotaviruses, gammherpesviruses and bunyamwera
virus relocalize PABPC1 from the cytoplasm to the nucleus"
[file:genes/human/PABPC1/PABPC1-uniprot.txt]. Conversely some viruses need it: siRNA
against PABPC1 in HepG2 cells reduced dengue replication, "implying that PABPC1 and
LARP1 positively impact DENV replication", with the authors checking that the effect
was not a growth defect [PMID:26735137]. That is the basis of the single IMP row, kept
as non-core host-factor biology.

## Disease

Heterozygous de novo missense variants clustering in the MLLE/PABP domain cause
developmental delay with speech delay and autistic features; coimmunoprecipitation
"showed a significant weakening of the interaction between mutant PABPC1 and PAIP2",
and in mouse "Pabpc1 knockdown decreases the proliferation of neural progenitor cells"
with rescue by wild type but not by three of four variants [PMID:35511136]. The
mechanism proposed is "interference with the translation initiation and subsequently an
impaired neurogenesis in cortical development" [PMID:35511136] — i.e. the disease
supports the closed-loop initiation function rather than adding a new one.

## Ontology gap: PAM2 motif binding

Ninety-seven of the 167 GOA rows are bare `GO:0005515 protein binding`, and a large
share of them are the same molecular event: a PAM2 motif docking into the MLLE/PABC
pocket. GO already has region- and motif-level binding terms (`GO:0070064` proline-rich
region binding, `GO:0031369` translation initiation factor binding), so a `PAM2 motif
binding` child of `protein binding` would convert a long tail of uninformative rows
into one informative molecular function. The structural basis is characterised in
[PMID:14685257] (PABC-Paip1/Paip2 peptide complexes), [PMID:20418951] (eRF3 MLLE),
[PMID:20181956] (GW182 and ataxin-2 on the MLLE) and [PMID:21098120] (LARP4 variant
PAM2w). This is recorded in `proposed_new_terms`.

## Curation decisions worth flagging

- The three EIF4G1 `protein binding` rows are MODIFYed to `GO:0031369 translation
  initiation factor binding` rather than removed, because that is the informative
  molecular function the policy asks for and each cited paper assays the PABP-eIF4G
  contact directly.
- `GO:0003723 RNA binding` IPI from [PMID:23041282] carries `RNAcentral:URS000080E35F_32630`
  (a poly(A) oligomer) as the interacting entity, so it is MODIFYed to `poly(A) binding`.
  The companion `mRNA binding` EXP row from the same paper is kept: `poly(A) binding`
  sits under single-stranded RNA binding, not under mRNA binding, so that would be a
  lateral move rather than a refinement.
- `GO:0008266 poly(U) RNA binding` is kept as non-core. It is directly measured —
  "PABP1 and Sam68, bound with similar efficiency to both polyU and polyA RNAs"
  [PMID:21984414] — but on beads from nuclear extract, and it sits against the
  A-selectivity measured in [PMID:7908267]. Real, peripheral.
- A new `mRNA 5'-UTR binding` row is proposed: PABP binds the adenine-rich
  autoregulatory sequence in the 5' UTR of its own mRNA with a measured dissociation
  constant of 2.3 nM [PMID:17212783]. This is the autoregulatory arm of the gene and
  nothing in GOA captures it.
- `membrane` (NK-cell membrane proteome) and `extracellular exosome` (urinary exosome
  proteome) are marked over-annotated: no transmembrane segment or lipid anchor exists
  in the record, and a 4 µM cytosolic protein in a crude fraction is the expected
  background.
