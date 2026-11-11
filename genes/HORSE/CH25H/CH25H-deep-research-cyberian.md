---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T04:12:01.478071'
end_time: '2026-10-26T04:23:57.185430'
duration_seconds: 715.71
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: CH25H
  gene_symbol: CH25H
  uniprot_accession: F6T000
  protein_description: 'SubName: Full=Cholesterol 25-hydroxylase {ECO:0000313|Ensembl:ENSECAP00000003097.2};'
  gene_info: Name=CH25H {ECO:0000313|Ensembl:ENSECAP00000003097.2};
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: Fatty_acid_hydroxylase. (IPR006694); Sterol_desaturase-rel. (IPR050307);
    FA_hydroxylase (PF04116)
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    agent_type: claude
    port: 3311
    skip_permissions: true
    manage_server: true
    workdir_base: /Users/cjm/.cache/drc-cyberian-work
citation_count: 63
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** F6T000
- **Protein Description:** SubName: Full=Cholesterol 25-hydroxylase {ECO:0000313|Ensembl:ENSECAP00000003097.2};
- **Gene Information:** Name=CH25H {ECO:0000313|Ensembl:ENSECAP00000003097.2};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Fatty_acid_hydroxylase. (IPR006694); Sterol_desaturase-rel. (IPR050307); FA_hydroxylase (PF04116)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CH25H" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CH25H' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CH25H** (gene ID: CH25H, UniProt: F6T000) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Cholesterol 25-hydroxylase (CH25H) of the horse (*Equus caballus*; UniProt F6T000): function, localization and pathways

## 1. Introduction and summary

The horse protein F6T000 is an unreviewed TrEMBL entry of 270 amino acids, automatically annotated from the Ensembl gene ENSECAG00000004572 on horse chromosome 1 and derived from the Thoroughbred reference genome [uniprot-F6T000-entry][wade-2009-horse-genome-abstract]. It is named cholesterol 25-hydroxylase (CH25H) and carries a single FA_hydroxylase (Pfam PF04116) domain, placing it in the sterol desaturase / fatty acid hydroxylase superfamily of membrane-bound di-iron oxidases [uniprot-F6T000-entry]. Identity verification is unambiguous: Ensembl Compara classifies the horse gene as a one-to-one ortholog of human CH25H (82.6% identity) and of mouse Ch25h (78.9% identity) [ensembl-ENSECAG00000004572-orthologs], and the horse sequence retains all three histidine-box motifs that coordinate the di-iron center in the experimentally characterized human and mouse enzymes (see Section 2). There is no confusion with another gene sharing the symbol; however, there is essentially no experimental literature on the horse protein itself. The only horse-specific mention found is a transcriptomic study of equine keratinocytes in which CH25H was marginally downregulated, a result the authors themselves flagged as possibly artifactual [cvitas-2022-equine-keratinocytes-ibh-fulltext]. Two equine cell-based antiviral screens tested exogenous 25-HC and found no activity against West Nile virus or equid herpesvirus 4 [cochet-2024-equine-ipsc-wnv-screen-fulltext][normand-2024-ehv4-antiviral-screen-fulltext], but neither examined the horse enzyme. A high-confidence AlphaFold model of F6T000, in which the three catalytic histidine boxes converge into a single cluster, adds structural support for a conserved di-iron active site [alphafold-F6T000-structure-analysis-summary]. Everything below about function is therefore inferred from orthologs (chiefly human and mouse), and the strength of that inference rests on high sequence conservation and conservation of catalytic residues.

On that basis, horse CH25H is predicted to be an endoplasmic reticulum (ER)-resident, multi-pass integral membrane enzyme that hydroxylates cholesterol at carbon 25 to produce 25-hydroxycholesterol (25-HC), using molecular oxygen, a reductant and a non-heme di-iron cofactor; it is not a cytochrome P450 [lund-1998-ch25h-cloning-abstract][rahman-2026-ch25h-inhibitors-abstract][uniprot-O95992-human-CH25H-entry]. Its product 25-HC is a potent regulatory oxysterol that binds INSIG proteins to block SREBP processing and cholesterol synthesis [radhakrishnan-2007-oxysterol-insig-abstract][lund-1998-ch25h-cloning-abstract], activates ACAT to deplete the "accessible" pool of plasma-membrane cholesterol [abrams-2020-oxysterols-accessible-cholesterol-abstract][wang-2020-ch25h-sarscov2-abstract], and is the precursor (via CYP7B1) of 7α,25-dihydroxycholesterol, the chemoattractant ligand of the G protein-coupled receptor EBI2/GPR183 [hannedouche-2011-oxysterols-ebi2-abstract][yi-2012-oxysterol-gradient-abstract]. In mammals CH25H is an interferon- and Toll-like receptor-inducible gene of macrophages and dendritic cells, and its product mediates broad antiviral and antibacterial defense, restrains IL-1-driven inflammation, and positions B cells in lymphoid tissue [park-2010-ch25h-interferon-abstract][blanc-2013-stat1-25hc-abstract][liu-2013-ch25h-viral-entry-abstract][reboldi-2014-25hc-il1-abstract][cyster-2014-25hc-immunity-review-abstract].

