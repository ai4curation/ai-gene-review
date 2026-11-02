---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T22:53:10.748692'
end_time: '2026-10-25T23:04:08.861648'
duration_seconds: 658.11
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: VAPA
  gene_symbol: VAPA
  uniprot_accession: A0A3Q2H1L9
  protein_description: 'RecName: Full=Vesicle-associated membrane protein-associated
    protein A {ECO:0000256|ARBA:ARBA00018309};'
  gene_info: Name=VAPA {ECO:0000313|VGNC:VGNC:58706};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the VAMP-associated protein (VAP) (TC 9.B.17)
  protein_domains: Ig-like_fold. (IPR013783); MSP_dom. (IPR000535); PapD-like_sf.
    (IPR008962); VAP. (IPR016763); Motile_Sperm (PF00635)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3284
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 108
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A3Q2H1L9
- **Protein Description:** RecName: Full=Vesicle-associated membrane protein-associated protein A {ECO:0000256|ARBA:ARBA00018309};
- **Gene Information:** Name=VAPA {ECO:0000313|VGNC:VGNC:58706};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the VAMP-associated protein (VAP) (TC 9.B.17)
- **Key Domains:** Ig-like_fold. (IPR013783); MSP_dom. (IPR000535); PapD-like_sf. (IPR008962); VAP. (IPR016763); Motile_Sperm (PF00635)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "VAPA" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'VAPA' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **VAPA** (gene ID: VAPA, UniProt: A0A3Q2H1L9) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# VAPA (Vesicle-associated membrane protein-associated protein A) in the horse, *Equus caballus* (UniProt A0A3Q2H1L9)

## 1. Introduction and summary

VAPA is a small, tail-anchored integral membrane protein of the endoplasmic reticulum (ER). Its job is to act as a docking receptor that recruits cytosolic and organelle-bound proteins to the cytoplasmic face of the ER. It does not catalyse a reaction or transport a substrate itself. Its N-terminal major sperm protein (MSP) domain binds short peptide motifs called FFAT ("two phenylalanines in an acidic tract") and related phospho-FFAT motifs. These motifs occur in lipid-transfer proteins, signalling adaptors, ion channels and trafficking factors, so VAPA anchors one side of many ER membrane contact sites: with the Golgi, endosomes, the plasma membrane, mitochondria and lipid droplets. At these sites, lipid-transfer proteins such as OSBP, CERT, Nir2, ORP3 and STARD3 move sterols, ceramide, phosphatidylinositol and PI4P between membranes [loewen-2003-ffat-motif-abstract; kaiser-2005-msp-ffat-structure-abstract; murphy-2016-vap-review-abstract; dimattia-2020-phospho-ffat-abstract]. The protein was first described in *Aplysia* as a VAMP-binding protein needed for neurotransmitter release, which is where the name comes from [skehel-1995-aplysia-vap33-abstract]. The contact-site tethering role has since become its best-supported primary function in mammalian cells [murphy-2016-vap-review-abstract; lev-2008-vap-review-abstract].

No experimental study of horse VAPA was found. The horse entry A0A3Q2H1L9 is an unreviewed TrEMBL record from the 2009 horse genome assembly, and all of its functional and localisation statements are propagated automatically from human VAPA (Q9P0L0) [uniprot-A0A3Q2H1L9-entry; uniprot-Q9P0L0-human-VAPA-entry]. One naming trap needs flagging. In the equine veterinary literature, "VapA" almost always means the virulence-associated protein A of the bacterium *Rhodococcus equi*, which causes pneumonia in foals. That protein is plasmid-encoded, perturbs host endolysosomes [rofe-2017-rhodococcus-vapa-endolysosome-abstract] and is used as a marker of virulent strains on horse farms [petry-2017-rhodococcus-vapa-horse-farms-abstract]. It is unrelated to the host ER protein studied here, and none of that literature has been used to annotate horse VAPA.

Within the host genome the symbol is unambiguous. The horse gene (VGNC:58706, NCBI GeneID 100055344, chromosome 8) is annotated as the VAPA ortholog. Horse RefSeq isoform X2 (XP_023503236, 249 aa) is 98.4% identical to canonical human VAPA (245/249 identical residues) [refseq-XP_023503236-horse-VAPA-isoformX2; uniprot-Q9P0L0-human-VAPA-entry]. The accession under study, A0A3Q2H1L9, is the longer isoform X1 (XP_023503235, 294 aa), which carries a 45-residue insertion (GITPPGTAPAVTSVSSINNTVATPASYNMKNDPRGLTVFKQEKQK) immediately after the MSP domain [uniprot-A0A3Q2H1L9-entry]. This insertion is not an equine oddity. Human VAPA has an equivalent 294-residue isoform 2 (Q9P0L0-2), in which the corresponding residue L139 is replaced by a 46-residue segment (LGITPPGNAPTVTSMSSINNTVATPASYHTKDDPRGLSVLKQEKQK) supported by full-length cDNA evidence [uniprot-Q9P0L0-human-VAPA-entry; uniprot-Q9P0L0-2-human-VAPA-isoform2]. Horse A0A3Q2H1L9 and human isoform 2 are 282 of 294 residues identical over their full length. Most of the differences lie in the inserted segment, which is less conserved than the MSP domain and transmembrane anchor [uniprot-A0A3Q2H1L9; uniprot-Q9P0L0-2-human-VAPA-isoform2]. Homologous 294-residue VAPA isoforms with a similar insert occur in other mammals, such as macaque and dog, and in the donkey with an identical insert [uniprot-A0A5F7ZL45; uniprot-A0A8I3MVB2; uniprot-A0A8C4KTX6]. A second horse entry, A0A3Q2H6V0 (320 aa), also contains the identical insert [uniprot-A0A3Q2H6V0]. A0A3Q2H1L9 is therefore best read as the horse ortholog of human VAPA isoform 2, encoded by a conserved alternative exon. The rest of this report describes VAPA function as established in mammals (human, rat, mouse) and in conserved structural work. No study was found that separates the functions of the two splice forms, so the conclusions apply to both.

## 2. Gene identity, domain architecture and topology

The horse protein has the canonical three-part VAP architecture. An N-terminal MSP domain (residues 14–131 in A0A3Q2H1L9; InterPro IPR000535, Pfam PF00635, PapD-like/Ig-like β-sandwich fold) is followed by a linker containing a disordered region (180–212 in the long isoform) and a coiled-coil segment (217–244). The C-terminus is a single hydrophobic transmembrane helix (273–293) [uniprot-A0A3Q2H1L9-entry]. Because the transmembrane segment sits at the extreme C-terminus, VAPA is a type IV (tail-anchored) membrane protein: the MSP domain and coiled coil face the cytosol and the short C-terminal tail lies in or across the ER bilayer [uniprot-Q9P0L0-human-VAPA-entry; lev-2008-vap-review-abstract]. The family classification (VAP family, TC 9.B.17; PANTHER PTHR10809:SF155; PIRSF019693) places the horse protein firmly with vertebrate VAPA rather than its paralogs VAPB or MOSPD2 [uniprot-A0A3Q2H1L9-entry].

