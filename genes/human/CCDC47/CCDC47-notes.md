# CCDC47 (Q96A33) curation notes

## Identity
- HGNC: CCDC47; aka Calumin; "PAT complex subunit CCDC47" (UniProt RecName).
- Single-pass type I ER membrane protein. Signal peptide 1-20; cytoplasmic 21-135; TM 136-155; lumenal 156-483. N-glycosylated at N178. Large lumenal domain with C-terminal disordered/coiled-coil basic region.
- Disease: Trichohepatoneurodevelopmental syndrome (THNS, MIM:618268), autosomal recessive: woolly/coarse hair, liver dysfunction, dysmorphic features, hypotonia, global developmental delay. (This is the "CHISEL"/trichohepatoenteric-like phenotype referenced in the task.)

## Core function: PAT complex / multipass translocon (MPT)
CCDC47 is the scaffold subunit of the PAT (Protein Associated with the ER Translocon) complex, an obligate heterodimer with WDR83OS/Asterix. The PAT complex is one of three accessory subcomplexes (GEL: TMCO1+RAB5IF; BOS: NCLN+NOMO+TMEM147; PAT: CCDC47+Asterix) of the multipass translocon (MPT) that assembles around the ribosome–Sec61 channel during synthesis of multipass membrane proteins.

- [PMID:32814900 "Here we identify the PAT complex, an abundant obligate heterodimer of the widely conserved ER-resident membrane proteins CCDC47 and Asterix."]
- [PMID:32814900 "The PAT complex engages nascent TMDs that contain unshielded hydrophilic side chains within the lipid bilayer, and it disengages concomitant with substrate folding."]
- [PMID:32814900 "Cells that lack either subunit of the PAT complex show reduced biogenesis of numerous multi-spanning membrane proteins."]
- [PMID:32814900 "CCDC47 and Asterix form an obligate complex because knockdown or knockout of either protein results in substantial loss of the other"]
- [PMID:32814900 "Asterix is the substrate- interacting subunit of the PAT complex, while CCDC47 is needed for Asterix stability."]
- [PMID:32814900 "Thus, the PAT complex is an intramembrane chaperone that protects TMDs during assembly to minimize misfolding of multi-spanning membrane proteins and maintain cellular protein homeostasis."]

Note: Asterix, not CCDC47, directly contacts substrate TMDs; CCDC47's role is as the stable scaffold/occluder. The UniProt FUNCTION states CCDC47 "occludes the lateral gate of the SEC61 complex" (By similarity).

### Multipass translocon membership and substrate-driven assembly
- [PMID:32820719 "Here we describe a ~ 360 kDa ribosome-associated complex comprising the core Sec61 channel and five accessory factors: TMCO1, CCDC47 and the Nicalin-TMEM147-NOMO complex."]
- [PMID:32820719 "These results identify a new human translocon and provide a molecular framework for understanding its role in multi-pass membrane protein biogenesis."]
- McGilvray et al. cryo-EM resolved CCDC47 residues 52-239 in complex with the translocon; CCDC47 is ribosome-associated within this assembly. The structure paper "An ER translocon for multi-pass membrane protein biogenesis" reports the architecture of a ribosome-bound TMCO1 translocon including CCDC47 (supports GO:0043022 ribosome binding, IDA, PMID:32820719).
- [PMID:36261522 "This 'multipass translocon' is distinguished by three components that selectively bind the ribosome-Sec61 complex during multipass protein synthesis: the GET- and EMC-like (GEL), protein associated with translocon (PAT) and back of Sec61 (BOS) complexes."]
- [PMID:36261522 "Reconstitution studies demonstrate a role for multipass translocon components in protein topogenesis, and cells lacking these components show reduced multipass protein stability."]

UniProt FUNCTION synthesis: "Component of the multi-pass translocon (MPT) complex that mediates insertion of multi-pass membrane proteins into the lipid bilayer of membranes... The MPT complex takes over after the SEC61 complex... Within the PAT subcomplex, CCDC47 occludes the lateral gate of the SEC61 complex."

