---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:29:12.574826'
end_time: '2026-10-26T03:36:31.319407'
duration_seconds: 438.74
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: PEA15
  gene_symbol: PEA15
  uniprot_accession: A0A9L0RWM8
  protein_description: 'RecName: Full=Astrocytic phosphoprotein PEA-15 {ECO:0000256|ARBA:ARBA00015367};
    AltName: Full=15 kDa phosphoprotein enriched in astrocytes {ECO:0000256|ARBA:ARBA00033278};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: DEATH-like_dom_sf. (IPR011029); DED_dom. (IPR001875); PEA15_DED.
    (IPR029546); DED (PF01335)
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
citation_count: 64
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0RWM8
- **Protein Description:** RecName: Full=Astrocytic phosphoprotein PEA-15 {ECO:0000256|ARBA:ARBA00015367}; AltName: Full=15 kDa phosphoprotein enriched in astrocytes {ECO:0000256|ARBA:ARBA00033278};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** DEATH-like_dom_sf. (IPR011029); DED_dom. (IPR001875); PEA15_DED. (IPR029546); DED (PF01335)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PEA15" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PEA15' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PEA15** (gene ID: PEA15, UniProt: A0A9L0RWM8) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PEA15 (Astrocytic phosphoprotein PEA-15) in the horse, *Equus caballus* (UniProt A0A9L0RWM8)

## Introduction and summary

PEA-15 (phosphoprotein enriched in astrocytes, 15 kDa; also called PED, "phosphoprotein enriched in diabetes") is a small, non-catalytic cytoplasmic adaptor protein built from a single N-terminal death effector domain (DED) and a short, flexible C-terminal tail. Its best-established molecular function is as a phosphorylation-regulated binding partner for the ERK1/2 MAP kinases. In its unphosphorylated state it binds ERK1/2 through two docking sites on the kinase and holds them in the cytoplasm. This blocks ERK-driven nuclear transcription and proliferation, while still letting cytoplasmic ERK act on selected partners such as RSK2 and the integrin-activation machinery [formstecher-2001-pea15-erk-sequestration-abstract][mace-2013-erk2-pea15-structure-fulltext][vaidyanathan-2007-pea15-erk-rsk2-abstract]. Its second main function uses the same DED. PEA-15 binds the DED-containing adaptors of the extrinsic apoptosis pathway, FADD and caspase-8, and in this way inhibits apoptosis triggered by Fas and TNF receptor 1 [condorelli-1999-ped-antiapoptotic-fas-tnfr1-abstract][kitsberg-1999-pea15-knockout-astrocytes-abstract]. Two phosphorylation sites, Ser104 (protein kinase C) and Ser116 (CaMKII or Akt), act as a switch between these two activities. Phosphorylation releases ERK and favours FADD binding [kubes-1998-pea15-ser104-ser116-abstract][renganathan-2005-pea15-phosphorylation-fadd-abstract][krueger-2005-pea15-phosphorylation-erk-abstract]. PEA-15 has also been linked to glucose transport, through its overexpression in type 2 diabetes and its effects on GLUT1 and GLUT4 trafficking, and to stabilisation of phospholipase D [condorelli-1998-ped-glucose-transport-diabetes-abstract][zhang-2000-pea15-phospholipase-d-abstract].

No experimental study of PEA-15 in the horse was found. A PubMed search for PEA15 together with horse, equine or *Equus* returned no records. The horse protein is known only from the genome assembly [wade-2009-horse-genome-abstract] and from automatic annotation [uniprot-A0A9L0RWM8-entry]. Everything stated below about function is therefore inferred from mammalian orthologues, mainly human, mouse and rat. As shown in the next section, that inference is unusually secure: the 130-residue core of the horse protein is identical in sequence to human PEA-15.

## Identity verification and the horse gene product

The target entry, A0A9L0RWM8, is an unreviewed TrEMBL record of 176 amino acids. It derives from the Ensembl gene model ENSECAG00000019187 on horse chromosome 5, with RefSeq XP_070124104.1 and NCBI GeneID 100058382. Its name, "Astrocytic phosphoprotein PEA-15", was assigned by automatic rules. It carries one DED (PROSITE PS50168, residues 49–127), the PEA15-specific DED InterPro signature (IPR029546), CDD cd08338 (DED_PEA15) and PANTHER subfamily PTHR48169:SF1 ("Astrocytic phosphoprotein PEA-15") [uniprot-A0A9L0RWM8-entry]. The CTD cross-reference 8682 is the human PEA15 gene identifier, which confirms that the gene symbol PEA15 and the protein description refer to the same orthologue.

