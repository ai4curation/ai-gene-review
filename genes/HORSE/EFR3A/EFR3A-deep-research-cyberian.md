---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:42:24.242505'
end_time: '2026-10-26T02:54:11.021801'
duration_seconds: 706.78
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: EFR3A
  gene_symbol: EFR3A
  uniprot_accession: A0A9L0S4L8
  protein_description: 'RecName: Full=Protein EFR3 homolog A {ECO:0000256|ARBA:ARBA00072621};
    AltName: Full=Protein EFR3-like {ECO:0000256|ARBA:ARBA00077982};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the EFR3 family.
  protein_domains: ARM-like. (IPR011989); ARM-type_fold. (IPR016024); EFR3-like_ARM.
    (IPR049152); EFR3_Homologs. (IPR051851); EFR3_ARM (PF21052)
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
citation_count: 93
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0S4L8
- **Protein Description:** RecName: Full=Protein EFR3 homolog A {ECO:0000256|ARBA:ARBA00072621}; AltName: Full=Protein EFR3-like {ECO:0000256|ARBA:ARBA00077982};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the EFR3 family.
- **Key Domains:** ARM-like. (IPR011989); ARM-type_fold. (IPR016024); EFR3-like_ARM. (IPR049152); EFR3_Homologs. (IPR051851); EFR3_ARM (PF21052)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "EFR3A" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'EFR3A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **EFR3A** (gene ID: EFR3A, UniProt: A0A9L0S4L8) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# EFR3A (Protein EFR3 homolog A) in the horse, *Equus caballus* — UniProt A0A9L0S4L8

## 1. Introduction and summary

The horse protein A0A9L0S4L8 is an unreviewed, computationally predicted UniProtKB/TrEMBL entry named "Protein EFR3 homolog A" (alternative name EFR3-like). It is derived from the Thoroughbred reference genome assembly and belongs to the EFR3 family. It carries a single large EFR3-like armadillo (ARM)-repeat domain (Pfam PF21052, residues 12–644) and is placed in the PANTHER subfamily PTHR12444:SF1 "Protein EFR3 homolog A" [uniprot-A0A9L0S4L8; wade-2009-horse-genome-abstract]. The UniProt record gives no gene symbol, but the Ensembl cross-reference ties it to the horse gene ENSECAG00000014883 on chromosome 9. That same gene also produces the TrEMBL entries A0A3Q2GU27, A0A3Q2KQA4 and F6UA29, all of which UniProt labels with the gene name EFR3A. So the symbol "EFR3A" is correct for this protein and is not ambiguous [notes-sequence-analysis]. No experimental study of EFR3A in the horse exists. Everything said here about function is therefore inferred from orthologues. The inference is strong, because the horse sequence is about 98% identical to human EFR3A (Q14156) over the aligned region [notes-sequence-analysis], and the core function of the EFR3 family has been conserved from budding yeast through *Drosophila* to mammals [baird-2008-stt4-complex-abstract; nakatsu-2012-pi4kiiia-pm-abstract; wu-2014-pi4k-complex-structure-abstract].

EFR3A is not an enzyme. It is a peripheral membrane scaffold, and its job is to place the lipid kinase phosphatidylinositol 4-kinase IIIα (PI4KIIIα/PI4KA) on the cytoplasmic face of the plasma membrane. PI4KA phosphorylates phosphatidylinositol (PI) at the 4-position of the inositol ring to produce phosphatidylinositol 4-phosphate (PI4P). This is the first and committed step in making the plasma-membrane pools of PI(4,5)P2 and PI(3,4,5)P3 [lees-2017-pi4kiiia-architecture-abstract; nakatsu-2012-pi4kiiia-pm-abstract]. EFR3A is anchored to the membrane by palmitoylation of an N-terminal cysteine cluster together with a basic, lipid-binding surface on its ARM-repeat rod [nakatsu-2012-pi4kiiia-pm-fulltext; wu-2014-pi4k-complex-structure-fulltext]. Its C-terminal segment, which is disordered on its own, folds on binding the TTC7–FAM126 regulatory subunits of the PI4KA complex and so recruits the kinase to the membrane [suresh-2024b-efr3-recruitment-abstract; suresh-2023-pi4ka-review-abstract]. Through this role EFR3A supports plasma-membrane identity, phosphoinositide-dependent signalling through PLC and PI3K, GPCR responsiveness, PI4P-driven phosphatidylserine transport at ER–plasma membrane contact sites, and the membrane localisation and signalling of oncogenic KRAS [nakatsu-2012-pi4kiiia-pm-abstract; bojjireddy-2015-efr3-palmitoylation-abstract; adhikari-2021-kras-efr3a-abstract; gannaban-2026-glycosphingolipids-abstract].

One caveat matters for annotating this particular entry. Our alignment shows that the A0A9L0S4L8 isoform starts with "MID" in place of the first ~28 residues of canonical EFR3A. It therefore lacks the conserved N-terminal Cys-rich motif (CCCC at human residues 6–9). Experiments have shown that this motif is the palmitoylation site that EFR3A needs to reach the plasma membrane [notes-sequence-analysis; nakatsu-2012-pi4kiiia-pm-fulltext]. The full-length horse product of the same gene (A0A3Q2GU27, 821 aa) keeps the motif. If the A0A9L0S4L8 transcript is real and not a gene-model artefact, its product may be mostly cytosolic. The inferred functions below apply most directly to the canonical, palmitoylated EFR3A protein.

## 2. Identity verification, gene structure and domain architecture

A0A9L0S4L8 is 796 residues long (89.9 kDa) and is annotated only at protein existence level 3, "inferred from homology". Its descriptive annotations (PI4K complex subunit, cell membrane, lipid anchor, palmitate) were all transferred automatically by ARBA rules [uniprot-A0A9L0S4L8]. A global alignment with human EFR3A (Q14156, 821 aa) gives 783 identical positions, 13 substitutions and one 25-residue N-terminal gap. Across the remaining ~770 residues, horse residue *n* corresponds to human residue *n*+25 [notes-sequence-analysis]. The family, PANTHER subfamily, Pfam domain and residue-level identity all agree, so this is the horse orthologue of EFR3A rather than of the paralogue EFR3B or an unrelated protein that shares the symbol.