## 2. Identity, gene structure and sequence features of horse CH25H

The F6T000 sequence (270 residues) can be compared directly with reviewed human CH25H (O95992, 272 residues). In a simple position-by-position comparison over the shared length, 83% of residues are identical, in close agreement with the 82.6% identity reported by Ensembl Compara for the one-to-one ortholog pair [uniprot-F6T000-entry][uniprot-O95992-human-CH25H-entry][ensembl-ENSECAG00000004572-orthologs]. The differences cluster at the extreme N- and C-termini; the central catalytic region is nearly invariant. The three histidine boxes characteristic of the di-iron hydroxylase family are present in the horse sequence as H143-VLHH (box 1; human HLLHH), H157-KMHHQ (box 2; human HKVHHQ) and HHDLHH at residues 238–243 (box 3, identical to human) [uniprot-F6T000-entry][uniprot-O95992-human-CH25H-entry]. Lund and colleagues showed at the cloning of mouse and human CH25H that such histidine clusters are essential for catalytic activity [lund-1998-ch25h-cloning-abstract], and later work confirmed that mutating the two terminal histidines of box 3 (H242Q/H243Q in the numbering used for mouse Ch25h, the same paired histidines of the HHDLHH motif) abolishes 25-HC production [rahman-2026-ch25h-inhibitors-fulltext][zang-2020-ch25h-sarscov2-fusion-fulltext]. Because horse CH25H retains the HHDLHH motif with these histidines at positions 242–243, it is expected to be catalytically competent.

The predicted three-dimensional structure supports the same conclusion. UniProt's automatic sequence analysis (Phobius) predicts four transmembrane helices in F6T000 (residues 38–62, 92–112, 124–145 and 166–185) and places the fatty acid hydroxylase domain at residues 128–263 [uniprot-F6T000-entry]. The AlphaFold model of the horse protein (AF-F6T000-F1) is predicted with high confidence overall (mean pLDDT 91.1, with 85% of residues above 90), and every histidine in the three boxes is modelled with pLDDT above 96 [alphafold-F6T000-prediction][alphafold-F6T000-structure-analysis-summary]. In my own measurement of this model, eight of the ten box histidines (H143, H147, H157, H160, H161, H239, H242 and H243) point their imidazole NE2 atoms to within about 2–5 Å of a common centroid, even though they are spread over 100 residues of sequence [alphafold-F6T000-structure-analysis-summary]. The three His boxes thus converge into one compact histidine cluster at the membrane interface, the arrangement expected for a non-heme di-iron site in this enzyme family [lund-1998-ch25h-cloning-abstract]. This is a computational prediction and not an experimental structure, but it independently supports the view that the horse protein has a functional catalytic center.

Gene architecture is also conserved. The human and mouse CH25H genes lack introns [lund-1998-ch25h-cloning-abstract]. In the horse, the Ensembl transcript ENSECAT00000004474 has three exons spanning chromosome 1:39,447,354–39,450,445, but the entire 270-codon open reading frame (chr1:39,448,004–39,448,816) lies within the second exon, so the coding region is likewise uninterrupted [ensembl-ENSECAT00000004474-lookup]. UniProt's automatic annotation assigns only a generic "membrane" location to F6T000 [uniprot-F6T000-entry], whereas the reviewed human entry, based on the mouse ortholog, specifies ER membrane, multi-pass [uniprot-O95992-human-CH25H-entry].

## 3. Enzymatic activity, cofactor and substrate specificity

CH25H catalyzes the reaction cholesterol + AH2 + O2 → 25-hydroxycholesterol + A + H2O (EC 1.14.99.38; Rhea:21104), and UniProt also records an NADPH-dependent form of the reaction on the basis of the original characterization [uniprot-O95992-human-CH25H-entry][lund-1998-ch25h-cloning-abstract]. The horse entry already carries the IBA (phylogenetically inferred) GO annotation "cholesterol 25-hydroxylase activity" [uniprot-F6T000-entry]. Mechanistically the enzyme is unusual among sterol hydroxylases: rather than a heme-thiolate cytochrome P450 such as CYP27A1 or CYP3A4, it belongs to a small family of enzymes that use a di-iron cofactor bound by histidine boxes to hydroxylate hydrophobic substrates [lund-1998-ch25h-cloning-abstract]. Its closest relatives are other ER di-iron lipid oxidases of cholesterol biosynthesis, notably the sterol C4-methyl oxidase SC4MOL (MSMO1) and the sterol C5-desaturase SC5D, which are described as phylogenetically close to CH25H [rahman-2026-ch25h-inhibitors-fulltext]. This evolutionary relationship explains the "Sterol_desaturase-related" InterPro family assignment of F6T000 [uniprot-F6T000-entry].