I aligned this sequence with reviewed human PEA-15 (Q15121, 130 aa) [uniprot-Q15121-human-PEA15-entry]. Horse residues 47–176 are 100% identical to human residues 1–130 (analysis done for this report; sequences from the UniProt entries). The horse model differs only by a 46-residue N-terminal extension (MLPTATLEETVPGADSQRALFLYQPGRATAGPFCLLAPGCASERAF). This extension most likely comes from an upstream alternative start or exon in the gene model. A second horse TrEMBL entry, F7AD02 (139 aa), carries a different and shorter 9-residue extension (MLPTATLEV) before the same 130-residue core [uniprot-F7AD02-horse-PEA15-sequence]. Human PEA15 likewise has an alternatively spliced isoform with an unrelated N-terminal extension [uniprot-Q15121-human-PEA15-entry]. Whether the N-terminally extended horse forms are made as proteins is not known. Because the canonical protein starts at the conserved Met of MAEYGTLL, horse residue 47 corresponds to human residue 1. The regulatory sites Ser104 and Ser116 therefore sit at Ser150 and Ser162 of A0A9L0RWM8, and the ERK-binding C-terminal motif (human 121–129) sits at horse 167–175.

This extreme conservation matches early observations. Mouse and human PEA-15 are 96% identical [estelles-1996-pea15-two-mrnas-abstract], and PEA-15 immunoreactivity, including its phosphorylation, is detectable in the brains of mammals, birds, amphibians and fish [danziger-1995-pea15-expression-conservation-abstract]. No literature describes a different "PEA15" gene that could be confused with this one. The symbol is unambiguous.

## Molecular architecture: a death effector domain plus a regulatory tail

PEA-15 was first purified as a heat-stable, acidic 15 kDa cytosolic phosphoprotein from striatal astrocytes. It exists as an unphosphorylated form (N) and two phosphorylated isoelectric variants (Pa, Pb) [araujo-1993-pea15-pkc-substrate-abstract]. The deduced mouse protein has 130 residues and initially showed no similarity to any known protein [estelles-1996-pea15-two-mrnas-abstract]. Hill and colleagues solved its NMR structure and found an N-terminal DED, the classic six-helix bundle of the death-domain superfamily. Its helices α1–α6 span residues 2–14, 17–27, 33–37, 42–51, 61–69 and 73–89, and are followed by a C-terminal tail of irregular structure [hill-2002-pea15-erk-docking-structure-fulltext]. NMR footprinting and mutagenesis showed that both the DED and the tail are needed to bind ERK. The ERK-binding face of the DED resembles the surface that the death domain of *Drosophila* Tube uses to bind its partners. This suggests that death-fold modules reuse a common interaction surface [hill-2002-pea15-erk-docking-structure-abstract].

The crystal structures of PEA-15 bound to ERK2 in unphosphorylated, monophosphorylated and dually phosphorylated states explained how so small a protein inhibits a kinase [mace-2013-erk2-pea15-structure-abstract]. PEA-15 binds in a bipartite way. Its DED occupies the ERK2 DEF-docking site and directly contacts the activation loop at the Thr-X-Tyr region. The C-terminal residues 122–127 bind the D-peptide (D-motif/DEJL) docking groove in a reverse orientation, with Pro126 filling the ΦA pocket [mace-2013-erk2-pea15-structure-fulltext]. The D-site interaction alone is weak (Kd about 18 µM), whereas the full bipartite interaction is tight (Kd about 700 nM) [mace-2013-erk2-pea15-structure-fulltext]. Binding through the DEF site sets off an allosteric conduit that disrupts key features of active ERK2. It also shields the phosphorylated activation loop from phosphatases, so that ERK is ready to act as soon as it is released [mace-2013-erk2-pea15-structure-abstract]. These findings are consistent with earlier biophysical work. That work proposed the C-terminal 121-LXLXXXXKK-129 segment as a reverse D-motif, and showed that an Elk-1 D-motif peptide displaces PEA-15 from ERK2, so that PEA-15 blocks ERK2 interactions with D-motif substrates [callaway-2005-pea15-erk2-anisotropy-abstract]. On the kinase side, ERK2 residues before the αG helix and in the MAP kinase insert are needed for PEA-15 binding [chou-2003-pea15-erk-integrin-abstract][whitehurst-2004-pea15-erk2-nuclear-entry-abstract]. PEA-15 has no enzymatic activity of its own. Reviews describe it as a molecular adaptor or scaffold [fiory-2009-ped-pea15-review-abstract][greig-2014-pea15-review-abstract].