Structural work on yeast Efr3 showed that the N-terminal two-thirds of the protein consists of α-helical repeats that fold into an elongated rod. The C-terminal region is largely unstructured [wu-2014-pi4k-complex-structure-abstract]. Reviews of mammalian EFR3A describe the same arrangement: an extended superhelical ARM-like rod in the first two-thirds of the protein and a triple-helical motif in the C-terminal part [trybus-2025-efr3a-review-abstract]. This matches the horse domain annotation, in which the EFR3-like ARM-repeat domain covers residues 12–644 and the C-terminal ~150 residues carry no domain assignment [uniprot-A0A9L0S4L8]. Higher vertebrates have two paralogous genes, EFR3A and EFR3B, and each produces several isoforms [trybus-2025-efr3a-review-abstract]. The two paralogues are broadly co-expressed and overlap in function [marekbukowiec-2025-efr3a-disease-abstract].

Whether the protein lacks its N-terminal anchor depends on which isoform is meant, so isoform structure matters here. NCBI Gene (GeneID 100057838) places horse EFR3A on chromosome 9 (NC_091692.1, 27 exons) and lists four classes of RefSeq model protein. Isoform X1 (XP_005613338.1, 821 aa) begins with the canonical MPTRVCCCC… palmitoylation motif, and so does X3 (XP_005613342.1, 728 aa). Isoforms X2 (785 aa) and X4 (692 aa) start at an internal methionine equivalent to human Met37 (MEKLTFYAV…) and therefore lack the motif [ncbi-refseq-horse-efr3a-isoforms; notes-sequence-analysis]. Humans have an N-terminally truncated form as well. Isoform 2 of human EFR3A (VSP_022217) is missing residues 1–36, which removes the Cys cluster, and it is supported by a full-ORF cDNA clone from the German cDNA Consortium [uniprot-Q14156; bechtel-2007-german-cdna-orf-abstract]. A0A9L0S4L8 begins "MID-KDGLVKADMEKL…", 11 residues upstream of that Met37-equivalent, so it implies yet another alternative first exon or start site [notes-sequence-analysis]. Two independent annotation pipelines (Ensembl and NCBI Gnomon) predict horse EFR3A products without the palmitoylation motif, and the human orthologue has a cDNA-supported form of the same kind. A short, non-palmitoylated EFR3A variant therefore looks like a plausible conserved feature and not simply a gene-model error, although the exact start of A0A9L0S4L8 remains unverified.

## 3. Molecular function: a membrane scaffold for the PI4KIIIα complex

The EFR3 function was first worked out in *Saccharomyces cerevisiae*. There, the PI 4-kinase Stt4 makes plasma-membrane PtdIns4P in cortical "PIK patches". Efr3 is a membrane protein that is essential for both Ypp1 (the TTC7 orthologue) and Stt4 to assemble at these patches [baird-2008-stt4-complex-abstract]. Nakatsu and colleagues then showed that the mammalian orthologue PI4KIIIα, previously thought to sit in the ER, is targeted to the plasma membrane as part of an evolutionarily conserved complex with EFR3 and TTC7. They also showed that EFR3/rolling blackout is a palmitoylated peripheral scaffold and not a transmembrane lipase, as had earlier been proposed [nakatsu-2012-pi4kiiia-pm-fulltext; huang-2004-rolling-blackout-abstract]. Chung and colleagues confirmed that PI4KIIIα reaches the plasma membrane only when both EFR3 and TTC7 are present. EFR3 is the membrane-anchored component, and it recruits PI4KIIIα indirectly through TTC7 [chung-2015-pi4kiiia-plasticity-fulltext].

The metazoan complex has a further subunit, FAM126A (hyccin) or its paralogue FAM126B. FAM126A is an intrinsic component of the plasma-membrane PI4KIIIα–TTC7–EFR3 complex and is needed for its stability [baskin-2016-fam126a-abstract]. The PI4KIIIα–TTC7–FAM126 core is an obligate ~700-kDa dimer of heterotrimers. It presents a broad, membrane-facing surface, and the kinase active sites point toward that surface [lees-2017-pi4kiiia-architecture-abstract; dornan-2018-pi4ka-ttc7-fam126-abstract]. EFR3 is absent from this soluble core. It is the membrane receptor that docks it, and it binds TTC7/Ypp1 rather than PI4KA itself [suresh-2023-pi4ka-review-abstract]. UniProt therefore describes the complete complex as PI4KA, EFR3 (EFR3A or EFR3B), TTC7 (TTC7A or TTC7B) and HYCC (HYCC1/FAM126A or HYCC2/FAM126B) [uniprot-Q14156; salter-2021-pi4ka-variants-abstract].

The structural basis of recruitment is now known for EFR3A itself. Suresh and colleagues solved a cryo-EM structure of a C-terminal EFR3A fragment (residues 721–791, modelled 724–787) bound to PI4KA–TTC7B–FAM126A. The EFR3A C-terminus changes from disordered to ordered on binding and forms a triple-helical motif that contacts both TTC7B and FAM126A. The TTC7B interface is mainly hydrophobic, about 800 Å², and involves helix α1 (residues 728–735) and the second half of helix α3 (761–785) [suresh-2024b-efr3-recruitment-fulltext]. Mutations that disrupt this interface on either side reduce PI4KA recruitment to the plasma membrane, and phosphorylation sites and disease-associated variants map to it [suresh-2024b-efr3-recruitment-abstract]. In horse A0A9L0S4L8 this module corresponds to roughly residues 696–766. It is essentially identical to the human sequence; the only change in the 42 C-terminal residues is a conservative I→V substitution [notes-sequence-analysis]. Binding studies with every EFR3–TTC7–FAM126 combination found similar affinities for most, but the EFR3A–TTC7B–FAM126A combination bound about 10-fold more tightly [suresh-2025-ttc7b-nanobody-abstract].