Mammalian VAPs were cloned as homologues of *Aplysia* VAP-33. Human VAPA ("hVAP-33") shares about 50% identity with the mollusc protein, keeps its length and domain organisation, and is broadly expressed rather than neuron-restricted [weir-1998-vap33-vamp-abstract; nishimura-1999-hvap-a-abstract]. VAPA forms homodimers and also heterodimerises with VAPB through the transmembrane domains [nishimura-1999-hvap-a-abstract]. Dimerisation needs both the N- and C-terminal regions [weir-2001-vapa-dimer-snare-abstract]. UniProt also records a disulfide-linked homodimer for human VAPA [uniprot-Q9P0L0-human-VAPA-entry]. Dimerisation matters functionally because a VAP dimer has two MSP domains, so it can engage dimeric FFAT partners avidly and help build stable tethers [murphy-2016-vap-review-abstract].

## 3. Molecular mechanism: the MSP domain as an FFAT/phospho-FFAT receptor

The main biochemical activity of VAPA is binding FFAT motifs. Loewen, Roy and Levine identified the FFAT motif (consensus EFFDAxE) as a short targeting determinant shared by otherwise unrelated lipid-binding proteins (the OSBP/ORP family, CERT, the Nir/RdgB family) and the yeast transcriptional regulator Opi1p. They showed that it binds VAP homologues directly to target these proteins to the ER [loewen-2003-ffat-motif-abstract]. Kaiser and colleagues then solved crystal structures of the rat VAP-A MSP domain alone and in complex with an FFAT peptide. They used the complex to design an FFAT-binding-defective VAP mutant, which also blocked function of the yeast homologue Scs2p and altered ER morphology when overexpressed in COS7 cells [kaiser-2005-msp-ffat-structure-abstract]. An NMR structure of the VAP-A MSP domain bound to the OSBP FFAT region showed that five of the six conserved FFAT residues are needed for a stable complex. Several of these act through electrostatic contacts with the basic MSP surface, and an acidic patch upstream of the core motif contributes to binding through intermediate encounter complexes [furuita-2010-vapa-osbp-nmr-abstract].

Later work showed that the FFAT code is flexible. A quantitative yeast reporter system showed that every one of the seven FFAT elements tolerates substitution, and that weak ER targeting via VAP persists even with two substituted elements. This identified FFAT-like motifs in proteins such as AKAP220, AKAP110 and FAPP2 [mikitova-2012-ffat-thermodynamics-abstract]. Murphy and Levine applied a scoring algorithm to the roughly 100-member human and yeast VAP interactome ("VAPome"). They estimated that about half of the VAPome binds VAP directly or indirectly through FFAT–MSP interactions, and described VAP as essentially the sole general receptor for cytoplasmic proteins on the ER surface [murphy-2016-vap-review-abstract]. Di Mattia et al. (2020) added a second class, the phospho-FFAT motif. In these motifs a key acidic residue is replaced by serine or threonine, and phosphorylation of that residue is needed for MSP binding [dimattia-2020-phospho-ffat-abstract]. Their crystal structures of the VAP-A MSP domain with conventional and phospho-FFAT peptides showed that the second phenylalanine of the motif inserts into a hydrophobic pocket formed by K52, T54, K94, M96 and K125 of VAP-A. A K94D/M96D ("KD/MD") double mutant abolishes FFAT binding and is the standard loss-of-function tool [dimattia-2020-phospho-ffat-fulltext]. All of these residues fall in the MSP region, where horse and human VAPA are identical apart from one conservative position (S72 in human, L72 in horse), so the FFAT-binding pocket is fully conserved in the horse protein [uniprot-A0A3Q2H1L9-entry; uniprot-Q9P0L0-human-VAPA-entry]. Proximity-labelling (BioID) interactomes of the human VAP family support this receptor model. VAPA, VAPB and MOSPD2 assemble into one ER-resident complex that recognises FFAT motifs, while the related MOSPD1 and MOSPD3 form a separate complex that prefers FFNT ("two phenylalanines in a neutral tract") motifs. VAPA therefore belongs to the main FFAT-reading arm of a larger family of ER tethers [cabukusta-2020-human-vapome-abstract]. Because phosphorylation can switch FFAT binding on, VAPA-dependent contacts can be controlled by kinase signalling, and Di Mattia et al. showed this directly for STARD3-mediated ER–endosome contacts [dimattia-2020-phospho-ffat-abstract].

## 4. Lipid transfer at ER–Golgi contact sites

The best-characterised physiological role of VAPA is at ER–trans-Golgi contacts, where it docks lipid-transfer proteins that also bind the Golgi through PI4P-binding PH domains. OSBP was the first such partner found by unbiased screening. A yeast two-hybrid screen with OSBP isolated VAP-A, and OSBP–VAP-A complexes affected ER export of a temperature-sensitive VSV-G reporter and of fluorescent ceramide, with reduced sphingomyelin synthesis [wyles-2002-vapa-osbp-abstract]. CERT, the START-domain protein that extracts ceramide from the ER and delivers it to the Golgi for sphingomyelin synthesis [hanada-2003-cert-abstract], has an FFAT motif that co-immunoprecipitates VAP-A and VAP-B. Mutating that motif impaired ER-to-Golgi ceramide transport at near-endogenous expression levels without affecting the transfer activity measured in vitro. VAP binding therefore restricts CERT's otherwise random transfer activity to the right place [kawano-2006-cert-vap-abstract]. Peretti et al. showed that RNAi depletion of VAP-A and VAP-B lowers Golgi PI4P, diacylglycerol and sphingomyelin and substantially inhibits Golgi-mediated transport. These effects were coordinated through the FFAT proteins Nir2, OSBP and CERT, with Nir2 acting upstream to maintain the Golgi PI4P pool [peretti-2008-vap-golgi-lipid-abstract].

Mesmin and colleagues defined the mechanism by reconstitution. OSBP bridges the ER (FFAT to VAP-A) and the Golgi (PH domain to PI4P), transfers sterol from the ER to the Golgi through its ORD domain, and carries PI4P back to the ER, where the ER phosphatase Sac1 hydrolyses it. PI4P hydrolysis provides the energy that drives sterol transport against its gradient [mesmin-2013-osbp-four-step-abstract]. VAPA is therefore the fixed ER-side anchor of a lipid counter-transport cycle. Related work showed that VAP family proteins also support in-trans PI4P turnover by Sac1 at contact sites, first in yeast through the VAP homologues Scs2/Scs22 and Osh proteins at ER–PM contacts [stefan-2011-osh-sac1-contacts-abstract], and in mammals through FAPP1 at ER–TGN contacts [venditti-2019-fapp1-sac1-vap-abstract]. UniProt records a VAPA–PLEKHA3 (FAPP1)–SACM1L ternary complex from the latter study [uniprot-Q9P0L0-human-VAPA-entry]. Through these partners VAPA indirectly controls Golgi PI4P, sphingomyelin and cholesterol, and therefore the lipid identity and export competence of the Golgi.

## 5. Contacts with endosomes, the plasma membrane, mitochondria and lipid droplets

