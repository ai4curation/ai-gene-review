# ACOX1 (Q15067) — gene review notes

## Identity and core biochemistry

ACOX1 is the human peroxisomal **straight-chain acyl-CoA oxidase 1** (also called
palmitoyl-CoA oxidase / SCOX / AOX), UniProt Q15067, HGNC:119, gene ID 51, on
chromosome 17. It is the **first and rate-limiting enzyme of peroxisomal fatty-acid
β-oxidation**, initiating degradation of very-long-chain fatty acids (VLCFAs).

- UniProt FUNCTION: "Involved in the initial and rate-limiting step of peroxisomal
  beta-oxidation of straight-chain saturated and unsaturated very-long-chain fatty
  acids (VLCFAs)" [file:human/ACOX1/ACOX1-uniprot.txt].
- Mechanism: it is an FAD-dependent oxidase that "Catalyzes the desaturation of fatty
  acyl-CoAs that have a saturated bond between C2 and C3 (2,3-saturated acyl-CoA) to
  2-trans-enoyl-CoAs ((2E)-enoyl-CoAs), and donates electrons directly to molecular
  oxygen (O(2)), thereby producing hydrogen peroxide (H(2)O(2))"
  [file:human/ACOX1/ACOX1-uniprot.txt]. This is the key distinction from the
  mitochondrial acyl-CoA dehydrogenases, which pass electrons to ETF rather than O2.
- Reaction (EC 1.3.3.6, Rhea:RHEA:38959): "a 2,3-saturated acyl-CoA + O2 = a
  (2E)-enoyl-CoA + H2O2" [file:human/ACOX1/ACOX1-uniprot.txt].
- Cofactor: FAD (Name=FAD; Xref=ChEBI:CHEBI:57692) [file:human/ACOX1/ACOX1-uniprot.txt].
  Active site proton acceptor at residue 421; FAD binding at 139 and 178.
- Pathway: "Lipid metabolism; peroxisomal fatty acid beta-oxidation."
  [file:human/ACOX1/ACOX1-uniprot.txt].

The original biochemical characterization confirms straight-chain / eicosanoid substrate
specificity and direct O2 electron transfer: "The palmitoyl-CoA oxidase (ACOX) oxidizes
the CoA esters of straight chain fatty acids and prostaglandins and donates electrons
directly to molecular oxygen, thereby producing H2O2" [PMID:7876265]. The maximal
activities for saturated fatty acids were observed with C12-18 substrates; Km for
palmitoyl-CoA ≈ 10 µM [PMID:7876265].

Human liver actually contains two peroxisomal acyl-CoA oxidases with different substrate
specificities: (i) palmitoyl-CoA oxidase = ACOX1, "oxidizing very long straight-chain
fatty acids and eicosanoids", and (ii) a branched-chain acyl-CoA oxidase (ACOX2)
[PMID:8943006]. This is important for interpreting GOA annotations sourced from
PMID:8943006, which is primarily about the branched-chain oxidase (ACOX2) but confirms
the two-oxidase division of labour.

## Isoforms

Three alternative-splicing isoforms. Isoforms 1 (ACOX1a, exon 3I) and 2 (ACOX1b,
exon 3II) differ in substrate profile: "[Isoform 1]: Shows highest activity against
medium-chain fatty acyl-CoAs" (optimum decanoyl-CoA, C10) vs "[Isoform 2]: Is active
against a much broader range of substrates and shows activity towards long-chain and
very-long-chain fatty acyl-CoAs" [file:human/ACOX1/ACOX1-uniprot.txt]. Both can reverse
the Acox1-null mouse phenotype, isoform 2 more effectively [file:human/ACOX1/ACOX1-uniprot.txt].
The chain-length-specific MF GO terms in GOA (medium/long/very-long-chain fatty acyl-CoA
oxidase activity) reflect this isoform substrate spread and the large Rhea reaction set
in the UniProt record.

## Structure / subunit

Homodimeric FAD-flavoprotein. "The crystal structure of ACOX1 revealed that this enzyme
acts as a homodimer bound to Flavin adenine dinucleotide (FAD)" [PMID:32169171]. UniProt
SUBUNIT: "Homodimer (PubMed:32169171). Interacts with LONP2 (PubMed:18281296)"
[file:human/ACOX1/ACOX1-uniprot.txt]. The 660-aa precursor (component A) is proteolytically
processed into a 51-kDa B chain and 21-kDa C chain; the B+C heterodimer is enzymatically
active [PMID:7876265]. C-terminal SKL is the PTS1 peroxisomal targeting signal
[PMID:8117268; file:human/ACOX1/ACOX1-uniprot.txt MOTIF 658..660].

## Localization

Peroxisome / peroxisomal matrix. UniProt SUBCELLULAR LOCATION: "Peroxisome
{ECO:0000269|PubMed:32169171}" [file:human/ACOX1/ACOX1-uniprot.txt]. In the Bellen paper,
"both hACOX1WT and hACOX1N237S are localized to peroxisomes" (co-expressed eYFP-PTS1
marker) [PMID:32169171]. Import is PTS1/PEX5-dependent (Reactome R-HSA-9033235/9033236
capture the transient cytosolic → matrix translocation step). The single Reactome-sourced
`cytosol` annotation reflects the pre-import state of the newly synthesized protein, not
the site of catalysis.