The scaffold arrangement is even older than the split between fungi and animals. In *Arabidopsis thaliana*, PI4Kα1 is tethered to the plasma membrane by a complex of NO-POLLEN-GERMINATION proteins (TTC7-like), EFR3-OF-PLANTS (EFOP) proteins and HYCCIN-containing proteins. Synthetic mis-targeting experiments show that lipid anchoring and scaffolding together localise the kinase, and that this localisation is required for function [noack-2022-plant-pi4k-efop-abstract]. The EFR3–TTC7–hyccin–PI4KIIIα module, with EFR3 as the lipid-anchored base, therefore appears to be an ancestral eukaryotic device for making plasma-membrane PI4P. This strengthens the inference that the horse orthologue does the same job.

## 4. Membrane anchoring, palmitoylation and subcellular localisation

EFR3A acts at the cytoplasmic leaflet of the plasma membrane. In mammalian cells, FLAG-tagged EFR3A and EFR3B are palmitoylated on an N-terminal Cys-rich motif that is conserved across metazoa. Palmitoylation-deficient mutants (C6S/C7S/C8S/C9S in EFR3A) stay in the cytosol, and the corresponding EFR3B mutant can no longer recruit TTC7B or PI4KIIIα to the plasma membrane [nakatsu-2012-pi4kiiia-pm-fulltext]. Bojjireddy and colleagues independently found that EFR3s are palmitoylated plasma-membrane proteins with a small cytosolic pool [bojjireddy-2015-efr3-palmitoylation-abstract]. UniProt's experimentally supported annotation of human EFR3A is accordingly "cell membrane; lipid anchor", with a minor cytosolic fraction [uniprot-Q14156].

A second, electrostatic anchor sits in the ARM-repeat rod. In yeast Efr3 a conserved basic patch at one end of the rod binds acidic phospholipids that are enriched in the plasma membrane, and mutating this patch weakens liposome binding [wu-2014-pi4k-complex-structure-fulltext]. Palmitoylation also does more than tether the protein. In EFR3B, different patterns of double palmitoylation within the tri-cysteine motif create distinct "lipoforms". These lipoforms partition differently between liquid-ordered and liquid-disordered regions of the membrane and differ in how they interact with TMEM150A, which in turn sets how PI4KIIIα is divided between two complexes [batrouni-2022-palmitoylation-code-abstract]. Consistent with this, EFR3A is found in cholesterol-sensitive detergent-resistant membranes and interacts with flotillin-2. Its knockdown lowers plasma-membrane lipid order, which points to a possible role in organising raft-like domains [trybus-2023-efr3a-raft-abstract]. Plasma-membrane retention of EFR3A also depends on the outer-leaflet lipid environment: blocking synthesis of the glycosphingolipids GM3 or SM4 displaces both EFR3A and PI4KIIIα from the plasma membrane [gannaban-2026-glycosphingolipids-abstract].

For the horse entry, these findings point to a specific risk. Because A0A9L0S4L8 lacks the N-terminal CCCC motif [notes-sequence-analysis], its automatic "Lipid-anchor; Palmitate" keywords [uniprot-A0A9L0S4L8] are probably wrong for this isoform. It may still reach the membrane in part through the basic-patch mechanism or by binding membrane-associated partners, but this has not been tested. The plasma membrane (GO:0005886) is the right cellular-component term for the canonical gene product.

## 5. Pathways: plasma-membrane phosphoinositide homeostasis and downstream signalling

PI4KIIIα, positioned by EFR3, makes most of the plasma-membrane PI4P. This pool acts directly on effectors and also feeds PI(4,5)P2 synthesis by PI4P 5-kinases, and from there PLC, PI3K and other downstream outputs [suresh-2023-pi4ka-review-abstract; nakatsu-2012-pi4kiiia-pm-abstract]. Knocking out PI4KIIIα causes a profound loss of plasma-membrane PI4P. PI(4,5)P2 falls only modestly overall, because PIP5Ks are up-regulated, but much of the PI(4,5)P2 and of the proteins normally restricted to the plasma membrane ends up on intracellular membranes. The EFR3–PI4KIIIα axis therefore helps define plasma-membrane identity [nakatsu-2012-pi4kiiia-pm-abstract].

The pathway connects closely to receptor-driven PLC signalling. In *Drosophila*, temperature-sensitive mutants of the EFR3 orthologue *rolling blackout* (*rbo*) lose phototransduction within minutes. They show activity-dependent depletion of DAG and accumulation of PIP and PIP2, which indicates a failure of the G-protein–PLC–TRP signalling cycle [huang-2004-rolling-blackout-abstract]. *rbo* mutants also have defects in bulk endocytosis at synapses and in non-neuronal cells, while clathrin-mediated endocytosis is unaffected [vijayakrishnan-2009-rbo-endocytosis-abstract]. In mammalian cells, the TMEM150A-containing form of the complex acts in rapid PI(4,5)P2 resynthesis after PLC activation [chung-2015-pi4kiiia-plasticity-abstract; batrouni-2022-palmitoylation-code-abstract]. Depleting EFR3A and EFR3B together impaired the sustained Ca²⁺ response to angiotensin II through AT1a receptors, raised basal receptor phosphorylation and sped up Gq desensitisation, while plasma-membrane phosphoinositide recovery was barely affected. This suggests a role in regulating GPCR phosphorylation state, although whether it is direct or indirect is unclear [bojjireddy-2015-efr3-palmitoylation-abstract; uniprot-Q14156]. A more recent preprint reports that rapid resensitisation of AT1 receptors requires their EFR3-dependent sorting, together with a PIP5K1A-generated PI(4,5)P2 pool, into an AP2-positive plasma-membrane compartment [gulyas-2025-gpcr-resensitization-abstract]. EFR3A knockdown also disturbs EGFR and PLCγ phosphorylation and EGF-induced Ca²⁺ signalling [trybus-2023-efr3a-raft-abstract].

