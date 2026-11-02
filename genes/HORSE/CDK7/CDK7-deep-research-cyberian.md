---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:07:48.417131'
end_time: '2026-10-26T02:26:04.824257'
duration_seconds: 1096.41
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: CDK7
  gene_symbol: CDK7
  uniprot_accession: A0A9L0R074
  protein_description: 'RecName: Full=Serine/threonine-protein {ECO:0000256|PROSITE-ProRule:PRU10027};
    EC=2.7.11.1 {ECO:0000256|PROSITE-ProRule:PRU10027};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the protein kinase superfamily. Ser/Thr protein
  protein_domains: CDK. (IPR050108); CDK7. (IPR037770); Kinase-like_dom_sf. (IPR011009);
    Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)
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
citation_count: 79
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0R074
- **Protein Description:** RecName: Full=Serine/threonine-protein {ECO:0000256|PROSITE-ProRule:PRU10027}; EC=2.7.11.1 {ECO:0000256|PROSITE-ProRule:PRU10027};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the protein kinase superfamily. Ser/Thr protein
- **Key Domains:** CDK. (IPR050108); CDK7. (IPR037770); Kinase-like_dom_sf. (IPR011009); Prot_kinase_dom. (IPR000719); Protein_kinase_ATP_BS. (IPR017441)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CDK7" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CDK7' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CDK7** (gene ID: CDK7, UniProt: A0A9L0R074) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CDK7 (cyclin-dependent kinase 7) in the horse, *Equus caballus* (UniProt A0A9L0R074)

## 1. Introduction and summary

UniProt A0A9L0R074 is an unreviewed (TrEMBL) 415-residue horse protein, predicted automatically from the Thoroughbred reference genome. Its name, "Serine/threonine-protein", is a truncated automatic label. The entry assigns EC 2.7.11.1, 2.7.11.22 (cyclin-dependent kinase) and 2.7.11.23 ([RNA-polymerase]-subunit kinase) by rule-based annotation. It places the protein in the CMGC kinase group, CDC2/CDKX subfamily, with a CDK7-specific InterPro signature (IPR037770), PANTHER subfamily PTHR24056:SF0 "cyclin-dependent kinase 7" and the CDD model cd07841 (STKc_CDK7) [uniprot-A0A9L0R074-entry; wade-2009-horsegenome-abstract]. The Ensembl cross-reference for the underlying translation (ENSECAP00000055752) describes it as "Cyclin-dependent kinase 7". The horse proteome holds several other unreviewed CDK7 entries of different lengths, including K9K3U4 (346 residues, the same length as human CDK7) [uniprot-horse-CDK7-entries]. This fits a gene with several annotated transcript models, of which A0A9L0R074 is one.

**Identity check.** I aligned A0A9L0R074 directly against reviewed human CDK7 (P50613, 346 aa). Over residues 1–339 the two are 96.8% identical, with only 11 substitutions, all of them conservative or outside the catalytic core. Every functionally defined residue is conserved: the ATP-binding lysine K41, the catalytic-loop aspartate D137 (the annotated proton acceptor), the DFG aspartate D155, both T-loop phosphorylation sites (S164 and T170), and C312, the cysteine targeted by covalent CDK7 inhibitors.

The sequences diverge only after residue 339. Human CDK7 ends ...EALEQGGLPKKLIF (346), whereas the horse model continues with a different 76-residue tail (...EALEQGVAVKIQLSHHRHWV...LLPKNWP) [uniprot-A0A9L0R074-entry; uniprot-P50613-human-CDK7]. The gene symbol CDK7 is therefore unambiguous for this protein, which is the horse ortholog of CDK7. It is very likely a gene-model or alternative-splice variant differing only at the extreme C-terminus (see Section 8). No experimental literature exists on horse CDK7 itself. Everything below about function is inferred from the near-identical human protein and from the deeply conserved biology of CDK7 in vertebrates, insects and fungi, and the report says so wherever it relies on that inference.

**Function in brief.** CDK7 is an ATP-dependent serine/threonine protein kinase that works only as part of the trimeric CDK-activating kinase (CAK), with cyclin H and the RING-finger assembly factor MAT1 [fisher-1994-cyclinh-abstract; makela-1994-cyclinh-abstract; devault-1995-mat1-abstract; tassan-1995-mat1-abstract]. It has two linked roles. In its cell-cycle role, as the CDK-activating kinase, it phosphorylates the activation-segment (T-loop) threonine of the cell-cycle CDKs: CDK1 Thr161, CDK2 Thr160, and CDK4/6 Thr172 [fesquet-1993-mo15-abstract; matsuoka-1994-cdk4-abstract; larochelle-2007-chemgen-abstract; schachter-2013-cdk4-abstract]. In its transcription role, as the kinase subunit of the general transcription factor TFIIH, it phosphorylates Ser5 and Ser7 of the heptad repeats (YSPTSPS) in the C-terminal domain (CTD) of RNA polymerase II subunit RPB1 [roy-1994-tfiih-abstract; serizawa-1995-tfiih-abstract; shiekhattar-1995-tfiih-abstract; akhtar-2009-ctd-abstract; glovercutter-2009-ser7-abstract]. It also activates the transcriptional CDKs CDK9, CDK12 and CDK13 by T-loop phosphorylation [larochelle-2012-pausing-abstract; rimel-2020-targets-abstract].

CDK7 acts in the nucleus, where TFIIH-bound and free CAK pools coexist [tassan-1995-mat1-abstract; adamczewski-1996-mat1-abstract; uniprot-A0A9L0R074-entry].

## 2. Discovery, subunit composition and assembly of the CAK

