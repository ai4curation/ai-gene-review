# DREB2A (At5g05410, UniProt O82132) — Gene Review Notes

Arabidopsis thaliana DEHYDRATION-RESPONSIVE ELEMENT-BINDING PROTEIN 2A.
AP2/ERF-family transcription factor. ORF/locus AT5G05410; synonym ERF045.

## Summary of biology

DREB2A is a sequence-specific DNA-binding transcription factor of the AP2/ERF
superfamily (ERF/DREB subfamily) that binds the dehydration-responsive
element / C-repeat (DRE/CRT) cis-element, core motif A/GCCGAC, in target gene
promoters and activates their transcription. It is a master regulator of the
ABA-independent branch of drought-, high-salinity- and heat-stress-responsive
gene expression in Arabidopsis. A central negative regulatory domain (NRD; the
~30 aa region between residues 136-165, containing a PEST sequence) targets the
protein for ubiquitin-mediated degradation by the RING E3 ligases DRIP1/DRIP2
and the 26S proteasome; deletion of this region produces a constitutively active
form (DREB2A-CA) that confers drought and heat tolerance. Under heat stress
DREB2A is stabilized and induces the heat-stress regulatory cascade, including
the heat-shock transcription factor gene HsfA3.

## DNA binding / TF activity / nucleus (core functions)

- DREB2A binds the DRE sequence in vitro and activates DRE-driven reporter
  transcription in Arabidopsis protoplasts. [PMID:9707537 "Both the DREB1A and DREB2A proteins specifically bound to the DRE sequence in vitro and activated the transcription of the b-glucuronidase reporter gene driven by the DRE sequence in Arabidopsis leaf protoplasts."]
- Core binding motif A/GCCGAC; DREB2A prefers ACCGAC and can also recognize
  A/GCCGACNA/G/C. [PMID:16617101 "We found that the DREB2A protein could recognize not only A/GCCGACNT, but also A/GCCGACNA/G/C, and prefers ACCGAC to GCCGAC."]
- AP2/ERF DNA-binding domain (UniProt FT DNA_BIND 78..135); mutagenesis of
  V91 and E96 affects CRT/DRE binding. [file:ARATH/DREB2A/DREB2A-uniprot.txt "MUTAGEN 91 ... V->A: Affects the binding to the CRT/DRE cis-element."]
- Nuclear localization: GFP-DREB2A localizes to the nucleus; the protein
  carries an N-terminal NLS. [PMID:16617101 "Synthetic green fluorescent protein gave a strong signal in the nucleus under unstressed control conditions when fused to constitutive active DREB2A but only a weak signal when fused to full-length DREB2A."]
  IDA nuclear localization also reported by PMID:18552202 and PMID:25490919.
- Transcriptional activation domain maps to the acidic C-terminus (residues
  254-335). [PMID:16617101 "DREB2A domain analysis using Arabidopsis protoplasts identified a transcriptional activation domain between residues 254 and 335"]

## Drought / water deprivation / osmotic stress

- DREB2A (and DREB2B) genes are induced by dehydration and high-salt stress.
  [PMID:10809011 "Northern analysis showed that both genes are induced by dehydration and high-salt stress."]
- DREB2A-CA overexpression confers drought tolerance and upregulates many water
  stress-inducible genes. [PMID:16617101 "Overexpression of constitutive active DREB2A resulted in significant drought stress tolerance but only slight freezing tolerance in transgenic Arabidopsis plants."]
- IMP annotation to "response to water deprivation" via dreb2a phenotype.
  [PMID:17030801 "DREB2A up-regulated genes were down-regulated in DREB2A knockout mutants under stress conditions."]

## Heat stress / heat acclimation

- DREB2A has dual function in water- and heat-stress responses; DREB2A-CA
  overexpression induces heat-shock-related genes including AtHsfA3 and HSPs,
  and increases thermotolerance; dreb2a knockouts have reduced thermotolerance.
  [PMID:17030801 "Thermotolerance was significantly increased in plants overexpressing DREB2A CA and decreased in DREB2A knockout plants. Collectively, these results indicate that DREB2A functions in both water and HS-stress responses."]
- DREB2A controls HsfA3 as a downstream gene in the heat-stress regulatory
  network. [PMID:17030801 "DREB2A controls HSF as one of the downstream genes."]
- DREB2A is stabilized in the nucleus under heat stress. [PMID:17030801 "These data indicate that the DREB2A protein is stabilized by HS stress and nuclear-localized during stress conditions."]
- Heat-stress-specific positive regulation (IDA, response to heat + positive
  regulation of transcription) via the DPB3-1/NF-YA2/NF-YB3 trimer that enhances
  DREB2A transactivation of HsfA3. [PMID:25490919 "The identified trimer comprising NF-YA2, NF-YB3, and DPB3-1 enhanced HsfA3 promoter transactivation by DREB2A"]
- Heat-acclimation expression study (transcript-level only): DREB2-subfamily
  genes induced under heat stress in suspension cultures — this is an
  expression/cross-talk observation, not a DREB2A-function knockout assay.
  [PMID:16807682 "the transcriptional induction of DREB2 (dehydration responsive element-binding factor 2) subfamily genes and COR47/rd17 under heat stress suggested cross-talk between the signaling pathways for heat and dehydration responses."]

## Post-translational regulation / degradation (DRIP1/DRIP2)

- Central NRD (residues ~136-165) contains a PEST sequence; full-length DREB2A
  is unstable and degraded by the 26S proteasome; deletion gives DREB2A-CA.
  [PMID:16617101 "The DREB2A FL protein containing the PEST sequence may be degraded rapidly by the ubiquitin-proteasome system, whereas DREB2A CA may have a long lifetime in the nucleus."]