A second downstream branch is non-vesicular lipid transport at ER–plasma membrane contact sites. There, ORP5 and ORP8 move phosphatidylserine (PS) to the plasma membrane in exchange for PI4P, using the PI4P gradient that PI4KIIIα maintains. Removing EFR3A or PI4KA lowers plasma-membrane PI4P and PS [adhikari-2021-kras-efr3a-abstract; gannaban-2026-glycosphingolipids-abstract]. This matters for KRAS, which needs plasma-membrane PS to localise and signal. EFR3A turned up in RAS proximity-labelling interactomes and binds oncogenic KRAS preferentially. Losing EFR3A or PI4KA reduces plasma-membrane KRAS, oncogenic signalling and tumorigenesis, and artificially tethering PI4KA to the plasma membrane rescues these defects. This shows that EFR3A acts here mainly through PI4KA recruitment [adhikari-2021-kras-efr3a-abstract; adhikari-2021-kras-efr3a-fulltext].

EFR3 also takes part in insulin signalling and in metabolic stress responses. In 3T3-L1 adipocytes, knocking down EFR3 or PI4KIIIα impairs insulin-stimulated glucose transport. Super-resolution imaging shows that EFR3 knockdown blocks the insulin-stimulated dispersal of GLUT4 within the plasma membrane after vesicle fusion [koester-2022-efr3-glut4-abstract]. In *Drosophila*, hypoxia and ATP depletion cause an acute, reversible loss of plasma-membrane PI4P and PI(4,5)P2, which releases polybasic polarity proteins from the membrane. Normal homeostasis and recovery of these lipids require PI4KIIIα and its targeting factors Rbo/EFR3 and TTC7 [lu-2022-hypoxia-pi4p-abstract]. Both studies point the same way: EFR3's physiological effects follow from its control over the size of the plasma-membrane PI4P/PI(4,5)P2 pool and how quickly that pool turns over.

## 6. Regulation of EFR3-dependent recruitment

Several mechanisms tune how much PI4KIIIα EFR3 recruits. In yeast, phosphorylation of the unstructured Efr3 C-terminus weakens binding to Ypp1 [wu-2014-pi4k-complex-structure-abstract]. In mammals, phosphorylation of EFR3B likewise lowers its affinity for TTC7–FAM126 [suresh-2025-ttc7b-nanobody-abstract], and several post-translational modification sites map to the EFR3A C-terminal interface [suresh-2024b-efr3-recruitment-abstract]. The complex can also reorganise: TMEM150A strongly reduces TTC7 association with EFR3–PI4KIIIα without removing PI4KIIIα from the plasma membrane [chung-2015-pi4kiiia-plasticity-abstract]. The palmitoylation "code" on EFR3 then controls how PI4KIIIα is divided between the TTC7-containing and TMEM150A-containing assemblies [batrouni-2022-palmitoylation-code-abstract]. As a tool for studying this, a TTC7B-selective nanobody that sterically blocks EFR3 binding lowers PI4KA membrane recruitment and plasma-membrane PI4P [suresh-2025-ttc7b-nanobody-abstract]. The complex is also controlled by dephosphorylation. The palmitoylated calcineurin isoform CNAβ1 localises to the plasma membrane and associates with the EFR3B–PI4KA–TTC7B–FAM126A complex, where it uses a docking motif in the FAM126A tail. Calcineurin inhibitors reduce PI4P production during Gq-coupled GPCR signalling, which suggests that Ca²⁺/calcineurin signalling feeds back to support PI4KA complex activity [ulengintalkish-2021-calcineurin-pi4k-abstract]. This study used EFR3B, so the EFR3A-containing complex has not been tested directly.

## 7. Physiological roles and disease associations (from other mammals)

Mouse genetics points to a role in the nervous system, although how this links to the PI4K mechanism is not yet worked out. Deleting Efr3a specifically in the brain increased the survival and maturation of adult-born hippocampal neurons and raised BDNF–TrkB signalling [qian-2017-efr3a-neurogenesis-abstract]. Partial loss of Efr3a reduced spiral ganglion neuron degeneration after drug-induced hair-cell loss and in early ageing, together with higher p-Akt and neurotrophic signalling [hu-2017b-efr3a-spiral-ganglion-abstract; hu-2017-efr3a-hearing-loss-abstract]. In humans, rare deleterious missense variants in EFR3A are enriched in autism spectrum disorder, and EFR3A is expressed in developing cortical neurons [gupta-2014-efr3a-autism-abstract]. Its paralogue has a non-redundant role in the brain: deleting Efr3b in mouse brain lowers CA2 pyramidal-neuron excitability and impairs social novelty recognition [wei-2024-efr3b-social-abstract]. EFR3A and EFR3B can therefore not fully substitute for each other in vivo. Mutations in other subunits of the complex cause hypomyelinating leukodystrophy (FAM126A, PI4KA) and intestinal and immune disease (TTC7A, PI4KA), which shows that the complex as a whole is needed in many tissues [baskin-2016-fam126a-abstract; salter-2021-pi4ka-variants-abstract]. Reviews add associations of EFR3A with cardiovascular disorders and several cancers [marekbukowiec-2025-efr3a-disease-abstract; trybus-2025-efr3a-review-abstract]. No horse phenotype or disease association has been reported.

## 8. Implications for functional annotation of A0A9L0S4L8

Taken together, the best-supported annotations for horse EFR3A (by orthology to human and mouse EFR3A, with conserved mechanism back to yeast Efr3) are as follows. For cellular component: plasma membrane, specifically the cytoplasmic side as a peripheral, lipid-anchored protein, as part of the phosphatidylinositol 4-kinase complex with PI4KA, TTC7 and FAM126/HYCC [nakatsu-2012-pi4kiiia-pm-fulltext; baskin-2016-fam126a-abstract; uniprot-Q14156]. For molecular function: a scaffold or adaptor activity that recruits the PI4KA–TTC7–FAM126 complex to the plasma membrane, mediated by C-terminal binding to TTC7 and FAM126 and by membrane binding through palmitoylation and a basic patch. EFR3A has no catalytic activity of its own [wu-2014-pi4k-complex-structure-abstract; suresh-2024b-efr3-recruitment-abstract]. For biological process: protein localisation to the plasma membrane, and phosphatidylinositol phosphate biosynthesis (PI → PI4P at the plasma membrane) together with the downstream PI(4,5)P2 homeostasis. Regulation of GPCR signalling and desensitisation is a more peripheral annotation [nakatsu-2012-pi4kiiia-pm-abstract; bojjireddy-2015-efr3-palmitoylation-abstract]. Annotators should keep in mind that this specific isoform lacks the palmitoylation motif. It may be better to propagate full annotations to the canonical horse EFR3A entry (A0A3Q2GU27) or the RefSeq isoform X1 (XP_005613338.1). Annotations for A0A9L0S4L8 should be limited to what the C-terminal TTC7/FAM126-binding module and the ARM rod support, namely PI4K complex binding, until its membrane association is tested [notes-sequence-analysis; ncbi-refseq-horse-efr3a-isoforms]. Insulin-stimulated glucose transport is an additional, more peripheral process supported by adipocyte data [koester-2022-efr3-glut4-abstract].