CDK7 was first identified as MO15, a Xenopus kinase cloned by homology. Biochemical purification of the activity that turns on cdc2 in starfish oocytes then showed that MO15 is the catalytic subunit of a kinase that "activates cdc2-cdks complexes through phosphorylation of Thr161 (or its homologues)". Depleting MO15 from Xenopus egg extracts removed CAK activity [fesquet-1993-mo15-abstract]. In 1994 two groups identified the regulatory partner. Fisher and Morgan purified mammalian CAK as a 42/37-kDa heterodimer, cloned the 37-kDa subunit as a new cyclin (cyclin H), and reconstituted activity in vitro, establishing that MO15 is itself a cyclin-dependent kinase, CDK7 [fisher-1994-cyclinh-abstract]. Mäkelä and colleagues found cyclin H as a MO15 partner in a two-hybrid screen and showed that it enhances MO15 activity toward CDK2/cyclin A [makela-1994-cyclinh-abstract]. Mouse MO15 combined with cyclin H also phosphorylated and activated cyclin D–CDK4 at Thr172, extending CAK specificity to the G1 CDKs. Notably, CAK activity was present at constant levels throughout the cell cycle and in quiescent cells [matsuoka-1994-cdk4-abstract].

A third subunit, MAT1 ("ménage à trois"), was then found in starfish and Xenopus CAK. It is a RING-finger protein that stabilizes the cyclin H–CDK7 complex [devault-1995-mat1-abstract]. In the human system, stoichiometric MAT1 was required to reconstitute an active CDK7–cyclin H complex in vitro. MAT1 was associated with nuclear CDK7–cyclin H at all cell-cycle stages, and the ternary complex phosphorylated both T-loop and CTD substrates [tassan-1995-mat1-abstract]. Fisher and colleagues showed that there are two routes to an active CDK7–cyclin H complex. One is MAT1(p36)-dependent assembly, which does not need T170 phosphorylation. The other is a MAT1-independent route that requires T170 to be phosphorylated by a "CAK-activating kinase" [fisher-1995-cakassembly-abstract]. Both regulatory residues, S164 and T170, are conserved in the horse protein [uniprot-A0A9L0R074-entry; uniprot-P50613-human-CDK7]. MAT1 was later shown to bind tightly to CDK7 and cyclin H and to stimulate kinase activity even where it is not strictly needed for complex formation [adamczewski-1996-mat1-abstract].

## 3. Catalytic activity and substrate specificity

CDK7 catalyses the ATP-dependent transfer of the γ-phosphate to serine or threonine hydroxyls of protein substrates (L-seryl/L-threonyl-[protein] + ATP → O-phospho-[protein] + ADP + H+). It is unusual among CDKs because it recognizes two structurally unrelated classes of substrate [fisher-2005-review-abstract].

The first class is the activation segment of other CDKs. Here CDK7 phosphorylates a threonine (CDK1 T161, CDK2 T160, CDK4/6 T172) that is required for their full activity [fesquet-1993-mo15-abstract; fisher-1994-cyclinh-abstract; matsuoka-1994-cdk4-abstract]. CAK binds monomeric CDK2 as well as cyclin-bound CDK2, preferring the cyclin-bound form [fisher-1994-cyclinh-abstract; uniprot-A0A9L0R074-entry].

The second class is the RNA polymerase II CTD, whose consensus repeat Y1S2P3T4S5P6S7 is phosphorylated by CDK7 on Ser5 and Ser7. Akhtar et al. showed that yeast Kin28 and its human counterpart CDK7 are Ser7 kinases as well as the long-recognized Ser5 kinase, placing "bivalent" Ser5/Ser7 marks early in transcription [akhtar-2009-ctd-abstract]. In human analog-sensitive CDK7 (CDK7as) cells, CDK7 was a major Ser7 kinase and contributed, together with CDK9, to Ser5 phosphorylation. Both TFIIH and recombinant CDK7–cyclin H–MAT1 phosphorylated Ser5 and Ser7 in vitro [glovercutter-2009-ser7-abstract].

Beyond these two classes, quantitative phosphoproteomics with the selective covalent inhibitor SY-351 found hundreds of high-confidence CDK7 targets in human cells. Transcription- and splicing-associated proteins dominated, including SF3B1 and U2AF2, and CDK7 inhibition caused widespread splicing defects [rimel-2020-targets-abstract]. The same study showed that CDK7 directly activates CDK9, CDK12 and CDK13. This, together with the earlier evidence that CDK7 is required for the activating phosphorylation of CDK9 in vivo [larochelle-2012-pausing-abstract], makes CDK7 a "master regulator" CAK for the transcriptional CDKs as well as the cell-cycle CDKs [rimel-2020-targets-abstract].

Substrate choice also depends on which complex CDK7 is in: TFIIH restricts CDK7 activity largely to the Pol II CTD. Other substrates such as SPT5 and SF3B1 are phosphorylated preferentially by the free three-subunit CAK [rimel-2020-targets-abstract]. The CAK assembly state therefore helps determine substrate choice.

CDK7 also phosphorylates sequence-specific transcription factors, which links the basal machinery to signal-dependent gene activation. Free CAK and TFIIH both phosphorylated Ser77 in the AF-1 activation domain of retinoic acid receptor α. RARα bound CAK and TFIIH, and co-expressing CDK7 increased Ser77 phosphorylation and RARα transactivation in cells. This was the first example of a transactivator being activated by phosphorylation from a general transcription factor [rocheteegly-1997-rara-abstract]. Similarly, TFIIH-associated CDK7 phosphorylates estrogen receptor α at Ser118 in a ligand-dependent way. This requires a ligand-regulated contact between the receptor's AF2 helix 12 and the TFIIH core subunits p62 and XPD [chen-2000-er-abstract]. These receptor sites, like the CTD heptad, are proline-directed serines, which fits (as an inference, not a tested specificity rule) with the general CMGC-family preference for Ser/Thr-Pro motifs.

