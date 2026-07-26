# RFWD3 (Q6PCD5) review notes

Gene: RFWD3 / RNF201 ; Fanconi anemia complementation group W (FANCW). Human, 774 aa,
chromosome 16. Domains: degenerate RING-type zinc finger (aa 287-331), coiled-coil
(361-413), WD40 β-propeller (repeats ~495-628, crystallized in PDB 6CVZ residues 425-774).
EC 2.3.2.27 (RING-type E3 ligase). ATM/ATR phospho-substrate at Ser46 and Ser63.

## Core biology (synthesis)

RFWD3 is a RING-finger E3 ubiquitin ligase. It is recruited via its C-terminal WD40 domain
to the RPA2 subunit of the RPA complex that coats ssDNA at stalled replication forks / sites
of DNA damage. Once localized, RFWD3 polyubiquitinates RPA (all three subunits) and RAD51,
promoting their VCP/p97-dependent removal/turnover from DNA damage sites so that homologous
recombination (HR) and interstrand crosslink (ICL) repair can progress. It also promotes
ubiquitination of proteins on ssDNA to drive PCNA ubiquitination and translesion synthesis
(TLS). Biallelic RFWD3 mutations cause Fanconi anemia group W (FANCW). A secondary, less
central function is stabilization of p53 in the late DNA-damage response via an RFWD3-MDM2
complex (G1/S checkpoint).

## Key provenance

### Catalytic activity / MF
- [PMID:21504906 "RFWD3 has E3 ligase activity in vitro"] — first in-vivo characterization.
- [PMID:26474068 "We demonstrate that the E3 ligase RFWD3 mediates RPA ubiquitination"]
- UniProt: EC=2.3.2.27, RING-type (degenerate). Catalytic Cys315 (C315A abolishes activity).

### RPA / RAD51 ubiquitination, HR, fork restart
- [PMID:26474068 "RFWD3 is necessary for replication fork restart, normal repair kinetics during replication stress, and homologous recombination (HR) at stalled replication forks"]
- [PMID:26474068 "we found that depletion of RFWD3 decreased fork restart"]
- [PMID:28575658 "we identified RAD51, the central HR protein, as another target of RFWD3. We show that RFWD3 polyubiquitinates both RPA and RAD51 in vitro and in vivo"]
- [PMID:28575658 "RFWD3 inhibits persistent mitomycin C (MMC)-induced RAD51 and RPA foci by promoting VCP/p97-mediated protein dynamics and subsequent degradation"]
- [PMID:28575658 "Phosphorylation by ATR and ATM kinases is required for this activity in vivo"]
- [PMID:28575658 "facilitates timely removal of RPA and RAD51 from DNA damage sites, which is crucial for progression to the late-phase HR and suppression of the FA phenotype"]

### RPA recruitment via WD40 / ICL repair / FANCW
- [PMID:28575657 "cells with mutations in RFWD3, an E3 ubiquitin ligase that interacts with and ubiquitylates replication protein A (RPA), show profound defects in ICL repair"]
- [PMID:28575657 "An amino acid substitution in the WD40 repeats of RFWD3 (I639K) found in a new FA subtype abolishes interaction of RFWD3 with RPA, thereby preventing RFWD3 recruitment to sites of ICL-induced replication fork stalling"]
- [PMID:28575657 "RFWD3 with a GFP tag at the N terminus, but not GFP alone, translocates to tracks of laser micro-irradiation and co-localizes with the phosphorylated form of histone variant H2AX"]
- [PMID:28575657 "The narrow spectrum of genotoxins (ICL-inducing agents) to which RFWD3Δ/Δ cells show sensitivity argues strongly that ICL repair is a major function of RFWD3"]
- [PMID:28575657 "unloading of RPA from sites of ICL induction is perturbed in RFWD3-deficient cells"]
- [PMID:28691929 "we propose RFWD3 as an FA gene, FANCW"]
- [PMID:28691929 "HR was disrupted in RFWD3-mutant cells as a result of impaired relocation of mutant RFWD3 to chromatin and defective physical interaction with replication protein A"]

### Recruitment to stalled forks / RPA2 binding / checkpoint
- [PMID:21504906 "we identified RFWD3 as a novel replication protein A (RPA)-associated protein. Using purified proteins, we observed a direct interaction between RPA2 and RFWD3"]
- [PMID:21504906 "RFWD3 is recruited to stalled replication forks and co-localizes with RPA2 in response to replication stress"]
- [PMID:21504906 "RFWD3 is important for ATR-dependent Chk1 activation in response to replication stress"]
- [PMID:21558276 title] RFWD3 associates with RPA and facilitates RPA-mediated DNA damage response; up-regulated in S-G2; partially at PML bodies (UniProt subcell).

### Translesion synthesis
- [PMID:33321094 "the E3 ubiquitin ligase RFWD3 promotes ubiquitylation of proteins on ssDNA"]
- [PMID:33321094 "PCNA ubiquitylation is inhibited without RFWD3, and TLS across different DNA lesions is drastically impaired"]

### p53 / MDM2 (secondary role)
- [PMID:20173098 "an E3 ubiquitin ligase RFWD3 (RNF201/FLJ10520) forms a complex with Mdm2 and p53 to synergistically ubiquitinate p53 and is required to stabilize p53 in the late response to DNA damage"]
- [PMID:20173098 "RFWD3 is phosphorylated by ATM/ATR kinases and the phosphorylation mutant fails to stimulate p53 ubiquitination"]
- [PMID:20173098 "Our study identifies RFWD3 as a positive regulator of p53 stability when the G(1) cell cycle checkpoint is activated"]

## Annotation decisions summary
- Core MF = RING E3 ubiquitin ligase activity (GO:0061630); process = ICL repair (GO:0036297),
  HR (GO:0000724), protein ubiquitination (GO:0016567); locations = nucleus (GO:0005634),
  site of DNA damage (GO:0090734).
- protein binding (GO:0005515) IPI annotations: all MARK_AS_OVER_ANNOTATED (uninformative;
  the biologically meaningful partners RPA2, RAD51, MDM2, p53, UBE2N are captured by specific
  terms or the core function).
- p53-axis terms (p53 binding, MDM2/MDM4 binding, G1 checkpoint, response to IR) =
  KEEP_AS_NON_CORE (secondary, single-group evidence).
- cytoplasm / cytosol / PML body = KEEP_AS_NON_CORE (undamaged-cell pool, not the functional site).
</content>
