# Rel (Relish; CG11992; UniProt Q94527) notes

## Identity
- Compound NF-kappaB family transcription factor resembling mammalian p105/p100: N-terminal Rel homology domain (RHD) plus C-terminal IkappaB-like ankyrin-repeat domain
  [PMID:8816802 "Relish, a compound Drosophila protein that, like mammalian p105 and p100, contains both a Rel homology domain and an I kappa B-like domain"].

## Activation (Imd/PGRP pathway)
- Signal-induced endoproteolytic cleavage; RHD (REL-68) goes to the nucleus, IkappaB-like part (REL-49) stays in cytoplasm
  [PMID:11269501 "An N-terminal fragment, containing the DNA-binding Rel homology domain, translocates to the nucleus where it binds to the promoter of the Cecropin A1 gene"],
  [PMID:11269501 "This endoproteolytic cleavage does not involve the proteasome, requires the DREDD caspase"].
- Cleavage is Cactus-independent [PMID:11400160].
- IKK (IKKbeta/Kenny) phosphorylates Relish S528/S529, needed for Pol II recruitment, not for cleavage
  [PMID:19497884 "these phosphorylation sites are not required for Relish cleavage, nuclear translocation, or DNA binding. Instead they are critical for recruitment of RNA polymerase II and antimicrobial peptide gene induction"].
- REL-68 alone activates Diptericin [PMID:19135474 "overexpression of REL-68 separately from REL-49 is sufficient to activate strong constitutive transcription of the Diptericin gene"].
- Forms homo- and heterodimers with Dif and Dorsal [PMID:20679214 "all combinations of homo- and heterodimers are formed, but with varying degrees of efficiency"].

## Immune roles
- Required for humoral immunity (antibacterial and some antifungal peptides), not cellular immunity
  [PMID:10619029 "Relish is specifically required for the induction of the humoral immune response, including both antibacterial and antifungal peptides"].
- Antiviral: STING-IKKbeta-Relish axis [PMID:30119996 "two components of the IMD pathway, the kinase dIKKβ and the transcription factor Relish, were required to control infection by two picorna-like viruses"];
  2'3'-cGAMP protection requires Relish [PMID:33262294 "this protection was abrogated in flies with mutations in the gene encoding the NF-κB transcription factor Relish"].
- Feedback: Relish induces negative regulators (miR-317, miR-308, miR-275, IMZF, lncRNAs) to restore homeostasis (PMIDs 36155909, 37358278, 37804878, 38762126, 37956726).
- Relish restrains JAK/STAT by interfering with Domeless dimerization [PMID:35905720 "Activated Imd signaling then employs the effector Relish to interfere with the dimerization of JAK/STAT transmembrane receptor Domeless"].

## Non-immune / context-specific
- Neural fate (ectopic bristles) [PMID:18000549], dendrite morphogenesis RNAi screen [PMID:23977298], DNA damage systemic response [PMID:21664581], amino-acid starvation induction of AMPs [PMID:17166233], neurodegeneration with Dnr1 [PMID:23613578].

## Deep research
- Falcon deep research was attempted; the first run was killed (exit 137, memory pressure on the shared host). Literature recorded here from cached publications.

## Review decisions
- Core: RNA Pol II-specific DNA-binding transcription activator, nuclear, in PGRP (Imd) and STING pathways.
- Generic protein binding removed except DIF-Relish dimerization (MODIFY to protein heterodimerization activity).
- ARBA IEA development terms (cell development, system development, anatomical part development) marked over-annotated.
