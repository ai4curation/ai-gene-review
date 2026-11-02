---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:54:14.653470'
end_time: '2026-10-26T03:08:23.348448'
duration_seconds: 848.7
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: HSPA4
  gene_symbol: HSPA4
  uniprot_accession: A0A9L0S5Z5
  protein_description: 'RecName: Full=Heat shock 70 kDa protein 4 {ECO:0000256|ARBA:ARBA00018348};'
  gene_info: Name=HSPA4 {ECO:0000313|Ensembl:ENSECAP00000071556.1};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the heat shock protein 70 family.
  protein_domains: ATPase_NBD. (IPR043129); Heat_shock_70_CS. (IPR018181); HSP70_C_sf.
    (IPR029048); HSP70_peptide-bd_sf. (IPR029047); Hsp_70_fam. (IPR013126)
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
citation_count: 83
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0S5Z5
- **Protein Description:** RecName: Full=Heat shock 70 kDa protein 4 {ECO:0000256|ARBA:ARBA00018348};
- **Gene Information:** Name=HSPA4 {ECO:0000313|Ensembl:ENSECAP00000071556.1};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the heat shock protein 70 family.
- **Key Domains:** ATPase_NBD. (IPR043129); Heat_shock_70_CS. (IPR018181); HSP70_C_sf. (IPR029048); HSP70_peptide-bd_sf. (IPR029047); Hsp_70_fam. (IPR013126)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HSPA4" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HSPA4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HSPA4** (gene ID: HSPA4, UniProt: A0A9L0S5Z5) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# HSPA4 (Apg-2/HSPH2) in the horse, *Equus caballus* (UniProt A0A9L0S5Z5): a research report on function, localization and pathways

## Introduction and summary

The horse protein A0A9L0S5Z5 is an unreviewed, automatically annotated 800-residue product of the Ensembl gene ENSECAG00000020813 on horse chromosome 14. Its sequence comes from the Thoroughbred reference genome, and it is named "Heat shock 70 kDa protein 4" (gene symbol HSPA4) [uniprot-A0A9L0S5Z5-entry; wade-2009-horse-genome-fulltext]. I checked that the symbol and the protein actually match. The horse sequence is about 97% identical to reviewed human HSPA4 (P34932) across its whole length. The only large difference is a 40-residue segment in the C-terminal helical region that the horse model lacks. NCBI's independent RefSeq model for horse HSPA4 (isoform X1, XP_001918259.2, 840 residues) is identical to A0A9L0S5Z5 at all 800 shared positions and does include that segment [refseq-horse-HSPA4-proteins; notes-sequence-analysis]. The InterPro, CDD and PANTHER signatures in the entry are specific to the HSPA4 subfamily (HSPA4_NBD, ASKHA_NBD_HSP70_HSPA4, PTHR45639:SF6), not the general Hsp70 family [uniprot-A0A9L0S5Z5-entry; notes-sequence-analysis]. The symbol is therefore not ambiguous: this protein is the horse orthologue of mammalian HSPA4, also called Apg-2, HSP70RY or HSPH2. Almost no literature deals with the horse protein itself. Everything said here about its function is inferred from orthologues, mainly human and mouse, plus the closely related yeast and nematode Hsp110 proteins.

The name is misleading, and that matters for annotation. HSPA4 is not a canonical Hsp70. It belongs to the Hsp110 (HSPH) family, a large, divergent branch of the Hsp70 superfamily [kaneko-1997-apg2-cloning-abstract; easton-2000-hsp110-grp170-abstract; kampinga-2009-hsp-nomenclature-abstract; bracher-2015-hsp70-nef-review-fulltext]. Its main, well-established molecular function is as a **nucleotide exchange factor (NEF) for cytosolic Hsp70/Hsc70 chaperones**. It binds the Hsp70 nucleotide-binding domain and speeds the release of ADP, which lets ATP rebind and the Hsp70 substrate-binding cycle start again [dragovic-2006-hsp110-nef-abstract; raviol-2006-yeast-hsp110-nef-abstract; polier-2008-hsp70-hsp110-structure-abstract; schuermann-2008-hsp110-hsc70-structure-abstract]. HSPA4 does not catalyse a metabolic reaction. It has a weak intrinsic ATPase activity [raviol-2006-human-yeast-hsp110-abstract], and it can bind unfolded polypeptides directly, acting as a "holdase" [oh-1997-hsp110-thermoresistance-abstract; gotoh-2004-apg2-chaperone-hcc-abstract].

Animals lack Hsp100 disaggregases. In the metazoan cytosol, HSPA4 is one of the Hsp110 NEFs that, together with Hsc70 (HSPA8) and J-domain proteins (DNAJB1, DNAJA1/2), make up the main protein-disaggregation machine. This machine dissolves heat-induced aggregates and amyloid fibrils of α-synuclein, Tau and huntingtin [shorter-2011-mammalian-disaggregase-fulltext; rampelt-2012-hsp110-disaggregation-abstract; nillegoda-2015-hsp70-cochaperone-disaggregation-fulltext; gao-2015-alpha-synuclein-disaggregase-fulltext; scior-2018-htt-trimeric-chaperone-abstract; nachman-2020-tau-disaggregation-fulltext].

The protein works in the cytoplasm. In epithelia, part of it is also recruited to tight junctions, where it binds the SH3 domain of ZO-1 (TJP1) and modulates ZO-1/ZONAB signalling [tsapara-2006-apg2-zo1-zonab-abstract; aijaz-2007-apg2-tight-junction-fulltext]. In mice, loss of Hspa4 impairs spermatogenesis, causes cardiac hypertrophy and skeletal myopathy marked by accumulated ubiquitinated proteins, and is lethal at birth when combined with loss of its paralogue Hspa4l. All of these fit a role in cellular protein quality control [held-2011-hspa4-spermatogenesis-abstract; mohamed-2012-hspa4-cardiac-hypertrophy-abstract; mohamed-2014-hspa4l-hspa4-double-mutant-abstract; elkenani-2022-hspa4-skeletal-myopathy-fulltext]. The only horse-specific observation is that HSPA4 is a hub gene in the heat-shock network of blood transcripts that rise after endurance racing [su-2025-yili-horse-transcriptome-fulltext].