- DRIP1 and DRIP2 are C3HC4 RING-domain E3 ubiquitin ligases that interact with
  DREB2A in the nucleus and mediate its ubiquitination and proteasomal
  degradation, negatively regulating drought-responsive gene expression.
  [PMID:18552202 "DRIP1 and DRIP2 act as novel negative regulators in drought-responsive gene expression by targeting DREB2A to 26S proteasome proteolysis."]
- The DRIP1 interaction underpins the GO:0005515 IPI (WITH UniProtKB:Q9M9Y4 =
  DRIP1, and Q94AY3 = DRIP2). [file:ARATH/DREB2A/DREB2A-goa.tsv "PMID:18552202\tUniProtKB:Q9M9Y4"]

## Protein-protein interactions (GO:0005515 IPI annotations)

These are real, experimentally supported interactions but "protein binding"
(GO:0005515) is uninformative as a molecular function. Underlying interactors:
- DRIP1 (Q9M9Y4) / DRIP2 (Q94AY3) — RING E3 ligases. [PMID:18552202]
- RCD1 (Q8RY59) — Radical-induced Cell Death1; SLiM-mediated binding to the
  RCD1 RST domain. [PMID:27881680] and [PMID:19548978 RCD1/SRO1].
- MED25 (Q7XYY2 / Q7XYY2-1) — Mediator subunit; interaction reported, with NMR
  structural data on a DREB2A peptide (PDB 5OAP, residues 255-272). [PMID:21536906], [PMID:22447446]
- DPB3-1 / NF-YC10 (Q9LN09) — heat-stress coactivator. [PMID:25490919]
- DOG1 (A0SVK0) and IMPA6 (Q9FWY7) — large-scale interactome. [PMID:32612234]

UniProt INTERACTION block confirms DOG1, DRIP1, IMPA6, MED25, RCD1.
[file:ARATH/DREB2A/DREB2A-uniprot.txt "O82132; Q9M9Y4: DRIP1; NbExp=4"]

## Target-promoter binding annotations (GO:0000976, IPI, WITH AGI loci)

Multiple TAIR annotations to "transcription cis-regulatory region binding"
(GO:0000976) with WITH-field AGI loci come from large yeast-one-hybrid /
gene-regulatory-network screens (enhanced Y1H, secondary cell wall network,
nitrogen network, PXY/vascular network, PRC2 regulation, plant-defense network).
These document DREB2A binding to specific target promoters and support the
sequence-specific DNA-binding TF function, although several of the networks
(secondary cell wall, vascular development, nitrogen metabolism, PRC2) are
contexts where DREB2A is a node in a large Y1H matrix rather than an established
in planta regulator. [PMID:22037706 Enhanced Y1H], [PMID:25533953 secondary cell wall GRN], [PMID:31806676 PXY vascular network], [PMID:30356219 nitrogen network], [PMID:27650334 PRC2], [PMID:25352272 plant-defense promoter integration].

## Weaker / expression-readout annotations (candidates for non-core or over-annotation)

- response to UV-B (GO:0010224): DREB2A (At5g05410) appears as a UV-B-*induced*
  transcript whose induction depends on HY5; it is a downstream readout, not an
  effector demonstrated to act in the UV-B response.
  [PMID:14739338 "we found that loss of HY5 impairs the UV-B-responsive expression of several genes, including ... At5g05410 ( DREB2A )"]
  PMID:18266923 is about a novel UV-B cis-element (UVBox) on ANAC13 and does not
  establish a DREB2A UV-B function; its abstract does not mention DREB2A.
  [PMID:18266923 "two cis-regulatory elements, designated MRE(ANAC13) and UVBox(ANAC13), are required for maximal UV-B induction of the ANAC13 gene"]
- response to hydrogen peroxide (GO:0042542, IEP, PMID:17030801): the cited
  paper is the dual drought/heat function paper; H2O2 response is not its focus.
  Treat as non-core expression-association.
- cellular response to hypoxia (GO:0071456, HEP, PMID:31519798): high-throughput
  expression/epigenome study; DREB2A/heat-stress transcripts are progressively
  upregulated during hypoxia. HEP = inferred from high-throughput expression
  pattern; a transcript-level association, non-core.
  [PMID:31519798 "Hypoxia promoted a progressive upregulation of heat stress transcripts"]
- heat acclimation (GO:0010286, IEP, PMID:16807682): transcript induction in
  suspension cultures; expression-based, non-core (but biologically consistent
  with the heat role).

## Provenance / IEA backbone annotations

- GO:0003677 DNA binding (IEA, InterPro IPR016177) — correct, subsumed by the
  experimental DNA-binding TF activity.
- GO:0003700 DNA-binding transcription factor activity (IEA InterPro;
  IDA PMID:9707537; ISS PMID:11118137) — core, experimentally supported.
- GO:0005634 nucleus (IEA SubCell; ISM AtSubP; IDA PMID:16617101/18552202/25490919/21443605)
  — core, multiple IDA.
- GO:0006355 regulation of DNA-templated transcription (IEA InterPro) — correct
  but general; the experimental data support positive regulation specifically.

## Conclusions for review actions

Core: GO:0003700 (DNA-binding TF activity), GO:0000976 (DRE/CRT cis-regulatory
region binding), GO:0005634 (nucleus), GO:0045893 (positive regulation of
transcription), GO:0009414 (response to water deprivation), GO:0009408 (response
to heat). DNA binding (GO:0003677) and regulation of transcription (GO:0006355)
are accepted as correct but general/non-core electronic backbone.
The eight GO:0005515 "protein binding" IPI annotations are real interactions but
uninformative as MF; mark over-annotated (do not endorse as core).
UV-B, H2O2, hypoxia, heat-acclimation are expression-readout associations →
keep as non-core.
