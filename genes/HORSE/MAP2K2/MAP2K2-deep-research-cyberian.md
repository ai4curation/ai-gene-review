---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:44:13.246867'
end_time: '2026-10-26T02:59:25.841331'
duration_seconds: 912.59
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: MAP2K2
  gene_symbol: MAP2K2
  uniprot_accession: A0A9L0SHX8
  protein_description: 'RecName: Full=Serine/threonine-protein {ECO:0000256|PROSITE-ProRule:PRU10027};
    EC=2.7.11.1 {ECO:0000256|PROSITE-ProRule:PRU10027};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the protein kinase superfamily. Ser/Thr protein
  protein_domains: Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase. (IPR050915);
    Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS.
    (IPR008271)
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
citation_count: 89
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0SHX8
- **Protein Description:** RecName: Full=Serine/threonine-protein {ECO:0000256|PROSITE-ProRule:PRU10027}; EC=2.7.11.1 {ECO:0000256|PROSITE-ProRule:PRU10027};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** Kinase-like_dom_sf. (IPR011009); MAP_kinase_kinase. (IPR050915); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441); Ser/Thr_kinase_AS. (IPR008271)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MAP2K2" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MAP2K2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MAP2K2** (gene ID: MAP2K2, UniProt: A0A9L0SHX8) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MAP2K2 (MEK2) in the horse, *Equus caballus*: function, localization and pathway role of UniProt A0A9L0SHX8

## 1. Introduction and summary

UniProt A0A9L0SHX8 is an unreviewed, computationally predicted 390-residue protein from the domestic horse. UniProt names it only "Serine/threonine-protein" (an apparently truncated "serine/threonine-protein kinase") (EC 2.7.11.1). It assigns the entry to the STE group of the protein kinase superfamily and to the MAP kinase kinase subfamily, and the PANTHER subfamily is "mitogen-activated protein kinase kinase 2" [uniprot-A0A9L0SHX8-entry]. The entry comes from the Ensembl annotation of the Thoroughbred reference genome [wade-2009-horse-genome]. The Ensembl gene it belongs to, ENSECAG00000009157 on horse chromosome 7, is named MAP2K2 ("mitogen-activated protein kinase kinase 2", VGNC:59406) [ensembl-ENSECAG00000009157-lookup].

My own pairwise alignments confirm the identification (notes/sequence_analysis.md). Over its full length the horse protein shares 354 identical residues (91%) with human MEK2 (P36507) but only 300 (77%) with human MEK1. Its first 363 residues align to human MEK2 without gaps and differ at only 13 positions. The gene symbol MAP2K2 is therefore unambiguous for this protein, and the large body of literature on mammalian MEK2 applies to it by orthology. Almost no work has been done on MEK2 specifically in the horse, however. The horse-specific evidence below comes from pharmacological studies in equine cells that use MEK1/2 inhibitors, which act on both paralogues.

In summary, MAP2K2 encodes MEK2, a dual-specificity protein kinase. It sits at the centre of the RAS–RAF–MEK–ERK (classical MAPK) cascade, and its only well-established physiological substrates are the MAP kinases ERK1 and ERK2. RAF kinases activate MEK2 by phosphorylating two serines in its activation loop. Active MEK2 then phosphorylates ERK1/2 on both the threonine and the tyrosine of the Thr-Glu-Tyr (TEY) motif, which activates ERK more than 100-fold [zheng-1993-mek1-mek2-cloning; zheng-1994-mek-activation-phosphorylation; roskoski-2012-mek1-2-review]. MEK2 is mostly cytoplasmic. A leucine-rich nuclear export signal keeps it there, and it also shuttles continuously through the nucleus and helps anchor and export ERK [zheng-1994-mek-cytoplasmic-localization; fukuda-1997-mapk-mapkk-interaction; adachi-2000-erk-nuclear-export]. Scaffolds place a fraction of the MEK pool at membranes and endosomes [stewart-1999-ksr-mek-localization; teis-2002-p14-mp1-endosomes]. In mice MEK2 can substitute fully for MEK1 when expressed at the same level [aoidi-2016-mek2-knockin-rescue]. Even so, cell-based studies point to distinct MEK2 outputs, including cytoplasmic retention of the ERK2 it activates and an ERK-independent restraint on macrophage IL-1β production [skarpen-2008-mek1-mek2-erk2-sorting; talwar-2019-mek2-il1b].

A notable feature of this particular isoform is its divergent C-terminus. Its last 27 residues do not match the conserved MEK2 tail, which contains the "DVD" docking site that upstream MAP3Ks use to bind and activate MEKs [takekawa-2005-dvd-docking]. This isoform may therefore be poorly activated by RAF, as discussed in Section 6.

## 2. Gene identity, evolutionary relationships and isoform structure

The mammalian genome contains two ERK-activating MEK genes, MAP2K1 (MEK1) and MAP2K2 (MEK2). Invertebrate models such as *C. elegans*, *Drosophila* and *Xenopus* carry a single Mek gene [belanger-2003-mek2-dispensable]. MEK1 was cloned first, as a 393-residue kinase related to the fission-yeast byr1 gene product [crews-1992-mek-primary-structure]. MEK2 was cloned independently from human, as a 400-residue protein about 80% identical to MEK1 [zheng-1993-mek1-mek2-cloning], and from rat, as MKK2, 81% identical to MKK1 but encoded by a distinct gene with a different tissue distribution [wu-1993-mkk2]. The two paralogues differ mainly in short inserts in the C-terminal lobe, including a proline-rich region [xu-1997-mek1-mek2-differential].

The horse protein A0A9L0SHX8 has all the hallmarks of MEK2 rather than MEK1. Its N-terminal 60 residues are essentially identical to human MEK2 (only T17A differs). The proline-rich insert between residues roughly 270 and 310 is MEK2-like and lacks the threonine equivalent to MEK1 Thr292, the ERK feedback site that is absent from MEK2 [catalanotti-2009-mek1-mek2-heterodimer]. The UniProt features map onto the expected landmarks: a protein kinase domain at residues 72–373, the ATP-binding lysine at Lys101, and the catalytic-loop proton acceptor Asp194 [uniprot-A0A9L0SHX8-entry]. All of these align with the same positions in human MEK2.

