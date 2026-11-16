# GRK1 (human, UniProtKB:Q15835) review notes

Journal of the GO annotation review. Reviewed together with SAG (P10523): GRK1
phosphorylates light-activated rhodopsin and SAG then caps the phosphorylated receptor.
Quotes are verbatim from the cached file named in the bracket.

## 1. Inputs read

- `GRK1-uniprot.txt` (entry version 222): function, catalytic activity, activity
  regulation, subunit, location, PTM, disease, features.
- `GRK1-ai-review.yaml`: 36 seeded rows, all PENDING at the start.
- GOA-cited papers in `publications/` (all abstract-only, `full_text_available: false`):
  PMID:12601058, PMID:15946941, PMID:1656454, PMID:9020843, PMID:9147475.
- Reactome cache: R-HSA-2514859 (pathway), R-HSA-2581474 (reaction).
- `modules/visual_phototransduction.yaml` (annoton `grk1_kinase`, and the recoverin
  annoton whose target is GRK1).
- `GRK1-deep-research-openscientist.md`: provider report, used only as a list of leads.
  Nothing is quoted from it; each paper cited below was fetched and read.

## 2. What the UniProt record says, and on what evidence

- Catalytic activity EC 2.7.11.14, both the seryl and the threonyl reaction, with
  evidence `ECO:0000269|PubMed:15946941` (human enzyme).
  [file:human/GRK1/GRK1-uniprot.txt "Reaction=L-seryl-[rhodopsin] + ATP = O-phospho-L-seryl-[rhodopsin] +"]
- Kinetics on the human enzyme: [file:human/GRK1/GRK1-uniprot.txt "KM=3.5 uM for rhodopsin {ECO:0000269|PubMed:15946941};"]
- Recoverin inhibition, the recoverin-binding N-terminal region (residues 1-15),
  farnesylation of Cys-560 with carboxyl methylation, and the Ser-491/Thr-492
  autophosphorylation sites are all `By similarity` to bovine GRK1 (P28327). They are
  not human experiments.
- Location: outer segment membrane with `ECO:0000269|PubMed:12601058` (human retina);
  the lipid anchor is by similarity to bovine. The note that location does not change
  with light is by similarity to mouse (Q9WVL4).
- Ser-21 is phosphorylated by PKA and by autocatalysis (`ECO:0000269|PubMed:15946941`);
  K219A abolishes autophosphorylation and rhodopsin phosphorylation (same paper).
- Disease: Oguchi type 2 (CSNBO2, MIM:613411).

## 3. GOA-cited papers

### PMID:15946941 (Horner et al. 2005, J Biol Chem) - abstract only
Source of the IDA rows (rhodopsin kinase activity, GPCR kinase activity, regulation of
opsin-mediated signaling) and of three IC rows.
- [PMID:15946941 "In rod cells of the vertebrate retina, phosphorylation of rhodopsin is mediated by GRK1."]
- [PMID:15946941 "To compare the biochemical properties of GRK1 and GRK7, we measured the K(m) and V(max) of these kinases for ATP and rhodopsin, a model substrate."]
- [PMID:15946941 "Phosphorylation of GRK1 and GRK7 by PKA reduces the ability of GRK1 and GRK7 to phosphorylate rhodopsin in vitro."]
- [PMID:15946941 "We also determined that cAMP-dependent protein kinase (PKA) phosphorylates GRK1 at Ser(21) and GRK7 at Ser(23) and Ser(36) in vitro."]
The abstract does not name the species of the recombinant kinases. UniProt attributes
the kinetics and the Ser-21 site to the human entry with this paper as evidence; the
FLAG-tagged kinases were expressed in HEK-293 cells and the rod outer segments were
bovine. Full text not read.

### PMID:12601058 (Cideciyan et al. 2003, IOVS) - abstract only
Source of the IDA location row and the three IMP process rows.
- [PMID:12601058 "Normal human retina revealed strongly labeled cone outer segments with anti-GRK1 and anti-GRK7."]
- [PMID:12601058 "Normal deactivation kinetics in human L/M cones can occur without GRK7 when GRK1 is present in ESCS, but does not occur when GRK7 is present but GRK1 is deficient in Oguchi disease."]
- [PMID:12601058 "Lack of both GRK1 and GRK7 in S cones of patients with ESCS results in a more pronounced abnormality in deactivation kinetics and suggests the existence of partial compensation by either GRK when the other is deficient."]
This is human in vivo physiology (paired-flash ERG) and human post-mortem
immunocytochemistry. The patients carry NR2E3 mutations; the GRK1 "perturbation" is the
absence of GRK1 immunoreactivity in ESCS S cones, plus the comparison with GRK1-deficient
Oguchi patients. The abstract describes cone outer segments only; rod labelling is not
mentioned in the abstract.