## 4. Structural basis of activation

The 3-Å crystal structure of monomeric human CDK7 bound to ATP showed a canonical bilobal kinase fold in an inactive conformation, similar to inactive CDK2, even though T170 was phosphorylated [lolli-2004-structure-abstract]. Two structures of the trimeric complex in 2020 explained the requirement for both partners.

Greber et al. solved the human CAK catalytic module alone and bound to the covalent inhibitor THZ1. MAT1 substantially extends the CDK7–cyclin H interface, which explains its role as an assembly factor, and it contacts the CDK7 T-loop in a way that may enhance activity [greber-2020-cryoem-abstract]. In this structure the T-loop residues S164 and T170 sit near positively charged residues. The CDK7 C-terminal region is poorly ordered and "only visible until residue C312", and THZ1 "is bound in the ATP-binding pocket of CDK7 and stretches to the covalently modified cysteine C312" [greber-2020-cryoem-fulltext].

Peissert et al. solved the *Chaetomium thermophilum* CAK at 2.6 Å. Together with mutagenesis, it showed that CDK7 can be activated by MAT1 alone, independent of T-loop phosphorylation, because MAT1 positions the T-loop in its active conformation. T170 phosphorylation instead tunes activity and substrate preference [peissert-2020-structure-abstract; peissert-2020-structure-fulltext].

The horse protein conserves the whole kinase domain (residues 12–295), the T-loop and C312 [uniprot-A0A9L0R074-entry]. Its divergent tail starts after residue 339, beyond the last residue ordered in the human structure. So the structural mechanism of activation by cyclin H and MAT1 should apply to it essentially unchanged (an inference).

## 5. Role in the cell cycle: the metazoan CDK-activating kinase

Whether CDK7 is the physiological CAK was debated at first. In budding yeast, CAK activity comes from the unrelated monomeric kinase Cak1/Civ1, and the yeast CDK7 ortholog Kin28 acts only in TFIIH [larochelle-1998-drosophila-abstract]. Genetic evidence in metazoans settled the question. Drosophila *cdk7* null and temperature-sensitive mutants lacked CAK activity in vivo, failed to activate Cdc2/cyclin A and Cdc2/cyclin B, and could not divide [larochelle-1998-drosophila-abstract].

In human cells, Larochelle et al. replaced wild-type CDK7 with an analog-sensitive allele. Inhibiting CDK7 in G1 blocked activation, though not formation, of CDK2/cyclin complexes and delayed S phase. Inhibiting it in G2 blocked mitotic entry and disrupted CDK1/cyclin B assembly, showing that for CDK1 the cyclin-binding and T-loop phosphorylation steps depend on each other [larochelle-2007-chemgen-abstract]. Schachter et al. extended this to G1. CDK7 is the CDK4- and CDK6-activating kinase, and it is needed continuously to maintain their activity. CDK7's own activating phosphorylation rises as cells leave quiescence, setting up a CDK7→CDK4 T-loop cascade that may limit the rate of restriction-point passage [schachter-2013-cdk4-abstract].

Mouse genetics agree. Mice lacking the CAK assembly factor Mat1 die around implantation, and their cells cannot enter S phase [rossi-2001-mat1mice-abstract]. Conditional inactivation of *Cdk7* showed it is essential for proliferation through phosphorylation of Cdk1 and Cdk2, although, unexpectedly, it was dispensable for global transcription in that setting. Removing Cdk7 from tissues with high turnover depleted adult stem cells and caused premature aging phenotypes [ganuza-2012-mice-abstract].

## 6. Role in RNA polymerase II transcription as the TFIIH kinase

Three independent studies in 1994–1995 showed that the CTD kinase of the general transcription factor TFIIH (also called BTF2) is MO15/CDK7 in complex with cyclin H [roy-1994-tfiih-abstract; serizawa-1995-tfiih-abstract; shiekhattar-1995-tfiih-abstract]. Antibodies against cyclin H or CDK7 inhibited TFIIH-dependent transcription and CTD phosphorylation within the preinitiation complex (PIC). CAK existed both inside TFIIH and as a smaller free complex [shiekhattar-1995-tfiih-abstract]. Through its association with TFIIH, CDK7 was also linked to nucleotide excision repair [roy-1994-tfiih-abstract]. TFIIH-associated kinase activity is constant through the cell cycle and falls after UV irradiation [adamczewski-1996-mat1-abstract].

Work on the budding yeast ortholog Kin28 first established the core logic of how CDK7 acts in transcription. Kin28 was identified as a subunit of TFIIH and of its kinase subassembly TFIIK. Feaver et al. showed that human CAK has the CTD kinase activity characteristic of TFIIH [feaver-1994-tfiik-abstract]. Chromatin immunoprecipitation showed that TFIIH-dependent Ser5 phosphorylation is concentrated at promoters, whereas Ser2 phosphorylation appears in coding regions, and that capping enzyme cross-links to promoters [komarnitsky-2000-ctdforms-abstract]. Genetic analysis showed that Kin28, but not the other CTD kinases, is needed in vivo to target the capping guanylyltransferase to Ser5-phosphorylated CTD [rodriguez-2000-kin28-abstract]. Together these results established that the TFIIH kinase couples transcription initiation to 5′ capping.

