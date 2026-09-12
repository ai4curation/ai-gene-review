# QDPR (Dihydropteridine reductase / DHPR) — review notes

UniProtKB:P09417, HGNC:9752, EC 1.5.1.34. Human, NCBITaxon:9606.

## Deep research provenance

`just deep-research-falcon human QDPR` was attempted (2026-07-05) but the falcon/Edison
run timed out (600s) and exited with code 1; no `QDPR-deep-research-falcon.md` was produced.
Per project policy I did NOT fabricate a `-deep-research-*.md`. This review is grounded in
the cached UniProt record, the seeded GOA, cached `publications/PMID_*.md`, and the dismech
BH4-deficiency disorder file (DHPR Deficiency subtype).

## Verified core biology

DHPR is the cytosolic NAD(P)H-dependent enzyme that regenerates tetrahydrobiopterin (BH4)
by reducing quinonoid-dihydrobiopterin (q-BH2) back to BH4. It is an essential component of
the aromatic amino acid hydroxylating systems (PAH, TH, TPH), which use BH4 as cofactor.

- [PMID:3033643 "Dihydropteridine reductase (DHPR; EC 1.6.99.7) catalyzes the NADH-mediated reduction of quinonoid dihydrobiopterin and is an essential component of the pterin-dependent aromatic amino acid hydroxylating systems."] — establishes MF (q-BH2 → BH4, NADH-dependent), dihydrobiopterin metabolism, and the link to aromatic-amino-acid hydroxylation. (Note the abstract uses the older EC 1.6.99.7; current is EC 1.5.1.34.)
- UniProt FUNCTION: "Catalyzes the conversion of quinonoid dihydrobiopterin into tetrahydrobiopterin." (ECO:0000269|PubMed:3033643, ECO:0000269|PubMed:8262916)
- UniProt CATALYTIC ACTIVITY: 5,6,7,8-tetrahydropteridine + NAD(+) = 6,7-dihydropteridine + NADH + H(+); RHEA:17869; EC 1.5.1.34. Physiological direction right-to-left (i.e. q-dihydropteridine + NADH → tetrahydropteridine). Also NADP(+) variant (RHEA:17865). So both NADH and NADPH are cofactors.
- [PMID:8262916 "A human dihydropteridine reductase (EC 1.6.99.10) has been created from a rat cDNA clone ... kinetic identity to the naturally occurring enzyme has been proven. Crystallization has also been achieved, and the crystal structure was solved using 2.5 A data"] — first structural characterization (PDB 1HDR); confirms activity/catalysis (EXP annotation to GO:0004155). Homodimer; SDR family.
- UniProt: SDR (short-chain dehydrogenase/reductase) family; SDR33C1. Rossmann NAD(P)-binding fold; ACT_SITE Tyr150 (proton acceptor); NADP binding residues 14-38.

## Disease

DHPR deficiency (HPABH4C, MIM:261630; MONDO:0009862; Orphanet 226) — autosomal recessive
BH4-deficient ("malignant"/atypical) hyperphenylalaninemia. Second most common HPA-associated
BH4 deficiency. Loss of BH4 regeneration → hyperphenylalaninemia + dopamine/serotonin
(monoamine neurotransmitter) deficiency + secondary cerebral folate deficiency; NOT corrected
by dietary Phe restriction alone; lethal if untreated.
- UniProt DISEASE (HPABH4C): "attributable to depletion of the neurotransmitters dopamine and serotonin, whose syntheses are controlled by tryptophan and tyrosine hydroxylases that use BH-4 as cofactor. Patients do not respond to phenylalanine-restricted diet."
- dismech `Tetrahydrobiopterin_Deficiency.yaml` DHPR Deficiency subtype: [PMID:32022462 "Biallelic pathogenic variants in QDPR gene lead to BH4‐deficient HPA, accompanied with a severe biogenic amines deficiency"].

## Localization

- Cytosol/cytoplasm: well established. GO:0005829 cytosol (TAS Reactome R-HSA-71130); GO:0005737 cytoplasm (IBA; IDA LIFEdb). This is the physiologically relevant compartment (BH4 salvage cycle serves cytosolic aromatic-amino-acid hydroxylases).
- GO:0005739 mitochondrion (HTP, PMID:34800366): large-scale MS mitochondrial-proteome mapping. DHPR is a soluble cytosolic enzyme in the SDR family with no mitochondrial targeting features (INIT_MET removed, N-acetyl-Ala2; no transit peptide). Likely a co-purifying/cytosolic contaminant or low-confidence assignment — mark as over-annotated / non-core, do not assert core mitochondrial localization.
- GO:0070062 extracellular exosome (HDA x2, urinary/prostatic exosome proteomics): typical of abundant cytosolic proteins captured in exosome proteomes; not a site of catalytic function. Keep as non-core / over-annotated.

## Term scrutiny

- GO:0009055 electron transfer activity (TAS PMID:3033643): the term is the ETC electron-carrier function ("directed movement of electrons from one molecular entity to another, typically mediated by electron carriers"). DHPR performs NAD(P)H-dependent hydride transfer to a pteridine (an oxidoreductase reaction), not electron-carrier shuttling. This is a generic/imprecise over-annotation; MODIFY to the specific GO:0004155 (already present) — the reference PMID:3033643 supports the reductase activity, not a distinct electron-carrier function.
- GO:0006520 amino acid metabolic process (TAS PMID:3033643): DHPR is not itself an amino-acid-metabolizing enzyme; it regenerates the BH4 cofactor used by the aromatic-amino-acid hydroxylases. The role is indirect/upstream. Very high-level term; keep as non-core (the biologically informative BP terms are BH4 biosynthesis/regeneration and pteridine metabolism). PMID:3033643 supports the link to aromatic-amino-acid hydroxylation.
- GO:0006559 L-phenylalanine catabolic process (IBA; in UniProt DR line, NOT in GOA tsv) — DHPR supports PAH-mediated Phe→Tyr via BH4 regeneration; not in the GOA snapshot so not reviewed as an existing annotation.

## Core functions
- MF: GO:0004155 6,7-dihydropteridine reductase activity (EC 1.5.1.34) — with NADH binding GO:0070404 and NADPH binding GO:0070402.
- BP: GO:0006729 tetrahydrobiopterin biosynthetic process (BH4 regeneration/salvage).
- CC: GO:0005829 cytosol.