VAPA tethers the ER to many organelles besides the Golgi. At late endosomes, the cholesterol-transfer protein STARD3 and its relative STARD3NL use FFAT motifs to bind ER VAPs and form an endosome–ER tethering complex. Endogenous contacts were detected by proximity ligation [alpy-2013-stard3-vap-abstract]. STARD3 has a phospho-FFAT, and its phosphorylation is needed both to form these contacts and for STARD3-mediated sterol transfer from the ER to endosomes [dimattia-2020-phospho-ffat-abstract]. In vitro reconstitution showed that STARD3 and its ER partner VAP together form a machine for highly efficient cholesterol transport within membrane contacts. In cells, STARD3 shifts cholesterol from the plasma membrane to endosomes, which depends on both its transfer activity and its ability to make VAP-dependent contacts [wilhelm-2017-stard3-cholesterol-abstract]. In VAPA/VAPB double-knockout HeLa cells, PI4P builds up on endosomes, WASH-dependent actin comets accumulate and retromer-mediated endosome-to-Golgi budding is impaired. These phenotypes are mimicked by OSBP depletion. VAP is recruited to retromer budding sites through the sorting nexin SNX2 [dong-2016-vap-endosome-pi4p-abstract]. The same study noted that VAPA appears in wild-type cells as a doublet of two splice variants [dong-2016-vap-endosome-pi4p-fulltext], which is relevant to the two predicted horse isoforms. On the secretory side, WDR44 binds VAPA and VAPB through an FFAT motif and aligns a subset of Rab11-positive tubular endosomes with the ER. WDR44 and GRAF2 are required for Rab8/10/11-dependent export of newly synthesised E-cadherin, MMP14 and CFTR ΔF508 [luckenardjomande-2020-wdr44-vap-abstract; luckenardjomande-2020-wdr44-vap-fulltext].

At ER–plasma membrane junctions, VAPA partners with several proteins. The phosphatidylinositol-transfer protein Nir2 associates with ER VAPs through its FFAT motif and is recruited to ER–PM junctions after receptor stimulation [chang-2013-nir2-erpm-abstract]. There it exchanges phosphatidylinositol (ER to PM) for phosphatidic acid (PM to ER), keeping cells able to sustain PLC signalling. Mutating the Nir2 FFAT motif greatly reduced this activity [kim-2015-nir2-pi-transfer-abstract; kim-2015-nir2-pi-transfer-fulltext]. ORP3 interacts with VAPA through canonical and FFAT-like motifs, and this interaction is strengthened when ORP3 is hyperphosphorylated. The ORP3–VAPA complex goes to plasma-membrane sites through the ORP3 PH domain and stimulates R-Ras signalling, Akt S473 phosphorylation and β1-integrin activity [lehto-2005-orp3-vapa-abstract; weber-boyvat-2015-orp3-rras-abstract]. This is the basis for the UniProt statement that VAPA can be recruited to the plasma membrane [uniprot-Q9P0L0-human-VAPA-entry]. In neurons, the voltage-gated potassium channels Kv2.1 and Kv2.2 bind VAPA and VAPB through a non-canonical, phosphorylation-dependent FFAT-like motif in the channel's PRC (proximal restriction and clustering) domain. This interaction forms and remodels ER–PM junctions independently of ion conduction. Knocking out VAPA reduces Kv2.1 clustering, and endogenous VAPs co-localise with Kv2 channels at ER–PM junctions in mouse brain [johnson-2018-kv2-vap-abstract; kirmiz-2018-vap-kv2-neurons-abstract; kirmiz-2018-kv2-erpm-remodeling-abstract].

VAPA also binds the bridge-like lipid-transfer protein VPS13A through an FFAT motif. VPS13A localises to ER–mitochondria contacts and lipid droplets, and losing it reduces ER–mitochondria contacts and alters mitochondrial morphology and lipid-droplet motility [yeshaw-2019-vps13a-vap-abstract]. VAPA also takes part in autophagosome biogenesis. When autophagy is induced, VAPA and VAPB are recruited to autophagosome formation sites on the ER. There they bind the FFAT motifs of FIP200 (RB1CC1) and ULK1, stabilise the ULK1/FIP200 complex and promote the WIPI2/FIP200 tether between the ER and the isolation membrane. Depleting VAPA and VAPB reduces ULK1 puncta and stalls isolation-membrane progression [zhao-2018-vap-autophagosome-abstract]. The FIP200 motif was later shown to be a phospho-FFAT [uniprot-Q9P0L0-human-VAPA-entry; dimattia-2020-phospho-ffat-abstract]. In neurons, VAPA binds the FFAT motif of protrudin. VAPA knockdown in PC12 cells mislocalises protrudin and blocks NGF-induced neurite outgrowth, a defect rescued by wild-type but not by binding-defective VAPA [saita-2009-protrudin-vap-abstract]. Taken together, these partners show VAPA as a general ER adaptor. The identity of the partner, more than any property of VAPA itself, decides which organelle is contacted and which lipid or signal is exchanged [wu-2018-er-contact-review-abstract; murphy-2016-vap-review-abstract].

## 6. ER architecture, SNARE-related trafficking and historical localisation claims

Because VAPA concentrates its partners on the ER, overexpressing it with partners reshapes the ER. Co-expressing ORP3 with VAP-A induces stacked "organised smooth ER" [lehto-2005-orp3-vapa-abstract]. Nir2–VAP-B interaction produces stacked ER arrays and Nir3–VAP-B drives gross ER remodelling with microtubule bundling. These paralog data are shown here to illustrate the shared MSP mechanism [amarilio-2005-vap-nir-er-structure-abstract]. FFAT-binding-defective VAP alters ER morphology as well [kaiser-2005-msp-ffat-structure-abstract]. These are largely overexpression phenotypes, but they support UniProt's statement that VAPA "may regulate ER morphology" together with ORP3 [uniprot-Q9P0L0-human-VAPA-entry].

The older vesicle-trafficking role comes from the original *Aplysia* work, where antibodies against VAP-33 blocked synaptic transmission [skehel-1995-aplysia-vap33-abstract], and from in vitro binding of VAPA to VAMP and a broad set of SNAREs and fusion factors (syntaxin 1A, rbet1, rsec22, α-SNAP, NSF). Weir and colleagues placed VAP-A in the ER/ERGIC of COS-7 cells and proposed a general role in ER–Golgi SNARE traffic [weir-1998-vap33-vamp-abstract; weir-2001-vapa-dimer-snare-abstract]. Lapierre et al. found VAP-33 bound to the occludin C-terminus and co-localised with it at tight junctions, with a further intracellular vesicular pool [lapierre-1999-vap33-occludin-abstract]. This study is the source of the "tight junction" and "cell membrane" locations propagated to the horse entry [uniprot-A0A3Q2H1L9-entry]. Later reviews generally read these earlier SNARE and tight-junction data as indirect or secondary to the ER contact-site function, given VAPA's tail-anchored ER topology and FFAT-dependent recruitment of most partners [lev-2008-vap-review-abstract; murphy-2016-vap-review-abstract]. For annotation, the ER membrane, and specifically ER membrane contact sites, should be taken as the primary site of action. Plasma-membrane and tight-junction locations are low-confidence or context-specific.

## 7. Host–pathogen interactions, antiviral restriction and disease relevance