## Identity, nomenclature and evolutionary classification

Mouse *apg-2* was first cloned from a testis cDNA library using the related *apg-1* gene as a probe. Its predicted product of 841 amino acids was much longer than human "HSP70RY" (701 residues), and about the same length as hamster Hsp110 and Apg-1. Kaneko and colleagues therefore placed APG-2 in the Hsp110 family rather than the Hsp70 family. They interpreted HSP70RY as a truncated isoform of the same gene [kaneko-1997-apg2-cloning-abstract].

Easton, Kaneko and Subjeck later reviewed the large Hsp70 relatives. They defined the Hsp110 family (cytosolic and nuclear) and the Grp170 family (in the ER) as distinct groups within an Hsp70 superfamily. Both are recognisable by a long loop inserted between the β-sandwich peptide-binding domain and the α-helical "lid", by an enlarged helical domain, and by a C-terminal extension [easton-2000-hsp110-grp170-abstract]. The HUGO-aligned nomenclature guidelines for human heat-shock proteins put the HSPH (Hsp110) family alongside HSPA (Hsp70) [kampinga-2009-hsp-nomenclature-abstract]. The literature uses HSPH2 interchangeably for the HSPA4 product; Nillegoda et al., for example, call the human Hsp110 they used "HSPH2" [nillegoda-2015-hsp70-cochaperone-disaggregation-fulltext]. Mammals have three cytosolic Hsp110 paralogues: Hsp105/HSPH1, Apg-1/HSPA4L and Apg-2/HSPA4 [bracher-2015-hsp70-nef-review-fulltext].

The UniProt "SIMILARITY" line ("Belongs to the heat shock protein 70 family") is broad and should be read as membership of the Hsp70 superfamily. The specific signatures in the horse entry show that it belongs to the HSPA4 clade of the Hsp110 family [uniprot-A0A9L0S5Z5-entry]. My own comparison of the horse and human sequences found 776 identical residues in matched blocks (97% of the horse length) and 22 scattered single-residue substitutions. The N-terminal nucleotide-binding domain is essentially invariant. The horse model lacks a 40-residue stretch that in human HSPA4 lies at positions 680–719, in the C-terminal helical region [notes-sequence-analysis]. To find out whether this gap is a property of horse HSPA4 or of one gene model, I compared the entry with NCBI's RefSeq predictions for the horse gene. The 840-residue isoform X1 (XP_001918259.2) matches A0A9L0S5Z5 exactly at all 800 residues the two share, and also contains the 40-residue segment. It is 96.9% identical to human HSPA4 over its full length. The 735-residue isoform X2 (XP_023473466.1, XP_070090444.1) lacks the first 105 residues but also keeps the segment [refseq-horse-HSPA4-proteins; notes-sequence-analysis]. Two independent annotation pipelines therefore agree on the core horse sequence. A0A9L0S5Z5 looks like an in-frame variant missing one internal segment, as if an exon were skipped. Whether that variant is a real minor transcript has not been tested; I tried to check the Ensembl exon structure, but the Ensembl service did not return data during this work. The canonical horse protein is most likely the 840-residue form, which matches the human and mouse proteins in length [kaneko-1997-apg2-cloning-abstract].

## Domain architecture and structural basis of activity

Hsp110 proteins have the same overall architecture as Hsp70s: an N-terminal actin-fold nucleotide-binding domain (NBD), a β-sandwich domain and an α-helix bundle domain. They differ by long insertions and C-terminal extensions [bracher-2015-hsp70-nef-review-fulltext; easton-2000-hsp110-grp170-abstract]. The horse entry matches this layout, with ATPase_NBD (IPR043129), HSP70 peptide-binding (IPR029047) and C-terminal (IPR029048) superfamily signatures, and a HYOU1_C-type C-terminal domain (PF27508) [uniprot-A0A9L0S5Z5-entry].

The mechanism comes mainly from crystal structures of the yeast orthologue Sse1p bound to the NBD of Hsp70. Polier et al. showed that ATP-bound Sse1p uses both its own NBD and its three-helix bundle domain to embrace the Hsp70 NBD. This opens the Hsp70 nucleotide cleft and releases bound ADP. Sse1p mutations that abolish NEF activity are lethal, so nucleotide exchange is the essential function of the protein [polier-2008-hsp70-hsp110-structure-abstract]. Schuermann et al. solved the structure of an Hsp110:Hsc70 complex independently. They described an extensive protein–protein interface, symmetric bridging between the nucleotides in the two NBDs, and an electropositive pore through which nucleotides enter and leave. They explained exchange as the coupled open/closed isomerisation of the two NBDs [schuermann-2008-hsp110-hsc70-structure-abstract]. Andréasson et al. mapped the same yeast complex in solution with hydrogen–deuterium exchange and site-specific crosslinking. The two NBDs face each other with extensive contacts, and a second contact runs from the protruding C-terminal α-helical subdomain of Sse1 to the edge of Hsp70 NBD lobe II. Sse1 releases nucleotide by a Bag-1-like mechanism that tilts lobe II and opens the cleft. Its binding mode is unique, but the mechanism converges with that of other NEF families [andreasson-2008-hsp110-hsp70-dynamics-abstract]. The second contact matters for the horse protein. The 40-residue segment missing from the A0A9L0S5Z5 model lies in the corresponding C-terminal helical region [notes-sequence-analysis], so if that isoform were expressed, its Hsp70-binding surface might be affected. This is an untested inference.