With respect to substrate specificity, the defining substrate is cholesterol, hydroxylated on the side chain at C25. When macrophages are stimulated with interferon or infected, comprehensive oxysterol profiling identified 25-HC as the only oxysterol that these cells synthesize and secrete [blanc-2013-stat1-25hc-abstract], supporting a high regiospecificity in vivo. Catalytic activity in cells can be blocked by iron chelators (ciclopirox, 1,10-phenanthroline), consistent with an iron-dependent mechanism, and by the aminosteroid U73343, which spares SC4MOL and SC5D, indicating that the substrate-binding pocket differs sufficiently from its nearest family members to permit selective inhibition [rahman-2026-ch25h-inhibitors-abstract][rahman-2026-ch25h-inhibitors-fulltext]. No experimental three-dimensional structure of any CH25H ortholog was identified; the horse entry is linked to an AlphaFold model only (Section 2) [uniprot-F6T000-entry]. The enzyme is described as a challenging ER-resident transmembrane protein to study biochemically, and the human protein is N-glycosylated [rahman-2026-ch25h-inhibitors-abstract][uniprot-O95992-human-CH25H-entry].

## 4. Subcellular localization and the site of action of its product

CH25H itself is an ER-resident polytopic membrane protein [lund-1998-ch25h-cloning-abstract][rahman-2026-ch25h-inhibitors-abstract], so cholesterol hydroxylation is expected to occur in the ER membrane of horse cells as well. Its product, however, acts in several compartments and also outside the producing cell. 25-HC is secreted by activated macrophages and acts as a paracrine factor on neighboring cells [blanc-2013-stat1-25hc-abstract][bauman-2009-25hc-iga-abstract], and LPS administration to humans raises plasma 25-HC concentration [diczfalusy-2009-ch25h-lps-abstract]. Within target cells, 25-HC binds the ER proteins INSIG-1/2, retaining SCAP–SREBP in the ER [radhakrishnan-2007-oxysterol-insig-abstract]; activates ER-localized ACAT, which esterifies and thereby removes accessible cholesterol from the plasma membrane [abrams-2020-oxysterols-accessible-cholesterol-abstract][wang-2020-ch25h-sarscov2-abstract]; and accumulates in late endosomes, where it impedes cholesterol export [zang-2020-ch25h-sarscov2-fusion-abstract]. When converted by CYP7B1 to 7α,25-dihydroxycholesterol, it becomes an extracellular chemoattractant gradient in lymphoid follicles [yi-2012-oxysterol-gradient-abstract]. Thus the enzyme's own location (ER membrane) is distinct from the many sites at which its metabolite acts.

## 5. Pathway context I: sterol homeostasis

The first biological role ascribed to CH25H was in cholesterol feedback regulation. Expression of CH25H in cultured cells reduces cholesterol synthesis from acetate and suppresses the proteolytic cleavage of SREBP-1 and SREBP-2, suggesting the enzyme produces a co-repressor of SREBP processing [lund-1998-ch25h-cloning-abstract]. The molecular basis of this repression was later explained by the finding that oxysterols, including 25-HC, act by binding INSIG proteins via their third and fourth transmembrane helices, causing INSIG to bind SCAP and blocking ER-to-Golgi transport of SREBPs [radhakrishnan-2007-oxysterol-insig-abstract]. In parallel, 25-HC is described as an endogenous ligand of the liver X receptors (LXRs), which induce cholesterol efflux genes [liang-2026-ch25h-antiviral-review-fulltext], and it activates ACAT to promote cholesterol esterification and depletion of accessible membrane cholesterol [abrams-2020-oxysterols-accessible-cholesterol-abstract]. In the CH25H-deficient macrophage, failure of this circuit leaves SREBP2 active and cholesterol synthesis high [dang-2017-oxysterol-aim2-abstract][reboldi-2014-25hc-il1-abstract]. 25-HC itself is further metabolized by the oxysterol 7α-hydroxylase CYP7B1, which degrades 25-HC in the context of immune regulation and simultaneously generates the EBI2 ligand [bauman-2009-25hc-iga-abstract][yi-2012-oxysterol-gradient-abstract]. Whether these sterol-regulatory effects are prominent in horse liver or other tissues has not been examined; the basal expression of the murine gene is low in most tissues [lund-1998-ch25h-cloning-abstract], and Bgee lists horse expression in synovial membrane and a limited set of other tissues [uniprot-F6T000-entry].

