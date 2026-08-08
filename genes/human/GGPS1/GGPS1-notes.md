# GGPS1 (human) — curation notes

UniProt: O95749 (GGPPS_HUMAN). Gene symbol GGPS1 (HGNC:4249). 300 aa, ~34.9 kDa.
Two isoforms (O95749-1 displayed; O95749-2 lacks residues 1..54, VSP_056578).

## Identity / core function

GGPS1 encodes **geranylgeranyl pyrophosphate synthase (GGPP synthase / GGPPSase)**, a
cytosolic *trans*-prenyltransferase of the FPP/GGPP synthase family (Pfam PF00348
polyprenyl_synt; PANTHER PTHR12001). It catalyzes sequential head-to-tail (1'-4)
condensations of isopentenyl diphosphate (IPP) onto an allylic diphosphate primer to
build the C20 isoprenoid **geranylgeranyl diphosphate (GGPP)**.

UniProt lists three catalytic-activity reactions with distinct EC numbers, all supported
experimentally by the crystallographic study (PubMed:16698791):
- IPP + DMAPP → geranyl-PP (GPP) + PPi (EC 2.5.1.1)
- IPP + GPP → farnesyl-PP (FPP) + PPi (EC 2.5.1.10)
- IPP + FPP → geranylgeranyl-PP (GGPP) + PPi (EC 2.5.1.29)  ← the physiologically defining step
[file:human/GGPS1/GGPS1-uniprot.txt "Reaction=isopentenyl diphosphate + (2E,6E)-farnesyl diphosphate = (2E,6E,10E)-geranylgeranyl diphosphate + diphosphate"]

The enzyme requires Mg2+ (binds 3 Mg2+ ions) [file:human/GGPS1/GGPS1-uniprot.txt "Binds 3 Mg(2+) ions"] and is
subject to product inhibition by GGPP [file:human/GGPS1/GGPS1-uniprot.txt "Subject to product inhibition by geranylgeranyl"].

Human recombinant enzyme makes GGPP from FPP + IPP:
[PMID:10026212 "The GGPPSase expressed in Escherichia coli catalyzes the GGPP formation (240 nmol/min/mg) from FPP and isopentenyl diphosphate."]
[PMID:9741684 "Recombinant, purified histidine-tagged protein exhibited the enzymatic properties associated with GGPP synthase, namely the synthesis of GGPP from farnesyl diphosphate and isopentenyl diphosphate."]

## Biological role

GGPP is the C20 isoprenoid lipid donor for **protein geranylgeranylation**. GGTase-I and
RabGGTase (GGTase-II) transfer GGPP onto C-terminal cysteines of small GTPases of the
Rho/Rac and Rab families, anchoring them to membranes. GGPP is also a precursor for
ubiquinone/dolichol side chains and other isoprenoids.
[PMID:32403198 "For geranylgeranylation, FPP has to be converted to geranylgeranyl pyrophosphate (GGPP), by geranylgeranyl diphosphate synthase (GGPPS; EC:2.5.1.29), encoded by GGPS1. GGPP will then be transferred by 2 types of geranylgeranyl transferase (GGTase I or GGTase II) onto the recipient proteins."]

The enzyme sits in the mevalonate/isoprenoid branch downstream of FPP synthase; UniProt
records three UniPathway steps (geranyl-PP, farnesyl-PP, geranylgeranyl-PP biosynthesis).

## Structure / oligomeric state

Human GGPPS is a **homohexamer (trimer of homodimers)**; crystal structure at 2.7 Å with
Mg and geranylgeranyl phosphate bound (PubMed:16698791).
[file:human/GGPS1/GGPS1-uniprot.txt "Homohexamer; trimer of homodimers."]
The gel-filtration ~280 kDa oligomer was seen in the earliest characterization
[PMID:10026212 "The human GGPPSase behaves as an oligomeric molecule with 280 kDa on a gel filtration column"].
This hexameric self-association is the basis of the IPI "identical protein binding"
(GO:0042802) annotations (self-interaction O95749–O95749 in HuRI/interactome screens).

## Localization

Cytosolic. HPA immunofluorescence → cytosol (IDA, GO_REF:0000052).
Disease paper (PubMed:32403198) immunohistochemistry:
- Dermal fibroblasts: uniform cytoplasmic + perinuclear + some organelles
  [PMID:32403198 "In human dermal fibroblasts, GGPPS showed a rather uniform cytoplasmic expression, along with signals concentrated in some organelles and in the perinuclear region."]
- Skeletal muscle: prominent **Z disc** localization (co-labeled with desmin)
  [PMID:32403198 "GGPPS showed a prominent Z disc localization (Z disc labeled with desmin antibody) in the longitudinal section of normal human muscle biopsy."]

Note: cytoplasm/perinuclear/Z-disc are the annotated locations; the Z-disc/sarcomeric and
perinuclear pools likely reflect a tissue-specific, possibly non-catalytic
scaffolding/localization role suggested by the disease-mutation cluster (see below).

## Disease

Biallelic (recessive) GGPS1 missense variants cause **Muscular dystrophy, congenital
hearing loss, and ovarian insufficiency syndrome (MDHLO; MIM:619518)**
(PubMed:32403198). Recurrent variants (F257C, Y259C, R261G, R261H; plus P15S) cluster in a
5-residue microdomain in the 11th α-helix on the outer surface of the hexamer, OUTSIDE the
catalytic barrel; this domain is conserved in animals but not plants.
[PMID:32403198 "The mutations do not abolish enzymatic activity of this essential enzyme, but with a highly distinctive genotype/phenotype correlation define the mevalonate pathway as essential for muscle, hearing, and endocrine functions."]
Mutant enzymes retain 70–85% (bacterial) / ~50% (patient myoblast) activity
[PMID:32403198 "the other mutants (F257C, Y259C, R261G, and R261H) consistently showed a reduced rate of activity of approximately 70 to 85% of wild‐type"].
The domain "faces outward, where it could potentially interact with as yet to be defined
binding partners involved in the localization or shuttling of the enzyme."

## Interactions (IPI, IntAct)

UniProt INTERACTION block lists: ATOX1 (O00244), self GGPS1 (O95749, NbExp=7), SDCBP
(O00560). These derive from high-throughput binary interactome screens:
- PMID:25416956 (Rolland et al., Cell 2014, HI-II-14): protein binding (with ATOX1 O00244) + identical protein binding (self)
- PMID:32296183 (Luck et al., Nature 2020, HuRI): protein binding (with SDCBP O00560) + identical protein binding (self)
- PMID:31515488 (Fragoza et al., Nat Commun 2019): identical protein binding (self)
Individual GGPS1 mentions are not in the article body text (data are in supplementary
interactome tables); these are systematic Y2H/binary screens. Self-interaction is
biologically consistent with the obligate homohexamer. The heterotypic hits (ATOX1, SDCBP)
are HT binary screen results with no dedicated follow-up establishing a specific cellular
function; treat "protein binding" as non-informative (over-annotation for core function).

## Annotation summary (decisions)

- Catalytic MF GO:0004311 (GGPP synthase activity): ACCEPT for IDA (10026212, 9741684) and
  IMP (32403198). The redundant IBA and IEA(EC/RHEA) copies of the same correct core MF →
  ACCEPT (own correct core function, not over-annotation).
- EC-derived partial-reaction MFs GO:0004161 (DMAPP-transtransferase, EC 2.5.1.1) and
  GO:0004337 ((2E,6E)-FPP synthase, EC 2.5.1.10): these are the DMAPP→GPP and GPP→FPP
  chain-elongation steps the same active site performs en route to GGPP. Documented in
  UniProt catalytic-activity block. KEEP_AS_NON_CORE (real activities but the physiological
  product/role is GGPP, not GPP/FPP release).
- GO:0004659 prenyltransferase activity (IEA, InterPro): correct parent of the enzyme's
  activity but less informative than GO:0004311 → MARK_AS_OVER_ANNOTATED (general parent).
- BP GO:0033386 (GGPP biosynthetic process): ACCEPT (core). GO:0008299 isoprenoid
  biosynthetic process (IBA + IEA) and GO:0006720 isoprenoid metabolic process (IDA + IEA):
  correct but general parents → KEEP_AS_NON_CORE.
- UniPathway BP GO:0033384 (GPP biosynthetic process) and GO:0045337 (FPP biosynthetic
  process): the intermediate steps; KEEP_AS_NON_CORE (real but not the defining product).
- CC GO:0005829 cytosol (IDA + 3× Reactome TAS): ACCEPT. GO:0005737 cytoplasm (IEA + IMP):
  ACCEPT (correct, more general). GO:0048471 perinuclear region (IEA + IMP) and GO:0030018
  Z disc (IEA + IMP): supported by PubMed:32403198 IHC; KEEP_AS_NON_CORE (tissue/context
  specific, not the bulk cytosolic pool).
- Protein binding GO:0005515 (IPI, 2×): MARK_AS_OVER_ANNOTATED (bare, uninformative;
  HT binary screens; never REMOVE per policy).
- Identical protein binding GO:0042802 (IPI, 3×): ACCEPT/KEEP_AS_NON_CORE — self-interaction
  reflects the real homohexamer, but it is a structural property, not the core catalytic
  function → KEEP_AS_NON_CORE.

## Cross-refs
- Reactome: R-HSA-9717830 (GGPS1 hexamer transfers IPPP to GPP), R-HSA-9717834 (…to DMAPP),
  R-HSA-1655832 (expression of GGPS1). PDB: 2Q80, 6R4V, 9CSL, etc.
- Drug target: nitrogen-containing bisphosphonates (zoledronate etc.) and DGBP inhibit
  GGPPS (DrugBank entries in UniProt).