Bracher and Verghese contrasted this mode with that of bacterial GrpE. GrpE drives a wedge into the DnaK nucleotide cleft, whereas Sse1p attaches to the flank of NBD subdomain IIB and anchors on the rest of the NBD. Because the contact residues are highly conserved across the Hsp110/Grp170 family, all members presumably bind Hsp70 the same way [bracher-2015-hsp70-nef-review-fulltext]. The horse NBD is essentially identical to the human one [notes-sequence-analysis], so the horse protein almost certainly binds Hsc70/Hsp70 this way.

## Molecular function: Hsp70 nucleotide exchange factor, holdase and ATPase

Two papers published together in 2006 established that Hsp110 proteins are NEFs for Hsp70. Dragovic et al. showed that mammalian Hsp110 and yeast Sse1p/Sse2p catalyse efficient nucleotide exchange on Hsp70 (yeast Ssa1p and the ribosome-associated Ssb1p). Exchange required the N-terminal ATPase domain and the extreme C-terminus. In vitro, the Hsp110 proteins substantially increased the rate and yield of Hsp70-mediated refolding of heat-denatured luciferase, and yeast lacking *SSE1* had a luciferase folding defect under heat stress [dragovic-2006-hsp110-nef-abstract]. Raviol et al. found the same activity independently. Sse1p formed a stable, nucleotide-sensitive complex with Ssa1p, did not need to hydrolyse ATP itself to act as a NEF, and was essential in vivo; overexpressing the unrelated NEF Fes1p only partly made up for its loss [raviol-2006-yeast-hsp110-nef-abstract]. In the Hsp70 reaction cycle, J-domain proteins stimulate ATP hydrolysis by Hsp70 to trap substrate. HSPA4 and other NEFs then remove ADP so that ATP can bind and release the substrate. HSPA4 therefore controls how fast client proteins cycle on and off Hsc70 [bracher-2015-hsp70-nef-review-fulltext; dragovic-2006-hsp110-nef-abstract].

Mouse and human HSPA4 papers describe the protein as an HSP110-family NEF and co-chaperone for HSP70 [held-2011-hspa4-spermatogenesis-abstract; mohamed-2012-hspa4-cardiac-hypertrophy-abstract; elkenani-2022-hspa4-skeletal-myopathy-fulltext]. The direct biochemistry on human Apg-2/HSPA4 in the disaggregation studies below confirms that this paralogue works as an Hsc70 NEF in reconstituted systems [shorter-2011-mammalian-disaggregase-fulltext; nillegoda-2015-hsp70-cochaperone-disaggregation-fulltext; gao-2015-alpha-synuclein-disaggregase-fulltext].

HSPA4 has activities of its own besides nucleotide exchange. Oh et al. showed with the related Hsp110 that the family binds heat-denatured proteins selectively and keeps them soluble and able to refold. They did this more efficiently than Hsc70, and the bound substrates were refolded once Hsc70 and Hdj-1 were added [oh-1997-hsp110-thermoresistance-abstract]. Recombinant Apg-2 has a similar chaperone (holdase) activity in a luciferase thermal-denaturation assay [gotoh-2004-apg2-chaperone-hcc-abstract]. Bracher and Verghese note that Hsp110 homologues seem to prefer aromatic residues in substrate sequences, whereas canonical Hsp70s prefer aliphatic and proline residues [bracher-2015-hsp70-nef-review-fulltext].

Raviol, Bukau and Mayer compared human Apg-2 with yeast Sse1. Both had intrinsic ATPase activity, and ATP binding and hydrolysis changed the conformation of both, as seen by tryptophan fluorescence. Only Sse1, however, was stimulated by the J-protein Sis1 or showed nucleotide-dependent changes in protease sensitivity. Hsp110 subtypes therefore differ biochemically, and the yeast mechanism should not be transferred to HSPA4 without care [raviol-2006-human-yeast-hsp110-abstract]. Mattoo et al. went further. They argued that the human cytosolic Hsp110s (HSPH1 and HSPH2) are true chaperones that, with Hsp40, use ATP to unfold stable misfolded polypeptides, and that Hsp70 and Hsp110 take turns releasing bound substrate from one another during disaggregation [mattoo-2013-hsp110-unfoldase-abstract]. That view is still debated. Rampelt et al. found that the Hsp110 contribution to disaggregation depends on nucleotide exchange, not ATPase activity [rampelt-2012-hsp110-disaggregation-abstract].

## The metazoan Hsp70–Hsp40–Hsp110 disaggregase

Bacteria, fungi and plants rescue aggregated proteins with Hsp100/ClpB AAA+ disaggregases working with Hsp70. Animals have no Hsp100 homologue. Shorter showed that mammalian cytosol (rabbit reticulocyte lysate and a second cytosolic source, labelled RLC and SHC) still has a potent ATP-dependent disaggregation and reactivation activity that does not need p97. Immunodepletion experiments removed either the heat-inducible Hsp105 or the constitutive Apg-2. Purified Apg-2 together with Hsc70 or Hsp70 and the J-protein Hdj1 (DNAJB1) was necessary and sufficient to dissolve large disordered aggregates slowly and recover native protein. Adding Apg-2 back to Apg-2-depleted cytosol restored activity. In this system Hsp110 had to engage substrate, engage Hsp70, promote nucleotide exchange and hydrolyse ATP [shorter-2011-mammalian-disaggregase-fulltext].

Rampelt et al. showed that Hsp110 remodels the human Hsp70–Hsp40 system to disaggregate and refold heat- and chemically denatured aggregates, both in vitro and in cell extracts. The effect depended on nucleotide exchange. Knocking down Hsp110 in *C. elegans*, but not an unrelated NEF, impaired the dissolution of heat-induced aggregates and sharply shortened lifespan after heat shock. Hsp110-powered Hsp70 is therefore the main disaggregation machine in metazoa [rampelt-2012-hsp110-disaggregation-abstract].

