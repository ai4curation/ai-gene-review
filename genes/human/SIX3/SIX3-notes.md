# SIX3 notes

Automated deep research was unavailable for this session (falcon 402, OpenAI 401); no
`-deep-research-<provider>.md` file was generated. These notes come from cached publications,
the UniProt record and QuickGO annotation lookups of mouse Six3 (Q62233).

## Molecular function
- Homeodomain TF of the Six3/6 (Optix) subfamily; does not pair with EYA. Instead it recruits Groucho/TLE:
  [PMID:12050133 "Six3 does not interact with any known member of the Eya family"];
  [PMID:12050133 "demonstrated that Six3 acts as a potent transcriptional repressor upon its interaction with Groucho-related members"].
- Human SIX3 binds TLE1 and AES via the Six domain (and the TLE WD domain):
  [PMID:12441302 "the Six domain of both SIX3 and SIX6 strongly interact with the QD domain of TLE1 and AES"].
- HPE eh1-motif variants abolish human SIX3 corepressor activity:
  [PMID:18791198 "we can also confirm that this interaction is essential for human SIX3 co-repressor activity"].
- Direct repression of Wnt1 (mouse): [PMID:12569128 "We demonstrate that Six3 binds to the Wnt1 promoter region in vivo and represses Wnt1 expression in the most anterior neuroectoderm."]
- Direct repression of Wnt8b for neuroretina specification: [PMID:20890044 "Six3 directly repressed Wnt8b expression in vivo"].
- Context-dependent activator: Shh SBE2 enhancer [PMID:18836447 "Six3 functions as a context dependent activator or repressor of target gene expression in the developing eye and forebrain"];
  Pax6/Sox2 in lens ectoderm [PMID:17066077 "Six3 directly activates Pax6 and probably also Sox2 in the PLE"]; rhodopsin [PMID:17666527].
- Non-transcriptional: binds geminin, competing with Cdt1 [PMID:14973488 "Six3 can promote cell proliferation without transcription"].

## Biological roles
- Forebrain: Six3-null mice lack telencephalon/rostral diencephalon (Wnt1 expansion) [PMID:12569128]; haploinsufficiency fails to activate Shh, causing HPE [PMID:18694563].
- Eye: medaka knockdown -> no forebrain/eyes; proximodistal optic vesicle patterning; cooperation with Pax6 [PMID:12163408].
- Lens induction via Pax6 [PMID:17066077, PMID:12072567]; pituitary with Hesx1 [PMID:18775421]; ependymal maturation [PMID:22071110].
- Human disease: HPE2 [PMID:10369266 "We propose that SIX3 is the HPE2 gene"]; 89% of tested variants LOF [PMID:18791198].

## Review decisions
- Core MF: GO:0001227 repressor activity (NEW), GO:0001222 corepressor binding, GO:0000981 (activator in context).
- Visual perception REMOVE (IEA) / over-annotated (TAS). Protein binding (NR4A3) -> GO:0061629.
- Lens fiber apoptosis, apoptotic process in development, neuroblast migration, lens fiber differentiation: over-annotations (indirect).
- Module `retinal_determination_network` annoton (GO:0000981 in eye development) is consistent, but SIX3 is
  better described as a repressor (GO:0001227) and, unlike fly So, does not act via EYA; module role text emphasises the So/Eya partnership.
