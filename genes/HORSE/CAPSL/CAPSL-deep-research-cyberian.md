---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:43:30.611715'
end_time: '2026-10-26T01:52:06.703285'
duration_seconds: 516.09
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: CAPSL
  gene_symbol: CAPSL
  uniprot_accession: A0A3Q2I3U9
  protein_description: 'SubName: Full=Calcyphosine like {ECO:0000313|Ensembl:ENSECAP00000041901.3};'
  gene_info: Name=CAPSL {ECO:0000313|VGNC:VGNC:16048};
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: Ca-bind. (IPR051581); EF-hand-dom_pair. (IPR011992); EF_Hand_1_Ca_BS.
    (IPR018247); EF_hand_dom. (IPR002048); EF-hand_7 (PF13499)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3301
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 48
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A3Q2I3U9
- **Protein Description:** SubName: Full=Calcyphosine like {ECO:0000313|Ensembl:ENSECAP00000041901.3};
- **Gene Information:** Name=CAPSL {ECO:0000313|VGNC:VGNC:16048};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Ca-bind. (IPR051581); EF-hand-dom_pair. (IPR011992); EF_Hand_1_Ca_BS. (IPR018247); EF_hand_dom. (IPR002048); EF-hand_7 (PF13499)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CAPSL" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CAPSL' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CAPSL** (gene ID: CAPSL, UniProt: A0A3Q2I3U9) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CAPSL (Calcyphosine-like) in the Horse (*Equus caballus*; UniProt A0A3Q2I3U9): A Review of Function, Localization and Pathways

## 1. Introduction and Summary

CAPSL (calcyphosine-like, also called calcyphosin-like protein) is a small, acidic EF-hand calcium-binding protein of the calcyphosine family. The horse protein A0A3Q2I3U9 is an unreviewed, computationally predicted TrEMBL entry derived from the Ensembl gene model ENSECAG00000036819 on horse chromosome 21. It is linked to the VGNC symbol CAPSL (VGNC:16048), and InterPro, Pfam and PANTHER classify it as an EF-hand protein of the calcyphosin-like subfamily (PTHR34524:SF5) [uniprot-A0A3Q2I3U9]. No experimental study has been published on horse CAPSL. What can be said about its function therefore comes from its near-identity to human CAPSL (Q8WWF8) and from experimental work in human, bovine, mouse and ciliate systems.

The most direct mechanistic evidence comes from two 2026 cryo-electron tomography studies. They identify CAPSL as a **microtubule inner protein (MIP) that lines the lumen of the A-tubule of doublet microtubules in the transition zone (TZ) of motile cilia**. In human multiciliated airway cells, several CAPSL copies per 8-nm tubulin repeat bind protofilaments A10–A13, mainly contacting α-tubulin, and the assignment is supported by an N-terminal helix that only CAPSL carries [zhou-2026-transition-zone-fulltext]. In bovine tracheal cilia, CAPSL forms a pseudo-helical spiral in the TZ doublet lumen and stabilizes microtubules in vitro [cai-2026-tz-doublet-preprint-abstract]. The best-supported primary function of CAPSL is therefore structural. It is a calcium-binding lattice-stabilizing protein inside the specialised proximal segment of the motile ciliary axoneme. It is not an enzyme, transporter or classical signal transducer.

Other reported roles are less mechanistically defined. Heterozygous loss-of-function CAPSL variants have been associated with familial exudative vitreoretinopathy (FEVR), and endothelial-specific Capsl deletion in mice delays retinal angiogenesis with reduced MYC-target gene expression [liu-2024-capsl-fevr-abstract]. CAPSL has also been implicated in adipogenesis and autophagy in multiple symmetric lipomatosis [lindner-2019-capsl-lipomatosis-abstract], and the CAPSL–IL7R locus has been associated with autoimmune disease [santiago-2008-capsl-il7r-t1d-abstract]. How these phenotypes relate to the ciliary MIP function is unresolved.

## 2. Gene and Protein Identity: Verification for the Horse Entry

