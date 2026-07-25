# ACLY (ATP-citrate synthase / ATP-citrate lyase) — review notes

UniProt: P53396 (ACLY_HUMAN), 1101 aa, Homo sapiens (9606). HGNC:115.

## Identity and catalytic function

ACLY is the cytosolic homotetrameric enzyme that produces the acetyl-CoA used
for de novo lipogenesis, cholesterol synthesis and protein acetylation. Citrate
exported from mitochondria is cleaved in the cytosol.

- RecName in UniProt: "ATP-citrate synthase"; AltName "ATP-citrate (pro-S-)-lyase";
  "Citrate cleavage enzyme"; EC 2.3.3.8
  [file:human/ACLY/ACLY-uniprot.txt "RecName: Full=ATP-citrate synthase"].
- CATALYTIC ACTIVITY (UniProt / Rhea RHEA:21160): "oxaloacetate + acetyl-CoA + ADP +
  phosphate = citrate + ATP + CoA"; physiological direction right-to-left (i.e.
  citrate + ATP + CoA -> acetyl-CoA + oxaloacetate + ADP + Pi)
  [file:human/ACLY/ACLY-uniprot.txt "Reaction=oxaloacetate + acetyl-CoA + ADP +"].
- FUNCTION: "Catalyzes the cleavage of citrate into oxaloacetate and acetyl-CoA, the
  latter serving as common substrate in multiple biochemical reactions in protein,
  carbohydrate and lipid metabolism."
  [file:human/ACLY/ACLY-uniprot.txt "Catalyzes the cleavage of citrate into oxaloacetate and"].
