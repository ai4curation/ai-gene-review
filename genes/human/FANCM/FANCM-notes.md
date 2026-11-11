# FANCM (Q8IYD8) gene review notes

Human Fanconi anemia group M protein. 2048 aa, ~250 kDa. HGNC:23168, chr14. DEAH-box
helicase family, FANCM sub-subfamily. Ortholog of archaeal Hef, S. pombe Fml1, S. cerevisiae Mph1.

## Domain architecture (UniProt Q8IYD8)
- N-terminal helicase ATP-binding (DEAH/SF2) domain ~98-266; Walker A ATP-binding 111-118; DEAH box 214-217 (K117 catalytic).
- Helicase C-terminal domain ~452-627.
- CENPS/CENPX (MHF) interaction region ~661-800.
- C-terminal ERCC4/XPF-like (nuclease-dead) + (HhH)2 domain; FAAP24 interaction region ~1727-2048.
- Large intrinsically disordered central/C-terminal regions.

## Core biology
FANCM is a DNA-dependent ATPase / ATP-dependent DNA translocase that anchors the FA core complex
to chromatin at stalled replication forks and DNA interstrand crosslinks (ICLs). Its N-terminal
translocase catalyzes ATP-dependent branch migration of forks and Holliday junctions (fork
remodeling); its nuclease-dead C-terminal ERCC4-like domain heterodimerizes with FAAP24, and it
binds the MHF1/MHF2 (CENPS/CENPX) histone-fold complex. Required for efficient FANCD2
monoubiquitination, ATR checkpoint signaling, replication traverse of ICLs, and suppression of
sister-chromatid exchange / crossover recombination.

## Provenance quotes

Catalytic/translocase engine:
- [PMID:16116422 "FANCM can dissociate DNA triplex, possibly due to its ability to translocate on duplex DNA."]
- [PMID:16116422 "FANCM may act as an engine that translocates the FA core complex along DNA."]
- [PMID:16116422 "FANCM is essential for FANCD2 monoubiquitination and becomes hyperphosphorylated in response to DNA damage."]
- Human FANCM is a translocase, not a canonical duplex-unwinding helicase: [PMID:19423727 "HEF and MPH1 possess helicase activity, 20 , 21 whereas for FANCM only translocase activity was observed."]
- ATPase required for cross-linker resistance / fork remodeling but not for FANCD2 monoub: [PMID:19423727 "The ATPase activity of FANCM is required for cross-linker resistance but not for FANCD2 monoubiquitination and focus formation."]
- Branch migration of fork/HJ: [PMID:20347429 "FANCM has a DNA branch migration activity that can process branched DNA structures such as a movable replication fork (MRF)"]
- [PMID:20347429 "FANCM translocates on dsDNA and can unwind the D-loop and also process branched DNA structures, such as model DNA replication forks and the Holliday junction, by DNA branch migration"]
- ATP dependence of branch migration: [PMID:20347429 "Branch migration by the FANCM-MHF1-MHF2 ensemble is completely dependent on ATP"] and K117R abolishes it: [PMID:20347429 "the ATPase deficient FANCMK117R mutant did not display any DNA branch migration activity even with MHF1-MHF2 present"]

Recruitment / chromatin anchoring / FA pathway:
- [PMID:19423727 "the recruitment of the FA core complex seems to depend on FANCM."]
- [PMID:19423727 "FANCM is rather responsible for the recruitment of the FA core complex to the chromatin, which may than allow efficient FANCD2 monoubiquitination and focus formation. This function does not require ATP hydrolysis"]
- [PMID:17289582 "FAAP24, a protein that targets FANCM to structures that mimic intermediates formed during the replication/repair of damaged DNA."]
- [PMID:17289582 "the FANCM/FAAP24 complex may play a key role in recruitment of the FA core complex to damaged DNA."]
- [PMID:17289582 "FAAP24 ... associates with the C-terminal region of FANCM, and is a component of the FA core complex."]
- FANCM chromatin-restricted: [PMID:20347429 "FANCM was exclusively detected in the chromatin (P; pellet) fraction under all conditions"]