## Open Questions

First, it is unclear whether the A0A9L0S4L8 transcript (ENSECAT00000116354), which lacks the first coding exon and the CCCC palmitoylation motif, is a real horse mRNA isoform or a gene-prediction artefact. Horse RNA-seq or long-read transcript data would settle this. If it is real, localisation experiments would show whether the truncated protein is cytosolic and whether it acts as a dominant-negative "sink" for TTC7–FAM126, which the intact C-terminal binding module would allow. Related to this, it is not known how short, non-palmitoylated EFR3A isoforms (human isoform 2, horse RefSeq X2/X4) are expressed across tissues or what they do [bechtel-2007-german-cdna-orf-abstract; ncbi-refseq-horse-efr3a-isoforms]. Ensembl's REST service was unavailable during this research, so the transcript support for ENSECAT00000116354 could not be checked. Second, the relative contributions of EFR3A and EFR3B, and of the different TTC7 and FAM126 paralogues, to PI4KA recruitment in specific tissues are not resolved for any species. This is especially true for equine tissues such as skeletal muscle and the nervous system, and tissue proteomics would help. Third, it is still not known how EFR3 controls GPCR phosphorylation and resensitisation: whether through local PI(4,5)P2 pools, β-arrestin and AP2 sorting, or interactions with kinases and phosphatases such as calcineurin [ulengintalkish-2021-calcineurin-pi4k-abstract; bojjireddy-2015-efr3-palmitoylation-abstract; gulyas-2025-gpcr-resensitization-abstract]. Fourth, it remains open whether the reported EFR3A interactions with KRAS and flotillin-2 are direct and whether they work independently of PI4KA [adhikari-2021-kras-efr3a-abstract; trybus-2023-efr3a-raft-abstract]. Fifth, the full-length structure of EFR3A on a membrane, including how the ARM rod, the basic patch and the palmitoyl chains orient the PI4KA dimer of trimers toward its substrate, has not been determined [lees-2017-pi4kiiia-architecture-abstract; suresh-2024b-efr3-recruitment-abstract]. Finally, the neuroprotective effects of reduced Efr3a in mouse hippocampus and cochlea have not been mechanistically linked to PI4P synthesis. Comparative work in horses, where neurodegenerative and myelin disorders are clinically important, could be informative.

## References