Several viruses use VAPA's ER-anchoring function and the lipid environment it maintains. Hepatitis C virus non-structural proteins NS5A and NS5B bind VAPA (hVAP-33), and the interferon-induced protein viperin binds the VAPA C-terminal region and competes with NS5A, inhibiting HCV replication [wang-2012-viperin-vap-abstract; uniprot-Q9P0L0-human-VAPA-entry]. The antiviral factor IFITM3 binds VAPA and prevents its association with OSBP. Cholesterol then accumulates in late endosomes and multivesicular bodies, which blocks fusion-mediated viral entry, and changing VAPA levels changes IFITM3 restriction [aminibavil-2013-ifitm3-vapa-abstract]. These studies confirm that the VAPA–OSBP axis controls endosomal cholesterol in vivo, and they suggest that VAPA in horses could similarly affect susceptibility to enveloped viruses, though this has not been tested.

For disease, most work concerns the paralog VAPB, whose P56S mutation in the MSP domain causes familial ALS8 and late-onset spinal muscular atrophy [nishimura-2004-vapb-als-abstract]. Mutant VAPB aggregates in ER-derived tubular clusters, loses FFAT binding, and traps wild-type VAPA and VAPB. VAP knockdown in primary neurons causes Golgi dispersion and cell death, and VAPA and VAPB levels are reduced in sporadic ALS patients and SOD1 transgenic mice [teuling-2007-vapb-mutant-aggregates-abstract]. The equivalent proline is conserved in VAPA, and the P56S mutation destabilises the VAP-A MSP domain in vitro [furuita-2010-vapa-osbp-nmr-abstract]. Reviews conclude that VAP-related neurodegeneration most likely reflects reduced total VAP function at contact sites rather than the loss of any single interaction [murphy-2016-vap-review-abstract; lev-2008-vap-review-abstract]. No VAPA-associated disease has been reported in horses.

## 8. Synthesis for functional annotation of horse VAPA

Combining the orthology evidence with the mammalian experimental literature gives a consistent annotation for horse VAPA (A0A3Q2H1L9). Its molecular function is a protein-binding adaptor or receptor activity. Specifically, its MSP domain binds FFAT and phospho-FFAT motifs, and VAPA forms homo- and heterodimers with VAPB. It has no enzymatic or transporter activity of its own [loewen-2003-ffat-motif-abstract; kaiser-2005-msp-ffat-structure-abstract; dimattia-2020-phospho-ffat-abstract; nishimura-1999-hvap-a-abstract]. It acts at the cytosolic face of the ER membrane, as a tail-anchored protein concentrated at ER–Golgi, ER–endosome, ER–plasma membrane and ER–mitochondria contact sites [uniprot-Q9P0L0-human-VAPA-entry; murphy-2016-vap-review-abstract]. The biological processes it serves are membrane contact site tethering and the non-vesicular lipid transport these contacts support. This includes sterol/PI4P exchange by OSBP, ceramide transport by CERT for sphingomyelin synthesis, PI/PA exchange by Nir2 that sustains phosphoinositide signalling, ER-to-endosome cholesterol transfer by STARD3, and ER–isolation membrane contacts during autophagosome biogenesis [zhao-2018-vap-autophagosome-abstract; wilhelm-2017-stard3-cholesterol-abstract; mesmin-2013-osbp-four-step-abstract; kawano-2006-cert-vap-abstract; kim-2015-nir2-pi-transfer-abstract; alpy-2013-stard3-vap-abstract; dimattia-2020-phospho-ffat-abstract]. Through these partners it also controls PI4P homeostasis on Golgi and endosomes, retromer/WASH-dependent endosomal budding, Golgi export, ER morphology and neuronal ER–PM junction organisation [peretti-2008-vap-golgi-lipid-abstract; dong-2016-vap-endosome-pi4p-abstract; kirmiz-2018-vap-kv2-neurons-abstract]. A direct role in SNARE-mediated vesicle fusion and a stable tight-junction location are historical, weakly supported claims [weir-2001-vapa-dimer-snare-abstract; lapierre-1999-vap33-occludin-abstract].

## Open Questions

The biggest gap is that no experimental work exists on horse VAPA, so every functional statement here depends on the near-identity of horse and human VAPA in the MSP, coiled-coil and transmembrane regions. The most useful horse-specific question is what the alternative exon in A0A3Q2H1L9 (XP_023503235) does. It is conserved in human VAPA isoform 2 and in other mammals [uniprot-Q9P0L0-2-human-VAPA-isoform2; uniprot-A0A5F7ZL45; uniprot-A0A8I3MVB2], yet no functional study comparing the long and short forms was found. It is also unknown which isoform is expressed in which horse tissue (Bgee reports high expression in muscle) and which isoform the PeptideAtlas evidence on the entry refers to. A third open point is whether the extra ~45 residues, which are rich in proline, serine and threonine and so likely flexible and possibly phosphorylated, lengthen the reach of VAPA tethers between the ER and the membrane opposite. Dong et al. noted that VAPA runs as a doublet of splice variants in human cells [dong-2016-vap-endosome-pi4p-fulltext], so isoform-specific knockout and rescue experiments are feasible. Other open questions apply to VAPA in general: how the many FFAT and phospho-FFAT partners compete for a limited VAPA pool [murphy-2016-vap-review-abstract; dimattia-2020-phospho-ffat-abstract]; which kinases and phosphatases control phospho-FFAT-dependent contacts in vivo; how VAPA and VAPB divide their functions, given that most loss-of-function studies remove both [dong-2016-vap-endosome-pi4p-abstract; peretti-2008-vap-golgi-lipid-abstract]; and whether the reported plasma-membrane and tight-junction pools of VAPA are real or reflect ER–PM contacts [lapierre-1999-vap33-occludin-abstract; weber-boyvat-2015-orp3-rras-abstract]. In equine biology, further work could look at VAPA in skeletal muscle ER–PM junctions (relevant to Kv2 and lipid signalling), at its potential role in equine viral infections through the IFITM3/OSBP axis [aminibavil-2013-ifitm3-vapa-abstract], and at whether VAP levels change in equine motor neuron disease, by analogy with human ALS [teuling-2007-vapb-mutant-aggregates-abstract].

## References