### PMID:1656454 (Lorenz et al. 1991, PNAS) - abstract only
- [PMID:1656454 "Light-dependent deactivation of rhodopsin as well as homologous desensitization of beta-adrenergic receptors involves receptor phosphorylation that is mediated by the highly specific protein kinases rhodopsin kinase (RK) and beta-adrenergic receptor kinase (beta ARK), respectively."]
- [PMID:1656454 "We report here the cloning of a complementary DNA for RK."]
The abstract does not state the species of the cDNA. Human GRK1 was cloned later
(PMID:8812493 and PMID:9147475 in the UniProt record), so this paper cannot be the human
clone; the human UniProt record does not cite it. TAS rows citing it (protein kinase
activity, regulation of GPCR signaling, G protein-coupled opsin signaling) are judged on
the claim, which other evidence supports.

### PMID:9147475 (Zhao et al. 1997, Vis Neurosci) - abstract only
- [PMID:9147475 "This study demonstrates that rat and human pineals express protein kinases that are identical to the corresponding rod photoreceptor rhodopsin kinases."]
- [PMID:9147475 "These data demonstrate that the mammalian pineal contains light-sensitive opsins and a kinase involved in their inactivation."]
Human cDNA cloning plus localization; no kinase assay is described in the abstract.

### PMID:9020843 (Yamamoto et al. 1997, Nat Genet) - abstract only
- [PMID:9020843 "As rhodopsin kinase works with arrestin in shutting off rhodopsin after it has been activated by a photon of light, it is reasonable to propose that some cases of Oguchi disease might be caused by defects in rhodopsin kinase."]
- [PMID:9020843 "Our results indicate that null mutations in the rhodopsin kinase gene are a cause of Oguchi disease and extend the known genetic heterogeneity in congenital stationary night blindness."]

### Reactome
- R-HSA-2581474: [Reactome:R-HSA-2581474 "GRK1 is activated by MII whereupon it phosphorylates MII at multiple serine and threonine sites on its C terminus."]
  and [Reactome:R-HSA-2581474 "A substantial fraction of rhodopsin kinase (GRK1) is bound to recoverin (RCVRN) in darkness, when internal Ca2+ levels are high."]
- R-HSA-2514859 is the pathway summary; it does not name GRK1 in the cached text.

## 4. GO terms looked up (QuickGO, 2026-11-13)

- GO:0050254 rhodopsin kinase activity: "Catalysis of the reaction: ATP + rhodopsin = ADP +
  phosphorhodopsin." Narrow synonyms include "cone opsin kinase activity" and "GPCR kinase
  1 activity". It is_a GO:0004703 G protein-coupled receptor kinase activity, which is_a
  GO:0004674 protein serine/threonine kinase activity, which is_a GO:0004672 protein
  kinase activity. So the three generic kinase terms are all ancestors of the specific one.
- GO:0016059 negative regulation of opsin-mediated signaling pathway is_a GO:0022400
  regulation of opsin-mediated signaling pathway is_a GO:0008277 regulation of G
  protein-coupled receptor signaling pathway is_a GO:0009966 regulation of signal
  transduction. GO:0022400 `regulates` GO:0016056 G protein-coupled opsin signaling pathway.
- GO:0002029 desensitization of G protein-coupled receptor signaling pathway: "... after
  prolonged stimulation with an agonist of the pathway"; is_a negative regulation of GPCR
  signaling (GO:0045744), so also under GO:0008277 and GO:0009966.
- GO:0036368 photoresponse recovery is_a GO:0009416 response to light stimulus.
- GO:0141190 transducin-mediated opsin signaling pathway (is_a GO:0016056): its definition
  includes "The signal is terminated by phosphorylation of the C-terminal tail of rhodopsin
  by rhodopsin kinase to allow arrestin to bind and block G protein binding."
- GO:0097381 photoreceptor disc membrane and GO:0042622 photoreceptor outer segment
  membrane are both part_of GO:0001750 photoreceptor outer segment.

## 5. PAINT

`just paint-losses human GRK1`: "No IRD or IKR loss on this gene's lineage."
IBA rows: GO:0050254 from PTN002806936 (donors include bovine P28327, mouse, rat,
zebrafish and human Q15835 itself); GO:0009966 and GO:0005737 from PTN001219785 (a deeper
GRK node; donors include Drosophila Gprk2 FBgn0261988 and human GRK4 P32298).

## 6. Orthologue annotation state (QuickGO, for donor tracing only)

- Bovine GRK1 P28327: rhodopsin kinase activity EXP (PMID:12686556, PMID:1527025,
  PMID:16675451, PMID:1730692, PMID:21299498); membrane EXP (PMID:14561760, PMID:1527025).
