# SPCH (SPEECHLESS) — research notes

UniProt: Q700C7 (SPCH_ARATH), AT5G53210, 364 aa, bHLH transcription factor (bHLH098 / AtbHLH98).
Taxon: Arabidopsis thaliana (NCBITaxon:3702).

## Overview / synthesized function

SPCH is the master bHLH transcription factor that initiates the stomatal cell
lineage. It is necessary and sufficient to trigger the asymmetric "entry"
divisions of meristemoid mother cells (MMCs) that establish the stomatal
lineage. It acts at the first step of a three-bHLH cascade (SPCH → MUTE →
FAMA): SPCH drives lineage initiation/amplifying asymmetric divisions, MUTE
drives the meristemoid-to-guard-mother-cell transition, and FAMA drives
terminal guard cell differentiation.

- [PMID:17183265 "we report the identification of a gene, SPEECHLESS (SPCH), encoding a basic helix-loop-helix (bHLH) transcription factor that is necessary and sufficient for the asymmetric divisions that establish the stomatal lineage in Arabidopsis thaliana"]
- [PMID:17183265 "We demonstrate that SPCH and two paralogues are successively required for the initiation, proliferation and terminal differentiation of cells in the stomatal lineage."]

## bHLH DNA-binding TF activity and heterodimerization

SPCH is a genuine sequence-specific DNA-binding transcription factor. It
functions as a heterodimer with SCRM/ICE1 (ICE1) and SCRM2; these heterodimers
are nuclear-localized DNA-binding transcription factors. The bHLH domain
(residues 99–150; basic motif 99–112) is required for DNA binding and target
gene activation.

- [PMID:18641265 "we identify two paralogous proteins, SCREAM (SCRM) and SCRM2, which directly interact with and specify the sequential actions of SPCH, MUTE, and FAMA"]
- [PMID:18641265 "these nuclear-localized bHLH heterodimers most likely act as DNA binding transcription factors"]
- UniProt SUBUNIT: "Forms dimers with SCRM and SCRM2 (PubMed:18641265, PubMed:28507175)."
- UniProt FUNCTION: "Activates transcription when in the presence of SCRM/ICE1 (PubMed:28507175). Functions as a dimer with SCRM or SCRM2 during stomatal initiation (PubMed:18641265)."
- GOA WITH/FROM for PMID:18641265 IPI annotations: UniProtKB:Q9LPW3 and UniProtKB:Q9LSE2 (SCRM/ICE1 and SCRM2).

The spch-5 allele carries a point mutation in the bHLH domain (R111W;
HVTVERNRR→PVTVPRNRP at 104-112) and shows decreased ability to initiate/amplify
lineages, defects in asymmetric cell fate allocation, and misorientation of
division planes — confirming the bHLH domain mediates SPCH's DNA-binding/
transactivation function in vivo.

- [PMID:28507175 "Our results also show that BR-dependent stomata formation and expression of some, but not all, SPCH target genes require the integrity of the bHLH domain of SPCH."]
- [PMID:28507175 "spch-5 leaf phenotype is dosage dependent and results from the decreased ability to initiate and amplify lineages, defects in asymmetric cell fate allocation, and misorientation of asymmetric division planes"]

GO:0001216 "DNA-binding transcription activator activity" definition (QuickGO):
"A DNA-binding transcription factor activity that activates or increases
transcription of specific gene sets." This is the IDA annotation from
PMID:28507175 (SPCH activates target gene transcription with SCRM/ICE1) — a
correct, specific MF for SPCH. It subsumes the more general GO:0003700
"DNA-binding transcription factor activity" (IEA/ISS).

## Subcellular localization

SPCH is nuclear. UniProt SUBCELLULAR LOCATION: Nucleus (PROSITE-ProRule and
PubMed:19008449 IDA). The cytoplasm annotation (GO:0005737) is from a single
computational predictor (AtSubP / GO_REF:0000122, ISM) and is not supported by
experimental data; SPCH function is nuclear. Treat cytoplasm as
over-annotation (prediction-only, contradicted by IDA nuclear localization).

- TAIR GOA: GO:0005634 nucleus IDA PMID:19008449.
- TAIR GOA: GO:0005737 cytoplasm ISM GO_REF:0000122 (AtSubP prediction only).

## Stomatal lineage / asymmetric cell division (core biological process)

SPCH controls regulation of stomatal complex development and stomatal complex
development by promoting the first asymmetric (entry) divisions and the
amplifying asymmetric divisions of the stomatal lineage.