MHF complex / DNA binding / fork remodeling stimulation:
- [PMID:20347428 "FANCM forms a conserved DNA-remodeling complex with a histone-fold heterodimer, MHF. We find that MHF stimulates DNA binding and replication fork remodeling by FANCM."]
- [PMID:20347428 "FANCM and MHF are rapidly recruited to forks stalled by DNA interstrand crosslinks, and both are required for cellular resistance to such lesions."]
- [PMID:20347428 "In vertebrates, FANCM-MHF associates with the Fanconi anemia (FA) core complex, promotes FANCD2 monoubiquitination in response to DNA damage, and suppresses sister-chromatid exchanges."]
- MHF1/MHF2 = CENPS/CENPX: [PMID:20347429 "MHF1 has also been identified as a component of the CENPA-CAD complex and named centromere protein S (CENPS)"]
- MHF is core complex component: [PMID:20347429 "These results thus identify MHF1 and MHF2 as novel components of the FA core complex."]
- [PMID:20347429 "MHF1-MHF2 form a complex that binds DNA and stimulates the branch migration activity of FANCM"]

FA core complex membership (BRAFT supercomplex):
- UniProt SUBUNIT: FA core complex = CENPS, CENPX, FANCA, FANCB, FANCC, FANCE, FANCF, FANCG, FANCL, FANCM, FAAP24, FAAP100; associates with BLM complex to form BRAFT.

ICL repair / checkpoint:
- [PMID:20347429 "MHF1 plays a role in ICL repair and in the recovery of replication forks stalled by topoisomerase I-DNA cleavage intermediates"]
- FANCD2 monoub required: [PMID:29231814 "MMC-induced monoubiquitination of FANCD2 was impaired ... Genetic complementation of patient's cells with wild-type FANCM improved their resistance to MMC re-establishing FANCD2 monoubiquitination."]
- Checkpoint proficiency preserved in patient cells: [PMID:29231814 "we failed to observe any major impairment in the MMC- phosphorylation of H2AX and CHK1"]

HR regulation (not core HR): FANCM not essential for HR/RAD51 foci:
- [PMID:19423727 "EUFA867 lymphoblasts showed normal Rad51 foci, indicating that FANCM is not essential for homologous recombination repair. FANCM may have a more regulatory function in the homologous recombination process"]
- Crossover/SCE suppression: [PMID:19423727 "The increased sister chromatid exchanges ... hint at a role for FANCM in the suppression of crossover recombination."]

Meiotic / germ cell expression (POF15, SPGF28):
- [PMID:29231814 "FANCM protein was preferentially expressed along the chromosomes in pachytene cells, which undergo meiotic recombination."]
- Truncation removes C-terminal endonuclease + FAAP24 domain: [PMID:29231814 "This variant leads to the p.Gln1701* truncation ... which removes the C-terminal endonuclease and the FA associated protein 24 (FAAP24)-interaction domain ... FAAP24 mediates chromatin association of FANCM."]

Replisome / replication timing:
- [PMID:32769987 "The other interacts with the FANCM DNA translocase, is more prominent in late S phase, and favors heterochromatin."]

## Annotation-specific judgments
- RNA helicase activity (GO:0003724, IEA from EC:3.6.4.13): legacy alt-name "ATP-dependent RNA helicase";
  functionally FANCM is a DNA-dependent ATPase / DNA translocase — no RNA helicase activity demonstrated.
  EC→GO over-mapping; REMOVE.
- 3'-5' DNA helicase activity (GO:0043138, IBA+IEA): human FANCM shows translocase/branch-migration,
  not canonical processive duplex unwinding ("only translocase activity was observed", PMID:19423727).
  MODIFY -> DNA translocase activity (GO:0015616).
- protein binding (GO:0005515, 7 IPI incl. FAAP24, CENPS, MCM2, TRIM27, EPN2 + interactome maps):
  uninformative; MARK_AS_OVER_ANNOTATED (specific interactions captured via complex/MHF terms).
- cytosol (GO:0005829, TAS Reactome PKR pathway): FANCM is nuclear/chromatin-restricted; peripheral
  PKR-signaling annotation; MARK_AS_OVER_ANNOTATED.