The identity checks requested for this target pass. The horse UniProt entry names the gene CAPSL, gives the description "Calcyphosine like" and the organism *Equus caballus* (NCBI taxon 9796), and comes from the Thoroughbred reference genome [uniprot-A0A3Q2I3U9; wade-2009-horse-genome-abstract]. The predicted protein has 225 residues (26.2 kDa) with three PROSITE EF-hand domains (residues 56–91, 92–127 and 128–163), two Pfam EF-hand_7 pairs, two PROSITE EF_HAND_1 calcium-binding loop signatures and an inferred GO annotation "calcium ion binding" (IEA) [uniprot-A0A3Q2I3U9]. As part of this review I aligned the sequences. Horse residues 18–225 align without gaps to the full 208-residue human CAPSL (Q8WWF8) with only six conservative substitutions (D54N, M65V, V80A, V130I, S154T, I200V in human numbering), which is about 97% identity [uniprot-A0A3Q2I3U9; uniprot-Q8WWF8-human-CAPSL-entry]. The horse model adds a 17-residue N-terminal extension (MQERASIVASLSNWWQQ) that human CAPSL lacks. This may be a gene-model artefact from an upstream start codon and should be treated with caution. The human UniProt entry itself flags an erroneous initiation in one cDNA [uniprot-Q8WWF8-human-CAPSL-entry].

The literature search found no conflicting use of the symbol. "CAPSL" publications concern calcyphosine-like in mammals. The paralogs CAPS (calcyphosine) and CAPS2 (calcyphosine 2) are distinct genes [zhou-2026-transition-zone-fulltext]. They should not be confused with unrelated proteins abbreviated "CAPS" (Ca²⁺-dependent activator protein for secretion, CADPS/CADPS2), which appear in some search hits. Everything below concerns the calcyphosine-family protein, and horse-specific function is inferred by orthology.

## 3. Domain Architecture, Calcium Binding and the Calcyphosine Family

CAPSL belongs to the calcyphosine family. This lineage of EF-hand proteins resembles calmodulin in overall shape but is phylogenetically distinct from it. The 2.65 Å crystal structure of Ca²⁺-loaded human CAPS, the closest paralog, shows two globular lobes, each holding a pair of EF-hand motifs, in a calmodulin-like topology. It differs from calmodulin in EF-hand 4, in its N- and C-terminal regions and in the interdomain linker. Its C-terminal lobe has a large hydrophobic pocket in the Ca²⁺-bound state, and the protein stays monomeric whether or not Ca²⁺ is bound. Together with phylogeny, these features define the calcyphosine family, which extends from arthropods to humans [dong-2008-calcyphosine-structure-abstract]. An early family member, the rabbit R2D5 antigen, binds Ca²⁺ with a calmodulin-like conformational change and can be phosphorylated by CaMKII and PKA. It is expressed in olfactory receptor neurons and in ependymal cells [nemoto-1993-r2d5-calcyphosine-abstract], both of which are ciliated.

Horse CAPSL has the same bilobed EF-hand arrangement. My inspection of the sequence (not a published analysis) suggests that the first two EF-hand loops are canonical. They are DDNNNRTLDFKE and DKDGNGTIDFNE, with Asp/Asn at positions 1, 3 and 5 and Glu at position 12, which fits the two PROSITE EF_HAND_1 hits. The third and fourth putative loops depart from the canonical pattern, so the protein probably binds Ca²⁺ at fewer than four sites [uniprot-A0A3Q2I3U9]. Calcium binding has not been measured directly for CAPSL in any species. The structural work assigns the TZ densities to a bilobal protein with short α-helices typical of EF-hand motifs [zhou-2026-transition-zone-fulltext].

Microtubule binding appears to be a property of the whole family. Human CAPS binds microtubules, promotes their bundling in vitro and in cells, and is needed for robust kinetochore fibres in the mitotic spindle [setu-2024-calcyphosine-spindle-abstract]. Zhou and colleagues describe the calcyphosine family as microtubule-binding on this basis [zhou-2026-transition-zone-fulltext].

## 4. Primary Function: A Microtubule Inner Protein of the Ciliary Transition Zone

### 4.1 Structural identification in human and bovine motile cilia