- **adhikari-2021-kras-efr3a**: Adhikari H, Kattan WE, Kumar S, Zhou P, Hancock JF, Counter CM (2021). Oncogenic KRAS is dependent upon an EFR3A-PI4KA signaling axis for potent tumorigenic activity. *Nature communications* 12:5248. PMID: 34504076; PMCID: PMC8429657; DOI: 10.1038/s41467-021-25523-5. https://pubmed.ncbi.nlm.nih.gov/34504076/
- **baird-2008-stt4-complex**: Baird D, Stefan C, Audhya A, Weys S, Emr SD (2008). Assembly of the PtdIns 4-kinase Stt4 complex at the plasma membrane requires Ypp1 and Efr3. *The Journal of cell biology* 183:1061-74. PMID: 19075114; PMCID: PMC2600738; DOI: 10.1083/jcb.200804003. https://pubmed.ncbi.nlm.nih.gov/19075114/
- **baskin-2016-fam126a**: Baskin JM, Wu X, Christiano R, Oh MS, Schauder CM, Gazzerro E et al. (2016). The leukodystrophy protein FAM126A (hyccin) regulates PtdIns(4)P synthesis at the plasma membrane. *Nature cell biology* 18:132-8. PMID: 26571211; PMCID: PMC4689616; DOI: 10.1038/ncb3271. https://pubmed.ncbi.nlm.nih.gov/26571211/
- **batrouni-2022-palmitoylation-code**: Batrouni AG, Bag N, Phan HT, Baird BA, Baskin JM (2022). A palmitoylation code controls PI4KIIIα complex formation and PI(4,5)P2 homeostasis at the plasma membrane. *Journal of cell science* 135:. PMID: 34569608; PMCID: PMC8592054; DOI: 10.1242/jcs.259365. https://pubmed.ncbi.nlm.nih.gov/34569608/
- **bechtel-2007-german-cdna-orf**: Bechtel S, Rosenfelder H, Duda A, Schmidt CP, Ernst U, Wellenreuther R et al. (2007). The full-ORF clone resource of the German cDNA Consortium. *BMC genomics* 8:399. PMID: 17974005; PMCID: PMC2213676; DOI: 10.1186/1471-2164-8-399. https://pubmed.ncbi.nlm.nih.gov/17974005/
- **bojjireddy-2015-efr3-palmitoylation**: Bojjireddy N, Guzman-Hernandez ML, Reinhard NR, Jovic M, Balla T (2015). EFR3s are palmitoylated plasma membrane proteins that control responsiveness to G-protein-coupled receptors. *Journal of cell science* 128:118-28. PMID: 25380825; PMCID: PMC4282049; DOI: 10.1242/jcs.157495. https://pubmed.ncbi.nlm.nih.gov/25380825/
- **chung-2015-pi4kiiia-plasticity**: Chung J, Nakatsu F, Baskin JM, De Camilli P (2015). Plasticity of PI4KIIIα interactions at the plasma membrane. *EMBO reports* 16:312-20. PMID: 25608530; PMCID: PMC4364870; DOI: 10.15252/embr.201439151. https://pubmed.ncbi.nlm.nih.gov/25608530/
- **dornan-2018-pi4ka-ttc7-fam126**: Dornan GL, Dalwadi U, Hamelin DJ, Hoffmann RM, Yip CK, Burke JE (2018). Probing the Architecture, Dynamics, and Inhibition of the PI4KIIIα/TTC7/FAM126 Complex. *Journal of molecular biology* 430:3129-3142. PMID: 30031006; DOI: 10.1016/j.jmb.2018.07.020. https://pubmed.ncbi.nlm.nih.gov/30031006/
- **gannaban-2026-glycosphingolipids**: Gannaban R, Ali S, Chen W, Nguyen M, Lai L, Moore TI et al. (2026). Glycosphingolipids regulate phosphatidylserine transport machinery that operates at ER-PM contact sites. *Nature communications* 17:. PMID: 42286018; PMCID: PMC13408342; DOI: 10.1038/s41467-026-74252-0. https://pubmed.ncbi.nlm.nih.gov/42286018/
- **gulyas-2025-gpcr-resensitization**: Gulyas G, Baba T, Toth DJ, Inoue A, Balla T (2025). FAST RESENSITIZATION OF G PROTEIN-COUPLED RECEPTORS REQUIRES THEIR PI(4,5)P2-DEPENDENT SORTING INTO AN AP2 POSITIVE COMPARTMENT. *bioRxiv : the preprint server for biology* :. PMID: 40568163; PMCID: PMC12190482; DOI: 10.1101/2025.03.28.645988. https://pubmed.ncbi.nlm.nih.gov/40568163/
- **gupta-2014-efr3a-autism**: Gupta AR, Pirruccello M, Cheng F, Kang HJ, Fernandez TV, Baskin JM et al. (2014). Rare deleterious mutations of the gene EFR3A in autism spectrum disorders. *Molecular autism* 5:31. PMID: 24860643; PMCID: PMC4032628; DOI: 10.1186/2040-2392-5-31. https://pubmed.ncbi.nlm.nih.gov/24860643/
- **hu-2017-efr3a-hearing-loss**: Hu H, Ma Y, Ye B, Wang Q, Yang T, Lv J et al. (2017). The role of Efr3a in age-related hearing loss. *Neuroscience* 341:1-8. PMID: 27867060; DOI: 10.1016/j.neuroscience.2016.11.013. https://pubmed.ncbi.nlm.nih.gov/27867060/
- **hu-2017b-efr3a-spiral-ganglion**: Hu H, Ye B, Zhang L, Wang Q, Liu Z, Ji S et al. (2017). Efr3a Insufficiency Attenuates the Degeneration of Spiral Ganglion Neurons after Hair Cell Loss. *Frontiers in molecular neuroscience* 10:86. PMID: 28424585; PMCID: PMC5372784; DOI: 10.3389/fnmol.2017.00086. https://pubmed.ncbi.nlm.nih.gov/28424585/
- **huang-2004-rolling-blackout**: Huang FD, Matthies HJ, Speese SD, Smith MA, Broadie K (2004). Rolling blackout, a newly identified PIP2-DAG pathway lipase required for Drosophila phototransduction. *Nature neuroscience* 7:1070-8. PMID: 15361878; DOI: 10.1038/nn1313. https://pubmed.ncbi.nlm.nih.gov/15361878/
- **koester-2022-efr3-glut4**: Koester AM, Geiser A, Laidlaw KME, Morris S, Cutiongco MFA, Stirrat L et al. (2022). EFR3 and phosphatidylinositol 4-kinase IIIα regulate insulin-stimulated glucose transport and GLUT4 dispersal in 3T3-L1 adipocytes. *Bioscience reports* 42:. PMID: 35735144; PMCID: PMC9272592; DOI: 10.1042/BSR20221181. https://pubmed.ncbi.nlm.nih.gov/35735144/
- **lees-2017-pi4kiiia-architecture**: Lees JA, Zhang Y, Oh MS, Schauder CM, Yu X, Baskin JM et al. (2017). Architecture of the human PI4KIIIα lipid kinase complex. *Proceedings of the National Academy of Sciences of the United States of America* 114:13720-13725. PMID: 29229838; PMCID: PMC5748228; DOI: 10.1073/pnas.1718471115. https://pubmed.ncbi.nlm.nih.gov/29229838/
- **lu-2022-hypoxia-pi4p**: Lu J, Dong W, Hammond GR, Hong Y (2022). Hypoxia controls plasma membrane targeting of polarity proteins by dynamic turnover of PI4P and PI(4,5)P2. *eLife* 11:. PMID: 35678383; PMCID: PMC9242647; DOI: 10.7554/eLife.79582. https://pubmed.ncbi.nlm.nih.gov/35678383/
- **marekbukowiec-2025-efr3a-disease**: Marek-Bukowiec K, Trybus M, Hryniewicz-Jankowska A, Czogalla A, Sikorski AF (2025). A Potential Role of EFR3A in Human Disease States. *Biomolecules* 15:. PMID: 40305161; PMCID: PMC12024565; DOI: 10.3390/biom15040466. https://pubmed.ncbi.nlm.nih.gov/40305161/
- **nakatsu-2012-pi4kiiia-pm**: Nakatsu F, Baskin JM, Chung J, Tanner LB, Shui G, Lee SY et al. (2012). PtdIns4P synthesis by PI4KIIIα at the plasma membrane and its impact on plasma membrane identity. *The Journal of cell biology* 199:1003-16. PMID: 23229899; PMCID: PMC3518224; DOI: 10.1083/jcb.201206095. https://pubmed.ncbi.nlm.nih.gov/23229899/
- **noack-2022-plant-pi4k-efop**: Noack LC, Bayle V, Armengot L, Rozier F, Mamode-Cassim A, Stevens FD et al. (2022). A nanodomain-anchored scaffolding complex is required for the function and localization of phosphatidylinositol 4-kinase alpha in plants. *The Plant cell* 34:302-332. PMID: 34010411; PMCID: PMC8774046; DOI: 10.1093/plcell/koab135. https://pubmed.ncbi.nlm.nih.gov/34010411/
- **qian-2017-efr3a-neurogenesis**: Qian Q, Liu Q, Zhou D, Pan H, Liu Z, He F et al. (2017). Brain-specific ablation of Efr3a promotes adult hippocampal neurogenesis via the brain-derived neurotrophic factor pathway. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology* 31:2104-2113. PMID: 28193719; DOI: 10.1096/fj.201601207R. https://pubmed.ncbi.nlm.nih.gov/28193719/
- **salter-2021-pi4ka-variants**: Salter CG, Cai Y, Lo B, Helman G, Taylor H, McCartney A et al. (2021). Biallelic PI4KA variants cause neurological, intestinal and immunological disease. *Brain : a journal of neurology* 144:3597-3610. PMID: 34415310; PMCID: PMC8719846; DOI: 10.1093/brain/awab313. https://pubmed.ncbi.nlm.nih.gov/34415310/
- **suresh-2023-pi4ka-review**: Suresh S, Burke JE (2023). Structural basis for the conserved roles of PI4KA and its regulatory partners and their misregulation in disease. *Advances in biological regulation* 90:100996. PMID: 37979461; DOI: 10.1016/j.jbior.2023.100996. https://pubmed.ncbi.nlm.nih.gov/37979461/
- **suresh-2024-efr3-recruitment**: Suresh S, Shaw AL, Pemberton JG, Scott MK, Harris NJ, Parson MA et al. (2024). Molecular basis for plasma membrane recruitment of PI4KA by EFR3. *bioRxiv : the preprint server for biology* :. PMID: 38746453; PMCID: PMC11092606; DOI: 10.1101/2024.04.30.587787. https://pubmed.ncbi.nlm.nih.gov/38746453/
- **suresh-2024b-efr3-recruitment**: Suresh S, Shaw AL, Pemberton JG, Scott MK, Harris NJ, Parson MAH et al. (2024). Molecular basis for plasma membrane recruitment of PI4KA by EFR3. *Science advances* 10:eadp6660. PMID: 39705356; PMCID: PMC11661448; DOI: 10.1126/sciadv.adp6660. https://pubmed.ncbi.nlm.nih.gov/39705356/
- **suresh-2025-ttc7b-nanobody**: Suresh S, Shaw AL, Akintola DK, Lunke M, Doerr S, Rohilla P et al. (2025). Development of an inhibitory TTC7B selective nanobody that blocks EFR3 recruitment of PI4KA. *The Journal of biological chemistry* 301:110886. PMID: 41197736; PMCID: PMC12765194; DOI: 10.1016/j.jbc.2025.110886. https://pubmed.ncbi.nlm.nih.gov/41197736/
- **trybus-2023-efr3a-raft**: Trybus M, Hryniewicz-Jankowska A, Wójtowicz K, Trombik T, Czogalla A, Sikorski AF (2023). EFR3A: a new raft domain organizing protein? *Cellular & molecular biology letters* 28:86. PMID: 37880612; PMCID: PMC10601247; DOI: 10.1186/s11658-023-00497-y. https://pubmed.ncbi.nlm.nih.gov/37880612/
- **trybus-2025-efr3a-review**: Trybus M, Hryniewicz-Jankowska A, Czogalla A, Sikorski AF (2025). EFR3A, an Intriguing Gene, and Protein with a Scaffolding Function. *Cells* 14:. PMID: 40136694; PMCID: PMC11941745; DOI: 10.3390/cells14060445. https://pubmed.ncbi.nlm.nih.gov/40136694/
- **ulengintalkish-2021-calcineurin-pi4k**: Ulengin-Talkish I, Parson MAH, Jenkins ML, Roy J, Shih AZL, St-Denis N et al. (2021). Palmitoylation targets the calcineurin phosphatase to the phosphatidylinositol 4-kinase complex at the plasma membrane. *Nature communications* 12:6064. PMID: 34663815; PMCID: PMC8523714; DOI: 10.1038/s41467-021-26326-4. https://pubmed.ncbi.nlm.nih.gov/34663815/
- **vijayakrishnan-2009-rbo-endocytosis**: Vijayakrishnan N, Woodruff EA, Broadie K (2009). Rolling blackout is required for bulk endocytosis in non-neuronal cells and neuronal synapses. *Journal of cell science* 122:114-25. PMID: 19066280; PMCID: PMC2714403; DOI: 10.1242/jcs.036673. https://pubmed.ncbi.nlm.nih.gov/19066280/
- **wade-2009-horse-genome**: Wade CM, Giulotto E, Sigurdsson S, Zoli M, Gnerre S, Imsland F et al. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science (New York, N.Y.)* 326:865-7. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158. https://pubmed.ncbi.nlm.nih.gov/19892987/
- **wei-2024-efr3b-social**: Wei X, Wang J, Yang E, Zhang Y, Qian Q, Li X et al. (2024). Efr3b is essential for social recognition by modulating the excitability of CA2 pyramidal neurons. *Proceedings of the National Academy of Sciences of the United States of America* 121:e2314557121. PMID: 38190534; PMCID: PMC10801834; DOI: 10.1073/pnas.2314557121. https://pubmed.ncbi.nlm.nih.gov/38190534/
- **wu-2014-pi4k-complex-structure**: Wu X, Chi RJ, Baskin JM, Lucast L, Burd CG, De Camilli P et al. (2014). Structural insights into assembly and regulation of the plasma membrane phosphatidylinositol 4-kinase complex. *Developmental cell* 28:19-29. PMID: 24360784; PMCID: PMC4349574; DOI: 10.1016/j.devcel.2013.11.012. https://pubmed.ncbi.nlm.nih.gov/24360784/
- **uniprot-A0A9L0S4L8**: UniProtKB/TrEMBL entry A0A9L0S4L8 (Protein EFR3 homolog A, Equus caballus), entry version 15; saved as citations/uniprot-A0A9L0S4L8.txt. https://rest.uniprot.org/uniprotkb/A0A9L0S4L8.txt
- **uniprot-Q14156**: UniProtKB/Swiss-Prot entry Q14156 (EFR3A_HUMAN); saved as citations/uniprot-Q14156.txt. https://rest.uniprot.org/uniprotkb/Q14156.txt
- **ncbi-refseq-horse-efr3a-isoforms**: NCBI Gene 100057838 (EFR3A, Equus caballus) RefSeq proteins XP_005613338.1, XP_005613339.1, XP_005613342.1, XP_070077931.1; saved as citations/ncbi-refseq-horse-efr3a-isoforms.fasta. https://www.ncbi.nlm.nih.gov/gene/100057838
- **notes-sequence-analysis**: This study's alignment of A0A9L0S4L8 with human Q14156 and comparison with sibling horse EFR3A entries and RefSeq isoforms; see notes-sequence-analysis.md.