## 6. Pathway context II: innate immunity, antiviral and antibacterial defense, and inflammation

In mammals CH25H is best understood as an inducible immune gene. LPS increases Ch25h expression roughly 35-fold within two hours in mouse bone-marrow macrophages via TLR4 in a MyD88-independent manner [diczfalusy-2009-ch25h-lps-abstract]. Park and Scott showed that TLR3- and TLR4-driven induction in dendritic cells and macrophages depends on TRIF-dependent type I interferon production, IFNAR and the JAK–STAT1 pathway, and that IFN-α, IFN-β and IFN-γ each induce Ch25h through STAT1 [park-2010-ch25h-interferon-abstract]. Blanc and colleagues showed that STAT1 binds the Ch25h locus directly, establishing CH25H as a bona fide interferon-stimulated gene [blanc-2013-stat1-25hc-abstract].

The antiviral function of CH25H was established in parallel studies. Liu and colleagues identified CH25H as a broadly antiviral ISG whose product 25-HC inhibited a wide array of enveloped viruses, including VSV, HSV, HIV, MHV68, Ebola, Rift Valley fever and Nipah viruses, by blocking fusion between the viral and cellular membranes; Ch25h-deficient mice were more susceptible to MHV68 [liu-2013-ch25h-viral-entry-abstract]. During the COVID-19 pandemic, two groups showed that CH25H is induced by SARS-CoV-2 and that 25-HC blocks spike-mediated membrane fusion, one attributing this to ACAT-driven depletion of accessible plasma-membrane cholesterol [wang-2020-ch25h-sarscov2-abstract] and the other to accumulation of 25-HC in late endosomes and blockade of cholesterol export [zang-2020-ch25h-sarscov2-fusion-abstract]. Importantly for the question of whether antiviral activity derives from catalysis, a histidine-box mutant of CH25H failed to make 25-HC or 7α,25-diHC [zang-2020-ch25h-sarscov2-fusion-fulltext]. The same accessible-cholesterol mechanism protects cells against the intracellular bacteria *Listeria monocytogenes* and *Shigella flexneri*, which exploit that cholesterol pool to spread [abrams-2020-oxysterols-accessible-cholesterol-abstract]. Viral countermeasures and the dynamic regulation of this axis in RNA virus infections have recently been reviewed [liang-2026-ch25h-antiviral-review-abstract].

CH25H also provides negative feedback on inflammation. Ch25h-deficient macrophages overproduce IL-1 family cytokines because 25-HC normally antagonizes SREBP processing to reduce Il1b transcription and represses inflammasome activity; Ch25h-null mice are more sensitive to septic shock and develop worse experimental autoimmune encephalomyelitis [reboldi-2014-25hc-il1-abstract]. A follow-up study showed that the relevant inflammasome is AIM2: without 25-HC, macrophage cholesterol rises, mitochondrial respiration falters, mitochondrial DNA leaks into the cytosol, and AIM2 is activated, a phenotype rescued by AIM2 deficiency [dang-2017-oxysterol-aim2-abstract]. These studies place CH25H downstream of type I interferon as the link between interferon signaling and suppression of IL-1β.

## 7. Pathway context III: adaptive immunity and the EBI2 oxysterol axis

25-HC is the obligate intermediate in synthesis of 7α,25-dihydroxycholesterol, which is produced by sequential action of CH25H and CYP7B1 and inactivated by HSD3B7 [yi-2012-oxysterol-gradient-abstract]. Two groups independently identified 7α,25-diHC as the high-affinity endogenous agonist of EBI2/GPR183 (dissociation constant ~450 pM), a chemotactic receptor that directs migration of B and T cells [hannedouche-2011-oxysterols-ebi2-abstract][liu-2011-oxysterols-ebi2-abstract]. Ch25h-deficient mice, like EBI2-deficient mice, fail to position activated B cells in the outer follicle of the spleen and mount reduced plasma-cell responses [hannedouche-2011-oxysterols-ebi2-abstract]. Lymphoid stromal cells at the follicle perimeter are the main CH25H- and CYP7B1-expressing cells creating the oxysterol gradient, while CH25H is repressed in follicular dendritic cells [yi-2012-oxysterol-gradient-abstract]. Independently of EBI2, macrophage-derived 25-HC suppresses B-cell proliferation, AID expression and IgA class switching, so that Ch25h-null mice have elevated serum IgA [bauman-2009-25hc-iga-abstract]. These roles in immune-cell guidance and antibody regulation are synthesized in an authoritative review [cyster-2014-25hc-immunity-review-abstract]. In the horse, UniProt contains gene-model entries for GPR183 (F6VPM1) and CYP7B1 (F7BTH5, annotated as 25/26-hydroxycholesterol 7α-hydroxylase), so the enzymes and receptor needed to make and sense 7α,25-diHC appear to be present; a horse HSD3B7 entry was not found by the same search, which may reflect incomplete annotation rather than absence [uniprot-horse-ebi2-axis-genes-search]. The equine EBI2 axis has not been studied experimentally.

