---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:29:06.807835'
end_time: '2026-10-26T00:36:58.419613'
duration_seconds: 471.61
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: PARD3B
  gene_symbol: PARD3B
  uniprot_accession: A0A9L0JEY6
  protein_description: 'RecName: Full=Partitioning defective 3 homolog B {ECO:0000256|ARBA:ARBA00071372};
    AltName: Full=PAR3-beta {ECO:0000256|ARBA:ARBA00080501}; AltName: Full=Partitioning
    defective 3-like protein {ECO:0000256|ARBA:ARBA00080550};'
  gene_info: Name=PARD3B {ECO:0000313|Ensembl:ENSEASP00005051886.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the PAR3 family.
  protein_domains: PAR3. (IPR052213); Par3/HAL_N. (IPR021922); PDZ. (IPR001478); PDZ_sf.
    (IPR036034); Par3_HAL_N_term (PF12053)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3302
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 57
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JEY6
- **Protein Description:** RecName: Full=Partitioning defective 3 homolog B {ECO:0000256|ARBA:ARBA00071372}; AltName: Full=PAR3-beta {ECO:0000256|ARBA:ARBA00080501}; AltName: Full=Partitioning defective 3-like protein {ECO:0000256|ARBA:ARBA00080550};
- **Gene Information:** Name=PARD3B {ECO:0000313|Ensembl:ENSEASP00005051886.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the PAR3 family.
- **Key Domains:** PAR3. (IPR052213); Par3/HAL_N. (IPR021922); PDZ. (IPR001478); PDZ_sf. (IPR036034); Par3_HAL_N_term (PF12053)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PARD3B" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PARD3B' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PARD3B** (gene ID: PARD3B, UniProt: A0A9L0JEY6) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PARD3B (Partitioning defective 3 homolog B, PAR3β / Par3L) in the donkey, *Equus asinus* (UniProt A0A9L0JEY6)

## 1. Introduction and summary

The donkey protein A0A9L0JEY6 comes from the chromosome-level donkey reference genome, which was assembled from a male Dezhou donkey [wang-2020-donkey-genome-abstract]. It is an unreviewed TrEMBL entry of 1,204 residues, encoded on chromosome 4 by the Ensembl gene ENSEASG00005002870. Its name, PARD3B ("Partitioning defective 3 homolog B"), and all of its functional annotations come from automatic rules (ARBA) and from phylogenetic transfer (TreeGrafter/PANTHER PTHR16484:SF4). No experiment has been done on this donkey protein [uniprot-A0A9L0JEY6-entry]. The identity check still comes out clean. The gene symbol, protein name, PAR3-family membership and domain set (an N-terminal Par3/HAL_N region, three PDZ domains, and long disordered C-terminal stretches) all agree with each other. A global alignment shows about 88% identity with the canonical human PARD3B isoform (Q8TEW8; 1,205 aa). Identity rises to 95–99% across the N-terminal oligomerization region, the three PDZ domains, and the short PDZ2–PDZ3 linker that is known to bind LKB1 (see [SEQUENCE_ANALYSIS.md](SEQUENCE_ANALYSIS.md)). The symbol is not ambiguous here. The literature describes this one gene under three names: PAR3β, Par3L (Par3-like) and PARD3B [kohjima-2002-par3beta-abstract; gao-2002-par3l-splice-abstract; thompson-2022-par3-family-review-abstract]. No paper addresses the equine gene, so everything below is inferred from orthologs, mainly human and mouse, and from the wider Par-3 family.

The core finding is that PARD3B is a non-catalytic, multi-PDZ scaffold or adaptor of the Par-3/Bazooka family. Its biology has split away from that of its paralog PARD3. Classical PAR3 binds PAR6 and atypical PKC (aPKC) and builds the apical PAR polarity complex. PARD3B cannot bind either PAR6 or aPKC [kohjima-2002-par3beta-abstract], and the reason is that the motifs that let PARD3 engage aPKC are mutated in PARD3B [thompson-2022-par3-family-review-fulltext]. Even so, PARD3B goes to epithelial cell–cell junctions. Human PAR3β co-localizes with ZO-1 at tight junctions [kohjima-2002-par3beta-abstract; gao-2002-par3l-splice-abstract]. In tissues, PARD3B lies laterally, together with E-cadherin and Src, at adherens-junction-rich membranes of columnar epithelia and in the basal stem-cell layer of stratified epithelia [thompson-2022-par3-family-review-fulltext]. The clearest molecular function shown so far is signal regulation, not polarity. Par3L binds the master kinase LKB1 (STK11) through a short sequence unique to Par3L that lies between PDZ2 and PDZ3. In doing so it inhibits LKB1 kinase activity and lowers phosphorylation of AMPK. This restraint is needed to keep mouse mammary stem cells alive [huo-2014-par3l-mammary-abstract; huo-2014-par3l-mammary-fulltext], and the same mechanism supports survival of colorectal cancer cells [li-2017-par3l-lkb1-abstract]. Other experimentally supported partners and processes are phosphorylation-dependent binding of 14-3-3 [izaki-2005-par3beta-1433-abstract], binding to the spindle-orientation adaptor Inscuteable [izaki-2006-insc-lgn-abstract], lumen formation in 3D epithelial cysts [wang-2021-proximity-lumen-abstract], mitotic spindle fidelity and tumour suppression in the gut, as shown with knockout mice [zhang-2026-par3l-chromosome-abstract], and upkeep of the kidney filtration barrier. In podocytes, PARD3B is the main Par-3 paralog, and it works there redundantly with PARD3 but without needing Par6 [koehler-2016-par3a-kidney-abstract; koehler-2022-par3a-par3b-podocyte-abstract].

## 2. Identity, gene structure and domain architecture

The donkey entry carries the InterPro signatures PAR3 (IPR052213), Par3/HAL_N (IPR021922; Pfam PF12053) and PDZ (IPR001478/IPR036034). PROSITE places three PDZ domains at residues 198–286, 380–453 and 495–570. MobiDB-lite predicts long disordered, compositionally biased regions between residues 600 and 1204 [uniprot-A0A9L0JEY6-entry]. This is the standard Par-3 family layout. Thompson's review describes family members as having an N-terminal PB1-like head-to-tail oligomerization domain (conserved region 1, CR1), three PDZ domains, a membrane-lipid-associating region, and a C-terminal low-complexity "coiled-coil" region that may act as an intrinsically disordered region [thompson-2022-par3-family-review-fulltext]. Human PAR3β was first cloned as a 1,205-amino-acid protein with three PDZ domains and a region homologous to the aPKC-binding domain of PAR3α [kohjima-2002-par3beta-abstract]. Gao and colleagues found human Par3L independently and showed that both Par3 and Par3L are expressed as many alternatively spliced variants [gao-2002-par3l-splice-abstract]. UniProt lists six human isoforms [uniprot-Q8TEW8-entry]. The donkey sequence is almost the same length as the human canonical isoform, and its alignment has only five gap positions. This suggests that the Ensembl model corresponds to the isoform-1-like transcript, though other donkey isoforms surely exist and have not yet been annotated.

Vertebrates have two Par-3/Baz paralogs, PARD3 (PAR-3) and PARD3B (PAR-3-like). Drosophila has a single gene, *bazooka*, and lacks a Par3L-type gene [thompson-2022-par3-family-review-abstract; huo-2014-par3l-mammary-fulltext]. Thompson notes that the split into an apical PARD3 and a junctional PARD3B happened at about the same time as stratified squamous epithelia appeared in vertebrates [thompson-2022-par3-family-review-abstract]. Equids are eutherian mammals, and PANTHER places the donkey protein in the PARD3B subfamily [uniprot-A0A9L0JEY6-entry]. So the donkey gene is the ortholog of human and mouse PARD3B, not of PARD3.

## 3. Loss of PAR6/aPKC binding: a divergent Par-3 paralog

The most important biochemical feature of PARD3B is what it cannot do. Kohjima and colleagues showed that human PAR3β, unlike other PAR3 proteins, binds none of the PAR6 or aPKC isotypes, even though it has a region resembling the aPKC-binding domain and a first PDZ domain like the one in PAR3α that engages PAR6 [kohjima-2002-par3beta-abstract]. Gao and colleagues reported that no Par3L isoform detectably binds aPKC. Some Par3L splice isoforms did show differential binding to Par6 [gao-2002-par3l-splice-abstract], and UniProt's "Interacts with PARD6B" annotation comes from that observation [uniprot-Q8TEW8-entry]. The structural reason is now understood. In PARD3, conserved Phe-X-Arg (FXR) and Lys-Arg (KR) motifs on either side of Ser827 insert into the aPKC kinase domain. In vertebrate PARD3B, both motifs are mutated [thompson-2022-par3-family-review-fulltext]. Huo and Macara therefore described Par3L's function as "enigmatic", because it binds neither Par6 nor aPKC [huo-2014-par3l-mammary-fulltext]. They concluded that the classical apical jobs of PARD3, which are recruiting Cdc42–Par6–aPKC and polarizing exocyst-dependent trafficking, appear not to be shared by PARD3B [thompson-2022-par3-family-review-fulltext].

Later proximity proteomics made this simple picture more complicated. In BioID experiments with PAR6B as bait in Caco-2 cells grown as 3D cysts, PARD3B turned up in PAR6B proximity, and was enriched more than fivefold in 3D compared with 2D culture. PARD3B co-localized with PAR6B at junctions in 2D culture and at the apical membrane in 3D. Endogenous PARD3B still did not co-immunoprecipitate with PARD6 or PARD3, which suggests that any PARD3B-containing polarity complex is weak or transient [wang-2021-proximity-lumen-fulltext]. The most defensible statement for annotation is that PARD3B does not form the stable PAR3–PAR6–aPKC ternary complex. A weak or context-dependent association with PAR6B remains possible.

In vivo genetics in the kidney now support the conclusion that PARD3B works independently of Par6 and aPKC. Koehler and colleagues deleted *Pard3a*, *Pard3b* or both in mouse podocytes. Only loss of both genes caused severe glomerular disease, so the two paralogs are highly redundant. In rescue experiments in *Drosophila* nephrocytes depleted of Bazooka, Par3A acted through aPKC–Par6, whereas Par3B function did not depend on Par6. Loss of both Par3A and Par3B raised levels of the actin-associated protein synaptopodin. The authors concluded that Par3A acts through aPKC–Par6 and RhoA-GTP, while Par3B uses Par6-independent functions that affect synaptopodin localization. Both paralogs thus link polarity signalling to actin regulators [koehler-2022-par3a-par3b-podocyte-abstract]. This is the clearest organism-level evidence that PARD3B is a working polarity scaffold in its own right and not merely a weaker copy of PARD3.

## 4. Subcellular localization: tight junctions, lateral membranes and adherens junctions

Several lines of experimental evidence put PARD3B at epithelial cell–cell contacts. Both endogenous and exogenous human PAR3β localize to tight junctions, which shows that tight-junction targeting does not need the ternary complex [kohjima-2002-par3beta-abstract]. Every Par3L isoform tested associated with tight junctions in epithelial cells [gao-2002-par3l-splice-abstract]. UniProt's curated human entry records the protein at the endomembrane system, partly along the cell–cell contact region, and co-localized with TJP1 (ZO-1) at epithelial tight junctions [uniprot-Q8TEW8-entry]. The donkey entry inherits these terms through ARBA rules: Cell junction, tight junction, and Endomembrane system [uniprot-A0A9L0JEY6-entry]. Localization does not depend on 14-3-3 binding, since S746A Par3β mutants still reach tight junctions in MDCK cells and Rac-induced ruffles in HeLa cells [izaki-2005-par3beta-1433-abstract].

Tissue immunostaining refines the picture. Across many monolayered columnar epithelia, PARD3 is always apical and overlaps CRB3, whereas PARD3B is always lateral and overlaps E-cadherin and Src. In stratified epithelia such as skin, prostate, epididymis and bronchus, PARD3B and Src are confined to basal-layer cells. These cells lack PARD3 and typical apical proteins, and in them PARD3B lies with adherens junctions around the whole plasma membrane [thompson-2022-par3-family-review-fulltext]. Thompson concludes that vertebrate PARD3B is "strictly junctional in many epithelia" [thompson-2022-par3-family-review-abstract]. In mouse intestine, Par3L localizes to the junctions of crypt cells [zhang-2026-par3l-chromosome-fulltext]. Kidney podocytes are a specialized non-epithelial-sheet setting. There, *Pard3b*, not *Pard3a*, is the dominant Par-3 gene expressed, and the protein sits at the base of the slit diaphragm, partly co-localizing with podocin [koehler-2016-par3a-kidney-abstract]. The slit diaphragm is a modified cell–cell junction, so this finding fits the general picture of PARD3B as a junction-associated scaffold. The best-supported localization for the donkey protein is therefore the cytoplasmic face of epithelial lateral cell–cell junctions: adherens and tight junctions, and the cell cortex. It may also sit on endomembranes. Membrane association probably also uses the phosphoinositide-binding ability of Par-3 family PDZ domains, which was shown for PARD3 PDZ2 [wu-2007-par3-pdz-pi-abstract]. Whether the corresponding PARD3B domain binds lipids has not been tested directly. The "phosphatidylinositol binding" GO term on the donkey entry is a TreeGrafter inference [uniprot-A0A9L0JEY6-entry].

## 5. Primary molecular function: a scaffold that restrains LKB1–AMPK signalling

The most rigorous mechanistic study of PARD3B is the work of Huo and Macara on mouse mammary gland. Par3, although needed for mammary morphogenesis, is not essential for mammary stem-cell function. Par3L, by contrast, is expressed by multipotent stem (cap) cells of the terminal end buds, and ablating it causes rapid and profound loss of stem cells [huo-2014-par3l-mammary-abstract]. Looking for a partner, the authors found that Par3L, but not Par3, binds LKB1, the mammalian homolog of the *C. elegans* polarity kinase PAR-4. Mapping showed that binding needs PDZ2 and PDZ3 together with the intervening sequence. LKB1 does not bind any single isolated PDZ domain. The key determinant is a short linker between PDZ2 and PDZ3 that has no similarity to Par3 or to any other sequence in GenBank. Swapping this linker for the Par3 sequence abolished LKB1 binding, and that mutant could not rescue ductal outgrowth [huo-2014-par3l-mammary-fulltext]. Functionally, wild-type Par3L suppressed AMPK phosphorylation in HEK293T cells without changing LKB1 or AMPK levels, while the binding mutant had much less effect. Co-expressing LKB1 with its activator STRADα strongly suppressed stem-cell colony outgrowth and raised apoptosis. The authors concluded that Par3L maintains stem cells by suppressing LKB1 kinase activity [huo-2014-par3l-mammary-fulltext]. Li and colleagues extended this to human colorectal cancer cells. CRISPR knockout of Par3L reduced proliferation, activated caspase-3 and increased sensitivity to chemotherapy and irradiation. It also caused abnormal activation of LKB1/AMPK, and LKB1 knockdown partly rescued the cell death [li-2017-par3l-lkb1-abstract].

For annotation, the main molecular function of PARD3B is therefore a non-enzymatic scaffold or adaptor that negatively regulates a protein kinase, specifically LKB1/STK11 and through it AMPK. It is not an enzyme and has no transporter activity. In the donkey sequence, the LKB1-binding PDZ2–PDZ3 linker is nearly identical to the human one (38 of 41 residues; [SEQUENCE_ANALYSIS.md](SEQUENCE_ANALYSIS.md)), which strongly supports the idea that the donkey protein keeps this activity. Thompson's review places this finding in context. PARD3B co-localizes with Src at junctions, and Src kinases have also been proposed to antagonize LKB1, so PARD3B may couple E-cadherin–Src signalling at adherens junctions to the restraint of LKB1 [thompson-2022-par3-family-review-fulltext]. That idea remains a hypothesis.

## 6. Other interactions and processes: 14-3-3, Inscuteable, spindles and lumens

Beyond LKB1, a few direct interactions have been shown in low-throughput studies. Par3β binds 14-3-3 proteins in a phosphorylation-dependent way, and Ser746 is essential for binding. Because Ser746Ala mutants still localize normally, 14-3-3 binding probably controls something other than targeting [izaki-2005-par3beta-1433-abstract]. This serine and its surrounding sequence are conserved in the donkey protein, as Ser743 ([SEQUENCE_ANALYSIS.md](SEQUENCE_ANALYSIS.md)). Human Inscuteable (INSC) binds both Par3 and Par3β as well as the Pins homologs LGN and AGS3. INSC acts as an adaptor that bridges Par3 to LGN [izaki-2006-insc-lgn-abstract]. This link to the LGN–NuMA spindle-orientation machinery is the basis for the "asymmetrical cell division" wording in the UniProt function statement [uniprot-Q8TEW8-entry]. Large-scale binary interaction screens also report many PDZ-type partners, including TJP2/ZO-2, PTEN and FZD7 [uniprot-Q8TEW8-entry]. These high-throughput results need confirmation and are not used here as primary evidence.

Genetic and cell-biological studies tie PARD3B to epithelial morphogenesis and to genome stability. In 3D Caco-2 cysts, two independent shRNAs against PARD3B produced cysts with several small lumens instead of a single large one. This shows that PARD3B is required for normal lumen formation [wang-2021-proximity-lumen-fulltext]. The N-terminal region of Par3L, like that of Par3, disrupts tight-junction formation when overexpressed in MDCK cells [gao-2002-par3l-splice-abstract]. This mirrors the dominant-negative effect of the self-associating PAR-3 CR1 domain [mizuno-2003-par3-selfassoc-abstract], and suggests that PARD3B also forms CR1-mediated oligomers. The structural basis is known for PARD3. Its N-terminal domain adopts a PB1-like fold and polymerizes into helical filaments through front-to-back contacts, and this oligomerization alone accounts for the domain's role in targeting Par-3 to the membrane in MDCK cells [feng-2007-par3-ntd-pb1-abstract]. The corresponding Par3_HAL_N region of donkey PARD3B is 85 of 90 residues identical to human PARD3B ([SEQUENCE_ANALYSIS.md](SEQUENCE_ANALYSIS.md)), but its oligomerization has not been tested directly. Germline *Pard3b* knockout mice develop gastrointestinal adenomas from three months of age, as well as prostate hyperplasia and lung tumours, and they show delayed mammary development. Their intestinal epithelium has more mitotic cells with a much higher fraction of aberrant spindles. Proteomics on endogenously FLAG-tagged Par3L found partners involved in chromatin remodelling, spindle assembly, cytoskeleton and extracellular matrix, trafficking, metabolism and mRNA processing [zhang-2026-par3l-chromosome-abstract; zhang-2026-par3l-chromosome-fulltext]. Taken together, these data suggest a role for junctional PARD3B in symmetric, planar divisions of epithelial progenitors. Thompson had proposed this before the knockout data appeared [thompson-2022-par3-family-review-fulltext].

## 7. Regulation, disease associations and pleiotropic phenotypes

Most of the remaining literature is correlative and says little about the primary function, so it is summarized only briefly. A GWAS found PARD3B variants associated with slower progression to AIDS. One SNP is a predicted exonic splicing enhancer that alters PARD3B splice-isoform profiles in B-cell lines [troyer-2011-pard3b-aids-abstract]. PARD3B transcription responds to the androgen receptor in glioblastoma cells [yang-2022-pard3b-gbm-abstract]. In SWI/SNF-deficient cancers, a PARD3B enhancer is held repressed by CHD3/NuRD, and derepressed PARD3B kills the cells [takeuchi-2026-chd3-pard3b-abstract]. Overexpressing Par3L in macrophages promotes M1 polarization through NF-κB p65 and ERK [huang-2024-par3l-macrophage-abstract]. In endothelial cells, depleting eNOS raises PARD3B expression along with that of other polarity genes, and the cells become more polarized during sprouting angiogenesis [smith-2021-enos-polarity-abstract]. These studies show that PARD3B levels are tightly regulated and that too much of it can be toxic. Its loss can promote tumours, as the knockout mice show [zhang-2026-par3l-chromosome-abstract], and it can also support tumour-cell survival [li-2017-par3l-lkb1-abstract]. This two-sided behaviour fits a scaffold that tunes kinase signalling, such as LKB1–AMPK, rather than one that switches a pathway on or off. None of these phenotypes has been studied in equids. The donkey genome paper does not discuss PARD3B [wang-2020-donkey-genome-abstract].

## 8. Synthesis for functional annotation of A0A9L0JEY6

Based on orthology and the high sequence conservation of every functional module, the donkey protein is best annotated as follows. It is a non-catalytic, PDZ-domain scaffold or adaptor of the Par-3 family. It localizes to epithelial cell–cell junctions (bicellular tight junctions and lateral adherens-junction membranes, at the cell cortex) and to endomembranes [kohjima-2002-par3beta-abstract; thompson-2022-par3-family-review-fulltext]. Its best-supported molecular activity is binding LKB1/STK11 and inhibiting its kinase activity, which negatively regulates LKB1–AMPK signalling and so supports stem-cell and progenitor survival [huo-2014-par3l-mammary-fulltext; li-2017-par3l-lkb1-abstract]. Further experimentally supported functions are phosphorylation-dependent binding of 14-3-3 [izaki-2005-par3beta-1433-abstract] and binding of INSC [izaki-2006-insc-lgn-abstract], together with roles in epithelial lumen formation [wang-2021-proximity-lumen-fulltext] mitotic spindle fidelity [zhang-2026-par3l-chromosome-fulltext], and maintenance of the podocyte architecture and filtration barrier. In podocytes the protein sits at the base of the slit diaphragm and acts redundantly with PARD3, independently of Par6 [koehler-2016-par3a-kidney-abstract; koehler-2022-par3a-par3b-podocyte-abstract]. Annotators should not transfer PARD3-specific functions, such as binding aPKC or the PAR6–aPKC complex, apical recruitment of Cdc42–Par6–aPKC, or PTEN binding by PDZ3, without evidence specific to PARD3B [kohjima-2002-par3beta-abstract; thompson-2022-par3-family-review-fulltext; feng-2008-par3-pten-abstract]. The TreeGrafter GO terms on the donkey entry, such as "apical plasma membrane", "establishment of centrosome localization" and "phosphatidylinositol binding", are inherited at the PTHR16484 family level and may partly reflect PARD3 biology [uniprot-A0A9L0JEY6-entry].

## Open Questions

Several questions remain unresolved and would be worth pursuing. First, nobody has tested the equine protein: localization, the LKB1 interaction and the splice-isoform repertoire in donkey or horse tissues are all unknown, and the current Ensembl model may represent only one isoform. Second, the structural basis of LKB1 inhibition is undefined. It is unknown whether the PDZ2–PDZ3 linker blocks the LKB1–STRAD–MO25 complex, competes with substrates, or sequesters LKB1 at junctions. A co-crystal structure or AlphaFold-multimer modelling of this interface would help. Third, it is unclear whether the PARD3B PDZ2 domain binds phosphoinositides as PARD3 PDZ2 does [wu-2007-par3-pdz-pi-abstract], and whether the N-terminal CR1 oligomerizes into PB1-like filaments as in PARD3 [mizuno-2003-par3-selfassoc-abstract; feng-2007-par3-ntd-pb1-abstract]. It is also unknown how PARD3B controls synaptopodin localization in podocytes, and whether it has a role in equine kidney disease [koehler-2022-par3a-par3b-podocyte-abstract]. These features would explain how PARD3B targets membranes independently of aPKC. Fourth, the conflicting data on PAR6B association [gao-2002-par3l-splice-abstract; kohjima-2002-par3beta-abstract; wang-2021-proximity-lumen-fulltext] need to be resolved with quantitative binding assays for each isoform. Fifth, the role of 14-3-3 binding at Ser746 and the kinase that phosphorylates this site remain unknown [izaki-2005-par3beta-1433-abstract]. Sixth, the mechanism linking PARD3B to spindle fidelity and tumour suppression in the gut, and its possible coupling to E-cadherin–Src signalling [thompson-2022-par3-family-review-fulltext; zhang-2026-par3l-chromosome-fulltext], deserves tissue-specific knockout studies. Finally, the genetic association with AIDS progression [troyer-2011-pard3b-aids-abstract] has no mechanistic explanation, and the function of PARD3B in immune cells is almost unexplored.

## References

* **wang-2020-donkey-genome**: Wang C, Li H, Guo Y, et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun* 11:6014. PMID: [33293529](https://pubmed.ncbi.nlm.nih.gov/33293529/); DOI: [10.1038/s41467-020-19813-7](https://doi.org/10.1038/s41467-020-19813-7); PMCID: PMC7723042
* **kohjima-2002-par3beta**: Kohjima M, Noda Y, Takeya R, et al. (2002). PAR3beta, a novel homologue of the cell polarity protein PAR3, localizes to tight junctions. *Biochem Biophys Res Commun* 299:641-6. PMID: [12459187](https://pubmed.ncbi.nlm.nih.gov/12459187/); DOI: [10.1016/s0006-291x(02)02698-0](https://doi.org/10.1016/s0006-291x(02)02698-0)
* **gao-2002-par3l-splice**: Gao L, Macara IG, Joberty G (2002). Multiple splice variants of Par3 and of a novel related gene, Par3L, produce proteins with different binding properties. *Gene* 294:99-107. PMID: [12234671](https://pubmed.ncbi.nlm.nih.gov/12234671/); DOI: [10.1016/s0378-1119(02)00681-9](https://doi.org/10.1016/s0378-1119(02)00681-9)
* **izaki-2005-par3beta-1433**: Izaki T, Kamakura S, Kohjima M, Sumimoto H (2005). Phosphorylation-dependent binding of 14-3-3 to Par3beta, a human Par3-related cell polarity protein. *Biochem Biophys Res Commun* 329:211-8. PMID: [15721295](https://pubmed.ncbi.nlm.nih.gov/15721295/); DOI: [10.1016/j.bbrc.2005.01.115](https://doi.org/10.1016/j.bbrc.2005.01.115)
* **izaki-2006-insc-lgn**: Izaki T, Kamakura S, Kohjima M, Sumimoto H (2006). Two forms of human Inscuteable-related protein that links Par3 to the Pins homologues LGN and AGS3. *Biochem Biophys Res Commun* 341:1001-6. PMID: [16458856](https://pubmed.ncbi.nlm.nih.gov/16458856/); DOI: [10.1016/j.bbrc.2006.01.050](https://doi.org/10.1016/j.bbrc.2006.01.050)
* **huo-2014-par3l-mammary**: Huo Y, Macara IG (2014). The Par3-like polarity protein Par3L is essential for mammary stem cell maintenance. *Nat Cell Biol* 16:529-37. PMID: [24859006](https://pubmed.ncbi.nlm.nih.gov/24859006/); DOI: [10.1038/ncb2969](https://doi.org/10.1038/ncb2969); PMCID: PMC4083567
* **li-2017-par3l-lkb1**: Li T, Liu D, Lei X, Jiang Q (2017). Par3L enhances colorectal cancer cell survival by inhibiting Lkb1/AMPK signaling pathway. *Biochem Biophys Res Commun* 482:1037-1041. PMID: [27908725](https://pubmed.ncbi.nlm.nih.gov/27908725/); DOI: [10.1016/j.bbrc.2016.11.154](https://doi.org/10.1016/j.bbrc.2016.11.154)
* **thompson-2022-par3-family-review**: Thompson BJ (2022). Par-3 family proteins in cell polarity & adhesion. *FEBS J* 289:596-613. PMID: [33565714](https://pubmed.ncbi.nlm.nih.gov/33565714/); DOI: [10.1111/febs.15754](https://doi.org/10.1111/febs.15754); PMCID: PMC9290619
* **wang-2021-proximity-lumen**: Wang LT, Proulx MÈ, Kim AD, et al. (2021). A proximity proteomics screen in three-dimensional spheroid cultures identifies novel regulators of lumen formation. *Sci Rep* 11:22807. PMID: [34815476](https://pubmed.ncbi.nlm.nih.gov/34815476/); DOI: [10.1038/s41598-021-02178-2](https://doi.org/10.1038/s41598-021-02178-2); PMCID: PMC8610992
* **zhang-2026-par3l-chromosome**: Zhang W, Dai F, Hong Y, et al. (2026). Polarity protein Par3L deletion causes chromosomal segregation defects and tumorigenesis. *J Biol Chem* 302:110966. PMID: [41274508](https://pubmed.ncbi.nlm.nih.gov/41274508/); DOI: [10.1016/j.jbc.2025.110966](https://doi.org/10.1016/j.jbc.2025.110966); PMCID: PMC12767855
* **mizuno-2003-par3-selfassoc**: Mizuno K, Suzuki A, Hirose T, et al. (2003). Self-association of PAR-3-mediated by the conserved N-terminal domain contributes to the development of epithelial tight junctions. *J Biol Chem* 278:31240-50. PMID: [12756256](https://pubmed.ncbi.nlm.nih.gov/12756256/); DOI: [10.1074/jbc.M303593200](https://doi.org/10.1074/jbc.M303593200)
* **wu-2007-par3-pdz-pi**: Wu H, Feng W, Chen J, et al. (2007). PDZ domains of Par-3 as potential phosphoinositide signaling integrators. *Mol Cell* 28:886-98. PMID: [18082612](https://pubmed.ncbi.nlm.nih.gov/18082612/); DOI: [10.1016/j.molcel.2007.10.028](https://doi.org/10.1016/j.molcel.2007.10.028)
* **feng-2008-par3-pten**: Feng W, Wu H, Chan LN, Zhang M (2008). Par-3-mediated junctional localization of the lipid phosphatase PTEN is required for cell polarity establishment. *J Biol Chem* 283:23440-9. PMID: [18550519](https://pubmed.ncbi.nlm.nih.gov/18550519/); DOI: [10.1074/jbc.M802482200](https://doi.org/10.1074/jbc.M802482200)
* **ohno-2001-par-apkc-review**: Ohno S (2001). Intercellular junctions and cellular polarity: the PAR-aPKC complex, a conserved core cassette playing fundamental roles in cell polarity. *Curr Opin Cell Biol* 13:641-8. PMID: [11544035](https://pubmed.ncbi.nlm.nih.gov/11544035/); DOI: [10.1016/s0955-0674(00)00264-7](https://doi.org/10.1016/s0955-0674(00)00264-7)
* **troyer-2011-pard3b-aids**: Troyer JL, Nelson GW, Lautenberger JA, et al. (2011). Genome-wide association study implicates PARD3B-based AIDS restriction. *J Infect Dis* 203:1491-502. PMID: [21502085](https://pubmed.ncbi.nlm.nih.gov/21502085/); DOI: [10.1093/infdis/jir046](https://doi.org/10.1093/infdis/jir046); PMCID: PMC3080910
* **yang-2022-pard3b-gbm**: Yang JD, Chen JT, Liu SH, Chen RM (2022). Contribution of the Testosterone Androgen Receptor-PARD3B Signaling Axis to Tumorigenesis and Malignance of Glioblastoma Multiforme through Stimulating Cell Proliferation and Colony Formation. *J Clin Med* 11. PMID: [36013056](https://pubmed.ncbi.nlm.nih.gov/36013056/); DOI: [10.3390/jcm11164818](https://doi.org/10.3390/jcm11164818); PMCID: PMC9410375
* **takeuchi-2026-chd3-pard3b**: Takeuchi M, Okimoto Y, Fukushima M, et al. (2026). Targeting the CHD3 chromatin remodeler exploits a synthetic lethal vulnerability in dual SMARCA4/SMARCA2-deficient cancers via derepression of PARD3B. *NPJ Precis Oncol* 10. PMID: [42174139](https://pubmed.ncbi.nlm.nih.gov/42174139/); DOI: [10.1038/s41698-026-01499-7](https://doi.org/10.1038/s41698-026-01499-7); PMCID: PMC13469703
* **huang-2024-par3l-macrophage**: Huang YM, Wu YS, Dang YY, et al. (2024). Par3L, a polarity protein, promotes M1 macrophage polarization and aggravates atherosclerosis in mice via p65 and ERK activation. *Acta Pharmacol Sin* 45:112-124. PMID: [37731037](https://pubmed.ncbi.nlm.nih.gov/37731037/); DOI: [10.1038/s41401-023-01161-z](https://doi.org/10.1038/s41401-023-01161-z); PMCID: PMC10770347
* **koehler-2016-par3a-kidney**: Koehler S, Tellkamp F, Niessen CM, et al. (2016). Par3A is dispensable for the function of the glomerular filtration barrier of the kidney. *Am J Physiol Renal Physiol* 311:F112-9. PMID: [27122542](https://pubmed.ncbi.nlm.nih.gov/27122542/); DOI: [10.1152/ajprenal.00171.2016](https://doi.org/10.1152/ajprenal.00171.2016)
* **koehler-2022-par3a-par3b-podocyte**: Koehler S, Odenthal J, Ludwig V, et al. (2022). Scaffold polarity proteins Par3A and Par3B share redundant functions while Par3B acts independent of atypical protein kinase C/Par6 in podocytes to maintain the kidney filtration barrier. *Kidney Int* 101:733-751. PMID: [34929254](https://pubmed.ncbi.nlm.nih.gov/34929254/); DOI: [10.1016/j.kint.2021.11.030](https://doi.org/10.1016/j.kint.2021.11.030)
* **feng-2007-par3-ntd-pb1**: Feng W, Wu H, Chan LN, Zhang M (2007). The Par-3 NTD adopts a PB1-like structure required for Par-3 oligomerization and membrane localization. *EMBO J* 26:2786-96. PMID: [17476308](https://pubmed.ncbi.nlm.nih.gov/17476308/); DOI: [10.1038/sj.emboj.7601702](https://doi.org/10.1038/sj.emboj.7601702); PMCID: PMC1888665
* **smith-2021-enos-polarity**: Smith TL, Oubaha M, Cagnone G, et al. (2021). eNOS controls angiogenic sprouting and retinal neovascularization through the regulation of endothelial cell polarity. *Cell Mol Life Sci* 79:37. PMID: [34971428](https://pubmed.ncbi.nlm.nih.gov/34971428/); DOI: [10.1007/s00018-021-04042-y](https://doi.org/10.1007/s00018-021-04042-y); PMCID: PMC8739159
* **uniprot-A0A9L0JEY6**: UniProtKB/TrEMBL entry A0A9L0JEY6_EQUAS, Partitioning defective 3 homolog B (Equus asinus), entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0JEY6.txt
* **uniprot-Q8TEW8**: UniProtKB/Swiss-Prot entry Q8TEW8 (PAR3L_HUMAN), Partitioning defective 3 homolog B (Homo sapiens). https://rest.uniprot.org/uniprotkb/Q8TEW8.txt


## Citations

1. feng-2007-par3-ntd-pb1-abstract.md
2. feng-2007-par3-ntd-pb1-summary.md
3. feng-2008-par3-pten-abstract.md
4. feng-2008-par3-pten-summary.md
5. gao-2002-par3l-splice-abstract.md
6. gao-2002-par3l-splice-summary.md
7. huang-2024-par3l-macrophage-abstract.md
8. huang-2024-par3l-macrophage-summary.md
9. huo-2014-par3l-mammary-abstract.md
10. huo-2014-par3l-mammary-fulltext.txt
11. huo-2014-par3l-mammary-summary.md
12. izaki-2005-par3beta-1433-abstract.md
13. izaki-2005-par3beta-1433-summary.md
14. izaki-2006-insc-lgn-abstract.md
15. izaki-2006-insc-lgn-summary.md
16. koehler-2016-par3a-kidney-abstract.md
17. koehler-2016-par3a-kidney-summary.md
18. koehler-2022-par3a-par3b-podocyte-abstract.md
19. koehler-2022-par3a-par3b-podocyte-summary.md
20. kohjima-2002-par3beta-abstract.md
21. kohjima-2002-par3beta-summary.md
22. li-2017-par3l-lkb1-abstract.md
23. li-2017-par3l-lkb1-summary.md
24. metadata.json
25. mizuno-2003-par3-selfassoc-abstract.md
26. mizuno-2003-par3-selfassoc-summary.md
27. ohno-2001-par-apkc-review-abstract.md
28. ohno-2001-par-apkc-review-summary.md
29. smith-2021-enos-polarity-abstract.md
30. smith-2021-enos-polarity-fulltext.txt
31. smith-2021-enos-polarity-summary.md
32. takeuchi-2026-chd3-pard3b-abstract.md
33. takeuchi-2026-chd3-pard3b-fulltext.txt
34. takeuchi-2026-chd3-pard3b-summary.md
35. thompson-2022-par3-family-review-abstract.md
36. thompson-2022-par3-family-review-fulltext.txt
37. thompson-2022-par3-family-review-summary.md
38. troyer-2011-pard3b-aids-abstract.md
39. troyer-2011-pard3b-aids-summary.md
40. uniprot-A0A9L0JEY6-entry.txt
41. uniprot-A0A9L0JEY6-sequence.fasta
42. uniprot-Q8TEW8-entry.txt
43. uniprot-Q8TEW8-sequence.fasta
44. wang-2020-donkey-genome-abstract.md
45. wang-2020-donkey-genome-fulltext.txt
46. wang-2020-donkey-genome-summary.md
47. wang-2021-proximity-lumen-abstract.md
48. wang-2021-proximity-lumen-fulltext.txt
49. wang-2021-proximity-lumen-summary.md
50. wu-2007-par3-pdz-pi-abstract.md
51. wu-2007-par3-pdz-pi-summary.md
52. yang-2022-pard3b-gbm-abstract.md
53. yang-2022-pard3b-gbm-fulltext.txt
54. yang-2022-pard3b-gbm-summary.md
55. zhang-2026-par3l-chromosome-abstract.md
56. zhang-2026-par3l-chromosome-fulltext.txt
57. zhang-2026-par3l-chromosome-summary.md