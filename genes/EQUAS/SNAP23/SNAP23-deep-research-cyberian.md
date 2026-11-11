---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:13:22.467153'
end_time: '2026-10-26T01:27:05.312538'
duration_seconds: 822.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: SNAP23
  gene_symbol: SNAP23
  uniprot_accession: A0A8C4M285
  protein_description: 'SubName: Full=Synaptosome associated protein 23 {ECO:0000313|Ensembl:ENSEASP00005019168.1};'
  gene_info: Name=SNAP23 {ECO:0000313|Ensembl:ENSEASP00005019168.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the SNAP-25 family.
  protein_domains: T_SNARE_dom. (IPR000727)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3303
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
- **UniProt Accession:** A0A8C4M285
- **Protein Description:** SubName: Full=Synaptosome associated protein 23 {ECO:0000313|Ensembl:ENSEASP00005019168.1};
- **Gene Information:** Name=SNAP23 {ECO:0000313|Ensembl:ENSEASP00005019168.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the SNAP-25 family.
- **Key Domains:** T_SNARE_dom. (IPR000727)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SNAP23" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SNAP23' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SNAP23** (gene ID: SNAP23, UniProt: A0A8C4M285) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SNAP23 (Synaptosomal-associated protein 23) in the donkey, *Equus asinus*: UniProt A0A8C4M285

## 1. Introduction and summary

A0A8C4M285 is an unreviewed (TrEMBL) entry produced automatically from the Ensembl gene model ENSEASG00005013173 on donkey chromosome 2. The model was annotated on the chromosome-level Dezhou donkey reference genome [uniprot-A0A8C4M285-entry; wang-2020-donkey-genome-abstract]. The entry names the product "Synaptosome associated protein 23", gene SNAP23, places it in the SNAP-25 family, and identifies a single t-SNARE coiled-coil homology domain (PROSITE PS50192; InterPro IPR000727) at residues 14–76. The only experimental-style annotations it carries are inferred ones: "Cell membrane; Lipid-anchor", plus GO terms for SNARE complex and SNAP receptor activity [uniprot-A0A8C4M285-entry]. The identity check holds. The gene symbol, the protein description, the SNAP-25 family assignment and the t-SNARE domain all match the well-studied mammalian SNAP-23, and residues 1–89 of the donkey sequence are 94% identical to human SNAP-23 (O00161) [uniprot-O00161-entry]. No study on donkey SNAP23 itself exists. The only equid experimental data come from horse platelets, where SNAP-23 was detected and appeared to be activated on stimulation [brunso-2010-equine-platelets-abstract]. Everything else in this report is inferred by orthology from human, mouse and rat work.

SNAP-23 is the ubiquitously expressed paralog of neuronal SNAP-25. It was first found as a 23-kDa human B-lymphocyte protein that binds many syntaxins and VAMPs tightly, and it is expressed in every tissue examined [ravichandran-1996-snap23-discovery-abstract]. It was found independently in mouse as "syndet" [wang-1997-syndet-abstract]. In molecular terms it is a Qbc-SNARE, a target-membrane SNARE that lacks a transmembrane domain. It carries two SNARE motifs, an N-terminal Qb motif and a C-terminal Qc motif. A central cysteine-rich linker is palmitoylated and anchors the protein to the inner leaflet of the plasma membrane [kadkova-2019-snap25-family-review-abstract; vogel-1999-palmitoylation-abstract; agarwal-2019-cysteine-rich-domain-abstract]. The protein has no catalytic activity. Its "primary function" is structural: with a Qa-syntaxin (most often syntaxin-4, but also syntaxin-2, -3, -6 or -11) and an R-SNARE on the vesicle (VAMP2, VAMP3, VAMP7 or VAMP8), it supplies two of the four helices of the trans-SNARE bundle. The energy released as that bundle zippers drives the vesicle membrane to fuse with the plasma membrane [sutton-1998-snare-structure-abstract; freedman-2003-homotetramer-abstract; rea-1998-syndet-glut4-abstract; kawanishi-2000-glut4-3t3l1-abstract]. Through this activity SNAP-23 is required for regulated exocytosis in platelets, mast cells and neutrophils, for insulin-stimulated GLUT4 delivery in adipocytes, for TLR4 recycling to the macrophage surface, for Ca²⁺-triggered lysosomal exocytosis with syntaxin-4 and VAMP7, and for delivering MHC-I to phagosomes for cross-presentation in dendritic cells [rao-2004-lysosomal-exocytosis-abstract; nairgupta-2014-dc-cross-presentation-abstract]. In several of these pathways, signalling reaches SNAP-23 through IKK2-mediated phosphorylation of its linker [suzuki-2008-ikk2-mast-cell-abstract; karim-2013-ikk-platelet-abstract]. It also takes part in constitutive exocytosis needed for cell survival and early embryonic development [williams-2018-platelet-snap23-deletion-abstract; cardenas-2021-platelet-mast-cell-development-abstract; kinoshita-2019-tlr4-stx11-abstract; suh-2011-knockout-lethality-abstract; kaul-2015-cell-survival-abstract].

The key caveat for this accession is that A0A8C4M285 is only 97 residues long. Its first 89 residues correspond to the N-terminal Qb SNARE motif and the cysteine-rich palmitoylation cluster. The sequence then diverges (…CNR**FNIRSRAQ**) and ends, so the product lacks the C-terminal Qc SNARE motif. The donkey proteome contains other SNAP23 gene products, including a 211-residue canonical-length form (A0A8C4M333) [uniprot-donkey-snap23-isoforms-sequences]. In Ensembl, A0A8C4M285 is encoded by a transcript that shares exons 1–4 with the full-length forms and ends in a predicted alternative terminal exon [ensembl-ENSEASG00005013173-gene]. It is therefore a truncated splice variant predicted from the gene model, with no expression evidence. On its own it cannot form a complete fusogenic SNARE complex, as Section 6 explains.

## 2. Identity, sequence features and domain architecture

UniProt lists five *E. asinus* SNAP23 entries, all from the same reference proteome: A0A8C4M5X5 (222 aa), A0A8C4M333 (211 aa), A0A9L0K6I4 (209 aa), A0A9L0J3X0 (158 aa) and the subject of this report, A0A8C4M285 (97 aa) [uniprot-donkey-snap23-isoforms-sequences]. All five share the same N-terminus, MDNLSSEEIQLR…. The 211-residue form is 189/211 (≈90%) identical to human SNAP-23a (O00161-1) over its full length, and it ends in the canonical C-terminal motif …ADTNKDRIDNANARAKKLIDS. This confirms that the locus is the true SNAP23 ortholog and not a different gene with a similar symbol [uniprot-O00161-entry; uniprot-donkey-snap23-isoforms-sequences].

Comparing A0A8C4M285 with human SNAP-23 gives five substitutions in residues 1–89: Q11L, I16V, K49G, G58S and L59M. Several features known to matter in the human protein are conserved. The first is the N-terminal 18 residues, which deletion mapping showed are needed for binding both syntaxin and VAMP [vaidyanathan-2001-last-exon-abstract]. The second is the Qb coiled-coil (UniProt domain 14–76), including Gln-48. In the SNAP-23N crystal structure this glutamine is buried at the helix interface and corresponds to the "0-layer" glutamine of the SNARE ionic layer [freedman-2003-homotetramer-abstract; sutton-1998-snare-structure-abstract]. The third is the full cysteine cluster C79, C80, C83, C85 and C87. The five cysteines of SNAP-23 are palmitoylated, and C79, C80 and C83 are especially important for membrane association [agarwal-2019-cysteine-rich-domain-abstract].

The point of divergence, immediately after Arg-89, is noteworthy. In the human SNAP-23b isoform, residues 90–142 are deleted by alternative splicing [mollinedo-1997-snap23-isoforms-abstract], and in the UniProt human entry the 23a and 23b sequences likewise diverge right after …CPCNR [uniprot-O00161-entry]. The truncated donkey product therefore switches to new sequence at the same position as a known splice junction. The Ensembl gene model explains how this happens. Gene ENSEASG00005013173 spans about 15 kb on chromosome 2 (minus strand) and has five protein-coding transcripts [ensembl-ENSEASG00005013173-gene]. Transcript ENSEAST00005020804, which encodes A0A8C4M285, shares its first four exons (104, 42, 49 and 118 bp) with the 211-residue transcript ENSEAST00005020803. Its fifth and final exon is a 96-bp segment at chr2:191,100,026–191,100,121. That segment sits inside the intron that, in the full-length transcripts, separates exon 4 from the exon encoding the linker and Qc region [ensembl-ENSEASG00005013173-gene]. Only 28 nucleotides of this terminal exon are coding (…AGA TTT AAC ATC AGA AGC CGG GCT CAG TAA), which add FNIRSRAQ and then a stop codon [ensembl-ENSEAST00005020804-cds]. So A0A8C4M285 is the product of a predicted alternative terminal exon, not of intron retention. The exon 4/exon 5 junction falls exactly at the codon-89 boundary that the human SNAP-23b splice also uses. Whether this terminal exon is actually used in donkey tissues has not been tested. Human SNAP23 is known to make at least five splice variants (a–e) in inflammatory cells, and these differ in subcellular distribution [shukla-2001-snap23-splice-variants-abstract]. A truncated equid variant is therefore biologically plausible, but it could equally be a gene-model artefact.

## 3. Molecular function: a Qbc t-SNARE that supplies two helices to the fusion complex

SNARE complexes are parallel four-helix bundles. In the founding neuronal structure, syntaxin-1A and synaptobrevin-II each contribute one helix and SNAP-25 contributes two. Leucine-zipper-like layers flank a central ionic layer made of one arginine and three glutamines [sutton-1998-snare-structure-abstract]. The SNAP-25 family, comprising SNAP-25, SNAP-23, SNAP-29 and SNAP-47 in vertebrates, is defined by having both the Qb and the Qc SNARE domain in one polypeptide [kadkova-2019-snap25-family-review-abstract]. Of these, SNAP-23 is the member that drives regulated exocytosis outside the nervous system, and SNAP-25 and SNAP-23 can partly substitute for each other in cross-rescue experiments [kadkova-2019-snap25-family-review-abstract].

Biochemical evidence for this role in SNAP-23 comes from several directions. Human SNAP-23 binds multiple syntaxins and VAMPs in vitro [ravichandran-1996-snap23-discovery-abstract]. In 3T3-L1 adipocytes, VAMP2, syntaxin-4 and syndet/SNAP-23 form an SDS-resistant ternary complex, measured by surface plasmon resonance [rea-1998-syndet-glut4-abstract]. Wild-type SNAP23 promotes binding between syntaxin-4 and VAMP2 [kawanishi-2000-glut4-3t3l1-abstract]. The isolated N-terminal coiled coil, SNAP-23N, assembles spontaneously with SNAP-23C, syntaxin-4 and VAMP-3 into a heterotetramer. On its own it crystallizes as a parallel homotetramer, which shows how a single coiled-coil motif can join several different SNARE assemblies [freedman-2003-homotetramer-abstract]. Truncations show that the two halves of the protein do different jobs. Removing the N-terminal 18 residues abolishes binding to both syntaxin and VAMP. Removing the C-terminal 23 residues, encoded by the last exon, leaves syntaxin binding intact but abolishes VAMP binding [vaidyanathan-2001-last-exon-abstract]. Similarly, SNAP23 residues 1–202 bind syntaxin-4 but not VAMP2 and act as a dominant negative for GLUT4 translocation, whereas residues 1–161 bind neither partner [kawanishi-2000-glut4-3t3l1-abstract].

SNAP-23 pairs with several Qa-syntaxins depending on the cell type. These include syntaxin-4 in adipocytes and at the mast-cell and neutrophil plasma membrane, syntaxin-2 in platelet dense-granule release, syntaxin-6 in neutrophils, and syntaxin-11 in lymphocytes and macrophages [rea-1998-syndet-glut4-abstract; chen-2000-platelet-dense-granule-abstract; martinmartin-2000-neutrophil-abstract; valdez-1999-stx11-late-endosome-abstract; kinoshita-2019-tlr4-stx11-abstract; gigon-2023-neutrophil-degranulation-abstract]. The R-SNARE partners reported include VAMP2, VAMP3 and VAMP8 [rea-1998-syndet-glut4-abstract; freedman-2003-homotetramer-abstract; kinoshita-2019-tlr4-stx11-fulltext]. Fusion also depends on the general SNARE recycling machinery: platelet dense-granule release is stimulated by α-SNAP and blocked by dominant-negative α-SNAP or by anti-NSF antibodies [chen-2000-platelet-dense-granule-abstract].

## 4. Membrane anchoring and subcellular localization

SNAP-23 has neither a signal sequence nor a transmembrane segment. It is still tightly bound to membranes, through acylation of its cysteine-rich domain [wang-1997-syndet-abstract]. Palmitoylation of the central cysteine cluster was shown in vivo, and the level of palmitoylation correlated with how well the protein bound syntaxin in cells [vogel-1999-palmitoylation-abstract]. Mutagenesis in RBL mast cells settled the point. A mutant lacking all five cysteines, or a P119A mutant thought to block recognition by palmitoyl transferases, was entirely cytosolic and inhibited exocytosis in a dominant-negative way. Grafting a heterologous transmembrane anchor onto the cysteine-free mutant restored both membrane association and exocytosis [agarwal-2019-cysteine-rich-domain-abstract]. The palmitoylated region also sends SNAP-23 into cholesterol- and sphingolipid-rich raft domains. About 54% of endogenous SNAP-23 in PC12 cells is raft-associated, roughly three times the fraction for SNAP-25, and this difference maps to a cysteine in SNAP-23 at the position where SNAP-25 has a conserved phenylalanine [salaun-2005-lipid-rafts-abstract]. UniProt lists ZDHHC13 and ZDHHC17 as interacting palmitoyl transferases [uniprot-O00161-entry]. All five cysteines are conserved in A0A8C4M285, so the truncated donkey product is predicted to be palmitoylated and membrane-associated, consistent with its automatic "Cell membrane; Lipid-anchor" annotation [uniprot-A0A8C4M285-entry].

In most cells SNAP-23 sits mainly at the plasma membrane. In polarized HepG2 and MDCK epithelial cells it is found at both the apical and basolateral surfaces with little intracellular staining, which suggests it acts as a general plasma-membrane t-SNARE. Canine SNAP-23 is also cleaved by botulinum neurotoxin E [low-1998-polarized-epithelia-abstract]. In adipocytes it is found at the plasma membrane and in an intracellular compartment [wang-1997-syndet-abstract]. In some secretory cells it moves: in mast cells, stimulation shifts SNAP-23 from lamellipodia-like surface projections onto granule membranes [guo-1998-mast-cell-compound-exocytosis-abstract]. In resting neutrophils it sits mainly on specific and tertiary granules and moves to the cell surface on activation [martinmartin-2000-neutrophil-abstract]. Platelets keep a substantial soluble, non-membrane pool [chen-2000-platelet-dense-granule-abstract]. SNAP-23 has also been reported on cytosolic lipid droplets, where together with syntaxin-5 and VAMP4 it was said to promote droplet–droplet fusion [bostrom-2007-lipid-droplet-fusion-abstract]. That report should be read with caution. A later paper on SNAP23 by the same first author was retracted, and the retraction notice states that this author was found guilty of scientific misconduct by the University of Gothenburg [bostrom-2010-retraction-notice-fulltext]. The 2007 paper has not been retracted, as far as PubMed shows, but its lipid-droplet findings have not been independently confirmed in the literature reviewed here.

## 5. Biological processes and pathways

**Platelet granule secretion (hemostasis).** Platelet secretion is the process where genetic evidence for SNAP-23 is strongest. Early work showed that antibodies against SNAP-23, or an inhibitory C-terminal SNAP-23 peptide, block calcium-induced dense-granule release, and that SNAP-23 forms a complex with syntaxin-2 in platelets [chen-2000-platelet-dense-granule-abstract]. SNAP-23 is regulated by phosphorylation. Ser95 and Ser120, in the Qb–Qc linker, become phosphorylated when platelets or mast cells are activated [hepp-2005-phosphorylation-mast-cell-abstract]. In platelets, Ser95 phosphorylation lies downstream of phospholipase C, Ca²⁺ and PKC, and requires IκB kinase-β. Blocking IKK-β prevents SNARE complex formation and secretion, and phosphorylated SNAP-23 increases fusion of SNARE proteoliposomes [karim-2013-ikk-platelet-abstract]. Platelet-specific *Snap23* deletion in mice abolishes dense-, α- and lysosomal-granule secretion while granule cargo and granule number stay normal. The mice also develop macrothrombocytopenia, a bleeding defect and almost no arterial or venous thrombosis, making SNAP23 the first single gene shown to be essential for every kind of platelet exocytosis [williams-2018-platelet-snap23-deletion-abstract]. An independent conditional knockout confirmed the degranulation defect. It also found fewer α-granules and abnormal surface translocation of membrane proteins, which points to a further role in constitutive exocytosis [cardenas-2021-platelet-mast-cell-development-abstract]. Horse platelets are the only equid system in which SNAP-23 has been examined. They secrete mainly by granule–granule fusion into chains that then fuse with the surface membrane, with little actin polymerization. SNAP-23 is present and was "more activated" after stimulation than in human platelets, especially with collagen [brunso-2010-equine-platelets-abstract]. This suggests SNAP-23-dependent fusion may matter even more for platelet secretion in equids than in humans.

**Mast cell and granulocyte degranulation (innate immunity).** In mast cells SNAP-23 is needed for compound exocytosis, in which granules fuse both with the plasma membrane and with one another [guo-1998-mast-cell-compound-exocytosis-abstract]. Overexpressing human SNAP-23 enhances exocytosis, which the C-terminal VAMP-binding mutant fails to do [vaidyanathan-2001-last-exon-abstract]. Phospho-mutants at Ser95/Ser120 inhibit secretion [hepp-2005-phosphorylation-mast-cell-abstract]. Genetic work identified the kinase. After FcεRI cross-linking, IκB kinase 2 (IKK2/IKK-β) phosphorylates SNAP-23 in a way that does not depend on NF-κB. Mast-cell IKK2 is needed for IgE-mediated degranulation and anaphylaxis, and a phosphomimetic SNAP-23 partly restores degranulation in IKK2-deficient mast cells [suzuki-2008-ikk2-mast-cell-abstract]. So an IKK2→SNAP-23 phosphorylation step links immunoreceptor signalling directly to the fusion machinery in both mast cells and platelets [karim-2013-ikk-platelet-abstract]. Biochemical profiling of RBL-2H3 mast cells put SNAP23 at the centre of SNARE complex formation with syntaxin-4. VAMP8 was found on mediator-containing granules, which suggests a STX4–SNAP23–VAMP8 exocytic complex [paumet-2000-rbl-snares-abstract]. In mice, deleting SNAP23 in connective-tissue mast cells blocks their development entirely, and that model showed connective-tissue mast cells are needed for anaphylaxis [cardenas-2021-platelet-mast-cell-development-abstract]. In human neutrophils, SNAP-23 mediates exocytosis of specific granules with syntaxin-6 [martinmartin-2000-neutrophil-abstract]. More recent inhibition studies with syntaxin-4 also implicate it in azurophilic- and specific-granule release and in ROS production, but not in release of mitochondrial DNA during NET formation [gigon-2023-neutrophil-degranulation-abstract].

**Insulin-regulated GLUT4 trafficking (metabolism).** In 3T3-L1 adipocytes, syndet/SNAP-23 and syntaxin-4 are the plasma-membrane t-SNAREs for VAMP2 on GLUT4 storage vesicles. Anti-syndet antibodies or a C-terminal peptide reduce insulin-stimulated GLUT4 translocation by about 40% without affecting GLUT1 [rea-1998-syndet-glut4-abstract]. A dominant-negative SNAP23 that lacks VAMP2 binding selectively blocks GLUT4 translocation [kawanishi-2000-glut4-3t3l1-abstract]. A separate line of work links SNAP23 to lipid storage. SNAP23 knockdown reduces lipid-droplet fusion and size, and raising SNAP23 levels restored insulin sensitivity in oleate-loaded cardiomyocytes. This led to the proposal that SNAP23 connects fatty-acid influx to insulin resistance [bostrom-2007-lipid-droplet-fusion-abstract]. A follow-up study by the same group, implicating SNAP23 and Munc18c in insulin resistance in human skeletal muscle, was retracted [bostrom-2010-retraction-notice-fulltext], so the link to insulin resistance remains unproven. The GLUT4 role rests on the independent adipocyte studies above. Those studies also show that SNAP-23 assembly with syntaxin-4 is restrained by the SM protein Munc18c: in COS cells, Munc18c reduced the amount of SNAP-23 bound to syntaxin-4 in a dose-dependent way. The mouse adipocyte SNAP-23 used in that work was 87% identical to human and sat mainly at the plasma membrane [araki-1997-munc18c-abstract].

**Endosome-to-plasma membrane recycling and TLR4 signalling.** In IFN-γ-activated macrophages, LPS causes TLR4 to be endocytosed, after which it is replenished at the surface. That replenishment needs syntaxin-11 and SNAP-23. A FRET sensor reporting SNAP-23 conformation showed an STX11-dependent change after LPS, consistent with SNARE assembly [kinoshita-2019-tlr4-stx11-abstract]. This places SNAP-23 in a pathway that sustains TLR4 at the cell surface and so supports microbial recognition. SNAP-23 also forms complexes with syntaxin-11 in B lymphocytes and HeLa cells [valdez-1999-stx11-late-endosome-abstract]. In NK cells, syntaxin-11 binds SNAP23, and mutant syntaxin-11 proteins from familial hemophagocytic lymphohistiocytosis type 4 that lack all or part of the SNARE domain bind it less well. This points to a SNAP23–STX11 pairing in cytotoxic secretory-lysosome exocytosis [hellewell-2014-stx11-sacylation-abstract]. The same IKK2 phosphorylation logic works in antigen presentation. In dendritic cells, TLR/MyD88 signals drive IKK2 to phosphorylate SNAP23 on phagosomes. Phospho-SNAP23 stabilizes SNARE complexes that fuse the VAMP3/VAMP8-marked endosomal recycling compartment with the phagosome, delivering MHC class I for cross-presentation to CD8 T cells [nairgupta-2014-dc-cross-presentation-abstract].

**Lysosomal exocytosis and other regulated secretion.** Many cell types carry out Ca²⁺-triggered exocytosis of conventional lysosomes, which helps repair plasma-membrane wounds. This process uses a SNARE complex of SNAP-23, syntaxin-4 and the lysosomal R-SNARE TI-VAMP/VAMP7. The lysosomal Ca²⁺ sensor synaptotagmin VII binds SNAP-23 through its C2A domain in a Ca²⁺-dependent manner that syntaxin-4 facilitates, and cleaving SNAP-23 with botulinum neurotoxin E inhibits lysosomal exocytosis [rao-2004-lysosomal-exocytosis-abstract]. In human sperm, antibody-inhibition studies showed that the Ca²⁺- and Rab3A-triggered acrosome reaction needs SNAP-23 together with SNAP-25, several syntaxins and VAMP2 [tomes-2002-sperm-acrosome-abstract]. That suggests a role in fertilization, although the evidence is pharmacological rather than genetic.

**Neuronal postsynaptic plasticity.** SNAP-25 dominates presynaptic release, but SNAP-23 has a postsynaptic role. Deleting SNAP-23 in pyramidal neurons leaves basal transmission and AMPA/NMDA currents unchanged, yet it greatly reduces theta-burst-induced LTP and impairs spatial memory [huang-2023-neuronal-snap23-abstract]. The IEA/TreeGrafter GO terms on the donkey entry for "synaptic vesicle priming" and "synaptic vesicle fusion to presynaptic active zone membrane" [uniprot-A0A8C4M285-entry] are probably carried over from SNAP-25 family members, and the experimental literature on SNAP-23 itself does not support them.

**Cell survival and development.** Germline *Snap23*-null mouse embryos die as blastocysts before implantation, around E3.5 [suh-2011-knockout-lethality-abstract; suh-2011-knockout-lethality-fulltext]. Conditional deletion blocks B- and T-lymphocyte development, and acute loss in fibroblasts causes rapid apoptosis [kaul-2015-cell-survival-abstract]. These phenotypes are much broader than a defect in regulated secretion. They point to an essential housekeeping role in constitutive delivery of membrane and cargo to the cell surface, which matches the conclusions drawn from the platelet and mast-cell knockouts [cardenas-2021-platelet-mast-cell-development-abstract].

## 6. Implications for the truncated donkey product A0A8C4M285

The domain map in Section 2 and the structure–function data in Section 3 allow a fairly specific prediction for this 97-residue product. It keeps an intact N-terminal 18-residue region, which is needed for binding syntaxin and VAMP [vaidyanathan-2001-last-exon-abstract]. It keeps the Qb coiled coil with Gln-48 at the 0-layer, so it can probably join coiled-coil assemblies, including the SNAP-23N homotetramer seen in crystals [freedman-2003-homotetramer-abstract]. It keeps the full palmitoylation cluster, so it should be anchored to membranes [agarwal-2019-cysteine-rich-domain-abstract; vogel-1999-palmitoylation-abstract]. It lacks the linker phosphorylation sites Ser95 and Ser120 [hepp-2005-phosphorylation-mast-cell-abstract; karim-2013-ikk-platelet-abstract]. Most importantly, it lacks the whole Qc SNARE motif and the C-terminus encoded by the last exon. In full-length SNAP-23 that region is needed for VAMP binding and for SNAP-23 to bridge syntaxin and VAMP [vaidyanathan-2001-last-exon-abstract; kawanishi-2000-glut4-3t3l1-abstract]. Even the much smaller C-terminal truncation SNAP23(1–202) acts as a dominant negative in exocytosis [kawanishi-2000-glut4-3t3l1-abstract].

If A0A8C4M285 is translated at all, it would most likely act as a membrane-anchored Qb-only fragment. Such a fragment could join partial t-SNARE assemblies but could not drive fusion without a separate Qc donor. In principle it could therefore regulate SNAP-23-dependent exocytosis by competing with the full-length protein, but this has not been tested in any system. For functional annotation, the reasonable course is to transfer the family-level terms (SNARE complex, plasma membrane, lipid anchor, SNAP receptor activity / SNARE binding) with the caveat that this isoform is incomplete. Process terms such as "exocytosis" or "vesicle fusion with plasma membrane" are better attached to the canonical-length donkey SNAP23 product (A0A8C4M333) than to this fragment.

## 7. Evidence quality and gaps

Nearly all the evidence summarized here comes from human cells and rodent models. The strongest sources are the precise biochemistry (deletion mapping, structural studies, site-directed mutagenesis of the palmitoylation and phosphorylation sites) [vaidyanathan-2001-last-exon-abstract; freedman-2003-homotetramer-abstract; agarwal-2019-cysteine-rich-domain-abstract; hepp-2005-phosphorylation-mast-cell-abstract] and the conditional mouse genetics [williams-2018-platelet-snap23-deletion-abstract; cardenas-2021-platelet-mast-cell-development-abstract; kaul-2015-cell-survival-abstract; suh-2011-knockout-lethality-abstract]. Several older functional studies used antibody or peptide inhibition in permeabilized cells, which is less specific [chen-2000-platelet-dense-granule-abstract; rea-1998-syndet-glut4-abstract; martinmartin-2000-neutrophil-abstract; tomes-2002-sperm-acrosome-abstract]. The work linking SNAP23 to lipid droplets and insulin resistance needs particular caution. One paper from that line was retracted, and its first author was found to have committed scientific misconduct [bostrom-2010-retraction-notice-fulltext]. Claims resting only on the 2007 lipid-droplet study [bostrom-2007-lipid-droplet-fusion-abstract] should therefore not be used for annotation without independent support. The single equid study is comparative and descriptive, relying on western blots and electron microscopy [brunso-2010-equine-platelets-abstract]. Transfer to the donkey is supported by very high sequence conservation, about 90% identity for the canonical-length product, and by conservation of every functionally mapped residue present in A0A8C4M285. The donkey-specific annotations in UniProt are all electronic (ARBA, TreeGrafter, InterPro) [uniprot-A0A8C4M285-entry].

## Open Questions

The first open question is whether A0A8C4M285 is real. The 97-residue model needs support from donkey RNA-seq or long-read transcript data showing the splice junction after codon 89 and the FNIRSRAQ-stop extension, and from proteomics showing the protein exists. Whether the alternative terminal exon that produces it [ensembl-ENSEASG00005013173-gene] has canonical splice sites and is conserved in other perissodactyls is also open, as is whether it is conserved in horse (*Equus caballus*), where a 52-residue SNAP23 fragment (A0A5F5PYQ4) is also annotated. The horse UniProt listing was checked during this research but not archived as a citation. A second question is whether the Qb-only fragment, if expressed, is palmitoylated, binds syntaxin-4 or syntaxin-11, and inhibits SNAP-23-dependent exocytosis in a dominant-negative manner, as the C-terminal truncations studied in adipocytes and mast cells do [kawanishi-2000-glut4-3t3l1-abstract; vaidyanathan-2001-last-exon-abstract]. A third concerns equid platelets, whose secretion appears to rely more on fusion than human platelets do [brunso-2010-equine-platelets-abstract]. It would be worth measuring the SNAP-23 isoforms, Ser95 phosphorylation by IKK-β, and partner syntaxins and VAMPs in horse and donkey platelets [karim-2013-ikk-platelet-abstract; suzuki-2008-ikk2-mast-cell-abstract], given the clinical interest in equine hemostasis and thrombosis. A fourth is how much the donkey isoforms (222, 211, 209, 158 and 97 aa) correspond to the human SNAP-23a–e splice variants and whether they share their distinct subcellular distributions [shukla-2001-snap23-splice-variants-abstract]. It also remains to be shown independently whether SNAP23 really acts at lipid droplets, given the retraction of related work [bostrom-2010-retraction-notice-fulltext]. Finally, the electronic GO annotations to presynaptic vesicle priming and fusion should be re-evaluated. The only direct neuronal data for SNAP-23 support a postsynaptic role in plasticity rather than a presynaptic one [huang-2023-neuronal-snap23-abstract].

## References

In-text citations add a suffix to each key (`-abstract`, `-fulltext`, `-entry`, `-gene`, `-cds`) that names the file in `citations/` the claim was taken from. Each paper also has a `-summary.md` written by the research agent.

* **[agarwal-2019-cysteine-rich-domain]** Agarwal V, Naskar P, Agasti S, et al. (2019). The cysteine-rich domain of synaptosomal-associated protein of 23 kDa (SNAP-23) regulates its membrane association and regulated exocytosis from mast cells. *Biochim Biophys Acta Mol Cell Res* 1866(10):1618-1633. PMID: 31260699; PMCID: PMC8258691; DOI: [10.1016/j.bbamcr.2019.06.015](https://doi.org/10.1016/j.bbamcr.2019.06.015); https://pubmed.ncbi.nlm.nih.gov/31260699/
* **[araki-1997-munc18c]** Araki S, Tamori Y, Kawanishi M, et al. (1997). Inhibition of the binding of SNAP-23 to syntaxin 4 by Munc18c. *Biochem Biophys Res Commun* 234(1):257-62. PMID: 9168999; DOI: [10.1006/bbrc.1997.6560](https://doi.org/10.1006/bbrc.1997.6560); https://pubmed.ncbi.nlm.nih.gov/9168999/
* **[bostrom-2007-lipid-droplet-fusion]** Boström P, Andersson L, Rutberg M, et al. (2007). SNARE proteins mediate fusion between cytosolic lipid droplets and are implicated in insulin sensitivity. *Nat Cell Biol* 9(11):1286-93. PMID: 17922004; DOI: [10.1038/ncb1648](https://doi.org/10.1038/ncb1648); https://pubmed.ncbi.nlm.nih.gov/17922004/
* **[bostrom-2010-retraction-notice]** Boström P, Andersson L, Vind B, et al. (2017). Statement of Retraction. The SNARE Protein SNAP23 and the SNARE-Interacting Protein Munc18c in Human Skeletal Muscle Are Implicated in Insulin Resistance/Type 2 Diabetes. Diabetes 2010;59:1870-1878. DOI: 10.2337/db09-1503. PMID: 20460426. *Diabetes* 66(5):1426. PMID: 28232494; PMCID: PMC5399612; DOI: [10.2337/db17-rt05a](https://doi.org/10.2337/db17-rt05a); https://pubmed.ncbi.nlm.nih.gov/28232494/
* **[brunso-2010-equine-platelets]** Brunso L, Segura D, Monreal L, et al. (2010). The secretory mechanisms in equine platelets are independent of cytoskeletal polymerization and occur through membrane fusion. *Platelets* 21(8):658-66. PMID: 20958115; DOI: [10.3109/09537101003716200](https://doi.org/10.3109/09537101003716200); https://pubmed.ncbi.nlm.nih.gov/20958115/
* **[cardenas-2021-platelet-mast-cell-development]** Cardenas RA, Gonzalez R, Sanchez E, et al. (2021). SNAP23 is essential for platelet and mast cell development and required in connective tissue mast cells for anaphylaxis. *J Biol Chem* 296:100268. PMID: 33837726; PMCID: PMC7948755; DOI: [10.1016/j.jbc.2021.100268](https://doi.org/10.1016/j.jbc.2021.100268); https://pubmed.ncbi.nlm.nih.gov/33837726/
* **[chen-2000-platelet-dense-granule]** Chen D, Bernstein AM, Lemons PP, et al. (2000). Molecular mechanisms of platelet exocytosis: role of SNAP-23 and syntaxin 2 in dense core granule release. *Blood* 95(3):921-9. PMID: 10648404; DOI: [10.1182/blood.v95.3.921.003k17_921_929](https://doi.org/10.1182/blood.v95.3.921.003k17_921_929); https://pubmed.ncbi.nlm.nih.gov/10648404/
* **[freedman-2003-homotetramer]** Freedman SJ, Song HK, Xu Y, et al. (2003). Homotetrameric structure of the SNAP-23 N-terminal coiled-coil domain. *J Biol Chem* 278(15):13462-7. PMID: 12556468; DOI: [10.1074/jbc.m210483200](https://doi.org/10.1074/jbc.m210483200); https://pubmed.ncbi.nlm.nih.gov/12556468/
* **[gigon-2023-neutrophil-degranulation]** Gigon L, Fettrelet T, Miholic M, et al. (2023). Syntaxin-4 and SNAP23 are involved in neutrophil degranulation, but not in the release of mitochondrial DNA during NET formation. *Front Immunol* 14:1272699. PMID: 37885878; PMCID: PMC10599146; DOI: [10.3389/fimmu.2023.1272699](https://doi.org/10.3389/fimmu.2023.1272699); https://pubmed.ncbi.nlm.nih.gov/37885878/
* **[guo-1998-mast-cell-compound-exocytosis]** Guo Z, Turner C, Castle D (1998). Relocation of the t-SNARE SNAP-23 from lamellipodia-like cell surface projections regulates compound exocytosis in mast cells. *Cell* 94(4):537-48. PMID: 9727496; DOI: [10.1016/s0092-8674(00)81594-9](https://doi.org/10.1016/s0092-8674(00)81594-9); https://pubmed.ncbi.nlm.nih.gov/9727496/
* **[hellewell-2014-stx11-sacylation]** Hellewell AL, Foresti O, Gover N, et al. (2014). Analysis of familial hemophagocytic lymphohistiocytosis type 4 (FHL-4) mutant proteins reveals that S-acylation is required for the function of syntaxin 11 in natural killer cells. *PLoS One* 9(6):e98900. PMID: 24910990; PMCID: PMC4049605; DOI: [10.1371/journal.pone.0098900](https://doi.org/10.1371/journal.pone.0098900); https://pubmed.ncbi.nlm.nih.gov/24910990/
* **[hepp-2005-phosphorylation-mast-cell]** Hepp R, Puri N, Hohenstein AC, et al. (2005). Phosphorylation of SNAP-23 regulates exocytosis from mast cells. *J Biol Chem* 280(8):6610-20. PMID: 15611044; DOI: [10.1074/jbc.m412126200](https://doi.org/10.1074/jbc.m412126200); https://pubmed.ncbi.nlm.nih.gov/15611044/
* **[huang-2023-neuronal-snap23]** Huang M, Bin NR, Rai J, et al. (2023). Neuronal SNAP-23 is critical for synaptic plasticity and spatial memory independently of NMDA receptor regulation. *iScience* 26(5):106664. PMID: 37168570; PMCID: PMC10165271; DOI: [10.1016/j.isci.2023.106664](https://doi.org/10.1016/j.isci.2023.106664); https://pubmed.ncbi.nlm.nih.gov/37168570/
* **[kadkova-2019-snap25-family-review]** Kádková A, Radecke J, Sørensen JB (2019). The SNAP-25 Protein Family. *Neuroscience* 420:50-71. PMID: 30267828; DOI: [10.1016/j.neuroscience.2018.09.020](https://doi.org/10.1016/j.neuroscience.2018.09.020); https://pubmed.ncbi.nlm.nih.gov/30267828/
* **[karim-2013-ikk-platelet]** Karim ZA, Zhang J, Banerjee M, et al. (2013). IκB kinase phosphorylation of SNAP-23 controls platelet secretion. *Blood* 121(22):4567-74. PMID: 23613522; PMCID: PMC3668489; DOI: [10.1182/blood-2012-11-470468](https://doi.org/10.1182/blood-2012-11-470468); https://pubmed.ncbi.nlm.nih.gov/23613522/
* **[kaul-2015-cell-survival]** Kaul S, Mittal SK, Feigenbaum L, et al. (2015). Expression of the SNARE protein SNAP-23 is essential for cell survival. *PLoS One* 10(2):e0118311. PMID: 25706117; PMCID: PMC4338070; DOI: [10.1371/journal.pone.0118311](https://doi.org/10.1371/journal.pone.0118311); https://pubmed.ncbi.nlm.nih.gov/25706117/
* **[kawanishi-2000-glut4-3t3l1]** Kawanishi M, Tamori Y, Okazawa H, et al. (2000). Role of SNAP23 in insulin-induced translocation of GLUT4 in 3T3-L1 adipocytes. Mediation of complex formation between syntaxin4 and VAMP2. *J Biol Chem* 275(11):8240-7. PMID: 10713150; DOI: [10.1074/jbc.275.11.8240](https://doi.org/10.1074/jbc.275.11.8240); https://pubmed.ncbi.nlm.nih.gov/10713150/
* **[kinoshita-2019-tlr4-stx11]** Kinoshita D, Sakurai C, Morita M, et al. (2019). Syntaxin 11 regulates the stimulus-dependent transport of Toll-like receptor 4 to the plasma membrane by cooperating with SNAP-23 in macrophages. *Mol Biol Cell* 30(9):1085-1097. PMID: 30811271; PMCID: PMC6724512; DOI: [10.1091/mbc.e18-10-0653](https://doi.org/10.1091/mbc.e18-10-0653); https://pubmed.ncbi.nlm.nih.gov/30811271/
* **[low-1998-polarized-epithelia]** Low SH, Roche PA, Anderson HA, et al. (1998). Targeting of SNAP-23 and SNAP-25 in polarized epithelial cells. *J Biol Chem* 273(6):3422-30. PMID: 9452464; DOI: [10.1074/jbc.273.6.3422](https://doi.org/10.1074/jbc.273.6.3422); https://pubmed.ncbi.nlm.nih.gov/9452464/
* **[martinmartin-2000-neutrophil]** Martín-Martín B, Nabokina SM, Blasi J, et al. (2000). Involvement of SNAP-23 and syntaxin 6 in human neutrophil exocytosis. *Blood* 96(7):2574-83. PMID: 11001914; DOI: [10.1182/blood.v96.7.2574](https://doi.org/10.1182/blood.v96.7.2574); https://pubmed.ncbi.nlm.nih.gov/11001914/
* **[mollinedo-1997-snap23-isoforms]** Mollinedo F, Lazo PA (1997). Identification of two isoforms of the vesicle-membrane fusion protein SNAP-23 in human neutrophils and HL-60 cells. *Biochem Biophys Res Commun* 231(3):808-12. PMID: 9070898; DOI: [10.1006/bbrc.1997.6196](https://doi.org/10.1006/bbrc.1997.6196); https://pubmed.ncbi.nlm.nih.gov/9070898/
* **[nairgupta-2014-dc-cross-presentation]** Nair-Gupta P, Baccarini A, Tung N, et al. (2014). TLR signals induce phagosomal MHC-I delivery from the endosomal recycling compartment to allow cross-presentation. *Cell* 158(3):506-21. PMID: 25083866; PMCID: PMC4212008; DOI: [10.1016/j.cell.2014.04.054](https://doi.org/10.1016/j.cell.2014.04.054); https://pubmed.ncbi.nlm.nih.gov/25083866/
* **[paumet-2000-rbl-snares]** Paumet F, Le Mao J, Martin S, et al. (2000). Soluble NSF attachment protein receptors (SNAREs) in RBL-2H3 mast cells: functional role of syntaxin 4 in exocytosis and identification of a vesicle-associated membrane protein 8-containing secretory compartment. *J Immunol* 164(11):5850-7. PMID: 10820264; DOI: [10.4049/jimmunol.164.11.5850](https://doi.org/10.4049/jimmunol.164.11.5850); https://pubmed.ncbi.nlm.nih.gov/10820264/
* **[rao-2004-lysosomal-exocytosis]** Rao SK, Huynh C, Proux-Gillardeaux V, et al. (2004). Identification of SNAREs involved in synaptotagmin VII-regulated lysosomal exocytosis. *J Biol Chem* 279(19):20471-9. PMID: 14993220; DOI: [10.1074/jbc.m400798200](https://doi.org/10.1074/jbc.m400798200); https://pubmed.ncbi.nlm.nih.gov/14993220/
* **[ravichandran-1996-snap23-discovery]** Ravichandran V, Chawla A, Roche PA (1996). Identification of a novel syntaxin- and synaptobrevin/VAMP-binding protein, SNAP-23, expressed in non-neuronal tissues. *J Biol Chem* 271(23):13300-3. PMID: 8663154; DOI: [10.1074/jbc.271.23.13300](https://doi.org/10.1074/jbc.271.23.13300); https://pubmed.ncbi.nlm.nih.gov/8663154/
* **[rea-1998-syndet-glut4]** Rea S, Martin LB, McIntosh S, et al. (1998). Syndet, an adipocyte target SNARE involved in the insulin-induced translocation of GLUT4 to the cell surface. *J Biol Chem* 273(30):18784-92. PMID: 9668052; DOI: [10.1074/jbc.273.30.18784](https://doi.org/10.1074/jbc.273.30.18784); https://pubmed.ncbi.nlm.nih.gov/9668052/
* **[salaun-2005-lipid-rafts]** Salaün C, Gould GW, Chamberlain LH (2005). The SNARE proteins SNAP-25 and SNAP-23 display different affinities for lipid rafts in PC12 cells. Regulation by distinct cysteine-rich domains. *J Biol Chem* 280(2):1236-40. PMID: 15542596; PMCID: PMC2387193; DOI: [10.1074/jbc.m410674200](https://doi.org/10.1074/jbc.m410674200); https://pubmed.ncbi.nlm.nih.gov/15542596/
* **[shukla-2001-snap23-splice-variants]** Shukla A, Corydon TJ, Nielsen S, et al. (2001). Identification of three new splice variants of the SNARE protein SNAP-23. *Biochem Biophys Res Commun* 285(2):320-7. PMID: 11444845; DOI: [10.1006/bbrc.2001.5144](https://doi.org/10.1006/bbrc.2001.5144); https://pubmed.ncbi.nlm.nih.gov/11444845/
* **[suh-2011-knockout-lethality]** Suh YH, Yoshimoto-Furusawa A, Weih KA, et al. (2011). Deletion of SNAP-23 results in pre-implantation embryonic lethality in mice. *PLoS One* 6(3):e18444. PMID: 21479242; PMCID: PMC3066230; DOI: [10.1371/journal.pone.0018444](https://doi.org/10.1371/journal.pone.0018444); https://pubmed.ncbi.nlm.nih.gov/21479242/
* **[sutton-1998-snare-structure]** Sutton RB, Fasshauer D, Jahn R, et al. (1998). Crystal structure of a SNARE complex involved in synaptic exocytosis at 2.4 A resolution. *Nature* 395(6700):347-53. PMID: 9759724; DOI: [10.1038/26412](https://doi.org/10.1038/26412); https://pubmed.ncbi.nlm.nih.gov/9759724/
* **[suzuki-2008-ikk2-mast-cell]** Suzuki K, Verma IM (2008). Phosphorylation of SNAP-23 by IkappaB kinase 2 regulates mast cell degranulation. *Cell* 134(3):485-95. PMID: 18692471; PMCID: PMC2586340; DOI: [10.1016/j.cell.2008.05.050](https://doi.org/10.1016/j.cell.2008.05.050); https://pubmed.ncbi.nlm.nih.gov/18692471/
* **[tomes-2002-sperm-acrosome]** Tomes CN, Michaut M, De Blas G, et al. (2002). SNARE complex assembly is required for human sperm acrosome reaction. *Dev Biol* 243(2):326-38. PMID: 11884041; DOI: [10.1006/dbio.2002.0567](https://doi.org/10.1006/dbio.2002.0567); https://pubmed.ncbi.nlm.nih.gov/11884041/
* **[vaidyanathan-2001-last-exon]** Vaidyanathan VV, Puri N, Roche PA (2001). The last exon of SNAP-23 regulates granule exocytosis from mast cells. *J Biol Chem* 276(27):25101-6. PMID: 11350976; DOI: [10.1074/jbc.m103536200](https://doi.org/10.1074/jbc.m103536200); https://pubmed.ncbi.nlm.nih.gov/11350976/
* **[valdez-1999-stx11-late-endosome]** Valdez AC, Cabaniols JP, Brown MJ, et al. (1999). Syntaxin 11 is associated with SNAP-23 on late endosomes and the trans-Golgi network. *J Cell Sci* 112 ( Pt 6):845-54. PMID: 10036234; DOI: [10.1242/jcs.112.6.845](https://doi.org/10.1242/jcs.112.6.845); https://pubmed.ncbi.nlm.nih.gov/10036234/
* **[vogel-1999-palmitoylation]** Vogel K, Roche PA (1999). SNAP-23 and SNAP-25 are palmitoylated in vivo. *Biochem Biophys Res Commun* 258(2):407-10. PMID: 10329400; DOI: [10.1006/bbrc.1999.0652](https://doi.org/10.1006/bbrc.1999.0652); https://pubmed.ncbi.nlm.nih.gov/10329400/
* **[wang-1997-syndet]** Wang G, Witkin JW, Hao G, et al. (1997). Syndet is a novel SNAP-25 related protein expressed in many tissues. *J Cell Sci* 110 ( Pt 4):505-13. PMID: 9067602; DOI: [10.1242/jcs.110.4.505](https://doi.org/10.1242/jcs.110.4.505); https://pubmed.ncbi.nlm.nih.gov/9067602/
* **[wang-2020-donkey-genome]** Wang C, Li H, Guo Y, et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun* 11(1):6014. PMID: 33293529; PMCID: PMC7723042; DOI: [10.1038/s41467-020-19813-7](https://doi.org/10.1038/s41467-020-19813-7); https://pubmed.ncbi.nlm.nih.gov/33293529/
* **[williams-2018-platelet-snap23-deletion]** Williams CM, Li Y, Brown E, et al. (2018). Platelet-specific deletion of SNAP23 ablates granule secretion, substantially inhibiting arterial and venous thrombosis in mice. *Blood Adv* 2(24):3627-3636. PMID: 30573565; PMCID: PMC6306884; DOI: [10.1182/bloodadvances.2018023291](https://doi.org/10.1182/bloodadvances.2018023291); https://pubmed.ncbi.nlm.nih.gov/30573565/
* **[ensembl-ENSEASG00005013173-gene]** Ensembl. Gene ENSEASG00005013173 (SNAP23, *Equus asinus*), lookup with transcripts and exons via the Ensembl REST API. https://rest.ensembl.org/lookup/id/ENSEASG00005013173?expand=1
* **[ensembl-ENSEAST00005020804-cds]** Ensembl. CDS sequence of transcript ENSEAST00005020804 (encodes ENSEASP00005019168 = A0A8C4M285). https://rest.ensembl.org/sequence/id/ENSEAST00005020804?type=cds
* **[uniprot-A0A8C4M285-entry]** UniProt Consortium. UniProtKB/TrEMBL entry A0A8C4M285_EQUAS, Synaptosome associated protein 23 (*Equus asinus*), entry version 21 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A8C4M285.txt
* **[uniprot-O00161-entry]** UniProt Consortium. UniProtKB/Swiss-Prot entry O00161 (SNP23_HUMAN), Synaptosomal-associated protein 23 (*Homo sapiens*). https://rest.uniprot.org/uniprotkb/O00161.txt
* **[uniprot-donkey-snap23-isoforms-sequences]** UniProt Consortium. FASTA sequences of all UniProtKB entries with gene SNAP23 in *Equus asinus* (taxon 9793): A0A8C4M5X5, A0A8C4M285, A0A8C4M333, A0A9L0J3X0, A0A9L0K6I4. https://rest.uniprot.org/uniprotkb/stream?query=gene:SNAP23+AND+organism_id:9793&format=fasta


## Citations

1. agarwal-2019-cysteine-rich-domain-abstract.md
2. agarwal-2019-cysteine-rich-domain-summary.md
3. araki-1997-munc18c-abstract.md
4. araki-1997-munc18c-summary.md
5. bostrom-2007-lipid-droplet-fusion-abstract.md
6. bostrom-2007-lipid-droplet-fusion-summary.md
7. bostrom-2010-retraction-notice-abstract.md
8. bostrom-2010-retraction-notice-fulltext.txt
9. bostrom-2010-retraction-notice-summary.md
10. brunso-2010-equine-platelets-abstract.md
11. brunso-2010-equine-platelets-summary.md
12. cardenas-2021-platelet-mast-cell-development-abstract.md
13. cardenas-2021-platelet-mast-cell-development-fulltext.txt
14. cardenas-2021-platelet-mast-cell-development-summary.md
15. chen-2000-platelet-dense-granule-abstract.md
16. chen-2000-platelet-dense-granule-summary.md
17. ensembl-ENSEASG00005013173-gene-summary.md
18. ensembl-ENSEASG00005013173-gene.json
19. ensembl-ENSEAST00005020804-cds.txt
20. freedman-2003-homotetramer-abstract.md
21. freedman-2003-homotetramer-summary.md
22. gigon-2023-neutrophil-degranulation-abstract.md
23. gigon-2023-neutrophil-degranulation-fulltext.txt
24. gigon-2023-neutrophil-degranulation-summary.md
25. guo-1998-mast-cell-compound-exocytosis-abstract.md
26. guo-1998-mast-cell-compound-exocytosis-summary.md
27. hellewell-2014-stx11-sacylation-abstract.md
28. hellewell-2014-stx11-sacylation-fulltext.txt
29. hellewell-2014-stx11-sacylation-summary.md
30. hepp-2005-phosphorylation-mast-cell-abstract.md
31. hepp-2005-phosphorylation-mast-cell-summary.md
32. huang-2023-neuronal-snap23-abstract.md
33. huang-2023-neuronal-snap23-fulltext.txt
34. huang-2023-neuronal-snap23-summary.md
35. kadkova-2019-snap25-family-review-abstract.md
36. kadkova-2019-snap25-family-review-summary.md
37. karim-2013-ikk-platelet-abstract.md
38. karim-2013-ikk-platelet-summary.md
39. kaul-2015-cell-survival-abstract.md
40. kaul-2015-cell-survival-fulltext.txt
41. kaul-2015-cell-survival-summary.md
42. kawanishi-2000-glut4-3t3l1-abstract.md
43. kawanishi-2000-glut4-3t3l1-summary.md
44. kinoshita-2019-tlr4-stx11-abstract.md
45. kinoshita-2019-tlr4-stx11-fulltext.txt
46. kinoshita-2019-tlr4-stx11-summary.md
47. low-1998-polarized-epithelia-abstract.md
48. low-1998-polarized-epithelia-summary.md
49. martinmartin-2000-neutrophil-abstract.md
50. martinmartin-2000-neutrophil-summary.md
51. mollinedo-1997-snap23-isoforms-abstract.md
52. mollinedo-1997-snap23-isoforms-summary.md
53. nairgupta-2014-dc-cross-presentation-abstract.md
54. nairgupta-2014-dc-cross-presentation-summary.md
55. paumet-2000-rbl-snares-abstract.md
56. paumet-2000-rbl-snares-summary.md
57. rao-2004-lysosomal-exocytosis-abstract.md
58. rao-2004-lysosomal-exocytosis-summary.md
59. ravichandran-1996-snap23-discovery-abstract.md
60. ravichandran-1996-snap23-discovery-summary.md
61. rea-1998-syndet-glut4-abstract.md
62. rea-1998-syndet-glut4-summary.md
63. salaun-2005-lipid-rafts-abstract.md
64. salaun-2005-lipid-rafts-summary.md
65. shukla-2001-snap23-splice-variants-abstract.md
66. shukla-2001-snap23-splice-variants-summary.md
67. suh-2011-knockout-lethality-abstract.md
68. suh-2011-knockout-lethality-fulltext.txt
69. suh-2011-knockout-lethality-summary.md
70. sutton-1998-snare-structure-abstract.md
71. sutton-1998-snare-structure-summary.md
72. suzuki-2008-ikk2-mast-cell-abstract.md
73. suzuki-2008-ikk2-mast-cell-summary.md
74. tomes-2002-sperm-acrosome-abstract.md
75. tomes-2002-sperm-acrosome-summary.md
76. uniprot-A0A8C4M285-entry.txt
77. uniprot-O00161-entry.txt
78. uniprot-donkey-snap23-isoforms-sequences.fasta
79. vaidyanathan-2001-last-exon-abstract.md
80. vaidyanathan-2001-last-exon-summary.md
81. valdez-1999-stx11-late-endosome-abstract.md
82. valdez-1999-stx11-late-endosome-summary.md
83. vogel-1999-palmitoylation-abstract.md
84. vogel-1999-palmitoylation-summary.md
85. wang-1997-syndet-abstract.md
86. wang-1997-syndet-summary.md
87. wang-2020-donkey-genome-abstract.md
88. wang-2020-donkey-genome-fulltext.txt
89. wang-2020-donkey-genome-summary.md
90. williams-2018-platelet-snap23-deletion-abstract.md
91. williams-2018-platelet-snap23-deletion-summary.md