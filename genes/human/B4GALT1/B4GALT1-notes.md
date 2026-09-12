# B4GALT1 (human, UniProt P15291) — gene review notes

## Identity and overview

- HGNC: B4GALT1 (synonym GGTB2). UniProt P15291 (B4GT1_HUMAN), 398 aa.
- Beta-1,4-galactosyltransferase 1 (beta4Gal-T1 / B4GalT1). CAZy family GT7.
- Type II single-pass Golgi membrane glycosyltransferase: short N-terminal cytosolic
  tail, single transmembrane domain, stem region, C-terminal luminal catalytic domain.
- Multiple EC numbers reflect distinct acceptors of the SAME catalytic chemistry
  (transfer of Gal from UDP-Gal in beta-1,4 linkage): EC 2.4.1.38 (to GlcNAc on
  glycoproteins/N-glycans), EC 2.4.1.90 (to free GlcNAc -> LacNAc), EC 2.4.1.22
  (lactose synthase, to glucose, only with alpha-lactalbumin), EC 2.4.1.275 (to GlcNAc
  on glycolipids).

## Core molecular function (verified from primary literature)

- Transfers galactose from UDP-alpha-D-galactose in beta(1->4) linkage to non-reducing
  terminal GlcNAc of complex N-glycans and glycolipids, forming Galbeta1-4GlcNAc
  (type-2 N-acetyllactosamine, LacNAc). [UniProt P15291 FUNCTION; PMID:16157350 "beta-1,4-Galactosyltransferase-I (beta4Gal-T1) transfers galactose from UDP-galactose to N-acetylglucosamine (GlcNAc) residues of the branched N-linked oligosaccharide chains of glycoproteins"]
- Branch specificity: prefers the 1,2-1,6-arm GlcNAc of biantennary N-glycans
  (~10-fold lower Km than the 1,3-arm). [PMID:16157350 "the K(m) of 1,2-1,6-arm is approximately tenfold lower than for 1,2-1,3-arm and 1,4-1,3-arm"]
- Mn2+ is a required cofactor (crystallized with Mn2+ and GlcNAc/UDP). [UniProt CC COFACTOR; PMID:16157350]
- Catalytic/substrate-binding residues mapped by mutagenesis: Tyr284, Tyr309, Trp310
  critical for GlcNAc binding; Tyr309 also in UDP-Gal binding. [PMID:2120039 "Tyr284, Tyr309 and Trp310 are critically involved in the N-acetyglucosamine binding and Tyr309 is involved in UDP-galactose binding as well"]
- Galactosylates IgG Fc N-glycans (Asn297), a prerequisite for downstream sialylation;
  used widely as a glyco-engineering tool. [PMID:27872474; PMID:29133956; PMID:37632720; PMID:38321209 — all EXP/IDA for beta-1,4-GalT activity in GOA]

## Lactose synthase (bifunctional, mammary-specific)

- With LALBA/alpha-lactalbumin forms the lactose synthase complex (1:1). alpha-LA
  promotes glucose binding to beta4Gal-T1, switching acceptor specificity from GlcNAc
  to glucose so the complex makes lactose (Galbeta1-4Glc). [PMID:11419947 "The lactose synthase (LS) enzyme is a 1:1 complex of a catalytic component, beta1,4-galactosyltransferse (beta4Gal-T1) and a regulatory component, alpha-lactalbumin (LA)... LA promotes the binding of glucose (Glc) to beta4Gal-T1, thereby altering its sugar acceptor specificity from N-acetylglucosamine (GlcNAc) to glucose, which enables LS to synthesize lactose"]
- Conformational change (residues ~345-365, His347 metal coordination, hydrophobic
  N-acetyl pocket Arg359/Phe360/Ile363) underlies the acceptor switch. [PMID:11419947]
- This is a CORE, evolutionarily selected function in lactating mammary gland — not a
  pleiotropic side effect. Both LacNAc synthesis and lactose synthesis are core.

## Localization

- Resident enzyme of the trans-Golgi cisternae (codistributes with TPPase in trans
  Golgi). [PMID:6121819 "Label by gold particles was limited to two to three trans cisternae of the Golgi apparatus"]
- Golgi retention via the transmembrane domain; homodimerizes (Cys29/His32 dependent)
  and associates with alpha/beta-tubulin. [PMID:7744867 "beta-1,4-galactosyltransferase (GT) forms homodimers and large oligomers in vivo... large aggregates of GT are associated with alpha- and beta-tubulins"]
- HPA IDA + Ensembl/Reactome all place it in Golgi/Golgi membrane. CORE location = Golgi
  apparatus / Golgi membrane / Golgi trans cisterna.

## Cell-surface / secreted pools (context-specific, NON-CORE)

- A long isoform with a 13-aa N-terminal cytoplasmic extension (alternative initiation)
  is preferentially targeted to the plasma membrane; the short isoform is the Golgi
  form. [PMID:1714903 "the longer GalTase protein, containing this unique 13-amino acid peptide, is preferentially targeted to the plasma membrane, and the shorter GalTase protein resides primarily within the Golgi compartment"]
- Cell-surface GalT proposed as a cell-cell/cell-matrix recognition molecule and ZP3
  sperm receptor; this is the LONG isoform (P15291-1) and is a secondary/specialized
  role (UniProt FUNCTION [Isoform Long], By similarity to mouse P15535). Treat as
  non-core.
- ecto-GalT on enterocyte brush border / basolateral membrane / desmosome / external
  side of PM. [PMID:3917437 "Antigenic sites... were found at the plasma membrane of absorptive enterocytes with the most intense labeling appearing along the brush border membrane... a role in adhesion appears possible on the basolateral plasma membrane"] — surface pool, non-core; "desmosome" is incidental immuno-EM localization.
