# GOT2 (human) — gene review notes

UniProt: P00505 (AATM_HUMAN). HGNC:4433. Also KYAT4.

## Identity and core biochemistry

GOT2 encodes the **mitochondrial aspartate aminotransferase** (mAspAT / mAST / GOT), a
homodimeric, pyridoxal-5'-phosphate (PLP)-dependent class-I aminotransferase. The mature
protein (residues 30–430) follows cleavage of a 29-residue mitochondrial transit peptide.

- RecName / EC: "Aspartate aminotransferase, mitochondrial; Short=mAspAT; EC=2.6.1.1"
  [file:human/GOT2/GOT2-uniprot.txt "EC=2.6.1.1 {ECO:0000269|PubMed:26902786, ECO:0000269|PubMed:31422819}"].
- Core reaction: "Reaction=L-aspartate + 2-oxoglutarate = oxaloacetate + L-glutamate"
  [file:human/GOT2/GOT2-uniprot.txt "Reaction=L-aspartate + 2-oxoglutarate = oxaloacetate + L-glutamate"].
- Cofactor: "Name=pyridoxal 5'-phosphate" [file:human/GOT2/GOT2-uniprot.txt].
  UniProt MOD_RES 279 = "N6-(pyridoxal phosphate)lysine" (the catalytic Schiff-base lysine).
- Homodimer [file:human/GOT2/GOT2-uniprot.txt "SUBUNIT: Homodimer"].
- Localization: "Mitochondrion matrix" and "Cell membrane" [file:human/GOT2/GOT2-uniprot.txt].
- Structures solved: PDB 5AX8 (2.99 Å), 8SKR (EM), 9YB6 (1.50 Å).

## Function (UniProt FUNCTION)

"Catalyzes the irreversible transamination of the L-tryptophan metabolite L-kynurenine to
form kynurenic acid (KA). As a member of the malate-aspartate shuttle, it has a key role in
the intracellular NAD(H) redox balance. Is important for metabolite exchange between
mitochondria and cytosol, and for amino acid metabolism. Facilitates cellular uptake of
long-chain free fatty acids."
[file:human/GOT2/GOT2-uniprot.txt, ECO:0000269|PubMed:31422819, ECO:0000269|PubMed:9537447]

So GOT2 has one core catalytic function plus THREE genuine additional roles:
1. **Core**: L-aspartate:2-oxoglutarate transaminase (EC 2.6.1.1) — malate-aspartate shuttle.
2. **Kynurenine aminotransferase (KAT4 / EC 2.6.1.7)**: L-kynurenine + 2-oxoglutarate ->
   kynurenate. Second CATALYTIC ACTIVITY block, ECO:0000250 (by similarity to P00507 pig).
   Genuine secondary activity — GOT2 is one of the four human KATs. KEEP_AS_NON_CORE.
