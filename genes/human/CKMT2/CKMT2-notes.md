# CKMT2 (human) — sarcomeric mitochondrial creatine kinase (S-MtCK), UniProt P17540

## Identity and family
- HGNC:1996, gene CKMT2, "Creatine kinase S-type, mitochondrial"; AltNames "Sarcomeric mitochondrial creatine kinase" (S-MtCK), "Basic-type mitochondrial creatine kinase" (Mib-CK). EC 2.7.3.2. 419 aa precursor with a 39-residue mitochondrial transit peptide [UniProtKB:P17540].
- One of two human mitochondrial CK genes: CKMT2 (sarcomeric, heart/skeletal muscle) vs CKMT1 (ubiquitous). Separate nuclear genes; the sarcomeric and ubiquitous cDNAs share ~73% nucleotide / ~80% amino-acid identity but <66% identity with cytosolic CKs [PMID:2324105 "The human sarcomeric and ubiquitous cDNAs share 73% nucleotide and 80% predicted amino acid sequence identities, but have less than 66% identity with the cytosolic creatine kinases."].
- Belongs to the ATP:guanido phosphotransferase family (phosphagen kinase) [UniProtKB:P17540].

## Catalytic function
- Reversibly catalyzes phosphate transfer between ATP and creatine: creatine + ATP = N-phosphocreatine + ADP + H(+) (RHEA:17157, EC 2.7.3.2) [UniProtKB:P17540 "Reaction=creatine + ATP = N-phosphocreatine + ADP + H(+)"].
- "Creatine kinase isoenzymes play a central role in energy transduction in tissues with large, fluctuating energy demands, such as skeletal muscle, heart, brain and spermatozoa." [UniProtKB:P17540].
- Direct GO support: creatine kinase activity GO:0004111 (IBA from GO_Central; IEA from RHEA/EC 2.7.3.2; TAS PMID:2324105). Process: phosphocreatine biosynthetic process GO:0046314 (IBA, IEA).

## Oligomeric assembly (octamer)
- "Exists as an octamer composed of four CKMT2 homodimers." [UniProtKB:P17540]. The X-ray structure of human S-MtCK (PDB 4Z9M, 2.10 Å, residues 27-416, in complex with ADP) shows 8 chains (A–H) [UniProtKB:P17540 DR PDB; 4Z9M].
- General MtCK biology: occurs as dimers and octamers; the octamer (four dimers) is the membrane-active, structurally stable unit located in the mitochondrial intermembrane/cristae space. (Background, web; corroborates octamer model.)

## Subcellular localization and cardiolipin binding
- "SUBCELLULAR LOCATION: Mitochondrion inner membrane; Peripheral membrane protein; Intermembrane side." [UniProtKB:P17540]. Reactome: mitochondrial inner membrane (TAS).
- "Mitochondrial creatine kinase binds cardiolipin." [UniProtKB:P17540 MISCELLANEOUS]. A cardiolipin-binding region maps to residues 40-64 [UniProtKB:P17540 FT REGION 40..64 Cardiolipin-binding]. Octameric MtCK binds the outer face of the inner membrane mainly through electrostatic interactions with cardiolipin (background, web).
- GOA localization annotations: mitochondrion GO:0005739 (IBA; HDA PMID:20833797; HTP PMID:34800366; TAS PMID:2324105) and mitochondrial inner membrane GO:0005743 (IEA UniProtKB-SubCell/ARBA; TAS Reactome).
- The mitochondrial intermembrane space (GO:0005758) is the precise compartment for the catalytically active octamer (used as a core_function location).

## Coupling to ANT and the phosphocreatine (PCr) shuttle
- S-MtCK is positioned at contact sites where it functionally couples to the adenine nucleotide translocator (ANT): mitochondrial ATP exported by ANT is used to phosphorylate creatine, producing phosphocreatine that diffuses to the cytosol; ADP is fed back to oxidative phosphorylation. This is the phosphate-loading limb of the PCr/Cr shuttle (background, web; consistent with phosphocreatine biosynthetic process GO:0046314).

## Permeability transition / contact-site role
- Octameric MtCK at inner/outer membrane contact sites bridges cardiolipin (inner membrane) and VDAC (outer membrane), recruiting ANT into proteolipid complexes; presence of the octamer at contact sites can restrain VDAC–ANT interaction and modulate mitochondrial permeability transition pore opening (background, web). This is a context/regulatory role, not the core catalytic function.

## Tissue expression
- "Sarcomere-specific. Found only in heart and skeletal muscles." [UniProtKB:P17540 TISSUE SPECIFICITY]. HPA: group enriched in heart muscle, skeletal muscle, tongue [UniProtKB:P17540 DR HPA].
- RNA blot: "heart-derived MtCK is sarcomere-specific, but the ubiquitous MtCK mRNA is expressed in most tissues." [PMID:2324105].

## Interactions (GOA protein binding annotations)
- IntAct/binary-interactome IPI annotations (GO:0005515, generic "protein binding"): CETN3 (O15182), NRF1 (Q16656-4), P4HA3 (Q7Z4N8), KLHL42 (Q9P2K6) from PMID:32296183 (HuRI binary interactome); CKMT1B (P12532) from PMID:33961781 (BioPlex). These are high-throughput interactome hits; "protein binding" is uninformative as a molecular function and several are likely non-physiological. The CKMT1B hit is biologically plausible (MtCK paralog hetero-association) but the generic term carries no functional content.

## GO review reasoning summary
- Core: creatine kinase activity (GO:0004111), phosphocreatine biosynthetic process (GO:0046314), mitochondrial intermembrane space (GO:0005758, location of active octamer).
- ACCEPT: GO:0004111 (IBA, IEA-RHEA, TAS), GO:0046314 (IBA, IEA), GO:0005743 mitochondrial inner membrane (IEA, TAS Reactome — directly supported localization), GO:0005739 mitochondrion (HDA/HTP/IBA/TAS — well-supported localization but less specific).
- MODIFY (too general → creatine kinase activity): GO:0003824 catalytic activity, GO:0016301 kinase activity, GO:0016772 transferase activity transferring phosphorus-containing groups, GO:0016775 phosphotransferase activity nitrogenous group as acceptor (all IEA/InterPro).
- MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE: GO:0006936 muscle contraction (TAS PMID:2324105) — CKMT2 supplies energy to contracting muscle but is not part of the contractile machinery; this is downstream/contextual.
- protein binding GO:0005515 (IPI, x2 references): uninformative; high-throughput. Do not adopt as core. Mark over-annotated (per curation guideline avoid bare protein binding).
</content>
</invoke>