## Primary function: cytoplasmic anchoring and routing of ERK1/2 MAP kinases

The defining function of PEA-15 is to control where ERK1/2 is located in the cell. Formstecher and colleagues showed that PEA-15 binds ERK1/2 and keeps them out of the nucleus, which blocks ERK-dependent transcription and proliferation. This anchoring requires a nuclear export sequence in PEA-15. Cells with genetic deletion of PEA-15 showed more nuclear ERK, more c-Fos transcription and faster proliferation [formstecher-2001-pea15-erk-sequestration-abstract]. Hill et al. placed this predicted nuclear export sequence in the N-terminus of PEA-15 [hill-2002-pea15-erk-docking-structure-fulltext]. Mechanistically, PEA-15 binds through the ERK2 MAP kinase insert. In this way it blocks the interaction of ERK2 with nucleoporins that ERK2 needs to enter the nucleus without karyopherins, and in vitro it also blocks ERK2 activation by MEK1 [whitehurst-2004-pea15-erk2-nuclear-entry-abstract]. The physiological relevance of anchoring ERK in the cytoplasm is supported by cancer-cell studies. In breast cancer, PEA-15 levels are inversely related to invasiveness, and PEA-15 suppresses invasion only when it can bind ERK and exclude it from the nucleus [glading-2007-pea15-tumor-invasion-abstract].

PEA-15 does not simply switch ERK off. It redirects ERK output towards cytoplasmic targets. It binds both ERK and the ERK substrate RSK2, raises the amount of ERK bound to RSK2, and enhances RSK2 activation and CREB-dependent transcription. Lymphocytes lacking PEA-15 show impaired RSK2 activation after phorbol ester stimulation, and re-expressing PEA-15 rescues this [vaidyanathan-2007-pea15-erk-rsk2-abstract]. PEA-15 was originally isolated in an expression screen because it reversed the suppression of integrin activation caused by H-Ras/Raf. This activity needs the DED [ramos-1998-pea15-ded-integrin-abstract], depends on PEA-15 binding ERK1/2, and is lost with mutations in either the DED or the tail that prevent ERK binding [chou-2003-pea15-erk-integrin-abstract]. Overexpressed PEA-15 has also been reported to increase Ras-GTP loading and MEK and ERK activity in CHO cells, again in a DED-dependent way [ramos-2000-pea15-ras-erk-abstract]. The best in vivo evidence that anchoring ERK is a physiological function, and not an artefact of overexpression, comes from PEA-15-null mice. Lymphocytes in these mice develop normally. After CD3/CD28 stimulation, however, their T cells move more ERK into the nucleus, transcribe and secrete more IL-2, and proliferate more in response to IL-2. In wild-type T cells, T-cell receptor activation itself causes PEA-15 to release ERK, and overexpressing PEA-15 in Jurkat cells blocks nuclear ERK and IL-2 transcription. T-cell apoptosis was unchanged in the knockout, which suggests that in this cell type the ERK-anchoring activity matters more than the anti-apoptotic one [pastorino-2010-pea15-tcell-erk-abstract]. Taken together, the data present PEA-15 as a scaffold that decides which ERK functions a cell carries out, keeping ERK at cytoplasmic and membrane-proximal targets and away from nuclear ones [vaidyanathan-2007-pea15-erk-rsk2-abstract][greig-2014-pea15-review-abstract].

## Second function: inhibition of death-receptor-induced apoptosis