- Soluble/secreted GalT in milk, amniotic fluid, ascites (proteolytic shedding of the
  catalytic domain) retains activity. [PMID:33805 "UDP-galactose: N-acetylglucosamine galactosyltransferase was isolated from pooled human milk, pooled amniotic fluid and from two different individual samples of malignant ascites"] Explains extracellular-region/exosome CC annotations. The processed secreted form is catalytically active (UniProt) but the dominant physiological state is Golgi-resident — secreted/exosome locations are non-core.

## Disease

- Hypomorphic/LoF mutations cause CDG type IId (CDG2D), a congenital disorder of
  glycosylation. [UniProt: PMID:11901181, PMID:30653653, PMID:32157688 (CDG2D variants);
  not in GOA annotation set]
- Amish missense p.Asn352Ser reduces GalT activity ~50%, lowers LDL-C and fibrinogen,
  reduces coronary artery disease risk, via reduced galactosylation/sialylation of
  ApoB100, fibrinogen, IgG, transferrin. [PMID:34855475 "The mutant protein had 50% lower galactosyltransferase activity compared with the wild-type protein. N-linked glycan profiling of human serum found serine 352 allele to be associated with decreased galactosylation and sialylation of apolipoprotein B100, fibrinogen, immunoglobulin G, and transferrin"] This is the basis for the IMP "positive regulation of circulating fibrinogen levels" and "lipid metabolic process" annotations — these are downstream physiological/disease consequences of the core galactosyltransferase activity, NOT direct dedicated B4GALT1 processes. Treat as non-core / over-annotation.

## Annotation strategy summary

- CORE MF: beta-N-acetylglucosaminylglycopeptide beta-1,4-galactosyltransferase activity
  (GO:0003831); N-acetyllactosamine synthase activity (GO:0003945); lactose synthase
  activity (GO:0004461); manganese ion binding (GO:0030145).
- CORE BP: protein N-linked glycosylation (GO:0006487); lactose biosynthetic process
  (GO:0005989).
- CORE CC: Golgi membrane (GO:0000139) / Golgi apparatus (GO:0005794) / Golgi trans
  cisterna (GO:0000138).
- Generic MF terms (galactosyltransferase activity GO:0008378, glycosyltransferase
  activity GO:0016757, UDP-galactosyltransferase activity GO:0035250) -> MODIFY to the
  specific beta-1,4-GalT activity.
- Generic/parent processes (carbohydrate metabolic GO:0005975, oligosaccharide
  biosynthetic GO:0009312) -> MODIFY/over-annotated.
- protein-containing complex (GO:0032991) -> too generic; the real complex is lactose
  synthase. MODIFY toward a complex term or mark over-annotated; there is no
  lactose-synthase complex GO CC term -> propose one.
- Surface/secreted/exosome/granule/desmosome/filopodium CC -> KEEP_AS_NON_CORE or
  over-annotated (surface long-isoform pool + shed soluble form, not the core Golgi
  function).
- IMP fibrinogen/lipid BP -> downstream disease physiology, non-core.

## Falcon integration (dated 2026-06-21)

The provided report is `B4GALT1-deep-research-falcon.md` (an LLM deep-research synthesis
with non-resolvable internal citation keys, e.g. "wiertelak2025...", "chen2023..."; these
are NOT fetchable PMIDs, so per workflow they are used for orientation only and NOT cited
as supporting_text in the YAML).

Findings USED (concordant with primary literature / UniProt, and independently verified
here):
- Core MF = beta-1,4-GalT transferring Gal from UDP-Gal to terminal GlcNAc, forming
  type-2 LacNAc; Mn2+ cofactor; UDP-Gal donor. (Matches UniProt + PMID:16157350.)
- Core localization = trans-Golgi / Golgi membrane, type II topology. (Matches
  PMID:6121819, PMID:7744867.)
- Lactose synthase with LALBA is a well-supported, tissue-specific core function.
  (Matches PMID:11419947.)
- Downstream cancer migration/invasion, apoptosis, autophagy, inflammatory and
  TGF-beta/galectin-8 roles are pleiotropic, context-specific consequences of altered
  glycosylation, NOT core B4GALT1 processes, and should not be annotated as dedicated
  processes. (Concordant with the "do not over-annotate pleiotropic BP" guidance; none
  of these are in the GOA set anyway.)
- The report's framing that cytosol/nucleus localization is unsupported is correct.

Findings REJECTED or DOWNWEIGHTED (and why):
- All specific cancer/disease mechanistic claims (chen2023 integrin alpha6/beta1
  substrates in HCC; hsu2024 galectin-8/TGFBR2 in CRC; dai2026 inhibitor apoptosis;
  wang2020 glioblastoma apoptosis/autophagy; buduo2021 platelet TPO; tang2023 Alzheimer
  glycomics; xu2025 inhibitor Arg187/Glu313) rest on non-resolvable citation keys that I
  could not verify against fetchable PMIDs. They are plausible but unverifiable here, are
  not in the GOA annotation set, and do not change any annotation action. NOT used as
  evidence; recorded here only as context.
- The report repeatedly conflates B4GALT1 with family members (e.g. B4GALT3 in
  retinoblastoma) and uses "B4GALT family" effects; I did not transfer any family-level
  claim to B4GALT1.
- The active-site residue numbers quoted by Falcon (Arg187/Glu313) differ from the
  experimentally verified substrate-binding residues in PMID:2120039 (Tyr284/Tyr309/
  Trp310) and PMID:11419947 (His347, Arg359/Phe360/Ile363); I used only the primary,
  verified residues and ignored the Falcon residue numbers.
</content>
</invoke>