The two horse TrEMBL entries for MAP2K2 disagree. The 430-residue entry F6YUU0 has the canonical MEK2 C-terminus (residues 364–400 of human MEK2, with a single G392S change) but a divergent and probably mis-predicted N-terminus [uniprot-F6YUU0-entry]. A0A9L0SHX8 has the reverse problem: a correct N-terminus and kinase core, but the human sequence TNHTFIKRSEVEEVDFAGWLCKTLRLNQPGTPTRTAV is replaced by MQAVTAPPCYVHHRRHSSALLGSPLFM (notes/sequence_analysis.md). The most parsimonious reading is that a full-length, human-like horse MEK2 of about 400 residues exists, and that A0A9L0SHX8 represents an alternative 3′-end transcript (alternative terminal exon or intron retention). That inference awaits transcript-level confirmation.

## 3. Catalytic activity and substrate specificity

MEK2 is a dual-specificity kinase. Although UniProt's automatic pipeline gives it the generic EC 2.7.11.1 (serine/threonine kinase), its defining activity is the sequential or concomitant phosphorylation of a threonine and a tyrosine in the TEY activation-loop motif of ERK1 and ERK2. The reviewed human entry describes the reaction as EC 2.7.12.2, covering phosphorylation of seryl, threonyl and tyrosyl residues, with Mg²⁺ as cofactor [uniprot-P36507-entry]. Zheng and Guan expressed human MEK2 in *E. coli* and showed that the purified enzyme stimulated threonine and tyrosine phosphorylation of recombinant ERK1 and raised ERK1 kinase activity more than 100-fold [zheng-1993-mek1-mek2-cloning]. In side-by-side comparisons, recombinant MEK2 was the most active ERK activator tested, roughly seven times more active than recombinant MEK1 [zheng-1993-properties-meks]. Rat MKK2 expressed in COS cells likewise phosphorylated and activated p42 and p44 MAPK (ERK2 and ERK1) [wu-1993-mkk2].

MEK2's substrate specificity is unusually narrow, and docking interactions outside the active site enforce it. A conserved basic docking site at the extreme N-terminus of MEK1 and MEK2 is necessary and sufficient for high-affinity, direct binding of ERK1 and ERK2. Peptides spanning this site inhibit ERK phosphorylation by MEK [bardwell-2001-mek-docking-site]. Independent work mapped the MAPK-binding region of MAPKK to residues 1–32 [fukuda-1997-mapk-mapkk-interaction], and MEKs form stable complexes with ERKs in vitro [zheng-1993-properties-meks]. The N-terminal segment of the horse protein, MLARRKPVLPALTINPAIAEG, is identical to human MEK2 apart from one conservative change at position 17, so ERK docking is expected to be preserved.

Structurally, MEK2 has the canonical bilobal protein kinase fold. Crystal structures of human MEK1 and MEK2 in ternary complexes with MgATP and allosteric inhibitors revealed a pocket adjacent to the ATP site that is unique to MEKs. Inhibitors bound there lock the unphosphorylated enzyme in a closed but catalytically inactive conformation [ohren-2004-mek1-mek2-structures]. Because this pocket is unique to MEKs, it explains how such inhibitors can be selective without competing with ATP. MEK inhibitors of this kind (PD184352, PD98059) are the tools that have been used in horse cells (Section 7). The horse kinase domain is almost identical to human MEK2 across the ATP and allosteric pockets, so these compounds are expected to inhibit equine MEK2 as well.

## 4. Regulation: activation by RAF, scaffolds and feedback

MEK2 is activated by phosphorylation of two serines in its activation segment. In human MEK1 these are Ser218 and Ser222. Mutating either to alanine abolished activation by growth-factor-stimulated cell lysates or by c-Raf, and the two sites are the main c-Raf phosphorylation sites. The residues are conserved throughout the MEK family down to yeast STE7, where mutating them destroys function [zheng-1994-mek-activation-phosphorylation]. The corresponding residues in human MEK2 are Ser222 (annotated "phosphoserine; by RAF") and Ser226 [uniprot-P36507-entry]. Both are present in the horse protein, within the conserved segment LIDSMANSFVGT (notes/sequence_analysis.md). Besides RAF, Mos and MEKK1 can phosphorylate MEKs, and v-Raf phosphorylates and activates MKK2 in vitro [zheng-1994-mek-activation-phosphorylation; wu-1993-mkk2].

Current models put MEK2 at the heart of a dimer-driven allosteric switch rather than treating it as a passive substrate. RAF kinases are activated by dimerization of their kinase domains [lavoie-2015-raf-regulation]. The pseudokinases KSR1/2 were long viewed as scaffolds that bridge RAF and MEK. KSR1 assembles a large complex with HSP90, 14-3-3, MEK1 and MEK2 and shifts MEK into membrane-associated fractions [stewart-1999-ksr-mek-localization]. Lavoie and colleagues showed that MEK binding to the KSR1 kinase domain asymmetrically drives BRAF–KSR1 heterodimerization, which in turn stimulates BRAF activity toward free MEK molecules [lavoie-2018-mek-ksr-braf]. On this basis UniProt annotates human MEK2 as an activator of BRAF in a KSR1/2-dependent manner [uniprot-P36507-entry].

Upstream MAP3Ks recognize MEKs through the DVD, a stretch of about 20 residues immediately C-terminal to the catalytic domain. Mutating the DVD strongly inhibits MAPKK binding to, and activation by, its MAP3Ks, including Raf-1 for MEK1. DVD mutants cannot be activated by external stimuli in cells [takekawa-2005-dvd-docking]. Structural work on the RAF–MEK interface explains why this C-terminal region matters. The crystal structure of the BRAF kinase domain bound to MEK1 shows a face-to-face heterodimer. This complex is sensitive to MEK1 phosphorylation and exists independently of BRAF dimerization. Stable BRAF–MEK complexes predominate in cells with wild-type BRAF, and conformation-specific RAF inhibitors can trap a dormant BRAF–MEK complex [haling-2014-braf-mek-structure]. That structure was solved with MEK1, but the C-lobe sequence of MEK2 is highly similar (Section 2), so MEK2 presumably engages RAF the same way.