The DED also lets PEA-15 join the death-inducing signalling complex (DISC) of the extrinsic apoptosis pathway. In MCF-7 and HeLa cells, about fivefold overexpression of PED/PEA-15 blocked apoptosis induced by FasL and TNFα. PED/PEA-15 co-precipitated with FADD and caspase-8 (FLICE), lowered FADD–caspase-8 association and reduced caspase-8 activation, which suggests that it competes for DED–DED interactions [condorelli-1999-ped-antiapoptotic-fas-tnfr1-abstract]. Genetic evidence comes from PEA-15-null mice. Astrocytes lacking PEA-15 survive TNFα less well, and in vitro PEA-15 binds both FADD and caspase-8 [kitsberg-1999-pea15-knockout-astrocytes-abstract]. This anti-apoptotic activity depends on phosphorylation of Ser116. Akt binds PEA-15 and phosphorylates Ser116 with near-stoichiometric efficiency. A non-phosphorylatable S116G mutant is degraded about three times faster and protects much less against apoptosis, and inhibiting Akt lowers PEA-15 levels and makes glioma cells sensitive to TRAIL [trencia-2003-akt-phosphorylates-ped-abstract]. Reviews note that PEA-15 may also act on intrinsic apoptotic pathways, but the extrinsic (DISC) mechanism is the best supported [fiory-2009-ped-pea15-review-abstract][greig-2014-pea15-review-abstract].

## Regulation by phosphorylation: a switch between proliferation and survival

PEA-15 is a major endogenous substrate of PKC. Araujo et al. mapped the PKC site to the sequence LTRIPSAKK [araujo-1993-pea15-pkc-substrate-abstract], which contains Ser104. In astrocytes stimulated with endothelin, a second site, Ser116, is phosphorylated in a Ca²⁺-dependent manner by CaMKII. Prior phosphorylation at Ser116 makes subsequent PKC phosphorylation of Ser104 easier [kubes-1998-pea15-ser104-ser116-abstract]. Akt also targets Ser116 [trencia-2003-akt-phosphorylates-ped-abstract]. These modifications produce the non-, mono- and bi-phosphorylated forms seen on two-dimensional gels, and suggested early on that PEA-15 integrates several signals [renault-2003-pea15-apoptosis-cellcycle-abstract].

The functional consequences have been mapped in some detail. Phosphorylation at Ser104 blocks ERK binding in vitro and in vivo, whereas phosphorylation at Ser116 promotes FADD binding. All phospho-forms stay mostly in the cytoplasm [renganathan-2005-pea15-phosphorylation-fadd-abstract]. Krueger et al. reported that full release of ERK1/2 required phosphorylation of both sites. Phosphomimetic PEA-15 could not hold ERK in the cytoplasm, so cells expressing high PEA-15 levels could still proliferate. Phosphorylated PEA-15 is present in normal mammary epithelium [krueger-2005-pea15-phosphorylation-erk-abstract]. RSK2 scaffolding is also controlled by PEA-15 phosphorylation [vaidyanathan-2007-pea15-erk-rsk2-abstract]. The resulting model is that unphosphorylated PEA-15 restrains ERK and so limits proliferation, while phosphorylated PEA-15 releases ERK and becomes a stable, FADD-binding anti-apoptotic protein. Phosphorylation therefore acts as a switch between controlling proliferation and controlling death [renganathan-2005-pea15-phosphorylation-fadd-abstract][greig-2014-pea15-review-abstract]. In the horse protein, all of these residues and motifs are conserved at the offset positions given above (Ser150 and Ser162).

## Other reported partners and roles: glucose transport and phospholipase D

PEA-15 was independently rediscovered as PED in a differential-display screen. Its mRNA and protein were overexpressed in fibroblasts, skeletal muscle and adipose tissue from people with type 2 diabetes. In L6 myotubes, overexpressed PED/PEA-15 increased plasma-membrane GLUT1 but impaired insulin-stimulated GLUT4 translocation and glucose uptake, in a PKC-dependent way [condorelli-1998-ped-glucose-transport-diabetes-abstract]. Later work extended this to defects in insulin secretion and to effects on glucose tolerance [fiory-2009-ped-pea15-review-abstract]. The UniProt keywords "Sugar transport" and "Transport" for the horse entry come from these studies [uniprot-A0A9L0RWM8-entry]. They describe a regulatory effect, not a transporter function. A yeast two-hybrid screen identified PEA-15 as a partner of phospholipase D1. Binding involves part of the DED and C-terminal flanking residues, and the PEA-15 contact on PLD1 overlaps the RhoA site. PEA-15 did not change intrinsic PLD activity but raised PLD1 and PLD2 protein levels, which suggests that it stabilises or chaperones these proteins [zhang-2000-pea15-phospholipase-d-abstract]. These activities are less well established than ERK anchoring and DISC inhibition, and their mechanisms are less clear.

