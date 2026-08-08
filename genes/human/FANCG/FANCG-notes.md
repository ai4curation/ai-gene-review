# FANCG (O15287, XRCC9) — review notes

## Identity / overview
- Human Fanconi anemia group G protein; 622 aa; gene = FANCG, synonym XRCC9; chr 9p13.
- TPR-repeat protein (UniProt lists TPR 1–4 at 246–279, 344–377, 453–486, 514–547; InterPro FANCG + FANCG_N; Gene3D TPR domain). No catalytic domain; α-helical solenoid scaffold. Cryo-EM structures of the human FA core complex include FANCG (PDB 7KZP/7KZQ/… chains G/H).
- Subunit of the multisubunit FA core complex (FANCA, FANCB, FANCC, FANCE, FANCF, FANCG, FANCL/PHF9, FANCM + FAAP20/FAAP100/FAAP24). The core complex is an E3 ubiquitin ligase (FANCL = catalytic RING) that monoubiquitinates the FANCD2–FANCI (ID2) heterodimer during S-phase interstrand crosslink (ICL) repair.

## Key functional evidence (with provenance)

- XRCC9 = complementing gene for MMC-hypersensitive CHO UV40; corrects chromosomal instability and mutagen sensitivity. [PMID:9256465 "We cloned and sequenced a human cDNA, designated XRCC9 , that partially corrected the hypersensitivity of UV40 to mitomycin C, cisplatin, ethyl methanesulfonate, UV, and γ-radiation"] and [PMID:9256465 "XRCC9 is a candidate tumor suppressor gene that might operate in a postreplication repair or a cell cycle checkpoint function"]. Note: 1997 paper could not assign a pathway ("no similarity with known proteins").

- FANCG is the FA complementation group G gene, identical to XRCC9. [PMID:9806548 "we report the identification of the gene mutated in group G, FANCG ... We identified the gene as human XRCC9"].

- FANCG is a component of a functional nuclear FA complex with FANCA and FANCC (Garcia-Higuera 1999, PMID:10373536, cited in UniProt). FANCG binds FANCA directly and strongly by Y2H. [PMID:10627486 "Using the yeast 2-hybrid system and full-length cDNA, the authors found a strong interaction between FANCA and FANCG proteins"].

- FANCF forms a nuclear complex with FANCA, FANCC and FANCG; each FA protein (except FANCD) required for complex formation → multiprotein nuclear FA complex maintains genomic integrity. [PMID:11063725 "FANCF was found predominantly in the nucleus, where it complexes with FANCA, FANCC and FANCG"] and [PMID:11063725 "a model in which a multi-protein FA complex serves a nuclear function to maintain genomic integrity"].

- FA core complex is required for DNA damage recognition at a stalled fork and monoubiquitinates FANCD2/FANCI; FANCG is one of the eight core subunits. [PMID:22266823 "Eight of the FA proteins comprise the FA core complex, a multisubunit complex required for DNA damage recognition at a stalled replication fork ... the complex, an E3 ligase, monoubiquitinates the FANCD2/FANCI heterodimer"]. FANCG specifically required for error-prone TLS/point mutagenesis: [PMID:22266823 "FANCA-deficient and FANCG-deficient cells exhibited a decrease in spontaneous and DNA damage-inducible point mutagenesis"].

- FA pathway (ubiquitinated FANCI–FANCD2) required for replication-coupled ICL repair in S phase. [PMID:19965384 "FANCI-FANCD2 is required for replication-coupled ICL repair in S phase"] (used to support ICL-repair BP; FANCG is upstream core-complex subunit needed for that monoubiquitination).

- FA core complex membership / chromatin loading (FAAP20 papers, FANCM-MHF, Rev1): [PMID:22343915 "FAAP20 is an integral component of the FA nuclear core complex ... required for DNA-damage-induced chromatin loading of FANCA and the functional integrity of the FA pathway"]. FANCM-MHF associates with the FA core complex and promotes FANCD2 monoubiquitination [PMID:20347428 "FANCM-MHF associates with the Fanconi anemia (FA) core complex, promotes FANCD2 monoubiquitination in response to DNA damage"]. FAAP20 links RNF8 ubiquitin signaling to the FA core complex [PMID:22705371 "a ubiquitin signaling cascade initiated by RNF8 ... and mediated by FAAP20, a component of the FA core complex"].

## Secondary / likely non-core roles
- Phospho-Ser7-dependent complex with BRCA2(FANCD1), FANCD2, XRCC3 (distinct from core complex). UniProt: "When phosphorylated at Ser-7, forms a complex with BRCA2, FANCD2 and XRCC3" (PMID:18212739). Ser7Ala abolishes BRCA2/FANCD2/XRCC3 binding but not FANCA/FANCF core-complex binding. Links FANCG to homologous-recombination machinery; not the canonical core-complex activity → treat as non-core.
- Mitochondrial/oxidative-stress role: FANCG interacts with mitochondrial peroxiredoxin-3 (PRDX3) and a fraction localizes to mitochondria; FA-G cells show distorted mitochondria and reduced mitochondrial peroxidase activity. [PMID:17060495 "the FA group G (FANCG) protein is found in mitochondria. Wild-type but not G546R mutant FANCG physically interacts with the mitochondrial peroxidase peroxiredoxin-3 (PRDX3)"] and [PMID:17060495 "FA-G cells demonstrate distorted mitochondrial structures"]. Real, experimentally supported, but a minor moonlighting/secondary role secondary to the nuclear ICL-repair function → KEEP_AS_NON_CORE (mitochondrion, mitochondrion organization, PRDX3 binding).
- αII-spectrin (SPTAN1) SH3-domain interaction via an SH3-binding motif in FANCG [PMID:19102630 "FANCG interacted with ... the SH3 domain ... The site of interaction in FANCG was mapped to a motif that binds to SH3 domains"] — specific but non-core scaffold interaction.

## Molecular function interpretation
- FANCG has NO known enzymatic/DNA-binding activity of its own. Within the FA core complex, DNA/branched-structure binding is via FANCM-MHF and the E3 catalysis via FANCL. FANCG is a TPR α-solenoid that acts as a protein-protein adaptor/scaffold: it binds FANCA directly and is required for assembly, stability and nuclear accumulation of the core complex.
- Therefore the GOA MF "damaged DNA binding" (TAS, PMID:9806548, source PINC/ProtInc — an old low-quality mapping; the 9806548 abstract makes no DNA-binding claim) is best read as a complex-level property mis-attributed to the FANCG subunit → over-annotation.
- "protein binding" (GO:0005515) IPI rows: the FANCA/FANCF rows are biologically central but the term is uninformative → keep as non-core. Rows from large binary-interactome / neurodegeneration-aggregation / host-pathogen screens (VIM, GFAP, CYP3A4, RAB5A, SUOX, tax, etc.) are non-specific → over-annotated.

## Action summary rationale
- Core: FA nuclear complex (CC), interstrand cross-link repair (BP), DNA damage response (BP), DNA repair (BP), chromatin/nucleoplasm/nucleus locations. 
- Non-core: cytoplasm/cytosol (minor form), nuclear speck, mitochondrion + mitochondrion organization + PRDX3 binding, spectrin/other specific PPIs.
- Over-annotated: damaged DNA binding (MF), high-throughput/aggregation/host-pathogen protein-binding rows.
