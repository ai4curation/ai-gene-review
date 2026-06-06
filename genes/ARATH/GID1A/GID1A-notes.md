# GID1A (Q9MAA7) — Arabidopsis thaliana — curation notes

## Identity and overview
- GID1A = GA INSENSITIVE DWARF1A, locus At3g05120. Synonyms CXE10 (carboxylesterase 10), GID1L1.
- Soluble nuclear gibberellin (GA) receptor; one of three Arabidopsis paralogs (GID1A/B/C), orthologs of rice OsGID1.
- Belongs to the carboxylesterase / hormone-sensitive lipase (HSL, 'GDXG' lipolytic enzyme) superfamily with an α/β-hydrolase fold, but functions as a hormone RECEPTOR, NOT as a catalytically active hydrolase.

## Function: GA receptor, not an active hydrolase
- "GID1 was first described in rice as a nuclear localized protein similar to hormone-sensitive lipase family without hydrolase activity" [PMID:24961590 "GID1 was first described in rice as a nuclear localized protein similar to hormone-sensitive lipase family without hydrolase activity (Ueguchi-Tanaka et al., 2005)"].
- All three recombinant AtGID1 proteins bind bioactive GA with higher affinity to GA4 [PMID:16709201 "The GA-binding activities of the three recombinant proteins were confirmed by an in vitro assay... all recombinants showed higher affinity to GA(4) than to other GAs"].
- Crystal structure of GID1A–GA–GAI(DELLA) ternary complex: GID1A binds GA in a deep pocket covered by its N-terminal helical switch, which then binds DELLA [PMID:19037309 "GID1A occludes gibberellin in a deep binding pocket covered by its N-terminal helical switch region, which in turn interacts with the DELLA domain"]. GID1 is called a "nuclear receptor" here [PMID:19037309 "By binding to a nuclear receptor, GIBBERELLIN INSENSITIVE DWARF1 (GID1), gibberellins regulate gene expression by promoting degradation of the transcriptional regulator DELLA proteins"].
- => `hydrolase activity` (GO:0016787, IEA from InterPro) is a spurious over-annotation derived from the lipase/esterase fold and should be removed. The UniProt EC=3.-.-.- is nominal; the catalytic Ser is not functional as a hydrolase in vivo.

## Mechanism / signaling
- GA-bound GID1 interacts with DELLA repressors (GAI, RGA, RGL1, RGL2, RGL3) in a GA-dependent manner; this is the receptor's effector step [UniProt SUBUNIT; PMID:17194763 "GA enhances the interaction between GID1 and DELLA proteins... the N-terminal sequence containing the DELLA domain is necessary for GID1 binding"].
- The GA–GID1–DELLA complex promotes DELLA interaction with the SLY1 F-box of SCF(SLY1), leading to DELLA polyubiquitination and 26S proteasomal degradation, derepressing GA responses [PMID:17194763 "the GA-GID1 complex promotes the interaction between RGA and the F-box protein SLY1, a component of the SCF(SLY1) E3 ubiquitin ligase that targets the DELLA protein for degradation"].
- GA-GID1 can also downregulate DELLA repression without degradation (proteolysis-independent) [PMID:18827182 "GA-bound GID1 can block DELLA repressor activity by direct protein-protein interaction with the DELLA domain. Thus, a SLY1-independent mechanism for GA signaling may function without DELLA degradation"].
- GID1A acts as a POSITIVE regulator of the GA signaling pathway [PMID:17194763 "GID1a-1c act as positive regulators of GA signaling, consistent with a role in perceiving bioactive GAs"].
- The DELLA domain is the "receiver domain" for activated GID1A [PMID:17416730 "the GAI DELLA domain alone can mediate GA-dependent GID1A interactions, we propose that the DELLA domain functions as a receiver domain for activated GA receptors"].

## Genetics / redundancy / phenotypes
- Single gid1 mutants ~ no/normal visible phenotype (UniProt DISRUPTION PHENOTYPE; PMID:17194763, PMID:17521411). Triple gid1a gid1b gid1c is an extreme GA-insensitive dwarf, non-germinating, GA-unresponsive [PMID:17521411 "The triple knockout seedlings were severe dwarfs... completely lost their ability to respond to exogenously applied GA"], [PMID:17416730 "mutants lacking the three GID1 GA receptor genes are GA insensitive with respect to GA-promoted growth responses, GA-promoted DELLA repressor degradation, and GA-regulated gene expression"].
- GID1A makes the strongest single contribution; gid1a gid1c reduced stem height; gid1a gid1b reduced male fertility (functional specialization within redundancy) [PMID:17194763 "gid1a gid1c and gid1a gid1b displayed reduced stem height and lower male fertility, respectively, indicating some functional specificity"].
- Floral organ development defects in the triple mutant [PMID:17194763 "Flower formation occurred in long days but was delayed, with severe defects in floral organ development"] — supports floral organ morphogenesis BP.