## Expression and subcellular localisation

PEA-15 was named for its abundance in astrocytes. It is nonetheless found in all cultured brain cell types and in peripheral tissues including eye and lung, and its expression and phosphorylation increase during development [danziger-1995-pea15-expression-conservation-abstract]. Two mRNAs that differ in 3′UTR length are expressed in brain and peripheral tissues [estelles-1996-pea15-two-mrnas-abstract]. Human PEA-15 is reported to be ubiquitous, and most abundant in glucose-using tissues such as heart, brain, muscle and fat [uniprot-Q15121-human-PEA15-entry]. For horse, the UniProt entry links to Expression Atlas baseline data, but no specific study exists [uniprot-A0A9L0RWM8-entry].

PEA-15 is a cytoplasmic protein. Fractionation finds it mostly in the cytosol, with the PKC-phosphorylated form also associated with membranes and with stabilised microtubules [danziger-1995-pea15-expression-conservation-abstract][estelles-1996-pea15-two-mrnas-abstract]. Its nuclear export sequence keeps it, and the ERK bound to it, in the cytoplasm [formstecher-2001-pea15-erk-sequestration-abstract][greig-2014-pea15-review-fulltext]. This cytoplasmic distribution does not change with phosphorylation state [renganathan-2005-pea15-phosphorylation-fadd-abstract]. The horse entry's "Cytoplasm" annotation (GO:0005737) is therefore well supported by orthology. The horse entry's other GO terms, "MAPK cascade" and "negative regulation of extrinsic apoptotic signaling pathway via death domain receptors" [uniprot-A0A9L0RWM8-entry], match the two experimentally best-supported functions described above. Annotations that would capture the function more precisely include ERK binding (MAP kinase binding), negative regulation of ERK1/2 nuclear import (cytoplasmic sequestration), and death effector domain binding to FADD and caspase-8.

## Open Questions

The main gap is that nothing about PEA-15 has been measured directly in the horse. Every functional statement here is inferred from rodent and human orthologues. The inference is strong because the 130-residue core is identical, but it remains an inference. A first question is whether the N-terminal extensions in the horse gene models are real. A0A9L0RWM8 carries a 46-residue extension and F7AD02 a 9-residue one. Transcript evidence (RNA-seq 5′ ends, Ensembl/RefSeq support) and proteomics could show whether these products are translated. If they are, it would be worth testing whether an extended N-terminus affects the nuclear export sequence or the DED surfaces that bind ERK and FADD, both of which lie near the canonical N-terminus. The PeptideAtlas keyword on the horse entry suggests that peptides have been detected, but the specific peptides, and whether any cover the extension, should be checked.

A second set of questions concerns the general biology. It is still unclear how the Ser104/Ser116 switch is coordinated in vivo, and whether the results that single and double phosphorylation regulate ERK binding differently [renganathan-2005-pea15-phosphorylation-fadd-abstract][krueger-2005-pea15-phosphorylation-erk-abstract] are consistent with each other. The structural basis for FADD and caspase-8 binding, and for the PLD1 and Akt interactions, has not been solved in the way the ERK2 complex has. The relationship between PEA-15's DISC activity and the ERK it holds in the cytoplasm is also unresolved: are they mutually exclusive in one molecule, or do they act together? Finally, given the links to insulin resistance in humans [condorelli-1998-ped-glucose-transport-diabetes-abstract], equine metabolic syndrome and insulin dysregulation would be a natural place to test whether PEA-15 expression in horse muscle and adipose tissue changes the way PED does in human type 2 diabetes. The protein's abundance in astrocytes and its protection against TNF-induced death also make it a candidate in equine neuroinflammatory conditions. No such data exist at present.

## References