- **uniprot-A0A3Q2H1L9-entry** — UniProtKB/TrEMBL entry A0A3Q2H1L9 (VAPA, *Equus caballus*), entry version 32. https://rest.uniprot.org/uniprotkb/A0A3Q2H1L9.txt
- **uniprot-A0A3Q2H1L9** — UniProtKB A0A3Q2H1L9 sequence (FASTA). https://rest.uniprot.org/uniprotkb/A0A3Q2H1L9.fasta
- **uniprot-Q9P0L0-human-VAPA-entry** — UniProtKB/Swiss-Prot entry Q9P0L0 (VAPA_HUMAN). https://rest.uniprot.org/uniprotkb/Q9P0L0.txt
- **uniprot-Q9P0L0-2-human-VAPA-isoform2** — UniProtKB Q9P0L0-2, human VAPA isoform 2 (294 aa). https://rest.uniprot.org/uniprotkb/Q9P0L0-2.fasta
- **uniprot-A0A3Q2H6V0** — UniProtKB A0A3Q2H6V0, horse VAPA (320 aa). https://rest.uniprot.org/uniprotkb/A0A3Q2H6V0.fasta
- **uniprot-A0A5F7ZL45** — UniProtKB A0A5F7ZL45, *Macaca mulatta* VAPA (294 aa). https://rest.uniprot.org/uniprotkb/A0A5F7ZL45.fasta
- **uniprot-A0A8I3MVB2** — UniProtKB A0A8I3MVB2, *Canis lupus familiaris* VAPA (294 aa). https://rest.uniprot.org/uniprotkb/A0A8I3MVB2.fasta
- **uniprot-A0A8C4KTX6** — UniProtKB A0A8C4KTX6, *Equus asinus* VAPA (294 aa). https://rest.uniprot.org/uniprotkb/A0A8C4KTX6.fasta
- **refseq-XP_023503236-horse-VAPA-isoformX2** — NCBI RefSeq protein XP_023503236, VAPA isoform X2 [*Equus caballus*], 249 aa. https://www.ncbi.nlm.nih.gov/protein/XP_023503236
- **alpy-2013-stard3-vap** — Alpy F, Rousseau A, Schwab Y, Legueux F, Stoll I, Wendling C, Spiegelhalter C, Kessler P, Mathelin C, Rio MC, Levine TP, Tomasetto C. STARD3 or STARD3NL and VAP form a novel molecular tether between late endosomes and the ER. Journal of cell science 2013. PMID:24105263; DOI:10.1242/jcs.139295. https://pubmed.ncbi.nlm.nih.gov/24105263/ https://doi.org/10.1242/jcs.139295
- **amarilio-2005-vap-nir-er-structure** — Amarilio R, Ramachandran S, Sabanay H, Lev S. Differential regulation of endoplasmic reticulum structure through VAP-Nir protein interaction. The Journal of biological chemistry 2005. PMID:15545272; DOI:10.1074/jbc.m409566200. https://pubmed.ncbi.nlm.nih.gov/15545272/ https://doi.org/10.1074/jbc.m409566200
- **aminibavil-2013-ifitm3-vapa** — Amini-Bavil-Olyaee S, Choi YJ, Lee JH, Shi M, Huang IC, Farzan M, Jung JU. The antiviral effector IFITM3 disrupts intracellular cholesterol homeostasis to block viral entry. Cell host & microbe 2013. PMID:23601107; PMCID:PMC3646482; DOI:10.1016/j.chom.2013.03.006. https://pubmed.ncbi.nlm.nih.gov/23601107/ https://doi.org/10.1016/j.chom.2013.03.006
- **cabukusta-2020-human-vapome** — Cabukusta B, Berlin I, van Elsland DM, Forkink I, Spits M, de Jong AWM, Akkermans JJLL, Wijdeven RHM, Janssen GMC, van Veelen PA, Neefjes J. Human VAPome Analysis Reveals MOSPD1 and MOSPD3 as Membrane Contact Site Proteins Interacting with FFAT-Related FFNT Motifs. Cell reports 2020. PMID:33296653; DOI:10.1016/j.celrep.2020.108475. https://pubmed.ncbi.nlm.nih.gov/33296653/ https://doi.org/10.1016/j.celrep.2020.108475
- **chang-2013-nir2-erpm** — Chang CL, Hsieh TS, Yang TT, Rothberg KG, Azizoglu DB, Volk E, Liao JC, Liou J. Feedback regulation of receptor-induced Ca2+ signaling mediated by E-Syt1 and Nir2 at endoplasmic reticulum-plasma membrane junctions. Cell reports 2013. PMID:24183667; DOI:10.1016/j.celrep.2013.09.038. https://pubmed.ncbi.nlm.nih.gov/24183667/ https://doi.org/10.1016/j.celrep.2013.09.038
- **dimattia-2020-phospho-ffat** — Di Mattia T, Martinet A, Ikhlef S, McEwen AG, Nominé Y, Wendling C, Poussin-Courmontagne P, Voilquin L, Eberling P, Ruffenach F, Cavarelli J, Slee J, Levine TP, Drin G, Tomasetto C, Alpy F. FFAT motif phosphorylation controls formation and lipid transfer function of inter-organelle contacts. The EMBO journal 2020. PMID:33124732; PMCID:PMC7705450; DOI:10.15252/embj.2019104369. https://pubmed.ncbi.nlm.nih.gov/33124732/ https://doi.org/10.15252/embj.2019104369
- **dong-2016-vap-endosome-pi4p** — Dong R, Saheki Y, Swarup S, Lucast L, Harper JW, De Camilli P. Endosome-ER Contacts Control Actin Nucleation and Retromer Function through VAP-Dependent Regulation of PI4P. Cell 2016. PMID:27419871; PMCID:PMC4963242; DOI:10.1016/j.cell.2016.06.037. https://pubmed.ncbi.nlm.nih.gov/27419871/ https://doi.org/10.1016/j.cell.2016.06.037
- **furuita-2010-vapa-osbp-nmr** — Furuita K, Jee J, Fukada H, Mishima M, Kojima C. Electrostatic interaction between oxysterol-binding protein and VAMP-associated protein A revealed by NMR and mutagenesis studies. The Journal of biological chemistry 2010. PMID:20178991; PMCID:PMC2857075; DOI:10.1074/jbc.m109.082602. https://pubmed.ncbi.nlm.nih.gov/20178991/ https://doi.org/10.1074/jbc.m109.082602
- **hanada-2003-cert** — Hanada K, Kumagai K, Yasuda S, Miura Y, Kawano M, Fukasawa M, Nishijima M. Molecular machinery for non-vesicular trafficking of ceramide. Nature 2003. PMID:14685229; DOI:10.1038/nature02188. https://pubmed.ncbi.nlm.nih.gov/14685229/ https://doi.org/10.1038/nature02188
- **johnson-2018-kv2-vap** — Johnson B, Leek AN, Solé L, Maverick EE, Levine TP, Tamkun MM. Kv2 potassium channels form endoplasmic reticulum/plasma membrane junctions via interaction with VAPA and VAPB. Proceedings of the National Academy of Sciences of the United States of America 2018. PMID:29941597; PMCID:PMC6077746; DOI:10.1073/pnas.1805757115. https://pubmed.ncbi.nlm.nih.gov/29941597/ https://doi.org/10.1073/pnas.1805757115
- **kaiser-2005-msp-ffat-structure** — Kaiser SE, Brickner JH, Reilein AR, Fenn TD, Walter P, Brunger AT. Structural basis of FFAT motif-mediated ER targeting. Structure (London, England : 1993) 2005. PMID:16004875; DOI:10.1016/j.str.2005.04.010. https://pubmed.ncbi.nlm.nih.gov/16004875/ https://doi.org/10.1016/j.str.2005.04.010
- **kawano-2006-cert-vap** — Kawano M, Kumagai K, Nishijima M, Hanada K. Efficient trafficking of ceramide from the endoplasmic reticulum to the Golgi apparatus requires a VAMP-associated protein-interacting FFAT motif of CERT. The Journal of biological chemistry 2006. PMID:16895911; DOI:10.1074/jbc.m605032200. https://pubmed.ncbi.nlm.nih.gov/16895911/ https://doi.org/10.1074/jbc.m605032200
- **kim-2015-nir2-pi-transfer** — Kim YJ, Guzman-Hernandez ML, Wisniewski E, Balla T. Phosphatidylinositol-Phosphatidic Acid Exchange by Nir2 at ER-PM Contact Sites Maintains Phosphoinositide Signaling Competence. Developmental cell 2015. PMID:26028218; PMCID:PMC4476625; DOI:10.1016/j.devcel.2015.04.028. https://pubmed.ncbi.nlm.nih.gov/26028218/ https://doi.org/10.1016/j.devcel.2015.04.028
- **kirmiz-2018-kv2-erpm-remodeling** — Kirmiz M, Palacio S, Thapa P, King AN, Sack JT, Trimmer JS. Remodeling neuronal ER-PM junctions is a conserved nonconducting function of Kv2 plasma membrane ion channels. Molecular biology of the cell 2018. PMID:30091655; PMCID:PMC6233057; DOI:10.1091/mbc.e18-05-0337. https://pubmed.ncbi.nlm.nih.gov/30091655/ https://doi.org/10.1091/mbc.e18-05-0337
- **kirmiz-2018-vap-kv2-neurons** — Kirmiz M, Vierra NC, Palacio S, Trimmer JS. Identification of VAPA and VAPB as Kv2 Channel-Interacting Proteins Defining Endoplasmic Reticulum-Plasma Membrane Junctions in Mammalian Brain Neurons. The Journal of neuroscience : the official journal of the Society for Neuroscience 2018. PMID:30012696; PMCID:PMC6113906; DOI:10.1523/jneurosci.0893-18.2018. https://pubmed.ncbi.nlm.nih.gov/30012696/ https://doi.org/10.1523/jneurosci.0893-18.2018
- **lapierre-1999-vap33-occludin** — Lapierre LA, Tuma PL, Navarre J, Goldenring JR, Anderson JM. VAP-33 localizes to both an intracellular vesicle population and with occludin at the tight junction. Journal of cell science 1999. PMID:10523508; DOI:10.1242/jcs.112.21.3723. https://pubmed.ncbi.nlm.nih.gov/10523508/ https://doi.org/10.1242/jcs.112.21.3723
- **lehto-2005-orp3-vapa** — Lehto M, Hynynen R, Karjalainen K, Kuismanen E, Hyvärinen K, Olkkonen VM. Targeting of OSBP-related protein 3 (ORP3) to endoplasmic reticulum and plasma membrane is controlled by multiple determinants. Experimental cell research 2005. PMID:16143324; DOI:10.1016/j.yexcr.2005.08.003. https://pubmed.ncbi.nlm.nih.gov/16143324/ https://doi.org/10.1016/j.yexcr.2005.08.003
- **lev-2008-vap-review** — Lev S, Ben Halevy D, Peretti D, Dahan N. The VAP protein family: from cellular functions to motor neuron disease. Trends in cell biology 2008. PMID:18468439; DOI:10.1016/j.tcb.2008.03.006. https://pubmed.ncbi.nlm.nih.gov/18468439/ https://doi.org/10.1016/j.tcb.2008.03.006
- **loewen-2003-ffat-motif** — Loewen CJ, Roy A, Levine TP. A conserved ER targeting motif in three families of lipid binding proteins and in Opi1p binds VAP. The EMBO journal 2003. PMID:12727870; PMCID:PMC156073; DOI:10.1093/emboj/cdg201. https://pubmed.ncbi.nlm.nih.gov/12727870/ https://doi.org/10.1093/emboj/cdg201
- **luckenardjomande-2020-wdr44-vap** — Lucken-Ardjomande Häsler S, Vallis Y, Pasche M, McMahon HT. GRAF2, WDR44, and MICAL1 mediate Rab8/10/11-dependent export of E-cadherin, MMP14, and CFTR ΔF508. The Journal of cell biology 2020. PMID:32344433; PMCID:PMC7199855; DOI:10.1083/jcb.201811014. https://pubmed.ncbi.nlm.nih.gov/32344433/ https://doi.org/10.1083/jcb.201811014
- **mesmin-2013-osbp-four-step** — Mesmin B, Bigay J, Moser von Filseck J, Lacas-Gervais S, Drin G, Antonny B. A four-step cycle driven by PI(4)P hydrolysis directs sterol/PI(4)P exchange by the ER-Golgi tether OSBP. Cell 2013. PMID:24209621; DOI:10.1016/j.cell.2013.09.056. https://pubmed.ncbi.nlm.nih.gov/24209621/ https://doi.org/10.1016/j.cell.2013.09.056
- **mikitova-2012-ffat-thermodynamics** — Mikitova V, Levine TP. Analysis of the key elements of FFAT-like motifs identifies new proteins that potentially bind VAP on the ER, including two AKAPs and FAPP2. PloS one 2012. PMID:22276202; PMCID:PMC3261905; DOI:10.1371/journal.pone.0030455. https://pubmed.ncbi.nlm.nih.gov/22276202/ https://doi.org/10.1371/journal.pone.0030455
- **murphy-2016-vap-review** — Murphy SE, Levine TP. VAP, a Versatile Access Point for the Endoplasmic Reticulum: Review and analysis of FFAT-like motifs in the VAPome. Biochimica et biophysica acta 2016. PMID:26898182; DOI:10.1016/j.bbalip.2016.02.009. https://pubmed.ncbi.nlm.nih.gov/26898182/ https://doi.org/10.1016/j.bbalip.2016.02.009
- **nishimura-1999-hvap-a** — Nishimura Y, Hayashi M, Inada H, Tanaka T. Molecular cloning and characterization of mammalian homologues of vesicle-associated membrane protein-associated (VAMP-associated) proteins. Biochemical and biophysical research communications 1999. PMID:9920726; DOI:10.1006/bbrc.1998.9876. https://pubmed.ncbi.nlm.nih.gov/9920726/ https://doi.org/10.1006/bbrc.1998.9876
- **nishimura-2004-vapb-als** — Nishimura AL, Mitne-Neto M, Silva HC, Richieri-Costa A, Middleton S, Cascio D, Kok F, Oliveira JR, Gillingwater T, Webb J, Skehel P, Zatz M. A mutation in the vesicle-trafficking protein VAPB causes late-onset spinal muscular atrophy and amyotrophic lateral sclerosis. American journal of human genetics 2004. PMID:15372378; PMCID:PMC1182111; DOI:10.1086/425287. https://pubmed.ncbi.nlm.nih.gov/15372378/ https://doi.org/10.1086/425287
- **peretti-2008-vap-golgi-lipid** — Peretti D, Dahan N, Shimoni E, Hirschberg K, Lev S. Coordinated lipid transfer between the endoplasmic reticulum and the Golgi complex requires the VAP proteins and is essential for Golgi-mediated transport. Molecular biology of the cell 2008. PMID:18614794; PMCID:PMC2526681; DOI:10.1091/mbc.e08-05-0498. https://pubmed.ncbi.nlm.nih.gov/18614794/ https://doi.org/10.1091/mbc.e08-05-0498
- **petry-2017-rhodococcus-vapa-horse-farms** — Petry S, Sévin C, Fleury MA, Duquesne F, Foucher N, Laugier C, Henry-Amar M, Tapprest J. Differential distribution of <i>vapA</i>-positive <i>Rhodococcus equi</i> in affected and unaffected horse-breeding farms. The Veterinary record 2017. PMID:28642343; DOI:10.1136/vr.104088. https://pubmed.ncbi.nlm.nih.gov/28642343/ https://doi.org/10.1136/vr.104088
- **rofe-2017-rhodococcus-vapa-endolysosome** — Rofe AP, Davis LJ, Whittingham JL, Latimer-Bowman EC, Wilkinson AJ, Pryor PR. The Rhodococcus equi virulence protein VapA disrupts endolysosome function and stimulates lysosome biogenesis. MicrobiologyOpen 2017. PMID:27762083; PMCID:PMC5387311; DOI:10.1002/mbo3.416. https://pubmed.ncbi.nlm.nih.gov/27762083/ https://doi.org/10.1002/mbo3.416
- **saita-2009-protrudin-vap** — Saita S, Shirane M, Natume T, Iemura SI, Nakayama KI. Promotion of neurite extension by protrudin requires its interaction with vesicle-associated membrane protein-associated protein. The Journal of biological chemistry 2009. PMID:19289470; PMCID:PMC2679478; DOI:10.1074/jbc.m807938200. https://pubmed.ncbi.nlm.nih.gov/19289470/ https://doi.org/10.1074/jbc.m807938200
- **skehel-1995-aplysia-vap33** — Skehel PA, Martin KC, Kandel ER, Bartsch D. A VAMP-binding protein from Aplysia required for neurotransmitter release. Science (New York, N.Y.) 1995. PMID:7667638; DOI:10.1126/science.7667638. https://pubmed.ncbi.nlm.nih.gov/7667638/ https://doi.org/10.1126/science.7667638
- **stefan-2011-osh-sac1-contacts** — Stefan CJ, Manford AG, Baird D, Yamada-Hanff J, Mao Y, Emr SD. Osh proteins regulate phosphoinositide metabolism at ER-plasma membrane contact sites. Cell 2011. PMID:21295699; DOI:10.1016/j.cell.2010.12.034. https://pubmed.ncbi.nlm.nih.gov/21295699/ https://doi.org/10.1016/j.cell.2010.12.034
- **teuling-2007-vapb-mutant-aggregates** — Teuling E, Ahmed S, Haasdijk E, Demmers J, Steinmetz MO, Akhmanova A, Jaarsma D, Hoogenraad CC. Motor neuron disease-associated mutant vesicle-associated membrane protein-associated protein (VAP) B recruits wild-type VAPs into endoplasmic reticulum-derived tubular aggregates. The Journal of neuroscience : the official journal of the Society for Neuroscience 2007. PMID:17804640; PMCID:PMC6672975; DOI:10.1523/jneurosci.2661-07.2007. https://pubmed.ncbi.nlm.nih.gov/17804640/ https://doi.org/10.1523/jneurosci.2661-07.2007
- **venditti-2019-fapp1-sac1-vap** — Venditti R, Masone MC, Rega LR, Di Tullio G, Santoro M, Polishchuk E, Serrano IC, Olkkonen VM, Harada A, Medina DL, La Montagna R, De Matteis MA. The activity of Sac1 across ER-TGN contact sites requires the four-phosphate-adaptor-protein-1. The Journal of cell biology 2019. PMID:30659099; PMCID:PMC6400556; DOI:10.1083/jcb.201812021. https://pubmed.ncbi.nlm.nih.gov/30659099/ https://doi.org/10.1083/jcb.201812021
- **wang-2012-viperin-vap** — Wang S, Wu X, Pan T, Song W, Wang Y, Zhang F, Yuan Z. Viperin inhibits hepatitis C virus replication by interfering with binding of NS5A to host protein hVAP-33. The Journal of general virology 2012. PMID:21957124; DOI:10.1099/vir.0.033860-0. https://pubmed.ncbi.nlm.nih.gov/21957124/ https://doi.org/10.1099/vir.0.033860-0
- **weber-boyvat-2015-orp3-rras** — Weber-Boyvat M, Kentala H, Lilja J, Vihervaara T, Hanninen R, Zhou Y, Peränen J, Nyman TA, Ivaska J, Olkkonen VM. OSBP-related protein 3 (ORP3) coupling with VAMP-associated protein A regulates R-Ras activity. Experimental cell research 2015. PMID:25447204; DOI:10.1016/j.yexcr.2014.10.019. https://pubmed.ncbi.nlm.nih.gov/25447204/ https://doi.org/10.1016/j.yexcr.2014.10.019
- **weir-1998-vap33-vamp** — Weir ML, Klip A, Trimble WS. Identification of a human homologue of the vesicle-associated membrane protein (VAMP)-associated protein of 33 kDa (VAP-33): a broadly expressed protein that binds to VAMP. The Biochemical journal 1998. PMID:9657962; PMCID:PMC1219579; DOI:10.1042/bj3330247. https://pubmed.ncbi.nlm.nih.gov/9657962/ https://doi.org/10.1042/bj3330247
- **weir-2001-vapa-dimer-snare** — Weir ML, Xie H, Klip A, Trimble WS. VAP-A binds promiscuously to both v- and tSNAREs. Biochemical and biophysical research communications 2001. PMID:11511104; DOI:10.1006/bbrc.2001.5437. https://pubmed.ncbi.nlm.nih.gov/11511104/ https://doi.org/10.1006/bbrc.2001.5437
- **wilhelm-2017-stard3-cholesterol** — Wilhelm LP, Wendling C, Védie B, Kobayashi T, Chenard MP, Tomasetto C, Drin G, Alpy F. STARD3 mediates endoplasmic reticulum-to-endosome cholesterol transport at membrane contact sites. The EMBO journal 2017. PMID:28377464; PMCID:PMC5430228; DOI:10.15252/embj.201695917. https://pubmed.ncbi.nlm.nih.gov/28377464/ https://doi.org/10.15252/embj.201695917
- **wu-2018-er-contact-review** — Wu H, Carvalho P, Voeltz GK. Here, there, and everywhere: The importance of ER membrane contact sites. Science (New York, N.Y.) 2018. PMID:30072511; PMCID:PMC6568312; DOI:10.1126/science.aan5835. https://pubmed.ncbi.nlm.nih.gov/30072511/ https://doi.org/10.1126/science.aan5835
- **wyles-2002-vapa-osbp** — Wyles JP, McMaster CR, Ridgway ND. Vesicle-associated membrane protein-associated protein-A (VAP-A) interacts with the oxysterol-binding protein to modify export from the endoplasmic reticulum. The Journal of biological chemistry 2002. PMID:12023275; DOI:10.1074/jbc.m201191200. https://pubmed.ncbi.nlm.nih.gov/12023275/ https://doi.org/10.1074/jbc.m201191200
- **yeshaw-2019-vps13a-vap** — Yeshaw WM, van der Zwaag M, Pinto F, Lahaye LL, Faber AI, Gómez-Sánchez R, Dolga AM, Poland C, Monaco AP, van IJzendoorn SC, Grzeschik NA, Velayos-Baeza A, Sibon OC. Human VPS13A is associated with multiple organelles and influences mitochondrial morphology and lipid droplet motility. eLife 2019. PMID:30741634; PMCID:PMC6389287; DOI:10.7554/elife.43561. https://pubmed.ncbi.nlm.nih.gov/30741634/ https://doi.org/10.7554/elife.43561
- **zhao-2018-vap-autophagosome** — Zhao YG, Liu N, Miao G, Chen Y, Zhao H, Zhang H. The ER Contact Proteins VAPA/B Interact with Multiple Autophagy Proteins to Modulate Autophagosome Biogenesis. Current biology : CB 2018. PMID:29628370; DOI:10.1016/j.cub.2018.03.002. https://pubmed.ncbi.nlm.nih.gov/29628370/ https://doi.org/10.1016/j.cub.2018.03.002