Selective chemical-genetic and pharmacological inhibition has since mapped CDK7 activity across the whole Pol II transcription cycle [fisher-2019-review-abstract]. At promoter escape and early elongation, CDK7 activity promotes TFIIE release and DSIF recruitment, establishing promoter-proximal pausing. CDK7 is also required for the activating phosphorylation of CDK9 (P-TEFb), which in turn drives pause release, Ser2 phosphorylation and histone H2B ubiquitylation. The authors described this as an "incoherent feed-forward" circuit governing the initiation-to-elongation switch [larochelle-2012-pausing-abstract]. Later in the cycle, CDK7 inhibition reduces NELF recruitment and pausing and delays termination [glovercutter-2009-ser7-abstract]. It also reduces capping-enzyme recruitment and alters H3K4me3 and H3K36me3 distributions, because TFIIH-phosphorylated CTD directly stimulates the SETD1A/B methyltransferases [ebmeier-2017-chromatin-abstract]. These effects are dose dependent: low inhibitor doses rapidly clear paused Pol II and alter gene expression and cell-cycle progression. Higher doses reduce bulk CTD phosphorylation and activate p53 [kelso-2014-pic-abstract]. Finally, recent evidence suggests TFIIH restrains CDK7 and that release of CAK from TFIIH may be needed for full kinase activation toward non-CTD substrates [rimel-2020-targets-abstract].

Because some tumors depend heavily on super-enhancer-driven transcription, CDK7 has become an anticancer target. The covalent inhibitor THZ1 reaches a cysteine outside the canonical kinase domain [kwiatkowski-2014-thz1-abstract], identified structurally as C312 [greber-2020-cryoem-fulltext]. This cysteine is conserved in the horse protein [uniprot-A0A9L0R074-entry].

## 7. Evolutionary conservation and divergence of CAK function

CDK7 orthologs are found across eukaryotes, but the coupling of its two roles differs between lineages, which is relevant when transferring annotations to the horse. In metazoans a single CDK7 acts as both the CAK and the TFIIH kinase. Genetic evidence for this comes from Drosophila [larochelle-1998-drosophila-abstract], human cells [larochelle-2007-chemgen-abstract; schachter-2013-cdk4-abstract] and mice [ganuza-2012-mice-abstract; rossi-2001-mat1mice-abstract]. In budding yeast the roles are split. The ortholog Kin28 functions as the TFIIH CTD kinase [feaver-1994-tfiik-abstract; rodriguez-2000-kin28-abstract], whereas CDK activation is done by the unrelated monomeric kinase Cak1/Civ1 [larochelle-1998-drosophila-abstract]. Fission yeast is intermediate. Its CDK7 ortholog Mcs6 and the Cak1-like kinase Csk1 are partially redundant CAKs for Cdc2, and Mcs6 is essential, implying other required functions such as transcription [lee-1999-mcs6-abstract]. Fisher has argued that despite this rewiring, every lineage keeps a connection between the CAK–CDK network and transcription [fisher-2005-review-abstract]. The horse belongs to the metazoan pattern. Its protein is 96.8% identical to human CDK7 over the catalytic and regulatory regions (Section 1), so the dual CAK/TFIIH role can be assigned to it with high confidence.

## 8. Subcellular localization and the horse-specific gene model

CDK7 works mainly in the nucleus. MAT1–CDK7–cyclin H complexes are nuclear at all cell-cycle stages in human cells [tassan-1995-mat1-abstract], and TFIIH, the transcription/repair site of CDK7 action, is a nuclear, promoter- and gene-associated complex [glovercutter-2009-ser7-abstract; shiekhattar-1995-tfiih-abstract]. UniProt annotates the horse protein as nuclear by automatic rule [uniprot-A0A9L0R074-entry]. Rimel et al. note that current models place CAK action on cell-cycle CDKs partly in the cytoplasm and TFIIH-associated CDK7 in the nucleus, but they state that this division is not firmly established [rimel-2020-targets-fulltext].

For the horse entry specifically, the most important open issue is the 76-residue C-terminal extension after residue 339. In human CDK7 this region lies beyond the ordered part of the protein in the CAK structure, which ends at C312 [greber-2020-cryoem-fulltext]. The novel horse sequence contains no recognizable domain annotation in UniProt, and the same gene has a 346-residue entry (K9K3U4) of the canonical length [uniprot-horse-CDK7-entries]. So A0A9L0R074 most likely represents an alternative 3′ exon or retained-intron transcript model rather than the main CDK7 product (an inference that needs transcript evidence to confirm). The core functions described above depend on the kinase domain, T-loop and cyclin H/MAT1 interfaces, all of which are intact. They should therefore apply, with the caveat that an altered C-terminus could in principle affect CAK/TFIIH incorporation or regulation in ways no one has tested.

## 9. Summary for functional annotation

Taking the evidence together, horse CDK7 (A0A9L0R074) can be annotated with high confidence, by orthology, as follows. Its molecular function is cyclin-dependent protein serine/threonine kinase activity (EC 2.7.11.22) together with RNA polymerase II CTD heptapeptide-repeat kinase activity (EC 2.7.11.23), phosphorylating Ser5 and Ser7 of the CTD, with ATP binding and cyclin binding [akhtar-2009-ctd-abstract; glovercutter-2009-ser7-abstract]. It is the catalytic subunit of the CDK-activating kinase complex (with CCNH and MNAT1) and of the TFIIH holocomplex [fisher-1994-cyclinh-abstract; tassan-1995-mat1-abstract; serizawa-1995-tfiih-abstract].

