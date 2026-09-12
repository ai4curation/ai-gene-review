# BBS9 (PTHB1; UniProt Q3SYG4) review notes

## Identity / overview
- Human gene BBS9 (HGNC:30000), aka PTHB1 (Parathyroid hormone-responsive B1 gene). 887 aa, MANE isoform Q3SYG4-1. Chromosome 7. [UniProt Q3SYG4]
- Causes autosomal-recessive Bardet–Biedl syndrome type 9 (BBS9; MIM:615986). The recurrent pathogenic missense G141R severely destabilizes the protein [UniProt; PMID:16380913; PMID:26085087].

## Core function: BBSome subunit / scaffold
- BBS9 is one of the seven/eight core BBSome subunits (BBS1, BBS2, BBS4, BBS5, BBS7, BBS8/TTC8, BBS9, BBIP10/BBIP1). The BBSome is a coat-like adaptor that sorts/traffics specific membrane (signaling-receptor) proteins to and within the primary cilium. [PMID:17574030 "we identify a complex composed of seven highly conserved BBS proteins. This complex, the BBSome, localizes to nonmembranous centriolar satellites in the cytoplasm but also to the membrane of the cilium ... the BBSome is required for ciliogenesis but is dispensable for centriolar satellite function"]
- BBSome assembly is chaperonin-assisted: BBS6/BBS10/BBS12 + CCT/TRiC mediate BBSome assembly; in Mkks(BBS6)-null mice BBS2/BBS7/BBS9 are unstable and degraded, leading to failure of BBSome assembly. [PMID:20080638; PMID:23943788 "in Mkks−/− mice, several BBSome components (e.g. Bbs2, Bbs7 and Bbs9) are unstable and degraded, leading to failure of BBSome assembly"]
- Structural basis: BBS9 N-terminal residues 1–407 form a seven-bladed β-propeller (PDB 4YD8, 1.80 Å). BBS9 also has GAE (gamma-adaptin ear), platform/pf, hairpin (hp) and C-terminal α-helical (CtH) domains. With BBS2 and BBS7 it forms the structural core/scaffold of the BBSome (cryo-EM 6XT9, full-length BBS9 modelled). [UniProt REGION 1..407 "Seven-bladed beta-propeller"; PMID:26085087 (structural characterization of BBS9; G141R abolishes stability; Ser142/Tyr186 mutagenesis)]
- Residue 141 is "critical for protein stability"; the BBS9 G141R disease variant causes severe loss of protein stability / aberrant folding. [UniProt SITE 141; PMID:26085087]

## Localization
- BBSome / BBS9 localizes both to nonmembranous centriolar satellites in the cytoplasm and to the ciliary membrane. [PMID:17574030]
- ComplexPortal/IDA places the BBSome at the ciliary membrane (GO:0060170). [PMID:19081074, ComplexPortal CPX-1908]
- IDA localizations (HPA / GO_Central immunofluorescence and PMID:23943788): cilium (GO:0005929), ciliary transition zone (GO:0035869), ciliary tip (GO:0097542), centriolar satellite (GO:0034451), cytosol (GO:0005829). [GO_REF:0000052; PMID:23943788]
- Pericentriolar material (GO:0000242) and cilium IDA from mouse Bbs imaging (MGI). [PMID:22139371]
- UniProt subcellular location: cytoplasm; cytoskeleton/MTOC/centrosome; centriolar satellite; cilium membrane.

## BBSome trafficking regulation / interactions
- BBS9 (and the BBSome) interacts with LZTFL1/BBS17; the BBS9 region 685–765 mediates LZTL1 interaction; LZTFL1 regulates BBSome ciliary trafficking and Smoothened/Hedgehog. [UniProt REGION 685..765; PMID:22072986]
- ARL6/BBS3 (small GTPase, not a BBSome subunit) physically interacts with the BBSome; both depend on each other for ciliary localization. BBSome forms normally without Bbs3, but Bbs3 loss mislocalizes ciliary GPCR cargo (MCHR1) and affects retrograde transport. [PMID:22139371]
- AZI1/CEP131 (centriolar satellite protein) interacts with BBS4 and regulates BBSome ciliary trafficking. [PMID:24550735]
- NPHP5(IQCB1)/CEP290 regulate BBSome integrity, ciliary trafficking and cargo delivery. [PMID:25552655]
- Rab8/RAB3IP(Rabin8): BBSome binds Rabin8 (GEF for Rab8), promoting ciliary membrane biogenesis. [PMID:17574030; Reactome R-HSA-5617815]

## Curation considerations
- 13 GO:0005515 "protein binding" IPI annotations are uninformative per guidelines; they record specific BBSome subunit / regulator interactions (BBS1, BBS2, BBS4, BBS5, BBS7/TTC8, BBS10, BBS12, LZTFL1, IQCB1, AZI1/CEP131). The informative content is captured by the BBSome part_of (GO:0034464) annotations. Mark protein binding as over-annotated/non-core (keep but not core MF).
- The only true MF annotation is ND (GO:0003674). BBS9 has no catalytic activity; it is a structural/scaffolding subunit. A "structural molecule activity" (GO:0005198) MF could be proposed but is not in existing annotations; the BBSome subunit identity (CC) plus protein localization to cilium (BP) capture the function.
- fat cell differentiation (GO:0045444) is ISS/IEA from mouse ortholog; plausible BBS-related (obesity) downstream phenotype but indirect / non-core for a structural ciliary subunit -> KEEP_AS_NON_CORE.
- cytoplasm (GO:0005737, IEA SubCell) and membrane (GO:0016020) are general/parent terms superseded by more specific IDA terms (centriolar satellite, ciliary membrane). Mark membrane (parent of ciliary membrane) as over-annotated; cytoplasm is acceptable but general.
- GO:0061512 protein localization to cilium (IMP, PMID:23943788) and GO:0060271 cilium assembly capture the BP. protein localization to cilium is the more precise/mechanistic core BP (BBSome traffics cargo INTO cilium); cilium assembly is the broader downstream phenotype.

## Core function summary
1. Structural scaffold subunit of the BBSome (β-propeller + GAE/platform/α-helical core, with BBS2/BBS7). [PMID:17574030; PMID:26085087]
2. BBSome-mediated trafficking of membrane/signaling cargo to and within the primary cilium = protein localization to cilium. [PMID:17574030; PMID:23943788]
3. Required for ciliogenesis/cilium assembly (downstream). [PMID:17574030]
