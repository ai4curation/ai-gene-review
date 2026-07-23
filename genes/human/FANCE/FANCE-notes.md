# FANCE (Fanconi anemia group E protein) — review notes

UniProt: Q9HB96 (FANCE_HUMAN), 536 aa, chromosome 6. HGNC:3586. Gene ID 2178.

## Summary of biology

FANCE is one of the eight subunits of the Fanconi anemia (FA) core complex
(FANCA, FANCB, FANCC, FANCE, FANCF, FANCG, FANCL, FANCM, plus associated FAAP
proteins). The FA core complex is a nuclear multisubunit E3 ubiquitin ligase
(the catalytic RING subunit is FANCL) that monoubiquitinates the FANCD2–FANCI
(ID2) heterodimer in response to replication-blocking DNA interstrand crosslinks
(ICLs), triggering downstream ICL repair by nucleolytic incision, translesion
synthesis and homologous recombination.

FANCE's specific, distinguishing role within the core complex is that of a
molecular bridge/adaptor: it directly binds FANCC and directly binds the
substrate FANCD2, thereby physically linking the assembled core complex to its
downstream substrate. FANCE is also required for the nuclear accumulation of
FANCC.

## Key provenance

### Core function: bridge between FA core complex and FANCD2; FANCC nuclear accumulation
[PMID:12093742 "FANCE: the link between Fanconi anaemia complex assembly and activity"]
- [PMID:12093742 "Here we show that the recently identified FANCE protein is part of this nuclear complex, binding both FANCC and FANCD2. Indeed, FANCE is required for the nuclear accumulation of FANCC and provides a critical bridge between the FA complex and FANCD2."]
- [PMID:12093742 "Disease-associated FANCC mutants do not bind to FANCE, cannot accumulate in the nucleus and are unable to prevent chromosome breakage."]
- [PMID:12093742 "FANCE functions to target cytoplasmic FANCC to the nucleus as a result of a direct interaction between the two molecules ... In addition, FANCE binds to the FANCD2 protein, thereby providing a necessary link between the potential modifying nuclear complex and its likely substrate."]

### Direct FANCE–FANCC and FANCE–FANCD2 interactions (yeast 2/3-hybrid)
[PMID:12649160 "Fanconi anemia protein complex: mapping protein interactions in the yeast 2- and 3-hybrid systems"]
- [PMID:12649160 "A central region of FANCE was sufficient for FANCC binding. A Leu554Pro mutant of FANCC failed to interact with FANCE."]
- [PMID:12649160 "Direct interaction between FANCE and FANCD2 was also demonstrated in the yeast 2-hybrid system. This interaction involving an amino-terminal region of FANCD2 may provide a link between the FA protein complex and its downstream targets."]
- UniProt FT REGION 150..371 "Interaction with FANCC" (ECO:0000269|PubMed:12649160).

### FA core complex membership required for FANCD2 monoubiquitination
[PMID:17296736 "Chk1-mediated phosphorylation of FANCE is required for the Fanconi anemia/BRCA pathway"]
- [PMID:17296736 "Eight of the FA proteins (A, B, C, E, F, G, L, and M) form a core enzyme complex, required for the monoubiquitination of FANCD2 and the assembly of FANCD2 nuclear foci."]
- [PMID:17296736 "FANCE is assembled in the FA core complex and promotes the monoubiquitination of FANCD2"]
- Chk1 directly phosphorylates FANCE at Thr346 and Ser374; the non-phosphorylatable FANCE(T346A/S374A) still supports FANCD2 monoubiquitination and foci but fails to complement MMC hypersensitivity → phosphorylation has a function independent of FANCD2-Ub. [PMID:17296736 "Chk1-mediated phosphorylation of FANCE is required for a function independent of FANCD2 monoubiquitination."]
- UniProt: MOD_RES 346 Phosphothreonine by CHEK1; MOD_RES 374 Phosphoserine by CHEK1.

### Nuclear / chromatin localization
- UniProt SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:12093742, ECO:0000269|PubMed:17296736}.
- HPA IDA → nucleoplasm (GO:0005654) GO_REF:0000052.
- ComplexPortal IDA → chromatin (GO:0000785) PMID:22343915 (FA nuclear core complex is chromatin-associated / DNA-damage-induced chromatin loading).

### FA nuclear core complex (identification of FANCE as a subunit)
- [PMID:22266823 "We identified Fanconi anemia-associated protein (FAAP20), an integral subunit of the multisubunit Fanconi anemia core complex."] (FANCE identified as part of the FA core complex in this study; UniProt RN[16] "IDENTIFICATION IN THE FA COMPLEX", PMID:22266823).
- [PMID:20347428 "FANCM-MHF associates with the Fanconi anemia (FA) core complex"] — FANCM/MHF histone-fold complex study; FANCE is a subunit of the associated FA core complex (UniProt RN[9-11] identify FANCE in complexes with FANCA/B/C/F/G/L/M).
- ComplexPortal CPX-6263 "Fanconi anemia ubiquitin ligase complex".

### ICL repair (pathway-level)
[PMID:19965384 "The Fanconi anemia pathway promotes replication-dependent DNA interstrand cross-link repair"]
- [PMID:19965384 "A central event in the activation of the Fanconi anemia pathway is the mono-ubiquitylation of the FANCI-FANCD2 complex ... FANCI-FANCD2 is required for replication-coupled ICL repair in S phase."]
- Note: this NAS annotation on FANCE is a pathway-level attribution (the paper itself studies FANCI-FANCD2 in Xenopus egg extracts; FANCE participates as a core-complex subprovider upstream of FANCD2 monoubiquitination).

### Protein-binding (IPI) annotations
- PMID:12649160 IPI WITH FANCC (Q00597): direct FANCE–FANCC interaction — real, meaningful (underlies adaptor function).
- PMID:33961781 IPI WITH FANCC (Q00597): BioPlex proteome-scale AP-MS network (high-throughput); corroborates FANCE–FANCC.
- PMID:35512704 IPI WITH AKT1 (P31749): "Systematic discovery of mutation-directed neo-protein-protein interactions in cancer" — high-throughput neo-PPI screen; UniProt INTERACTION lists Q9HB96–P31749 (AKT1), NbExp=4. This is a reported interaction but not part of FANCE's core ICL-repair biology.

## Structure
- PDB 2ILR (2.0 Å, residues 273-536): C-terminal helical repeat domain (FANCE_c-term, CDD cd07439; Pfam PF11510 FA_FANCE). The C-terminal domain mediates FANCD2 binding.
- PDB 7KZP–7KZV (cryo-EM): FANCE within the assembled FA core complex.

## Disease
- Biallelic FANCE loss-of-function causes Fanconi anemia complementation group E (FANCE; MIM:600901): bone marrow failure, congenital malformations, cancer predisposition; cellular ICL hypersensitivity and chromosome instability. [PMID:11001585] (cDNA isolation / complementation group E), variant Q184 [PMID:17924555].

## Curation decisions (rationale)
- Core MF = molecular adaptor activity (GO:0060090): FANCE bridges FANCC/FA core complex to FANCD2. No specific catalytic MF (FANCE is non-catalytic; FANCL is the ligase).
- Core CC = Fanconi anaemia nuclear complex (GO:0043240).
- Core BP = interstrand cross-link repair (GO:0036297).
- `protein binding` (GO:0005515) annotations: kept as non-core (uninformative term, but valid interaction evidence). The AKT1 neo-PPI is non-core cancer-context.
- Reactome nucleoplasm TAS annotations (11 of them) all point to the same location; accept/keep-as-non-core (localization, correct but redundant).