- Mouse Grk1 Q9WVL4: rhodopsin kinase activity EXP PMID:10097103 and IMP PMID:12853434;
  GO:0016059 IMP PMID:10704496; photoreceptor outer segment IDA PMID:22183407.

## 7. Papers fetched and read beyond the GOA citations (2026-11-16)

All were confirmed by PubMed esummary before fetching with `just fetch-pmid`.

### Human
- PMID:9419375 (Cideciyan et al. 1998, PNAS; abstract only). The direct human
  loss-of-function study: an exon 5 deletion in the RK gene.
  [PMID:9419375 "In vitro experiments demonstrated that the mutation, a deletion of exon 5, abolishes the enzymatic activity of RK and is likely a null."]
  [PMID:9419375 "Both a homozygote and heterozygote with this RK mutation had recovery phase abnormalities of rod-isolated photoresponses by electroretinography (ERG); photoactivation was normal."]
  [PMID:9419375 "A slight slowing of cone deactivation kinetics in the homozygote was detected by ERG."]
  [PMID:9419375 "The role of RK in rods would thus be to accelerate inactivation of activated rhodopsin molecules that in concert with regeneration leads to the normal rate of recovery of sensitivity."]
- PMID:8812493 (Khani et al. 1996, Genomics; abstract only). Human gene and cDNA.
  [PMID:8812493 "In rod photoreceptors rhodopsin kinase (RK) mediates rapid desensitization of rod photoreceptors to light by catalyzing phosphorylation of the visual pigment rhodopsin."]
  [PMID:8812493 "The RK locus, assigned to chromosome 13 band q34, is composed of seven exons that encode a protein 92% identical in amino acid sequence to bovine rhodopsin kinase."]
- PMID:11717351 (Weiss et al. 2001, J Neurosci; abstract only).
  [PMID:11717351 "GRK7 and GRK1 are coexpressed in monkey and human cones, suggesting that coordinate regulation of desensitization by both kinases may occur in primates."]
  [PMID:11717351 "In pigs and dogs, cones express only GRK7, whereas in mice and rats, we detected only GRK1 in cones."]
- PMID:11754336 (Chen et al. 2001, Mol Vis; abstract only).
  [PMID:11754336 "We provide evidence that GRK1 and GRK7 are co-expressed in human cones."]

### Bovine (most of the enzymology)
- PMID:1730692 (Inglese et al. 1992, J Biol Chem; abstract only). Farnesylation.
  [PMID:1730692 "RK was determined to be modified by a farnesyl moiety and alpha-carboxyl-methylated."]
  [PMID:1730692 "A time course of Rho* phosphorylation revealed that non-processed RK is approximately 4-fold less active than wild-type RK."]
  Bovine numbering Cys558; the human equivalent is Cys-560 (UniProt, by similarity).
- PMID:7629115 (Chen et al. 1995, J Biol Chem; abstract only). Recoverin.
  [PMID:7629115 "RK, purified using immobilized Rv as an affinity matrix, catalyzed the light-dependent and Ca(2+)-independent incorporation of phosphates into rhodopsin when reconstituted with urea-stripped rod outer segment membranes."]
  [PMID:7629115 "When recoverin was added, the activity of RK became sensitive to free Ca2+, with EC50 = 3 microM."]
  [PMID:7629115 "Rv neither interacts with other members of the G-protein-coupled receptor kinase family such as beta-adrenergic receptor kinase 1 nor inhibits beta-adrenergic receptor kinase 1 activity."]
- PMID:16675451 (Higgins et al. 2006, J Biol Chem; abstract only; species of the kinase
  not stated in the abstract, UniProt files the paper under bovine P28327).
  [PMID:16675451 "In this study we map this interaction interface, showing that residues 1-15 of the kinase form the interaction site for recoverin binding."]
  [PMID:16675451 "Finally, we observe that a kinase mutant lacking the N-terminal recoverin binding site is unable to phosphorylate light-activated rhodopsin."]
- PMID:18339619 (Singh et al. 2008, J Biol Chem; abstract only). Six GRK1 crystal
  structures. [PMID:18339619 "Co-localization of the N terminus and the C-terminal extension near the hinge of the kinase domain suggests that activated GPCRs stimulate kinase activity by binding to this region to facilitate full closure of the kinase domain."]
- PMID:34262173 (Chen et al. 2021, Nature; full text cached; bovine GRK1 residues
  1-535 and bovine rhodopsin).
  [PMID:34262173 "Here we report a series of cryo-electron microscopy single-particle reconstructions of light-activated rhodopsin (Rho*) bound to rhodopsin kinase (GRK1), wherein the N terminus of GRK1 forms a helix that docks into the open cytoplasmic cleft of Rho*."]
  [PMID:34262173 "Full length bovine GRK1 (residues 1–561) has a farnesylation site at its C-terminus which limits its expression in insect cells."]
  The provider report says a GRK1-Rho* complex structure is still needed; this paper
  shows that statement is out of date.
