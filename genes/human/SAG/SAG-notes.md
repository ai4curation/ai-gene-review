# SAG (S-arrestin, arrestin-1, retinal S-antigen) notes

## Identity
Human SAG, UniProt P10523, 405 aa, arrestin family (PANTHER PTHR11792:SF15). Rod
(and some cone) photoreceptor arrestin. Also the retinal S-antigen of experimental
autoimmune uveitis; that is an antigenic property, not a function.

## Function (species noted)
- Arrestins bind GPCRs and switch off G protein activation [PMID:9333241 "Arrestins are soluble cytoplasmic proteins that bind to G-protein-coupled receptors, thus switching off activation of the G protein and terminating the signalling pathway that triggers the cellular response."]
- Mouse Sag knockout rods: rapid partial recovery then prolonged final phase; arrestin completes the quench of rhodopsin's catalytic activity [PMID:9333241 "This behaviour indicates that an arrestin-independent mechanism initiates the quench of rhodopsin's catalytic activity and that arrestin completes the quench."]
- Structure (bovine rhodopsin / mouse arrestin-1 mutants, XFEL): arrestin finger loop occupies the receptor cytoplasmic cavity used by transducin [PMID:26200343 "Arrestin binding to the receptors blocks their interactions with G proteins and leads to the receptor’s desensitization"].
- Bovine ROS extracts: arrestin inhibits dephosphorylation of photolysed rhodopsin by PP2A, but not of phosphorylase a, i.e. substrate-directed, not a phosphatase inhibitor [PMID:2550422].
- Human, mouse and bovine arrestin-1 self-associate (monomer-dimer-tetramer); only the monomer binds rhodopsin [PMID:21288033].
- Human genetics: homozygous 1147delA null alleles cause Oguchi disease (CSNB with very slow rod dark adaptation) [PMID:7670478].

## Location
- Human retina immuno-EM: proximal rod outer segment, on disc membranes, not plasma membrane, not in cones (with that antiserum) [PMID:3720866].
- Mouse: inner segment/perinuclear in dark, outer segment in light [PMID:12716919]; redistribution by diffusion, controlled by binding to photolysed rhodopsin in OS and microtubules in IS [PMID:15944125].

## Molecular function choice
GO offers no "rhodopsin inactivating" or "receptor desensitizer" activity specific to arrestin.
Candidates: GO:0002046 opsin binding (binding only), GO:0140311 protein sequestering activity
(binding to prevent a protein interacting with partners; existing IDA), GO:0030547 signaling
receptor inhibitor activity ("Binds to and modulates the activity of a signaling receptor").
GO:0030547 best states the core claim (binds P-Rh* and stops its catalytic activation of
transducin); it is the parent of nothing more specific suitable. Agree with the module.
GO:0140311 is also a valid reading and is kept (curator IDA).

## Rows considered doubtful
- Protein phosphatase inhibitor activity (TAS PMID:2550422): the paper says the effect is substrate-directed. Removed.
- GPCR internalization (IBA): beta-arrestin function; rhodopsin in discs is not endocytosed. Over-annotated.
- Spectrin binding (IEA from rat): source not seen. Undecided.