Nillegoda et al. found that full activity needs transient complexes of class A and class B J-proteins. These complexes give efficient disaggregation by the human HSPA8–HSPH2 (Hsc70–Apg-2/HSPA4) system and the nematode equivalent. In their reconstitutions, human Apg-2 was the Hsp110 component [nillegoda-2015-hsp70-cochaperone-disaggregation-fulltext]. Gao et al. then showed that Hsc70, DNAJB1 and an Hsp110 NEF (Apg2/HSPA4 or Hsp105α) disassemble preformed α-synuclein amyloid fibrils within minutes, by fragmentation and depolymerisation, into non-toxic monomers. None of the components acted alone. Apg2 greatly accelerated the reaction, and the unrelated NEF Bag1 gave about 80% less activity in a fluorescence dequenching assay [gao-2015-alpha-synuclein-disaggregase-fulltext].

Later studies extended the substrate range and showed how HSPA4 contributes. Scior et al. found that a trimeric complex of Hsc70, an Hsp110 and a J-protein completely suppresses fibril formation by huntingtin exon 1 (Q48) and resolubilises preformed huntingtin fibrils. The effect held in neural cells derived from Huntington's disease patients and in *C. elegans*, and the J-protein was the limiting component [scior-2018-htt-trimeric-chaperone-abstract]. Nachman et al. explicitly described the human Hsp70 disaggregase as HSPA8 (HSC70), DNAJB1 or DNAJB4, and HSPA4 (APG2). This machine took apart fibrils of all six Tau isoforms, as well as Sarkosyl-resistant Tau aggregates from cultured cells and Alzheimer's disease brain, and HSPA4 strongly increased the activity. The released monomers and small oligomers could seed new aggregation in cells, so the disaggregase cuts both ways [nachman-2020-tau-disaggregation-fulltext].

On mechanism, Wentink et al. found that DNAJB1 recognises oligomeric α-synuclein through multivalent contacts and directs HSP70 to the flexible termini of the fibril. DNAJB1 and HSP110 together then load many HSP70 molecules densely onto the fibril surface, producing "entropic pulling" forces. The authors argue that HSP110 takes an active part in remodelling the amyloid, beyond simply recycling Hsp70 nucleotide [wentink-2020-amyloid-disaggregation-hsp70-abstract]. Beton et al. watched single fibrils by atomic force microscopy, cryo-electron tomography and TIRF microscopy. Sub-stoichiometric Apg2 (HSPA4) greatly increased Hsc70 recruitment to α-synuclein fibrils, creating localised active zones. These zones then came apart in rapid, one-directional bursts of about four subunits per second [beton-2022-amyloid-hsp70-disaggregase-fulltext]. HSPA4 therefore acts catalytically and below stoichiometric amounts, and it sets how densely Hsc70 can be loaded onto a substrate.

Together these studies place HSPA4 at the centre of cytosolic protein quality control. It is the power-stroke NEF of the Hsc70–DNAJ disaggregase, and Hsp110 appears to be the NEF that most strongly promotes folding [bracher-2015-hsp70-nef-review-fulltext]. Nearly all of this biochemistry used human proteins. Because the horse NBD is essentially identical to the human one, the same activity is expected in the horse.

## Subcellular localization and non-chaperone interactions

The Hsp110 family is found in the cytoplasm and nucleus [easton-2000-hsp110-grp170-abstract], and the Hsp110 proteins have been described as exclusively cytosolic among the Hsp70 relatives [raviol-2006-yeast-hsp110-nef-abstract; raviol-2006-human-yeast-hsp110-abstract]. The disaggregase and refolding partners of HSPA4 (Hsc70, DNAJB1) also work in the cytosol [gao-2015-alpha-synuclein-disaggregase-fulltext]. The UniProt annotations of both the human protein and the horse entry give cytoplasm as the location [uniprot-P34932-human-HSPA4-entry; uniprot-A0A9L0S5Z5-entry]. The interaction most often recorded for human HSPA4 in IntAct is with HSPA8 (Hsc70) [uniprot-P34932-human-HSPA4-entry].

HSPA4 also has a second, junction-associated role. Tsapara, Matter and Balda screened an expression library with the SH3 domain of the tight-junction adaptor ZO-1 and recovered Apg-2. In MDCK canine kidney epithelial cells, Apg-2 co-immunoprecipitated with ZO-1 and was found partly at intercellular junctions. Heat shock increased both its recruitment to junctions and its binding to ZO-1. Apg-2 competed with the Y-box transcription factor ZONAB for the ZO-1 SH3 domain, changed ZONAB-driven reporter activity, and was needed for normal G1/S progression [tsapara-2006-apg2-zo1-zonab-abstract]. In a follow-up, depleting Apg-2 did not prevent tight junctions from forming. It did slow de novo junction assembly and the recruitment of ZO-1 to junctions, and in 3D culture the depleted cells failed to form polarised hollow cysts [aijaz-2007-apg2-tight-junction-fulltext]. This study is the source of the automatic UniProt annotation "Interacts with TJP1/ZO-1" carried by the horse entry [uniprot-A0A9L0S5Z5-entry]. Whether the junctional role uses the chaperone/NEF activity, or is a separate scaffolding interaction, is not known.

## Physiological roles revealed by loss-of-function in mammals

In mouse, *Hspa4* is expressed in all tissues [kaneko-1997-apg2-cloning-abstract; held-2011-hspa4-spermatogenesis-abstract]. It is not induced by classical heat shock in fibroblasts or Sertoli cells, which points to a constitutive "housekeeping" chaperone role [kaneko-1997-apg2-cloning-abstract]. Other studies, however, describe stress-induced expression in specific tissues [adachi-2015-hspa4-ibd-fulltext]. Knockout studies from one group (Adham and colleagues) show that tissues with heavy protein-folding loads depend on HSPA4.