- COFACTOR: Mg(2+) [file:human/ACLY/ACLY-uniprot.txt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420"].
- SUBUNIT: Homotetramer [file:human/ACLY/ACLY-uniprot.txt "SUBUNIT: Homotetramer."].
- SUBCELLULAR LOCATION: Cytoplasm, cytosol
  [file:human/ACLY/ACLY-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm, cytosol"].
- Active site His-760, tele-phosphohistidine intermediate; the H760A mutant has reduced
  activity [file:human/ACLY/ACLY-uniprot.txt "Tele-phosphohistidine intermediate"].

## Supporting literature (all cached)

- **PMID:1371749** (Elshourbagy 1992, abstract-only): cloning/expression of human ACLY
  cDNA; enzymatically active recombinant enzyme; His->Ala mutagenesis of the catalytic
  histidine "diminishes the catalytic activity of the expressed ATP-citrate lyase
  protein" [PMID:1371749 "Site-specific mutagenesis of His765----Ala diminishes the catalytic activity of the expressed"].
  Note the paper numbers the catalytic His as 765 (its 1105-aa numbering); UniProt maps
  the active-site His to residue 760. This is the primary source for the BHF-UCL
  experimental annotations (MF, acetyl-CoA/citrate/oxaloacetate metabolism, ATP binding).
- **PMID:9116495** (Lord 1997, abstract-only): "ATP:citrate lyase (ACL) is a major
  generator of cytosolic acetyl-coenzymeA, which is required for both fatty acid and
  cholesterol biosynthesis"; purified recombinant enzyme "observed to exist as a
  tetramer by gel filtration chromatography"
  [PMID:9116495 "ATP:citrate lyase (ACL) is a major generator of cytosolic acetyl-coenzymeA"].
- **PMID:10653665** (Potapova 2000, abstract-only): kinetic characterization;
  phosphorylation by PKA increases Vmax 6-fold and abolishes homotropic allosteric
  regulation by citrate; fructose 6-phosphate is a potent activator. Supports catalytic
  activity and allosteric/covalent regulation.
- **PMID:19286649** (Ma 2009, abstract-only): direct homogeneous assay; "ATP citrate
  lyase (ACL) is a cytosolic enzyme that catalyzes the synthesis of acetyl-CoA and
  oxaloacetate using citrate, CoA, and ATP as substrates and Mg(2+) as a necessary
  cofactor"; "The ACL-dependent synthesis of acetyl-CoA is thought to be an essential
  step for the de novo synthesis of fatty acids and cholesterol"
  [PMID:19286649 "The ACL-dependent synthesis of acetyl-CoA is thought to be an essential"].
- **PMID:23932781** (Lin 2013, abstract-only): ACLY acetylated at K540/K546/K554 by
  PCAF under high glucose; acetylation blocks ubiquitylation, stabilizes ACLY and
  "promotes de novo lipid synthesis, cell proliferation, and tumor growth"; SIRT2
  deacetylates/destabilizes. Source of the lipid-biosynthesis IDA and PTM annotations.
- **PMID:31873304** (Wei 2020, full text): cryo-EM of human ACLY. "ATP-citrate lyase
  (ACLY) synthesizes cytosolic acetyl coenzyme A (acetyl-CoA), a fundamental cellular
  building block"; "ACLY forms a homotetramer with a rigid citrate synthesis homology
  (CSH) module, flanked by four flexible acetyl-CoA synthetase homology (ASH) domains".
  ComplexPortal used this to annotate GO:0140615 (ATP-dependent citrate lyase complex)
  and coenzyme A metabolic process.
- **PMID:39881208** (Li 2025, full text): SLC25A1-ACLY axis maintains cytosolic
  acetyl-CoA. "In the cytosol, ATP citrate lyase (ACLY) converts citrate into
  oxaloacetate and acetyl-CoA"; "ACLY knockdown heightened cell susceptibility to RSL3-
  and erastin-induced ferroptosis"; "SLC25A1 and ACLY suppress ferroptosis through the
  breakdown of citrate to produce acetyl-CoA". Source of the acetyl-CoA IMP and negative
  regulation of ferroptosis IMP annotations.

## Curation reasoning summary

- **Core MF**: ATP citrate synthase activity (GO:0003878). Multiple IDA (PMID:9116495,
  10653665, 19286649, 1371749) plus IBA/IEA all converge; ACCEPT the experimental
  instances, ACCEPT the redundant IBA/IEA of the gene's own MF.
- **ATP binding (GO:0005524)**: genuine — ATP is a substrate, ATP-grasp domain, many
  BINDING residues to ATP. TAS (PMID:1371749) ACCEPT.
- **Core BP**: acetyl-CoA biosynthetic process (GO:0006085), citrate metabolic process
  (GO:0006101), oxaloacetate metabolic process (GO:0006107), coenzyme A metabolic
  process (GO:0015936) — all direct products/substrates of the reaction. fatty acid
  biosynthetic process (GO:0006633) and cholesterol biosynthetic process (GO:0006695) —
  downstream pathways ACLY feeds; core to the gene's physiological role, keep. lipid
  biosynthetic process (GO:0008610) is the general parent of FA/cholesterol biosynthesis;
  keep as non-core (more specific children are annotated).
- **negative regulation of ferroptosis (GO:0110076)**: IMP PMID:39881208; genuine but
  a downstream, context-specific (cancer-cell) consequence of acetyl-CoA supply →
  KEEP_AS_NON_CORE.
- **CC cytosol (GO:0005829)**: correct primary location; multiple IDA/TAS/IBA/IEA — ACCEPT.
- **ATP-dependent citrate lyase complex (GO:0140615)**: the homotetramer; part_of IPI
  (ComplexPortal, PMID:31873304) — ACCEPT.
- **Over-/mis-localizations**: extracellular region, azurophil/ficolin granule lumen
  (Reactome neutrophil-degranulation), extracellular exosome (HDA), membrane (HDA) —
  these are secretome/proteomics/degranulation captures of an abundant cytosolic enzyme,
  not sites of function → MARK_AS_OVER_ANNOTATED (per policy: do not REMOVE the HDA/TAS,
  they are legitimate localization detections, just not functional locations).
- **Generic IEA MF/BP**: catalytic activity (GO:0003824) and "acyltransferase activity,
  acyl groups converted into alkyl on transfer" (GO:0046912) and acyl-CoA metabolic
  process (GO:0006637) are uninformative/imprecise electronic parents → these are
  InterPro/ARBA over-generalizations. catalytic activity → MARK_AS_OVER_ANNOTATED
  (redundant with specific MF); GO:0046912 is arguably the wrong specific MF label for
  the citrate-lyase reaction → MARK_AS_OVER_ANNOTATED. acyl-CoA metabolic process is a
  reasonable parent but redundant/imprecise → KEEP_AS_NON_CORE.
- **protein binding (GO:0005515) IPI x3** (PMID:23932781, with Q5T4S7 UBR4-ish, Q8IXJ6
  BAP1, Q92831 PCAF/KAT2B): bare protein binding, uninformative → MARK_AS_OVER_ANNOTATED
  (policy forbids REMOVE for IPI protein binding).
