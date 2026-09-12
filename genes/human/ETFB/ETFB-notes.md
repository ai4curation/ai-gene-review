# ETFB (P38117) review notes

## Identity / core biology
ETFB is the **beta subunit of the electron-transfer flavoprotein (ETF)**, a soluble
mitochondrial-matrix FAD-containing heterodimer (ETFA + ETFB). ETF is the common
electron acceptor for the matrix FAD-dependent acyl-CoA dehydrogenases (fatty-acid
beta-oxidation and amino-acid catabolism), relaying electrons to ETF-ubiquinone
oxidoreductase (ETFDH) and thence to the respiratory-chain ubiquinone pool.

Supporting text:
- [file:UniProt P38117 FUNCTION "Heterodimeric electron transfer flavoprotein that accepts electrons from several mitochondrial dehydrogenases, including acyl-CoA dehydrogenases, glutaryl-CoA and sarcosine dehydrogenase"]
- [file:UniProt P38117 FUNCTION "It transfers the electrons to the main mitochondrial respiratory chain via ETF-ubiquinone oxidoreductase"]
- [PMID:8962055 abstract "They function as electron shuttles between primary flavoprotein dehydrogenases involved in mitochondrial fatty acid and amino acid catabolism and the membrane-bound electron transfer flavoprotein ubiquinone oxidoreductase."]
- [PMID:25416781 "ETF acts as a mobile electron carrier that shuttles electrons between several FAD-containing dehydrogenases present in the mitochondrial matrix and the membrane-bound ETF:quinone oxidoreductase"]
- [PMID:25416781 "in addition to complexes I and II, it is the third major provider of electrons to the ubiquinone pool of the mitochondrial respiratory chain"]

## Structure / domain / role of beta subunit
- Heterodimer: two domains from alpha, third domain entirely from beta; FAD lies in a cleft
  between subunits, mostly in the C-terminal portion of alpha [PMID:8962055].
- ETFB binds an AMP molecule that probably has a purely structural role
  [file:UniProt FUNCTION].
- **Recognition loop** (residues 183-205; ~191-200 in older numbering) at the surface of ETFB
  recognizes a hydrophobic patch on interacting dehydrogenases and acts as a static anchor
  [file:UniProt DOMAIN "The recognition loop recognizes a hydrophobic patch at the surface of interacting dehydrogenases and acts as a static anchor at the interface."].
- L195A severely impairs complex formation with ACADM (MCAD) [file:UniProt MUTAGEN 195].

## Localization
- Mitochondrial matrix. UniProt SUBCELLULAR LOCATION: "Mitochondrion matrix".
- Imported into matrix; unusual in lacking a cleavable leader peptide; energy-dependent import
  [PMID:8504797 "the cDNA-encoded beta-ETF polypeptide contains the information necessary to reach the mitochondrial matrix"].
- Reactome notes ETF resides on the matrix face of the mitochondrial inner membrane [R-HSA-169260].
- HPA IDA (GO_REF:0000052) and HTP mito proteome (PMID:34800366) both mitochondrion.

## Complex
- Part of the mitochondrial electron transfer flavoprotein complex (ETFA/ETFB heterodimer;
  ComplexPortal CPX-2731); GO:0045251 IPI from PMID:8962055 crystal structure.

## Regulation / PTM
- ETFBKMT (METTL20) trimethylates Lys-200 and Lys-203, adjacent to the recognition loop,
  reducing ETFB's ability to receive electrons from MCAD and GCDH [PMID:25416781].
- MBTPS1/S1P forms a trimeric complex with ETFA/ETFB, stabilizing the heterodimer and
  promoting FAD binding (flavination) [PMID:35362222 "S1P forms a trimeric complex with ETFA/ETFB. S1P enhances ETFA/ETFB flavination and maintains its stability."].
- ETFRF1 (LYRM5) is a "deflavinase" that removes FAD from ETF [PMID:27499296].

## Disease
- Biallelic ETFB variants cause **multiple acyl-CoA dehydrogenase deficiency (MADD) /
  glutaric acidemia type II (GA2B, MIM:231680)** [file:UniProt DISEASE; PMID:7912128;
  PMID:12815589]. GA2B variants D128N (decreased stability) and R164Q (reduced electron
  transfer activity).

## Annotation review decisions summary
- MF electron transfer activity (GO:0009055): CORE. Multiple IDA/TAS/IBA/IEA -> ACCEPT (one core, rest accept).
- BP fatty acid beta-oxidation using acyl-CoA dehydrogenase (GO:0033539): CORE (IDA/IBA/IEA) -> ACCEPT.
- BP amino acid catabolic process (GO:0009063): supported (dehydrogenases in aa catabolism) -> ACCEPT.
- BP respiratory electron transport chain (GO:0022904): supported (feeds ubiquinone pool) -> ACCEPT.
- CC mitochondrial matrix (GO:0005759): CORE location -> ACCEPT.
- CC mitochondrion (GO:0005739): broader; ACCEPT / KEEP_AS_NON_CORE (matrix is more precise).
- CC electron transfer flavoprotein complex (GO:0045251): CORE complex -> ACCEPT.
- protein binding (GO:0005515) IPIs x5: bare protein binding, uninformative -> MARK_AS_OVER_ANNOTATED
  (do NOT REMOVE experimental IPIs per policy). WITH/FROM: ETFA (P13804), ETFRF1 (Q6IPR1),
  MBTPS1 via PMID:35362222 (P13804|Q14703). These are real interactions but the GO term itself
  is uninformative.

## Deep research
falcon DR file not present within poll window; grounded in UniProt, cached PMIDs, Reactome,
and the MADD disorder KB.