The transition zone is the proximal segment of the cilium, just distal to the basal body. It gates which proteins enter the cilium, and its doublet microtubules (DMTs) have a specialised structure. Zhou et al. applied in situ cryo-electron tomography and subtomogram averaging to human multiciliated respiratory epithelial cells and resolved TZ DMTs at subnanometer resolution, identifying nine constituent proteins [zhou-2026-transition-zone-abstract]. Prominent "shelf-like" densities in the A-tubule lumen were assigned to the calcyphosine family by a stepwise approach. The authors first screened 197 human EF-hand proteins for strong enrichment in lung multiciliated cells, which left only seven candidates (CAPS, CAPSL, CETN2, CLXN, EFCAB11, EFCAB12 and EFHB). They then fitted AlphaFold3 and Boltz-2 models of these candidates into the densities; CAPS and CAPSL gave plausible but imperfect fits. Grafting a loop from the experimental structure of the *Tetrahymena* CAPS homolog RIB22 (PDB 8G3D) onto the CAPSL model improved the fit, and an unbiased DomainSeeker search ranked the optimised human CAPSL model as the top-scoring solution [zhou-2026-transition-zone-fulltext]. A density for an N-terminal α-helix (αN), present in CAPSL but absent from CAPS and CAPS2, further supported the assignment to CAPSL. Ultrastructure expansion microscopy (U-ExM) with an anti-CAPSL antibody independently confirmed CAPSL at the TZ of multiciliated respiratory cells, and CAPS2 was also detected there [zhou-2026-transition-zone-fulltext].

In the model, several CAPSL copies bind protofilaments A10–A13 in each 8-nm repeat, some at substoichiometric occupancy, possibly shared with paralogs. CAPSL mainly recognises α-tubulin, with minor contacts to β-tubulin and the neighbouring lateral α-tubulin. Its arrangement resembles that of SPACA9, another shelf-like MIP that forms striations in sperm singlet microtubules and axonemal B-tubules, although the two proteins bind different sites [zhou-2026-transition-zone-fulltext]. The CAPSL zone also extends further into the cilium than the ECT2L/DZANK1 inter-doublet linkers, so the TZ itself contains distinct sub-zones [zhou-2026-transition-zone-fulltext].

A separate study of bovine tracheal cilia at 4.7–5.0 Å resolution reached the same conclusion. It identified CAPSL as a lumenal MIP of the TZ doublet that forms a pseudo-helical spiral, and showed that CAPSL stabilizes microtubules in vitro. The authors describe the TZ doublet as a structurally independent segment defined by 8-nm-periodic MIPs and MAPs [cai-2026-tz-doublet-preprint-abstract]. This is a preprint and has not been peer reviewed. Even so, two independent groups, using two species (human in situ and bovine), place CAPSL in the same location. Their agreement makes the localization robust, and the horse protein differs from human CAPSL at only six positions, so the inference extends to the horse.

### 4.2 Proposed mechanism

The structural data point to a scaffold role for CAPSL. By binding across adjacent protofilaments inside the A-tubule, CAPSL probably reinforces the TZ doublet lattice, much as other MIPs are thought to increase the rigidity and stability of axonemal microtubules [howardtill-2025-rib22-abstract; kubo-2023-tetrahymena-doublet-abstract]. The in vitro microtubule-stabilizing activity reported for bovine CAPSL supports this view [cai-2026-tz-doublet-preprint-abstract]. Because CAPSL has EF-hands, Ca²⁺ might tune its binding or the mechanics of the TZ. This has not been tested. Calcium-signalling proteins are known to sit in motile cilia, where they couple Ca²⁺ to motility [hikmet-2026-fallopian-cilia-fulltext].

### 4.3 Evolutionary conservation of calcyphosin-family MIPs

The calcyphosin MIP role is ancient. In the ciliate *Tetrahymena thermophila*, RIB22 is a calmodulin-like protein that clusters phylogenetically with vertebrate calcyphosins. It sits in the A-tubule of doublet and triplet microtubules of cilia and basal bodies, depends on the conserved MIP RIB72 for its localization, and forms a ternary complex with the RIB72A EF-hand domain and FAM166A. Strains lacking RIB22 have impaired ciliary function [howardtill-2025-rib22-abstract; howardtill-2025-rib22-fulltext]. RIB22 was identified as a native DMT MIP by single-particle cryo-EM, and its docking needs RIB72A [kubo-2023-tetrahymena-doublet-fulltext]. Its structure was the template used to model human CAPSL [zhou-2026-transition-zone-fulltext]. Calcyphosin-like modules are also used in land plants. The liverwort protein MpCAFA joins a CAPS-like N-terminal region to a FAP115-like region, localizes along spermatozoid cilia and is needed for normal swimming speed [morita-2025-mpcafa-abstract]. Zhou et al. report that CAPS/CAPSL homologs are broadly conserved across ciliated organisms and are induced by the motile ciliogenesis transcription factor FOXJ1 [zhou-2026-transition-zone-fulltext], citing a zebrafish screen of Foxj1-induced genes [choksi-2014-zebrafish-cilia-genes-abstract].