## Citations

1. alpy-2013-stard3-vap-abstract.md
2. alpy-2013-stard3-vap-summary.md
3. amarilio-2005-vap-nir-er-structure-abstract.md
4. amarilio-2005-vap-nir-er-structure-summary.md
5. aminibavil-2013-ifitm3-vapa-abstract.md
6. aminibavil-2013-ifitm3-vapa-fulltext.txt
7. aminibavil-2013-ifitm3-vapa-summary.md
8. cabukusta-2020-human-vapome-abstract.md
9. cabukusta-2020-human-vapome-summary.md
10. chang-2013-nir2-erpm-abstract.md
11. chang-2013-nir2-erpm-summary.md
12. dimattia-2020-phospho-ffat-abstract.md
13. dimattia-2020-phospho-ffat-fulltext.txt
14. dimattia-2020-phospho-ffat-summary.md
15. dong-2016-vap-endosome-pi4p-abstract.md
16. dong-2016-vap-endosome-pi4p-fulltext.txt
17. dong-2016-vap-endosome-pi4p-summary.md
18. furuita-2010-vapa-osbp-nmr-abstract.md
19. furuita-2010-vapa-osbp-nmr-summary.md
20. hanada-2003-cert-abstract.md
21. hanada-2003-cert-summary.md
22. johnson-2018-kv2-vap-abstract.md
23. johnson-2018-kv2-vap-summary.md
24. kaiser-2005-msp-ffat-structure-abstract.md
25. kaiser-2005-msp-ffat-structure-summary.md
26. kawano-2006-cert-vap-abstract.md
27. kawano-2006-cert-vap-summary.md
28. kim-2015-nir2-pi-transfer-abstract.md
29. kim-2015-nir2-pi-transfer-fulltext.txt
30. kim-2015-nir2-pi-transfer-summary.md
31. kirmiz-2018-kv2-erpm-remodeling-abstract.md
32. kirmiz-2018-kv2-erpm-remodeling-fulltext.txt
33. kirmiz-2018-kv2-erpm-remodeling-summary.md
34. kirmiz-2018-vap-kv2-neurons-abstract.md
35. kirmiz-2018-vap-kv2-neurons-summary.md
36. lapierre-1999-vap33-occludin-abstract.md
37. lapierre-1999-vap33-occludin-summary.md
38. lehto-2005-orp3-vapa-abstract.md
39. lehto-2005-orp3-vapa-summary.md
40. lev-2008-vap-review-abstract.md
41. lev-2008-vap-review-summary.md
42. loewen-2003-ffat-motif-abstract.md
43. loewen-2003-ffat-motif-summary.md
44. luckenardjomande-2020-wdr44-vap-abstract.md
45. luckenardjomande-2020-wdr44-vap-fulltext.txt
46. luckenardjomande-2020-wdr44-vap-summary.md
47. mesmin-2013-osbp-four-step-abstract.md
48. mesmin-2013-osbp-four-step-summary.md
49. meta.json
50. mikitova-2012-ffat-thermodynamics-abstract.md
51. mikitova-2012-ffat-thermodynamics-fulltext.txt
52. mikitova-2012-ffat-thermodynamics-summary.md
53. murphy-2016-vap-review-abstract.md
54. murphy-2016-vap-review-summary.md
55. nishimura-1999-hvap-a-abstract.md
56. nishimura-1999-hvap-a-summary.md
57. nishimura-2004-vapb-als-abstract.md
58. nishimura-2004-vapb-als-summary.md
59. peretti-2008-vap-golgi-lipid-abstract.md
60. peretti-2008-vap-golgi-lipid-summary.md
61. petry-2017-rhodococcus-vapa-horse-farms-abstract.md
62. petry-2017-rhodococcus-vapa-horse-farms-summary.md
63. refseq-XP_023503236-horse-VAPA-isoformX2.fasta
64. rofe-2017-rhodococcus-vapa-endolysosome-abstract.md
65. rofe-2017-rhodococcus-vapa-endolysosome-fulltext.txt
66. rofe-2017-rhodococcus-vapa-endolysosome-summary.md
67. saita-2009-protrudin-vap-abstract.md
68. saita-2009-protrudin-vap-summary.md
69. skehel-1995-aplysia-vap33-abstract.md
70. skehel-1995-aplysia-vap33-summary.md
71. stefan-2011-osh-sac1-contacts-abstract.md
72. stefan-2011-osh-sac1-contacts-summary.md
73. teuling-2007-vapb-mutant-aggregates-abstract.md
74. teuling-2007-vapb-mutant-aggregates-summary.md
75. uniprot-A0A3Q2H1L9-entry.txt
76. uniprot-A0A3Q2H1L9.fasta
77. uniprot-A0A3Q2H6V0.fasta
78. uniprot-A0A5F7ZL45.fasta
79. uniprot-A0A8C4KTX6.fasta
80. uniprot-A0A8I3MVB2.fasta
81. uniprot-K7FSH6.fasta
82. uniprot-Q9P0L0-2-human-VAPA-isoform2.fasta
83. uniprot-Q9P0L0-human-VAPA-entry.txt
84. uniprot-Q9P0L0-human-VAPA.fasta
85. venditti-2019-fapp1-sac1-vap-abstract.md
86. venditti-2019-fapp1-sac1-vap-fulltext.txt
87. venditti-2019-fapp1-sac1-vap-summary.md
88. wang-2012-viperin-vap-abstract.md
89. wang-2012-viperin-vap-summary.md
90. weber-boyvat-2015-orp3-rras-abstract.md
91. weber-boyvat-2015-orp3-rras-summary.md
92. weir-1998-vap33-vamp-abstract.md
93. weir-1998-vap33-vamp-summary.md
94. weir-2001-vapa-dimer-snare-abstract.md
95. weir-2001-vapa-dimer-snare-summary.md
96. wilhelm-2017-stard3-cholesterol-abstract.md
97. wilhelm-2017-stard3-cholesterol-fulltext.txt
98. wilhelm-2017-stard3-cholesterol-summary.md
99. wu-2018-er-contact-review-abstract.md
100. wu-2018-er-contact-review-fulltext.txt
101. wu-2018-er-contact-review-summary.md
102. wyles-2002-vapa-osbp-abstract.md
103. wyles-2002-vapa-osbp-summary.md
104. yeshaw-2019-vps13a-vap-abstract.md
105. yeshaw-2019-vps13a-vap-fulltext.txt
106. yeshaw-2019-vps13a-vap-summary.md
107. zhao-2018-vap-autophagosome-abstract.md
108. zhao-2018-vap-autophagosome-summary.md