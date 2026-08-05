# FANCF (Q9NPI8) review notes

Human Fanconi anemia group F protein. 374 aa, chromosome 11p14.3. HGNC:3587.

## Core biology

FANCF is a subunit of the Fanconi anemia (FA) nuclear **core complex** (FANCA, FANCB,
FANCC, FANCE, FANCF, FANCG, FANCL, FANCM + associated FAAP proteins). The core complex is
a multisubunit ubiquitin ligase (FANCL is the RING E3, UBE2T the E2) whose essential job is
**monoubiquitination of the FANCD2-FANCI (ID2) complex** in response to DNA damage
(especially interstrand cross-links, ICLs) and replication stress. Monoubiquitinated ID2 is
loaded onto chromatin and coordinates the downstream ICL-repair steps (nucleolytic
unhooking, translesion synthesis, homologous recombination).

FANCF itself has no catalytic activity and no recognizable sequence motif; its function is
**structural — a flexible molecular adaptor/scaffold** that bridges the FANCA:FANCG and
FANCC:FANCE subcomplexes and is required for assembly/stability of the intact core complex
and hence for FANCD2 monoubiquitination.

- de Winter 2000 [PMID:11063725 "FANCF was found predominantly in the nucleus, where it complexes with FANCA, FANCC and FANCG"] — nuclear localization + core-complex membership; interactions lost in FA cell lines (each subunit required for complex).
- Kowal 2007 (crystal structure of C-terminal domain 156-357) [PMID:17082180 "The human FANCF protein reportedly functions as a molecular adaptor within the FA nuclear complex, bridging between the subcomplexes A:G and C:E"] and [PMID:17082180 "Two C-terminal loops of FANCF are essential for monoubiquitination of FANCD2 and normal cellular resistance to the DNA cross-linking agent mitomycin C"] and [PMID:17082180 "FANCF mutants bearing amino acid substitutions in this C-terminal surface fail to interact with other components of the FA complex, indicating that this surface is critical for the proper assembly of the FA core complex"]. FANCF C-terminal fold resembles the Cand1 HEAT-repeat regulator of a cullin-RING ligase. MUTAGEN residues (L209R, F251R, Y287A/L289A/F339A/V341A/L344A) reduce FANCD2 monoubiquitination (UniProt features, ECO:0000269|PubMed:17082180).
- Gordon & Buchwald 2003 [PMID:12649160 "FANCG was shown to interact with both the amino-terminus of FANCA and the carboxyl-terminal region of FANCF"] and [PMID:12649160 "FANCG was able to mediate interaction between FANCA and FANCF"] — Y2H/Y3H mapping of FANCF/FANCG contact.

## FA core complex membership (subunit evidence, UniProt)
- FANCA, FANCC, FANCG complex: PMID:11063725.
- FANCA/FANCC/FANCE/FANCG/FANCL: PMID:12724401.
- +FANCB: PMID:15502827. +FANCM: PMID:16116422.
- ComplexPortal CPX-6263 "Fanconi anemia ubiquitin ligase complex".
- Cryo-EM structures of the human FA core complex 7KZP/7KZQ/... include FANCF chain F (1-374).

## Downstream pathway / process
- Knipscheer 2009 [PMID:19965384 "FANCI-FANCD2 is required for replication-coupled ICL repair in S phase"] — establishes the FA pathway drives replication-dependent ICL repair (NAS basis for FANCF ICL-repair BP annotation via ComplexPortal).
- FANCM-MHF (histone-fold MHF1/MHF2) DNA-remodeling complex recruits/anchors the core complex to stalled forks and promotes FANCD2 monoubiquitination [PMID:20347428 "FANCM-MHF associates with the Fanconi anemia (FA) core complex, promotes FANCD2 monoubiquitination in response to DNA damage"]. This is the IDA basis (PMID:20347428) for FANCF part_of FA nuclear complex.
- FAAP20 is an integral core-complex protein required for DNA-damage-induced chromatin loading of FANCA and functional integrity of the pathway [PMID:22343915 "FAAP20 is an integral component of the FA nuclear core complex" ; "the FAAP20-UBZ domain ... is required for DNA-damage-induced chromatin loading of FANCA and the functional integrity of the FA pathway"] — supports chromatin localization of the core complex (FANCF chromatin IDA, ComplexPortal).

## Localization
- Nucleus/nucleoplasm predominant (PMID:11063725; HPA immunofluorescence GO_REF:0000052). Chromatin upon DNA damage (ComplexPortal PMID:22343915). Reactome also models a cytosolic FA core complex:HSP70 species that binds PKR (R-HSA-9835411, PKR-mediated signaling) — peripheral/less-established, non-core.

## Interactome (protein binding IPI)
- PMID:11063725: FANCA (O15360), FANCG (O15287) — core partners (adaptor function).
- PMID:12649160: FANCA (O15360), FANCG (O15287) — Y2H contact mapping.
- PMID:32296183 (HuRI binary interactome): TCP11 (Q8WWU5-7) — high-throughput Y2H, no established FA relevance; non-core.
- PMID:32814053 (neurodegeneration Y2H interactome): HTT/huntingtin (P42858) — high-throughput screen, no established FA relevance; non-core.

## Disease
Biallelic FANCF loss → Fanconi anemia complementation group F (MIM:603467): bone marrow
failure, congenital malformations, cancer predisposition, cellular ICL hypersensitivity and
chromosomal instability [PMID:10615118, de Winter 2000 Nat Genet, FANCF cloning].

## Action rationale summary
- FA nuclear complex (GO:0043240) part_of, ICL repair (GO:0036297), nucleoplasm/nucleus/chromatin, DNA damage response: ACCEPT (well supported, on-target).
- protein binding (GO:0005515): FANCA/FANCG (PMID:11063725, 12649160) MODIFY → molecular adaptor activity (GO:0060090), the informative MF. TCP11/HTT large-scale hits: KEEP_AS_NON_CORE (real IPI, uninformative, no functional relevance).
- cytosol (GO:0005829, Reactome PKR): KEEP_AS_NON_CORE (predominantly nuclear; peripheral).
