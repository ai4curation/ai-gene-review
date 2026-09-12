# RNF185 review notes

UniProt: Q96GF1 (RN185_HUMAN), 192 aa, gene RNF185. HGNC:26783. Chromosome 22. Close paralog of RNF5/RMA1 (RNF5/RNF185-like family, IPR045103).

## Core identity
RNF185 is a membrane-anchored RING-type E3 ubiquitin ligase (EC 2.3.2.27). C3HC4 RING domain (ZN_FING 39-80; catalytic Cys-39; C39A or C39A/C79A abolishes ligase activity) plus two C-terminal transmembrane helices (131-151, 172-192) with cytoplasmic N-terminus. The RING domain is responsible for E3 ligase activity.

[file:human/RNF185/RNF185-uniprot.txt "The RING-type zinc finger domain is responsible for E3 ubiquitin ligase activity"]
[file:human/RNF185/RNF185-uniprot.txt "MUTAGEN 39 ... C->A: Abolished E3 ubiquitin-protein ligase activity"]

## Primary role: ERAD (CFTR), partly redundant with RNF5
RNF185 is an ER-membrane ERAD E3 ligase. It controls the cotranslational ubiquitination and degradation of CFTR/CFTRdeltaF508, in a RING- and proteasome-dependent manner, and forms an E3 ligase module with RNF5 that is central to CFTR degradation. Co-depletion of RNF5 + RNF185 profoundly blocks CFTRdeltaF508 degradation. RNF185 physically interacts with RNF5 (IntAct EBI-2340249/EBI-348482).

[file:human/RNF185/RNF185-uniprot.txt "Responsible for the cotranslational ubiquitination and degradation of CFTR in the ERAD pathway"]
[PMID:24019521 "identify RNF185 and RNF5 as a novel E3 ligase module that is central to the control of CFTR degradation"]
[PMID:27485036 "RNFT1 and RNF185, but not CGRRF1 and RNF19B, exhibited significant resistance to ER stressor in an E3 activity-dependent manner"]

RNF185 is upregulated by the UPR / ER stress (thapsigargin, tunicamycin) and protects cells from ER stress-induced apoptosis. It positively regulates ERAD (GO:1904294, IMP PMID:27485036).

[file:human/RNF185/RNF185-uniprot.txt "Protects cells from ER stress-induced apoptosis"]

## E2 partners
Preferentially associates with the ERAD E2 enzymes UBE2J1 and UBE2J2; also binds UBE2D family in interactome screens.
[file:human/RNF185/RNF185-uniprot.txt "Preferentially associates with the E2 enzymes UBE2J1 and UBE2J2"]

## Secondary / non-core roles
- Mitochondrial autophagy: K63-linked polyubiquitination of BNIP1 at the mitochondrial outer membrane, stimulating LC3II accumulation and autophagolysosome formation; recruits p62. This is the original 2011 characterization ("mitochondrial E3 ligase").
  [PMID:21931693 "human RNF185 is a mitochondrial ubiquitin E3 ligase that regulates selective mitochondrial autophagy in cultured cells"]
  [PMID:21931693 "BNIP1 ... is polyubiquitinated by RNF185 through K63-based ubiquitin linkage in vivo"]
- Innate antiviral immunity: K27-linked polyubiquitination of cGAS (CGAS) at K173/K384, promoting cGAS enzymatic activity and cGAS-STING signaling / type I IFN. RNF185 is the first E3 ligase of cGAS.
  [PMID:28273161 "RNF185 specifically catalyzed the K27-linked poly-ubiquitination of cGAS, which promoted its enzymatic activity"]
  [file:human/RNF185/RNF185-uniprot.txt "catalyzing 'Lys-27'-linked polyubiquitination of CGAS at 'Lys-173' and 'Lys-384', thereby promoting CGAS cyclic GMP-AMP synthase activity"]

## Localization
UniProt records both Mitochondrion outer membrane (PMID:21931693) and ER membrane (PMID:24019521, PMID:27485036). The 2011 study reported mitochondrial outer membrane; later ERAD studies firmly place it at the ER membrane. ER membrane is the core compartment for its ERAD function; mitochondrial OM is a real but secondary localization tied to the BNIP1/autophagy role. Cytoplasm IEA (ARBA) is generic.

