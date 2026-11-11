---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:05:44.433247'
end_time: '2026-10-26T00:15:03.117275'
duration_seconds: 558.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: LNPEP
  gene_symbol: LNPEP
  uniprot_accession: A0A9L0JGC2
  protein_description: 'RecName: Full=Leucyl-cystinyl aminopeptidase {ECO:0000256|ARBA:ARBA00071211};
    EC=3.4.11.3 {ECO:0000256|ARBA:ARBA00066490}; AltName: Full=Oxytocinase {ECO:0000256|ARBA:ARBA00080172};'
  gene_info: Name=LNPEP {ECO:0000313|Ensembl:ENSEASP00005052244.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the peptidase M1 family.
  protein_domains: Aminopeptidase_N-like_N. (IPR045357); Aminopeptidase_N-like_N_sf.
    (IPR042097); ERAP1-like_C_dom. (IPR024571); M1_APN-typ. (IPR034016); Peptidase_M1.
    (IPR001930)
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
citation_count: 96
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JGC2
- **Protein Description:** RecName: Full=Leucyl-cystinyl aminopeptidase {ECO:0000256|ARBA:ARBA00071211}; EC=3.4.11.3 {ECO:0000256|ARBA:ARBA00066490}; AltName: Full=Oxytocinase {ECO:0000256|ARBA:ARBA00080172};
- **Gene Information:** Name=LNPEP {ECO:0000313|Ensembl:ENSEASP00005052244.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the peptidase M1 family.
- **Key Domains:** Aminopeptidase_N-like_N. (IPR045357); Aminopeptidase_N-like_N_sf. (IPR042097); ERAP1-like_C_dom. (IPR024571); M1_APN-typ. (IPR034016); Peptidase_M1. (IPR001930)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LNPEP" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LNPEP' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LNPEP** (gene ID: LNPEP, UniProt: A0A9L0JGC2) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# LNPEP (Leucyl-cystinyl aminopeptidase / IRAP / oxytocinase) in the donkey, *Equus asinus* (UniProt A0A9L0JGC2)

## 1. Introduction and summary

The donkey gene *LNPEP* encodes leucyl-cystinyl aminopeptidase (EC 3.4.11.3), a protein known in other mammals under three historical names that reflect the three routes by which it was discovered: placental leucine aminopeptidase (P-LAP) or oxytocinase in humans [rogi-1996-plap-abstract], insulin-regulated (or insulin-responsive) membrane aminopeptidase (IRAP, vp165, gp160) in rat adipocytes [keller-1995-vp165-abstract][kandror-1994-gp160marker-abstract], and the angiotensin IV (AT4) receptor in the brain [albiston-2001-at4irap-abstract]. It is a type II single-pass membrane zinc metallopeptidase of the M1 family whose large C-terminal ectodomain removes N-terminal residues from peptide hormones, most characteristically the N-terminal half-cystine of the disulfide-cyclized nonapeptides oxytocin and vasopressin [matsumoto-2000-solubleplap-abstract][wallis-2007-vasopressin-abstract]. Its distinctive feature among M1 aminopeptidases is a long cytoplasmic N-terminal tail carrying dileucine and tankyrase-binding motifs that targets the enzyme to a specialized, regulated endosomal storage compartment: the GLUT4 storage vesicle in fat and muscle, and a Rab14-positive endosomal compartment in dendritic cells [keller-1995-vp165-abstract][saveanu-2009-crosspresentation-abstract][vear-2020-review-fulltext]. Upon insulin stimulation, IRAP is translocated with GLUT4 to the plasma membrane, where its exteriorized catalytic domain gains access to circulating peptides; vasopressin is the best validated physiological substrate [ross-1997-trafficking-abstract][wallis-2007-vasopressin-abstract]. In dendritic cells, the same enzyme trims the N-termini of antigenic peptide precursors within endosomes for MHC class I cross-presentation [saveanu-2009-crosspresentation-abstract].

No experimental study of the donkey protein itself was found. The donkey entry is an unreviewed TrEMBL record derived from the donkey genome assembly (Wang et al. 2020, Nat Commun, PMID 33293529, cited in the UniProt record) with all functional annotations transferred automatically (ARBA, PIRSR, TreeGrafter). The functional account given here therefore rests mainly on orthology: the donkey sequence (1026 aa) is 91% identical to human LNPEP/IRAP (Q9UIQ6, 1025 aa) over a global alignment computed for this report, and every functionally characterized motif discussed below is conserved at the same position (Section 2). The closest direct evidence comes from the horse (*Equus caballus*), a congener of the donkey, in which LNPEP protein has been identified by mass spectrometry in reproductive tissues, pituitary, placenta and the early conceptus, and in which a serum oxytocinase pool that does not rise in pregnancy has been measured [dielamorim-2023-mareoxytocinase-fulltext][dielamorim-2022-conceptus-fulltext]. These equine studies are described in Section 8. The inference that the donkey protein is a functional IRAP orthologue is therefore strong, but enzyme kinetics, subcellular trafficking and insulin regulation have not been measured in any equid.

## 2. Gene identity and verification for the donkey protein

The UniProt record A0A9L0JGC2 (gene name LNPEP, Ensembl ENSEASG00005018806, donkey chromosome 11) describes a 1026-residue protein assigned to the peptidase M1 family, with a predicted helical transmembrane segment at residues 110–131, an aminopeptidase N-like N-terminal domain (174–358), the M1 catalytic domain (393–611), an ERAP1-like C-terminal domain (690–1009), zinc ligands at His464, His468 and Glu487 and the catalytic proton acceptor Glu465 (UniProt A0A9L0JGC2 flat file, retrieved for this report). The gene symbol, the "oxytocinase" alternative name, the EC number and the domain architecture all match the human LNPEP gene product and its rodent orthologue IRAP, which Keller and colleagues established are the same protein [keller-2003-companion-abstract]. There is no evidence of a different gene sharing the symbol, so the literature on human, rat and mouse IRAP/P-LAP is applicable.

To verify conservation of functional elements, the donkey and human sequences were aligned (Biopython global alignment, BLOSUM62; 933 identical positions over 1025 human residues, 91%). The HEXXH zinc-binding motif (HELAH, 464–468) and the GAMEN exopeptidase motif (428–432), which define the oxytocinase subfamily of M1 enzymes [tsujimoto-2005-oxytocinase-abstract], occur at identical positions in both species. In the cytoplasmic tail, the two dileucine motifs described in the rat clone [keller-1995-vp165-abstract] (donkey/human "SRLL" at 51–54 and "AKLL" at 74–77) and the tankyrase-binding sequence RQSPDG at residues 96–101, which matches exactly the 96RQSPDG101 motif mapped by Chi and Lodish [chi-2000-tankyrase-abstract] and the general RXXPDG tankyrase-binding motif [sbodio-2002-tbm-abstract], are perfectly conserved. One informative difference is in the juxtamembrane stalk: the human Phe154–Ala155 bond, proposed as the secretase cleavage site that liberates soluble P-LAP into maternal serum and reported to be restricted to hominids [pham-2009-ko-abstract], is Leu-Ala in the donkey ("QPLATNG" versus human "QPFATNG"). This is consistent with the conclusion from mouse work that non-hominid species lack the pregnancy-induced circulating oxytocinase of humans [pham-2009-ko-abstract], and, as discussed in Section 8, with measurements in mares showing a serum oxytocinase pool that does not increase in pregnancy [dielamorim-2023-mareoxytocinase-fulltext].

## 3. Enzymatic activity and substrate specificity

IRAP/P-LAP is a zinc-dependent exopeptidase that releases single N-terminal amino acids. The human enzyme was cloned from placenta and shown to contain the HEXXH(X)18E zinc motif of the M1 family, placing it with aminopeptidase N and aminopeptidase A [rogi-1996-plap-abstract]. Independently, gp160, the major protein other than GLUT4 in rat adipocyte GLUT4 vesicles, was shown to be homologous to aminopeptidase N and to possess aminopeptidase activity in vitro [kandror-1994-gp160aminopeptidase-abstract]. A recombinant soluble form of human P-LAP purified from CHO cells is a zinc-containing homodimer of about 280 kDa with broad activity on aminoacyl artificial substrates and sensitivity to classical aminopeptidase inhibitors [matsumoto-2000-solubleplap-abstract]; this underlies the UniProt description that hydrolysis of aminoacyl arylamides exceeds that of the cystinyl derivative.

The defining natural substrates are oxytocin and vasopressin. Among N-terminal cysteine, disulfide-bonded hormones, P-LAP sequentially released residues from vasopressin and oxytocin but did not cleave calcitonin or endothelins [matsumoto-2000-solubleplap-abstract]. The rat enzyme (vp165) was screened against 22 peptide hormones: angiotensin III, angiotensin IV and Lys-bradykinin bound with half-saturation constants of 20–600 nM and were cleaved, while vasopressin bound more weakly but was cleaved more rapidly at saturation [herbst-1997-vasopressin-abstract]. With recombinant human IRAP, only vasopressin, oxytocin and Met-enkephalin were rapidly cleaved from a tested panel, whereas angiotensin IV and LVV-hemorphin-7 were bound but not hydrolyzed [lew-2003-at4inhibitors-abstract]. P-LAP expressed in neural PC12 cells also degraded the opioid peptides Met-enkephalin and dynorphin A(1–8) [matsumoto-2001-substrates-abstract]. A broader in vitro substrate list, summarized in a recent review, includes Lys-bradykinin, angiotensin III, Met-enkephalin, dynorphin A 1–8, neurokinin A, neuromedin B, somatostatin and cholecystokinin-8, but the same review emphasizes that only vasopressin has been confirmed as a physiological substrate in vivo [vear-2020-review-fulltext]. That in vivo confirmation came from IRAP-deficient mice, whose adipocytes and skeletal muscle failed to process vasopressin and oxytocin from the N-terminus, and in which injected vasopressin had a threefold longer circulating half-life and endogenous plasma vasopressin was twofold elevated [wallis-2007-vasopressin-abstract].

IRAP also trims antigenic peptide precursors. Compared directly with ERAP1 in vitro, it efficiently trimmed a variety of long peptide sequences and in most cases accumulated mature 8–9-residue epitopes, but it could also over-trim and destroy some epitopes, and its pattern of intermediate accumulation was epitope-dependent and distinct from ERAP1, arguing for a separate role in antigen processing [georgiadou-2010-trimming-abstract][vear-2020-review-fulltext]. Its endosomal trimming activity is required for cross-presentation (Section 6) [saveanu-2009-crosspresentation-abstract]. Taken together, the specificity is best described as a broad N-terminal exopeptidase activity on peptide hormones and long antigenic precursors, combined with an unusual capacity, unique within the M1 family, to remove the N-terminal half-cystine of disulfide-cyclized peptides.

## 4. Structural basis of catalysis and specificity

Crystal structures of human IRAP explain how a single active site handles cyclic hormones and long linear peptides. The first structure showed a closed four-domain arrangement with a large, largely buried cavity abutting the active site, and a GAMEN exopeptidase loop in a conformation markedly different from other aminopeptidases, which the authors proposed explains IRAP's ability to accommodate cyclic peptides such as oxytocin and vasopressin [hermans-2015-irapstructure-abstract]. A structure with a bound antigenic-precursor analogue revealed a semi-closed conformation in which the peptide N-terminus sits at the catalytic zinc while its C-terminal portion extends along an internal cavity between domains II and IV, supporting a "limited selectivity" model in which hydrophobic contacts and shape complementarity beyond the active site contribute affinity [mpakali-2015-irapstructure-abstract]. A complex with a selective inhibitor captured a fully closed conformation, with domains II and IV juxtaposed to exclude solvent and a GAMEN-adjacent loop reconfigured to admit bulky side chains, revealing active-site plasticity that may underlie substrate permissiveness and selectivity relative to ERAP1 and ERAP2 [mpakali-2017-conformational-abstract]. Finally, a macrocyclic inhibitor combining features of angiotensin IV and oxytocin/vasopressin bound in a near-canonical substrate-like pose; small-angle X-ray scattering indicated that IRAP is open in solution and closes on ligand binding, with the GAMEN loop excluding the catalytic water as a mechanism of inhibition [mpakali-2020-macrocycle-abstract]. Because the donkey protein conserves the zinc ligands, the GAMEN motif and 91% overall identity, these structural conclusions are expected to apply directly to it.

The angiotensin IV (AT4) "receptor" was purified and identified as IRAP; AT4 ligands such as angiotensin IV and LVV-hemorphin-7 bind IRAP with nanomolar affinity and inhibit its catalytic activity [albiston-2001-at4irap-abstract], and kinetic analyses showed they are competitive inhibitors acting at the catalytic site rather than agonists of a signaling receptor [lew-2003-at4inhibitors-abstract]. The prevailing model is that their memory-enhancing effects arise from extended half-lives of neuropeptide substrates, and specific small-molecule IRAP inhibitors reproduce these effects [albiston-2011-inhibitors-abstract].

## 5. Subcellular localization and regulated trafficking: the GLUT4 storage compartment

IRAP is a type II membrane protein, with its N-terminus in the cytosol and catalytic domain in the lumen or extracellular space [rogi-1996-plap-abstract][keller-1995-vp165-abstract]. Although UniProt annotates the donkey protein to the plasma membrane, in unstimulated cells the enzyme is predominantly intracellular. In rat adipocytes gp160 was completely colocalized with GLUT4 by three independent fractionation criteria and cycled to the surface in response to insulin with GLUT4-like kinetics [kandror-1994-gp160marker-abstract]. Surface biotinylation in 3T3-L1 adipocytes showed that insulin raises surface IRAP with a half-time of about 2 min in a wortmannin-sensitive (PI3-kinase-dependent) manner, that IRAP continuously recycles, and that IRAP- and GLUT4-immunoisolated vesicles have the same protein composition [ross-1997-trafficking-abstract]. Newly synthesized IRAP passes through the trans-Golgi network to perinuclear specialized endosomes, from which a small fraction slowly recycles to the plasma membrane; at the cell surface its catalytic C-terminus is exteriorized and can act on circulating peptides [vear-2020-review-fulltext]. After endocytosis, IRAP is retrieved from endosomes to the trans-Golgi network by retromer, which binds the IRAP cytoplasmic tail directly and, unlike for GLUT4, without the need for sortilin [pan-2019-dispensable-fulltext]. Regulated localization is not confined to fat and muscle: in brain and in PC12 cells P-LAP is membrane-bound rather than soluble and translocates from intracellular vesicles to the cell surface on forskolin stimulation [matsumoto-2001-substrates-abstract]. In the insulin-responsive vesicles of adipocytes IRAP is a major cargo together with GLUT4, LRP1, sortilin and VAMP2, and these vesicles are held intracellularly by the tether TUG and other proteins until insulin signaling through the Rab GAPs AS160/TBC1D4 and TBC1D1 and the GTPase TC10α mobilizes them [bogan-2012-review-abstract].

The cytoplasmic tail is both a sorting signal and a regulator of the compartment. It contains two dileucine motifs, each preceded by an acidic cluster [keller-1995-vp165-abstract][vear-2020-review-fulltext]. Microinjection of the IRAP cytosolic domain (residues 1–109), or even residues 55–82, into adipocytes induced GLUT4 translocation independently of PI3-kinase, implying that the tail titrates a shared retention/sorting factor [waters-1997-nterminus-abstract]. Knockdown studies established that IRAP is required for GLUT4 retention: IRAP depletion raised basal surface GLUT4 by increasing exocytosis and relocalized GLUT4 to general endosomes, whereas GLUT4 depletion did not affect IRAP trafficking, so IRAP is both cargo and regulator of the insulin-responsive pathway [jordens-2010-sorting-abstract][yeh-2007-tankyrase-abstract]. The Rab GAP AS160 binds the IRAP N-terminus through its second phosphotyrosine-binding domain, independently of AS160 phosphorylation, which led to a model in which IRAP anchors AS160 on storage vesicles to keep their Rabs inactive [peck-2006-as160-abstract]; however, AS160 recruitment to GLUT4 compartments was later found not to require IRAP [jordens-2010-sorting-abstract], and in a retromer study IRAP ablation shifted GLUT4 to more acidic endosomes without affecting the formation, stability or insulin responsiveness of insulin-responsive vesicles [pan-2019-dispensable-abstract]. Whether IRAP is essential for or merely contributes to GLUT4 retention therefore depends on experimental system. In vivo, IRAP-null mice maintained normal glucose homeostasis but showed impaired insulin responses, 30–60% lower glucose uptake in some muscles and adipocytes, and a 40–85% reduction in total GLUT4 protein without a change in GLUT4 subcellular distribution [keller-2002-irapko-abstract], indicating that IRAP also stabilizes GLUT4 levels. Reviews additionally note impaired IRAP translocation in muscle and fat of people with type 2 diabetes, and enlarged hearts in IRAP-null mice [keller-2004-review-abstract].

Tankyrase-1 and tankyrase-2, poly(ADP-ribose) polymerases, bind the IRAP tail. Tankyrase-1 is a Golgi-associated peripheral membrane protein that colocalizes with perinuclear GLUT4 storage vesicles and binds IRAP through its ankyrin repeats and the IRAP sequence 96RQSPDG101 [chi-2000-tankyrase-abstract]; tankyrase-2 likewise binds IRAP and associates with tankyrase-1 [sbodio-2002-tankyrase2-abstract], and the RXXPDG motif was generalized as a tankyrase-binding motif [sbodio-2002-tbm-abstract]. Knockdown of tankyrase, or PARP inhibition, attenuated insulin-stimulated GLUT4 vesicle translocation and glucose uptake and shifted basal partitioning of GLUT4 and IRAP among endosomal compartments [yeh-2007-tankyrase-abstract]. These interactions account for the UniProt subunit annotation "Binds tankyrases 1 and 2" carried on the donkey record, and the motif is conserved in the donkey sequence (Section 2). Several other partners of the tail have been characterized. The vesicle tether p115 was isolated by affinity chromatography on IRAP residues 1–109, and overexpression of the IRAP-binding N-terminus of p115 blocked insulin-stimulated translocation of GLUT4 but not GLUT1 [hosaka-2005-p115-abstract]. Long-, medium- and short-chain acyl-CoA dehydrogenases bind IRAP residues 55–82 in a dileucine-dependent manner and localize to GLUT4 vesicles, and agents that dissociate them from IRAP triggered GLUT4 translocation [katagiri-2002-acad-abstract]. The GLUT4 retention protein TUG binds a short IRAP peptide previously shown to be critical for GLUT4 retention, and IRAP is released from TUG-bound membranes by insulin [habtemichael-2015-tug-abstract]. FHOD formins link IRAP endosomes to actin in immune cells (Section 6) [babdor-2017-tlr9-abstract][vear-2020-review-fulltext]. All of these binding regions lie in the cytoplasmic N-terminal ~110 residues, which are conserved in the donkey sequence (Section 2).

## 6. IRAP-positive endosomes in innate and adaptive immunity

In dendritic cells, IRAP marks a Rab14-positive endosomal storage compartment where it interacts with MHC class I molecules and trims peptide N-termini; IRAP deficiency compromised cross-presentation of internalized antigens in vitro and in vivo while sparing presentation of endogenous antigens, which relies on the related ER aminopeptidases ERAP1/ERAP2 [saveanu-2009-crosspresentation-abstract]. In steady-state mouse conventional DCs, IRAP colocalized with Rab14 and syntaxin 6, was recruited to phagosomes more strongly in CD8+ DCs, and was required for efficient cross-presentation of soluble and particulate antigen [weimershaus-2012-rab14-abstract]. IRAP-positive endosomes also carry TLR9 and its CpG ligand; through interaction with the formin FHOD4 and the actin cytoskeleton, IRAP retains these endosomes and restrains TLR9 trafficking to lysosomes, so IRAP loss enhanced TLR9 signaling in DCs and in infected mice [babdor-2017-tlr9-abstract]. These immune functions illustrate the same principle seen in adipocytes: the IRAP tail organizes a regulated endosomal compartment, and the luminal catalytic domain acts on peptides within it. The oxytocinase subfamily as a whole (IRAP, ERAP1, ERAP2) is thus specialized for intracellular peptide processing in distinct compartments [tsujimoto-2005-oxytocinase-abstract].

## 7. Physiological pathways: hormone metabolism, pregnancy and the brain

The pathway context of LNPEP is peptide hormone inactivation, linking insulin signaling to the metabolism of vasopressin and related peptides. Insulin approximately tripled vasopressin cleavage by intact adipocytes [herbst-1997-vasopressin-abstract], and in mice insulin accelerated vasopressin clearance in an IRAP-dependent manner, an acute "IRAP-dependent insulin effect" on vasopressin [wallis-2007-vasopressin-abstract]. This is the clearest example of interplay between the N-terminal trafficking domain and the C-terminal catalytic domain [vear-2020-review-fulltext]. The pathway was extended by showing that insulin-stimulated proteolytic cleavage of TUG releases IRAP together with GLUT4: mice with constitutive TUG proteolysis in muscle had more IRAP in T-tubule membranes, drank more water, had less renal AQP2 and secreted more vasopressin (judged by copeptin) to compensate for accelerated vasopressin degradation [habtemichael-2015-tug-abstract]. A review of this work frames P-LAP/IRAP as the principal vasopressinase linking insulin action to water balance, notes associations of *LNPEP* variants with the vasopressin response and mortality in sepsis, and proposes that increased surface IRAP in insulin-resistant muscle could drive compensatory vasopressin secretion and hypertension in the metabolic syndrome [li-2020-vasopressin-abstract]. Through cleavage of angiotensin III and other vasoactive peptides, P-LAP has been grouped with aminopeptidase A and ERAP1 as an M1 enzyme influencing blood pressure regulation [tsujimoto-2008-m1review-abstract].

In human pregnancy, serum P-LAP rises with gestation, and the soluble enzyme is thought to degrade oxytocin and vasopressin to maintain pregnancy homeostasis [rogi-1996-plap-abstract][matsumoto-2000-solubleplap-abstract]. However, IRAP-null mice show normal gestation, parturition, litter size and maternal behavior, and pregnant mouse serum contains no detectable IRAP; the hominid-restricted cleavage site suggests circulating oxytocinase may be a primate specialization [pham-2009-ko-abstract]. The donkey sequence lacks the human Phe at this site (Section 2); equine data bearing on this point are discussed in the next section.

In the brain, P-LAP is membrane-bound, increases on neuronal differentiation of PC12 cells and degrades enkephalin and dynorphin [matsumoto-2001-substrates-abstract]; IRAP distribution matches AT4 binding sites, and inhibition of IRAP by angiotensin IV, LVV-hemorphin-7 or small molecules enhances memory in rodents, probably by prolonging the action of neuropeptide substrates such as vasopressin and oxytocin [albiston-2001-at4irap-abstract][albiston-2011-inhibitors-abstract][hermans-2015-irapstructure-abstract]. An open question raised by reviewers is whether such inhibitors reach intracellular IRAP or act only on the surface pool [vear-2020-review-fulltext].

## 8. Evidence from equids: oxytocinase in horse reproduction

Although nothing has been published on donkey LNPEP, a series of recent studies in the horse, a congener with which the donkey can hybridize, give the most species-relevant data, and they concern the oxytocin-regulating side of the enzyme's function. Early comparative work detected cystine aminopeptidase (CAP, EC 3.4.11.3) activity in full-term horse placenta, which resolved into four activity peaks on gel filtration; the form whose inhibitor sensitivity matched that of pregnancy plasma CAP had an apparent molecular mass of about 115 kDa, smaller than the human (~325 kDa) enzyme, a trend the authors related to the number of tissue layers between maternal blood and trophoblast in different placental types [ikenaga-1994-elution-abstract]. Placental and plasma CAPs from pregnant animals of several species showed correlated sensitivities to L-methionine, EDTA and heat [ikenaga-1993-animals-abstract]. These activity measurements did not identify the gene, and other aminopeptidases may contribute to CAP activity.

Using ELISA, Western blotting, immunohistochemistry, RNA in situ hybridization and LC–MS/MS, Diel de Amorim and colleagues characterized LNPEP in mares. LNPEP protein (identified by mass spectrometry in the ~150 kDa gel region) and mRNA were found in the neurohypophysis and adenohypophysis, corpus luteum, endometrium, myometrium and placenta, with tissue activity ranking myometrium > follicle wall > endometrium > kidney > corpus luteum > liver, and oxytocin itself was detected in pituitary, corpus luteum and placenta [dielamorim-2023-mareoxytocinase-fulltext]. Critically for the question of a soluble circulating form, serum LNPEP measured by ELISA did not differ between pregnant and non-pregnant mares over the first three weeks after ovulation, was unaffected by progesterone, and did not change around foaling; the authors concluded that placental LNPEP does not contribute to the circulating pool, in contrast to the tenfold rise seen in human pregnancy [dielamorim-2023-mareoxytocinase-fulltext]. This fits the absence, in equids, of the hominid Phe154–Ala155 cleavage site (Section 2) [pham-2009-ko-abstract], although a companion study from the same group reported higher serum LNPEP on days 12–15 in pregnant and oxytocin-treated mares than in diestrus mares, and lower values after carbetocin treatment [dielamorim-2023-serumprog-abstract], so the regulation of the serum pool in mares is not fully resolved. In the early conceptus, *LNPEP* mRNA rose between day 10 and day 15, near the time of conceptus fixation, and the protein (annotated as *E. caballus* LNPEP isoform X2, 117.3 kDa) was identified by LC–MS/MS and localized to the trophectoderm; its expression correlated with prostaglandin F receptor and prostaglandin E synthase transcripts [dielamorim-2022-conceptus-fulltext]. In endometrium and corpus luteum, *LNPEP* transcript abundance changed over days 8–15 of diestrus and pregnancy, peaking in luteal tissue on days 10–12 [dielamorim-2022-endometrial-abstract]. The authors propose that LNPEP acts systemically and locally to limit oxytocin availability and thereby modulates oxytocin-driven endometrial prostaglandin release during maternal recognition of pregnancy [dielamorim-2023-mareoxytocinase-fulltext][dielamorim-2022-conceptus-fulltext]. These are largely correlative, small-sample expression studies; no enzyme activity on oxytocin was measured directly with the equine protein, and the ELISA used a detection antibody raised against a human N-terminal peptide [dielamorim-2023-mareoxytocinase-fulltext]. Nevertheless, they establish that the equid LNPEP protein is expressed in the expected oxytocin target and source tissues, which supports transfer of the oxytocinase function to the donkey orthologue.

## 9. Open Questions

The most fundamental gap is the absence of any direct data on the donkey protein; the closest evidence is the expression work in horses (Section 8). The donkey annotation is entirely computational, and even in horses it is not known whether LNPEP is expressed in adipose tissue, muscle, brain and dendritic cells as in rodents, whether it translocates with GLUT4 in equine insulin-sensitive tissues, or whether its kinetics on oxytocin and vasopressin match the human enzyme. Equine metabolic syndrome and insulin dysregulation are clinically important in horses and donkeys, which makes measuring IRAP translocation in equine muscle and adipose tissue, analogous to the human type 2 diabetes observations [keller-2004-review-abstract], a useful follow-up. Second, the origin and regulation of the serum LNPEP pool in equids is unclear: mare serum contains immunoreactive LNPEP that does not track pregnancy in one study [dielamorim-2023-mareoxytocinase-fulltext] but varied with pregnancy and oxytocin treatment in another [dielamorim-2023-serumprog-abstract], while older activity data suggest a placental CAP form resembles a plasma form [ikenaga-1994-elution-abstract]. Activity assays on oxytocin and vasopressin in jenny and mare serum, and identification of the proteolytic site that would release a soluble ectodomain without the hominid Phe154, would resolve this [pham-2009-ko-abstract]. Third, beyond vasopressin, the physiological substrates of IRAP remain uncertain even in model species [vear-2020-review-fulltext][keller-2003-companion-abstract], and the mechanism by which the cytoplasmic tail retains GLUT4 storage vesicles is still debated given conflicting AS160 data [jordens-2010-sorting-abstract]. Finally, the contribution of IRAP to equine cross-presentation and TLR9 signaling is unexplored. Useful follow-ups include RNA-seq-based tissue expression in donkey and horse, AlphaFold model comparison with the human crystal structures (an AlphaFold entry exists for A0A9L0JGC2), and recombinant expression of the donkey ectodomain for substrate profiling.

## 10. References

Citation keys in the text carry a suffix indicating the source used (-abstract: verbatim PubMed abstract; -fulltext: full text retrieved from Europe PMC). Files are in `citations/`, each with a `-summary.md` written by the research agent.

- **[albiston-2001-at4irap]** Albiston AL, McDowall SG, Matsacos D, Sim P, Clune E, Mustafa T, Lee J, Mendelsohn FA, Simpson RJ, Connolly LM, Chai SY. Evidence that the angiotensin IV (AT(4)) receptor is the enzyme insulin-regulated aminopeptidase. J Biol Chem. 2001;276:48623-6. PMID:11707427 DOI:10.1074/jbc.C100512200. https://pubmed.ncbi.nlm.nih.gov/11707427/ https://doi.org/10.1074/jbc.C100512200
- **[albiston-2011-inhibitors]** Albiston AL, Diwakarla S, Fernando RN, Mountford SJ, Yeatman HR, Morgan B, Pham V, Holien JK, Parker MW, Thompson PE, Chai SY. Identification and development of specific inhibitors for insulin-regulated aminopeptidase as a new class of cognitive enhancers. Br J Pharmacol. 2011;164:37-47. PMID:21470200 DOI:10.1111/j.1476-5381.2011.01402.x PMCID:PMC3171858. https://pubmed.ncbi.nlm.nih.gov/21470200/ https://doi.org/10.1111/j.1476-5381.2011.01402.x
- **[babdor-2017-tlr9]** Babdor J, Descamps D, Adiko AC, Tohmé M, Maschalidi S, Evnouchidou I, Vasconcellos LR, De Luca M, Mauvais FX, Garfa-Traore M, Brinkmann MM, Chignard M, Manoury B, Saveanu L. IRAP+ endosomes restrict TLR9 activation and signaling. Nat Immunol. 2017;18:509-518. PMID:28319098 DOI:10.1038/ni.3711. https://pubmed.ncbi.nlm.nih.gov/28319098/ https://doi.org/10.1038/ni.3711
- **[bogan-2012-review]** Bogan JS. Regulation of glucose transporter translocation in health and diabetes. Annu Rev Biochem. 2012;81:507-32. PMID:22482906 DOI:10.1146/annurev-biochem-060109-094246. https://pubmed.ncbi.nlm.nih.gov/22482906/ https://doi.org/10.1146/annurev-biochem-060109-094246
- **[chi-2000-tankyrase]** Chi NW, Lodish HF. Tankyrase is a golgi-associated mitogen-activated protein kinase substrate that interacts with IRAP in GLUT4 vesicles. J Biol Chem. 2000;275:38437-44. PMID:10988299 DOI:10.1074/jbc.M007635200. https://pubmed.ncbi.nlm.nih.gov/10988299/ https://doi.org/10.1074/jbc.M007635200
- **[dielamorim-2022-conceptus]** Diel de Amorim M, Klein C, Foster R, Dong L, Lopez-Rodriguez MF, Card C. Expression of Oxytocin/Neurophysin I and Oxytocinase in the Equine Conceptus from Day 8 to Day 21 Post-Ovulation. Animals (Basel). 2022;12:None. PMID:35405789 DOI:10.3390/ani12070799 PMCID:PMC8996865. https://pubmed.ncbi.nlm.nih.gov/35405789/ https://doi.org/10.3390/ani12070799
- **[dielamorim-2022-endometrial]** Diel de Amorim M, Bramer SA, Rajamanickam GD, Klein C, Card C. Endometrial and luteal gene expression of putative gene regulators of the equine maternal recognition of pregnancy. Anim Reprod Sci. 2022;245:107064. PMID:36087407 DOI:10.1016/j.anireprosci.2022.107064. https://pubmed.ncbi.nlm.nih.gov/36087407/ https://doi.org/10.1016/j.anireprosci.2022.107064
- **[dielamorim-2023-mareoxytocinase]** Diel de Amorim M, Dong L, Byron M, Foster RA, Klein C, Saleh M, Saleh T, Card C. Characterization of serum and tissue oxytocinase and tissue oxytocin in the pregnant and non-pregnant mare. Sci Rep. 2023;13:4616. PMID:36944665 DOI:10.1038/s41598-023-31540-9 PMCID:PMC10030782. https://pubmed.ncbi.nlm.nih.gov/36944665/ https://doi.org/10.1038/s41598-023-31540-9
- **[dielamorim-2023-serumprog]** Diel de Amorim M, Bramer SA, Rajamanickam GD, Klein C, Card C. Serum progesterone and oxytocinase, and endometrial and luteal gene expression in pregnant, nonpregnant, oxytocin, carbetocin and meclofenamic acid treated mares. Theriogenology. 2023;198:47-60. PMID:36549183 DOI:10.1016/j.theriogenology.2022.10.019. https://pubmed.ncbi.nlm.nih.gov/36549183/ https://doi.org/10.1016/j.theriogenology.2022.10.019
- **[georgiadou-2010-trimming]** Georgiadou D, Hearn A, Evnouchidou I, Chroni A, Leondiadis L, York IA, Rock KL, Stratikos E. Placental leucine aminopeptidase efficiently generates mature antigenic peptides in vitro but in patterns distinct from endoplasmic reticulum aminopeptidase 1. J Immunol. 2010;185:1584-92. PMID:20592285 DOI:10.4049/jimmunol.0902502 PMCID:PMC2910840. https://pubmed.ncbi.nlm.nih.gov/20592285/ https://doi.org/10.4049/jimmunol.0902502
- **[habtemichael-2015-tug]** Habtemichael EN, Alcázar-Román A, Rubin BR, Grossi LR, Belman JP, Julca O, Löffler MG, Li H, Chi NW, Samuel VT, Bogan JS. Coordinated Regulation of Vasopressin Inactivation and Glucose Uptake by Action of TUG Protein in Muscle. J Biol Chem. 2015;290:14454-61. PMID:25944897 DOI:10.1074/jbc.C115.639203 PMCID:PMC4505512. https://pubmed.ncbi.nlm.nih.gov/25944897/ https://doi.org/10.1074/jbc.C115.639203
- **[herbst-1997-vasopressin]** Herbst JJ, Ross SA, Scott HM, Bobin SA, Morris NJ, Lienhard GE, Keller SR. Insulin stimulates cell surface aminopeptidase activity toward vasopressin in adipocytes. Am J Physiol. 1997;272:E600-6. PMID:9142880 DOI:10.1152/ajpendo.1997.272.4.E600. https://pubmed.ncbi.nlm.nih.gov/9142880/ https://doi.org/10.1152/ajpendo.1997.272.4.E600
- **[hermans-2015-irapstructure]** Hermans SJ, Ascher DB, Hancock NC, Holien JK, Michell BJ, Chai SY, Morton CJ, Parker MW. Crystal structure of human insulin-regulated aminopeptidase with specificity for cyclic peptides. Protein Sci. 2015;24:190-9. PMID:25408552 DOI:10.1002/pro.2604 PMCID:PMC4315657. https://pubmed.ncbi.nlm.nih.gov/25408552/ https://doi.org/10.1002/pro.2604
- **[hosaka-2005-p115]** Hosaka T, Brooks CC, Presman E, Kim SK, Zhang Z, Breen M, Gross DN, Sztul E, Pilch PF. p115 Interacts with the GLUT4 vesicle protein, IRAP, and plays a critical role in insulin-stimulated GLUT4 translocation. Mol Biol Cell. 2005;16:2882-90. PMID:15800058 DOI:10.1091/mbc.e05-01-0072 PMCID:PMC1142432. https://pubmed.ncbi.nlm.nih.gov/15800058/ https://doi.org/10.1091/mbc.e05-01-0072
- **[ikenaga-1993-animals]** Ikenaga H, Mizuta Y, Ono K, Sawazaki T, Suzuki N, Tomoda I. Placental and plasma cystine aminopeptidase in pregnant animals. J Vet Med Sci. 1993;55:479-80. PMID:8357926 DOI:10.1292/jvms.55.479. https://pubmed.ncbi.nlm.nih.gov/8357926/ https://doi.org/10.1292/jvms.55.479
- **[ikenaga-1994-elution]** Ikenaga H, Ono K, Tomoda I. Elution profiles and molecular weights of placental cystine aminopeptidase in animals. J Vet Med Sci. 1994;56:1139-42. PMID:7696406 DOI:10.1292/jvms.56.1139. https://pubmed.ncbi.nlm.nih.gov/7696406/ https://doi.org/10.1292/jvms.56.1139
- **[jordens-2010-sorting]** Jordens I, Molle D, Xiong W, Keller SR, McGraw TE. Insulin-regulated aminopeptidase is a key regulator of GLUT4 trafficking by controlling the sorting of GLUT4 from endosomes to specialized insulin-regulated vesicles. Mol Biol Cell. 2010;21:2034-44. PMID:20410133 DOI:10.1091/mbc.e10-02-0158 PMCID:PMC2883947. https://pubmed.ncbi.nlm.nih.gov/20410133/ https://doi.org/10.1091/mbc.e10-02-0158
- **[kandror-1994-gp160aminopeptidase]** Kandror KV, Yu L, Pilch PF. The major protein of GLUT4-containing vesicles, gp160, has aminopeptidase activity. J Biol Chem. 1994;269:30777-80. PMID:7983006. https://pubmed.ncbi.nlm.nih.gov/7983006/
- **[kandror-1994-gp160marker]** Kandror KV, Pilch PF. gp160, a tissue-specific marker for insulin-activated glucose transport. Proc Natl Acad Sci U S A. 1994;91:8017-21. PMID:8058750 DOI:10.1073/pnas.91.17.8017 PMCID:PMC44536. https://pubmed.ncbi.nlm.nih.gov/8058750/ https://doi.org/10.1073/pnas.91.17.8017
- **[katagiri-2002-acad]** Katagiri H, Asano T, Yamada T, Aoyama T, Fukushima Y, Kikuchi M, Kodama T, Oka Y. Acyl-coenzyme A dehydrogenases are localized on GLUT4-containing vesicles via association with insulin-regulated aminopeptidase in a manner dependent on its dileucine motif. Mol Endocrinol. 2002;16:1049-59. PMID:11981039 DOI:10.1210/mend.16.5.0831. https://pubmed.ncbi.nlm.nih.gov/11981039/ https://doi.org/10.1210/mend.16.5.0831
- **[keller-1995-vp165]** Keller SR, Scott HM, Mastick CC, Aebersold R, Lienhard GE. Cloning and characterization of a novel insulin-regulated membrane aminopeptidase from Glut4 vesicles. J Biol Chem. 1995;270:23612-8. PMID:7559527 DOI:10.1074/jbc.270.40.23612. https://pubmed.ncbi.nlm.nih.gov/7559527/ https://doi.org/10.1074/jbc.270.40.23612
- **[keller-2002-irapko]** Keller SR, Davis AC, Clairmont KB. Mice deficient in the insulin-regulated membrane aminopeptidase show substantial decreases in glucose transporter GLUT4 levels but maintain normal glucose homeostasis. J Biol Chem. 2002;277:17677-86. PMID:11884418 DOI:10.1074/jbc.M202037200. https://pubmed.ncbi.nlm.nih.gov/11884418/ https://doi.org/10.1074/jbc.M202037200
- **[keller-2003-companion]** Keller SR. The insulin-regulated aminopeptidase: a companion and regulator of GLUT4. Front Biosci. 2003;8:s410-20. PMID:12700100 DOI:10.2741/1078. https://pubmed.ncbi.nlm.nih.gov/12700100/ https://doi.org/10.2741/1078
- **[keller-2004-review]** Keller SR. Role of the insulin-regulated aminopeptidase IRAP in insulin action and diabetes. Biol Pharm Bull. 2004;27:761-4. PMID:15187412 DOI:10.1248/bpb.27.761. https://pubmed.ncbi.nlm.nih.gov/15187412/ https://doi.org/10.1248/bpb.27.761
- **[lew-2003-at4inhibitors]** Lew RA, Mustafa T, Ye S, McDowall SG, Chai SY, Albiston AL. Angiotensin AT4 ligands are potent, competitive inhibitors of insulin regulated aminopeptidase (IRAP). J Neurochem. 2003;86:344-50. PMID:12871575 DOI:10.1046/j.1471-4159.2003.01852.x. https://pubmed.ncbi.nlm.nih.gov/12871575/ https://doi.org/10.1046/j.1471-4159.2003.01852.x
- **[li-2020-vasopressin]** Li DT, Habtemichael EN, Bogan JS. Vasopressin inactivation: Role of insulin-regulated aminopeptidase. Vitam Horm. 2020;113:101-128. PMID:32138946 DOI:10.1016/bs.vh.2019.08.017. https://pubmed.ncbi.nlm.nih.gov/32138946/ https://doi.org/10.1016/bs.vh.2019.08.017
- **[matsumoto-2000-solubleplap]** Matsumoto H, Rogi T, Yamashiro K, Kodama S, Tsuruoka N, Hattori A, Takio K, Mizutani S, Tsujimoto M. Characterization of a recombinant soluble form of human placental leucine aminopeptidase/oxytocinase expressed in Chinese hamster ovary cells. Eur J Biochem. 2000;267:46-52. PMID:10601849 DOI:10.1046/j.1432-1327.2000.00949.x. https://pubmed.ncbi.nlm.nih.gov/10601849/ https://doi.org/10.1046/j.1432-1327.2000.00949.x
- **[matsumoto-2001-substrates]** Matsumoto H, Nagasaka T, Hattori A, Rogi T, Tsuruoka N, Mizutani S, Tsujimoto M. Expression of placental leucine aminopeptidase/oxytocinase in neuronal cells and its action on neuronal peptides. Eur J Biochem. 2001;268:3259-66. PMID:11389728 DOI:10.1046/j.1432-1327.2001.02221.x. https://pubmed.ncbi.nlm.nih.gov/11389728/ https://doi.org/10.1046/j.1432-1327.2001.02221.x
- **[mpakali-2015-irapstructure]** Mpakali A, Saridakis E, Harlos K, Zhao Y, Papakyriakou A, Kokkala P, Georgiadis D, Stratikos E. Crystal Structure of Insulin-Regulated Aminopeptidase with Bound Substrate Analogue Provides Insight on Antigenic Epitope Precursor Recognition and Processing. J Immunol. 2015;195:2842-51. PMID:26259583 DOI:10.4049/jimmunol.1501103. https://pubmed.ncbi.nlm.nih.gov/26259583/ https://doi.org/10.4049/jimmunol.1501103
- **[mpakali-2017-conformational]** Mpakali A, Saridakis E, Harlos K, Zhao Y, Kokkala P, Georgiadis D, Giastas P, Papakyriakou A, Stratikos E. Ligand-Induced Conformational Change of Insulin-Regulated Aminopeptidase: Insights on Catalytic Mechanism and Active Site Plasticity. J Med Chem. 2017;60:2963-2972. PMID:28328206 DOI:10.1021/acs.jmedchem.6b01890. https://pubmed.ncbi.nlm.nih.gov/28328206/ https://doi.org/10.1021/acs.jmedchem.6b01890
- **[mpakali-2020-macrocycle]** Mpakali A, Saridakis E, Giastas P, Maben Z, Stern LJ, Larhed M, Hallberg M, Stratikos E. Structural Basis of Inhibition of Insulin-Regulated Aminopeptidase by a Macrocyclic Peptidic Inhibitor. ACS Med Chem Lett. 2020;11:1429-1434. PMID:32676150 DOI:10.1021/acsmedchemlett.0c00172 PMCID:PMC7357224. https://pubmed.ncbi.nlm.nih.gov/32676150/ https://doi.org/10.1021/acsmedchemlett.0c00172
- **[pan-2019-dispensable]** Pan X, Meriin A, Huang G, Kandror KV. Insulin-responsive amino peptidase follows the Glut4 pathway but is dispensable for the formation and translocation of insulin-responsive vesicles. Mol Biol Cell. 2019;30:1536-1543. PMID:30943117 DOI:10.1091/mbc.E18-12-0792 PMCID:PMC6724691. https://pubmed.ncbi.nlm.nih.gov/30943117/ https://doi.org/10.1091/mbc.E18-12-0792
- **[peck-2006-as160]** Peck GR, Ye S, Pham V, Fernando RN, Macaulay SL, Chai SY, Albiston AL. Interaction of the Akt substrate, AS160, with the glucose transporter 4 vesicle marker protein, insulin-regulated aminopeptidase. Mol Endocrinol. 2006;20:2576-83. PMID:16762977 DOI:10.1210/me.2005-0476. https://pubmed.ncbi.nlm.nih.gov/16762977/ https://doi.org/10.1210/me.2005-0476
- **[pham-2009-ko]** Pham V, Burns P, Albiston AL, Yeatman HR, Ng L, Diwakarla S, Chai SY. Reproduction and maternal behavior in insulin-regulated aminopeptidase (IRAP) knockout mice. Peptides. 2009;30:1861-5. PMID:19647771 DOI:10.1016/j.peptides.2009.07.019. https://pubmed.ncbi.nlm.nih.gov/19647771/ https://doi.org/10.1016/j.peptides.2009.07.019
- **[rogi-1996-plap]** Rogi T, Tsujimoto M, Nakazato H, Mizutani S, Tomoda Y. Human placental leucine aminopeptidase/oxytocinase. A new member of type II membrane-spanning zinc metallopeptidase family. J Biol Chem. 1996;271:56-61. PMID:8550619 DOI:10.1074/jbc.271.1.56. https://pubmed.ncbi.nlm.nih.gov/8550619/ https://doi.org/10.1074/jbc.271.1.56
- **[ross-1997-trafficking]** Ross SA, Herbst JJ, Keller SR, Lienhard GE. Trafficking kinetics of the insulin-regulated membrane aminopeptidase in 3T3-L1 adipocytes. Biochem Biophys Res Commun. 1997;239:247-51. PMID:9345303 DOI:10.1006/bbrc.1997.7459. https://pubmed.ncbi.nlm.nih.gov/9345303/ https://doi.org/10.1006/bbrc.1997.7459
- **[saveanu-2009-crosspresentation]** Saveanu L, Carroll O, Weimershaus M, Guermonprez P, Firat E, Lindo V, Greer F, Davoust J, Kratzer R, Keller SR, Niedermann G, van Endert P. IRAP identifies an endosomal compartment required for MHC class I cross-presentation. Science. 2009;325:213-7. PMID:19498108 DOI:10.1126/science.1172845. https://pubmed.ncbi.nlm.nih.gov/19498108/ https://doi.org/10.1126/science.1172845
- **[sbodio-2002-tankyrase2]** Sbodio JI, Lodish HF, Chi NW. Tankyrase-2 oligomerizes with tankyrase-1 and binds to both TRF1 (telomere-repeat-binding factor 1) and IRAP (insulin-responsive aminopeptidase). Biochem J. 2002;361:451-9. PMID:11802774 DOI:10.1042/0264-6021:3610451 PMCID:PMC1222327. https://pubmed.ncbi.nlm.nih.gov/11802774/ https://doi.org/10.1042/0264-6021:3610451
- **[sbodio-2002-tbm]** Sbodio JI, Chi NW. Identification of a tankyrase-binding motif shared by IRAP, TAB182, and human TRF1 but not mouse TRF1. NuMA contains this RXXPDG motif and is a novel tankyrase partner. J Biol Chem. 2002;277:31887-92. PMID:12080061 DOI:10.1074/jbc.M203916200. https://pubmed.ncbi.nlm.nih.gov/12080061/ https://doi.org/10.1074/jbc.M203916200
- **[tsujimoto-2005-oxytocinase]** Tsujimoto M, Hattori A. The oxytocinase subfamily of M1 aminopeptidases. Biochim Biophys Acta. 2005;1751:9-18. PMID:16054015 DOI:10.1016/j.bbapap.2004.09.011. https://pubmed.ncbi.nlm.nih.gov/16054015/ https://doi.org/10.1016/j.bbapap.2004.09.011
- **[tsujimoto-2008-m1review]** Tsujimoto M, Goto Y, Maruyama M, Hattori A. Biochemical and enzymatic properties of the M1 family of aminopeptidases involved in the regulation of blood pressure. Heart Fail Rev. 2008;13:285-91. PMID:17999179 DOI:10.1007/s10741-007-9064-8. https://pubmed.ncbi.nlm.nih.gov/17999179/ https://doi.org/10.1007/s10741-007-9064-8
- **[vear-2020-review]** Vear A, Gaspari T, Thompson P, Chai SY. Is There an Interplay Between the Functional Domains of IRAP? Front Cell Dev Biol. 2020;8:585237. PMID:33134302 DOI:10.3389/fcell.2020.585237 PMCID:PMC7550531. https://pubmed.ncbi.nlm.nih.gov/33134302/ https://doi.org/10.3389/fcell.2020.585237
- **[wallis-2007-vasopressin]** Wallis MG, Lankford MF, Keller SR. Vasopressin is a physiological substrate for the insulin-regulated aminopeptidase IRAP. Am J Physiol Endocrinol Metab. 2007;293:E1092-102. PMID:17684103 DOI:10.1152/ajpendo.00440.2007. https://pubmed.ncbi.nlm.nih.gov/17684103/ https://doi.org/10.1152/ajpendo.00440.2007
- **[waters-1997-nterminus]** Waters SB, D'Auria M, Martin SS, Nguyen C, Kozma LM, Luskey KL. The amino terminus of insulin-responsive aminopeptidase causes Glut4 translocation in 3T3-L1 adipocytes. J Biol Chem. 1997;272:23323-7. PMID:9287343 DOI:10.1074/jbc.272.37.23323. https://pubmed.ncbi.nlm.nih.gov/9287343/ https://doi.org/10.1074/jbc.272.37.23323
- **[weimershaus-2012-rab14]** Weimershaus M, Maschalidi S, Sepulveda F, Manoury B, van Endert P, Saveanu L. Conventional dendritic cells require IRAP-Rab14 endosomes for efficient cross-presentation. J Immunol. 2012;188:1840-6. PMID:22238454 DOI:10.4049/jimmunol.1101504. https://pubmed.ncbi.nlm.nih.gov/22238454/ https://doi.org/10.4049/jimmunol.1101504
- **[yeh-2007-tankyrase]** Yeh TY, Sbodio JI, Tsun ZY, Luo B, Chi NW. Insulin-stimulated exocytosis of GLUT4 is enhanced by IRAP and its partner tankyrase. Biochem J. 2007;402:279-90. PMID:17059388 DOI:10.1042/BJ20060793 PMCID:PMC1798437. https://pubmed.ncbi.nlm.nih.gov/17059388/ https://doi.org/10.1042/BJ20060793
- **UniProt A0A9L0JGC2** UniProtKB/TrEMBL entry A0A9L0JGC2_EQUAS, Leucyl-cystinyl aminopeptidase, *Equus asinus*. https://rest.uniprot.org/uniprotkb/A0A9L0JGC2.txt (local copy uniprot_A0A9L0JGC2.txt); human comparator UniProt Q9UIQ6 (human_Q9UIQ6.fasta).


## Citations

1. albiston-2001-at4irap-abstract.md
2. albiston-2001-at4irap-summary.md
3. albiston-2011-inhibitors-abstract.md
4. albiston-2011-inhibitors-summary.md
5. babdor-2017-tlr9-abstract.md
6. babdor-2017-tlr9-summary.md
7. bogan-2012-review-abstract.md
8. bogan-2012-review-summary.md
9. chi-2000-tankyrase-abstract.md
10. chi-2000-tankyrase-summary.md
11. dielamorim-2022-conceptus-abstract.md
12. dielamorim-2022-conceptus-fulltext.txt
13. dielamorim-2022-conceptus-summary.md
14. dielamorim-2022-endometrial-abstract.md
15. dielamorim-2022-endometrial-summary.md
16. dielamorim-2023-mareoxytocinase-abstract.md
17. dielamorim-2023-mareoxytocinase-fulltext.txt
18. dielamorim-2023-mareoxytocinase-summary.md
19. dielamorim-2023-serumprog-abstract.md
20. dielamorim-2023-serumprog-summary.md
21. georgiadou-2010-trimming-abstract.md
22. georgiadou-2010-trimming-summary.md
23. habtemichael-2015-tug-abstract.md
24. habtemichael-2015-tug-summary.md
25. herbst-1997-vasopressin-abstract.md
26. herbst-1997-vasopressin-summary.md
27. hermans-2015-irapstructure-abstract.md
28. hermans-2015-irapstructure-summary.md
29. hosaka-2005-p115-abstract.md
30. hosaka-2005-p115-summary.md
31. ikenaga-1993-animals-abstract.md
32. ikenaga-1993-animals-summary.md
33. ikenaga-1994-elution-abstract.md
34. ikenaga-1994-elution-summary.md
35. jordens-2010-sorting-abstract.md
36. jordens-2010-sorting-summary.md
37. kandror-1994-gp160aminopeptidase-abstract.md
38. kandror-1994-gp160aminopeptidase-summary.md
39. kandror-1994-gp160marker-abstract.md
40. kandror-1994-gp160marker-summary.md
41. katagiri-2002-acad-abstract.md
42. katagiri-2002-acad-summary.md
43. keller-1995-vp165-abstract.md
44. keller-1995-vp165-summary.md
45. keller-2002-irapko-abstract.md
46. keller-2002-irapko-summary.md
47. keller-2003-companion-abstract.md
48. keller-2003-companion-summary.md
49. keller-2004-review-abstract.md
50. keller-2004-review-summary.md
51. lew-2003-at4inhibitors-abstract.md
52. lew-2003-at4inhibitors-summary.md
53. li-2020-vasopressin-abstract.md
54. li-2020-vasopressin-summary.md
55. matsumoto-2000-solubleplap-abstract.md
56. matsumoto-2000-solubleplap-summary.md
57. matsumoto-2001-substrates-abstract.md
58. matsumoto-2001-substrates-summary.md
59. mpakali-2015-irapstructure-abstract.md
60. mpakali-2015-irapstructure-summary.md
61. mpakali-2017-conformational-abstract.md
62. mpakali-2017-conformational-summary.md
63. mpakali-2020-macrocycle-abstract.md
64. mpakali-2020-macrocycle-summary.md
65. pan-2019-dispensable-abstract.md
66. pan-2019-dispensable-fulltext.txt
67. pan-2019-dispensable-summary.md
68. peck-2006-as160-abstract.md
69. peck-2006-as160-summary.md
70. pham-2009-ko-abstract.md
71. pham-2009-ko-summary.md
72. rogi-1996-plap-abstract.md
73. rogi-1996-plap-summary.md
74. ross-1997-trafficking-abstract.md
75. ross-1997-trafficking-summary.md
76. saveanu-2009-crosspresentation-abstract.md
77. saveanu-2009-crosspresentation-summary.md
78. sbodio-2002-tankyrase2-abstract.md
79. sbodio-2002-tankyrase2-summary.md
80. sbodio-2002-tbm-abstract.md
81. sbodio-2002-tbm-summary.md
82. tsujimoto-2005-oxytocinase-abstract.md
83. tsujimoto-2005-oxytocinase-summary.md
84. tsujimoto-2008-m1review-abstract.md
85. tsujimoto-2008-m1review-summary.md
86. vear-2020-review-abstract.md
87. vear-2020-review-fulltext.txt
88. vear-2020-review-summary.md
89. wallis-2007-vasopressin-abstract.md
90. wallis-2007-vasopressin-summary.md
91. waters-1997-nterminus-abstract.md
92. waters-1997-nterminus-summary.md
93. weimershaus-2012-rab14-abstract.md
94. weimershaus-2012-rab14-summary.md
95. yeh-2007-tankyrase-abstract.md
96. yeh-2007-tankyrase-summary.md