## 5. Cellular and Tissue Localization

Several independent sources place CAPSL in motile ciliated epithelia. In addition to the airway TZ data above [zhou-2026-transition-zone-fulltext], a high-resolution antibody-based map of the human fallopian tube found CAPSL among the calcium-signalling proteins in motile cilia, together with CAPS, CABCOCO1, EFCAB1 and ENKUR [hikmet-2026-fallopian-cilia-fulltext]. Expression databases agree. Bgee lists the horse gene as expressed in "epithelium of bronchus" and the human gene in bronchial epithelial cells [uniprot-A0A3Q2I3U9; uniprot-Q8WWF8-human-CAPSL-entry]. In single-cell RNA-seq of lung, all three calcyphosine paralogs are expressed in multiciliated cells [zhou-2026-transition-zone-fulltext].

The Human Protein Atlas gives a consistent picture at the RNA level. CAPSL belongs to its "ciliated tissues – cilium organization" expression cluster, is enriched in choroid plexus and fallopian tube, and in single-cell data is highest in fallopian-tube, respiratory, efferent-duct, endometrial and ependymal ciliated cells and in spermatocytes and spermatids [hpa-ENSG00000152611-CAPSL-entry]. The same pattern holds in an ungulate: in single-cell RNA-seq of fetal and newborn sheep lung, CAPSL is one of the marker genes of the FOXJ1-expressing ciliated-cell cluster [leir-2025-sheep-cftr-lung-fulltext]. Sheep, like horses, are large ungulates, so this makes it likely that horse CAPSL is also expressed in airway multiciliated cells, as the Bgee annotation suggests.

Other cell types give a less specific picture. The Human Protein Atlas antibody-based immunofluorescence in cultured cell lines places CAPSL mainly in the nucleoplasm, on microtubules and in the primary cilium, with additional signal at the plasma membrane and the cytokinetic bridge [hpa-ENSG00000152611-CAPSL-entry]. Microtubules, the primary cilium and the cytokinetic bridge are all microtubule-based structures, so the cell-line data support microtubule binding by CAPSL even outside motile cilia. The primary-cilium signal is notable because it offers a possible link to the non-motile-cilium phenotypes discussed below. It is a high-throughput annotation and has not been confirmed by focused study. When CAPSL was overexpressed in HEK293T cells, which have no motile cilia, it was found in both the cytoplasm and the nucleus [liu-2024-capsl-fevr-fulltext]. UniProt's "cytoplasm" annotation for human CAPSL is inferred by curators (ECO:0000305), not experimentally determined [uniprot-Q8WWF8-human-CAPSL-entry]. CAPSL protein has also been detected in normal human adipocytes by immunohistochemistry [lindner-2019-capsl-lipomatosis-fulltext] and endothelial Capsl is required for normal retinal angiogenesis in mice [liu-2024-capsl-fevr-fulltext]. For the horse, the most defensible annotation is the transition-zone portion of the motile-cilium axoneme, specifically the lumen of the A-tubule of the doublet microtubule, which is within the cytoplasmic microtubule cytoskeleton. Cytoplasmic or nuclear pools may exist in non-ciliated cells.

## 6. Reported Roles Outside the Cilium: Angiogenesis, Adipogenesis and Immunity

### 6.1 Retinal angiogenesis and the MYC axis

