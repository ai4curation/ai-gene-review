# SLC25A11 (OGC / M2OM_HUMAN, Q02978) review notes

## Identity and family
- Human gene symbol SLC25A11 (HGNC:10981); synonyms OGC, SLC20A4. UniProt Q02978, entry name M2OM_HUMAN, 314 aa. [file:human/SLC25A11/SLC25A11-uniprot.txt]
- Named "Mitochondrial 2-oxoglutarate/malate carrier protein" / "Alpha-oxoglutarate carrier" / OGCP. [file:human/SLC25A11/SLC25A11-uniprot.txt]
- Member of the mitochondrial carrier (SLC25) family, TC 2.A.29: "Belongs to the mitochondrial carrier (TC 2.A.29) family." [file:human/SLC25A11/SLC25A11-uniprot.txt]
- Multi-pass inner-membrane protein with six transmembrane helices and the canonical tripartite Solcar repeat structure (three REPEAT / Solcar domains, three TRANSMEM-pair helices; PROSITE PS50920 SOLCAR x3, Pfam PF00153 Mito_carr x3). [file:human/SLC25A11/SLC25A11-uniprot.txt]

## Core molecular function: 2-oxoglutarate/malate antiporter
- UniProt FUNCTION: "Catalyzes the transport of 2-oxoglutarate (alpha-oxoglutarate) across the inner mitochondrial membrane in an electroneutral exchange for malate (PubMed:25637873, PubMed:38937634). Can also exchange 2-oxoglutarate for other dicarboxylic acids such as malonate, succinate, maleate and oxaloacetate, although with lower affinity (By similarity)." [file:human/SLC25A11/SLC25A11-uniprot.txt]
- CATALYTIC ACTIVITY (Rhea RHEA:71587, experimental, PubMed:25637873): "(S)-malate(in) + 2-oxoglutarate(out) = (S)-malate(out) + 2-oxoglutarate(in)". Additional by-similarity antiport reactions listed for malonate, succinate, maleate, oxaloacetate. [file:human/SLC25A11/SLC25A11-uniprot.txt]
- The transport is an antiporter (obligate exchange), reflected in the UniProt keyword "Antiport". [file:human/SLC25A11/SLC25A11-uniprot.txt]
- Ping-pong (consecutive, not simultaneous) exchange mechanism, monomer: "Substrate exchange across the membrane occurs consecutively with one substrate being transported first, then dissociating from the substrate binding site before the second substrate binds for transport in the opposite direction (PubMed:38937634)." SUBUNIT: "Monomer (PubMed:38937634)." [file:human/SLC25A11/SLC25A11-uniprot.txt]
- Direct experimental characterization of the human protein: OGC (Q02978) expressed in Lactococcus lactis fused-membrane vesicles catalyzes 2-oxoglutarate/[14C]-malate heteroexchange and malate/malate homoexchange, blocked by 2-oxoglutarate, malate, phenylsuccinate and NEM: "Heteroexchange of 2-oxoglutarate for [14C]-malate was quenched by excess of unlabelled 2-oxoglutarate added externally" [PMID:25637873 "Heteroexchange of 2-oxoglutarate for [14C]-malate was quenched by excess of unlabelled 2-oxoglutarate added externally, whereas addition of excess GSH had no effect on transport"]. Same paper shows OGC does NOT transport glutathione (GSH): "these mitochondrial carriers do not transport glutathione". [PMID:25637873]
- Historical description of the same activity: "The oxoglutarate carrier transports 2-oxoglutarate across the inner membranes of mitochondria in an electroneutral exchange for malate or other dicarboxylic acids." [PMID:1457818 abstract]

Chosen core MF term: **GO:0015367 oxoglutarate:malate antiporter activity** (verified via OLS: "oxoglutarate(out) + malate(in) = oxoglutarate(in) + malate(out)"). This is the most specific MF that the EXP evidence (PMID:25637873) supports and is already the EXP-annotated term in GOA. This is a transporter, NOT an enzyme — no catalytic (EC) MF should be assigned.

