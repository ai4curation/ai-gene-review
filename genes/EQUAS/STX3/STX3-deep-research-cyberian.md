---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:10:42.972467'
end_time: '2026-10-26T01:21:30.659930'
duration_seconds: 647.69
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: STX3
  gene_symbol: STX3
  uniprot_accession: A0A9L0J901
  protein_description: 'RecName: Full=Syntaxin-3 {ECO:0000256|ARBA:ARBA00072670};'
  gene_info: Name=STX3 {ECO:0000313|Ensembl:ENSEASP00005048853.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the syntaxin family.
  protein_domains: SNARE. (IPR010989); Syntaxin. (IPR045242); Syntaxin/epimorphin_CS.
    (IPR006012); Syntaxin_N. (IPR006011); T_SNARE_dom. (IPR000727)
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
citation_count: 91
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0J901
- **Protein Description:** RecName: Full=Syntaxin-3 {ECO:0000256|ARBA:ARBA00072670};
- **Gene Information:** Name=STX3 {ECO:0000313|Ensembl:ENSEASP00005048853.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the syntaxin family.
- **Key Domains:** SNARE. (IPR010989); Syntaxin. (IPR045242); Syntaxin/epimorphin_CS. (IPR006012); Syntaxin_N. (IPR006011); T_SNARE_dom. (IPR000727)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "STX3" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'STX3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **STX3** (gene ID: STX3, UniProt: A0A9L0J901) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Syntaxin-3 (STX3) of the Donkey, *Equus asinus* (UniProt A0A9L0J901): Function, Localization and Pathways

## Introduction and Summary

UniProt entry A0A9L0J901 is an unreviewed, computationally predicted protein of 289 residues from the donkey (*Equus asinus*) reference genome, annotated as Syntaxin-3 and encoded by the gene *STX3* on donkey chromosome 17. The sequence was derived from the donkey genome assemblies described by Wang and colleagues, which provide no functional information about the gene [wang-2020-donkey-genome-abstract]. No published experimental study addresses donkey or horse STX3 directly, so every functional statement in this report is an inference by orthology from human, rodent, amphibian and fish syntaxin 3. That inference is well supported: the donkey protein is 92% identical to human and rodent STX3 over its full length, and it carries the domains that define the syntaxin family (an N-terminal peptide, the three-helix Habc regulatory domain, the SNARE/H3 motif and a C-terminal tail anchor) (see `notes/sequence_analysis.md`). The gene symbol is unambiguous. The protein family, domain composition (IPR006011 Syntaxin_N, IPR000727 t-SNARE, IPR010989 SNARE) and the literature all describe the same molecule.

Syntaxin 3 is a Qa-SNARE (t-SNARE) of the plasma membrane. It was first described as a member of the syntaxin family of tail-anchored receptors for transport vesicles; in this family, different paralogues mark different target membranes [bennett-1993-syntaxin-family-abstract]. Its core molecular function is to pair with a Qbc-SNARE (SNAP-23 or SNAP-25) and an R-SNARE on the incoming vesicle (VAMP2, VAMP7 or VAMP8, depending on the cell type) to form the four-helix trans-SNARE complex that drives membrane fusion. Sec1/Munc18 proteins (Munc18-2/STXBP2 in epithelia and mast cells, Munc18-1/STXBP1 in retinal neurons) regulate it [riento-1998-munc18-2-syntaxin3-abstract; peng-2010-munc18b-abstract; curtis-2008-syntaxin3b-ribbon-abstract]. In polarized epithelial cells, syntaxin 3 is the apical-membrane fusion receptor. An N-terminal FMDE motif targets it to the apical membrane, and that apical localization is needed for the cell to become polarized [sharma-2006-apical-targeting-abstract]. Loss of syntaxin 3 in humans causes variant microvillus inclusion disease [wiegerinck-2014-mvid-abstract]. In the retina, a splice variant, syntaxin 3B, replaces syntaxin 1 at the ribbon synapses of photoreceptors and bipolar cells, where it is needed for tonic, graded glutamate release [morgans-1996-snare-ribbon-synapse-abstract; curtis-2008-syntaxin3b-ribbon-abstract; curtis-2010-syntaxin3b-exocytosis-abstract]. Syntaxin 3 is also needed in the photoreceptor inner segment to deliver rhodopsin, peripherin-2 and ROM1 to the outer segment, and photoreceptors die without it [kakakhel-2020-stx3-photoreceptor-abstract; janecke-2021-stx3-retinal-dystrophy-abstract].

The donkey gene model is unusual. Its C-terminal half of the SNARE motif matches exactly the sequence encoded by the retina-specific 3B exons, while its transmembrane anchor matches the ubiquitous 3A form. This report therefore treats the donkey protein as a syntaxin 3 whose functions most likely mirror both the 3A (epithelial/secretory) and 3B (retinal ribbon synapse) roles, depending on which transcripts are expressed in vivo.

## Identity, Domain Architecture and Isoform Assignment of the Donkey Protein

The UniProt record classifies A0A9L0J901 as a member of the syntaxin family, predicts a single C-terminal helical transmembrane segment (residues 264–288) and calls it a single-pass type IV (tail-anchored) membrane protein. The same topology was described for the founding members of the family, in which a C-terminal hydrophobic domain anchors the protein to the cytoplasmic face of membranes [bennett-1993-syntaxin-family-abstract]. A position-by-position comparison shows 92.4% identity to human STX3 (Q13277) and 92.0% identity to mouse Stx3A (Q64704). The N-terminal 225 residues are almost invariant. They include threonine 14, the residue phosphorylated by CaMKII in syntaxin 3B [liu-2014-stx3b-camkii-abstract], and the F31-M32-D33-E34 apical targeting motif, in which F31, D33 and E34 were shown to be critical for apical sorting [sharma-2006-apical-targeting-fulltext].

Mouse syntaxin 3 exists as four splice forms. Syntaxin 3B differs from 3A in its C-terminal region, syntaxin 3C has an alternative N-terminal segment, and syntaxin 3D is an 86-residue product without a membrane anchor. Syntaxins 3A and 3B, but not 3C or 3D, bind Munc18 [ibaraki-1995-four-forms-syntaxin3-abstract]. Curtis and colleagues mapped the gene structure. Exons 1–8 encode the shared N-terminus, and three alternative exon pairs (9A/B, 10A/B and 11A/B) encode the C-terminal half of the SNARE domain and the transmembrane domain, which differ between 3A and 3B [curtis-2008-syntaxin3b-ribbon-fulltext]. In the donkey protein, residues 226–263 (GAMIDRIENNMDQSVGFVERAVADTKKAVKYQSEARRK) are identical to mouse syntaxin 3B, whereas residues 264–289 (LIIIIVIVVVLLGILALVIGLSVGLK) match the 3A transmembrane anchor rather than the divergent 3B anchor (`notes/sequence_analysis.md`). The predicted protein is therefore a 3B/3A hybrid. It may be a real transcript, or an artifact of automated gene-model building that joined the 3B SNARE exon(s) to the 3A terminal exon. The second explanation seems more likely, because the two forms are reported to be produced by coordinated use of the A or B exon sets [curtis-2008-syntaxin3b-ribbon-fulltext]. Because the 3B SNARE segment is the region that determines how strongly syntaxin binds SNAP-25 [curtis-2008-syntaxin3b-ribbon-abstract], this caveat matters for any isoform-specific annotation. The domain-level functional inference (t-SNARE activity at the plasma membrane) does not depend on it.

A survey of all equid STX3 entries in UniProt shows that this hybrid is not the only donkey product of the gene (`notes/sequence_analysis.md`). Ensembl annotates six protein-coding transcripts at the donkey *STX3* locus on chromosome 17. Among the corresponding UniProt entries are a canonical syntaxin 3A (A0A8C4LHZ8; 3A SNARE half and 3A anchor) and a canonical syntaxin 3B (A0A8C4PQW9). The 3B entry carries the 3B-specific anchor KIMIMICCVILAIILASTIGGIFA, which differs from the mouse 3B anchor at a single residue. The splicing system described in mouse and human [ibaraki-1995-four-forms-syntaxin3-abstract; curtis-2008-syntaxin3b-ribbon-fulltext; janecke-2021-stx3-retinal-dystrophy-fulltext] is therefore conserved in equids. The 3B-SNARE/3A-anchor combination of A0A9L0J901 is an additional model. The same combination is predicted independently in the horse genome annotation (A0A3Q2H352). That favors a genuine, if probably minor, transcript over a one-off error, although the two annotations may draw on similar evidence pipelines. Several donkey and horse models also lack a transmembrane anchor and end in an alternative C-terminal sequence. They resemble the soluble Stx3S isoform in architecture, though not in their tail sequence [giovannone-2018-soluble-stx3-abstract].

The human STX3B transcript was characterized only recently. It is spliced in the same way as in mouse, is expressed only in the retina, and is the major retinal *STX3* transcript (GenBank MW273340) [janecke-2021-stx3-retinal-dystrophy-fulltext]. Additional splicing produces a soluble isoform without the transmembrane domain, Stx3S, which has a nuclear function discussed below [giovannone-2018-soluble-stx3-abstract].

## Molecular Mechanism: a Munc18-Regulated Qa-SNARE

Syntaxin 3 is a bona fide t-SNARE. Liposomes carrying syntaxin 3B with SNAP-25 fuse with liposomes carrying synaptobrevin-2/VAMP2 [curtis-2008-syntaxin3b-ribbon-abstract]. In native retina, syntaxin 3 is found in complexes with SNAP-25, synaptobrevin and complexin [morgans-1996-snare-ribbon-synapse-abstract]. In epithelial cells, the cognate partners are SNAP-23 and VAMP8 or VAMP7 [peng-2010-munc18b-abstract; vogel-2015-cargo-selective-exocytosis-abstract].

As for syntaxin 1, the activity of syntaxin 3 depends on a conformational switch between a closed state, in which the Habc domain folds back onto the SNARE motif, and an open state that can assemble into SNARE complexes. Single-molecule FRET showed that syntaxin 3B is mainly in the self-inhibited closed conformation and forms ternary SNARE complexes inefficiently [gething-2022-stx3b-conformation-abstract]. The Sec1/Munc18 proteins hold syntaxin 3 in this state while preparing it for fusion. Munc18b (Munc18-2/STXBP2) binds both the N-peptide and the closed Habc–linker–H3 conformation of syntaxin 3, as well as VAMP8 and the assembled Stx3/SNAP-23/VAMP8 complex, and overexpressing it increases constitutive exocytosis [peng-2010-munc18b-abstract]. In intestinal epithelia, Munc18-2 and syntaxin 3 colocalize at the apical membrane and co-immunoprecipitate. The complex responds to protein kinase C activation, and excess Munc18-2 displaces SNAP-23 and cellubrevin from syntaxin 3 [riento-1998-munc18-2-syntaxin3-abstract; riento-2000-munc18-2-apical-abstract]. Syntaxin 3 recruits Munc18b to the plasma membrane, rather than the reverse, and its apical targeting does not need Munc18b binding [sharma-2006-apical-targeting-abstract]. In retinal neurons, syntaxin 3B binds Munc18-1 with an affinity similar to syntaxin 1A [curtis-2008-syntaxin3b-ribbon-abstract]. A congenital nystagmus mutation in STXBP1 (p.His16Arg) has been linked to altered syntaxin 3B interaction [dey-2024-stx3b-review-fulltext].

Phosphorylation adds a further layer of regulation. CaMKII phosphorylates syntaxin 3B at threonine 14, and the phosphomimetic T14E mutant binds SNAP-25 more strongly [liu-2014-stx3b-camkii-abstract]. T14E also shifts syntaxin 3B toward the open conformation and partly relieves Munc18-1 inhibition of SNARE assembly, so phosphorylation acts as a conformational switch [gething-2022-stx3b-conformation-abstract]. In the retina, T14 phosphorylation is driven by light and calcium [dey-2024-stx3b-review-fulltext]. In RBL-2H3 mast cells, by contrast, constitutive phosphorylation at the same residue inhibits exocytosis by impairing the binding of syntaxin 3 to Munc18-2, which suggests the effect depends on cell type [tadokoro-2016-thr14-mast-cell-abstract]. Threonine 14 is conserved in the donkey protein.

## Apical Exocytosis and Epithelial Polarity

In polarized epithelia, syntaxin 3 sits at the apical plasma membrane and mediates fusion of apically directed carriers [sharma-2006-apical-targeting-abstract]. Its apical targeting signal is necessary and sufficient. It is centered on the FMDE motif, which lies exposed on the surface of the Habc three-helix bundle. When MDCK cells express syntaxin 3 that has been sent to the wrong membrane, apical proteins are missorted to the basolateral membrane, tight junctions form abnormally, and the cells fail to build an organized polarized epithelium [sharma-2006-apical-targeting-abstract]. Even before polarity is established, syntaxins 3 and 4 occupy mutually exclusive submicron clusters on the plasma membrane. Syntaxin 3 clusters depend on microtubules and cholesterol, and they move to the leading edge of migrating cells [low-2006-syntaxin-clusters-abstract]. Syntaxin 3 that reaches the basolateral membrane is removed by monoubiquitination in a conserved polybasic juxtamembrane region, followed by endocytosis and sorting into intraluminal vesicles and exosomes. This process helps maintain apical polarity and recruits specific cargo, such as GPRC5B, to exosomes [giovannone-2017-monoubiquitination-abstract]. The donkey sequence keeps this polybasic stretch (…SEARRKL…).

The best-defined pathway that uses syntaxin 3 is cargo-selective apical exocytosis in enterocytes. In genome-edited human intestinal cells, apical delivery of the Na+/H+ exchanger NHE3, the CFTR chloride channel and the fructose transporter GLUT5 requires a sequence of interactions: Rab11 and Rab8, the motor Myosin Vb, the Rab27 effector Slp4a, Munc18-2 and VAMP7, all converging on syntaxin 3. Brush-border hydrolases such as DPPIV and sucrase-isomaltase reach the apical membrane independently of this route [vogel-2015-cargo-selective-exocytosis-abstract]. Conditional deletion of Rab11a in mouse intestine shortens microvilli and moves syntaxin 3 away from the apical membrane, which places the protein downstream of the apical recycling endosome [knowles-2015-rab11a-stx3-abstract]. Two physiological examples show the pathway at work. Enterotoxin- and cyclic nucleotide-stimulated insertion of CFTR into the apical enterocyte membrane needs syntaxin 3, which binds CFTR [collaco-2010-cftr-abstract]. In gastric parietal cells, syntaxin 3 sits on H+,K+-ATPase tubulovesicles, and recombinant syntaxin 3 blocks cAMP-stimulated acid secretion, consistent with a role in fusing tubulovesicles with the apical canalicular membrane [ammar-2002-acid-secretion-abstract].

Human genetics confirms that this apical pathway does not work without syntaxin 3. Homozygous truncating *STX3* mutations cause variant microvillus inclusion disease (MVID): a congenital, intractable diarrhea in which enterocytes lose microvilli, form microvillus inclusions and accumulate subapical vesicles. Patient-derived organoids reproduce the phenotype [wiegerinck-2014-mvid-abstract]. Because *MYO5B*, *STXBP2* (Munc18-2) and *STX3* all cause overlapping MVID-like disorders, the three gene products are thought to act in one apical trafficking pathway [dhekne-2018-mutation-update-abstract]. Syntaxin 3 also serves the analogous axonal compartment of neurons. In hippocampal neurons it localizes to the axonal plasma membrane and is needed to target axonal cargoes such as NgCAM and neurexin [soohoo-2016-axonal-trafficking-abstract]. It also supports neurite outgrowth, and that activity is directly stimulated by arachidonic acid and by omega-3 fatty acids [darios-2006-omega3-syntaxin3-abstract].

## The Retina: Syntaxin 3B at Ribbon Synapses and Outer-Segment Trafficking

Retinal ribbon synapses lack syntaxin 1. Syntaxin 3 instead forms SNARE complexes with SNAP-25, synaptobrevin and complexin in photoreceptors and bipolar cells [morgans-1996-snare-ribbon-synapse-abstract]. Mouse retina expresses only the 3B splice form, whereas kidney expresses only 3A. Syntaxin 3B binds SNAP-25 with lower affinity than syntaxin 1A but still supports SNARE-mediated fusion [curtis-2008-syntaxin3b-ribbon-abstract]. Syntaxin 3B is concentrated on the presynaptic plasma membrane of ribbon terminals, partly close to the ribbon itself [liu-2014-stx3b-camkii-abstract]. In goldfish bipolar cells, a syntaxin 3B-derived inhibitory peptide blocks synaptic vesicle exocytosis measured by membrane capacitance [curtis-2010-syntaxin3b-exocytosis-abstract]. In salamander rods, the same approach selectively reduced ribbon-dependent multivesicular release, which suggests that syntaxin 3B takes part in homotypic vesicle–vesicle fusion at ribbons [hays-2020-multivesicular-rods-abstract]. Light- and calcium-driven CaMKII phosphorylation at T14 has been proposed to tune syntaxin 3B activity to the graded, sustained release that is characteristic of these synapses [liu-2014-stx3b-camkii-abstract; dey-2024-stx3b-review-fulltext]. Complexins 3 and 4 act as clamps on syntaxin 3B-containing complexes [dey-2024-stx3b-review-fulltext].

Syntaxin 3 has a second retinal role in the photoreceptor inner segment. In amphibian rods, it is enriched in the inner-segment plasma membrane at the base of the connecting cilium. There it pairs with SNAP-25 and acts with the exocyst, a Rab8 effector, to fuse rhodopsin transport carriers. Docosahexaenoic acid increases this pairing and the delivery of membrane to the outer segment [mazelova-2009-syntaxin3-rhodopsin-abstract]. Deleting *Stx3* specifically in mouse photoreceptors causes rapid, early-onset degeneration. Outer-segment proteins (rhodopsin, peripherin-2 and its partner ROM1) are mislocalized to the inner segment, cell body and synapse, and the C-terminus of peripherin-2 binds syntaxin 3 directly [kakakhel-2020-stx3-photoreceptor-abstract]. Cones use syntaxin 3 differently. Cone-specific knockout leaves cone opsins in place but causes early cone dysfunction, abnormalities of the connecting cilium, and depletion of STXBP1 and cone arrestin 4. Syntaxin 3, STXBP1 and arrestin 4 form a complex whose composition changes with light [tebbe-2026-stx3b-stxbp1-arrestin-abstract]. Photoreceptors survive with a single functional copy of the gene even in old age [perez-hurtado-2023-haplosufficient-abstract]. In humans, biallelic loss-of-function variants that affect exons shared by STX3A and STX3B cause MVID together with early-onset severe retinal dystrophy, and a rod-specific knockout mouse loses rods and then cones [janecke-2021-stx3-retinal-dystrophy-abstract].

## Regulated Secretion in Immune, Endocrine and Endothelial Cells

Outside epithelia and retina, syntaxin 3 mediates regulated fusion of secretory granules. In mast cells, silencing syntaxin 3 blocks granule fusion, while silencing its partner Munc18-2 impairs granule translocation. Both proteins are found on the granule surface and gather at fusion sites after stimulation [brochetta-2014-mast-cell-abstract]. Conditional knockout mice confirmed that syntaxin 3, not syntaxin 4, is crucial for regulated mast-cell exocytosis. It is particularly needed for multigranular compound exocytosis, while constitutive cytokine secretion is unaffected [sanchez-2019-compound-exocytosis-abstract]. In pancreatic beta cells, syntaxin 3 is abundant on insulin granules. It is required to recruit and fuse "newcomer" granules during both phases of glucose-stimulated insulin secretion, and its overexpression increases granule–granule fusion [zhu-2013-insulin-granule-abstract]. In endothelial cells, syntaxin 3 sits on Weibel–Palade bodies and binds VAMP8. Endothelial cells derived from an *STX3*-null MVID patient form normal Weibel–Palade bodies but secrete less von Willebrand factor, both basally and after stimulation [schillemans-2018-wpb-vwf-abstract]. Across these cell types the common thread is fusion of a specialized secretory organelle with the plasma membrane, often including compound or granule–granule fusion. Syntaxin 3 can therefore localize to the vesicle or granule membrane as well as the plasma membrane.

## Non-canonical Regulation and Functions

Several findings extend syntaxin 3 beyond its role as a fusion receptor. The Habc domain of syntaxin 3 is structurally related to the ubiquitin-binding GAT domain. It binds monomeric ubiquitin weakly and K63-linked (but not K48-linked) polyubiquitin chains efficiently, which may couple membrane fusion to ubiquitin signaling [giovannone-2020-habc-ubiquitin-abstract]. Polyunsaturated fatty acids act directly on syntaxin 3. Arachidonic acid, alpha-linolenic acid and DHA activate it to promote SNARE complex formation and membrane expansion [darios-2006-omega3-syntaxin3-abstract], and DHA increases syntaxin 3–SNAP-25 pairing in photoreceptors [mazelova-2009-syntaxin3-rhodopsin-abstract]. Finally, the soluble splice isoform Stx3S, which lacks the transmembrane anchor, binds the import receptor RanBP5/IPO5, enters the nucleus and interacts with the transcription factors ETV4 and ATF2 to regulate gene expression and cell proliferation [giovannone-2018-soluble-stx3-abstract]. The donkey and horse genome annotations include anchor-less STX3 models, but whether any of them is a functional, nuclear Stx3S equivalent has not been tested. In the brain, splicing between 3A and 3B is itself activity-regulated: long-term potentiation raises 3A and lowers 3B mRNA in dentate granule cells [rodger-1998-ltp-splicing-abstract].

## Synthesis for Functional Annotation of Donkey STX3

Taking the evidence together, the donkey STX3 product is best described as a tail-anchored Qa-SNARE whose molecular function is SNARE receptor activity, binding SNAP-23/SNAP-25, VAMP2/7/8 and Munc18-1/Munc18-2 [curtis-2008-syntaxin3b-ribbon-abstract; peng-2010-munc18b-abstract; vogel-2015-cargo-selective-exocytosis-abstract]. It acts in vesicle docking and fusion with the plasma membrane. Its main localization is the apical plasma membrane of polarized epithelia, where it is needed for apical exocytosis and for establishing epithelial polarity [sharma-2006-apical-targeting-abstract; wiegerinck-2014-mvid-abstract]. In the retina, it localizes to the presynaptic membrane of ribbon synapses, where it supports synaptic vesicle exocytosis [curtis-2010-syntaxin3b-exocytosis-abstract; liu-2014-stx3b-camkii-abstract], and to the inner-segment membrane near the connecting cilium, where it supports ciliary delivery of outer-segment proteins [mazelova-2009-syntaxin3-rhodopsin-abstract; kakakhel-2020-stx3-photoreceptor-abstract]. Secondary localizations are secretory granule membranes in mast cells, beta cells and endothelial cells [brochetta-2014-mast-cell-abstract; zhu-2013-insulin-granule-abstract; schillemans-2018-wpb-vwf-abstract]. The pathways involved are the Rab11/Rab8–Myo5B–Slp4a–Munc18-2–VAMP7–STX3 apical exocytosis module [vogel-2015-cargo-selective-exocytosis-abstract], CaMKII-regulated ribbon-synapse neurotransmitter release [liu-2014-stx3b-camkii-abstract], and Rab8/exocyst-dependent rhodopsin carrier fusion [mazelova-2009-syntaxin3-rhodopsin-abstract]. The IEA Gene Ontology terms already attached to the UniProt record (SNAP receptor activity, SNARE complex, plasma membrane, vesicle fusion, vesicle docking) are consistent with this literature. A more specific annotation to the apical plasma membrane would also be justified by orthology. The TreeGrafter-derived postsynaptic term ("exocytic insertion of neurotransmitter receptor to postsynaptic membrane") is not supported by any study retrieved here and should be treated with caution.

## Open Questions

The most immediate question for this record is whether the hybrid 3B-SNARE/3A-anchor sequence of A0A9L0J901 represents a real donkey transcript. Canonical 3A and 3B models are also annotated in the donkey, and the hybrid is predicted in the horse as well, so the question is about relative abundance and tissue distribution rather than whether 3A/3B splicing exists in equids. Equine retinal and intestinal RNA-seq, or long-read sequencing, would show whether donkeys express separate 3A and 3B transcripts as mice and humans do [curtis-2008-syntaxin3b-ribbon-fulltext; janecke-2021-stx3-retinal-dystrophy-fulltext], and whether a soluble Stx3S-like isoform is produced [giovannone-2018-soluble-stx3-abstract]. If the hybrid is real, it would be worth testing how a 3B SNARE motif behaves on a 3A anchor in epithelial cells, because the C-terminal half of the SNARE motif sets SNAP-25 binding affinity [curtis-2008-syntaxin3b-ribbon-abstract]. More broadly, it is unresolved why T14 phosphorylation appears to promote SNARE assembly in retinal syntaxin 3B [liu-2014-stx3b-camkii-abstract; gething-2022-stx3b-conformation-abstract] but to inhibit exocytosis in mast cells by weakening Munc18-2 binding [tadokoro-2016-thr14-mast-cell-abstract]. It is also unclear how the cone-specific STX3–STXBP1–arrestin 4 complex contributes to cone survival [tebbe-2026-stx3b-stxbp1-arrestin-abstract], and whether binding of K63-polyubiquitin to the Habc domain regulates fusion in vivo [giovannone-2020-habc-ubiquitin-abstract]. For veterinary biology, no study has looked at *STX3* variants in equids. Given the human MVID and retinal-dystrophy phenotypes [wiegerinck-2014-mvid-abstract; janecke-2021-stx3-retinal-dystrophy-abstract], *STX3* would be a reasonable candidate gene for congenital diarrhea or early-onset retinal degeneration in foals.

## References

Bibliographic details below were generated directly from PubMed records.

* **ammar-2002-acid-secretion**: Ammar DA, Zhou R, Forte JG et al. (2002). Syntaxin 3 is required for cAMP-induced acid secretion: streptolysin O-permeabilized gastric gland model. *American journal of physiology. Gastrointestinal and liver physiology* 282:G23-33. PMID: 11751154; DOI: 10.1152/ajpgi.00277.2002 (https://doi.org/10.1152/ajpgi.00277.2002); https://pubmed.ncbi.nlm.nih.gov/11751154/
* **bennett-1993-syntaxin-family**: Bennett MK, García-Arrarás JE, Elferink LA et al. (1993). The syntaxin family of vesicular transport receptors. *Cell* 74:863-73. PMID: 7690687; DOI: 10.1016/0092-8674(93)90466-4 (https://doi.org/10.1016/0092-8674(93)90466-4); https://pubmed.ncbi.nlm.nih.gov/7690687/
* **brochetta-2014-mast-cell**: Brochetta C, Suzuki R, Vita F et al. (2014). Munc18-2 and syntaxin 3 control distinct essential steps in mast cell degranulation. *Journal of immunology (Baltimore, Md. : 1950)* 192:41-51. PMID: 24323579; PMCID: PMC3905451; DOI: 10.4049/jimmunol.1301277 (https://doi.org/10.4049/jimmunol.1301277); https://pubmed.ncbi.nlm.nih.gov/24323579/
* **collaco-2010-cftr**: Collaco A, Marathe J, Kohnke H et al. (2010). Syntaxin 3 is necessary for cAMP- and cGMP-regulated exocytosis of CFTR: implications for enterotoxigenic diarrhea. *American journal of physiology. Cell physiology* 299:C1450-60. PMID: 20844248; PMCID: PMC3006332; DOI: 10.1152/ajpcell.00029.2010 (https://doi.org/10.1152/ajpcell.00029.2010); https://pubmed.ncbi.nlm.nih.gov/20844248/
* **curtis-2008-syntaxin3b-ribbon**: Curtis LB, Doneske B, Liu X et al. (2008). Syntaxin 3b is a t-SNARE specific for ribbon synapses of the retina. *The Journal of comparative neurology* 510:550-9. PMID: 18683220; PMCID: PMC2893228; DOI: 10.1002/cne.21806 (https://doi.org/10.1002/cne.21806); https://pubmed.ncbi.nlm.nih.gov/18683220/
* **curtis-2010-syntaxin3b-exocytosis**: Curtis L, Datta P, Liu X et al. (2010). Syntaxin 3B is essential for the exocytosis of synaptic vesicles in ribbon synapses of the retina. *Neuroscience* 166:832-41. PMID: 20060037; PMCID: PMC2837114; DOI: 10.1016/j.neuroscience.2009.12.075 (https://doi.org/10.1016/j.neuroscience.2009.12.075); https://pubmed.ncbi.nlm.nih.gov/20060037/
* **darios-2006-omega3-syntaxin3**: Darios F, Davletov B (2006). Omega-3 and omega-6 fatty acids stimulate cell membrane expansion by acting on syntaxin 3. *Nature* 440:813-7. PMID: 16598260; DOI: 10.1038/nature04598 (https://doi.org/10.1038/nature04598); https://pubmed.ncbi.nlm.nih.gov/16598260/
* **dey-2024-stx3b-review**: Dey H, Perez-Hurtado M, Heidelberger R (2024). Syntaxin 3B: A SNARE Protein Required for Vision. *International journal of molecular sciences* 25:None. PMID: 39408994; PMCID: PMC11476516; DOI: 10.3390/ijms251910665 (https://doi.org/10.3390/ijms251910665); https://pubmed.ncbi.nlm.nih.gov/39408994/
* **dhekne-2018-mutation-update**: Dhekne HS, Pylypenko O, Overeem AW et al. (2018). MYO5B, STX3, and STXBP2 mutations reveal a common disease mechanism that unifies a subset of congenital diarrheal disorders: A mutation update. *Human mutation* 39:333-344. PMID: 29266534; PMCID: PMC5838515; DOI: 10.1002/humu.23386 (https://doi.org/10.1002/humu.23386); https://pubmed.ncbi.nlm.nih.gov/29266534/
* **gething-2022-stx3b-conformation**: Gething C, Ferrar J, Misra B et al. (2022). Conformational change of Syntaxin-3b in regulating SNARE complex assembly in the ribbon synapses. *Scientific reports* 12:9261. PMID: 35661757; PMCID: PMC9166750; DOI: 10.1038/s41598-022-09654-3 (https://doi.org/10.1038/s41598-022-09654-3); https://pubmed.ncbi.nlm.nih.gov/35661757/
* **giovannone-2017-monoubiquitination**: Giovannone AJ, Reales E, Bhattaram P et al. (2017). Monoubiquitination of syntaxin 3 leads to retrieval from the basolateral plasma membrane and facilitates cargo recruitment to exosomes. *Molecular biology of the cell* 28:2843-2853. PMID: 28814500; PMCID: PMC5638587; DOI: 10.1091/mbc.E17-07-0461 (https://doi.org/10.1091/mbc.E17-07-0461); https://pubmed.ncbi.nlm.nih.gov/28814500/
* **giovannone-2018-soluble-stx3**: Giovannone AJ, Winterstein C, Bhattaram P et al. (2018). Soluble syntaxin 3 functions as a transcriptional regulator. *The Journal of biological chemistry* 293:5478-5491. PMID: 29475951; PMCID: PMC5900775; DOI: 10.1074/jbc.RA117.000874 (https://doi.org/10.1074/jbc.RA117.000874); https://pubmed.ncbi.nlm.nih.gov/29475951/
* **giovannone-2020-habc-ubiquitin**: Giovannone AJ, Reales E, Bhattaram P et al. (2020). The Habc domain of syntaxin 3 is a ubiquitin binding domain. *Scientific reports* 10:21350. PMID: 33288783; PMCID: PMC7721868; DOI: 10.1038/s41598-020-78412-0 (https://doi.org/10.1038/s41598-020-78412-0); https://pubmed.ncbi.nlm.nih.gov/33288783/
* **hays-2020-multivesicular-rods**: Hays CL, Grassmeyer JJ, Wen X et al. (2020). Simultaneous Release of Multiple Vesicles from Rods Involves Synaptic Ribbons and Syntaxin 3B. *Biophysical journal* 118:967-979. PMID: 31653448; PMCID: PMC7036726; DOI: 10.1016/j.bpj.2019.10.006 (https://doi.org/10.1016/j.bpj.2019.10.006); https://pubmed.ncbi.nlm.nih.gov/31653448/
* **ibaraki-1995-four-forms-syntaxin3**: Ibaraki K, Horikawa HP, Morita T et al. (1995). Identification of four different forms of syntaxin 3. *Biochemical and biophysical research communications* 211:997-1005. PMID: 7598732; DOI: 10.1006/bbrc.1995.1910 (https://doi.org/10.1006/bbrc.1995.1910); https://pubmed.ncbi.nlm.nih.gov/7598732/
* **janecke-2021-stx3-retinal-dystrophy**: Janecke AR, Liu X, Adam R et al. (2021). Pathogenic STX3 variants affecting the retinal and intestinal transcripts cause an early-onset severe retinal dystrophy in microvillus inclusion disease subjects. *Human genetics* 140:1143-1156. PMID: 33974130; PMCID: PMC8263458; DOI: 10.1007/s00439-021-02284-1 (https://doi.org/10.1007/s00439-021-02284-1); https://pubmed.ncbi.nlm.nih.gov/33974130/
* **kakakhel-2020-stx3-photoreceptor**: Kakakhel M, Tebbe L, Makia MS et al. (2020). Syntaxin 3 is essential for photoreceptor outer segment protein trafficking and survival. *Proceedings of the National Academy of Sciences of the United States of America* 117:20615-20624. PMID: 32778589; PMCID: PMC7456102; DOI: 10.1073/pnas.2010751117 (https://doi.org/10.1073/pnas.2010751117); https://pubmed.ncbi.nlm.nih.gov/32778589/
* **knowles-2015-rab11a-stx3**: Knowles BC, Weis VG, Yu S et al. (2015). Rab11a regulates syntaxin 3 localization and microvillus assembly in enterocytes. *Journal of cell science* 128:1617-26. PMID: 25673875; PMCID: PMC4518445; DOI: 10.1242/jcs.163303 (https://doi.org/10.1242/jcs.163303); https://pubmed.ncbi.nlm.nih.gov/25673875/
* **liu-2014-stx3b-camkii**: Liu X, Heidelberger R, Janz R (2014). Phosphorylation of syntaxin 3B by CaMKII regulates the formation of t-SNARE complexes. *Molecular and cellular neurosciences* 60:53-62. PMID: 24680688; PMCID: PMC4066811; DOI: 10.1016/j.mcn.2014.03.002 (https://doi.org/10.1016/j.mcn.2014.03.002); https://pubmed.ncbi.nlm.nih.gov/24680688/
* **low-2006-syntaxin-clusters**: Low SH, Vasanji A, Nanduri J et al. (2006). Syntaxins 3 and 4 are concentrated in separate clusters on the plasma membrane before the establishment of cell polarity. *Molecular biology of the cell* 17:977-89. PMID: 16339081; PMCID: PMC1356605; DOI: 10.1091/mbc.e05-05-0462 (https://doi.org/10.1091/mbc.e05-05-0462); https://pubmed.ncbi.nlm.nih.gov/16339081/
* **mazelova-2009-syntaxin3-rhodopsin**: Mazelova J, Ransom N, Astuto-Gribble L et al. (2009). Syntaxin 3 and SNAP-25 pairing, regulated by omega-3 docosahexaenoic acid, controls the delivery of rhodopsin for the biogenesis of cilia-derived sensory organelles, the rod outer segments. *Journal of cell science* 122:2003-13. PMID: 19454479; PMCID: PMC2723154; DOI: 10.1242/jcs.039982 (https://doi.org/10.1242/jcs.039982); https://pubmed.ncbi.nlm.nih.gov/19454479/
* **morgans-1996-snare-ribbon-synapse**: Morgans CW, Brandstätter JH, Kellerman J et al. (1996). A SNARE complex containing syntaxin 3 is present in ribbon synapses of the retina. *The Journal of neuroscience : the official journal of the Society for Neuroscience* 16:6713-21. PMID: 8824312; PMCID: PMC6579260; DOI: 10.1523/JNEUROSCI.16-21-06713.1996 (https://doi.org/10.1523/JNEUROSCI.16-21-06713.1996); https://pubmed.ncbi.nlm.nih.gov/8824312/
* **peng-2010-munc18b**: Peng RW, Guetg C, Abellan E et al. (2010). Munc18b regulates core SNARE complex assembly and constitutive exocytosis by interacting with the N-peptide and the closed-conformation C-terminus of syntaxin 3. *The Biochemical journal* 431:353-61. PMID: 20695848; DOI: 10.1042/BJ20100145 (https://doi.org/10.1042/BJ20100145); https://pubmed.ncbi.nlm.nih.gov/20695848/
* **perez-hurtado-2023-haplosufficient**: Perez-Hurtado M, Dao C, Saenz AE et al. (2023). Syntaxin 3 is haplosufficient for long-term photoreceptor survival in the mouse retina. *Frontiers in ophthalmology* 3:None. PMID: 37609371; PMCID: PMC10443939; DOI: 10.3389/fopht.2023.1208805 (https://doi.org/10.3389/fopht.2023.1208805); https://pubmed.ncbi.nlm.nih.gov/37609371/
* **riento-1998-munc18-2-syntaxin3**: Riento K, Galli T, Jansson S et al. (1998). Interaction of Munc-18-2 with syntaxin 3 controls the association of apical SNAREs in epithelial cells. *Journal of cell science* 111 ( Pt 17):2681-8. PMID: 9701566; DOI: 10.1242/jcs.111.17.2681 (https://doi.org/10.1242/jcs.111.17.2681); https://pubmed.ncbi.nlm.nih.gov/9701566/
* **riento-2000-munc18-2-apical**: Riento K, Kauppi M, Keranen S et al. (2000). Munc18-2, a functional partner of syntaxin 3, controls apical membrane trafficking in epithelial cells. *The Journal of biological chemistry* 275:13476-83. PMID: 10788461; DOI: 10.1074/jbc.275.18.13476 (https://doi.org/10.1074/jbc.275.18.13476); https://pubmed.ncbi.nlm.nih.gov/10788461/
* **rodger-1998-ltp-splicing**: Rodger J, Davis S, Laroche S et al. (1998). Induction of long-term potentiation in vivo regulates alternate splicing to alter syntaxin 3 isoform expression in rat dentate gyrus. *Journal of neurochemistry* 71:666-75. PMID: 9681457; DOI: 10.1046/j.1471-4159.1998.71020666.x (https://doi.org/10.1046/j.1471-4159.1998.71020666.x); https://pubmed.ncbi.nlm.nih.gov/9681457/
* **sanchez-2019-compound-exocytosis**: Sanchez E, Gonzalez EA, Moreno DS et al. (2019). Syntaxin 3, but not syntaxin 4, is required for mast cell-regulated exocytosis, where it plays a primary role mediating compound exocytosis. *The Journal of biological chemistry* 294:3012-3023. PMID: 30563839; PMCID: PMC6398129; DOI: 10.1074/jbc.RA118.005532 (https://doi.org/10.1074/jbc.RA118.005532); https://pubmed.ncbi.nlm.nih.gov/30563839/
* **schillemans-2018-wpb-vwf**: Schillemans M, Karampini E, van den Eshof BL et al. (2018). Weibel-Palade Body Localized Syntaxin-3 Modulates Von Willebrand Factor Secretion From Endothelial Cells. *Arteriosclerosis, thrombosis, and vascular biology* 38:1549-1561. PMID: 29880488; PMCID: PMC6039413; DOI: 10.1161/ATVBAHA.117.310701 (https://doi.org/10.1161/ATVBAHA.117.310701); https://pubmed.ncbi.nlm.nih.gov/29880488/
* **sharma-2006-apical-targeting**: Sharma N, Low SH, Misra S et al. (2006). Apical targeting of syntaxin 3 is essential for epithelial cell polarity. *The Journal of cell biology* 173:937-48. PMID: 16785322; PMCID: PMC2063918; DOI: 10.1083/jcb.200603132 (https://doi.org/10.1083/jcb.200603132); https://pubmed.ncbi.nlm.nih.gov/16785322/
* **soohoo-2016-axonal-trafficking**: Soo Hoo L, Banna CD, Radeke CM et al. (2016). The SNARE Protein Syntaxin 3 Confers Specificity for Polarized Axonal Trafficking in Neurons. *PloS one* 11:e0163671. PMID: 27662481; PMCID: PMC5035089; DOI: 10.1371/journal.pone.0163671 (https://doi.org/10.1371/journal.pone.0163671); https://pubmed.ncbi.nlm.nih.gov/27662481/
* **tadokoro-2016-thr14-mast-cell**: Tadokoro S, Shibata T, Inoh Y et al. (2016). Phosphorylation of syntaxin-3 at Thr 14 negatively regulates exocytosis in RBL-2H3 mast cells. *Cell biology international* 40:589-96. PMID: 26936588; DOI: 10.1002/cbin.10600 (https://doi.org/10.1002/cbin.10600); https://pubmed.ncbi.nlm.nih.gov/26936588/
* **tebbe-2026-stx3b-stxbp1-arrestin**: Tebbe L, Ikelle L, Makia MS et al. (2026). Syntaxin 3B Mediates Light-Dependent Interactions with STXBP1 and Arrestin 4: Distinct Roles in Rods and Cones. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)* 13:e13319. PMID: 41220299; PMCID: PMC12866690; DOI: 10.1002/advs.202513319 (https://doi.org/10.1002/advs.202513319); https://pubmed.ncbi.nlm.nih.gov/41220299/
* **vogel-2015-cargo-selective-exocytosis**: Vogel GF, Klee KM, Janecke AR et al. (2015). Cargo-selective apical exocytosis in epithelial cells is conducted by Myo5B, Slp4a, Vamp7, and Syntaxin 3. *The Journal of cell biology* 211:587-604. PMID: 26553929; PMCID: PMC4639860; DOI: 10.1083/jcb.201506112 (https://doi.org/10.1083/jcb.201506112); https://pubmed.ncbi.nlm.nih.gov/26553929/
* **wang-2020-donkey-genome**: Wang C, Li H, Guo Y et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications* 11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7 (https://doi.org/10.1038/s41467-020-19813-7); https://pubmed.ncbi.nlm.nih.gov/33293529/
* **wiegerinck-2014-mvid**: Wiegerinck CL, Janecke AR, Schneeberger K et al. (2014). Loss of syntaxin 3 causes variant microvillus inclusion disease. *Gastroenterology* 147:65-68.e10. PMID: 24726755; DOI: 10.1053/j.gastro.2014.04.002 (https://doi.org/10.1053/j.gastro.2014.04.002); https://pubmed.ncbi.nlm.nih.gov/24726755/
* **zhu-2013-insulin-granule**: Zhu D, Koo E, Kwan E et al. (2013). Syntaxin-3 regulates newcomer insulin granule exocytosis and compound fusion in pancreatic beta cells. *Diabetologia* 56:359-69. PMID: 23132338; DOI: 10.1007/s00125-012-2757-0 (https://doi.org/10.1007/s00125-012-2757-0); https://pubmed.ncbi.nlm.nih.gov/23132338/

UniProt records used for sequence comparison: A0A9L0J901 (donkey STX3, target), A0A8C4LHZ8, A0A8C4PQW9, A0A9L0JMU1, A0A9L0JRA1, A0A9L0JKT1 (other donkey STX3 models), A0A3Q2H352, F7BC79, F6ZUC9 (horse STX3 models), Q13277 (human STX3), Q64704 (mouse Stx3), Q08849 (rat Stx3); Ensembl gene ENSEASG00005007989; retrieved from https://rest.uniprot.org/uniprotkb/.


## Citations

1. ammar-2002-acid-secretion-abstract.md
2. ammar-2002-acid-secretion-summary.md
3. bennett-1993-syntaxin-family-abstract.md
4. bennett-1993-syntaxin-family-summary.md
5. brochetta-2014-mast-cell-abstract.md
6. brochetta-2014-mast-cell-fulltext.txt
7. brochetta-2014-mast-cell-summary.md
8. collaco-2010-cftr-abstract.md
9. collaco-2010-cftr-summary.md
10. curtis-2008-syntaxin3b-ribbon-abstract.md
11. curtis-2008-syntaxin3b-ribbon-fulltext.txt
12. curtis-2008-syntaxin3b-ribbon-summary.md
13. curtis-2010-syntaxin3b-exocytosis-abstract.md
14. curtis-2010-syntaxin3b-exocytosis-fulltext.txt
15. curtis-2010-syntaxin3b-exocytosis-summary.md
16. darios-2006-omega3-syntaxin3-abstract.md
17. darios-2006-omega3-syntaxin3-summary.md
18. dey-2024-stx3b-review-abstract.md
19. dey-2024-stx3b-review-fulltext.txt
20. dey-2024-stx3b-review-summary.md
21. dhekne-2018-mutation-update-abstract.md
22. dhekne-2018-mutation-update-fulltext.txt
23. dhekne-2018-mutation-update-summary.md
24. gething-2022-stx3b-conformation-abstract.md
25. gething-2022-stx3b-conformation-fulltext.txt
26. gething-2022-stx3b-conformation-summary.md
27. giovannone-2017-monoubiquitination-abstract.md
28. giovannone-2017-monoubiquitination-fulltext.txt
29. giovannone-2017-monoubiquitination-summary.md
30. giovannone-2018-soluble-stx3-abstract.md
31. giovannone-2018-soluble-stx3-summary.md
32. giovannone-2020-habc-ubiquitin-abstract.md
33. giovannone-2020-habc-ubiquitin-fulltext.txt
34. giovannone-2020-habc-ubiquitin-summary.md
35. hays-2020-multivesicular-rods-abstract.md
36. hays-2020-multivesicular-rods-summary.md
37. ibaraki-1995-four-forms-syntaxin3-abstract.md
38. ibaraki-1995-four-forms-syntaxin3-summary.md
39. janecke-2021-stx3-retinal-dystrophy-abstract.md
40. janecke-2021-stx3-retinal-dystrophy-fulltext.txt
41. janecke-2021-stx3-retinal-dystrophy-summary.md
42. kakakhel-2020-stx3-photoreceptor-abstract.md
43. kakakhel-2020-stx3-photoreceptor-summary.md
44. knowles-2015-rab11a-stx3-abstract.md
45. knowles-2015-rab11a-stx3-summary.md
46. liu-2014-stx3b-camkii-abstract.md
47. liu-2014-stx3b-camkii-fulltext.txt
48. liu-2014-stx3b-camkii-summary.md
49. low-2006-syntaxin-clusters-abstract.md
50. low-2006-syntaxin-clusters-summary.md
51. mazelova-2009-syntaxin3-rhodopsin-abstract.md
52. mazelova-2009-syntaxin3-rhodopsin-summary.md
53. morgans-1996-snare-ribbon-synapse-abstract.md
54. morgans-1996-snare-ribbon-synapse-summary.md
55. peng-2010-munc18b-abstract.md
56. peng-2010-munc18b-summary.md
57. perez-hurtado-2023-haplosufficient-abstract.md
58. perez-hurtado-2023-haplosufficient-fulltext.txt
59. perez-hurtado-2023-haplosufficient-summary.md
60. riento-1998-munc18-2-syntaxin3-abstract.md
61. riento-1998-munc18-2-syntaxin3-summary.md
62. riento-2000-munc18-2-apical-abstract.md
63. riento-2000-munc18-2-apical-summary.md
64. rodger-1998-ltp-splicing-abstract.md
65. rodger-1998-ltp-splicing-summary.md
66. sanchez-2019-compound-exocytosis-abstract.md
67. sanchez-2019-compound-exocytosis-summary.md
68. schillemans-2018-wpb-vwf-abstract.md
69. schillemans-2018-wpb-vwf-fulltext.txt
70. schillemans-2018-wpb-vwf-summary.md
71. sharma-2006-apical-targeting-abstract.md
72. sharma-2006-apical-targeting-fulltext.txt
73. sharma-2006-apical-targeting-summary.md
74. soohoo-2016-axonal-trafficking-abstract.md
75. soohoo-2016-axonal-trafficking-fulltext.txt
76. soohoo-2016-axonal-trafficking-summary.md
77. tadokoro-2016-thr14-mast-cell-abstract.md
78. tadokoro-2016-thr14-mast-cell-summary.md
79. tebbe-2026-stx3b-stxbp1-arrestin-abstract.md
80. tebbe-2026-stx3b-stxbp1-arrestin-fulltext.txt
81. tebbe-2026-stx3b-stxbp1-arrestin-summary.md
82. vogel-2015-cargo-selective-exocytosis-abstract.md
83. vogel-2015-cargo-selective-exocytosis-fulltext.txt
84. vogel-2015-cargo-selective-exocytosis-summary.md
85. wang-2020-donkey-genome-abstract.md
86. wang-2020-donkey-genome-fulltext.txt
87. wang-2020-donkey-genome-summary.md
88. wiegerinck-2014-mvid-abstract.md
89. wiegerinck-2014-mvid-summary.md
90. zhu-2013-insulin-granule-abstract.md
91. zhu-2013-insulin-granule-summary.md