## Annotation review decisions (summary)
- ubiquitin protein ligase activity (GO:0061630): CORE, ACCEPT (multiple IDA/EXP; EC 2.3.2.27; RING C39A abolishes).
- ERAD pathway (GO:0036503) / positive regulation of ERAD (GO:1904294): CORE, ACCEPT (IGI/IMP).
- ER membrane (GO:0005789) / ER (GO:0005783): CORE location, ACCEPT.
- ubiquitin-like protein conjugating enzyme binding (GO:0044390): KEEP_AS_NON_CORE (E2/UBE2J binding; ancillary).
- ubiquitin binding (GO:0043130, IDA): ACCEPT non-core (reflects RING/ubiquitin handling).
- protein autoubiquitination (GO:0051865): KEEP_AS_NON_CORE (RING property).
- metal ion binding (GO:0046872) / zinc: KEEP_AS_NON_CORE (RING structural).
- K27-linked ubiquitination (GO:0044314), defense response to virus (GO:0051607), positive regulation of innate immune response (GO:0045089), positive regulation of type I IFN signaling (GO:0060340): KEEP_AS_NON_CORE (cGAS immunity role, real but secondary).
- mitochondrial outer membrane (GO:0005741): KEEP_AS_NON_CORE (BNIP1/autophagy role).
- cytoplasm (GO:0005737, IEA ARBA): KEEP_AS_NON_CORE (generic).
- protein binding (GO:0005515, many IPI): KEEP_AS_NON_CORE (uninformative).
- protein-containing complex binding (GO:0044877): KEEP_AS_NON_CORE.
- transmembrane transport (GO:0055085, Reactome TAS): REMOVE (RNF185 is not a transporter; CFTR/ABC pathway bleed-through).
- ER mannose trimming (GO:1904380, IEA ARBA / Reactome TAS): REMOVE (no mannosidase activity; pathway-adjacency over-annotation).
- ER quality control compartment (GO:0044322, IEA inter-ontology): KEEP_AS_NON_CORE.
- ubiquitin-protein transferase activity (GO:0004842, IEA): ACCEPT (parent of ligase activity).
- ubiquitin-dependent protein catabolic process (GO:0006511) / protein ubiquitination (GO:0016567): ACCEPT/KEEP_AS_NON_CORE (generic parents of ERAD).

## Falcon deep-research findings (incorporated 2026-06)

Reviewed `RNF185-deep-research-falcon.md` (Edison/Falcon, 2026-06-12). Existing core ERAD/CFTR, RNF5 redundancy, BNIP1 K63 mitophagy, and cGAS K27/innate-immunity roles are already captured. Genuinely new RNF185-specific findings (all PubMed-verified, added to references):

- NEW substrate Tapasin and the RNF185/Membralin (MBRL/TMEM259) ERAD complex: RNF185/Membralin recognizes unassembled Tapasin and degrades it via ERAD, controlling peptide-loading-complex formation and MHC-I surface expression; loss of the complex raises Tapasin and increases surface MHC-I. This is the strongest new finding and defines a named ER ligase complex plus a new physiological substrate. [PMID:39353943 "Tapasin assembly surveillance by the RNF185/Membralin ubiquitin ligase complex regulates MHC-I surface expression"] (Nat Commun 2024; DOI 10.1038/s41467-024-52772-x). Added as reference (relevance HIGH); full text not cached, so no GO annotation/supporting_text added. Candidate future annotations: protein-containing complex (RNF185/Membralin), and an ERAD/antigen-presentation MF/BP once full text is available.
- NEW K27-linked substrate TUFM: RNF185 catalyzes K27-linked polyubiquitination of mitochondrial elongation factor TUFM (via RNF185 TM1, aa133-155), recruiting SQSTM1/p62 to drive mitophagy, exploited by Senecavirus A. [PMID:38084826 "E3 ubiquitin ligase RNF185 catalyzes K27-linked polyubiquitination of TUFM"] (Autophagy 2024; DOI 10.1080/15548627.2023.2293442). Added as reference (relevance MEDIUM) and as a corroborating reference id on the existing K27-linked ubiquitination annotation (GO:0044314).
- NEW K27-linked substrate EBOV GP1,2: RNF185 polyubiquitinates Ebolavirus glycoprotein GP on Lys-673 with K27 chains, diverting it to SQSTM1/p62-dependent reticulophagy/ERLAD (lysosomal) rather than the proteasome — crosstalk among calnexin cycle, ERAD and reticulophagy. [PMID:36224200 "the ER Ub ligase RNF185 ... polyubiquitinates EBOV-GP on lysine 673 via ubiquitin K27-linkage"] (Nat Commun 2022; DOI 10.1038/s41467-022-33805-9). Added as reference (relevance MEDIUM) and as a corroborating reference id on GO:0044314.
- Synthesis: across cGAS, EBOV-GP, and TUFM, RNF185 repeatedly builds non-degradative K27-linked chains read by SQSTM1/p62 to route cargo to autophagy/lysosome — reinforcing K27 + p62 as a recurring RNF185 signalling output distinct from its core K48/proteasomal ERAD (CFTR) activity.
- Riepe et al. 2024 (MBoC, DOI 10.1091/mbc.e23-08-0336) genome-wide CRISPR screen: RNF185 is a redundant CFTR-F508del ERAD E3 uncovered only in RNF5-KO sensitized backgrounds, with UBE2D3 genetically acting as a shared E2; corroborates existing RNF5/RNF185 redundancy. Peripheral/not cached; not added as a reference.
- Di Gregorio et al. 2023 review (IJMS, DOI 10.3390/ijms242417176) frames RNF185 among mitochondrial E3 ligases (autophagy, immune signalling, cancer); review-level context, not added.