## 8. Relevance to the horse and annotation implications

No study has measured 25-HC production by horse CH25H, determined its localization in equine cells, or tested its induction by interferon in horse macrophages. Two equine antiviral screens are relevant, although they tested exogenous 25-HC rather than the horse enzyme. In equine induced pluripotent stem cell-derived neural progenitor cells infected with West Nile virus, 25-HC was cytotoxic at 10 µM and had no antiviral activity at the non-toxic dose of 1 µM [cochet-2024-equine-ipsc-wnv-screen-fulltext]. In equine dermal fibroblasts infected with equid herpesvirus 4, 25-HC was also among the compounds with no antiviral effect, a result the authors found surprising given its activity against other viruses [normand-2024-ehv4-antiviral-screen-fulltext]. These negative results come from single compound screens in cell lines that may lack the relevant cholesterol-handling machinery, but they caution against assuming that the broad antiviral activity of 25-HC in human and mouse cells carries over to every equine virus–cell combination; the WNV study explicitly stresses that drug effects in human or rodent cells may not transpose to equine cells [cochet-2024-equine-ipsc-wnv-screen-abstract]. The only equine data point on the gene itself is transcriptomic: in keratinocytes from horses with insect bite hypersensitivity, CH25H was among genes downregulated after stimulation, but with a false discovery rate close to 5% that the authors considered potentially artifactual [cvitas-2022-equine-keratinocytes-ibh-fulltext]. The case for functional annotation of F6T000 therefore rests on orthology: a one-to-one ortholog relationship with experimentally characterized human and mouse enzymes [ensembl-ENSECAG00000004572-orthologs], ~83% sequence identity, a high-confidence predicted fold in which the three histidine boxes converge into a putative di-iron site [alphafold-F6T000-structure-analysis-summary], full conservation of the three histidine-box motifs including the HHDLHH box whose histidines are required for activity [rahman-2026-ch25h-inhibitors-fulltext][zang-2020-ch25h-sarscov2-fusion-fulltext], and conserved intronless coding structure [ensembl-ENSECAT00000004474-lookup][lund-1998-ch25h-cloning-abstract]. Reasonable inferred annotations are: molecular function cholesterol 25-hydroxylase activity (GO:0001567, already IBA) and iron ion binding; cellular component endoplasmic reticulum membrane (more specific than the current generic "membrane"); and biological processes cholesterol metabolic process, negative regulation of SREBP signaling/cholesterol biosynthesis, response to type I interferon, defense response to virus/negative regulation of viral entry, and B cell chemotaxis via 7α,25-diHC production. The immune process annotations should be regarded as lower-confidence for the horse because they depend on inducible expression and downstream partners whose regulation in horses is unexamined.

## Open Questions

The most basic open question is direct biochemical confirmation that horse CH25H converts cholesterol to 25-HC, which could be tested by expressing the F6T000 coding sequence in HEK293 cells and measuring 25-HC by GC-MS or LC-MS, using an HHDLHH-box H242Q/H243Q mutant as a control, as was done for mouse and human enzymes [rahman-2026-ch25h-inhibitors-fulltext][zang-2020-ch25h-sarscov2-fusion-fulltext]. A second question is whether the horse gene is interferon-inducible through STAT1 as in mouse [park-2010-ch25h-interferon-abstract][blanc-2013-stat1-25hc-abstract]; examining the promoter for STAT1/ISRE elements and measuring induction in equine monocyte-derived macrophages after IFN or LPS would address this. Third, it remains unclear whether 25-HC restricts equine pathogens. It is broadly active against enveloped viruses in other species [liu-2013-ch25h-viral-entry-abstract], yet two equine screens found no activity of exogenous 25-HC against West Nile virus in equine neural progenitors or against EHV-4 in equine fibroblasts [cochet-2024-equine-ipsc-wnv-screen-fulltext][normand-2024-ehv4-antiviral-screen-fulltext]. Dose-response studies in physiologically relevant equine cells (respiratory epithelium, macrophages), with endogenous CH25H overexpression or knockout rather than added sterol, and with other viruses such as equine influenza and equine arteritis virus, would resolve whether this is a cell-type, virus or species difference. Fourth, the high Bgee expression in synovial membrane noted in the horse entry [uniprot-F6T000-entry] is intriguing in light of interest in CH25H in osteoarthritis [rahman-2026-ch25h-inhibitors-abstract]; horses are a major model and patient population for osteoarthritis, so whether CH25H/25-HC contributes to equine joint inflammation is a tractable question. Finally, the equine EBI2 axis (CH25H, CYP7B1, HSD3B7, GPR183) and the precise localization of the horse protein (ER versus other membranes) remain unstudied, and an experimental structure of any CH25H ortholog would clarify the basis of its C25 regiospecificity.

