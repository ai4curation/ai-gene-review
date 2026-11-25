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


## Integrated functional assessment — 2026-10-25

FANCE recognizes the FANCD2 substrate within the Fanconi anaemia core machinery. Human interaction and complementation studies distinguish this recognition contribution from FANCL/UBE2T ubiquitin transfer. C-terminal FANCE recognition mutants retain the core associations that were tested but lose productive FANCD2 monoubiquitination and cross-link resistance; the inference of unchanged intrinsic catalytic competence remains qualified (PMID:12093742; PMID:24451376). The single core now uses GO:1990756 ubiquitin-like ligase-substrate adaptor activity, with interstrand cross-link repair, nucleoplasm and FA nuclear-complex membership as its process, location and assembly context. This is a refinement of the inherited adaptor claim, not an additional activity or a transfer of FANCL chemistry.

The inherited proposed annotation at position 25 originally cites PMID:12093742; PMID:12649160 is supporting evidence. Its five quotations and all other inherited quotation text, positions and reference associations remain unchanged. The integrated historical candidate contains 26 objects: 25 imported source contexts and one inherited proposed-source object, now reviewed as MODIFY. Current decisions are 20 ACCEPT, 3 KEEP_AS_NON_CORE, 2 MODIFY and 1 UNDECIDED. The inherited COMPLETE status has not been recomputed here. Generic FANCC/BioPlex associations remain supported non-core contexts, AKT1 binding is partner-specific, and the imported chromatin IDA remains unresolved without an absence claim.

Positive nuclear evidence includes human experiments and HPA nucleoplasmic imaging. Nucleoplasm is not used to erase broader nuclear or chromosome-associated observations. Reactome also models a cytosolic FANCE pool in a PKR-associated assembly; this does not establish an autonomous FANCE PKR mechanism. The 536-residue displayed protein, engineered constructs and external transcript/protein models remain distinct, with no natural alternative-products field invented.

The extra current nuclear-periphery IEA is retained as a separate source proposal. Its traced mouse donor PMID:27486799 measures Fancd2 with an anti-FANCD2 antibody and explicitly reports unsuccessful Fance immunohistology. Removal of that electronic transfer and an upstream attribution CHECK are proposed; the CHECK is NOT_REPORTED. This is not a negative localization claim about FANCE. Adopting the fresh source version and appending the new context require an explicit subsequent source integration.

Both complete assessments for PMID:12093742 and PMID:24451376 are preserved under labeled reading scopes. Immutable cache availability flags are separate from external original access and the passages or images actually inspected. The [FANCE evidence and source guide](FANCE-source-guide.md) records public article, figure, table, database and phylogenetic locators, including assay and access limits. No new publication quotation or provider-generated research file was created.


## Source-version adoption and proposal replacement — 2026-10-25

The current genuine GOA source version supplies seven previously absent supporting-entity lists at inherited positions 0–6 and the additional nuclear-periphery context at position 26. These fields are copied from the actual deterministic seeder output; the old source identifiers, evidence, terms, ordering and review text are retained. The UniProt source remains unchanged. The current GOA TSV is adopted byte-for-byte, without manual editing.

The nuclear-periphery source at 26 carries the accepted REMOVE decision and NOT_REPORTED attribution CHECK: its mouse donor paper measured Fancd2, not Fance. This does not assert FANCE absence or a NOT localization. The retired broad-adaptor proposal at 25 keeps its MODIFY recommendation and every original quotation. A specific GO:1990756 substrate-adaptor proposal at 27 uses bare PMID:12093742 and PMID:24451376 support and adds no quotation. This records the already-supported substrate-recognition specificity while avoiding two active broad/specific proposals for the same activity; FANCE remains distinct from FANCL/UBE2T ubiquitin-transfer chemistry.

There are now 28 total objects and 27 non-retired objects: 26 imported source contexts plus one active specific authored proposal, with the earlier broad proposal retained as retired history. Non-retired decisions are 20 ACCEPT, 3 KEEP_AS_NON_CORE, 1 MODIFY, 1 UNDECIDED, 1 REMOVE and 1 NEW. The retired object retains MODIFY. All 23 inherited quotation paths and reference associations, the 31 reference objects, core, biological description and inherited status remain unchanged. The earlier 26-object tally describes the preceding handoff, not this adopted source version. No new quotation or upstream report was added.

## Feedback clarification — 2026-10-25

The specific GO:1990756 ubiquitin-like ligase-substrate adaptor proposal now occupies the original authored position 25 with action NEW. Its original PMID:12093742 attribution and all five quotation paths are retained. The earlier broad GO:0030674 term was an authored proposal, not an imported GOA assertion. The retired/MODIFY representation and the duplicate last proposal at 27 are therefore removed; the preceding journal entries remain a record of that superseded representation. The genuine imported nuclear-periphery context at 26 remains present and reviewed as REMOVE. No imported source object is altered.

The chromatin context at 8 is ACCEPT: human FANCE is identified in the FA nuclear core and the core has a chromatin-associated pool. The curator's component-level projection is retained while keeping the precise figure caveat: PMID:22343915 Figure 5H measures FANCA/FANCG/FAAP20/H2A, not a separately labeled FANCE band. This does not make every FANCE nuclear pool chromatin-bound or change the core's nucleoplasm location.

The standalone description restores CHEK1 phosphorylation of FANCE Thr346/Ser374 after checking the actual original Methods, Results, Figures 1–2 captions and Table 1 of PMID:17296736. Human full-length FANCE TS/AA complementation retains basal FANCD2 monoubiquitination and foci but fails normal damage-induced upregulation and mitomycin C resistance. Purified recombinant Chk1 phosphorylates bacterial human-FANCE preparations containing these sites. The detailed downstream role remains unresolved; no kinase activity or new process annotation is assigned to FANCE. The source guide records exact access and construct limits.

There are now 27 objects, all non-retired: 26 imported source contexts and one authored NEW proposal. Decisions are 21 ACCEPT, 3 KEEP_AS_NON_CORE, 1 MODIFY, 1 REMOVE and 1 NEW. All 23 inherited quotation text/reference/path associations, 31 complete reference objects, natural-product boundary, core and questions/experiments remain unchanged. The AKT1-specific binding refinement remains a contextual interaction outside the cross-link-repair core and does not establish an endogenous AKT1 repair mechanism. The MGI attribution query remains CHECK and NOT_REPORTED; a demonstrated mismatch in the inspected source does not authorize silently changing the upstream record.

The prior canonical DRAFT status reflected three advisories: supported generic-binding retentions at positions 4 and 5 and a present but uncited generated deep-research file. These are not inferred biological failures or caused by the chromatin UNDECIDED action. They are documented rather than used to manufacture quotations, duplicate cores or unsupported annotations. Canonical validation will recompute the status after this revision. No new publication quotations are added under the standing campaign instruction.