3. **FABPpm / plasma-membrane fatty-acid-binding protein** (AltName "Plasma membrane-
   associated fatty acid-binding protein; Short=FABPpm"): moonlighting role in long-chain
   free-fatty-acid uptake at the plasma membrane. Established by Zhou et al. (see below).
   Genuine moonlighting function — KEEP_AS_NON_CORE (not over-annotation to remove).

## Moonlighting: FABPpm and ethanol (PMID:9537447, Zhou et al. 1998, Hepatology)

Abstract-only cached (full_text_available: false). HepG2 hepatoma cells cultured in ethanol.
- "Acute (24 hour) exposure to 0, 20, 40, or 80 mmol/L ethanol produced a dose-dependent
  (r = .98) increase in mAspAT messenger RNA (mRNA)".
- "Plasma membrane mAspAT content also correlated with mAspAT mRNA (r = .96)".
- "In cells cultured chronically at 0 to 80 mmol/L ethanol, fatty acid uptake Vmax increased
  in parallel with plasma membrane expression of mAspAT (r = .98)".
- "increased mAspAT-mediated fatty acid uptake may contribute to alcoholic fatty liver".
This is the primary experimental support for: plasma membrane localization (IDA GO:0005886),
fatty acid transport (IEP GO:0015908), response to ethanol (IDA GO:0045471), and the FABPpm
moonlighting role. Note: mitochondrial content was unchanged; ethanol drives PM translocation.

## Kynurenine aminotransferase (KAT4)

Second catalytic activity in UniProt:
"Reaction=L-kynurenine + 2-oxoglutarate = kynurenate + L-glutamate + H2O ... EC=2.6.1.7;
Evidence={ECO:0000250|UniProtKB:P00507}"
[file:human/GOT2/GOT2-uniprot.txt]. AltNames "Kynurenine aminotransferase 4 / IV",
"Kynurenine--oxoglutarate transaminase 4 / IV". GOA has GO:0016212 (L-kynurenine:2-oxoglutarate
transaminase activity) IEA from EC 2.6.1.7. Genuine but non-core (by-similarity in human).

## Disease and physiological role (PMID:31422819, van Karnebeek et al. 2019, AJHG)

Abstract-only cached. Bi-allelic GOT2 mutations cause DEE82 (developmental & epileptic
encephalopathy 82; MIM:618721), a "treatable malate-aspartate shuttle-related encephalopathy".
- "GOT2 encodes the mitochondrial glutamate oxaloacetate transaminase."
- "GOT2, a member of the malate-aspartate shuttle, plays an essential role in the intracellular
  NAD(H) redox balance."
- "GOT2 enzyme activity was deficient in fibroblasts with bi-allelic mutations."
- "De novo serine biosynthesis was impaired in fibroblasts with GOT2 mutations and
  GOT2-knockout HEK293 cells."
Provides EXP evidence (in GOA) for GO:0004069 catalytic activity of the human enzyme.
DEE82 variants: p.Leu209del, p.Arg262Gly (decreased GOT activity), p.Arg337Gly, p.Gly366Val
(decreased GOT activity) [file:human/GOT2/GOT2-uniprot.txt VARIANT records].

## Malate-aspartate shuttle (PMID:37647199, Broeks et al. 2023, Cell Rep)

Abstract-only cached. "The malate-aspartate shuttle is important for de novo serine
biosynthesis." "We genetically disrupted each MAS component to generate a panel of
MAS-deficient HEK293 cell lines". GOT2 is the mitochondrial transaminase arm of the MAS.
GOA IMP GO:0043490 malate-aspartate shuttle assigned by FlyBase from this paper. Abstract
foregrounds MDH1/OGC/MDH2 but MAS-component panel includes GOT2; annotation biologically sound.

## Crystal structure / catalytic activity (PMID:26902786, Jiang et al. 2016)

Abstract-only. "Mitochondrial aspartate aminotransferase (mAspAT) was recognized as a
moonlighting enzyme because it has not only aminotransferase activity but also a high-affinity
long-chain fatty acids (LCFA) binding site." "This enzyme plays a key role in amino acid
metabolism, biosynthesis of kynurenic acid and transport of the LCFA." "Optimal activity of the
enzyme occurred at a temperature of 47.5ºC and a pH of 8.5." Recombinant human mAspAT expressed,
purified, crystallized (2.99 Å, PDB 5AX8). Provides EXP support for GO:0004069 (in GOA).

## Catalytic-activity clinical assays (abstract-only)

- PMID:2182221 (Watazu et al. 1990): automated serum mAST assay using protease-401 to
  inactivate cytosolic AST. "Total mitochondrial aspartate aminotransferase (EC 2.6.1.1) ...
  in human serum". IDA GO:0004069.
- PMID:2567216 (Schiele et al. 1989): immunochemical measurement of serum mAST activity.
  "we measured the activity of the mitochondrial isoenzyme (mAST) of aspartate amino-transferase
  (EC 2.6.1.1, AST)". IDA GO:0004069 and GO:0006533. Note the abstract's conclusion is a
  negative clinical finding (mAST not useful as an alcohol marker) but it does directly assay
  mitochondrial AST activity.
- PMID:2731362 (Panteghini et al. 1989): serum AST isoenzyme kinetics after coronary
  reperfusion; measures "mitochondrial AST (m-AST)" activity. IDA GO:0004069.

## Hydroxyproline catabolism (PMID:21998747, Riedel et al. 2011)

Full text available. This paper is primarily about HOGA1 (4-hydroxy-2-oxoglutarate aldolase),
the terminal enzyme of 4-hydroxyproline degradation. It establishes that the pathway involves
four mitochondrial enzymes including "aspartate aminotransferase (AspAT)" which performs "the
conversion of 4-hydroxy-glutamate to 4-hydroxy-2-oxogluarate (HOG)". This is the basis for the
BHF-UCL TAS annotation GO:0019470 (trans-4-hydroxy-L-proline catabolic process). Reactome
R-HSA-6784393 ("PXLP-K279-GOT2 dimer transaminates 4-OH-L-glutamate to HOG") captures the same
GOT2 step. Genuine metabolic-pathway participation but a minor, context-specific branch — keep
as non-core.

## Proteomics / localization (HDA/HTP, abstract-heavy)

- PMID:34800366 (Morgenstern et al. 2021): high-confidence human mitochondrial proteome; HTP
  GO:0005739 mitochondrion. Consistent with core matrix localization.
- PMID:20833797 (Zhao et al. 2011): mitochondrial phosphoproteome from human muscle; HDA
  GO:0005739 mitochondrion. Consistent.
- PMID:22681889 (Baltz et al. 2012): mRNA-bound proteome (RNA interactome capture); HDA
  GO:0003723 RNA binding. Incidental — abundant mitochondrial metabolic enzymes are common
  "moonlighting" RNA-binders in interactome-capture datasets; not a core function.
- PMID:23533145 (Principe et al. 2013) and PMID:20458337 (Buschow et al. 2010): exosome
  proteomics; HDA GO:0070062 extracellular exosome. Incidental for an abundant enzyme.

## Curation decisions summary

Core functions (author-supplied, strictly validated):
- MF GO:0004069 (L-aspartate:2-oxoglutarate transaminase activity) — core catalysis.
- MF GO:0030170 (pyridoxal phosphate binding) — obligatory cofactor.
Core BP: GO:0043490 malate-aspartate shuttle; aspartate/glutamate/2-oxoglutarate metabolism.
Core CC: GO:0005759 mitochondrial matrix.

Moonlighting / secondary (KEEP_AS_NON_CORE, genuine): FABPpm plasma-membrane localization,
fatty acid transport, response to ethanol, kynurenine (KAT4) transaminase activity,
4-hydroxyproline catabolic branch.

Over-annotations (MARK_AS_OVER_ANNOTATED): generic parents GO:0003824 catalytic activity,
GO:0008483 transaminase activity, GO:0006520 amino acid metabolic process; incidental
GO:0003723 RNA binding and GO:0070062 extracellular exosome.

No REMOVE actions taken (no clearly-wrong IEA identified; all electronic terms are biologically
apt at worst as generic parents).
