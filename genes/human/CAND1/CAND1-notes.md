# CAND1 (Q86VP6) research notes

## Identity / domain architecture
- Cullin-associated NEDD8-dissociated protein 1 (CAND1), formerly TIP120A (TBP-interacting protein 120A). A ~120 kDa HEAT-repeat protein that clamps around the cullin scaffold. [PMID:15537541 "Cand1, a 120 kDa HEAT repeat protein, forms a tight complex with the Cul1-Roc1 SCF catalytic core, inhibiting the assembly of the multisubunit E3 complex."]

## Core molecular function: SCF/CRL assembly factor & F-box (substrate-receptor) exchange factor
- UniProt summary: key assembly factor of SCF E3 ligases that promotes exchange of the substrate-recognition F-box subunit; acts as an F-box protein exchange factor; activity coupled to neddylation cycles; in the deneddylated state cullin-binding CAND1 binds CUL1-RBX1, increasing SCF dissociation and promoting F-box exchange; probably similar role in other CRLs. [file:human/CAND1/CAND1-uniprot.txt "Key assembly factor of SCF (SKP1-CUL1-F-box protein) E3\nCC       ubiquitin ligase complexes that promotes the exchange of the substrate-\nCC       recognition F-box subunit"] [file:human/CAND1/CAND1-uniprot.txt "Acts as a F-box protein\nCC       exchange factor."]
- CAND1 binds unneddylated CUL1 and regulates SCF formation; dissociation of CAND1 promotes F-box incorporation. [PMID:12504026 "We found the majority of CUL1 is in a complex with CAND1 and ROC1 independent of SKP1 and F box protein SKP2. Both in vivo and in vitro, CAND1 prevents the binding of SKP1 and SKP2 to CUL1 while dissociation of CAND1 from CUL1 promotes the reverse reaction."]
- Neddylation of CUL1 (or SKP1+ATP) dissociates CAND1. [PMID:12504026 "Neddylation of CUL1 or the presence of SKP1 and ATP causes CAND1 dissociation."]
- CAND1 selectively binds unneddylated CUL1 and is dissociated by neddylation; forms CUL1-ROC1 ternary complex; regulates assembly of productive SCF ligases. [PMID:12504025 "p120(CAND1) selectively binds to unneddylated CUL1 and is dissociated by CUL1 neddylation. CAND1 formed a ternary complex with CUL1 and ROC1."]
- Associates with all cullins tested; forms a complex with CUL1 and Rbx1 but interferes with Skp1/F-box binding; reduces SCF ubiquitination of substrate; "negative regulator of SCF E3 ubiquitin ligases." [PMID:12609982 "TIP120A formed a complex with CUL1 and Rbx1, but interfered with the binding of Skp1 and F-box proteins to CUL1. TIP120A greatly reduced the ubiquitination of phosphorylated IkappaBalpha by SCF(beta-TrCP) ubiquitin ligase. These results suggest that TIP120A functions as a negative regulator of SCF E3 ubiquitin ligases"]

## Structural mechanism
- Crystal structure of Cand1-Cul1-Roc1: Cand1 superhelix clamps Cul1; a beta-hairpin occupies the adaptor (Skp1) binding site; HEAT repeats bury the Cul1 lysine whose neddylation blocks Cand1 association. [PMID:15537541 "a Cand1 beta hairpin protrusion partially occupies the adaptor binding site on Cul1, inhibiting its interactions with the Skp1 adaptor and the substrate-recruiting F box protein subunits."]

## In vivo dynamics / regulation
- Although early biochemistry framed CAND1 as an inhibitor/sequester, in vivo it is a positive regulator of CRL activity that promotes substrate-receptor exchange (dynamic recycling). [PMID:21249194 "CAND1 ... has been shown to function as a positive regulator of Cullin ligases in vivo."]
- In mammalian cells CAND1 is predominantly cytoplasmic and cullins are its major interactors; only small amounts bind Cul1 at steady state (consistent with transient exchange-factor action). [PMID:21249194 "we show that CAND1 is predominantly cytoplasmically localized and that cullins are the major CAND1 interacting proteins."]
- F-box protein + substrate promote dissociation of the cullin-CAND1 complex, coupling assembly to substrate availability and neddylation. [PMID:16861300 "Skp2-Skp1 abrogates the inhibitory influence of CAND1 on the neddylation of Cul1 by promoting the dissociation of the cullin-CAND1 complex"]

## Localization
- Predominantly cytoplasmic/cytosolic, with nuclear pools (CRL4 in nucleus per Reactome). Cytosol and nucleus are both supported. Exosome/membrane/secretory-granule/ficolin-granule annotations are high-throughput proteomic (HDA) or Reactome "exocytosis" assignments and are best treated as over-annotations / contaminant-type localizations rather than functional sites.

## Historical TIP120A / transcription annotations
- CAND1 was originally described as TIP120A, a TBP-interacting transcriptional regulator. [PMID:10581176 "TBP-interacting protein 120A (TIP120A) is a novel eukaryotic transcriptional regulator"]
- The TBP-class protein binding (GO:0017025), positive regulation of DNA-templated transcription (GO:0045893), positive regulation of RNA pol II PIC assembly (GO:0045899), and cell differentiation (GO:0030154, from PMID:10581176) annotations derive from this early work. They predate the CRL-assembly paradigm and are not the consensus core function; treat as non-core / over-annotated.

## Synthesis of core vs non-core
- CORE: F-box/substrate-receptor exchange factor & SCF/CRL assembly regulation (GO:0010265 SCF complex assembly; involvement in protein ubiquitination GO:0016567 as a regulator, not catalyst); binding to / being part of cullin-RING ligase complex (GO:0031461) in its unneddylated/exchange state; negative regulation of (premature/unproductive) CRL catalytic activity (GO:0043086); cytosol & nucleus localization.
- NON-CORE / historical: TBP-class binding and transcription-regulation terms, cell differentiation (TIP120A era).
- OVER-ANNOTATED / uninformative: many high-throughput "protein binding" (GO:0005515) IPI hits; extracellular region, secretory granule lumen, ficolin-1-rich granule lumen, extracellular exosome, membrane (HDA/Reactome contaminant-type localizations).
- NOTE: CAND1 is a regulator/assembly factor, NOT a catalytic E3 or a ubiquitin-transfer enzyme; protein ubiquitination annotations are "involved_in" (regulatory) and should be read as such.