- resolution of meiotic recombination intermediates (GO:0000712, IMP 20347428) and homologous
  recombination (GO:0035825, IEA): genuine but regulatory/non-core (FANCM limits crossovers/SCE;
  not essential for RAD51-dependent HR). KEEP_AS_NON_CORE.


## 2026-10-26 integrated evidence reassessment

The review now distinguishes ATP-driven branch migration from chromatin-associated recruitment of FA-core machinery. Two complementary core functions retain their original quotation positions. MHF-assisted DNA remodeling and FANCM:FAAP24 remodeling of DNA:RNA flaps and telomeric R-loops are explicitly separated by tested preparation. Positive hybrid-remodeling evidence supersedes the earlier blanket RNA-negative rationale above. The human motor is described as DNA translocase activity; this does not deny the positive directional-helicase experiments in fly and yeast donors.

Conserved SDSA participation is accepted from the verified PAINT placement, fly gap-repair products and Fml1 intermediate-processing/genetic evidence. Normal RAD51 foci do not exclude an active downstream role. Historical GO:0035825 is refined to SDSA on scientific scope; its absence from the fresh source is a separate lifecycle question. The specific human meiotic cleavage/rejoining assertion remains UNDECIDED. The inherited broad authored checkpoint proposal is retired and UNDECIDED, preserving both original quotations; it is not a claim of biological absence. Acute depletion, stable knockout and partially functional patient alleles remain distinct.

All 52 fresh GOA contexts were reviewed: 40 ACCEPT, three MODIFY to DNA translocase activity, eight KEEP_AS_NON_CORE and one UNDECIDED. The eight non-core contexts are seven supported generic interactions and a contextual cytosolic location. Exact supporting entities were adopted only through the accepted one-to-one source mapping. Historical old 12 is explicitly retired under the accepted current-source lifecycle decision, while its positive MODIFY interpretation and the independent active SDSA IBA remain. Both old 12 and authored 33 are retired for different documented reasons; all 54 objects remain stored and all 52 current contexts remain active.

Chromatin enrichment in particular human cells does not imply universal exclusion from nucleoplasm or context-specific cytosolic complexes. HPA055144 supports nucleoplasm in the tested cells, with actual A-431/U-2 OS images and PC-3 metadata distinguished. Reactome compartment decisions use FANCM's own entities. The three natural protein products remain separate, with no claim of equivalent activity, cofactor recruitment or localization.

All 38 inherited quotations and all prior reference findings are preserved. Shared PMID 20347428/20347429 reference assessments explicitly combine both evidence scopes; historical notes remain verbatim. New reference-prose spacing corrections do not change scientific judgments. No new quotation was manufactured. See [the evidence and interpretation guide](FANCM-source-guide.md) for public article locators, assay/species/product boundaries and actual access limits. The inherited notes above are retained as history; conclusions explicitly superseded here should not be read as the current judgment.

The historical GOA source identifies ARBA:ARBA00027491 for old 12. The official rule still outputs GO:0035825; target eligibility and the reason for the row's disappearance remain unresolved. Retirement preserves a historical source assertion and is not a claim of rule deletion or biological refutation. GO:0035825 is not treated as crossover-only or biologically disjoint from SDSA. The source-lifecycle choice is manual and independent of the positively supported mechanistic refinement.

The complete inherited Affinage report was inspected as discovery material. Its additional BTR-bridging, PCNA/AND-1, kinase-regulation, structural and synthetic-lethal/PARPi leads were not promoted to new assertions without an independent source audit. The core themes used here have primary-source support elsewhere. The report remains unchanged and is not cited merely to suppress the unused-research advisory. Eleven prior reference-review notes are additionally preserved verbatim under historical markers, alongside their current complete assessments.

## 2026-10-26 — Canonical validation

