# BBIP1 (BBIP10 / BBS18; UniProt A8MTZ0) — curation notes

## Identity
- Human gene, HGNC:28093, gene symbol BBIP1. Synonyms: BBIP10, BBS18, NCRNA00081.
- 92 aa, ~10.5 kDa; smallest of the eight BBSome core subunits. Was historically misannotated
  as a non-coding RNA ("non-protein coding RNA 81") before being recognized as a protein
  [UniProt A8MTZ0 CAUTION: "Was previously thought to be non-coding and described as 'non-protein coding RNA 81'"].
- Member of the BBIP10 family (Pfam PF14777, InterPro IPR028233). Present exclusively in ciliated organisms.
- N-terminal region 1–22 is disordered/polar; 4 splice isoforms annotated.

## Core biology — key primary paper
PMID:19081074 (Loktev et al., Dev Cell 2008; abstract-only in cache, full_text_available: false;
corresponds to UniProt "Ref.4" Loktev et al. supplying FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/HDAC6 interaction):
- Discovered BBIP10 as the eighth BBSome subunit. "We have now discovered a BBSome subunit that
  we named BBIP10. Similar to other BBSome subunits, BBIP10 localizes to the primary cilium,
  BBIP10 is present exclusively in ciliated organisms"
  [PMID:19081074 "BBIP10 localizes to the primary cilium, BBIP10 is present exclusively in ciliated organisms"].
- Depletion produces canonical BBS phenotypes in zebrafish
  [PMID:19081074 "depletion of BBIP10 yields characteristic BBS phenotypes in zebrafish"].
- A unique (non-BBSome-shared) function: required for cytoplasmic microtubule polymerization and
  acetylation [PMID:19081074 "BBIP10 is required for cytoplasmic microtubule polymerization and
  acetylation, two functions not shared with any other BBSome subunits"].
- Mechanism links to the tubulin deacetylase HDAC6: "inhibition of the tubulin deacetylase HDAC6
  restores microtubule acetylation in BBIP10-depleted cells, and BBIP10 physically interacts with HDAC6"
  [PMID:19081074]. HDAC6 = UniProt Q9UBN7 (the WITH/FROM in the GOA IPI row).
- Model: "BBSome-bound BBIP10 may therefore function to couple acetylation of axonemal microtubules
  and ciliary membrane growth" [PMID:19081074].

UniProt FUNCTION (from Ref.4): "Required for primary cilia assembly and BBSome stability. Regulates
cytoplasmic microtubule stability and acetylation." SUBUNIT: "Part of BBSome complex, that contains
BBS1, BBS2, BBS4, BBS5, BBS7, BBS8, BBS9 and BBIP10. Interacts with HDAC6." SUBCELLULAR LOCATION:
"Cell projection, cilium. Cytoplasm. Note=Localizes inside the primary cilium but not at centriolar satellites."

## BBSome architecture / assembly
PMID:22500027 (Zhang et al., JBC 2012; full text available):
- BBIP10 is "an integral BBSome protein that binds to the complex through BBS4"
  [PMID:22500027 "BBIP10, an integral BBSome protein that binds to the complex through BBS4"].
- PCM1 can interact with BBIP10 only when BBS4 is present [PMID:22500027].
- Establishes ordered BBSome assembly (core BBS7-BBS2-BBS9; then BBS1, BBS5, BBS8, BBS4).
- The GOA IPI row from this paper uses WITH/FROM UniProtKB:Q96RK4 (= BBS4), consistent with the
  BBIP10–BBS4 binding shown here. Supports a BBSome part_of / structural-binding annotation.

## Interaction mapping (high-throughput)
PMID:29039417 (Woodsmith et al., Nat Methods 2017; abstract-only):
- Yeast two-hybrid "off-switch" perturbation profiling across "eight subunits of the BBSome"; defined
  >1,000 interaction-disrupting mutations [PMID:29039417]. BBIP1 included as one of the eight subunits.
- GOA IPI row also uses WITH/FROM Q96RK4 (BBS4). Supports BBIP1 participating in BBSome via PPIs;
  generic "protein binding" (GO:0005515) is uninformative.

## Disease
PMID:24026985 (Scheidecker et al., J Med Genet 2014; not cached, cited in UniProt Ref.5):
- A null mutation in BBIP1 causes Bardet-Biedl syndrome 18 (BBS18) [MIM:615995]. Confirms BBIP1 as a
  bona fide BBSome subunit whose loss causes BBS (severe retinopathy, obesity, polydactyly, renal,
  intellectual disability).

## Structure
- Cryo-EM structure of the human BBSome includes BBIP1 (PDB 6XT9, chain J, residues 1-92; EMD-10617).
- ComplexPortal CPX-1908 = BBSome complex.

## Localization summary (for CC annotation review)
- BBSome (GO:0034464): strongly supported, multiple lines (IDA PMID:19081074, IPI, IBA, IEA). Core CC.
- Cilium / ciliary membrane (GO:0005929 / GO:0060170): BBIP10 localizes inside primary cilium; ciliary
  membrane is where the BBSome acts as a coat. Supported.
- Cytoplasm (GO:0005737): UniProt SUBCELLULAR LOCATION lists Cytoplasm; consistent with cytoplasmic
  microtubule role. Supported.
- Ciliary basal body (GO:0036064): IDA from HPA. The BBSome traffics via the basal body; plausible.
- Cytosol (GO:0005829): HPA IDA + multiple Reactome TAS. Generic; BBSome subunits cycle through
  cytosol before ciliary entry. Acceptable but less specific than BBSome / ciliary CCs.

## Process annotations
- cilium assembly (GO:0060271): supported by IMP (zebrafish/cell depletion phenotypes), NAS, IEA. Core BP.
- receptor localization to non-motile cilium (GO:0097500): IBA from GO_Central, based on the well-
  established BBSome role in trafficking signaling receptors (e.g. GPCRs like SSTR3, MCHR1) into/out
  of the primary cilium. Def: "A process in which a receptor is transported to, or maintained in, a
  location within a non-motile cilium." Strongly fits BBSome core function. Core BP.

## Notable functions NOT yet well captured by GO annotations
- Microtubule stabilization / cytoplasmic microtubule acetylation coupled via HDAC6 (PMID:19081074).
  This BBIP1-specific (non-BBSome-shared) activity is a candidate for additional BP/MF terms
  (e.g. regulation of microtubule polymerization/stability; negative regulation of tubulin deacetylation
  via HDAC6 binding). HDAC6 binding itself is more informative than generic protein binding.
- BBSome structural stability ("Required for ... BBSome stability") — supports a structural/scaffold role.