## Core biological processes
- Malate-aspartate shuttle (MAS): OGC is a required carrier of the MAS. Genetic disruption of OGC in HEK293 impairs the shuttle and serine biosynthesis: "MAS-deficient cells have reduced serine biosynthesis ... oxoglutarate-malate carrier (OGC)- and MDH2-deficient cells are less affected." [PMID:37647199 abstract]. GO term GO:0043490 malate-aspartate shuttle (OLS definition explicitly names "the malate-alpha-ketoglutarate carrier then transports the malate into the mitochondria").
- 2-oxoglutarate / malate transmembrane transport: directly follows from the antiporter activity; UniProt lists participation in "the malate-aspartate shuttle, the oxoglutarate/isocitrate shuttle, gluconeogenesis from lactate, and nitrogen metabolism (By similarity)." [file:human/SLC25A11/SLC25A11-uniprot.txt]
- Reactome pathways: "Malate-aspartate shuttle" (R-HSA-9856872) and "Organic anion transport by SLC5/17/25 transporters" (R-HSA-428643). Reaction entries R-HSA-198440 / R-HSA-376851 describe OGC exchanging malate and 2-oxoglutarate across the inner membrane. [file:human/SLC25A11/SLC25A11-uniprot.txt; reactome/R-HSA-198440.md; reactome/R-HSA-376851.md]

## Localization
- SUBCELLULAR LOCATION: "Mitochondrion inner membrane {ECO:0000250|UniProtKB:P97700}; Multi-pass membrane protein". [file:human/SLC25A11/SLC25A11-uniprot.txt] GO:0005743 mitochondrial inner membrane — the core CC.
- Mitochondrion (GO:0005739) HTP/HDA annotations from proteomics (PMID:34800366 high-confidence mito proteome; PMID:20833797 muscle mito phosphoproteome) are correct but less specific than the inner-membrane term.

## Secondary / by-similarity activities
- Proton transport under uncoupling conditions: "In addition can facilitate proton transport in the presence of protonophores such as long-chain fatty acids, contributing to mitochondrial uncoupling and regulation of mitochondrial energetic efficiency (By similarity)." Proton transporter reaction H(+)(in) = H(+)(out) (RHEA:34979) is by-similarity (ECO:0000250|UniProtKB:Q9CR62, mouse). [file:human/SLC25A11/SLC25A11-uniprot.txt] Supports the ISS/IEA proton transmembrane transporter (GO:0015078) annotations as non-core, by-similarity secondary function.

## Off-target / non-core annotations to flag
- **Nucleus (GO:0005634)** — HDA from a sperm-nucleus proteome (PMID:21630459). SLC25A11 is an integral inner-mitochondrial-membrane carrier; sperm-nucleus preps are notoriously contaminated by residual mitochondria. Non-core; MARK_AS_OVER_ANNOTATED.
- **Plasma membrane (GO:0005886)** — TAS from PMID:1457818, a 1992 gene-sequencing paper whose abstract describes the protein transporting across the inner mitochondrial membrane, not the plasma membrane. Inconsistent with all downstream evidence; the protein is an inner-membrane carrier. MARK_AS_OVER_ANNOTATED (TAS, so not REMOVE).
- **RNA binding (GO:0003723)** — HDA from a global mRNA-interactome capture (PMID:22681889). Not a curated sequence-specific RNA-binding function; typical of large RNA-interactome screens capturing abundant mitochondrial proteins. Non-core; MARK_AS_OVER_ANNOTATED.
- **protein binding (GO:0005515)** IPI annotations — uninformative bare "protein binding"; keep as non-core (never remove IPI). Two references:
  - PMID:32814053 (Y2H neurodegeneration interactome; HTT, CDH1, CALR, DLST, CDK5R1, NEK7, AHCYL1). Many are Y2H hits of unclear physiological relevance for a polytopic inner-membrane carrier.
  - PMID:37009826 (SMIM26/LINC00493 microprotein). UniProt records "Interacts with SMIM26 (PubMed:37009826)" as a genuine interaction. [file:human/SLC25A11/SLC25A11-uniprot.txt] Still bare protein binding → non-core.

## Disease
- Germline loss-of-function variants (E141K, M147V, P239T; all "loss of protein expression") predispose to metastatic paraganglioma/pheochromocytoma (PPGL6, MIM:618464), autosomal dominant. [file:human/SLC25A11/SLC25A11-uniprot.txt; PMID:29431636 title/entry] Establishes a tumour-suppressor-like role but is a disease consequence, not a directly annotatable normal GO function here.

## Modeling note
SLC25A11/OGC is a transporter, not an enzyme; no catalytic (EC) molecular function should be assigned. Its by-similarity proton transporter activity (GO:0015078), relevant only under protonophore/fatty-acid uncoupling conditions, is a secondary, non-core activity.

## Summary of core functions
1. MF: GO:0015367 oxoglutarate:malate antiporter activity (EXP, PMID:25637873).
2. BP: GO:0043490 malate-aspartate shuttle (IMP-supported at MAS level, PMID:37647199) + 2-oxoglutarate/malate transmembrane transport.
3. CC: GO:0005743 mitochondrial inner membrane.
</content>
</invoke>