All six canonical checks pass, including strict GOA matching, ontology/component validation and rendering of 116 narratives. Computed status is DRAFT with eight advisories: seven supported generic-binding decisions under the project policy and one unused inherited research file. Review all 52 current imported contexts: 40 ACCEPT, eight KEEP_AS_NON_CORE, three MODIFY and one UNDECIDED. Retain two complementary core functions and all three natural products without assuming functional equivalence. Human meiotic intermediate resolution remains unresolved. Preserve all 54 inherited object positions, 38 quotation paths and reference associations. Retain the historical GO:0035825 source assertion as retired with its positive SDSA refinement; the recovered ARBA00027491 rule still exists, and neither rule deletion nor biological absence is inferred. The independent SDSA IBA remains active. Retire the inherited authored checkpoint proposal as UNDECIDED, distinguishing acute depletion, stable knockout and partial patient alleles. Adopt exact current GOA supporting entities in 20 mapped contexts. Preserve 35 original reference identities and findings, expand to 45 references and retain historical review notes. Existing UniProt, publication/Reactome/family caches, provider output, prior history and unrelated work remain unchanged. Nine missing publication files are genuine additive fetches. The current UniProt snapshot remains private consultation; its protein comments, features and sequence equal the preserved inherited record. No new quotation is authored. Generated HTML is checked without replacing the inherited file.


## Feedback-linked biological refinements, 2026-10-26

Human FANCM directly supplies the ATP-dependent motor for disassembly of hybrid substrates. The FANCM:FAAP24 preparation, translocase-dead control, ATP-γ-S control and heterologous-flap test support the branch-migration mechanism [PMID:26593718, Figure 6 and Biochemical Analysis]. The telomeric plasmid R-loop experiment directly demonstrates disassembly by recombinant FANCM–FAAP24 with ATP [PMID:31138795, Figure 7b and In vitro R-loop resolution assays]. These experiments motivate R-loop processing (GO:0062176) alongside DNA translocase activity; substrate remodeling is not separately relabeled as an independently established DNA/RNA-hybrid-binding function. The inspected 2015 text says translocase-dead protein without naming K117R. The 2009 paper discusses K117R in its own recruitment/repair experiments [PMID:19423727, Discussion]; these are distinct citation contexts.

FANCM-dependent recruitment of FA core proteins to chromatin is a chromatin-protein adaptor role (GO:0140463) [PMID:19423727, chromatin-fractionation discussion]. MHF and FAAP24 help engage FANCM with DNA, so their pairwise interaction observations are not automatically evidence that FANCM recruits them as cargo [PMID:17289582, Abstract; PMID:20347428, Results on cooperative DNA binding and ICL recruitment, Figures 3 and 5; PMID:20347429, Figure 4 and Discussion]. The seven generic interaction rows remain individually assessed under the project exception; the functional core describes FA core recruitment.

The original 2005 abstract establishes the Hef/Mph1 relationship and damage-associated hyperphosphorylation [PMID:16116422, Abstract]. The 2010 work describes the C-terminal ERCC4/XPF-like region and FAAP24 association [PMID:20347429, Introduction]. The description uses the fold relationship without adding unassayed nuclease chemistry or a residue-specific claim. Human ovarian germ-cell expression and familial non-syndromic primary ovarian insufficiency are supported by the homozygous truncating-variant study [PMID:29231814, Results on FANCM expression, family segregation and patient-cell complementation; Discussion]. Male infertility is not added from the ovarian paper. Conserved SDSA is explicitly attributed to fly/Fml1 experiments and the accepted phylogenetic inference, rather than a newly claimed human SDSA assay [PMID:25205745; PMID:22723423; GO_REF:0000033].

The captured QuickGO paths place GO:0045003 below GO:0000724, but no is_a/part_of path leads to GO:0035825. This graph distinction does not imply biological disjointness. GO:0062176 is under chromatin remodeling and has no ancestor/descendant overlap with the existing process terms. Comparator coverage is uneven: SETX, DDX19B, DDX5 and human RNASEH1 lack the exact term in these queries, while DDX21, DDX23 and budding-yeast Sen1 carry it. The DDX21 abstract and Figure 2 caption directly describe R-loop unwinding [PMID:28790157]; the DDX23 abstract describes its helicase-dependent suppression role [PMID:28076779]. These comparator papers are not added as FANCM evidence. The pinned GO-CAM index has no FANCM/Q8IYD8 match; this is a bounded local-model check, not proof of global model absence.
