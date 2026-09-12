# RLBP1 (CRALBP) — gene review notes

## Identity
- UniProt: P12271 (RLBP1_HUMAN), 317 aa, 36.5 kDa [file:human/RLBP1/RLBP1-uniprot.txt "RLBP1_HUMAN             Reviewed;         317 AA."]
- HGNC:10024; Synonym CRALBP [file:human/RLBP1/RLBP1-uniprot.txt "GN   Name=RLBP1; Synonyms=CRALBP;"]
- Names: Retinaldehyde-binding protein 1 / Cellular retinaldehyde-binding protein [file:human/RLBP1/RLBP1-uniprot.txt "RecName: Full=Retinaldehyde-binding protein 1;"]

## Molecular function — soluble retinoid carrier, NO catalytic activity
- UniProt FUNCTION: "Soluble retinoid carrier essential the proper function of both rod and cone photoreceptors. Participates in the regeneration of active 11-cis-retinol and 11-cis-retinaldehyde, from the inactive 11-trans products of the rhodopsin photocycle and in the de novo synthesis of these retinoids from 11-trans metabolic precursors. The cycling of retinoids between photoreceptor and adjacent pigment epithelium cells is known as the 'visual cycle'." [file:human/RLBP1/RLBP1-uniprot.txt, ECO:0000269|PubMed:19846785]
- Ligands: binds 11-cis-retinal (ChEBI:16066) at residues 180 and 202 [file:human/RLBP1/RLBP1-uniprot.txt "BINDING         180 ... /ligand=\"11-cis-retinal\""]; natural ligands 11-cis-retinol (11cROL) and 11-cis-retinal (11cRAL) [reactome:R-HSA-2454264 "The natural ligands are 11-cis-retinol (11cROL) and 11-cis-retinal (11cRAL)"].
- Fold: CRAL-TRIO domain (aa 136-297); Sec14-like family (CDD SEC14; Pfam CRAL_TRIO; SUPFAM CRAL/TRIO). PANTHER PTHR10174 "ALPHA-TOCOPHEROL TRANSFER PROTEIN-RELATED". No enzymatic activity — it is a lipophilic ligand-binding/transport module. [file:human/RLBP1/RLBP1-uniprot.txt "DOMAIN          136..297 ... /note=\"CRAL-TRIO\"" and "CDD; cd00170; SEC14; 1."]
- Keywords: Retinol-binding; Sensory transduction; Transport; Vision. [file:human/RLBP1/RLBP1-uniprot.txt "KW   ... Retinol-binding; Sensory transduction; Transport; Vision."]

## Visual (retinoid) cycle role
- CRALBP carries 11-cis-retinol and 11-cis-retinaldehyde in RPE and Müller cells [PMID:9326942 "it carries 11-cis-retinol and 11-cis-retinaldehyde"].
- In the retinoid cycle, RLBP1 sequesters/binds 11-cis retinoids produced during the cycle (RLBP1:11cROL formation) [reactome:R-HSA-2454264 "it plays a role in sequestering 11-cis retinoids produced during the retinoid cycle"]; the bound 11-cis-retinol is presented for oxidation to 11-cis-retinal by RDH5/RDH10/RDH11 [reactome:R-HSA-2454081 "RDH5 oxidises 11cROL to 11cRAL"].
- RLBP1 must dissociate from 11cRAL before onward transport (RLBP1 is not in photoreceptors) [reactome:R-HSA-8960973 "It is assumed cellular retinaldehyde-binding protein (RLBP1) must dissociate from 11cRAL before 11cRAL is transported as RLBP1 is not present in photoreceptor cells."].
- Also binds all-trans-retinol (RLBP1:atROL) [reactome:R-HSA-2465971, title only].

## Localization / expression
- Subcellular: Cytoplasm [file:human/RLBP1/RLBP1-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm."]; HPA IDA cytosol (GOA GO:0005829 IDA).
- Tissue: Retina and pineal gland; NOT in photoreceptors; abundant in RPE and Müller glia [file:human/RLBP1/RLBP1-uniprot.txt "Not present in photoreceptor cells but is expressed abundantly in the adjacent retinal pigment epithelium (RPE) and in the Mueller glial cells of the retina."]; HPA "Tissue enriched (retina)".

## Disease
- Retinitis punctata albescens (RPA, MIM:136880); R150Q abolishes 11-cis-retinaldehyde binding [PMID:9326942 "The mutant protein lacked the ability to bind 11-cis-retinaldehyde."; file:human/RLBP1/RLBP1-uniprot.txt VARIANT 151 "R -> Q (in RPA; loss of ability to bind 11-cis-retinaldehyde"].
- Autosomal-recessive retinitis pigmentosa (arRP) [PMID:9326942, title/abstract].
- Bothnia retinal dystrophy (BRD, MIM:607475), R234W [file:human/RLBP1/RLBP1-uniprot.txt "Bothnia retinal dystrophy (BRD)"; PubMed:10102298 / 19846785].
- Newfoundland rod-cone dystrophy (NFRCD, MIM:607476), splice-junction mutations [file:human/RLBP1/RLBP1-uniprot.txt "Rod-cone dystrophy Newfoundland (NFRCD)"; PubMed:11868161].

## Annotation review reasoning
- GO:1902936 phosphatidylinositol bisphosphate binding (IBA, GO_REF:0000033): PANTHER-family-propagated. RLBP1's physiological ligands are retinoids (11-cis-retinal/retinol, all-trans-retinol), not PIP2; the CRAL-TRIO pocket in CRALBP is a retinoid pocket. No PIP2 binding is supported by any RLBP1 experimental evidence. The IBA family (PTN000019344) mixes Sec14/CRAL-TRIO proteins, some of which bind phosphoinositides; this is an over-propagation to RLBP1. Mark as MARK_AS_OVER_ANNOTATED (not REMOVE per policy: it is family-based and not clearly-wrong IEA; but it is not core). NOTE: This is IBA, not experimental.
- GO:0005515 protein binding (IPI, PMID:32296183 / IntAct, partner KLHL8): high-throughput HuRI Y2H; no functional context for RLBP1. Bare "protein binding" is uninformative. MARK_AS_OVER_ANNOTATED (never REMOVE a protein-binding IPI).
- Cytoplasm (IEA GO_REF:0000044) / cytosol (IDA HPA; TAS Reactome x7): consistent with soluble carrier in RPE/Müller cytosol. Cytosol IDA is the best-supported location → ACCEPT; cytoplasm IEA is the parent → KEEP_AS_NON_CORE; Reactome TAS cytosol duplicates → ACCEPT the reaction-derived location but non-core.
- cell body (GO:0044297, IEA GO_REF:0000107, from rat ortholog via Ensembl Compara): plausible for Müller glia but weakly supported by orthology transfer; KEEP_AS_NON_CORE.
- vitamin A metabolic process (GO:0006776, TAS PMID:9326942) and visual perception (GO:0007601, TAS PMID:9326942): both directly supported; core BP. ACCEPT.