Its biological processes follow from these two complexes. Through the CAK it activates CDK1, CDK2, CDK4 and CDK6 by T-loop phosphorylation and so drives G1/S and G2/M progression [larochelle-2007-chemgen-abstract; schachter-2013-cdk4-abstract]. Through TFIIH it acts in RNA polymerase II transcription initiation, promoter escape and promoter-proximal pausing, and it activates CDK9, CDK12 and CDK13 [larochelle-2012-pausing-abstract; rimel-2020-targets-abstract]. It also contributes to co-transcriptional mRNA capping, histone methylation, splicing and 3′-end formation [ebmeier-2017-chromatin-abstract; rimel-2020-targets-abstract], and it supports nucleotide excision repair through TFIIH [roy-1994-tfiih-abstract]. It also phosphorylates the AF-1 domains of nuclear receptors such as RARα and ERα, linking hormone signaling to the basal machinery [rocheteegly-1997-rara-abstract; chen-2000-er-abstract]. Its cellular component is the nucleus, including the nucleoplasm, the TFIIH holocomplex and the CAK complex [tassan-1995-mat1-abstract].

## Open Questions

The first question is about the gene model itself. Is the 415-residue product with its divergent C-terminal tail actually expressed in horse tissues, and in what proportion relative to the canonical 346-residue form? RNA-seq junction analysis of horse CDK7 (on ECA21), Iso-Seq data, or proteomic detection of tail-specific peptides would answer this. If the variant is expressed, the next question is whether it still assembles into CAK and TFIIH, and whether the replaced C-terminus (which in human contains the disordered tail beyond C312) changes stability, nuclear import or regulation.

More broadly, several mechanistic questions remain open for CDK7 in any mammal. It is unclear how CDK7 is partitioned between free CAK and TFIIH, and what drives CAK release from TFIIH [rimel-2020-targets-abstract]. It is also unclear whether CAK activity toward CDK4/6 is regulated and could limit the rate of restriction-point passage [schachter-2013-cdk4-abstract], and how the mild transcriptional phenotype of *Cdk7* loss in some mouse cells fits with the strong transcriptional effects of acute inhibition [ganuza-2012-mice-abstract; kelso-2014-pic-abstract]. The full set of direct substrates is also still being defined [rimel-2020-targets-abstract].

Finally, CDK7 inhibitors such as THZ1 depend on C312, which is conserved in the horse. They could be useful for veterinary oncology research (for example equine sarcoids or melanoma), but no studies of CDK7 in horses have been reported.

## References