Liu et al. performed whole-exome sequencing of 120 FEVR families without mutations in known FEVR genes. They found two heterozygous CAPSL variants, a stop-gain (p.R30X) and a missense change (p.L83F). The R30X protein was undetectable and L83F protein was greatly reduced, while mRNA levels were unchanged [liu-2024-capsl-fevr-fulltext]. Leu83 lies within the second annotated EF-hand domain of human CAPSL (residues 75–110), corresponding to horse residue 100 [uniprot-Q8WWF8-human-CAPSL-entry]. In mice, inducible endothelial-specific Capsl deletion (Pdgfb-iCreER) delayed radial and vertical retinal vascular progression and reduced endothelial proliferation and migration. Heterozygous animals showed no overt defect [liu-2024-capsl-fevr-fulltext]. In human retinal microvascular endothelial cells, CAPSL depletion impaired tube formation, proliferation, polarity, filopodia and lamellipodia formation, and collective migration. Transcriptomic and proteomic profiling showed suppression of the MYC signalling axis, and the expression pattern resembled that of c-MYC-depleted endothelial cells [liu-2024-capsl-fevr-abstract]. The authors propose that CAPSL acts upstream of MYC-driven endothelial programmes. They did not identify a direct molecular link, and reviewers noted that the mechanism of the missense variant is unclear [liu-2024-capsl-fevr-fulltext]. This pathway placement should be treated as a phenotypic association, not a defined signalling step.

### 6.2 Adipocyte biology and autophagy

In a four-generation family with multiple symmetric lipomatosis, the heterozygous nonsense variant CAPSL p.R9* was the leading candidate. CAPSL immunostaining was absent or scarce in adipose tissue from the index patient and from 10 sporadic MSL patients [lindner-2019-capsl-lipomatosis-abstract]. In 3T3-L1 pre-adipocytes, Capsl knockout increased lipid accumulation. Knockout and overexpression changed autophagy flux and SIRT1 expression in opposite directions, which led the authors to suggest that CAPSL restrains adipogenesis by modulating autophagy [lindner-2019-capsl-lipomatosis-fulltext]. No coding variants were found in 21 further patients, so CAPSL is not a common monogenic cause of MSL [lindner-2019-capsl-lipomatosis-abstract]. Lindner et al. also cite a proteomic study of olfactory cilia to suggest that CAPSL may interact with calmodulin [lindner-2019-capsl-lipomatosis-fulltext; klimmeck-2008-olfactory-calcium-abstract].

### 6.3 Genetic association with autoimmunity

CAPSL lies next to IL7R on human chromosome 5p13. SNPs in CAPSL (rs1445898, rs1010601) have been associated with type 1 diabetes [santiago-2008-capsl-il7r-t1d-abstract] and, in a small paediatric cohort, with Hashimoto's thyroiditis [borysewicz-2024-capsl-thyroid-abstract]. Because IL7R is a strong immunological candidate at the same locus, these associations cannot be assigned to CAPSL function.

## 7. Synthesis: Functional Annotation for Horse CAPSL

Taken together, the evidence supports annotating horse CAPSL as a calcium-binding EF-hand protein of the calcyphosine family. It acts as a structural microtubule inner protein of the motile-cilium transition zone, where it binds the lumenal surface of the doublet A-tubule (mainly α-tubulin) and probably stabilizes the TZ microtubule lattice. Cryo-ET in human airway cells and bovine trachea, antibody-based localization by U-ExM, ciliated-cell-specific expression in human and sheep [hpa-ENSG00000152611-CAPSL-entry; leir-2025-sheep-cftr-lung-fulltext], in vitro microtubule stabilization, and conservation of the calcyphosin-MIP role in *Tetrahymena* all support this annotation [zhou-2026-transition-zone-fulltext; cai-2026-tz-doublet-preprint-abstract; howardtill-2025-rib22-abstract]. The horse orthology is strong (about 97% identity to human). Reasonable GO-style annotations include calcium ion binding (IEA, InterPro), microtubule binding (by orthology and family evidence), and localization to the ciliary transition zone, the axoneme and the microtubule lumen of doublet microtubules (by orthology). For the angiogenesis and adipogenesis phenotypes, CAPSL's place in a pathway is still undefined. Any annotation of a role in MYC signalling or autophagy should be weak and should reflect phenotypic association in other species, not a demonstrated mechanism. No catalytic activity, transport substrate or receptor function has been reported or is predicted for CAPSL.

## 8. Open Questions