*Hspa4*⁻/⁻ mice on a mixed background were generally viable. Many males were subfertile, with fewer and less motile sperm, because pachytene spermatocytes failed to finish meiotic prophase I and underwent apoptosis [held-2011-hspa4-spermatogenesis-abstract]. *Hspa4* knockout hearts developed concentric hypertrophy and fibrosis, which got worse under pressure overload. They also showed increased gp130–STAT3, CaMKII and calcineurin–NFAT signalling and accumulated polyubiquitinated proteins. The defect was cardiomyocyte-autonomous, and the authors attributed it to impaired chaperone-dependent protein quality control [mohamed-2012-hspa4-cardiac-hypertrophy-abstract]. In skeletal muscle, *Hspa4* loss caused growth retardation, about 35% mortality around weaning and progressive myopathy, with accumulated LC3-II and p62 and more apoptosis. This implicates HSPA4 in muscle autophagy and protein homeostasis [elkenani-2022-hspa4-skeletal-myopathy-fulltext].

*Hspa4l*⁻/⁻*Hspa4*⁻/⁻ double mutants died as newborns with pulmonary hypoplasia, failed pneumocyte maturation and accumulated ubiquitinated proteins. The two Hsp110 paralogues can therefore substitute for each other [mohamed-2014-hspa4l-hspa4-double-mutant-abstract]. Bracher and Verghese likewise note that only the combined knockout is lethal [bracher-2015-hsp70-nef-review-fulltext]. In the gut, HSPA4 deficiency changed apoptosis and IL-17/IL-23 responses in experimental colitis [adachi-2015-hspa4-ibd-fulltext]. It also sped up gastric ulcer healing, through higher SDF-1/CXCR4 and Twist expression and faster fibroblast migration [sakurai-2015-hspa4-gastric-ulcer-abstract]. HSPA4 is overexpressed in several carcinomas and has anti-apoptotic activity [gotoh-2004-apg2-chaperone-hcc-abstract]. These phenotypes are probably downstream effects of a proteostasis defect, not separate functions. Genetics in an invertebrate with a single Hsp110 gene points the same way. In *Drosophila*, Hsp110 is expressed in all tissues and is not needed for larval cell proliferation, but it is required for long-term survival and nervous-system development, and its loss leads to ubiquitin-positive inclusions in the brain. Overexpressing it is also harmful, so Hsp110 levels need to be balanced against Hsp40 co-chaperones in vivo [rios-2026-drosophila-hsp110-abstract].

## Evidence specific to the horse

A literature search found no biochemical, structural or cell-biological study of equine HSPA4. The horse protein is known only from the reference-genome-based Ensembl gene model [wade-2009-horse-genome-fulltext; uniprot-A0A9L0S5Z5-entry]. The one study that discusses horse HSPA4 is a whole-blood transcriptome survey of Yili horses before and after a 5,000-metre race. It sampled only the three leading horses. A STRING protein-interaction network built from the 2,171 differentially expressed mRNAs had a heat-shock-protein core of ten hub genes: HSP90AA1, HSPA4, HSP90AB1, STIP1, KDM6B, HSPA4L, HSPA8, PTGES3, HSPD1 and TCP1 [su-2025-yili-horse-transcriptome-fulltext]. The co-appearance of HSPA4 with its biochemical partner HSPA8 and its paralogue HSPA4L fits the chaperone network described above. This is still correlational, high-throughput expression evidence from a very small sample. It suggests, but does not show, that equine HSPA4 responds to exercise-induced proteotoxic or thermal stress.

For annotation purposes, the horse protein should be assigned the functions supported for its orthologues: adenyl-nucleotide exchange factor activity toward Hsc70/Hsp70; ATP binding and weak ATP hydrolysis; and binding of unfolded proteins. The processes are chaperone-mediated protein folding/refolding and protein disaggregation (protein quality control), with location in the cytosol and possibly at tight junctions in epithelia. All of these are inferred by orthology and sequence conservation [notes-sequence-analysis].

## Open questions

The most immediate question is whether the 40-residue segment missing from the A0A9L0S5Z5 model (human residues 680–719, in the C-terminal helical region) reflects a real equine splice isoform. The RefSeq models include the segment, which suggests that the canonical horse protein is the 840-residue form [refseq-horse-HSPA4-proteins; notes-sequence-analysis]. The Ensembl exon structure could not be checked during this work. RT-PCR across the relevant exon junction, or long-read transcript data from horse tissues, would settle the question. If the isoform is real, it would be worth testing whether it changes substrate binding or holdase activity, since the NEF interface lies mainly in the NBD and the three-helix bundle.

A second question is how important HSPA4 is compared with its paralogues HSPH1 (Hsp105) and HSPA4L in equine tissues, especially skeletal and cardiac muscle under exercise and heat load. Quantitative proteomics or targeted expression studies in Thoroughbred muscle biopsies after heat acclimation would address this. The transcriptome hub finding [su-2025-yili-horse-transcriptome-fulltext] needs replication in larger cohorts and at the protein level.

Third, the mechanism of mammalian HSPA4 itself is still debated. Rampelt et al. find that its disaggregation role relies on nucleotide exchange [rampelt-2012-hsp110-disaggregation-abstract]. Shorter and Mattoo et al. find that it needs ATP hydrolysis and that it unfolds substrates directly [shorter-2011-mammalian-disaggregase-fulltext; mattoo-2013-hsp110-unfoldase-abstract]. Human Apg-2 also behaves differently from yeast Sse1 [raviol-2006-human-yeast-hsp110-abstract]. A structure of a mammalian HSPA4–Hsc70 complex, and of HSPA4 bound to substrate, would resolve this better than the yeast models.

A fourth question, from the amyloid work, is whether HSPA4-driven disaggregation protects cells or harms them. Tau species released by the HSC70/DNAJB1/HSPA4 machine can seed new aggregation [nachman-2020-tau-disaggregation-fulltext], and in flies both too little and too much Hsp110 are harmful [rios-2026-drosophila-hsp110-abstract]. Whether the balance shifts in long-lived animals such as horses, which are prone to exercise- and heat-induced muscle stress, is entirely unexplored.

