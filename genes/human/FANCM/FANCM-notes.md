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