Several mechanisms dampen MEK2 signalling. Active ERK phosphorylates MEKs, preferentially on threonine [zheng-1993-properties-meks]. In MEK1 the key feedback residue is Thr292 [roskoski-2012-mek1-2-review]. MEK2 lacks this residue, and Catalanotti and colleagues found that ERK feedback on MEK2 is mediated through a MEK1–MEK2 heterodimer. Phosphorylation of MEK1 Thr292 restrains MEK2 within the complex, and loss of MEK1 stabilizes MEK2 and ERK phosphorylation in cells and in Mek1-knockout embryos [catalanotti-2009-mek1-mek2-heterodimer]. MEK is also SUMOylated, with MEKK1 acting as a MEK-specific SUMO E3 ligase. SUMOylation disrupts MEK–ERK docking and dampens ERK activation, and oncogenic Ras relieves this brake [kubota-2011-mek-sumoylation]. MEK1 and MEK2 can also be regulated differently in some cell types. In U373, CHO and INS-1 cells, ERK-pathway stimuli activated MEK1 but not MEK2 [xu-1997-mek1-mek2-differential].

Bacterial virulence factors exploit the regulatory regions of MEK2, which is relevant to horses, a species susceptible to anthrax. Anthrax lethal factor is a Zn²⁺ metalloprotease that cleaves the N-termini of MAPKK1 and MAPKK2, inactivating the MAPK pathway [duesbery-1998-anthrax-lf-mapkk]. Cleavage always falls in the N-terminal proline-rich region preceding the kinase domain, where it removes the docking sequence [vitale-2000-lf-mapkk-susceptibility]. The consensus LF site is three to four basic or proline residues, then three variable residues, then an aliphatic residue at P1′. Mutating that P1′ residue to aspartate makes MEK2 resistant to cleavage [lee-2011-mek2-melanoma]. In the horse protein the sequence RRKP-VLP-A at residues 5–11 matches this consensus and is identical to human MEK2 (notes/sequence_analysis.md). The *Yersinia* effector YopJ acetylates activation-loop serines and threonines of MAPKKs and thereby blocks their phosphorylation [mukherjee-2006-yopj-acetylation]. UniProt records YopJ acetylation of human MEK2 Ser222 and Ser226 [uniprot-P36507-entry]. The horse protein's N-terminus and activation loop match human MEK2, so equine MEK2 is very likely susceptible to both toxins. This has not been tested directly.

## 5. Subcellular localization and nucleocytoplasmic dynamics

At steady state MEK2 is cytoplasmic. Immunofluorescence of native and transfected protein, subcellular fractionation and detergent permeabilization showed that MEK1 and MEK2 are found only in the cytoplasm of Swiss 3T3, HeLa, COS and PC12 cells. Unlike ERK, they do not accumulate in the nucleus after mitogen stimulation [zheng-1994-mek-cytoplasmic-localization]. This distribution is enforced by a leucine-rich nuclear export signal (NES) in the near N-terminal region, residues 33–44 in MAPKK [fukuda-1997-mapk-mapkk-interaction]. The equivalent stretch in horse MEK2, LQKKLEELELDE, is identical to human MEK2, and UniProt's coiled-coil prediction for residues 27–57 overlaps it [uniprot-A0A9L0SHX8-entry].

This cytoplasmic localization reflects rapid export rather than exclusion. When the NES is deleted from constitutively active MEK, the kinase accumulates in the nucleus. Mitogenic stimulation causes a massive but transient nuclear entry of MEK that is normally masked by efficient export [jaaro-1997-mek1-nuclear]. Microinjection experiments showed that MEK shuttles constantly between nucleus and cytoplasm. Wild-type MEK, but not an NES-disrupted mutant, exports nuclear ERK in a leptomycin B-sensitive (CRM1-dependent) manner, so ERK relocalization after signalling uses a MEK-dependent active export pathway [adachi-2000-erk-nuclear-export]. MEK also acts as a cytoplasmic anchor for inactive ERK. A peptide containing the ERK-binding site and NES is enough to retain ERK in the cytoplasm, and pathway activation dissociates the complex so that ERK can enter the nucleus [fukuda-1997-mapk-mapkk-interaction]. The NES matters physiologically. Disrupting it in constitutively active MAPKK greatly increased nuclear ERK activity and malignant transformation [fukuda-1997-mapkk-nes].

Beyond the bulk cytosol, MEKs are recruited to specific membrane compartments. KSR binding shifts MEK1/2 into large complexes in membrane fractions [stewart-1999-ksr-mek-localization]. The MP1 scaffold binds MEK1 and ERK1 and enhances their activation [schaeffer-1998-mp1], and the p14 adaptor targets MP1 to late endosomes, a localization required for proper ERK signalling [teis-2002-p14-mp1-endosomes]. These scaffold studies centred on MEK1, and how much MEK2 uses the MP1–p14 platform has not been resolved. One study in hepatocytes found that the two MEKs send ERK2 to different places. ERK2 activated by MEK1 accumulated in the nucleus and drove proliferation, whereas ERK2 activated by MEK2 stayed in the cytoplasm and supported survival. The difference traced to phosphorylation of Ser298 (by PAK) and Thr292 (by ERK) in the MEK1 proline-rich insert, which releases active ERK2 from MEK1 on cell adhesion. These sites are phosphorylated in MEK1 but not in MEK2 [skarpen-2008-mek1-mek2-erk2-sorting]. If this applies generally, MEK2 is an ERK activator that tends to keep its product in the cytoplasm. The horse protein lacks a MEK1-type Thr292 in its proline-rich insert (Section 2), so this model predicts the same behaviour for equine MEK2. The automatic GO annotations on the horse entry (early endosome, late endosome, focal adhesion, mitochondrion, regulation of Golgi inheritance) are rule-based IEA assignments inherited from family members [uniprot-A0A9L0SHX8-entry]. They should be treated as hypotheses for MEK2 specifically.

## 6. Biological roles and the significance of MEK1/MEK2 redundancy