Finally, the ZO-1-binding role [tsapara-2006-apg2-zo1-zonab-abstract; aijaz-2007-apg2-tight-junction-fulltext] was characterised in canine kidney cells. It has not been tested in other species or in vivo, and no one has shown whether it depends on chaperone activity. Equine epithelial barriers, such as the gut and skin, are a possible but unexplored setting for this function.

## References

- **uniprot-A0A9L0S5Z5-entry**: UniProtKB/TrEMBL A0A9L0S5Z5_HORSE, Heat shock 70 kDa protein 4 (HSPA4), *Equus caballus*. https://rest.uniprot.org/uniprotkb/A0A9L0S5Z5.txt (entry version 15).
- **uniprot-P34932-human-HSPA4-entry**: UniProtKB/Swiss-Prot P34932 (HSP74_HUMAN), Heat shock 70 kDa protein 4, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/P34932.txt
- **notes-sequence-analysis**: My own pairwise sequence comparison of A0A9L0S5Z5 and P34932 (this work; see notes-sequence-analysis.md).
- **wade-2009-horse-genome**: Wade CM, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 2009;326:865–867. PMID: 19892987; PMCID: PMC3785132; DOI: 10.1126/science.1178158.
- **kaneko-1997-apg2-cloning**: Kaneko Y, Kimura T, Kishishita M, Noda Y, Fujita J. Cloning of apg-2 encoding a novel member of heat shock protein 110 family. *Gene* 1997;189(1):19–24. PMID: 9161406; DOI: 10.1016/s0378-1119(96)00807-4.
- **kampinga-2009-hsp-nomenclature**: Kampinga HH, et al. Guidelines for the nomenclature of the human heat shock proteins. *Cell Stress Chaperones* 2009;14(1):105–111. PMID: 18663603; PMCID: PMC2673902; DOI: 10.1007/s12192-008-0068-7.
- **easton-2000-hsp110-grp170**: Easton DP, Kaneko Y, Subjeck JR. The hsp110 and Grp170 stress proteins: newly recognized relatives of the Hsp70s. *Cell Stress Chaperones* 2000;5(4):276–290. PMID: 11048651; PMCID: PMC312858; DOI: 10.1379/1466-1268(2000)005<0276:thagsp>2.0.co;2.
- **oh-1997-hsp110-thermoresistance**: Oh HJ, Chen X, Subjeck JR. Hsp110 protects heat-denatured proteins and confers cellular thermoresistance. *J Biol Chem* 1997;272(50):31636–31640. PMID: 9395504; DOI: 10.1074/jbc.272.50.31636.
- **gotoh-2004-apg2-chaperone-hcc**: Gotoh K, et al. Apg-2 has a chaperone-like activity similar to Hsp110 and is overexpressed in hepatocellular carcinomas. *FEBS Lett* 2004;560(1-3):19–24. PMID: 14987991; DOI: 10.1016/S0014-5793(04)00034-1.
- **dragovic-2006-hsp110-nef**: Dragovic Z, Broadley SA, Shomura Y, Bracher A, Hartl FU. Molecular chaperones of the Hsp110 family act as nucleotide exchange factors of Hsp70s. *EMBO J* 2006;25(11):2519–2528. PMID: 16688212; PMCID: PMC1478182; DOI: 10.1038/sj.emboj.7601138.
- **raviol-2006-yeast-hsp110-nef**: Raviol H, Sadlish H, Rodriguez F, Mayer MP, Bukau B. Chaperone network in the yeast cytosol: Hsp110 is revealed as an Hsp70 nucleotide exchange factor. *EMBO J* 2006;25(11):2510–2518. PMID: 16688211; PMCID: PMC1478168; DOI: 10.1038/sj.emboj.7601139.
- **raviol-2006-human-yeast-hsp110**: Raviol H, Bukau B, Mayer MP. Human and yeast Hsp110 chaperones exhibit functional differences. *FEBS Lett* 2006;580(1):168–174. PMID: 16364315; DOI: 10.1016/j.febslet.2005.11.069.
- **polier-2008-hsp70-hsp110-structure**: Polier S, Dragovic Z, Hartl FU, Bracher A. Structural basis for the cooperation of Hsp70 and Hsp110 chaperones in protein folding. *Cell* 2008;133(6):1068–1079. PMID: 18555782; DOI: 10.1016/j.cell.2008.05.022.
- **schuermann-2008-hsp110-hsc70-structure**: Schuermann JP, et al. Structure of the Hsp110:Hsc70 nucleotide exchange machine. *Mol Cell* 2008;31(2):232–243. PMID: 18550409; PMCID: PMC2892728; DOI: 10.1016/j.molcel.2008.05.006.
- **tsapara-2006-apg2-zo1-zonab**: Tsapara A, Matter K, Balda MS. The heat-shock protein Apg-2 binds to the tight junction protein ZO-1 and regulates transcriptional activity of ZONAB. *Mol Biol Cell* 2006;17(3):1322–1330. PMID: 16407410; PMCID: PMC1382320; DOI: 10.1091/mbc.e05-06-0507.
- **aijaz-2007-apg2-tight-junction**: Aijaz S, et al. Regulation of tight junction assembly and epithelial morphogenesis by the heat shock protein Apg-2. *BMC Cell Biol* 2007;8:49. PMID: 18028534; PMCID: PMC2211299; DOI: 10.1186/1471-2121-8-49.
- **held-2011-hspa4-spermatogenesis**: Held T, et al. Heat-shock protein HSPA4 is required for progression of spermatogenesis. *Reproduction* 2011;142(1):133–144. PMID: 21487003; DOI: 10.1530/REP-11-0023.
- **shorter-2011-mammalian-disaggregase**: Shorter J. The mammalian disaggregase machinery: Hsp110 synergizes with Hsp70 and Hsp40 to catalyze protein disaggregation and reactivation in a cell-free system. *PLoS One* 2011;6(10):e26319. PMID: 22022600; PMCID: PMC3194798; DOI: 10.1371/journal.pone.0026319.
- **mohamed-2012-hspa4-cardiac-hypertrophy**: Mohamed BA, et al. Targeted disruption of Hspa4 gene leads to cardiac hypertrophy and fibrosis. *J Mol Cell Cardiol* 2012;53(4):459–468. PMID: 22884543; DOI: 10.1016/j.yjmcc.2012.07.014.
- **rampelt-2012-hsp110-disaggregation**: Rampelt H, et al. Metazoan Hsp70 machines use Hsp110 to power protein disaggregation. *EMBO J* 2012;31(21):4221–4235. PMID: 22990239; PMCID: PMC3492728; DOI: 10.1038/emboj.2012.264.
- **mattoo-2013-hsp110-unfoldase**: Mattoo RUH, Sharma SK, Priya S, Finka A, Goloubinoff P. Hsp110 is a bona fide chaperone using ATP to unfold stable misfolded polypeptides and reciprocally collaborate with Hsp70 to solubilize protein aggregates. *J Biol Chem* 2013;288(29):21399–21411. PMID: 23737532; PMCID: PMC3774407; DOI: 10.1074/jbc.M113.479253.
- **mohamed-2014-hspa4l-hspa4-double-mutant**: Mohamed BA, et al. Respiratory distress and early neonatal lethality in Hspa4l/Hspa4 double-mutant mice. *Am J Respir Cell Mol Biol* 2014;50(4):817–824. PMID: 23980576; DOI: 10.1165/rcmb.2013-0132OC.
- **nillegoda-2015-hsp70-cochaperone-disaggregation**: Nillegoda NB, et al. Crucial HSP70 co-chaperone complex unlocks metazoan protein disaggregation. *Nature* 2015;524:247–251. PMID: 26245380; PMCID: PMC4830470; DOI: 10.1038/nature14884.
- **gao-2015-alpha-synuclein-disaggregase**: Gao X, et al. Human Hsp70 disaggregase reverses Parkinson's-linked α-synuclein amyloid fibrils. *Mol Cell* 2015;59(5):781–793. PMID: 26300264; PMCID: PMC5072489; DOI: 10.1016/j.molcel.2015.07.012.
- **bracher-2015-hsp70-nef-review**: Bracher A, Verghese J. The nucleotide exchange factors of Hsp70 molecular chaperones. *Front Mol Biosci* 2015;2:10. PMID: 26913285; PMCID: PMC4753570; DOI: 10.3389/fmolb.2015.00010.
- **adachi-2015-hspa4-ibd**: Adachi T, et al. Involvement of heat shock protein A4/Apg-2 in refractory inflammatory bowel disease. *Inflamm Bowel Dis* 2015;21(1):31–39. PMID: 25437815; PMCID: PMC4894780; DOI: 10.1097/MIB.0000000000000244.
- **sakurai-2015-hspa4-gastric-ulcer**: Sakurai T, et al. Heat shock protein A4 controls cell migration and gastric ulcer healing. *Dig Dis Sci* 2015;60(4):850–857. PMID: 25655005; DOI: 10.1007/s10620-015-3561-8.
- **elkenani-2022-hspa4-skeletal-myopathy**: Elkenani M, et al. Heat shock protein A4 ablation leads to skeletal muscle myopathy associated with dysregulated autophagy and induced apoptosis. *J Transl Med* 2022;20:229. PMID: 35568953; PMCID: PMC9107738; DOI: 10.1186/s12967-022-03418-3.
- **su-2025-yili-horse-transcriptome**: Su Y, et al. Comparative analysis of blood whole transcriptome profiles in Yili horses pre- and post-5000-meter racing. *Front Genet* 2025;16:1651628. PMID: 40949872; PMCID: PMC12425706; DOI: 10.3389/fgene.2025.1651628.
- **refseq-horse-HSPA4-proteins**: NCBI RefSeq predicted proteins for horse HSPA4: XP_001918259.2 (isoform X1, 840 aa), XP_023473466.1 and XP_070090444.1 (isoform X2, 735 aa). Retrieved via NCBI E-utilities (db=protein, query HSPA4[gene] AND Equus caballus[orgn] AND refseq[filter]).
- **andreasson-2008-hsp110-hsp70-dynamics**: Andréasson C, Fiaux J, Rampelt H, Druffel-Augustin S, Bukau B. Insights into the structural dynamics of the Hsp110-Hsp70 interaction reveal the mechanism for nucleotide exchange activity. *Proc Natl Acad Sci U S A* 2008;105(43):16519–16524. PMID: 18948593; PMCID: PMC2575452; DOI: 10.1073/pnas.0804187105.
- **scior-2018-htt-trimeric-chaperone**: Scior A, et al. Complete suppression of Htt fibrilization and disaggregation of Htt fibrils by a trimeric chaperone complex. *EMBO J* 2018;37(2):282–299. PMID: 29212816; PMCID: PMC5770855; DOI: 10.15252/embj.201797212.
- **nachman-2020-tau-disaggregation**: Nachman E, Wentink AS, et al. Disassembly of Tau fibrils by the human Hsp70 disaggregation machinery generates small seeding-competent species. *J Biol Chem* 2020;295(28):9676–9690. PMID: 32467226; PMCID: PMC7363153; DOI: 10.1074/jbc.RA120.013478.
- **wentink-2020-amyloid-disaggregation-hsp70**: Wentink AS, Nillegoda NB, et al. Molecular dissection of amyloid disaggregation by human HSP70. *Nature* 2020;587(7834):483–488. PMID: 33177717; DOI: 10.1038/s41586-020-2904-6.
- **beton-2022-amyloid-hsp70-disaggregase**: Beton JG, Monistrol J, et al. Cooperative amyloid fibre binding and disassembly by the Hsp70 disaggregase. *EMBO J* 2022;41(16):e110410. PMID: 35698800; PMCID: PMC9379549; DOI: 10.15252/embj.2021110410.
- **rios-2026-drosophila-hsp110**: Rios B, Xu S, Farmer SM, Ye X, Ye L, Morano KA, Zhang S. Nervous System Integrity in Drosophila: Essential and Dosage-Sensitive Roles of Hsp110. *Genetics* 2026 (online ahead of print), iyag240. PMID: 42703001; DOI: 10.1093/genetics/iyag240.