The most pressing question is physiological. Two structural studies agree on where CAPSL sits, but no one has yet described the phenotype of a CAPSL-null motile cilium. Knockout or knockdown in multiciliated airway cells, ependyma or sperm, with cryo-ET of TZ architecture and measurement of beat frequency and mucociliary clearance, would test whether CAPSL is needed for TZ doublet stability, ciliary gating or motility, and whether CAPS2 compensates. Relatedly, CAPSL has not been examined as a candidate gene for primary ciliary dyskinesia or other motile ciliopathies, although the same study implicated its TZ neighbours ECT2L and DZANK1 in PCD [zhou-2026-transition-zone-abstract].

Second, calcium binding has not been measured for CAPSL in any species. It is unknown how many EF-hands are functional, what their affinities are, and whether Ca²⁺ changes CAPSL's affinity for the TZ lattice. Isothermal titration or NMR with recombinant protein and microtubule co-sedimentation at different Ca²⁺ concentrations would answer these questions. It also remains to be shown whether the CAPSL-specific N-terminal helix (αN) targets CAPSL to the TZ instead of the distal axoneme [zhou-2026-transition-zone-fulltext].

Third, the non-ciliary phenotypes need to be reconciled with the ciliary role. Endothelial and adipocyte cells usually carry primary cilia, not motile ones. One possibility is that CAPSL also acts in primary cilia, which Human Protein Atlas immunofluorescence weakly suggests [hpa-ENSG00000152611-CAPSL-entry], or in cytoplasmic or nuclear microtubule networks as its paralog CAPS does in mitotic spindles [setu-2024-calcyphosine-spindle-abstract]. Another is that the MYC and autophagy effects are indirect. The molecular link between CAPSL loss and reduced MYC-target expression has not been established [liu-2024-capsl-fevr-fulltext].

Finally, for the horse itself, the 17-residue N-terminal extension of the Ensembl model should be checked against equine RNA-seq or Iso-Seq data and ribosome-profiling evidence. Equine airway and testis expression of CAPSL, and the protein's localization in horse respiratory cilia, have not been examined. Equine respiratory disease (such as equine asthma) and stallion sperm motility would be natural settings in which to test whether CAPSL variation matters.

## 9. References