## References

- [uniprot-F6T000-entry] UniProtKB/TrEMBL entry F6T000_HORSE, Cholesterol 25-hydroxylase, *Equus caballus* (entry version 75, 02-Sep-2026). https://rest.uniprot.org/uniprotkb/F6T000.txt
- [uniprot-O95992-human-CH25H-entry] UniProtKB/Swiss-Prot entry O95992 (CH25H_HUMAN). https://rest.uniprot.org/uniprotkb/O95992.txt
- [ensembl-ENSECAT00000004474-lookup] Ensembl REST lookup of horse transcript ENSECAT00000004474 (CH25H-201). https://rest.ensembl.org/lookup/id/ENSECAT00000004474?expand=1
- [ensembl-ENSECAG00000004572-orthologs] Ensembl Compara orthologues of horse gene ENSECAG00000004572. https://rest.ensembl.org/homology/id/horse/ENSECAG00000004572?type=orthologues
- [wade-2009-horse-genome] Wade CM, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. Science 2009;326:865-867. PMID:19892987; PMCID:PMC3785132; DOI:10.1126/science.1178158
- [lund-1998-ch25h-cloning] Lund EG, Kerr TA, Sakai J, Li WP, Russell DW. cDNA cloning of mouse and human cholesterol 25-hydroxylases, polytopic membrane proteins that synthesize a potent oxysterol regulator of lipid metabolism. J Biol Chem 1998. PMID:9852097; DOI:10.1074/jbc.273.51.34316
- [radhakrishnan-2007-oxysterol-insig] Radhakrishnan A, Ikeda Y, Kwon HJ, Brown MS, Goldstein JL. Sterol-regulated transport of SREBPs from endoplasmic reticulum to Golgi: oxysterols block transport by binding to Insig. Proc Natl Acad Sci USA 2007. PMID:17428920; PMCID:PMC1851665; DOI:10.1073/pnas.0700899104
- [bauman-2009-25hc-iga] Bauman DR, Bitmansour AD, McDonald JG, et al. 25-Hydroxycholesterol secreted by macrophages in response to Toll-like receptor activation suppresses immunoglobulin A production. Proc Natl Acad Sci USA 2009. PMID:19805370; PMCID:PMC2757821; DOI:10.1073/pnas.0909142106
- [diczfalusy-2009-ch25h-lps] Diczfalusy U, Olofsson KE, Carlsson AM, et al. Marked upregulation of cholesterol 25-hydroxylase expression by lipopolysaccharide. J Lipid Res 2009. PMID:19502589; PMCID:PMC2759831; DOI:10.1194/jlr.m900107-jlr200
- [park-2010-ch25h-interferon] Park K, Scott AL. Cholesterol 25-hydroxylase production by dendritic cells and macrophages is regulated by type I interferons. J Leukoc Biol 2010. PMID:20699362; PMCID:PMC2996899; DOI:10.1189/jlb.0610318
- [hannedouche-2011-oxysterols-ebi2] Hannedouche S, Zhang J, Yi T, et al. Oxysterols direct immune cell migration via EBI2. Nature 2011. PMID:21796212; PMCID:PMC4297623; DOI:10.1038/nature10280
- [liu-2011-oxysterols-ebi2] Liu C, Yang XV, Wu J, et al. Oxysterols direct B-cell migration through EBI2. Nature 2011. PMID:21796211; DOI:10.1038/nature10226
- [yi-2012-oxysterol-gradient] Yi T, Wang X, Kelly LM, et al. Oxysterol gradient generation by lymphoid stromal cells guides activated B cell movement during humoral responses. Immunity 2012. PMID:22999953; PMCID:PMC3465460; DOI:10.1016/j.immuni.2012.06.015
- [blanc-2013-stat1-25hc] Blanc M, Hsieh WY, Robertson KA, et al. The transcription factor STAT-1 couples macrophage synthesis of 25-hydroxycholesterol to the interferon antiviral response. Immunity 2013. PMID:23273843; PMCID:PMC3556782; DOI:10.1016/j.immuni.2012.11.004
- [liu-2013-ch25h-viral-entry] Liu SY, Aliyari R, Chikere K, et al. Interferon-inducible cholesterol-25-hydroxylase broadly inhibits viral entry by production of 25-hydroxycholesterol. Immunity 2013. PMID:23273844; PMCID:PMC3698975; DOI:10.1016/j.immuni.2012.11.005
- [reboldi-2014-25hc-il1] Reboldi A, Dang EV, McDonald JG, et al. 25-Hydroxycholesterol suppresses interleukin-1-driven inflammation downstream of type I interferon. Science 2014. PMID:25104388; PMCID:PMC4289637; DOI:10.1126/science.1254790
- [cyster-2014-25hc-immunity-review] Cyster JG, Dang EV, Reboldi A, Yi T. 25-Hydroxycholesterols in innate and adaptive immunity. Nat Rev Immunol 2014. PMID:25324126; DOI:10.1038/nri3755
- [dang-2017-oxysterol-aim2] Dang EV, McDonald JG, Russell DW, Cyster JG. Oxysterol restraint of cholesterol synthesis prevents AIM2 inflammasome activation. Cell 2017. PMID:29033131; PMCID:PMC5693620; DOI:10.1016/j.cell.2017.09.029
- [abrams-2020-oxysterols-accessible-cholesterol] Abrams ME, Johnson KA, Perelman SS, et al. Oxysterols provide innate immunity to bacterial infection by mobilizing cell surface accessible cholesterol. Nat Microbiol 2020. PMID:32284563; PMCID:PMC7442315; DOI:10.1038/s41564-020-0701-5
- [wang-2020-ch25h-sarscov2] Wang S, Li W, Hui H, et al. Cholesterol 25-Hydroxylase inhibits SARS-CoV-2 and other coronaviruses by depleting membrane cholesterol. EMBO J 2020. PMID:32944968; PMCID:PMC7537045; DOI:10.15252/embj.2020106057
- [zang-2020-ch25h-sarscov2-fusion] Zang R, Case JB, Yutuc E, et al. Cholesterol 25-hydroxylase suppresses SARS-CoV-2 replication by blocking membrane fusion. Proc Natl Acad Sci USA 2020. PMID:33239446; PMCID:PMC7749331; DOI:10.1073/pnas.2012197117
- [cochet-2024-equine-ipsc-wnv-screen] Cochet M, Piumi F, Gorna K, Berry N, Gonzalez G, Danckaert A, Aulner N, Blanchet O, et al. An equine iPSC-based phenotypic screening platform identifies pro- and anti-viral molecules against West Nile virus. Vet Res 2024. PMID:38493182; PMCID:PMC10943879; DOI:10.1186/s13567-024-01290-1
- [normand-2024-ehv4-antiviral-screen] Normand C, Thieulent CJ, Fortier C, Sutton G, Senamaud-Beaufort C, Jourdren L, et al. A Screening Study Identified Decitabine as an Inhibitor of Equid Herpesvirus 4 That Enhances the Innate Antiviral Response. Viruses 2024. PMID:38793627; PMCID:PMC11125953; DOI:10.3390/v16050746
- [alphafold-F6T000-prediction] AlphaFold Protein Structure Database entry AF-F6T000-F1 (model v6). https://alphafold.ebi.ac.uk/api/prediction/F6T000 ; model file https://alphafold.ebi.ac.uk/files/AF-F6T000-F1-model_v6.pdb
- [alphafold-F6T000-structure-analysis-summary] Own analysis of the AlphaFold model (His-box geometry, pLDDT) and UniProt feature annotations; see citations/alphafold-F6T000-structure-analysis-summary.md
- [uniprot-F6T000-entry] UniProtKB F6T000 entry in JSON format (sequence features, transmembrane predictions). https://rest.uniprot.org/uniprotkb/F6T000.json
- [uniprot-horse-ebi2-axis-genes-search] UniProtKB searches for horse (taxon 9796) GPR183, CYP7B1 and HSD3B7. https://rest.uniprot.org/uniprotkb/search?query=gene_exact:GPR183+AND+organism_id:9796
- [cvitas-2022-equine-keratinocytes-ibh] Cvitas I, Oberhaensli S, Leeb T, Marti E. Equine keratinocytes in the pathogenesis of insect bite hypersensitivity: Just another brick in the wall? PLoS One 2022. PMID:35913947; PMCID:PMC9342730; DOI:10.1371/journal.pone.0266263
- [rahman-2026-ch25h-inhibitors] Rahman A, Hayes EH, Adams DJ. Mass Spectrometry-Based Screening Reveals Inhibitors of Cholesterol 25-Hydroxylase. ACS Chem Biol 2026. PMID:42284103; PMCID:PMC13386465; DOI:10.1021/acschembio.6c00385
- [liang-2026-ch25h-antiviral-review] Liang Z, Xing S, Chen Y, et al. Dynamic regulatory mechanism of cholesterol 25-hydroxylase-mediated antiviral response in RNA virus infections. Front Cell Infect Microbiol 2026. PMID:42482992; PMCID:PMC13384843; DOI:10.3389/fcimb.2026.1790475