Through ERK1/2, the MEK1/2 node controls cell proliferation, differentiation, migration, survival and metabolism [roskoski-2012-mek1-2-review]. Mouse genetics shows that MEK2 is largely redundant with MEK1 in vivo. Mek2-null mice are viable and fertile, have no overt morphological defects, and show normal thymocyte development and T-cell-receptor responses, so MEK1 compensates for loss of MEK2 [belanger-2003-mek2-dispensable]. MEK2 is not functionally inert, however. Reducing total MEK dosage revealed a MEK2 contribution to placental development. Map2k1⁺/⁻;Map2k2⁺/⁻ embryos mostly die from defects confined to extra-embryonic tissues, with abnormal syncytiotrophoblast layer II and multinucleated trophoblast giant cells [nadeau-2009-map2k1-map2k2-placenta]. Mek1-null embryos die at mid-gestation from poorly vascularized placental labyrinth, and Mek1-null fibroblasts fail to migrate toward fibronectin even though Mek2 levels and ERK activation are normal [giroux-1999-mek1-deficient-placenta]. This initially suggested that MEK1 has functions MEK2 cannot provide. A knock-in experiment overturned that interpretation. When Mek2 coding sequence was placed under Mek1 regulatory control, homozygous mice were viable with no apparent phenotype. Across an allelic series, placental failure tracked the total amount of MEK protein, whichever isoform supplied it [aoidi-2016-mek2-knockin-rescue]. At the level of developmental genetics, then, MEK2 is a biochemically interchangeable ERK activator whose distinct phenotypes mostly reflect expression level and pattern.

Other studies find isoform-specific outputs that go beyond dosage. In fibroblasts, RNA interference suggested that MEK1 mainly supplies proliferative signals, whereas MEK2 loss caused massive cyclin D induction, CDK4/6 activation and centrosome over-amplification. This implies that MEK2 restrains G1/S progression [ussar-2004-mek1-mek2-g1s]. In SK-MEL-28 melanoma cells treated with anthrax lethal toxin, a cleavage-resistant MEK2 sustained ERK activity, proliferation and anchorage-independent growth, but a cleavage-resistant MEK1 did not, and the two isoforms regulated non-overlapping transcriptional targets [lee-2011-mek2-melanoma]. In bone-marrow macrophages, MEK2 deficiency left ERK1/2 phosphorylation intact but raised HIF-1α, Glut1, IL-1β and IL-6 after LPS stimulation, and MEK2 overexpression lowered IL-1β. This is an ERK-independent anti-inflammatory function of MEK2 [talwar-2019-mek2-il1b]. In haematopoietic cells, mice keeping only one functional Mek1 or Mek2 allele developed spontaneous B-cell activation inversely proportional to MEK protein and ERK activity, and died of glomerulonephritis or lymphoproliferative disease depending on which isoform remained. MEK dosage therefore sets a threshold for lymphocyte activation, with each isoform contributing distinctly [houde-2022-mek-lymphocyte].

In humans, heterozygous missense mutations in MAP2K2, alongside those in BRAF and MAP2K1, cause cardio-facio-cutaneous syndrome [rodriguez-viciana-2006-cfc]. UniProt annotates at least one of the MEK2 variants (a proline-to-glutamine change) as increasing kinase activity [uniprot-P36507-entry]. These findings show that the strength of MEK2 output matters for development.

These findings bear directly on the horse isoform. A0A9L0SHX8 keeps the ERK-docking N-terminus, the NES, the ATP-binding and catalytic residues and both activating serines, so in principle it is a competent ERK kinase once phosphorylated. Its divergent C-terminal 27 residues replace the region that, in MAPKKs, forms the DVD docking site for upstream MAP3Ks [takekawa-2005-dvd-docking]. Because DVD mutations prevent MAPKKs from being activated by their MAP3Ks and by external stimuli in cells [takekawa-2005-dvd-docking], this isoform is predicted to be poorly activated by RAF. If it is expressed at the protein level, it might act as a non-activatable ERK-binding species, possibly a dominant-negative sink for ERK or a partner for MEK1 heterodimers [catalanotti-2009-mek1-mek2-heterodimer]. These are structure-based predictions that have not been tested experimentally.

## 7. Evidence from horse cells

No study has characterized MEK2 as a distinct protein in the horse. Several studies in equine cells nonetheless show that the MEK1/2–ERK1/2 axis behaves in horses as it does in other mammals, using inhibitors that target the conserved allosteric pocket shared by MEK1 and MEK2 [ohren-2004-mek1-mek2-structures]. In primary equine aortic endothelial cells, FGF2 stimulated ERK1/2 phosphorylation, proliferation, scratch-wound closure and tube formation. The MEK1/2 inhibitor PD184352 (10 µM) blocked FGF2-induced ERK1/2 phosphorylation and reduced these angiogenic responses. VEGF-A, by contrast, failed to activate ERK in these cells, consistent with their high FGFR1 relative to VEGFR expression [finding-2024-equine-endothelial]. In equine articular chondrocytes, MEK–ERK signalling increased glycosaminoglycan synthesis in cartilage explants. Cyclic hyperosmotic loading induced SOX9 expression in passaged and osteoarthritic chondrocytes, and MEK1/2 inhibition prevented this induction [peffers-2010-equine-chondrocytes]. In a trophoblast-type model using the equine glycoprotein hormone α-subunit promoter, the MEK inhibitor PD98059 completely blocked PMA-induced promoter activation. This places the MEK–ERK cascade downstream of PKC in regulating equine chorionic gonadotropin subunit expression, although the host cells were human choriocarcinoma cells [thway-2001-equine-trophoblast]. None of these studies separated MEK2 from MEK1, so the specific contribution of horse MAP2K2 remains undefined.

## 8. Open Questions

Whether the A0A9L0SHX8 isoform exists as a protein is the most basic unresolved question. Its C-terminus differs from every characterized mammalian MEK2, and the other horse entry (F6YUU0) has a different, probably erroneous N-terminus. Long-read RNA sequencing of equine tissues and targeted proteomics would establish whether the 390-residue isoform, a canonical 400-residue MEK2, or both are expressed, and in which tissues. Comparing these with the Ensembl gene ENSECAG00000009157 would also allow the horse gene models to be corrected.

If the short isoform is expressed, its biochemistry is a natural follow-up. Can RAF bind and phosphorylate it on Ser222/Ser226 without a canonical DVD [takekawa-2005-dvd-docking]? Does it bind ERK through its intact N-terminal docking site [bardwell-2001-mek-docking-site]? Does it heterodimerize with MEK1 [catalanotti-2009-mek1-mek2-heterodimer]? A kinase assay with recombinant horse protein, BRAF and ERK2, compared against human MEK2, would answer these directly.