## Fruit-set / fertility (PMID:24961590)
- "GID1A plays a major role during fruit-set and growth, whereas GID1B and GID1C have specific roles in seed development and pod elongation" [PMID:24961590].
- GID1A expressed throughout the pistil [PMID:24961590 "GID1A is expressed throughout the whole pistil"].
- Supports `fruit morphogenesis` (GO:0048530) and `positive regulation of fertilization` (GO:1905516) for GID1A. The GOA IGI/IMP set (with GID1B Q9LYC1, GID1C Q940G6) reflects genetic redundancy analysis in this paper.
- NOTE on the negated annotation: GOA line "NOT|involved_in response to gibberellin (IGI, with Q9LYC1=RGL2... actually Q9LYC1 is GID1C? check)". The NOT annotation (with UniProtKB:Q9LYC1) and the non-negated IGI (with Q940G6) come from this fruit-set redundancy study; the NOT likely reflects a specific double-mutant combination where GID1A did not show a measurable contribution (redundancy masking). Treated cautiously / KEEP_AS_NON_CORE-style.

## Subcellular localization
- UniProt: Nucleus (by similarity, ECO:0000250). GID1 repeatedly described as a NUCLEAR receptor [PMID:19037309; PMID:24961590].
- Experimental GID1A-GFP/localization detected in BOTH nucleus and cytoplasm [GOA PMID:17416730 IDA: located_in nucleus AND cytoplasm]. Nuclear-cytoplasmic distribution is consistent with GA perception and DELLA (nuclear) interaction.
- TAIR ISM (GO_REF:0000122, AtSubP prediction) nucleus — redundant computational support for nucleus.

## GARU / stability (PMID:29042542)
- GID1 protein is itself a substrate of the RING E3 ligase GARU; GID1A interacts with GARU (basis of the IPI protein binding annotation and IDA nucleus). [PMID:29042542 "GARU (GA receptor RING E3 ubiquitin ligase) mediates ubiquitin-dependent degradation of GID1"]. GID1A localized to nucleus in this study (IDA).

## Hypoxia HEP (PMID:31519798)
- Genome-wide epigenome-to-translatome survey of hypoxia/reoxygenation in seedlings; GID1A appears as one of many regulated transcripts. This is a high-throughput expression pattern (HEP) annotation, not direct functional evidence that GID1A acts in the hypoxia response. Mark as over-annotated / non-core.

## Phytohormone network (PMID:32612234)
- Large-scale Y2H phytohormone protein interaction network; source of several IPI protein-binding interactions (incl. IMPA3 O04294, MES17 Q9SG92). High-throughput; supports DELLA + other interactions but `protein binding` is uninformative.

## Interaction partners (from GOA IPI WITH/FROM + UniProt INTERACTION)
- DELLAs: GAI (Q9LQT8), RGA (Q9SLH3), RGL1 (Q9C8Y3), RGL2 (Q8GXW1), RGL3 (Q9LF53) — GA-dependent, the core effector interactions.
- GID2/SLY-related Q9STX3 (GID2), AFPH2 Q9SV55, IMPA3 O04294 (importin alpha 3), MES17 Q9SG92.

## Curation decisions summary
- MF core: gibberellin binding (GO:0010331, IDA) — ACCEPT as core. No GO term "gibberellin receptor activity" exists (verified absent in OLS GO); propose as new term.
- hydrolase activity (GO:0016787) — REMOVE (fold-based mis-annotation; protein has no hydrolase activity).
- protein binding (GO:0005515, many IPI) — uninformative; KEEP_AS_NON_CORE (documents DELLA + other interactions) but not core; better captured by signaling BP and a future "GA-activated receptor / DELLA binding" MF.
- BP core: gibberellin-mediated signaling pathway (GO:0010476) + positive regulation of GA signaling (GO:0009939) — ACCEPT.
- response to gibberellin (GO:0009739) — ACCEPT (multiple lines), redundant with signaling.
- floral organ morphogenesis / fruit morphogenesis / positive regulation of fertilization — developmental outputs of GA signaling; KEEP_AS_NON_CORE (pleiotropic, redundant with paralogs).
- cellular response to hypoxia (GO:0071456, HEP) — MARK_AS_OVER_ANNOTATED.
- nucleus / cytoplasm — ACCEPT (nucleus core; cytoplasm experimentally observed).