- PMID:14561760 (Zhang et al. 2004, J Biol Chem; abstract only). PDE6D binds
  farnesylated GRK1.
  [PMID:14561760 "We find by yeast two-hybrid screening with a PDEdelta bait that it can interact with farnesylated rhodopsin kinase (GRK1) and that prenylation is essential for this interaction."]
- PMID:1527025 (Palczewski et al. 1992, J Biol Chem; abstract only). Autophosphorylation
  at Ser488/Thr489 (major) and Ser21 (minor); bovine numbering.

### Mouse
- PMID:10097103 (Chen et al. 1999, PNAS; full text cached). Grk1 knockout.
  [PMID:10097103 "This eliminated the light-dependent phosphorylation of rhodopsin and caused the single-photon response to become larger and longer lasting than normal."]
  [PMID:10097103 "Thus, under these conditions, phosphorylation of photoexcited rhodopsin did not occur in the absence of RK."]
  [PMID:10097103 "These data suggest that RK is solely responsible for normal rhodopsin deactivation in the dark-adapted rod."]
- PMID:10704496 (Lyubarsky et al. 2000, J Neurosci; abstract only). Cones.
  [PMID:10704496 "the cone-driven ERGs of GRK1 -/- animals recovered 30-50 times more slowly than those of WT mice"]
- PMID:12853434 (Zhu et al. 2003, J Neurosci; abstract only). Cone opsins.
  [PMID:12853434 "We found that, in the retina of these mice, the light-activated cone opsins were neither phosphorylated nor bound with mCAR."]
- PMID:31908030 (Kolesnikov et al. 2020, FASEB J; full text cached, abstract read).
  [PMID:31908030 "rod dark adaptation following exposure to bright bleaching light was significantly delayed in GRK1-S21A mice"]
- PMID:22183407 (Hagstrom et al. 2012; the MGI source for mouse Grk1 outer-segment
  location): the cache has no abstract, so the donor evidence for the ISS location row
  could not be read.

## 8. Decisions and their reasons

- Molecular function. `rhodopsin kinase activity` (GO:0050254) is the specific term and
  is accepted on all four rows. The human enzyme was assayed directly (PMID:15946941).
  `G protein-coupled receptor kinase activity`, `protein serine/threonine kinase
  activity` and `protein kinase activity` are its is_a ancestors; they are true but
  less specific than the evidence, so they are MODIFY to GO:0050254, not REMOVE.
  `ATP binding` is accepted (ATP is the co-substrate, Km measured on the human enzyme).
- Process. The specific terms are `negative regulation of opsin-mediated signaling
  pathway` (GO:0016059), `photoresponse recovery` (GO:0036368) and `desensitization of G
  protein-coupled receptor signaling pathway` (GO:0002029); all accepted. Their
  ancestors (`regulation of opsin-mediated signaling pathway`, `regulation of G
  protein-coupled receptor signaling pathway`, `regulation of signal transduction`,
  `response to light stimulus`) are MODIFY to the specific child the gene already
  carries. `signal transduction` and `G protein-coupled opsin signaling pathway` name
  the forward pathway; GRK1 switches it off, and in human GOA the terminators (GRK1,
  GRK7, SAG, ARR3) carry GO:0016059 while the activation chain (RHO, GNAT1/2, PDE6,
  cone opsins) carries the pathway term GO:0141190, so these rows are MODIFY to
  GO:0016059. `visual perception` is kept: loss of GRK1 causes night blindness with
  slowed dark adaptation (Oguchi disease).
- Location. Outer segment rows accepted (human immunocytochemistry, PMID:12601058).
  `membrane` is refined to `photoreceptor disc membrane` (GO:0097381), the term the
  Reactome row already carries. The IBA `cytoplasm` row comes from a deep GRK-family
  node; for GRK1 the supported site of action is the outer segment.
- No NEW rows. No source defect is recorded: the IMP rows cite PMID:12601058, whose
  patients carry NR2E3 mutations, and the abstract compares them with GRK1-deficient
  Oguchi patients; whether the full text contains new GRK1-patient recordings could not
  be checked (abstract-only), so the evidence code is not challenged.

## 9. Not verified

- Full texts of PMID:15946941, PMID:12601058, PMID:1656454, PMID:9147475, PMID:9020843
  (abstract-only caches). The species of the recombinant GRK1 in PMID:15946941 is taken
  from UniProt's attribution to the human entry, not from the abstract.
- PMID:22183407 (no abstract in cache).
- The PAINT tree and alignment behind PTN002806936 and PTN001219785 were not inspected.
- Recoverin inhibition, farnesylation and the autophosphorylation sites have not been
  shown on the human protein; the human record carries them by similarity to bovine.
