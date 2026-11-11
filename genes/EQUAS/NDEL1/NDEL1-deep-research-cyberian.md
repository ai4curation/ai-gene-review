---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:17:40.599322'
end_time: '2026-10-26T00:29:03.535908'
duration_seconds: 682.94
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: NDEL1
  gene_symbol: NDEL1
  uniprot_accession: A0A9L0IJ72
  protein_description: 'RecName: Full=Nuclear distribution protein nudE-like 1 {ECO:0000256|ARBA:ARBA00017587};'
  gene_info: Name=NDEL1 {ECO:0000313|Ensembl:ENSEASP00005040207.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the nudE family.
  protein_domains: NUDE. (IPR033494); NUDE_dom. (IPR006964); NUDE_C (PF04880)
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
citation_count: 91
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0IJ72
- **Protein Description:** RecName: Full=Nuclear distribution protein nudE-like 1 {ECO:0000256|ARBA:ARBA00017587};
- **Gene Information:** Name=NDEL1 {ECO:0000313|Ensembl:ENSEASP00005040207.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the nudE family.
- **Key Domains:** NUDE. (IPR033494); NUDE_dom. (IPR006964); NUDE_C (PF04880)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "NDEL1" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'NDEL1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **NDEL1** (gene ID: NDEL1, UniProt: A0A9L0IJ72) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# NDEL1 (Nuclear distribution protein nudE-like 1) in the donkey, *Equus asinus* (UniProt A0A9L0IJ72)

## 1. Introduction and summary

NDEL1 (also called NudEL or NUDEL) is a coiled-coil adaptor of the nudE family that regulates cytoplasmic dynein-1, the main minus-end-directed microtubule motor of animal cells. The donkey protein A0A9L0IJ72 is an unreviewed TrEMBL entry from the donkey genome project. It is annotated by homology only (protein existence level 3). Its family assignment, its domains (NUDE, IPR033494; NUDE_dom, IPR006964; Pfam NUDE_C, PF04880) and its predicted locations (kinetochore, centrosome and spindle) all come from automatic rules [uniprot-2026-a0a9l0ij72-entry]. No experimental study of donkey NDEL1 exists. However, the gene symbol is not ambiguous. Residues 1–338 of the donkey protein are 99% identical to human NDEL1 (Q9GZM8), and every functionally mapped residue is conserved (Section 2; notes/sequence_comparison.md). This report therefore infers the function of donkey NDEL1 from the experimental literature on the human, mouse, rat, *Xenopus* and yeast orthologs, and states clearly that this is an inference.

That literature describes NDEL1 primarily as a non-enzymatic, phosphoregulated scaffold. Its N-terminal coiled coil forms a parallel homodimer that binds a LIS1 dimer [derewenda-2007-ndel1-structure-abstract]. It also binds the N-terminus of the dynein intermediate chain [okada-2023-ic-ndel1-dynein-fulltext; garrott-2023-ndel1-dynein-dynactin-fulltext]. Through these contacts it recruits LIS1 to dynein [mckenney-2010-lis1-nude-dynein-force-abstract; zylkiewicz-2011-ndel1-scaffold-fulltext], which helps assemble the activated dynein–dynactin–cargo-adaptor transport complex [okada-2023-ic-ndel1-dynein-fulltext; zhao-2023-nde1-lis1-dynein-fulltext]. Cdk5, CDK1, ERK, Aurora A, DYRK2 and GSK3β phosphorylate the C-terminal half of NDEL1, and palmitoylation also modifies it. These modifications set where NDEL1 goes and which partners it binds [niethammer-2000-nudel-cdk5-abstract; yan-2003-nudel-mitotic-spindle-abstract; mori-2009-apkc-aurora-ndel1-abstract; shmueli-2010-ndel1-palmitoylation-abstract; woo-2019-dyrk2-gsk3b-ndel1-fulltext].

In cells, NDEL1 works at the centrosome (mother centriole), the mitotic spindle and kinetochores, microtubule plus ends, the axon initial segment, and dynein-driven membrane cargoes [guo-2006-nudel-centriole-abstract; vergnolle-2007-cenpf-ndel1-abstract; li-2005-nudel-dynein-mt-ends-abstract; kuijpers-2016-ndel1-axon-initial-segment-abstract; liang-2004-nudel-membrane-traffic-fulltext]. It is needed for microtubule organization, nucleus–centrosome coupling in migrating cortical neurons, chromosome segregation and early embryonic survival [shu-2004-ndel1-cortical-positioning-abstract; sasaki-2005-ndel1-knockout-abstract]. A de novo NDEL1 variant that abolishes LIS1 binding causes human lissencephaly, which confirms that the LIS1 interaction is central to NDEL1 function [tsai-2024-ndel1-lissencephaly-variant-fulltext]. Additional partners (katanin p60, 14-3-3ε, DISC1, neurofilament light chain, vimentin, CENP-F and Rab9) link it to other cytoskeletal and trafficking processes [toyooka-2005-katanin-ndel1-abstract; toyooka-2003-14-3-3epsilon-nudel-abstract; ozeki-2003-disc1-nudel-abstract; nguyen-2004-nudel-neurofilament-abstract; shim-2008-ndel1-vimentin-abstract; zhang-2022-nde1-rab9-abstract].

## 2. Identity of the donkey protein and conservation of functional elements

The donkey entry is a 481-residue protein encoded on chromosome 13 (Ensembl ENSEASG00005019855). It carries automatic GO terms such as microtubule binding, centrosome, kinetochore, spindle, cerebral cortex radially oriented cell migration, and vesicle transport along microtubule [uniprot-2026-a0a9l0ij72-entry]. The reviewed human ortholog is 345 residues long. UniProt describes it as being required for microtubule anchoring at the centrosome and as a positive regulator of dynein, with several mapped binding regions: self-association (56–166), the LIS1-binding segment (114–133), YWHAE/14-3-3ε (189–256), katanin p60 (195–256), DISC1 (241–280), and a 256–291 segment needed for centrosome targeting and for binding dynein, dynactin, γ-tubulin, PCM1 and pericentrin [uniprot-2026-q9gzm8-human-ndel1-entry].

A direct comparison found only three substitutions in the first 338 residues of the donkey protein (S228, M296 and S298 in place of human T, L and G), and every experimentally defined site in this region is retained. These include glutamate 48, which is needed for binding the dynein intermediate chain [garrott-2023-ndel1-dynein-dynactin-fulltext], and arginine 105 in the LIS1-binding coiled coil, whose substitution by proline causes lissencephaly in humans [tsai-2024-ndel1-lissencephaly-variant-fulltext]. The CDK phosphosites S198, T219, S231, S242 and T245 [uniprot-2026-q9gzm8-human-ndel1-entry] are present, as is the Aurora A site S251 [mori-2007-aurora-a-ndel1-centrosome-abstract; mori-2009-apkc-aurora-ndel1-abstract]. So are the DISC1 contacts L266 and E267 and the palmitoylated cysteine C273 [uniprot-2026-q9gzm8-human-ndel1-entry], as well as the DYRK2 and GSK3β sites S336 and S332 [woo-2019-dyrk2-gsk3b-ndel1-fulltext].

After residue 338 the donkey sequence departs from human isoform 1. Instead of the short tail GMLPLSV, it continues with a 143-residue, low-complexity extension that has no recognisable domain. Human NDEL1 already has alternatively spliced isoforms that differ only in their C-terminal ~30 residues [uniprot-2026-q9gzm8-human-ndel1-entry]. UniProt also lists ten donkey and nine horse NDEL1 entries of different lengths, including a 481-residue horse model [uniprot-2026-equus-ndel1-isoforms-search]. The only equid-specific NDEL1 study found is a re-analysis of oocyte RNA-seq data. It identified NDEL1 as one of ten genes whose transcript-isoform usage changes significantly between germinal-vesicle and metaphase-II oocytes in at least five mammals, a group that includes donkey and horse [sananmuang-2024-oocyte-transcript-usage-abstract]. Several NDEL1 transcripts are therefore expressed in equids. The extension is best read as an equid-specific splice or gene-model variant of the flexible C-terminal tail, not as a new functional domain. Whether it is expressed as protein remains an open question (Section 8). The conserved core holds everything needed for dimerization, LIS1 binding, dynein binding and phosphoregulation, so the mechanistic conclusions below should apply to the donkey protein.

## 3. Molecular architecture: a dimeric coiled-coil scaffold

NDEL1 has a bipartite structure. The N-terminal half is a long coiled coil (human residues ~28–190) [uniprot-2026-q9gzm8-human-ndel1-entry]. Crystal structures of this region, with continuous density for residues 10–166, show a stable parallel homodimer. Two supercoiled helices are thought to bind cooperatively to a LIS1 homodimer [derewenda-2007-ndel1-structure-abstract]. The C-terminal half is mostly unstructured but contains a short C-terminal coiled-coil segment. A crystal structure shows this segment forming a five-helix bundle with the giant neuron-specific insertion of ankyrin-B, with two NDEL1 helices per ankyrin, and the same interface anchors NDEL1 to ankyrin-G [ye-2020-ndel1-ankyrin-abstract]. This half also holds the regulatory phosphosites, the palmitoylation site and the regions that target NDEL1 to the centrosome and to kinetochores [guo-2006-nudel-centriole-abstract; zylkiewicz-2011-ndel1-scaffold-fulltext].

Dynein binding is split between the two halves. The N-terminal coiled coil binds the N-terminus of the dynein intermediate chain, and the E48A mutation abolishes this interaction. The C-terminal region adds further dynein affinity (Kd for full-length NDEL1 about 33 nM) and lowers affinity for LIS1 [garrott-2023-ndel1-dynein-dynactin-fulltext]. In *Xenopus* egg extracts, the N-terminal coiled coil alone restored dynein-dependent aster formation after NDEL1 depletion, provided it could bind both dynein and LIS1. The authors concluded that NDEL1 is a "regulated scaffold" whose interactions are tuned by phosphorylation of its C terminus [zylkiewicz-2011-ndel1-scaffold-fulltext].

One older claim needs a caution. NDEL1 was once proposed to be endooligopeptidase A, a thiol peptidase whose activity depended on Cys273 and was competitively inhibited by DISC1 [hayashi-2005-nudel-oligopeptidase-abstract]. The 2017 Bradshaw and Hayashi review still describes this activity [bradshaw-2017-nde1-ndel1-review-abstract]. UniProt, however, now records it under a CAUTION note as something "originally thought" [uniprot-2026-q9gzm8-human-ndel1-entry]. Cys273 has since been shown to be a palmitoylation site that controls dynein binding [shmueli-2010-ndel1-palmitoylation-abstract]. The consensus primary function of NDEL1 is therefore a non-catalytic scaffold or adaptor, not an enzyme.

## 4. Core function: recruiting LIS1 to cytoplasmic dynein and regulating its activation

NDEL1 was found in 2000 as a LIS1-binding protein homologous to the *Aspergillus* nuclear-migration protein NudE. It co-purified with cytoplasmic dynein heavy chain and was phosphorylated by Cdk5/p35 [niethammer-2000-nudel-cdk5-abstract; sasaki-2000-lis1-nudel-dynein-abstract]. The LIS1–NudE/L–dynein module is conserved back to fungi. In budding yeast, the NDEL1 homolog Ndl1 promotes dynein accumulation at microtubule plus ends by recruiting LIS1 (Pac1), and does not work through CLIP-170 [li-2005-nudel-dynein-mt-ends-abstract]. Genetic and RNAi experiments in mice place NDEL1 in the same pathway as LIS1 and dynein. Overexpressing LIS1 partly rescues neuronal positioning defects caused by NDEL1 knockdown, but the reverse rescue does not work, which puts NDEL1 upstream of LIS1 in delivering LIS1 to dynein [shu-2004-ndel1-cortical-positioning-abstract]. Compound Lis1/Ndel1 mutants show migration defects that worsen with gene dosage [sasaki-2005-ndel1-knockout-abstract].

Biophysical work has clarified what NDEL1 does at the molecular level. In single-molecule and optical-trap assays, NudE stably recruited LIS1 to the dynein holoenzyme. LIS1 then bound the motor domain in its pre-powerstroke state and switched dynein into a persistent-force mode that helps several motors move high-load cargo together [mckenney-2010-lis1-nude-dynein-force-abstract]. Later reconstitutions placed this step within the current model of dynein activation, in which autoinhibited "Phi" dynein must be opened (a step LIS1 promotes) to assemble with dynactin and a cargo adaptor [garrott-2023-ndel1-dynein-dynactin-fulltext; cianfrocco-2015-dynein-review-abstract]. Okada et al. showed that the N-terminus of the dynein intermediate chain is a conserved hub for both dynactin p150Glued and NDEL1. In their model, NDEL1 brings LIS1 to dynein, then the NDEL1–LIS1 pair separates so LIS1 can be handed to the motor before the active complex forms [okada-2023-ic-ndel1-dynein-fulltext]. Reconstitution with the paralog NDE1 gave a similar picture: NDE1 recruits LIS1 to autoinhibited dynein and promotes LIS1-driven complex assembly, and dynactin then displaces NDE1 from the intermediate chain before movement begins [zhao-2023-nde1-lis1-dynein-fulltext]. Cryo-EM of full-length human dynein added a structural intermediate. NDE1 speeds the formation of a "PhiL–LIS1" complex, in which a single LIS1 dimer is wedged between the two partly opened motor rings, and NDE1 itself is not part of this complex. This finding explains how a NudE-family protein can promote Phi opening catalytically without staying bound [yang-2026-nde1-lis1-autoinhibited-dynein-abstract].

Garrott et al. complicated this picture with purified NDEL1. In vitro, NDEL1 reduced the formation, landing rate and run length of dynein–dynactin–BicD2 complexes. It also sequestered LIS1 away from its binding site on dynein, and phosphomimetic mutations at the four CDK1 sites increased this inhibition [garrott-2023-ndel1-dynein-dynactin-fulltext]. The authors reconciled these results with cell-based evidence for activation by proposing that NDEL1 holds dynein and LIS1 together in a primed but inhibited state, and that a timed release of NDEL1 in cells permits activation [garrott-2023-ndel1-dynein-dynactin-fulltext]. Two cell-based studies support this release model. In adult sensory axons, NDEL1 lacking its key phosphorylation sites, or dominant-negative Cdk5, shut down dynein-driven transport of acidic organelles. The authors concluded that unphosphorylated NDEL1 inhibits dynein and that Cdk5 phosphorylation relieves the inhibition and lets LIS1 stimulate transport [pandey-2011-cdk5-switch-ndel1-abstract]. At the cell periphery, the protein CCSer2 weakens the dynein–NDEL1 interaction and thereby activates dynein locally, which fits a model in which spatially restricted factors trigger NDEL1 release [zang-2025-ccser2-dynein-abstract]. The dynein side of the interface is also regulated. GSK-3β phosphorylates conserved S87/T88 in the NDEL1-binding region of the intermediate chain and weakens NDEL1 binding. Insulin-sensitizing signals that inactivate GSK-3β stimulate dynein motility [gao-2015-gsk3b-dynein-ndel1-fulltext], which is the experimental basis for the electronically assigned GO term "insulin receptor signaling pathway" on the donkey entry [uniprot-2026-a0a9l0ij72-entry]. Taken together, the consensus is that NDEL1 acts early in dynein activation as a LIS1 delivery and scaffolding factor. It must leave before processive transport, and its net effect (permissive or inhibitory) depends on phosphorylation state and context.

## 5. Subcellular localization

The donkey entry's predicted locations (centrosome/microtubule organizing center, kinetochore and spindle) [uniprot-2026-a0a9l0ij72-entry] match the experimental evidence from other mammals. In interphase COS-7 and HeLa cells, NDEL1 is a mother-centriole protein that turns over rapidly. It reaches the new mother centriole after ninein but before dynactin. Its centrosomal localization depends on a C-terminal region that also binds dynein, dynactin, PCM-1, pericentrin and γ-tubulin [guo-2006-nudel-centriole-abstract]. Depleting NDEL1 lowers centrosomal levels of these proteins and impairs microtubule nucleation and anchoring, which suggests that NDEL1 tethers dynein and dynactin to the mother centriole [guo-2006-nudel-centriole-abstract]. More precisely, NDEL1 sits at the subdistal appendages of the mother centriole [inaba-2016-ndel1-ciliogenesis-fulltext], and it is required to bring TACC3 to the centrosome [mori-2007-aurora-a-ndel1-centrosome-abstract]. In neurons, NDEL1 is enriched at the centrosome in early neuroblasts and later moves into axons and growth cones together with retrograde dynein [sasaki-2000-lis1-nudel-dynein-abstract; niethammer-2000-nudel-cdk5-abstract]. Growth cones are also enriched in NDEL1 phosphorylated at S332/S336 [woo-2019-dyrk2-gsk3b-ndel1-fulltext]. In mature neurons, NDEL1 concentrates at the axon initial segment by binding ankyrin-G [kuijpers-2016-ndel1-axon-initial-segment-abstract; ye-2020-ndel1-ankyrin-abstract], which matches the "axon hillock" GO term on the donkey entry [uniprot-2026-a0a9l0ij72-entry].

During mitosis, NDEL1 moves from centrosomes to the spindle in early M phase, and its phosphorylation speeds its release from the microtubule organizing center [yan-2003-nudel-mitotic-spindle-abstract]. NDEL1 and NDE1 reach kinetochores before dynein, dynactin, ZW10 and LIS1 [stehman-2007-nude-nudel-mitosis-fulltext], and their kinetochore localization depends on CENP-F [vergnolle-2007-cenpf-ndel1-abstract]. NDEL1 is also found at microtubule plus ends (shown in yeast) [li-2005-nudel-dynein-mt-ends-abstract] and on dynein-driven membranes. These include lysosomes, the Golgi, late endosomes positive for Rab9 [liang-2004-nudel-membrane-traffic-fulltext; zhang-2022-nde1-rab9-abstract], and a vimentin–dynein–αCOP complex in growing neurites [shim-2008-ndel1-vimentin-abstract]. NDEL1 is therefore a cytoplasmic and cytoskeletal protein. It has no transmembrane segment and no catalytic site, and its location changes with the cell cycle and with phosphorylation.

## 6. Regulation by phosphorylation, 14-3-3ε and palmitoylation

Post-translational modification of the C-terminal half acts as the main switch on NDEL1 function. Cdk5/p35 phosphorylates NDEL1 in neurons, and inhibiting Cdk5 changes where NDEL1 sits and how neurites look [niethammer-2000-nudel-cdk5-abstract; sasaki-2000-lis1-nudel-dynein-abstract]. Cdk5-phosphorylated NDEL1 is bound by 14-3-3ε (YWHAE), which protects the phosphorylation from removal. Mice lacking 14-3-3ε mislocalize NDEL1 and LIS1 and have neuronal migration defects, and these defects worsen when combined with Lis1 heterozygosity. This finding explains why Miller–Dieker deletions, which remove both genes, are more severe than LIS1 loss alone [toyooka-2003-14-3-3epsilon-nudel-abstract]. The same Cdk5 phosphorylation promotes binding to the microtubule-severing enzyme katanin p60 [toyooka-2005-katanin-ndel1-abstract].

In mitosis, CDK1 (Cdc2) and ERK1/2 phosphorylate the same S/T-P motifs. Phosphorylation, or phosphomimetic mutations, strengthens LIS1 binding and moves NDEL1 from the centrosome to the spindle [yan-2003-nudel-mitotic-spindle-abstract]. At mitotic entry, Aurora A phosphorylates NDEL1 at S251. This phosphorylation is needed for centrosome maturation and separation, and the phosphorylated protein is then degraded through ubiquitination [mori-2007-aurora-a-ndel1-centrosome-abstract]. In neurons, an aPKC → Aurora A (T287) → NDEL1 S251 cascade at the neurite hillock recruits NDEL1 and supports microtubule emanation from the microtubule organizing center during neurite extension [mori-2009-apkc-aurora-ndel1-abstract]. A separate priming cascade acts at the C-terminal end. DYRK2 phosphorylates S336, which primes GSK3β to phosphorylate S332, and the scaffold TARA brings the two kinases together. This dual phosphorylation increases F-actin dynamics and promotes outgrowth and branching of axons and dendrites [woo-2019-dyrk2-gsk3b-ndel1-fulltext]. Palmitoylation adds a reversible lipid-based layer of control. Palmitoylated NDEL1 binds dynein less well and reduces dynein-dependent processes, including Golgi positioning, VSVG trafficking, retrograde transport and neuronal migration [shmueli-2010-ndel1-palmitoylation-abstract]. UniProt assigns this modification to Cys273 and lists ZDHHC2, ZDHHC3 and ZDHHC7 as the enzymes [uniprot-2026-q9gzm8-human-ndel1-entry]. All of these sites are conserved in the donkey protein (Section 2).

## 7. Biological processes: neuronal migration, mitosis, membrane traffic and cytoskeletal integration

The best-supported process is neuronal migration and positioning during cortical development. In utero knockdown of NDEL1 in mouse neocortex blocked neuronal positioning and separated the centrosome from the nucleus, the same phenotype seen after loss of LIS1 or dynein [shu-2004-ndel1-cortical-positioning-abstract]. Hypomorphic Ndel1 alleles cause mild migration defects that become worse in combination with Lis1 mutations [sasaki-2005-ndel1-knockout-abstract]. Katanin-dependent microtubule severing adds to this function: loss of NDEL1 or dominant-negative p60 lengthens the distance between nucleus and centrosome in migrating neurons [toyooka-2005-katanin-ndel1-abstract]. Human genetics now supports this mouse work. Two patients with pachygyria, one of whom also had subcortical band heterotopia, carry the same de novo mosaic NDEL1 variant, p.R105P. This variant abolishes LIS1 binding, fails to rescue NDEL1 knockdown, and disrupts nucleokinesis when expressed in mouse cortex. Single-cell and spatial transcriptomics show that Nde1 is expressed mainly in dividing radial glia and Ndel1 mainly in postmitotic migrating neurons, which accounts for the different disorders caused by the two paralogs (microcephaly for NDE1, lissencephaly for NDEL1) [tsai-2024-ndel1-lissencephaly-variant-fulltext].

NDEL1 is essential for life. Ndel1-null mice die around implantation, as do Lis1-null and dynein heavy chain-null mice, and their blastocysts fail to proliferate [sasaki-2005-ndel1-knockout-abstract]. In mitosis, NDEL1 supports dynein-driven transport of kinetochore proteins toward the poles, a process that helps switch off the spindle checkpoint [yan-2003-nudel-mitotic-spindle-abstract]. Blocking NudE and NudEL together arrests cells in metaphase, with misaligned chromosomes and dynein and dynactin displaced from kinetochores [stehman-2007-nude-nudel-mitosis-fulltext]. Individual depletion shows that the paralogs divide the work. NDE1 is needed to recruit dynein to kinetochores, whereas loss of NDEL1 causes kinetochore misattachments that the checkpoint does not detect, and therefore lagging chromosomes in anaphase [vergnolle-2007-cenpf-ndel1-abstract]. At the centrosome, NDEL1 also helps cells enter the cell cycle by suppressing the primary cilium. It stabilizes trichoplein at the subdistal appendages and so keeps Aurora A active, and kidney tubules of Ndel1-hypomorphic newborn mice contain more ciliated, quiescent cells [inaba-2016-ndel1-ciliogenesis-fulltext].

In interphase membrane traffic, NDEL1 mutants that cannot bind LIS1 or dynein scatter dynein-dependent organelles and slow the minus-end movement of lysosomes, and NDEL1 knockdown fragments the Golgi [liang-2004-nudel-membrane-traffic-fulltext]. In neurons, NDEL1 at the axon initial segment, together with LIS1, activates dynein locally to turn back somatodendritic cargo that enters the proximal axon. Blocking the ankyrin-G–NDEL1 interface with a structure-based peptide disrupts this polarized sorting [kuijpers-2016-ndel1-axon-initial-segment-abstract; ye-2020-ndel1-ankyrin-abstract]. Ndel1-null fibroblasts mislocalize β-COP vesicles [sasaki-2005-ndel1-knockout-abstract]. Structural work shows that GTP-bound Rab9A/B uses NDE1/NDEL1 as an effector to link late endosomes to dynein for retrograde transport to the trans-Golgi network. The crystal structure was solved with NDE1, and the NDEL1 role is inferred from sequence similarity and from cell assays [zhang-2022-nde1-rab9-abstract; uniprot-2026-q9gzm8-human-ndel1-entry].

Beyond microtubules, NDEL1 binds neurofilament light chain directly and promotes neurofilament assembly. Knocking it down destabilizes NF-L and produces neurodegeneration-like changes [nguyen-2004-nudel-neurofilament-abstract]. NDEL1 also assembles a vimentin–dynein–LIS1–αCOP complex that drives dynein-mediated transport of vimentin during neurite outgrowth [shim-2008-ndel1-vimentin-abstract]. Its interaction with DISC1, which the schizophrenia-associated truncated form of DISC1 cannot make, connects NDEL1 to neurite outgrowth and to psychiatric genetics [ozeki-2003-disc1-nudel-abstract; bradshaw-2017-nde1-ndel1-review-abstract]. NDEL1 is also needed after development is complete. Deleting Ndel1 postnatally causes fragmented microtubules, dendritic and synaptic pathology, hyperexcitability and dispersion of CA1 pyramidal neurons, and a single Reelin injection improves these defects [jiang-2016-ndel1-reelin-ca1-abstract].

## 8. Open questions

The main uncertainty for this entry is the 143-residue C-terminal extension of donkey A0A9L0IJ72. It replaces the short human tail after residue 338, which also removes the region around human Ser344, a mapped phosphosite. Donkey oocyte RNA-seq already shows that NDEL1 isoform usage is regulated [sananmuang-2024-oocyte-transcript-usage-abstract]. Mining those data for the 3′ exon structure, or long-read transcriptomics and proteomics of donkey or horse tissue, would show whether this isoform is a real protein product or a gene-model artifact. Several other NDEL1 models exist in both species. Even if the variant is expressed, it should not affect dimerization, LIS1 binding or dynein binding. It could, however, change the C-terminal effects on dynein affinity and LIS1 sequestration that Garrott et al. described [garrott-2023-ndel1-dynein-dynactin-fulltext], and it could change binding to CENP-F or neurofilaments, both mapped to the C-terminal half [uniprot-2026-q9gzm8-human-ndel1-entry].

It is also unclear whether the equid-specific tail affects regulation at the C-terminal end. The DYRK2/GSK3β sites S332 and S336 lie just before the point where the donkey sequence diverges, and the priming and docking of these kinases could depend on the residues that follow [woo-2019-dyrk2-gsk3b-ndel1-fulltext]. The C-terminal coiled coil that binds ankyrin [ye-2020-ndel1-ankyrin-abstract] should be mapped onto the donkey sequence to confirm that it lies within the conserved region.

More generally, the field has not yet reconciled the inhibitory effect of NDEL1 on dynein activation in vitro [garrott-2023-ndel1-dynein-dynactin-fulltext] with its positive role in cells and in NDE1 reconstitutions [zhao-2023-nde1-lis1-dynein-fulltext; okada-2023-ic-ndel1-dynein-fulltext; yang-2026-nde1-lis1-autoinhibited-dynein-abstract]. There is a further contradiction about phosphorylation. Phosphomimetic CDK sites strengthen inhibition in vitro [garrott-2023-ndel1-dynein-dynactin-fulltext], whereas in axons loss of these sites is what shuts transport down [pandey-2011-cdk5-switch-ndel1-abstract]. Useful next steps would be to identify what triggers NDEL1 release in cells (CCSer2 is one candidate [zang-2025-ccser2-dynein-abstract]), to measure how much NDEL1 and NDE1 overlap in function, and to obtain a structure of full-length NDEL1 bound to dynein and LIS1. The oligopeptidase claim [hayashi-2005-nudel-oligopeptidase-abstract] should be treated as doubtful until it is independently reproduced with purified recombinant protein. The Rab9-effector role was shown structurally with NDE1 and still needs direct testing for NDEL1 [zhang-2022-nde1-rab9-abstract]. Finally, no functional, expression or genetic-variation data exist for NDEL1 in equids. Any phenotypic role in donkeys (for example, in neurodevelopment) remains untested and is inferred entirely from rodent and human studies.

## 9. References

- **uniprot-2026-a0a9l0ij72-entry**: UniProtKB/TrEMBL entry A0A9L0IJ72_EQUAS (entry version 14, 02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0IJ72.txt. Sequence from Wang C et al. (2020) Nat Commun 11:6014, PMID: 33293529.
- **uniprot-2026-q9gzm8-human-ndel1-entry**: UniProtKB/Swiss-Prot entry Q9GZM8 (NDEL1_HUMAN). https://rest.uniprot.org/uniprotkb/Q9GZM8.txt
- **uniprot-2026-equus-ndel1-isoforms-search**: UniProtKB search for gene NDEL1 in taxa 9793/9796. https://rest.uniprot.org/uniprotkb/search?query=gene_exact:NDEL1+AND+(taxonomy_id:9796+OR+taxonomy_id:9793)
- **bradshaw-2017-nde1-ndel1-review**: Bradshaw NJ, Hayashi MA (2017). NDE1 and NDEL1 from genes to (mal)functions: parallel but distinct roles impacting on neurodevelopmental disorders and psychiatric illness. *Cellular and molecular life sciences : CMLS* 74(7):1191-1210. PMID: 27742926; PMCID: PMC11107680; DOI: 10.1007/s00018-016-2395-7; https://doi.org/10.1007/s00018-016-2395-7; https://pubmed.ncbi.nlm.nih.gov/27742926/
- **cianfrocco-2015-dynein-review**: Cianfrocco MA, DeSantis ME, Leschziner AE et al. (2015). Mechanism and regulation of cytoplasmic dynein. *Annual review of cell and developmental biology* 31:83-108. PMID: 26436706; PMCID: PMC4644480; DOI: 10.1146/annurev-cellbio-100814-125438; https://doi.org/10.1146/annurev-cellbio-100814-125438; https://pubmed.ncbi.nlm.nih.gov/26436706/
- **derewenda-2007-ndel1-structure**: Derewenda U, Tarricone C, Choi WC et al. (2007). The structure of the coiled-coil domain of Ndel1 and the basis of its interaction with Lis1, the causal protein of Miller-Dieker lissencephaly. *Structure (London, England : 1993)* 15(11):1467-81. PMID: 17997972; DOI: 10.1016/j.str.2007.09.015; https://doi.org/10.1016/j.str.2007.09.015; https://pubmed.ncbi.nlm.nih.gov/17997972/
- **gao-2015-gsk3b-dynein-ndel1**: Gao FJ, Hebbar S, Gao XA et al. (2015). GSK-3β Phosphorylation of Cytoplasmic Dynein Reduces Ndel1 Binding to Intermediate Chains and Alters Dynein Motility. *Traffic (Copenhagen, Denmark)* 16(9):941-61. PMID: 26010407; PMCID: PMC4543430; DOI: 10.1111/tra.12304; https://doi.org/10.1111/tra.12304; https://pubmed.ncbi.nlm.nih.gov/26010407/
- **garrott-2023-ndel1-dynein-dynactin**: Garrott SR, Gillies JP, Siva A et al. (2023). Ndel1 disfavors dynein-dynactin-adaptor complex formation in two distinct ways. *The Journal of biological chemistry* 299(6):104735. PMID: 37086789; PMCID: PMC10248797; DOI: 10.1016/j.jbc.2023.104735; https://doi.org/10.1016/j.jbc.2023.104735; https://pubmed.ncbi.nlm.nih.gov/37086789/
- **guo-2006-nudel-centriole**: Guo J, Yang Z, Song W et al. (2006). Nudel contributes to microtubule anchoring at the mother centriole and is involved in both dynein-dependent and -independent centrosomal protein assembly. *Molecular biology of the cell* 17(2):680-9. PMID: 16291865; PMCID: PMC1356579; DOI: 10.1091/mbc.e05-04-0360; https://doi.org/10.1091/mbc.e05-04-0360; https://pubmed.ncbi.nlm.nih.gov/16291865/
- **hayashi-2005-nudel-oligopeptidase**: Hayashi MA, Portaro FC, Bastos MF et al. (2005). Inhibition of NUDEL (nuclear distribution element-like)-oligopeptidase activity by disrupted-in-schizophrenia 1. *Proceedings of the National Academy of Sciences of the United States of America* 102(10):3828-33. PMID: 15728732; PMCID: PMC553309; DOI: 10.1073/pnas.0500330102; https://doi.org/10.1073/pnas.0500330102; https://pubmed.ncbi.nlm.nih.gov/15728732/
- **inaba-2016-ndel1-ciliogenesis**: Inaba H, Goto H, Kasahara K et al. (2016). Ndel1 suppresses ciliogenesis in proliferating cells by regulating the trichoplein-Aurora A pathway. *The Journal of cell biology* 212(4):409-23. PMID: 26880200; PMCID: PMC4754717; DOI: 10.1083/jcb.201507046; https://doi.org/10.1083/jcb.201507046; https://pubmed.ncbi.nlm.nih.gov/26880200/
- **jiang-2016-ndel1-reelin-ca1**: Jiang Y, Gavrilovici C, Chansard M et al. (2016). Ndel1 and Reelin Maintain Postnatal CA1 Hippocampus Integrity. *The Journal of neuroscience : the official journal of the Society for Neuroscience* 36(24):6538-52. PMID: 27307241; PMCID: PMC6601920; DOI: 10.1523/JNEUROSCI.2869-15.2016; https://doi.org/10.1523/JNEUROSCI.2869-15.2016; https://pubmed.ncbi.nlm.nih.gov/27307241/
- **kuijpers-2016-ndel1-axon-initial-segment**: Kuijpers M, van de Willige D, Freal A et al. (2016). Dynein Regulator NDEL1 Controls Polarized Cargo Transport at the Axon Initial Segment. *Neuron* 89(3):461-71. PMID: 26844830; DOI: 10.1016/j.neuron.2016.01.022; https://doi.org/10.1016/j.neuron.2016.01.022; https://pubmed.ncbi.nlm.nih.gov/26844830/
- **li-2005-nudel-dynein-mt-ends**: Li J, Lee WL, Cooper JA (2005). NudEL targets dynein to microtubule ends through LIS1. *Nature cell biology* 7(7):686-90. PMID: 15965467; PMCID: PMC1569433; DOI: 10.1038/ncb1273; https://doi.org/10.1038/ncb1273; https://pubmed.ncbi.nlm.nih.gov/15965467/
- **liang-2004-nudel-membrane-traffic**: Liang Y, Yu W, Li Y et al. (2004). Nudel functions in membrane traffic mainly through association with Lis1 and cytoplasmic dynein. *The Journal of cell biology* 164(4):557-66. PMID: 14970193; PMCID: PMC2171987; DOI: 10.1083/jcb.200308058; https://doi.org/10.1083/jcb.200308058; https://pubmed.ncbi.nlm.nih.gov/14970193/
- **mckenney-2010-lis1-nude-dynein-force**: McKenney RJ, Vershinin M, Kunwar A et al. (2010). LIS1 and NudE induce a persistent dynein force-producing state. *Cell* 141(2):304-14. PMID: 20403325; PMCID: PMC2881166; DOI: 10.1016/j.cell.2010.02.035; https://doi.org/10.1016/j.cell.2010.02.035; https://pubmed.ncbi.nlm.nih.gov/20403325/
- **mori-2007-aurora-a-ndel1-centrosome**: Mori D, Yano Y, Toyo-oka K et al. (2007). NDEL1 phosphorylation by Aurora-A kinase is essential for centrosomal maturation, separation, and TACC3 recruitment. *Molecular and cellular biology* 27(1):352-67. PMID: 17060449; PMCID: PMC1800650; DOI: 10.1128/MCB.00878-06; https://doi.org/10.1128/MCB.00878-06; https://pubmed.ncbi.nlm.nih.gov/17060449/
- **mori-2009-apkc-aurora-ndel1**: Mori D, Yamada M, Mimori-Kiyosue Y et al. (2009). An essential role of the aPKC-Aurora A-NDEL1 pathway in neurite elongation by modulation of microtubule dynamics. *Nature cell biology* 11(9):1057-68. PMID: 19668197; DOI: 10.1038/ncb1919; https://doi.org/10.1038/ncb1919; https://pubmed.ncbi.nlm.nih.gov/19668197/
- **nguyen-2004-nudel-neurofilament**: Nguyen MD, Shu T, Sanada K et al. (2004). A NUDEL-dependent mechanism of neurofilament assembly regulates the integrity of CNS neurons. *Nature cell biology* 6(7):595-608. PMID: 15208636; DOI: 10.1038/ncb1139; https://doi.org/10.1038/ncb1139; https://pubmed.ncbi.nlm.nih.gov/15208636/
- **niethammer-2000-nudel-cdk5**: Niethammer M, Smith DS, Ayala R et al. (2000). NUDEL is a novel Cdk5 substrate that associates with LIS1 and cytoplasmic dynein. *Neuron* 28(3):697-711. PMID: 11163260; DOI: 10.1016/s0896-6273(00)00147-1; https://doi.org/10.1016/s0896-6273(00)00147-1; https://pubmed.ncbi.nlm.nih.gov/11163260/
- **okada-2023-ic-ndel1-dynein**: Okada K, Iyer BR, Lammers LG et al. (2023). Conserved roles for the dynein intermediate chain and Ndel1 in assembly and activation of dynein. *Nature communications* 14(1):5833. PMID: 37730751; PMCID: PMC10511499; DOI: 10.1038/s41467-023-41466-5; https://doi.org/10.1038/s41467-023-41466-5; https://pubmed.ncbi.nlm.nih.gov/37730751/
- **ozeki-2003-disc1-nudel**: Ozeki Y, Tomoda T, Kleiderlein J et al. (2003). Disrupted-in-Schizophrenia-1 (DISC-1): mutant truncation prevents binding to NudE-like (NUDEL) and inhibits neurite outgrowth. *Proceedings of the National Academy of Sciences of the United States of America* 100(1):289-94. PMID: 12506198; PMCID: PMC140954; DOI: 10.1073/pnas.0136913100; https://doi.org/10.1073/pnas.0136913100; https://pubmed.ncbi.nlm.nih.gov/12506198/
- **pandey-2011-cdk5-switch-ndel1**: Pandey JP, Smith DS (2011). A Cdk5-dependent switch regulates Lis1/Ndel1/dynein-driven organelle transport in adult axons. *The Journal of neuroscience : the official journal of the Society for Neuroscience* 31(47):17207-19. PMID: 22114287; PMCID: PMC3249231; DOI: 10.1523/JNEUROSCI.4108-11.2011; https://doi.org/10.1523/JNEUROSCI.4108-11.2011; https://pubmed.ncbi.nlm.nih.gov/22114287/
- **sananmuang-2024-oocyte-transcript-usage**: Sananmuang T, Puthier D, Nguyen C et al. (2024). Differential transcript usage across mammalian oocytes at the germinal vesicle and metaphase II stages. *Theriogenology* 215:1-9. PMID: 37995439; DOI: 10.1016/j.theriogenology.2023.11.016; https://doi.org/10.1016/j.theriogenology.2023.11.016; https://pubmed.ncbi.nlm.nih.gov/37995439/
- **sasaki-2000-lis1-nudel-dynein**: Sasaki S, Shionoya A, Ishida M et al. (2000). A LIS1/NUDEL/cytoplasmic dynein heavy chain complex in the developing and adult nervous system. *Neuron* 28(3):681-96. PMID: 11163259; DOI: 10.1016/s0896-6273(00)00146-x; https://doi.org/10.1016/s0896-6273(00)00146-x; https://pubmed.ncbi.nlm.nih.gov/11163259/
- **sasaki-2005-ndel1-knockout**: Sasaki S, Mori D, Toyo-oka K et al. (2005). Complete loss of Ndel1 results in neuronal migration defects and early embryonic lethality. *Molecular and cellular biology* 25(17):7812-27. PMID: 16107726; PMCID: PMC1190282; DOI: 10.1128/MCB.25.17.7812-7827.2005; https://doi.org/10.1128/MCB.25.17.7812-7827.2005; https://pubmed.ncbi.nlm.nih.gov/16107726/
- **shim-2008-ndel1-vimentin**: Shim SY, Samuels BA, Wang J et al. (2008). Ndel1 controls the dynein-mediated transport of vimentin during neurite outgrowth. *The Journal of biological chemistry* 283(18):12232-40. PMID: 18303022; DOI: 10.1074/jbc.M710200200; https://doi.org/10.1074/jbc.M710200200; https://pubmed.ncbi.nlm.nih.gov/18303022/
- **shmueli-2010-ndel1-palmitoylation**: Shmueli A, Segal M, Sapir T et al. (2010). Ndel1 palmitoylation: a new mean to regulate cytoplasmic dynein activity. *The EMBO journal* 29(1):107-19. PMID: 19927128; PMCID: PMC2808373; DOI: 10.1038/emboj.2009.325; https://doi.org/10.1038/emboj.2009.325; https://pubmed.ncbi.nlm.nih.gov/19927128/
- **shu-2004-ndel1-cortical-positioning**: Shu T, Ayala R, Nguyen MD et al. (2004). Ndel1 operates in a common pathway with LIS1 and cytoplasmic dynein to regulate cortical neuronal positioning. *Neuron* 44(2):263-77. PMID: 15473966; DOI: 10.1016/j.neuron.2004.09.030; https://doi.org/10.1016/j.neuron.2004.09.030; https://pubmed.ncbi.nlm.nih.gov/15473966/
- **stehman-2007-nude-nudel-mitosis**: Stehman SA, Chen Y, McKenney RJ et al. (2007). NudE and NudEL are required for mitotic progression and are involved in dynein recruitment to kinetochores. *The Journal of cell biology* 178(4):583-94. PMID: 17682047; PMCID: PMC2064466; DOI: 10.1083/jcb.200610112; https://doi.org/10.1083/jcb.200610112; https://pubmed.ncbi.nlm.nih.gov/17682047/
- **toyooka-2003-14-3-3epsilon-nudel**: Toyo-oka K, Shionoya A, Gambello MJ et al. (2003). 14-3-3epsilon is important for neuronal migration by binding to NUDEL: a molecular explanation for Miller-Dieker syndrome. *Nature genetics* 34(3):274-85. PMID: 12796778; DOI: 10.1038/ng1169; https://doi.org/10.1038/ng1169; https://pubmed.ncbi.nlm.nih.gov/12796778/
- **toyooka-2005-katanin-ndel1**: Toyo-Oka K, Sasaki S, Yano Y et al. (2005). Recruitment of katanin p60 by phosphorylated NDEL1, an LIS1 interacting protein, is essential for mitotic cell division and neuronal migration. *Human molecular genetics* 14(21):3113-28. PMID: 16203747; DOI: 10.1093/hmg/ddi339; https://doi.org/10.1093/hmg/ddi339; https://pubmed.ncbi.nlm.nih.gov/16203747/
- **tsai-2024-ndel1-lissencephaly-variant**: Tsai MH, Ke HC, Lin WC et al. (2024). Novel lissencephaly-associated NDEL1 variant reveals distinct roles of NDE1 and NDEL1 in nucleokinesis and human cortical malformations. *Acta neuropathologica* 147(1):13. PMID: 38194050; PMCID: PMC10776482; DOI: 10.1007/s00401-023-02665-y; https://doi.org/10.1007/s00401-023-02665-y; https://pubmed.ncbi.nlm.nih.gov/38194050/
- **vergnolle-2007-cenpf-ndel1**: Vergnolle MA, Taylor SS (2007). Cenp-F links kinetochores to Ndel1/Nde1/Lis1/dynein microtubule motor complexes. *Current biology : CB* 17(13):1173-9. PMID: 17600710; DOI: 10.1016/j.cub.2007.05.077; https://doi.org/10.1016/j.cub.2007.05.077; https://pubmed.ncbi.nlm.nih.gov/17600710/
- **woo-2019-dyrk2-gsk3b-ndel1**: Woo Y, Kim SJ, Suh BK et al. (2019). Sequential phosphorylation of NDEL1 by the DYRK2-GSK3β complex is critical for neuronal morphogenesis. *eLife* 8:None. PMID: 31815665; PMCID: PMC6927744; DOI: 10.7554/eLife.50850; https://doi.org/10.7554/eLife.50850; https://pubmed.ncbi.nlm.nih.gov/31815665/
- **yan-2003-nudel-mitotic-spindle**: Yan X, Li F, Liang Y et al. (2003). Human Nudel and NudE as regulators of cytoplasmic dynein in poleward protein transport along the mitotic spindle. *Molecular and cellular biology* 23(4):1239-50. PMID: 12556484; PMCID: PMC141156; DOI: 10.1128/MCB.23.4.1239-1250.2003; https://doi.org/10.1128/MCB.23.4.1239-1250.2003; https://pubmed.ncbi.nlm.nih.gov/12556484/
- **yang-2026-nde1-lis1-autoinhibited-dynein**: Yang J, Zhao Y, Chai P et al. (2026). Nde1 promotes Lis1 binding to full-length autoinhibited human dynein 1. *Nature chemical biology* 22(2):274-283. PMID: 40751002; PMCID: PMC12965811; DOI: 10.1038/s41589-025-01981-6; https://doi.org/10.1038/s41589-025-01981-6; https://pubmed.ncbi.nlm.nih.gov/40751002/
- **ye-2020-ndel1-ankyrin**: Ye J, Li J, Ye F et al. (2020). Mechanistic insights into the interactions of dynein regulator Ndel1 with neuronal ankyrins and implications in polarity maintenance. *Proceedings of the National Academy of Sciences of the United States of America* 117(2):1207-1215. PMID: 31889000; PMCID: PMC6969496; DOI: 10.1073/pnas.1916987117; https://doi.org/10.1073/pnas.1916987117; https://pubmed.ncbi.nlm.nih.gov/31889000/
- **zang-2025-ccser2-dynein**: Zang JL, Gibson D, Zheng AM et al. (2025). CCSer2 gates dynein activity at the cell periphery. *The Journal of cell biology* 224(6):None. PMID: 40261303; PMCID: PMC12013514; DOI: 10.1083/jcb.202406153; https://doi.org/10.1083/jcb.202406153; https://pubmed.ncbi.nlm.nih.gov/40261303/
- **zhang-2022-nde1-rab9**: Zhang Y, Chen Z, Wang F et al. (2022). Nde1 is a Rab9 effector for loading late endosomes to cytoplasmic dynein motor complex. *Structure (London, England : 1993)* 30(3):386-395.e5. PMID: 34793709; DOI: 10.1016/j.str.2021.10.013; https://doi.org/10.1016/j.str.2021.10.013; https://pubmed.ncbi.nlm.nih.gov/34793709/
- **zhao-2023-nde1-lis1-dynein**: Zhao Y, Oten S, Yildiz A (2023). Nde1 promotes Lis1-mediated activation of dynein. *Nature communications* 14(1):7221. PMID: 37940657; PMCID: PMC10632352; DOI: 10.1038/s41467-023-42907-x; https://doi.org/10.1038/s41467-023-42907-x; https://pubmed.ncbi.nlm.nih.gov/37940657/
- **zylkiewicz-2011-ndel1-scaffold**: Zyłkiewicz E, Kijańska M, Choi WC et al. (2011). The N-terminal coiled-coil of Ndel1 is a regulated scaffold that recruits LIS1 to dynein. *The Journal of cell biology* 192(3):433-45. PMID: 21282465; PMCID: PMC3101096; DOI: 10.1083/jcb.201011142; https://doi.org/10.1083/jcb.201011142; https://pubmed.ncbi.nlm.nih.gov/21282465/


## Citations

1. bradshaw-2017-nde1-ndel1-review-abstract.md
2. bradshaw-2017-nde1-ndel1-review-summary.md
3. cianfrocco-2015-dynein-review-abstract.md
4. cianfrocco-2015-dynein-review-summary.md
5. derewenda-2007-ndel1-structure-abstract.md
6. derewenda-2007-ndel1-structure-summary.md
7. gao-2015-gsk3b-dynein-ndel1-abstract.md
8. gao-2015-gsk3b-dynein-ndel1-fulltext.txt
9. gao-2015-gsk3b-dynein-ndel1-summary.md
10. garrott-2023-ndel1-dynein-dynactin-abstract.md
11. garrott-2023-ndel1-dynein-dynactin-fulltext.txt
12. garrott-2023-ndel1-dynein-dynactin-summary.md
13. guo-2006-nudel-centriole-abstract.md
14. guo-2006-nudel-centriole-summary.md
15. hayashi-2005-nudel-oligopeptidase-abstract.md
16. hayashi-2005-nudel-oligopeptidase-summary.md
17. inaba-2016-ndel1-ciliogenesis-abstract.md
18. inaba-2016-ndel1-ciliogenesis-fulltext.txt
19. inaba-2016-ndel1-ciliogenesis-summary.md
20. jiang-2016-ndel1-reelin-ca1-abstract.md
21. jiang-2016-ndel1-reelin-ca1-summary.md
22. kuijpers-2016-ndel1-axon-initial-segment-abstract.md
23. kuijpers-2016-ndel1-axon-initial-segment-summary.md
24. li-2005-nudel-dynein-mt-ends-abstract.md
25. li-2005-nudel-dynein-mt-ends-summary.md
26. liang-2004-nudel-membrane-traffic-abstract.md
27. liang-2004-nudel-membrane-traffic-fulltext.txt
28. liang-2004-nudel-membrane-traffic-summary.md
29. mckenney-2010-lis1-nude-dynein-force-abstract.md
30. mckenney-2010-lis1-nude-dynein-force-summary.md
31. mori-2007-aurora-a-ndel1-centrosome-abstract.md
32. mori-2007-aurora-a-ndel1-centrosome-summary.md
33. mori-2009-apkc-aurora-ndel1-abstract.md
34. mori-2009-apkc-aurora-ndel1-summary.md
35. nguyen-2004-nudel-neurofilament-abstract.md
36. nguyen-2004-nudel-neurofilament-summary.md
37. niethammer-2000-nudel-cdk5-abstract.md
38. niethammer-2000-nudel-cdk5-summary.md
39. okada-2023-ic-ndel1-dynein-abstract.md
40. okada-2023-ic-ndel1-dynein-fulltext.txt
41. okada-2023-ic-ndel1-dynein-summary.md
42. ozeki-2003-disc1-nudel-abstract.md
43. ozeki-2003-disc1-nudel-summary.md
44. pandey-2011-cdk5-switch-ndel1-abstract.md
45. pandey-2011-cdk5-switch-ndel1-summary.md
46. sananmuang-2024-oocyte-transcript-usage-abstract.md
47. sananmuang-2024-oocyte-transcript-usage-summary.md
48. sasaki-2000-lis1-nudel-dynein-abstract.md
49. sasaki-2000-lis1-nudel-dynein-summary.md
50. sasaki-2005-ndel1-knockout-abstract.md
51. sasaki-2005-ndel1-knockout-summary.md
52. shim-2008-ndel1-vimentin-abstract.md
53. shim-2008-ndel1-vimentin-summary.md
54. shmueli-2010-ndel1-palmitoylation-abstract.md
55. shmueli-2010-ndel1-palmitoylation-summary.md
56. shu-2004-ndel1-cortical-positioning-abstract.md
57. shu-2004-ndel1-cortical-positioning-summary.md
58. stehman-2007-nude-nudel-mitosis-abstract.md
59. stehman-2007-nude-nudel-mitosis-fulltext.txt
60. stehman-2007-nude-nudel-mitosis-summary.md
61. toyooka-2003-14-3-3epsilon-nudel-abstract.md
62. toyooka-2003-14-3-3epsilon-nudel-summary.md
63. toyooka-2005-katanin-ndel1-abstract.md
64. toyooka-2005-katanin-ndel1-summary.md
65. tsai-2024-ndel1-lissencephaly-variant-abstract.md
66. tsai-2024-ndel1-lissencephaly-variant-fulltext.txt
67. tsai-2024-ndel1-lissencephaly-variant-summary.md
68. uniprot-2026-a0a9l0ij72-entry.txt
69. uniprot-2026-equus-ndel1-isoforms-search.tsv
70. uniprot-2026-q9gzm8-human-ndel1-entry.txt
71. vergnolle-2007-cenpf-ndel1-abstract.md
72. vergnolle-2007-cenpf-ndel1-summary.md
73. woo-2019-dyrk2-gsk3b-ndel1-abstract.md
74. woo-2019-dyrk2-gsk3b-ndel1-fulltext.txt
75. woo-2019-dyrk2-gsk3b-ndel1-summary.md
76. yan-2003-nudel-mitotic-spindle-abstract.md
77. yan-2003-nudel-mitotic-spindle-summary.md
78. yang-2026-nde1-lis1-autoinhibited-dynein-abstract.md
79. yang-2026-nde1-lis1-autoinhibited-dynein-summary.md
80. ye-2020-ndel1-ankyrin-abstract.md
81. ye-2020-ndel1-ankyrin-summary.md
82. zang-2025-ccser2-dynein-abstract.md
83. zang-2025-ccser2-dynein-summary.md
84. zhang-2022-nde1-rab9-abstract.md
85. zhang-2022-nde1-rab9-summary.md
86. zhao-2023-nde1-lis1-dynein-abstract.md
87. zhao-2023-nde1-lis1-dynein-fulltext.txt
88. zhao-2023-nde1-lis1-dynein-summary.md
89. zylkiewicz-2011-ndel1-scaffold-abstract.md
90. zylkiewicz-2011-ndel1-scaffold-fulltext.txt
91. zylkiewicz-2011-ndel1-scaffold-summary.md