## Citations

1. abrams-2020-oxysterols-accessible-cholesterol-abstract.md
2. abrams-2020-oxysterols-accessible-cholesterol-summary.md
3. alphafold-F6T000-model_v6.pdb
4. alphafold-F6T000-prediction.json
5. alphafold-F6T000-structure-analysis-summary.md
6. bauman-2009-25hc-iga-abstract.md
7. bauman-2009-25hc-iga-summary.md
8. blanc-2013-stat1-25hc-abstract.md
9. blanc-2013-stat1-25hc-fulltext.txt
10. blanc-2013-stat1-25hc-summary.md
11. cochet-2024-equine-ipsc-wnv-screen-abstract.md
12. cochet-2024-equine-ipsc-wnv-screen-fulltext.txt
13. cochet-2024-equine-ipsc-wnv-screen-summary.md
14. cvitas-2022-equine-keratinocytes-ibh-abstract.md
15. cvitas-2022-equine-keratinocytes-ibh-fulltext.txt
16. cvitas-2022-equine-keratinocytes-ibh-summary.md
17. cyster-2014-25hc-immunity-review-abstract.md
18. cyster-2014-25hc-immunity-review-summary.md
19. dang-2017-oxysterol-aim2-abstract.md
20. dang-2017-oxysterol-aim2-summary.md
21. diczfalusy-2009-ch25h-lps-abstract.md
22. diczfalusy-2009-ch25h-lps-summary.md
23. ensembl-ENSECAG00000004572-orthologs.json
24. ensembl-ENSECAT00000004474-lookup.json
25. hannedouche-2011-oxysterols-ebi2-abstract.md
26. hannedouche-2011-oxysterols-ebi2-summary.md
27. liang-2026-ch25h-antiviral-review-abstract.md
28. liang-2026-ch25h-antiviral-review-fulltext.txt
29. liang-2026-ch25h-antiviral-review-summary.md
30. liu-2011-oxysterols-ebi2-abstract.md
31. liu-2011-oxysterols-ebi2-summary.md
32. liu-2013-ch25h-viral-entry-abstract.md
33. liu-2013-ch25h-viral-entry-summary.md
34. lund-1998-ch25h-cloning-abstract.md
35. lund-1998-ch25h-cloning-summary.md
36. normand-2024-ehv4-antiviral-screen-abstract.md
37. normand-2024-ehv4-antiviral-screen-fulltext.txt
38. normand-2024-ehv4-antiviral-screen-summary.md
39. park-2010-ch25h-interferon-abstract.md
40. park-2010-ch25h-interferon-summary.md
41. radhakrishnan-2007-oxysterol-insig-abstract.md
42. radhakrishnan-2007-oxysterol-insig-summary.md
43. rahman-2026-ch25h-inhibitors-abstract.md
44. rahman-2026-ch25h-inhibitors-fulltext.txt
45. rahman-2026-ch25h-inhibitors-summary.md
46. reboldi-2014-25hc-il1-abstract.md
47. reboldi-2014-25hc-il1-summary.md
48. uniprot-F6T000-entry.json
49. uniprot-F6T000-entry.txt
50. uniprot-F6T000.fasta
51. uniprot-O95992-human-CH25H-entry.txt
52. uniprot-O95992-human-CH25H.fasta
53. uniprot-horse-ebi2-axis-genes-search.tsv
54. wade-2009-horse-genome-abstract.md
55. wade-2009-horse-genome-summary.md
56. wang-2020-ch25h-sarscov2-abstract.md
57. wang-2020-ch25h-sarscov2-fulltext.txt
58. wang-2020-ch25h-sarscov2-summary.md
59. yi-2012-oxysterol-gradient-abstract.md
60. yi-2012-oxysterol-gradient-summary.md
61. zang-2020-ch25h-sarscov2-fusion-abstract.md
62. zang-2020-ch25h-sarscov2-fusion-fulltext.txt
63. zang-2020-ch25h-sarscov2-fusion-summary.md