- **uniprot-A0A9L0RWM8-entry** — UniProtKB/TrEMBL entry A0A9L0RWM8_HORSE, "Astrocytic phosphoprotein PEA-15", *Equus caballus*. https://rest.uniprot.org/uniprotkb/A0A9L0RWM8.txt (entry version 15).
- **uniprot-Q15121-human-PEA15-entry** — UniProtKB/Swiss-Prot entry Q15121 (PEA15_HUMAN). https://rest.uniprot.org/uniprotkb/Q15121.txt
- **uniprot-F7AD02-horse-PEA15-sequence** — UniProtKB/TrEMBL entry F7AD02 (horse PEA15, 139 aa). https://rest.uniprot.org/uniprotkb/F7AD02.fasta
- **wade-2009-horse-genome** — Wade CM, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. Science 2009;326:865-867. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158
- **araujo-1993-pea15-pkc-substrate** — Araujo H, et al. Characterization of PEA-15, a major substrate for protein kinase C in astrocytes. J Biol Chem 1993;268(8):5911-20. PMID: 8449955
- **danziger-1995-pea15-expression-conservation** — Danziger N, et al. Cellular expression, developmental regulation, and phylogenic conservation of PEA-15, the astrocytic major phosphoprotein and protein kinase C substrate. J Neurochem 1995. PMID: 7861130; DOI: 10.1046/j.1471-4159.1995.64031016.x
- **estelles-1996-pea15-two-mrnas** — Estellés A, et al. The major astrocytic phosphoprotein PEA-15 is encoded by two mRNAs conserved on their full length in mouse and human. J Biol Chem 1996. PMID: 8662970; DOI: 10.1074/jbc.271.25.14800
- **condorelli-1998-ped-glucose-transport-diabetes** — Condorelli G, et al. PED/PEA-15 gene controls glucose transport and is overexpressed in type 2 diabetes mellitus. EMBO J 1998. PMID: 9670003; PMCID: PMC1170721; DOI: 10.1093/emboj/17.14.3858
- **condorelli-1999-ped-antiapoptotic-fas-tnfr1** — Condorelli G, et al. PED/PEA-15: an anti-apoptotic molecule that regulates FAS/TNFR1-induced apoptosis. Oncogene 1999. PMID: 10442631; DOI: 10.1038/sj.onc.1202831
- **kitsberg-1999-pea15-knockout-astrocytes** — Kitsberg D, et al. Knock-out of the neural death effector domain protein PEA-15 demonstrates that its expression protects astrocytes from TNFalpha-induced apoptosis. J Neurosci 1999. PMID: 10493725; PMCID: PMC6783010; DOI: 10.1523/JNEUROSCI.19-19-08244.1999
- **kubes-1998-pea15-ser104-ser116** — Kubes M, et al. Endothelin induces a calcium-dependent phosphorylation of PEA-15 in intact astrocytes: identification of Ser104 and Ser116 phosphorylated, respectively, by protein kinase C and calcium/calmodulin kinase II in vitro. J Neurochem 1998. PMID: 9721757; DOI: 10.1046/j.1471-4159.1998.71031307.x
- **ramos-1998-pea15-ded-integrin** — Ramos JW, et al. The death effector domain of PEA-15 is involved in its regulation of integrin activation. J Biol Chem 1998. PMID: 9852038; DOI: 10.1074/jbc.273.51.33897
- **ramos-2000-pea15-ras-erk** — Ramos JW, et al. Death effector domain protein PEA-15 potentiates Ras activation of extracellular signal receptor-activated kinase by an adhesion-independent mechanism. Mol Biol Cell 2000. PMID: 10982386; PMCID: PMC14961; DOI: 10.1091/mbc.11.9.2863
- **zhang-2000-pea15-phospholipase-d** — Zhang Y, et al. Regulation of expression of phospholipase D1 and D2 by PEA-15, a novel protein that interacts with them. J Biol Chem 2000. PMID: 10926929; DOI: 10.1074/jbc.M003329200
- **formstecher-2001-pea15-erk-sequestration** — Formstecher E, et al. PEA-15 mediates cytoplasmic sequestration of ERK MAP kinase. Dev Cell 2001. PMID: 11702783; DOI: 10.1016/s1534-5807(01)00035-1
- **hill-2002-pea15-erk-docking-structure** — Hill JM, et al. Recognition of ERK MAP kinase by PEA-15 reveals a common docking site within the death domain and death effector domain. EMBO J 2002. PMID: 12456656; PMCID: PMC136945; DOI: 10.1093/emboj/cdf641
- **renault-2003-pea15-apoptosis-cellcycle** — Renault F, et al. The multifunctional protein PEA-15 is involved in the control of apoptosis and cell cycle in astrocytes. Biochem Pharmacol 2003. PMID: 14555237; DOI: 10.1016/s0006-2952(03)00514-8
- **chou-2003-pea15-erk-integrin** — Chou FL, et al. PEA-15 binding to ERK1/2 MAPKs is required for its modulation of integrin activation. J Biol Chem 2003. PMID: 14506247; DOI: 10.1074/jbc.M309322200
- **trencia-2003-akt-phosphorylates-ped** — Trencia A, et al. Protein kinase B/Akt binds and phosphorylates PED/PEA-15, stabilizing its antiapoptotic action. Mol Cell Biol 2003;23(13):4511-4521. PMID: 12808093; PMCID: PMC164852; DOI: 10.1128/MCB.23.13.4511-4521.2003
- **whitehurst-2004-pea15-erk2-nuclear-entry** — Whitehurst AW, et al. The death effector domain protein PEA-15 prevents nuclear entry of ERK2 by inhibiting required interactions. J Biol Chem 2004. PMID: 14707138; DOI: 10.1074/jbc.M310031200
- **renganathan-2005-pea15-phosphorylation-fadd** — Renganathan H, et al. Phosphorylation of PEA-15 switches its binding specificity from ERK/MAPK to FADD. Biochem J 2005. PMID: 15916534; PMCID: PMC1199667; DOI: 10.1042/BJ20050378
- **krueger-2005-pea15-phosphorylation-erk** — Krueger J, et al. Phosphorylation of phosphoprotein enriched in astrocytes (PEA-15) regulates extracellular signal-regulated kinase-dependent transcription and cell proliferation. Mol Biol Cell 2005. PMID: 15917297; PMCID: PMC1182297; DOI: 10.1091/mbc.e04-11-1007
- **callaway-2005-pea15-erk2-anisotropy** — Callaway K, et al. Quantifying ERK2-protein interactions by fluorescence anisotropy: PEA-15 inhibits ERK2 by blocking the binding of DEJL domains. Biochim Biophys Acta 2005. PMID: 16324895; DOI: 10.1016/j.bbapap.2005.11.002
- **glading-2007-pea15-tumor-invasion** — Glading A, et al. PEA-15 inhibits tumor cell invasion by binding to extracellular signal-regulated kinase 1/2. Cancer Res 2007. PMID: 17308092; DOI: 10.1158/0008-5472.CAN-06-1378
- **vaidyanathan-2007-pea15-erk-rsk2** — Vaidyanathan H, et al. ERK MAP kinase is targeted to RSK2 by the phosphoprotein PEA-15. Proc Natl Acad Sci U S A 2007. PMID: 18077417; PMCID: PMC2148384; DOI: 10.1073/pnas.0704514104
- **pastorino-2010-pea15-tcell-erk** — Pastorino S, Renganathan H, Caliva MJ, Filbert EL, Opoku-Ansah J, Sulzmaier FJ, Gawecka JE, Werlen G, Shaw AS, Ramos JW. The death effector domain protein PEA-15 negatively regulates T-cell receptor signaling. FASEB J 2010;24(8):2818-28. PMID: 20354143; PMCID: PMC2909277; DOI: 10.1096/fj.09-144295
- **fiory-2009-ped-pea15-review** — Fiory F, et al. Frontiers: PED/PEA-15, a multifunctional protein controlling cell survival and glucose metabolism. Am J Physiol Endocrinol Metab 2009. PMID: 19531639; DOI: 10.1152/ajpendo.00228.2009
- **mace-2013-erk2-pea15-structure** — Mace PD, et al. Structure of ERK2 bound to PEA-15 reveals a mechanism for rapid release of activated MAPK. Nat Commun 2013. PMID: 23575685; PMCID: PMC3640864; DOI: 10.1038/ncomms2687
- **greig-2014-pea15-review** — Greig FH, Nixon GF. Phosphoprotein enriched in astrocytes (PEA)-15: a potential therapeutic target in multiple disease states. Pharmacol Ther 2014. PMID: 24657708; PMCID: PMC4127788; DOI: 10.1016/j.pharmthera.2014.03.006