- UniProt FUNCTION: "Required for the initiation, the spacing and the formation of stomata, by promoting the first asymmetric cell divisions (PubMed:19008449, PubMed:25680231, PubMed:25843888)."
- GO:2000038 "regulation of stomatal complex development" IMP PMID:19008449, PMID:25680231.
- GO:0010374 "stomatal complex development" IMP PMID:17183265.
- GO:0010052 "guard cell differentiation" IEA InterPro (family-level; SPCH itself acts upstream at lineage initiation rather than at terminal guard cell differentiation — that is FAMA's role — so this is a less precise / family-propagated term, KEEP_AS_NON_CORE).

## Regulation by MAPK and other kinases (PTM / activity regulation)

SPCH activity is negatively regulated by MPK3/MPK6 phosphorylation in a unique
MAPK target domain (the disordered region ~171-227, including Ser193, Ser211,
Thr214, Ser219). This couples the EPF–ERECTA/TMM–YODA(YDA) MAPK cascade to
stomatal patterning. SPCH is also phosphorylated by BIN2/ASK7 (GSK3-like;
inhibitory) and stabilized by CDKA;1 phosphorylation at Ser186 (promotes
stomatal development).

- [PMID:19008449 "a unique domain in a basic helix-loop-helix (bHLH) stomatal initiating factor, SPEECHLESS, renders it a MAPK phosphorylation target in vitro and modulates its function in vivo"]
- [PMID:19008449 "Positively acting transcription factors and negatively acting mitogen-activated protein kinase (MAPK) signaling control stomatal development in Arabidopsis"]
- [PMID:25680231 "phosphorylation at Serine 186 is positively required for SPCH function in regulating stomatal development"]
- GOA WITH/FROM for PMID:25680231 IPI: UniProtKB:P24100 (CDKA;1 / CDC2).

## Osmotic stress / low humidity (environmental integration; non-core)

SPCH protein level is post-transcriptionally decreased under osmotic stress via
the MAPK cascade, providing a route by which environmental stress reduces
growth by reducing MMC number. This is environmental modulation of SPCH abundance
(SPCH is the developmental effector), not a dedicated stress-response function
of SPCH itself.

- [PMID:25381317 "Arabidopsis plants, in response to osmotic stress, post-transcriptionally decrease the protein level of SPEECHLESS, the transcription factor promoting MMC identity, through the action of a mitogen-activated protein kinase (MAPK) cascade"]
- [PMID:25381317 "The growth reduction under osmotic stress was lessened by inhibition of the MAPK cascade or by a mutation that disrupted the MAPK target amino acids in SPEECHLESS"]
- GO:0006970 response to osmotic stress IEP PMID:25381317; GO:0047484 regulation of response to osmotic stress IMP PMID:25381317.

Low relative humidity (LRH) represses SPCH transcription via RNA-directed de
novo DNA methylation (RdDM) of the SPCH locus. Here SPCH is the target/effector
of the epigenetic response; the "response to low humidity" IEP captures
SPCH transcriptional repression under LRH, a downstream/environmental modulation
rather than a core SPCH molecular function.

- [PMID:22442411 "two genes in the stomatal development pathway, SPEECHLESS and FAMA, become de novo cytosine methylated and transcriptionally repressed"]
- [PMID:22442411 "growth under low relative humidity (LRH) induced additional methylation in two stomatal development gene loci, SPCH and FAMA"]
- GO:0090547 response to low humidity IEP PMID:22442411.

## Protein binding (GO:0005515) annotations — IPI

Three IPI "protein binding" annotations exist:
- PMID:18641265 → SCRM/ICE1 (Q9LPW3) and SCRM2 (Q9LSE2): functionally the core bHLH heterodimerization partners. Per curation guidelines, "protein binding" is uninformative; the informative term is protein dimerization activity / bHLH heterodimerization (captured by GO:0046983 and by core_functions). Keep as non-core (records a real, important interaction but with an uninformative MF term).
- PMID:25680231 → CDKA;1 (P24100): a regulatory kinase interaction (Ser186 phosphorylation). Real but uninformative MF term.
- PMID:32612234 → RACK1B (Q9C4Z6): from a large-scale phytohormone interactome (Y2H) screen. UniProt INTERACTION block records Q700C7–Q9C4Z6 (RACK1B), NbExp=3. High-throughput interactome; biological significance for SPCH unclear; uninformative MF term. Keep as non-core, not core.

GO:0046983 "protein dimerization activity" IEA InterPro: family-level but
biologically correct — SPCH forms bHLH dimers (with SCRM/SCRM2). This is the
informative MF version of the "protein binding" interactions and supports the
heterodimerization core function.

## TAS/family annotations

- GO:0006355 regulation of DNA-templated transcription: TAS PMID:11118137 (genome-wide TF survey) and IEA ARBA. SPCH is a transcriptional regulator; correct but general. The acts_upstream_of_or_within TAS is a generic TF statement.
- GO:0045893 positive regulation of DNA-templated transcription: IBA/IEA (GO_REF:0000108 inferred from GO:0001216). SPCH activates target genes (with SCRM/ICE1), so positive regulation of transcription is biologically supported.
- GO:0003700 DNA-binding transcription factor activity: ISS PMID:12679534, PMID:11118137 (bHLH family assignments). Correct but general; subsumed by the specific IDA GO:0001216.

## Interactor identity reference (from UniProt / GOA WITH-FROM)
- Q9LPW3 = SCRM / ICE1 (SCREAM)
- Q9LSE2 = SCRM2 (SCREAM2)
- P24100 = CDKA;1 (CDC2 / cyclin-dependent kinase A;1)
- Q9C4Z6 = RACK1B (receptor for activated C kinase 1B); UniProt INTERACTION: "Q700C7; Q9C4Z6: RACK1B; NbExp=3"
</content>
</invoke>