## Citations

1. adachi-2015-hspa4-ibd-abstract.md
2. adachi-2015-hspa4-ibd-fulltext.txt
3. adachi-2015-hspa4-ibd-summary.md
4. aijaz-2007-apg2-tight-junction-abstract.md
5. aijaz-2007-apg2-tight-junction-fulltext.txt
6. aijaz-2007-apg2-tight-junction-summary.md
7. andreasson-2008-hsp110-hsp70-dynamics-abstract.md
8. andreasson-2008-hsp110-hsp70-dynamics-summary.md
9. beton-2022-amyloid-hsp70-disaggregase-abstract.md
10. beton-2022-amyloid-hsp70-disaggregase-fulltext.txt
11. beton-2022-amyloid-hsp70-disaggregase-summary.md
12. bracher-2015-hsp70-nef-review-abstract.md
13. bracher-2015-hsp70-nef-review-fulltext.txt
14. bracher-2015-hsp70-nef-review-summary.md
15. dragovic-2006-hsp110-nef-abstract.md
16. dragovic-2006-hsp110-nef-summary.md
17. easton-2000-hsp110-grp170-abstract.md
18. easton-2000-hsp110-grp170-summary.md
19. elkenani-2022-hspa4-skeletal-myopathy-abstract.md
20. elkenani-2022-hspa4-skeletal-myopathy-fulltext.txt
21. elkenani-2022-hspa4-skeletal-myopathy-summary.md
22. gao-2015-alpha-synuclein-disaggregase-abstract.md
23. gao-2015-alpha-synuclein-disaggregase-fulltext.txt
24. gao-2015-alpha-synuclein-disaggregase-summary.md
25. gotoh-2004-apg2-chaperone-hcc-abstract.md
26. gotoh-2004-apg2-chaperone-hcc-summary.md
27. held-2011-hspa4-spermatogenesis-abstract.md
28. held-2011-hspa4-spermatogenesis-summary.md
29. kampinga-2009-hsp-nomenclature-abstract.md
30. kampinga-2009-hsp-nomenclature-summary.md
31. kaneko-1997-apg2-cloning-abstract.md
32. kaneko-1997-apg2-cloning-summary.md
33. mattoo-2013-hsp110-unfoldase-abstract.md
34. mattoo-2013-hsp110-unfoldase-summary.md
35. mohamed-2012-hspa4-cardiac-hypertrophy-abstract.md
36. mohamed-2012-hspa4-cardiac-hypertrophy-summary.md
37. mohamed-2014-hspa4l-hspa4-double-mutant-abstract.md
38. mohamed-2014-hspa4l-hspa4-double-mutant-summary.md
39. nachman-2020-tau-disaggregation-abstract.md
40. nachman-2020-tau-disaggregation-fulltext.txt
41. nachman-2020-tau-disaggregation-summary.md
42. nillegoda-2015-hsp70-cochaperone-disaggregation-abstract.md
43. nillegoda-2015-hsp70-cochaperone-disaggregation-fulltext.txt
44. nillegoda-2015-hsp70-cochaperone-disaggregation-summary.md
45. oh-1997-hsp110-thermoresistance-abstract.md
46. oh-1997-hsp110-thermoresistance-summary.md
47. polier-2008-hsp70-hsp110-structure-abstract.md
48. polier-2008-hsp70-hsp110-structure-summary.md
49. rampelt-2012-hsp110-disaggregation-abstract.md
50. rampelt-2012-hsp110-disaggregation-summary.md
51. raviol-2006-human-yeast-hsp110-abstract.md
52. raviol-2006-human-yeast-hsp110-summary.md
53. raviol-2006-yeast-hsp110-nef-abstract.md
54. raviol-2006-yeast-hsp110-nef-summary.md
55. refseq-horse-HSPA4-proteins-summary.md
56. refseq-horse-HSPA4-proteins.fasta
57. rios-2026-drosophila-hsp110-abstract.md
58. rios-2026-drosophila-hsp110-summary.md
59. sakurai-2015-hspa4-gastric-ulcer-abstract.md
60. sakurai-2015-hspa4-gastric-ulcer-summary.md
61. schuermann-2008-hsp110-hsc70-structure-abstract.md
62. schuermann-2008-hsp110-hsc70-structure-summary.md
63. scior-2018-htt-trimeric-chaperone-abstract.md
64. scior-2018-htt-trimeric-chaperone-summary.md
65. shorter-2011-mammalian-disaggregase-abstract.md
66. shorter-2011-mammalian-disaggregase-fulltext.txt
67. shorter-2011-mammalian-disaggregase-summary.md
68. su-2025-yili-horse-transcriptome-abstract.md
69. su-2025-yili-horse-transcriptome-fulltext.txt
70. su-2025-yili-horse-transcriptome-summary.md
71. tsapara-2006-apg2-zo1-zonab-abstract.md
72. tsapara-2006-apg2-zo1-zonab-summary.md
73. uniprot-A0A9L0S5Z5-entry.fasta
74. uniprot-A0A9L0S5Z5-entry.txt
75. uniprot-A0A9L0S5Z5-summary.md
76. uniprot-P34932-human-HSPA4-entry.fasta
77. uniprot-P34932-human-HSPA4-entry.txt
78. uniprot-P34932-human-HSPA4-summary.md
79. wade-2009-horse-genome-abstract.md
80. wade-2009-horse-genome-fulltext.txt
81. wade-2009-horse-genome-summary.md
82. wentink-2020-amyloid-disaggregation-hsp70-abstract.md
83. wentink-2020-amyloid-disaggregation-hsp70-summary.md