## Disease

- **Peroxisomal acyl-CoA oxidase deficiency / pseudo-neonatal adrenoleukodystrophy
  (Pseudo-NALD, MIM:264470)**: autosomal-recessive single-enzyme peroxisomal disorder.
  "characterized by increased plasma levels of very-long chain fatty acids, due to
  decreased or absent peroxisome acyl-CoA oxidase activity. Peroxisomes are intact and
  functioning." [file:human/ACOX1/ACOX1-uniprot.txt]. Two new cases with abnormal plasma
  VLCFA and biallelic ACOX1 mutations (homozygous deletion; compound het p.G231V + exon-13
  skipping) [PMID:18536048].
- **Mitchell syndrome (MITCH, MIM:618960)**: a distinct disorder caused by a recurrent
  *de novo* gain-of-function variant (p.N237S) causing episodic demyelination, sensorimotor
  polyneuropathy and hearing loss. The mutant is a stabilized, more-abundant toxic homodimer:
  "the mutant homodimer is clearly much more abundant than the wild type homodimer or the
  heterodimers" and "monomeric ACOX1N237S appears to be resistant to protein turnover, and
  preferentially exists as a mutant homodimer that is a toxic" [PMID:32169171]. Elevated
  peroxisomal H2O2 drives the axonal toxicity; "H2O2 is reduced by peroxisomal catalase, an
  abundant peroxisomal enzyme responsible for the conversion of H2O2 into O2", and catalase
  over-expression rescues the phenotype [PMID:32169171].

## Annotation-review reasoning highlights

- **Core MF**: acyl-CoA oxidase activity (GO:0003997), supported by multiple experimental
  IDA/IMP (PMID:8117268, PMID:7876265, PMID:18536048, PMID:32169171). Chain-length-resolved
  children (GO:0120524 long-chain, GO:0044535 very-long-chain, GO:0120523 medium-chain
  fatty acyl-CoA oxidase activity) are Rhea/IBA refinements consistent with the isoform
  substrate data; kept.
- **Core cofactor MF**: FAD binding (GO:0071949 / GO:0050660) — kept; drug/structure/UniProt
  evidence for FAD.
- **Core BP**: peroxisomal fatty-acid β-oxidation and VLCFA catabolism
  (GO:0006635, GO:0033540, GO:0140493, GO:0000038, GO:0009062, GO:0019395) and the coupled
  H2O2 biosynthetic process (GO:0050665) — kept.
- **`fatty acid binding` (GO:0005504)** IBA + InterPro IEA: over-annotation. ACOX1 acts on
  fatty **acyl-CoA thioesters**, not free fatty acids; there is no evidence it is a
  fatty-acid-binding transport/carrier protein. MARK_AS_OVER_ANNOTATED.
- **`oxidoreductase activity` (GO:0016491) and `oxidoreductase activity, acting on the CH-CH
  group of donors` (GO:0016627)** IEA: correct but uninformative ancestors of the specific
  acyl-CoA oxidase activity. MARK_AS_OVER_ANNOTATED.
- **`generation of precursor metabolites and energy` (GO:0006091)** IMP (PMID:7876265):
  misleading for peroxisomal β-oxidation, which is degradative/chain-shortening and
  H2O2-generating rather than an ATP/energy-yielding pathway (UniProt CAUTION notes products
  are routed to ER/mitochondria). MARK_AS_OVER_ANNOTATED.
- **`lipid metabolic process` (GO:0006629)** IDA (PMID:8117268): correct but too general;
  MODIFY to fatty acid beta-oxidation (GO:0006635).
- **`prostaglandin metabolic process` (GO:0006693)** IMP (PMID:7876265): ACOX1 oxidizes
  prostaglandin CoA esters, but this is a minor/non-core activity → KEEP_AS_NON_CORE.
- **`cytosol` (GO:0005829)** TAS Reactome: reflects the pre-import (PTS1 translocation)
  state, not the catalytic compartment → KEEP_AS_NON_CORE.
- **`membrane` (GO:0016020)** HDA (PMID:19946888, NK-cell membrane proteome): non-specific
  high-throughput hit; ACOX1 is a soluble matrix enzyme → MARK_AS_OVER_ANNOTATED.
- **`PDZ domain binding` (GO:0030165)** IDA (PMID:23209302): that paper is about the
  Radil/KIF14 PDZ interaction and does not (in the cached text) establish an ACOX1 PDZ
  interaction; ACOX1's C-terminus is the PTS1 tripeptide SKL, an atypical PDZ ligand match.
  I cannot verify ACOX1 involvement from the available text → UNDECIDED (do not remove an
  experimental annotation).
- **`protein binding` (GO:0005515)** IPI (LONP2, PMID:18281296): bare protein binding, keep
  the interaction record but MARK_AS_OVER_ANNOTATED per policy (uninformative MF).
- **`protein homodimerization activity` (GO:0042803)** IDA + IEA: ACCEPT — the physiological
  quaternary structure is a homodimer (crystal structure; co-IP) [PMID:32169171].
