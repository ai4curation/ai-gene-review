# nudE (Drosophila melanogaster, Q9VT70) - curation notes

## 2026-09-27 session (claude-code)

Sources: UniProt Q9VT70, GOA seed (36 rows), cached publications (all GOA PMIDs have full text); Falcon deep research not yet available at time of writing.

### Biology summary
- Single fly NudE/NDE1-NDEL1 family member [PMID:19417004 "has only a single gene for this protein"].
- Localization: kinetochores, spindles, nuclear envelope [PMID:19417004 "NudE can associate with kinetochores, spindles and the nuclear envelope"]; spindle envelope in male meiosis; NOT at centrosomes [PMID:19417004 "we do not see an accumulation of NudE near centrosomes in either neuroblasts or spermatocytes"].
- Phenotypes: centrosome detachment, unfocused spindle poles, congression failure with SAC arrest, failed centrosome migration to spermatocyte NE, male meiotic missegregation [PMID:19417004].
- Lis1 partner: TAP-tag association [PMID:19417004 "clearly demonstrate a strong association between NudE and Lis1"]; dendrite defects rescued by Lis1, Lis1-binding mutant only partially rescues [PMID:25908857].
- Neuronal cargo transport: co-moves with retrograde Golgi outposts, colocalizes with SV/mito markers [PMID:25908857 "indicating that NudE participates in the transport of multiple different types of cargo in neurons"].
- Nuclear positioning in da neurons [PMID:26490864 "the nuclei of mutant neurons were several micrometers distant from the dendritic arbors"].
- Oocyte specification [PMID:24531791]; border cell migration [PMID:22808215].

### Decisions
- Centrosome IBA/IEA and spindle pole centrosome ISS -> MARK_AS_OVER_ANNOTATED (fly-specific immunostaining negative).
- Centrosome duplication ISS -> MARK_AS_OVER_ANNOTATED (fly phenotype is detachment/migration).
- Kinesin complex IBA -> REMOVE (consistent with human NDE1/NDEL1 reviews).
- Microtubule binding (IBA/IEA/ISS) -> KEEP_AS_NON_CORE (authors note no known MT-binding domain).
- NEW GO:0140659 cytoskeletal motor regulator activity (ISS from human Nde1 reconstitution, PMID:37940657), matching the module's NudE-unit term and human NDEL1.

### Module relevance (nucleokinesis)
- Fly NudE supports the module's NudE-unit role (Lis1-dynein regulator; GO:0140659) and a nucleus-positioning role in postmitotic neurons, but there is no fly evidence for centrosome residency, differing from mammalian NDE1/NDEL1.