* [uniprot-A0A9L0R074-entry] UniProt Consortium. UniProtKB/TrEMBL entry A0A9L0R074_HORSE (Serine/threonine-protein; Equus caballus), entry version 15. https://rest.uniprot.org/uniprotkb/A0A9L0R074.txt (also citations/uniprot-A0A9L0R074.fasta)
* [uniprot-P50613-human-CDK7] UniProt Consortium. UniProtKB/Swiss-Prot entry P50613, CDK7_HUMAN. https://rest.uniprot.org/uniprotkb/P50613.fasta
* [uniprot-horse-CDK7-entries] UniProt Consortium. UniProtKB search gene:CDK7 AND organism_id:9796. https://rest.uniprot.org/uniprotkb/search?query=gene:CDK7+AND+organism_id:9796
* [adamczewski-1996-mat1] Adamczewski JP, Rossignol M, Tassan JP et al. (1996). MAT1, cdk7 and cyclin H form a kinase complex which is UV light-sensitive upon association with TFIIH. *The EMBO journal* 15:1877-84. PMID: 8617234; PMCID: PMC450106; https://pubmed.ncbi.nlm.nih.gov/8617234/
* [akhtar-2009-ctd] Akhtar MS, Heidemann M, Tietjen JR et al. (2009). TFIIH kinase places bivalent marks on the carboxy-terminal domain of RNA polymerase II. *Molecular cell* 34:387-93. PMID: 19450536; PMCID: PMC2757088; DOI: [10.1016/j.molcel.2009.04.016](https://doi.org/10.1016/j.molcel.2009.04.016); https://pubmed.ncbi.nlm.nih.gov/19450536/
* [chen-2000-er] Chen D, Riedl T, Washbrook E et al. (2000). Activation of estrogen receptor alpha by S118 phosphorylation involves a ligand-dependent interaction with TFIIH and participation of CDK7. *Molecular cell* 6:127-37. PMID: 10949034; https://pubmed.ncbi.nlm.nih.gov/10949034/
* [devault-1995-mat1] Devault A, Martinez AM, Fesquet D et al. (1995). MAT1 ('menage à trois') a new RING finger protein subunit stabilizing cyclin H-cdk7 complexes in starfish and Xenopus CAK. *The EMBO journal* 14:5027-36. PMID: 7588631; PMCID: PMC394606; DOI: [10.1002/j.1460-2075.1995.tb00185.x](https://doi.org/10.1002/j.1460-2075.1995.tb00185.x); https://pubmed.ncbi.nlm.nih.gov/7588631/
* [ebmeier-2017-chromatin] Ebmeier CC, Erickson B, Allen BL et al. (2017). Human TFIIH Kinase CDK7 Regulates Transcription-Associated Chromatin Modifications. *Cell reports* 20:1173-1186. PMID: 28768201; PMCID: PMC5564226; DOI: [10.1016/j.celrep.2017.07.021](https://doi.org/10.1016/j.celrep.2017.07.021); https://pubmed.ncbi.nlm.nih.gov/28768201/
* [feaver-1994-tfiik] Feaver WJ, Svejstrup JQ, Henry NL et al. (1994). Relationship of CDK-activating kinase and RNA polymerase II CTD kinase TFIIH/TFIIK. *Cell* 79:1103-9. PMID: 8001136; DOI: [10.1016/0092-8674(94)90040-x](https://doi.org/10.1016/0092-8674(94)90040-x); https://pubmed.ncbi.nlm.nih.gov/8001136/
* [fesquet-1993-mo15] Fesquet D, Labbé JC, Derancourt J et al. (1993). The MO15 gene encodes the catalytic subunit of a protein kinase that activates cdc2 and other cyclin-dependent kinases (CDKs) through phosphorylation of Thr161 and its homologues. *The EMBO journal* 12:3111-21. PMID: 8344251; PMCID: PMC413577; DOI: [10.1002/j.1460-2075.1993.tb05980.x](https://doi.org/10.1002/j.1460-2075.1993.tb05980.x); https://pubmed.ncbi.nlm.nih.gov/8344251/
* [fisher-1994-cyclinh] Fisher RP, Morgan DO (1994). A novel cyclin associates with MO15/CDK7 to form the CDK-activating kinase. *Cell* 78:713-24. PMID: 8069918; DOI: [10.1016/0092-8674(94)90535-5](https://doi.org/10.1016/0092-8674(94)90535-5); https://pubmed.ncbi.nlm.nih.gov/8069918/
* [fisher-1995-cakassembly] Fisher RP, Jin P, Chamberlin HM et al. (1995). Alternative mechanisms of CAK assembly require an assembly factor or an activating kinase. *Cell* 83:47-57. PMID: 7553872; DOI: [10.1016/0092-8674(95)90233-3](https://doi.org/10.1016/0092-8674(95)90233-3); https://pubmed.ncbi.nlm.nih.gov/7553872/
* [fisher-2005-review] Fisher RP (2005). Secrets of a double agent: CDK7 in cell-cycle control and transcription. *Journal of cell science* 118:5171-80. PMID: 16280550; DOI: [10.1242/jcs.02718](https://doi.org/10.1242/jcs.02718); https://pubmed.ncbi.nlm.nih.gov/16280550/
* [fisher-2019-review] Fisher RP (2019). Cdk7: a kinase at the core of transcription and in the crosshairs of cancer drug discovery. *Transcription* 10:47-56. PMID: 30488763; PMCID: PMC6602562; DOI: [10.1080/21541264.2018.1553483](https://doi.org/10.1080/21541264.2018.1553483); https://pubmed.ncbi.nlm.nih.gov/30488763/
* [ganuza-2012-mice] Ganuza M, Sáiz-Ladera C, Cañamero M et al. (2012). Genetic inactivation of Cdk7 leads to cell cycle arrest and induces premature aging due to adult stem cell exhaustion. *The EMBO journal* 31:2498-510. PMID: 22505032; PMCID: PMC3365431; DOI: [10.1038/emboj.2012.94](https://doi.org/10.1038/emboj.2012.94); https://pubmed.ncbi.nlm.nih.gov/22505032/
* [glovercutter-2009-ser7] Glover-Cutter K, Larochelle S, Erickson B et al. (2009). TFIIH-associated Cdk7 kinase functions in phosphorylation of C-terminal domain Ser7 residues, promoter-proximal pausing, and termination by RNA polymerase II. *Molecular and cellular biology* 29:5455-64. PMID: 19667075; PMCID: PMC2756882; DOI: [10.1128/MCB.00637-09](https://doi.org/10.1128/MCB.00637-09); https://pubmed.ncbi.nlm.nih.gov/19667075/
* [greber-2020-cryoem] Greber BJ, Perez-Bertoldi JM, Lim K et al. (2020). The cryoelectron microscopy structure of the human CDK-activating kinase. *Proceedings of the National Academy of Sciences of the United States of America* 117:22849-22857. PMID: 32855301; PMCID: PMC7502720; DOI: [10.1073/pnas.2009627117](https://doi.org/10.1073/pnas.2009627117); https://pubmed.ncbi.nlm.nih.gov/32855301/
* [kelso-2014-pic] Kelso TW, Baumgart K, Eickhoff J et al. (2014). Cyclin-dependent kinase 7 controls mRNA synthesis by affecting stability of preinitiation complexes, leading to altered gene expression, cell cycle progression, and survival of tumor cells. *Molecular and cellular biology* 34:3675-88. PMID: 25047832; PMCID: PMC4187722; DOI: [10.1128/MCB.00595-14](https://doi.org/10.1128/MCB.00595-14); https://pubmed.ncbi.nlm.nih.gov/25047832/
* [komarnitsky-2000-ctdforms] Komarnitsky P, Cho EJ, Buratowski S (2000). Different phosphorylated forms of RNA polymerase II and associated mRNA processing factors during transcription. *Genes & development* 14:2452-60. PMID: 11018013; PMCID: PMC316976; DOI: [10.1101/gad.824700](https://doi.org/10.1101/gad.824700); https://pubmed.ncbi.nlm.nih.gov/11018013/
* [kwiatkowski-2014-thz1] Kwiatkowski N, Zhang T, Rahl PB et al. (2014). Targeting transcription regulation in cancer with a covalent CDK7 inhibitor. *Nature* 511:616-20. PMID: 25043025; PMCID: PMC4244910; DOI: [10.1038/nature13393](https://doi.org/10.1038/nature13393); https://pubmed.ncbi.nlm.nih.gov/25043025/
* [larochelle-1998-drosophila] Larochelle S, Pandur J, Fisher RP et al. (1998). Cdk7 is essential for mitosis and for in vivo Cdk-activating kinase activity. *Genes & development* 12:370-81. PMID: 9450931; PMCID: PMC316490; DOI: [10.1101/gad.12.3.370](https://doi.org/10.1101/gad.12.3.370); https://pubmed.ncbi.nlm.nih.gov/9450931/
* [larochelle-2007-chemgen] Larochelle S, Merrick KA, Terret ME et al. (2007). Requirements for Cdk7 in the assembly of Cdk1/cyclin B and activation of Cdk2 revealed by chemical genetics in human cells. *Molecular cell* 25:839-50. PMID: 17386261; PMCID: PMC1858677; DOI: [10.1016/j.molcel.2007.02.003](https://doi.org/10.1016/j.molcel.2007.02.003); https://pubmed.ncbi.nlm.nih.gov/17386261/
* [larochelle-2012-pausing] Larochelle S, Amat R, Glover-Cutter K et al. (2012). Cyclin-dependent kinase control of the initiation-to-elongation switch of RNA polymerase II. *Nature structural & molecular biology* 19:1108-15. PMID: 23064645; PMCID: PMC3746743; DOI: [10.1038/nsmb.2399](https://doi.org/10.1038/nsmb.2399); https://pubmed.ncbi.nlm.nih.gov/23064645/
* [lee-1999-mcs6] Lee KM, Saiz JE, Barton WA et al. (1999). Cdc2 activation in fission yeast depends on Mcs6 and Csk1, two partially redundant Cdk-activating kinases (CAKs). *Current biology : CB* 9:441-4. PMID: 10226032; DOI: [10.1016/s0960-9822(99)80194-8](https://doi.org/10.1016/s0960-9822(99)80194-8); https://pubmed.ncbi.nlm.nih.gov/10226032/
* [lolli-2004-structure] Lolli G, Lowe ED, Brown NR et al. (2004). The crystal structure of human CDK7 and its protein recognition properties. *Structure (London, England : 1993)* 12:2067-79. PMID: 15530371; DOI: [10.1016/j.str.2004.08.013](https://doi.org/10.1016/j.str.2004.08.013); https://pubmed.ncbi.nlm.nih.gov/15530371/
* [makela-1994-cyclinh] Mäkelä TP, Tassan JP, Nigg EA et al. (1994). A cyclin associated with the CDK-activating kinase MO15. *Nature* 371:254-7. PMID: 8078587; DOI: [10.1038/371254a0](https://doi.org/10.1038/371254a0); https://pubmed.ncbi.nlm.nih.gov/8078587/
* [matsuoka-1994-cdk4] Matsuoka M, Kato JY, Fisher RP et al. (1994). Activation of cyclin-dependent kinase 4 (cdk4) by mouse MO15-associated kinase. *Molecular and cellular biology* 14:7265-75. PMID: 7935441; PMCID: PMC359261; DOI: [10.1128/mcb.14.11.7265-7275.1994](https://doi.org/10.1128/mcb.14.11.7265-7275.1994); https://pubmed.ncbi.nlm.nih.gov/7935441/
* [peissert-2020-structure] Peissert S, Schlosser A, Kendel R et al. (2020). Structural basis for CDK7 activation by MAT1 and Cyclin H. *Proceedings of the National Academy of Sciences of the United States of America* 117:26739-26748. PMID: 33055219; PMCID: PMC7604442; DOI: [10.1073/pnas.2010885117](https://doi.org/10.1073/pnas.2010885117); https://pubmed.ncbi.nlm.nih.gov/33055219/
* [rimel-2020-targets] Rimel JK, Poss ZC, Erickson B et al. (2020). Selective inhibition of CDK7 reveals high-confidence targets and new models for TFIIH function in transcription. *Genes & development* 34:1452-1473. PMID: 33060135; PMCID: PMC7608751; DOI: [10.1101/gad.341545.120](https://doi.org/10.1101/gad.341545.120); https://pubmed.ncbi.nlm.nih.gov/33060135/
* [rocheteegly-1997-rara] Rochette-Egly C, Adam S, Rossignol M et al. (1997). Stimulation of RAR alpha activation function AF-1 through binding to the general transcription factor TFIIH and phosphorylation by CDK7. *Cell* 90:97-107. PMID: 9230306; DOI: [10.1016/s0092-8674(00)80317-7](https://doi.org/10.1016/s0092-8674(00)80317-7); https://pubmed.ncbi.nlm.nih.gov/9230306/
* [rodriguez-2000-kin28] Rodriguez CR, Cho EJ, Keogh MC et al. (2000). Kin28, the TFIIH-associated carboxy-terminal domain kinase, facilitates the recruitment of mRNA processing machinery to RNA polymerase II. *Molecular and cellular biology* 20:104-12. PMID: 10594013; PMCID: PMC85066; DOI: [10.1128/MCB.20.1.104-112.2000](https://doi.org/10.1128/MCB.20.1.104-112.2000); https://pubmed.ncbi.nlm.nih.gov/10594013/
* [rossi-2001-mat1mice] Rossi DJ, Londesborough A, Korsisaari N et al. (2001). Inability to enter S phase and defective RNA polymerase II CTD phosphorylation in mice lacking Mat1. *The EMBO journal* 20:2844-56. PMID: 11387217; PMCID: PMC125252; DOI: [10.1093/emboj/20.11.2844](https://doi.org/10.1093/emboj/20.11.2844); https://pubmed.ncbi.nlm.nih.gov/11387217/
* [roy-1994-tfiih] Roy R, Adamczewski JP, Seroz T et al. (1994). The MO15 cell cycle kinase is associated with the TFIIH transcription-DNA repair factor. *Cell* 79:1093-101. PMID: 8001135; DOI: [10.1016/0092-8674(94)90039-6](https://doi.org/10.1016/0092-8674(94)90039-6); https://pubmed.ncbi.nlm.nih.gov/8001135/
* [schachter-2013-cdk4] Schachter MM, Merrick KA, Larochelle S et al. (2013). A Cdk7-Cdk4 T-loop phosphorylation cascade promotes G1 progression. *Molecular cell* 50:250-60. PMID: 23622515; PMCID: PMC3677717; DOI: [10.1016/j.molcel.2013.04.003](https://doi.org/10.1016/j.molcel.2013.04.003); https://pubmed.ncbi.nlm.nih.gov/23622515/
* [serizawa-1995-tfiih] Serizawa H, Mäkelä TP, Conaway JW et al. (1995). Association of Cdk-activating kinase subunits with transcription factor TFIIH. *Nature* 374:280-2. PMID: 7885450; DOI: [10.1038/374280a0](https://doi.org/10.1038/374280a0); https://pubmed.ncbi.nlm.nih.gov/7885450/
* [shiekhattar-1995-tfiih] Shiekhattar R, Mermelstein F, Fisher RP et al. (1995). Cdk-activating kinase complex is a component of human transcription factor TFIIH. *Nature* 374:283-7. PMID: 7533895; DOI: [10.1038/374283a0](https://doi.org/10.1038/374283a0); https://pubmed.ncbi.nlm.nih.gov/7533895/
* [tassan-1995-mat1] Tassan JP, Jaquenoud M, Fry AM et al. (1995). In vitro assembly of a functional human CDK7-cyclin H complex requires MAT1, a novel 36 kDa RING finger protein. *The EMBO journal* 14:5608-17. PMID: 8521818; PMCID: PMC394676; DOI: [10.1002/j.1460-2075.1995.tb00248.x](https://doi.org/10.1002/j.1460-2075.1995.tb00248.x); https://pubmed.ncbi.nlm.nih.gov/8521818/
* [wade-2009-horsegenome] Wade CM, Giulotto E, Sigurdsson S et al. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science (New York, N.Y.)* 326:865-7. PMID: 19892987; PMCID: PMC3785132; DOI: [10.1126/science.1178158](https://doi.org/10.1126/science.1178158); https://pubmed.ncbi.nlm.nih.gov/19892987/


## Citations

1. _metadata.json
2. adamczewski-1996-mat1-abstract.md
3. adamczewski-1996-mat1-summary.md
4. akhtar-2009-ctd-abstract.md
5. akhtar-2009-ctd-summary.md
6. chen-2000-er-abstract.md
7. chen-2000-er-summary.md
8. devault-1995-mat1-abstract.md
9. devault-1995-mat1-summary.md
10. ebmeier-2017-chromatin-abstract.md
11. ebmeier-2017-chromatin-summary.md
12. feaver-1994-tfiik-abstract.md
13. feaver-1994-tfiik-summary.md
14. fesquet-1993-mo15-abstract.md
15. fesquet-1993-mo15-summary.md
16. fisher-1994-cyclinh-abstract.md
17. fisher-1994-cyclinh-summary.md
18. fisher-1995-cakassembly-abstract.md
19. fisher-1995-cakassembly-summary.md
20. fisher-2005-review-abstract.md
21. fisher-2005-review-summary.md
22. fisher-2019-review-abstract.md
23. fisher-2019-review-summary.md
24. ganuza-2012-mice-abstract.md
25. ganuza-2012-mice-summary.md
26. glovercutter-2009-ser7-abstract.md
27. glovercutter-2009-ser7-summary.md
28. greber-2020-cryoem-abstract.md
29. greber-2020-cryoem-fulltext.txt
30. greber-2020-cryoem-summary.md
31. kelso-2014-pic-abstract.md
32. kelso-2014-pic-summary.md
33. komarnitsky-2000-ctdforms-abstract.md
34. komarnitsky-2000-ctdforms-summary.md
35. kwiatkowski-2014-thz1-abstract.md
36. kwiatkowski-2014-thz1-summary.md
37. larochelle-1998-drosophila-abstract.md
38. larochelle-1998-drosophila-summary.md
39. larochelle-2007-chemgen-abstract.md
40. larochelle-2007-chemgen-summary.md
41. larochelle-2012-pausing-abstract.md
42. larochelle-2012-pausing-fulltext.txt
43. larochelle-2012-pausing-summary.md
44. lee-1999-mcs6-abstract.md
45. lee-1999-mcs6-summary.md
46. lolli-2004-structure-abstract.md
47. lolli-2004-structure-summary.md
48. makela-1994-cyclinh-abstract.md
49. makela-1994-cyclinh-summary.md
50. matsuoka-1994-cdk4-abstract.md
51. matsuoka-1994-cdk4-summary.md
52. peissert-2020-structure-abstract.md
53. peissert-2020-structure-fulltext.txt
54. peissert-2020-structure-summary.md
55. rimel-2020-targets-abstract.md
56. rimel-2020-targets-fulltext.txt
57. rimel-2020-targets-summary.md
58. rocheteegly-1997-rara-abstract.md
59. rocheteegly-1997-rara-summary.md
60. rodriguez-2000-kin28-abstract.md
61. rodriguez-2000-kin28-summary.md
62. rossi-2001-mat1mice-abstract.md
63. rossi-2001-mat1mice-summary.md
64. roy-1994-tfiih-abstract.md
65. roy-1994-tfiih-summary.md
66. schachter-2013-cdk4-abstract.md
67. schachter-2013-cdk4-summary.md
68. serizawa-1995-tfiih-abstract.md
69. serizawa-1995-tfiih-summary.md
70. shiekhattar-1995-tfiih-abstract.md
71. shiekhattar-1995-tfiih-summary.md
72. tassan-1995-mat1-abstract.md
73. tassan-1995-mat1-summary.md
74. uniprot-A0A9L0R074-entry.txt
75. uniprot-A0A9L0R074.fasta
76. uniprot-P50613-human-CDK7.fasta
77. uniprot-horse-CDK7-entries.tsv
78. wade-2009-horsegenome-abstract.md
79. wade-2009-horsegenome-summary.md