How MEK1 and MEK2 divide the work in horse tissues is unexplored. All equine studies to date use pan-MEK inhibitors [finding-2024-equine-endothelial; peffers-2010-equine-chondrocytes]. Isoform-specific knockdown in equine endothelial cells or chondrocytes would show whether MEK2 carries a distinct share of ERK signalling there, as it does in the mouse placenta [nadeau-2009-map2k1-map2k2-placenta]. The placental finding also makes MEK2 a candidate contributor to equine trophoblast biology, including chorionic girdle and endometrial cup formation, where MEK–ERK signalling regulates glycoprotein hormone genes [thway-2001-equine-trophoblast]. Equine immune cells are an open area. The mouse data showing that MEK2 limits LPS-induced IL-1β through HIF-1α [talwar-2019-mek2-il1b] and that MEK dosage sets lymphocyte activation thresholds [houde-2022-mek-lymphocyte] could be tested in equine macrophages. That would be relevant to inflammatory conditions such as laminitis and equine asthma, where MEK inhibitors have not yet been characterized. Finally, given anthrax susceptibility in horses, it would be useful to confirm experimentally that anthrax lethal factor cleaves equine MEK2 at the conserved N-terminal site [duesbery-1998-anthrax-lf-mapkk; vitale-2000-lf-mapkk-susceptibility], and to test whether naturally occurring equine MAP2K2 variants affect developmental or musculoskeletal traits, as human MAP2K2 variants do in RASopathies [rodriguez-viciana-2006-cfc].

## 9. References

All literature identifiers below were taken from PubMed E-utilities records retrieved during this study. Sequence comparisons are my own analysis (notes/sequence_analysis.md).