## Citations

1. araujo-1993-pea15-pkc-substrate-abstract.md
2. araujo-1993-pea15-pkc-substrate-summary.md
3. callaway-2005-pea15-erk2-anisotropy-abstract.md
4. callaway-2005-pea15-erk2-anisotropy-summary.md
5. chou-2003-pea15-erk-integrin-abstract.md
6. chou-2003-pea15-erk-integrin-summary.md
7. condorelli-1998-ped-glucose-transport-diabetes-abstract.md
8. condorelli-1998-ped-glucose-transport-diabetes-summary.md
9. condorelli-1999-ped-antiapoptotic-fas-tnfr1-abstract.md
10. condorelli-1999-ped-antiapoptotic-fas-tnfr1-summary.md
11. danziger-1995-pea15-expression-conservation-abstract.md
12. danziger-1995-pea15-expression-conservation-summary.md
13. estelles-1996-pea15-two-mrnas-abstract.md
14. estelles-1996-pea15-two-mrnas-summary.md
15. fiory-2009-ped-pea15-review-abstract.md
16. fiory-2009-ped-pea15-review-summary.md
17. formstecher-2001-pea15-erk-sequestration-abstract.md
18. formstecher-2001-pea15-erk-sequestration-summary.md
19. glading-2007-pea15-tumor-invasion-abstract.md
20. glading-2007-pea15-tumor-invasion-summary.md
21. greig-2014-pea15-review-abstract.md
22. greig-2014-pea15-review-fulltext.txt
23. greig-2014-pea15-review-summary.md
24. hill-2002-pea15-erk-docking-structure-abstract.md
25. hill-2002-pea15-erk-docking-structure-fulltext.md
26. hill-2002-pea15-erk-docking-structure-summary.md
27. kitsberg-1999-pea15-knockout-astrocytes-abstract.md
28. kitsberg-1999-pea15-knockout-astrocytes-fulltext.md
29. kitsberg-1999-pea15-knockout-astrocytes-summary.md
30. krueger-2005-pea15-phosphorylation-erk-abstract.md
31. krueger-2005-pea15-phosphorylation-erk-fulltext.md
32. krueger-2005-pea15-phosphorylation-erk-summary.md
33. kubes-1998-pea15-ser104-ser116-abstract.md
34. kubes-1998-pea15-ser104-ser116-summary.md
35. mace-2013-erk2-pea15-structure-abstract.md
36. mace-2013-erk2-pea15-structure-fulltext.txt
37. mace-2013-erk2-pea15-structure-summary.md
38. pastorino-2010-pea15-tcell-erk-abstract.md
39. pastorino-2010-pea15-tcell-erk-summary.md
40. ramos-1998-pea15-ded-integrin-abstract.md
41. ramos-1998-pea15-ded-integrin-summary.md
42. ramos-2000-pea15-ras-erk-abstract.md
43. ramos-2000-pea15-ras-erk-fulltext.md
44. ramos-2000-pea15-ras-erk-summary.md
45. renault-2003-pea15-apoptosis-cellcycle-abstract.md
46. renault-2003-pea15-apoptosis-cellcycle-summary.md
47. renganathan-2005-pea15-phosphorylation-fadd-abstract.md
48. renganathan-2005-pea15-phosphorylation-fadd-fulltext.md
49. renganathan-2005-pea15-phosphorylation-fadd-summary.md
50. trencia-2003-akt-phosphorylates-ped-abstract.md
51. trencia-2003-akt-phosphorylates-ped-summary.md
52. uniprot-A0A9L0RWM8-entry.txt
53. uniprot-F7AD02-horse-PEA15-sequence.fasta
54. uniprot-Q15121-human-PEA15-entry.txt
55. vaidyanathan-2007-pea15-erk-rsk2-abstract.md
56. vaidyanathan-2007-pea15-erk-rsk2-fulltext.md
57. vaidyanathan-2007-pea15-erk-rsk2-summary.md
58. wade-2009-horse-genome-abstract.md
59. wade-2009-horse-genome-fulltext.txt
60. wade-2009-horse-genome-summary.md
61. whitehurst-2004-pea15-erk2-nuclear-entry-abstract.md
62. whitehurst-2004-pea15-erk2-nuclear-entry-summary.md
63. zhang-2000-pea15-phospholipase-d-abstract.md
64. zhang-2000-pea15-phospholipase-d-summary.md