## Citations

1. adhikari-2021-kras-efr3a-abstract.md
2. adhikari-2021-kras-efr3a-fulltext.txt
3. adhikari-2021-kras-efr3a-summary.md
4. baird-2008-stt4-complex-abstract.md
5. baird-2008-stt4-complex-fulltext.txt
6. baird-2008-stt4-complex-summary.md
7. baskin-2016-fam126a-abstract.md
8. baskin-2016-fam126a-fulltext.txt
9. baskin-2016-fam126a-summary.md
10. batrouni-2022-palmitoylation-code-abstract.md
11. batrouni-2022-palmitoylation-code-summary.md
12. bechtel-2007-german-cdna-orf-abstract.md
13. bechtel-2007-german-cdna-orf-summary.md
14. bojjireddy-2015-efr3-palmitoylation-abstract.md
15. bojjireddy-2015-efr3-palmitoylation-summary.md
16. chung-2015-pi4kiiia-plasticity-abstract.md
17. chung-2015-pi4kiiia-plasticity-fulltext.txt
18. chung-2015-pi4kiiia-plasticity-summary.md
19. citation_links.json
20. dornan-2018-pi4ka-ttc7-fam126-abstract.md
21. dornan-2018-pi4ka-ttc7-fam126-summary.md
22. gannaban-2026-glycosphingolipids-abstract.md
23. gannaban-2026-glycosphingolipids-fulltext.txt
24. gannaban-2026-glycosphingolipids-summary.md
25. gulyas-2025-gpcr-resensitization-abstract.md
26. gulyas-2025-gpcr-resensitization-fulltext.txt
27. gulyas-2025-gpcr-resensitization-summary.md
28. gupta-2014-efr3a-autism-abstract.md
29. gupta-2014-efr3a-autism-fulltext.txt
30. gupta-2014-efr3a-autism-summary.md
31. hu-2017-efr3a-hearing-loss-abstract.md
32. hu-2017-efr3a-hearing-loss-summary.md
33. hu-2017b-efr3a-spiral-ganglion-abstract.md
34. hu-2017b-efr3a-spiral-ganglion-fulltext.txt
35. hu-2017b-efr3a-spiral-ganglion-summary.md
36. huang-2004-rolling-blackout-abstract.md
37. huang-2004-rolling-blackout-summary.md
38. koester-2022-efr3-glut4-abstract.md
39. koester-2022-efr3-glut4-fulltext.txt
40. koester-2022-efr3-glut4-summary.md
41. lees-2017-pi4kiiia-architecture-abstract.md
42. lees-2017-pi4kiiia-architecture-summary.md
43. lu-2022-hypoxia-pi4p-abstract.md
44. lu-2022-hypoxia-pi4p-fulltext.txt
45. lu-2022-hypoxia-pi4p-summary.md
46. marekbukowiec-2025-efr3a-disease-abstract.md
47. marekbukowiec-2025-efr3a-disease-fulltext.txt
48. marekbukowiec-2025-efr3a-disease-summary.md
49. metadata.json
50. nakatsu-2012-pi4kiiia-pm-abstract.md
51. nakatsu-2012-pi4kiiia-pm-fulltext.txt
52. nakatsu-2012-pi4kiiia-pm-summary.md
53. ncbi-refseq-horse-efr3a-isoforms.fasta
54. noack-2022-plant-pi4k-efop-abstract.md
55. noack-2022-plant-pi4k-efop-fulltext.txt
56. noack-2022-plant-pi4k-efop-summary.md
57. qian-2017-efr3a-neurogenesis-abstract.md
58. qian-2017-efr3a-neurogenesis-summary.md
59. salter-2021-pi4ka-variants-abstract.md
60. salter-2021-pi4ka-variants-fulltext.txt
61. salter-2021-pi4ka-variants-summary.md
62. suresh-2023-pi4ka-review-abstract.md
63. suresh-2023-pi4ka-review-summary.md
64. suresh-2024-efr3-recruitment-abstract.md
65. suresh-2024-efr3-recruitment-fulltext.txt
66. suresh-2024-efr3-recruitment-summary.md
67. suresh-2024b-efr3-recruitment-abstract.md
68. suresh-2024b-efr3-recruitment-fulltext.txt
69. suresh-2024b-efr3-recruitment-summary.md
70. suresh-2025-ttc7b-nanobody-abstract.md
71. suresh-2025-ttc7b-nanobody-fulltext.txt
72. suresh-2025-ttc7b-nanobody-summary.md
73. trybus-2023-efr3a-raft-abstract.md
74. trybus-2023-efr3a-raft-fulltext.txt
75. trybus-2023-efr3a-raft-summary.md
76. trybus-2025-efr3a-review-abstract.md
77. trybus-2025-efr3a-review-fulltext.txt
78. trybus-2025-efr3a-review-summary.md
79. ulengintalkish-2021-calcineurin-pi4k-abstract.md
80. ulengintalkish-2021-calcineurin-pi4k-fulltext.txt
81. ulengintalkish-2021-calcineurin-pi4k-summary.md
82. uniprot-A0A9L0S4L8.txt
83. uniprot-Q14156.txt
84. vijayakrishnan-2009-rbo-endocytosis-abstract.md
85. vijayakrishnan-2009-rbo-endocytosis-summary.md
86. wade-2009-horse-genome-abstract.md
87. wade-2009-horse-genome-summary.md
88. wei-2024-efr3b-social-abstract.md
89. wei-2024-efr3b-social-fulltext.txt
90. wei-2024-efr3b-social-summary.md
91. wu-2014-pi4k-complex-structure-abstract.md
92. wu-2014-pi4k-complex-structure-fulltext.txt
93. wu-2014-pi4k-complex-structure-summary.md