* **[adachi-2000-erk-nuclear-export]** Adachi M, Fukuda M, Nishida E (2000). Nuclear export of MAP kinase (ERK) involves a MAP kinase kinase (MEK)-dependent active transport mechanism. J Cell Biol 148(5):849-56. PMID:10704436; DOI:10.1083/jcb.148.5.849; PMCID:PMC2174544. https://pubmed.ncbi.nlm.nih.gov/10704436/
* **[aoidi-2016-mek2-knockin-rescue]** Aoidi R, Maltais A, Charron J (2016). Functional redundancy of the kinases MEK1 and MEK2: Rescue of the Mek1 mutant phenotype by Mek2 knock-in reveals a protein threshold effect. Sci Signal 9(412):ra9. PMID:26814233; DOI:10.1126/scisignal.aad5658. https://pubmed.ncbi.nlm.nih.gov/26814233/
* **[bardwell-2001-mek-docking-site]** Bardwell AJ, Flatauer LJ, Matsukuma K, Thorner J, Bardwell L (2001). A conserved docking site in MEKs mediates high-affinity binding to MAP kinases and cooperates with a scaffold protein to enhance signal transmission. J Biol Chem 276(13):10374-86. PMID:11134045; DOI:10.1074/jbc.M010271200; PMCID:PMC3021106. https://pubmed.ncbi.nlm.nih.gov/11134045/
* **[belanger-2003-mek2-dispensable]** Bélanger LF, Roy S, Tremblay M, Brott B, Steff AM, Mourad W et al. (2003). Mek2 is dispensable for mouse growth and development. Mol Cell Biol 23(14):4778-87. PMID:12832465; DOI:10.1128/MCB.23.14.4778-4787.2003; PMCID:PMC162209. https://pubmed.ncbi.nlm.nih.gov/12832465/
* **[catalanotti-2009-mek1-mek2-heterodimer]** Catalanotti F, Reyes G, Jesenberger V, Galabova-Kovacs G, de Matos Simoes R, Carugo O et al. (2009). A Mek1-Mek2 heterodimer determines the strength and duration of the Erk signal. Nat Struct Mol Biol 16(3):294-303. PMID:19219045; DOI:10.1038/nsmb.1564. https://pubmed.ncbi.nlm.nih.gov/19219045/
* **[crews-1992-mek-primary-structure]** Crews CM, Alessandrini A, Erikson RL (1992). The primary structure of MEK, a protein kinase that phosphorylates the ERK gene product. Science 258(5081):478-80. PMID:1411546; DOI:10.1126/science.1411546. https://pubmed.ncbi.nlm.nih.gov/1411546/
* **[duesbery-1998-anthrax-lf-mapkk]** Duesbery NS, Webb CP, Leppla SH, Gordon VM, Klimpel KR, Copeland TD et al. (1998). Proteolytic inactivation of MAP-kinase-kinase by anthrax lethal factor. Science 280(5364):734-7. PMID:9563949; DOI:10.1126/science.280.5364.734. https://pubmed.ncbi.nlm.nih.gov/9563949/
* **[finding-2024-equine-endothelial]** Finding EJT, Faulkner A, Nash L, Wheeler-Jones CPD (2024). Equine Endothelial Cells Show Pro-Angiogenic Behaviours in Response to Fibroblast Growth Factor 2 but Not Vascular Endothelial Growth Factor A. Int J Mol Sci 25(11):. PMID:38892205; DOI:10.3390/ijms25116017; PMCID:PMC11172845. https://pubmed.ncbi.nlm.nih.gov/38892205/
* **[fukuda-1997-mapk-mapkk-interaction]** Fukuda M, Gotoh Y, Nishida E (1997). Interaction of MAP kinase with MAP kinase kinase: its possible role in the control of nucleocytoplasmic transport of MAP kinase. EMBO J 16(8):1901-8. PMID:9155016; DOI:10.1093/emboj/16.8.1901; PMCID:PMC1169793. https://pubmed.ncbi.nlm.nih.gov/9155016/
* **[fukuda-1997-mapkk-nes]** Fukuda M, Gotoh I, Adachi M, Gotoh Y, Nishida E (1997). A novel regulatory mechanism in the mitogen-activated protein (MAP) kinase cascade. Role of nuclear export signal of MAP kinase kinase. J Biol Chem 272(51):32642-8. PMID:9405481; DOI:10.1074/jbc.272.51.32642. https://pubmed.ncbi.nlm.nih.gov/9405481/
* **[giroux-1999-mek1-deficient-placenta]** Giroux S, Tremblay M, Bernard D, Cardin-Girard JF, Aubry S, Larouche L et al. (1999). Embryonic death of Mek1-deficient mice reveals a role for this kinase in angiogenesis in the labyrinthine region of the placenta. Curr Biol 9(7):369-72. PMID:10209122; DOI:10.1016/s0960-9822(99)80164-x. https://pubmed.ncbi.nlm.nih.gov/10209122/
* **[haling-2014-braf-mek-structure]** Haling JR, Sudhamsu J, Yen I, Sideris S, Sandoval W, Phung W et al. (2014). Structure of the BRAF-MEK complex reveals a kinase activity independent role for BRAF in MAPK signaling. Cancer Cell 26(3):402-413. PMID:25155755; DOI:10.1016/j.ccr.2014.07.007. https://pubmed.ncbi.nlm.nih.gov/25155755/
* **[houde-2022-mek-lymphocyte]** Houde N, Beuret L, Bonaud A, Fortier-Beaulieu SP, Truchon-Landry K, Aoidi R et al. (2022). Fine-tuning of MEK signaling is pivotal for limiting B and T cell activation. Cell Rep 38(2):110223. PMID:35021072; DOI:10.1016/j.celrep.2021.110223. https://pubmed.ncbi.nlm.nih.gov/35021072/
* **[jaaro-1997-mek1-nuclear]** Jaaro H, Rubinfeld H, Hanoch T, Seger R (1997). Nuclear translocation of mitogen-activated protein kinase kinase (MEK1) in response to mitogenic stimulation. Proc Natl Acad Sci U S A 94(8):3742-7. PMID:9108048; DOI:10.1073/pnas.94.8.3742; PMCID:PMC20511. https://pubmed.ncbi.nlm.nih.gov/9108048/
* **[kubota-2011-mek-sumoylation]** Kubota Y, O'Grady P, Saito H, Takekawa M (2011). Oncogenic Ras abrogates MEK SUMOylation that suppresses the ERK pathway and cell transformation. Nat Cell Biol 13(3):282-91. PMID:21336309; DOI:10.1038/ncb2169. https://pubmed.ncbi.nlm.nih.gov/21336309/
* **[lavoie-2015-raf-regulation]** Lavoie H, Therrien M (2015). Regulation of RAF protein kinases in ERK signalling. Nat Rev Mol Cell Biol 16(5):281-98. PMID:25907612; DOI:10.1038/nrm3979. https://pubmed.ncbi.nlm.nih.gov/25907612/
* **[lavoie-2018-mek-ksr-braf]** Lavoie H, Sahmi M, Maisonneuve P, Marullo SA, Thevakumaran N, Jin T et al. (2018). MEK drives BRAF activation through allosteric control of KSR proteins. Nature 554(7693):549-553. PMID:29433126; DOI:10.1038/nature25478; PMCID:PMC6433120. https://pubmed.ncbi.nlm.nih.gov/29433126/
* **[lee-2011-mek2-melanoma]** Lee CS, Dykema KJ, Hawkins DM, Cherba DM, Webb CP, Furge KA et al. (2011). MEK2 is sufficient but not necessary for proliferation and anchorage-independent growth of SK-MEL-28 melanoma cells. PLoS One 6(2):e17165. PMID:21365009; DOI:10.1371/journal.pone.0017165; PMCID:PMC3041822. https://pubmed.ncbi.nlm.nih.gov/21365009/
* **[mukherjee-2006-yopj-acetylation]** Mukherjee S, Keitany G, Li Y, Wang Y, Ball HL, Goldsmith EJ et al. (2006). Yersinia YopJ acetylates and inhibits kinase activation by blocking phosphorylation. Science 312(5777):1211-4. PMID:16728640; DOI:10.1126/science.1126867. https://pubmed.ncbi.nlm.nih.gov/16728640/
* **[nadeau-2009-map2k1-map2k2-placenta]** Nadeau V, Guillemette S, Bélanger LF, Jacob O, Roy S, Charron J (2009). Map2k1 and Map2k2 genes contribute to the normal development of syncytiotrophoblasts during placentation. Development 136(8):1363-74. PMID:19304888; DOI:10.1242/dev.031872. https://pubmed.ncbi.nlm.nih.gov/19304888/
* **[ohren-2004-mek1-mek2-structures]** Ohren JF, Chen H, Pavlovsky A, Whitehead C, Zhang E, Kuffa P et al. (2004). Structures of human MAP kinase kinase 1 (MEK1) and MEK2 describe novel noncompetitive kinase inhibition. Nat Struct Mol Biol 11(12):1192-7. PMID:15543157; DOI:10.1038/nsmb859. https://pubmed.ncbi.nlm.nih.gov/15543157/
* **[peffers-2010-equine-chondrocytes]** Peffers MJ, Milner PI, Tew SR, Clegg PD (2010). Regulation of SOX9 in normal and osteoarthritic equine articular chondrocytes by hyperosmotic loading. Osteoarthritis Cartilage 18(11):1502-8. PMID:20800688; DOI:10.1016/j.joca.2010.08.011; PMCID:PMC3078327. https://pubmed.ncbi.nlm.nih.gov/20800688/
* **[rodriguez-viciana-2006-cfc]** Rodriguez-Viciana P, Tetsu O, Tidyman WE, Estep AL, Conger BA, Cruz MS et al. (2006). Germline mutations in genes within the MAPK pathway cause cardio-facio-cutaneous syndrome. Science 311(5765):1287-90. PMID:16439621; DOI:10.1126/science.1124642. https://pubmed.ncbi.nlm.nih.gov/16439621/
* **[roskoski-2012-mek1-2-review]** Roskoski R (2012). MEK1/2 dual-specificity protein kinases: structure and regulation. Biochem Biophys Res Commun 417(1):5-10. PMID:22177953; DOI:10.1016/j.bbrc.2011.11.145. https://pubmed.ncbi.nlm.nih.gov/22177953/
* **[schaeffer-1998-mp1]** Schaeffer HJ, Catling AD, Eblen ST, Collier LS, Krauss A, Weber MJ (1998). MP1: a MEK binding partner that enhances enzymatic activation of the MAP kinase cascade. Science 281(5383):1668-71. PMID:9733512; DOI:10.1126/science.281.5383.1668. https://pubmed.ncbi.nlm.nih.gov/9733512/
* **[skarpen-2008-mek1-mek2-erk2-sorting]** Skarpen E, Flinder LI, Rosseland CM, Orstavik S, Wierød L, Oksvold MP et al. (2008). MEK1 and MEK2 regulate distinct functions by sorting ERK2 to different intracellular compartments. FASEB J 22(2):466-76. PMID:17928366; DOI:10.1096/fj.07-8650com. https://pubmed.ncbi.nlm.nih.gov/17928366/
* **[stewart-1999-ksr-mek-localization]** Stewart S, Sundaram M, Zhang Y, Lee J, Han M, Guan KL (1999). Kinase suppressor of Ras forms a multiprotein signaling complex and modulates MEK localization. Mol Cell Biol 19(8):5523-34. PMID:10409742; DOI:10.1128/MCB.19.8.5523; PMCID:PMC84397. https://pubmed.ncbi.nlm.nih.gov/10409742/
* **[takekawa-2005-dvd-docking]** Takekawa M, Tatebayashi K, Saito H (2005). Conserved docking site is essential for activation of mammalian MAP kinase kinases by specific MAP kinase kinase kinases. Mol Cell 18(3):295-306. PMID:15866172; DOI:10.1016/j.molcel.2005.04.001. https://pubmed.ncbi.nlm.nih.gov/15866172/
* **[talwar-2019-mek2-il1b]** Talwar H, Bouhamdan M, Bauerfeld C, Talreja J, Aoidi R, Houde N et al. (2019). MEK2 Negatively Regulates Lipopolysaccharide-Mediated IL-1β Production through HIF-1α Expression. J Immunol 202(6):1815-1825. PMID:30710049; DOI:10.4049/jimmunol.1801477; PMCID:PMC6401293. https://pubmed.ncbi.nlm.nih.gov/30710049/
* **[teis-2002-p14-mp1-endosomes]** Teis D, Wunderlich W, Huber LA (2002). Localization of the MP1-MAPK scaffold complex to endosomes is mediated by p14 and required for signal transduction. Dev Cell 3(6):803-14. PMID:12479806; DOI:10.1016/s1534-5807(02)00364-7. https://pubmed.ncbi.nlm.nih.gov/12479806/
* **[thway-2001-equine-trophoblast]** Thway TM, Wolfe MW (2001). Epidermal growth factor regulation of equine glycoprotein hormone alpha subunit expression in trophoblast cells. Biol Reprod 65(1):197-203. PMID:11420240; DOI:10.1095/biolreprod65.1.197. https://pubmed.ncbi.nlm.nih.gov/11420240/
* **[ussar-2004-mek1-mek2-g1s]** Ussar S, Voss T (2004). MEK1 and MEK2, different regulators of the G1/S transition. J Biol Chem 279(42):43861-9. PMID:15284233; DOI:10.1074/jbc.M406240200. https://pubmed.ncbi.nlm.nih.gov/15284233/
* **[vitale-2000-lf-mapkk-susceptibility]** Vitale G, Bernardi L, Napolitani G, Mock M, Montecucco C (2000). Susceptibility of mitogen-activated protein kinase kinase family members to proteolysis by anthrax lethal factor. Biochem J 352 Pt 3(Pt 3):739-45. PMID:11104681; PMCID:PMC1221512. https://pubmed.ncbi.nlm.nih.gov/11104681/
* **[wade-2009-horse-genome]** Wade CM, Giulotto E, Sigurdsson S, Zoli M, Gnerre S, Imsland F et al. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. Science 326(5954):865-7. PMID:19892987; DOI:10.1126/science.1178158; PMCID:PMC3785132. https://pubmed.ncbi.nlm.nih.gov/19892987/
* **[wu-1993-mkk2]** Wu J, Harrison JK, Dent P, Lynch KR, Weber MJ, Sturgill TW (1993). Identification and characterization of a new mammalian mitogen-activated protein kinase kinase, MKK2. Mol Cell Biol 13(8):4539-48. PMID:8393135; DOI:10.1128/mcb.13.8.4539-4548.1993; PMCID:PMC360070. https://pubmed.ncbi.nlm.nih.gov/8393135/
* **[xu-1997-mek1-mek2-differential]** Xu S, Khoo S, Dang A, Witt S, Do V, Zhen E et al. (1997). Differential regulation of mitogen-activated protein/ERK kinase (MEK)1 and MEK2 and activation by a Ras-independent mechanism. Mol Endocrinol 11(11):1618-25. PMID:9328344; DOI:10.1210/mend.11.11.0010. https://pubmed.ncbi.nlm.nih.gov/9328344/
* **[zheng-1993-mek1-mek2-cloning]** Zheng CF, Guan KL (1993). Cloning and characterization of two distinct human extracellular signal-regulated kinase activator kinases, MEK1 and MEK2. J Biol Chem 268(15):11435-9. PMID:8388392. https://pubmed.ncbi.nlm.nih.gov/8388392/
* **[zheng-1993-properties-meks]** Zheng CF, Guan KL (1993). Properties of MEKs, the kinases that phosphorylate and activate the extracellular signal-regulated kinases. J Biol Chem 268(32):23933-9. PMID:8226933. https://pubmed.ncbi.nlm.nih.gov/8226933/
* **[zheng-1994-mek-activation-phosphorylation]** Zheng CF, Guan KL (1994). Activation of MEK family kinases requires phosphorylation of two conserved Ser/Thr residues. EMBO J 13(5):1123-31. PMID:8131746; DOI:10.1002/j.1460-2075.1994.tb06361.x; PMCID:PMC394921. https://pubmed.ncbi.nlm.nih.gov/8131746/
* **[zheng-1994-mek-cytoplasmic-localization]** Zheng CF, Guan KL (1994). Cytoplasmic localization of the mitogen-activated protein kinase activator MEK. J Biol Chem 269(31):19947-52. PMID:8051079. https://pubmed.ncbi.nlm.nih.gov/8051079/
* **[uniprot-A0A9L0SHX8-entry]** UniProtKB/TrEMBL entry A0A9L0SHX8_HORSE, entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0SHX8.txt
* **[uniprot-P36507-entry]** UniProtKB/Swiss-Prot entry P36507 (MP2K2_HUMAN). https://rest.uniprot.org/uniprotkb/P36507.txt
* **[uniprot-F6YUU0-entry]** UniProtKB/TrEMBL entry F6YUU0 (horse MAP2K2, 430 aa). https://rest.uniprot.org/uniprotkb/F6YUU0.txt
* **[ensembl-ENSECAG00000009157-lookup]** Ensembl REST lookup of gene ENSECAG00000009157 (MAP2K2, EquCab3.0). https://rest.ensembl.org/lookup/id/ENSECAG00000009157?content-type=application/json