- **[uniprot-A0A3Q2I3U9]** UniProtKB/TrEMBL entry A0A3Q2I3U9_HORSE, "Calcyphosine like" (CAPSL), *Equus caballus*; Ensembl ENSECAT00000039145.3 / ENSECAP00000041901.3 / ENSECAG00000036819.3; VGNC:16048. https://rest.uniprot.org/uniprotkb/A0A3Q2I3U9.txt (files: citations/uniprot-A0A3Q2I3U9-entry.txt, .fasta)
- **[uniprot-Q8WWF8-human-CAPSL-entry]** UniProtKB/Swiss-Prot entry Q8WWF8 (CAPSL_HUMAN), Calcyphosin-like protein, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q8WWF8.txt
- **[zhou-2026-transition-zone]** Zhou H, Terbeck L, Berical A, Brunet M, Lange SM, Anderson JR, Olbrich H, et al. In situ structure of the human ciliary transition zone links linker defects to primary ciliary dyskinesia. *Science* 2026. PMID: 42721274; PMCID: PMC13650764; DOI: 10.1126/science.aei5957
- **[cai-2026-tz-doublet-preprint]** Cai B, Carmadiel AP, van Grinsven EJ, van Veghel T, Aher A, Aarts E, Xu Y, Beltro P, Beekman JM, Akhmanova A, Xu J, Wieczorek M. Structure of the mammalian ciliary transition zone microtubule doublet. bioRxiv preprint 2026. DOI: 10.64898/2026.06.11.731632 (Europe PMC PPR1251699)
- **[howardtill-2025-rib22]** Howard-Till RA, Li S, Pallabi Kar U, Fuentes CN, Fabritius AS, Winey M. A ternary complex of MIPs in the A-tubule of basal bodies and axonemes depends on RIB22 and the EF-hand domain of RIB72A in *Tetrahymena* cilia. *Mol Biol Cell* 2025. PMID: 39937672; PMCID: PMC12005106; DOI: 10.1091/mbc.e24-12-0557
- **[kubo-2023-tetrahymena-doublet]** Kubo S, Black CS, Joachimiak E, et al., Bui KH. Native doublet microtubules from *Tetrahymena thermophila* reveal the importance of outer junction proteins. *Nat Commun* 2023;14:2168. PMID: 37061538; PMCID: PMC10105768; DOI: 10.1038/s41467-023-37868-0
- **[dong-2008-calcyphosine-structure]** Dong H, Li X, Lou Z, Xu X, Su D, Zhou X, Zhou W, Bartlam M, Rao Z. Crystal-structure and biochemical characterization of recombinant human calcyphosine delineates a novel EF-hand-containing protein family. *J Mol Biol* 2008;383:455–464. PMID: 18775726; DOI: 10.1016/j.jmb.2008.08.048
- **[setu-2024-calcyphosine-spindle]** Setu B, Nie Q, Echele G, Spencer SA. Calcyphosine is a microtubule-associated protein required for spindle formation and function. bioRxiv preprint. DOI: 10.1101/2023.12.29.573632
- **[nemoto-1993-r2d5-calcyphosine]** Nemoto Y, Ikeda J, Katoh K, Koshimoto H, Yoshihara Y, Mori K. R2D5 antigen: a calcium-binding phosphoprotein predominantly expressed in olfactory receptor neurons. *J Cell Biol* 1993. PMID: 8227152; PMCID: PMC2200141; DOI: 10.1083/jcb.123.4.963
- **[morita-2025-mpcafa]** Morita M, Yamato KT. The MpCAFA gene encodes a ciliary protein required for spermatozoid motility in the liverwort *Marchantia polymorpha*. *J Plant Res* 2025. PMID: 40841643; DOI: 10.1007/s10265-025-01666-0
- **[choksi-2014-zebrafish-cilia-genes]** Choksi SP, Babu D, Lau D, Yu X, Roy S. Systematic discovery of novel ciliary genes through functional genomics in the zebrafish. *Development* 2014;141:3410–3419. PMID: 25139857; PMCID: PMC4199137; DOI: 10.1242/dev.108209
- **[hikmet-2026-fallopian-cilia]** Hikmet F, Digre A, Hansen JN, Schon SB, Lundberg E, Olovsson M, Uhlén M, Méar L, Lindskog C. A high-resolution spatial map of cilia-associated proteins in the human fallopian tube. *Nat Commun* 2026. PMID: 42010243; PMCID: PMC13096173; DOI: 10.1038/s41467-026-71692-6
- **[liu-2024-capsl-fevr]** Liu W, Li S, Yang M, Ma J, Liu L, Fei P, Xiang Q, Huang L, Zhao P, Yang Z, Zhu X. Dysfunction of Calcyphosine-Like gene impairs retinal angiogenesis through the MYC axis and is associated with familial exudative vitreoretinopathy. *eLife* 2024. PMID: 39264149; PMCID: PMC11392532; DOI: 10.7554/elife.96907
- **[lindner-2019-capsl-lipomatosis]** Lindner A, Marbach F, Tschernitz S, Ortner C, Berneburg M, Felthaus O, Prantl L, Kye MJ, Rappl G, Altmüller J, Thiele H, Schreml S, Schreml J. Calcyphosine-like (CAPSL) is regulated in Multiple Symmetric Lipomatosis and is involved in Adipogenesis. *Sci Rep* 2019. PMID: 31186450; PMCID: PMC6559987; DOI: 10.1038/s41598-019-44382-1
- **[klimmeck-2008-olfactory-calcium]** Klimmeck D, Mayer U, Ungerer N, Warnken U, Schnölzer M, Frings S, Möhrlen F. Calcium-signaling networks in olfactory receptor neurons. *Neuroscience* 2008;151:901–912. PMID: 18155848; DOI: 10.1016/j.neuroscience.2007.11.023
- **[santiago-2008-capsl-il7r-t1d]** Santiago JL, Alizadeh BZ, Martínez A, et al., Urcelay E. Study of the association between the CAPSL-IL7R locus and type 1 diabetes. *Diabetologia* 2008;51:1653–1658. PMID: 18563381; DOI: 10.1007/s00125-008-1070-4
- **[borysewicz-2024-capsl-thyroid]** Borysewicz-Sańczyk H, Wawrusiewicz-Kurylonek N, Gościk J, Sawicka B, Bossowski F, Corica D, Aversa T, Waśniewska M, Bossowski A. Prevalence of Selected Polymorphisms of Il7R, CD226, CAPSL, and CLEC16A Genes in Children and Adolescents with Autoimmune Thyroid Diseases. *Int J Mol Sci* 2024. PMID: 38612837; PMCID: PMC11012896; DOI: 10.3390/ijms25074028
- **[hpa-ENSG00000152611-CAPSL]** Human Protein Atlas entry for CAPSL (ENSG00000152611), RNA expression and subcellular location data. https://www.proteinatlas.org/ENSG00000152611.json (file: citations/hpa-ENSG00000152611-CAPSL-entry.json)
- **[leir-2025-sheep-cftr-lung]** Leir SH, Tkachenko S, Paranjapye A, Van Wettere AJ, Kerschner JL, Perisse IV, Marriott CM, Patrick T, Liu Y, White KL, Polejaeva IA, Harris A. Cellular imbalance in proximal and distal lung of CFTR-/- sheep in utero and at birth. *Mol Med* 2025. PMID: 40495135; PMCID: PMC12153128; DOI: 10.1186/s10020-025-01266-7
- **[wade-2009-horse-genome]** Wade CM, Giulotto E, Sigurdsson S, et al., Lindblad-Toh K. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 2009;326:865–867. PMID: 19892987; DOI: 10.1126/science.1178158