## Secondary / contextual functions
### ER calcium homeostasis
CCDC47/calumin binds Ca2+ with low affinity, high capacity; THNS patient cells show reduced ER Ca2+ stores and impaired Ca2+ signaling. This is plausibly a real role but is secondary to / partly downstream of its membrane-biogenesis scaffold function (loss of multipass membrane protein biogenesis would broadly perturb ER function).
- [PMID:30401460 "we identified bi-allelic variants in CCDC47 that encodes the Ca2+-binding ER transmembrane protein CCDC47. CCDC47, also known as calumin, has been shown to bind Ca2+ with low affinity and high capacity."]
- [PMID:30401460 "In vitro cellular experiments showed decreased total ER Ca2+ storage, impaired Ca2+ signaling mediated by the IP3R Ca2+ release channel, and reduced ER Ca2+ refilling via store-operated Ca2+ entry."]

### ERAD
Mouse Ccdc47/calumin co-IPs with ERAD machinery (p97/VCP, BiP, derlin-1, derlin-2, VIMP/SELENOS); knockdown reduces ERAD efficiency. This connects CCDC47 to ER protein quality control / proteostasis more broadly.
- [PMID:25009997 "Calumin co-immunoprecipitated with ERAD components such as p97, BIP, derlin-1, derlin-2 and VIMP, suggesting its involvement in ERAD."]
- [PMID:25009997 "calumin knockdown in HEK 293 cells resulted in ERAD being less efficient, as demonstrated by attenuation in both degradations of a misfolded α1-antitrypsin variant and the ER-to-cytosol dislocation of cholera toxin A1 subunit."]
- [PMID:25009997 "calumin homozygous mutant embryos die at embryonic days (E) 10.5-11.5"] — embryonic lethality, essential for development/ER organization (UniProt: "essential role in the maintenance of ER organization during embryogenesis").

## Over-annotations / non-core
- GO:0005515 protein binding (IPI) from interactome / innate-immunity network papers (PMID:21903422, PMID:32814053, PMID:32814900, PMID:35271311) — bare "protein binding" is uninformative. Note PMID:32814900 is the PAT-complex discovery paper but the GOA "protein binding" annotation collapses the meaningful WDR83OS/Asterix interaction; the informative content is captured by the PAT complex (protein folding chaperone complex) and chaperone terms instead.
  - PMID:21903422 = innate immunity (IRF/STING) interaction network (CCDC47 a network node; IntAct lists IRF7, STING1, TIRAP, IRAK1). Not a core function.
  - PMID:35271311 = OpenCell endogenous tagging cartography (high-throughput localization/interaction map).
  - PMID:32814053 = neurodegenerative-disease interactome map (high-throughput).
- GO:0003723 RNA binding (HDA, PMID:22658674) — from the mRNA-interactome capture atlas; high-throughput RBP capture, not a demonstrated specific RNA-binding function for CCDC47.
- GO:0001649 osteoblast differentiation (HDA, PMID:16210410) — from a quantitative membrane-proteome profiling of an MSC line during osteoblast differentiation; presence in a differential proteomics dataset, not evidence CCDC47 functions in osteoblast differentiation.
- GO:0016020 membrane (HDA, PMID:16210410, PMID:19946888) — generic; subsumed by the specific ER membrane terms.
- GO:0005509 calcium ion binding — IBA (GO_REF:0000033) and IEA (GO_REF:0000120). Supported by the low-affinity/high-capacity Ca2+ binding of calumin (PMID:30401460); retain but as non-core (a property contributing to ER Ca2+ buffering rather than the central biogenesis role).

## Localization
Well supported: ER membrane / rough ER membrane (multiple EXP/IDA: PMID:25009997, PMID:30401460, PMID:32814900). Core. RNA-seq / interactome localizations consistent.

## Summary of action plan
- CORE: PAT complex / MPT membership (GO:0160064 multi-pass translocon complex; GO:0101031 protein folding chaperone complex), multi-pass transmembrane protein insertion into ER membrane (GO:0160063), protein folding chaperone (GO:0044183), ribosome binding (GO:0043022), ER membrane localization (GO:0005789), endoplasmic reticulum (GO:0005783).
- NON-CORE (real but secondary): ER calcium ion homeostasis (GO:0032469), calcium ion binding (GO:0005509), ERAD pathway (GO:0036503).
- OVER-ANNOTATED: bare protein binding, RNA binding, osteoblast differentiation, generic membrane.
- MODIFY: GO:0045048 protein insertion into ER membrane (general) and GO:0006457 protein folding (general) -> replace with the specific multi-pass insertion term GO:0160063.