## Citations

1. adachi-2000-erk-nuclear-export-abstract.md
2. adachi-2000-erk-nuclear-export-fulltext.txt
3. adachi-2000-erk-nuclear-export-summary.md
4. aoidi-2016-mek2-knockin-rescue-abstract.md
5. aoidi-2016-mek2-knockin-rescue-summary.md
6. bardwell-2001-mek-docking-site-abstract.md
7. bardwell-2001-mek-docking-site-summary.md
8. belanger-2003-mek2-dispensable-abstract.md
9. belanger-2003-mek2-dispensable-summary.md
10. catalanotti-2009-mek1-mek2-heterodimer-abstract.md
11. catalanotti-2009-mek1-mek2-heterodimer-summary.md
12. crews-1992-mek-primary-structure-abstract.md
13. crews-1992-mek-primary-structure-summary.md
14. duesbery-1998-anthrax-lf-mapkk-abstract.md
15. duesbery-1998-anthrax-lf-mapkk-summary.md
16. ensembl-ENSECAG00000009157-lookup.json
17. finding-2024-equine-endothelial-abstract.md
18. finding-2024-equine-endothelial-fulltext.txt
19. finding-2024-equine-endothelial-summary.md
20. fukuda-1997-mapk-mapkk-interaction-abstract.md
21. fukuda-1997-mapk-mapkk-interaction-summary.md
22. fukuda-1997-mapkk-nes-abstract.md
23. fukuda-1997-mapkk-nes-summary.md
24. giroux-1999-mek1-deficient-placenta-abstract.md
25. giroux-1999-mek1-deficient-placenta-summary.md
26. haling-2014-braf-mek-structure-abstract.md
27. haling-2014-braf-mek-structure-summary.md
28. houde-2022-mek-lymphocyte-abstract.md
29. houde-2022-mek-lymphocyte-summary.md
30. jaaro-1997-mek1-nuclear-abstract.md
31. jaaro-1997-mek1-nuclear-summary.md
32. kubota-2011-mek-sumoylation-abstract.md
33. kubota-2011-mek-sumoylation-summary.md
34. lavoie-2015-raf-regulation-abstract.md
35. lavoie-2015-raf-regulation-summary.md
36. lavoie-2018-mek-ksr-braf-abstract.md
37. lavoie-2018-mek-ksr-braf-summary.md
38. lee-2011-mek2-melanoma-abstract.md
39. lee-2011-mek2-melanoma-fulltext.txt
40. lee-2011-mek2-melanoma-summary.md
41. mukherjee-2006-yopj-acetylation-abstract.md
42. mukherjee-2006-yopj-acetylation-summary.md
43. nadeau-2009-map2k1-map2k2-placenta-abstract.md
44. nadeau-2009-map2k1-map2k2-placenta-summary.md
45. ohren-2004-mek1-mek2-structures-abstract.md
46. ohren-2004-mek1-mek2-structures-summary.md
47. peffers-2010-equine-chondrocytes-abstract.md
48. peffers-2010-equine-chondrocytes-fulltext.txt
49. peffers-2010-equine-chondrocytes-summary.md
50. rodriguez-viciana-2006-cfc-abstract.md
51. rodriguez-viciana-2006-cfc-summary.md
52. roskoski-2012-mek1-2-review-abstract.md
53. roskoski-2012-mek1-2-review-summary.md
54. schaeffer-1998-mp1-abstract.md
55. schaeffer-1998-mp1-summary.md
56. skarpen-2008-mek1-mek2-erk2-sorting-abstract.md
57. skarpen-2008-mek1-mek2-erk2-sorting-summary.md
58. stewart-1999-ksr-mek-localization-abstract.md
59. stewart-1999-ksr-mek-localization-summary.md
60. takekawa-2005-dvd-docking-abstract.md
61. takekawa-2005-dvd-docking-summary.md
62. talwar-2019-mek2-il1b-abstract.md
63. talwar-2019-mek2-il1b-summary.md
64. teis-2002-p14-mp1-endosomes-abstract.md
65. teis-2002-p14-mp1-endosomes-summary.md
66. thway-2001-equine-trophoblast-abstract.md
67. thway-2001-equine-trophoblast-summary.md
68. uniprot-A0A9L0SHX8-entry.txt
69. uniprot-A0A9L0SHX8-summary.md
70. uniprot-F6YUU0-entry.txt
71. uniprot-P36507-entry.txt
72. ussar-2004-mek1-mek2-g1s-abstract.md
73. ussar-2004-mek1-mek2-g1s-summary.md
74. vitale-2000-lf-mapkk-susceptibility-abstract.md
75. vitale-2000-lf-mapkk-susceptibility-summary.md
76. wade-2009-horse-genome-abstract.md
77. wade-2009-horse-genome-summary.md
78. wu-1993-mkk2-abstract.md
79. wu-1993-mkk2-summary.md
80. xu-1997-mek1-mek2-differential-abstract.md
81. xu-1997-mek1-mek2-differential-summary.md
82. zheng-1993-mek1-mek2-cloning-abstract.md
83. zheng-1993-mek1-mek2-cloning-summary.md
84. zheng-1993-properties-meks-abstract.md
85. zheng-1993-properties-meks-summary.md
86. zheng-1994-mek-activation-phosphorylation-abstract.md
87. zheng-1994-mek-activation-phosphorylation-summary.md
88. zheng-1994-mek-cytoplasmic-localization-abstract.md
89. zheng-1994-mek-cytoplasmic-localization-summary.md