## Citations

1. borysewicz-2024-capsl-thyroid-abstract.md
2. borysewicz-2024-capsl-thyroid-summary.md
3. cai-2026-tz-doublet-preprint-abstract.md
4. cai-2026-tz-doublet-preprint-summary.md
5. choksi-2014-zebrafish-cilia-genes-abstract.md
6. choksi-2014-zebrafish-cilia-genes-summary.md
7. dong-2008-calcyphosine-structure-abstract.md
8. dong-2008-calcyphosine-structure-summary.md
9. hikmet-2026-fallopian-cilia-abstract.md
10. hikmet-2026-fallopian-cilia-fulltext.txt
11. hikmet-2026-fallopian-cilia-summary.md
12. howardtill-2025-rib22-abstract.md
13. howardtill-2025-rib22-fulltext.txt
14. howardtill-2025-rib22-summary.md
15. hpa-ENSG00000152611-CAPSL-entry.json
16. hpa-ENSG00000152611-CAPSL-summary.md
17. klimmeck-2008-olfactory-calcium-abstract.md
18. klimmeck-2008-olfactory-calcium-summary.md
19. kubo-2023-tetrahymena-doublet-abstract.md
20. kubo-2023-tetrahymena-doublet-fulltext.txt
21. kubo-2023-tetrahymena-doublet-summary.md
22. leir-2025-sheep-cftr-lung-abstract.md
23. leir-2025-sheep-cftr-lung-fulltext.txt
24. leir-2025-sheep-cftr-lung-summary.md
25. lindner-2019-capsl-lipomatosis-abstract.md
26. lindner-2019-capsl-lipomatosis-fulltext.txt
27. lindner-2019-capsl-lipomatosis-summary.md
28. liu-2024-capsl-fevr-abstract.md
29. liu-2024-capsl-fevr-fulltext.txt
30. liu-2024-capsl-fevr-summary.md
31. morita-2025-mpcafa-abstract.md
32. morita-2025-mpcafa-summary.md
33. nemoto-1993-r2d5-calcyphosine-abstract.md
34. nemoto-1993-r2d5-calcyphosine-summary.md
35. santiago-2008-capsl-il7r-t1d-abstract.md
36. santiago-2008-capsl-il7r-t1d-summary.md
37. setu-2024-calcyphosine-spindle-abstract.md
38. setu-2024-calcyphosine-spindle-summary.md
39. uniprot-A0A3Q2I3U9-entry.fasta
40. uniprot-A0A3Q2I3U9-entry.txt
41. uniprot-A0A3Q2I3U9-summary.md
42. uniprot-Q8WWF8-human-CAPSL-entry.fasta
43. uniprot-Q8WWF8-human-CAPSL-entry.txt
44. wade-2009-horse-genome-abstract.md
45. wade-2009-horse-genome-summary.md
46. zhou-2026-transition-zone-abstract.md
47. zhou-2026-transition-zone-fulltext.txt
48. zhou-2026-transition-zone-summary.md