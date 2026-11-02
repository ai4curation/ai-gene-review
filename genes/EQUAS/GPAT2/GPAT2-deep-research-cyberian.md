---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:48:20.756809'
end_time: '2026-10-25T23:56:21.979943'
duration_seconds: 481.22
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: GPAT2
  gene_symbol: GPAT2
  uniprot_accession: A0A9L0ILJ0
  protein_description: 'SubName: Full=Glycerol-3-phosphate acyltransferase 2, mitochondrial
    {ECO:0000313|Ensembl:ENSEASP00005037933.1};'
  gene_info: Name=GPAT2 {ECO:0000313|Ensembl:ENSEASP00005037933.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the GPAT/DAPAT family.
  protein_domains: GPAT/DHAPAT. (IPR022284); GPAT/DHAPAT_C. (IPR045520); GPAT/DHAPAT_LPLAT.
    (IPR041728); Plipid/glycerol_acylTrfase. (IPR002123); GPAT_C (PF19277)
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
citation_count: 60
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0ILJ0
- **Protein Description:** SubName: Full=Glycerol-3-phosphate acyltransferase 2, mitochondrial {ECO:0000313|Ensembl:ENSEASP00005037933.1};
- **Gene Information:** Name=GPAT2 {ECO:0000313|Ensembl:ENSEASP00005037933.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the GPAT/DAPAT family.
- **Key Domains:** GPAT/DHAPAT. (IPR022284); GPAT/DHAPAT_C. (IPR045520); GPAT/DHAPAT_LPLAT. (IPR041728); Plipid/glycerol_acylTrfase. (IPR002123); GPAT_C (PF19277)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GPAT2" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GPAT2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GPAT2** (gene ID: GPAT2, UniProt: A0A9L0ILJ0) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GPAT2 (Glycerol-3-phosphate acyltransferase 2, mitochondrial) in the donkey, *Equus asinus* (UniProt A0A9L0ILJ0)

## 1. Introduction and summary

The donkey protein A0A9L0ILJ0 is an unreviewed TrEMBL entry, named GPAT2 from the Ensembl gene model ENSEASG00005002382 on donkey chromosome 6. It is 718 residues long and belongs to the GPAT/DAPAT family. Its annotations are all electronic: phospholipid metabolism, a membrane location, and GO terms (glycerol-3-phosphate O-acyltransferase activity, mitochondrial membrane, triglyceride biosynthesis and piRNA processing) transferred by the TreeGrafter/PANTHER subfamily PTHR12563:SF15 (UniProt record, see `sequence_analysis/`). The protein was predicted from the chromosome-level genome of a male Dezhou donkey [wang-2020-donkey-genome-abstract]. No study has examined GPAT2 directly in the donkey or in any other equid. This report therefore takes everything it says about function from experiments on the mouse, rat and human orthologues. It first checks that those orthologues are the right comparison, and it marks every functional statement as inferred by orthology.

Taken together, the evidence shows that GPAT2 is an integral protein of the mitochondrial outer membrane. It has two jobs, both concentrated in male germ cells. In the first, it is a glycerolipid acyltransferase that catalyses the first committed step of de novo glycerolipid synthesis: it moves an acyl group from acyl-CoA to the *sn*-1 position of glycerol-3-phosphate, which gives lysophosphatidic acid (LPA) (EC 2.3.1.15) [wendel-2009-gpat-review-fulltext; wang-2007-gpat2-cloning-abstract]. Unlike the other GPAT isoforms, it is sensitive to *N*-ethylmaleimide (NEM) and strongly prefers arachidonoyl-CoA (20:4). It channels arachidonate into phosphatidic acid and triacylglycerol (TAG) in primary spermatocytes [lewin-2004-mtgpat2-abstract; cattaneo-2012-gpat2-arachidonic-fulltext]. In the second, it is a PIWIL2/MILI-binding protein of the mitochondrial surface that is needed for primary piRNA biogenesis, for silencing retrotransposons in the fetal male germline and for germ-cell survival. This second role is reported not to depend on its catalytic activity [shiromoto-2013-gpat2-pirna-abstract; shiromoto-2019-gpat2-pirna-abstract]. Under normal conditions GPAT2 expression is largely limited to the testis, where DNA methylation switches it on and off. It is re-expressed in several cancers, which makes it a cancer-testis gene [garcia-fabiani-2015-gpat2-methylation-fulltext; pellon-maison-2014-gpat2-cancer-testis-fulltext].

## 2. Identity verification and sequence-level evidence for orthology

Before transferring function, we checked that the donkey sequence is a true orthologue of the characterised mammalian GPAT2 proteins and not some other acyltransferase. A global alignment (BLOSUM62) of the donkey protein against human GPAT2 (Q6NUI2, 795 aa) and mouse Gpat2 (Q14DK4, 801 aa) gave 81.5% and 78.6% identity over the aligned columns (`sequence_analysis/alignment_summary.txt`). These values fit one-to-one orthology among eutherian mammals. They are far higher than the roughly 27% identity reported between mouse GPAT2 and its paralogue GPAT1 [wang-2007-gpat2-cloning-abstract]. The gene symbol, the UniProt description, the InterPro domains (GPAT/DHAPAT, IPR022284; its LPLAT and C-terminal subdomains, IPR041728 and IPR045520; the phospholipid/glycerol acyltransferase domain, IPR002123) and the PANTHER subfamily all agree with the literature on mammalian GPAT2. The symbol is not ambiguous within mammals. The name "GPAT2" is also used for unrelated plant (*Arabidopsis*) and algal (*Phaeodactylum*) glycerol-3-phosphate acyltransferases, which turned up in literature searches; those were left out as non-orthologous.

The four acyltransferase blocks that define the glycerolipid acyltransferase family were found in the sequence by inspection. In this family, the invariant histidine and aspartate of block I, the glycine of block III and the proline of block IV are needed for catalysis, while the phenylalanine and arginine of block II and the glutamate and serine of block III bind glycerol-3-phosphate [lewin-1999-gpat-motifs-abstract; wendel-2009-gpat-review-fulltext]. The donkey protein has the block I catalytic dyad as "STHKSLLD" (residues 203–210, with the H-x4-D motif at His205/Asp210). It also has a block II-like "LGGLFL" segment near residue 247, a block III-like "FLEE" near residue 288 and a block IV-like "VPVAITYD" near residue 326. Human and mouse GPAT2 have the same motifs at the same positions (`sequence_analysis/alignment_summary.txt`), and UniProt's SMART annotation places the PlsC acyltransferase domain at residues 199–333. This conservation supports a catalytically competent enzyme. The donkey model does differ from human GPAT2 at the C-terminus: the two proteins agree closely up to about residue 630, after which the donkey sequence becomes divergent and stops at 718 residues, while human GPAT2 is 795. That pattern points to a gene-model problem (a mispredicted last exon or a frameshift) more than to true biology, and the region should not be over-interpreted. It lies outside the catalytic domain.

## 3. Enzymatic activity and substrate specificity

GPAT2 was first found as an activity, not as a gene. In mice lacking the major mitochondrial isoform GPAT1, liver mitochondria kept a GPAT activity and a protein that reacted with anti-GPAT1 antibodies but had a different isoelectric point. Unlike GPAT1, this activity was inactivated by NEM, did not prefer palmitoyl-CoA over oleoyl-CoA, was inhibited by dihydroxyacetone phosphate and polymyxin B, was temperature-sensitive and was not activated by acetone. On this basis it was named mtGPAT2 [lewin-2004-mtgpat2-abstract]. Cloning from mouse testis then gave a 798-residue open reading frame (calculated mass 88.8 kDa). Transfecting it into Cos-7 cells raised NEM-sensitive GPAT activity by only about 30% but raised the incorporation of [14C]oleate into TAG by 84% [wang-2007-gpat2-cloning-abstract]. Reviews of the mammalian GPAT family describe GPAT2 as a minor, NEM-sensitive mitochondrial isoform. It can start TAG synthesis in cultured cells, but it cannot stand in for GPAT1 in the liver [gimeno-2008-gpat-review-abstract; wendel-2009-gpat-review-fulltext].

The key finding on substrate preference came from Cattaneo and colleagues. They expressed GPAT2 in CHO-K1 and Vero cells and found no change in total or NEM-sensitive GPAT activity with palmitoyl-, oleoyl- or linoleoyl-CoA. With arachidonoyl-CoA, however, specific activity doubled, and this increase was NEM-sensitive. Two other polyunsaturated donors, eicosapentaenoyl-CoA (20:5 n-3) and docosahexaenoyl-CoA (22:6 n-3), were not used [cattaneo-2012-gpat2-arachidonic-fulltext]. The main radiolabelled product was phosphatidic acid (PA), not LPA. Membranes from GPAT2-expressing cells also showed higher 1-acylglycerol-3-phosphate acyltransferase (AGPAT/LPAAT, EC 2.3.1.51) activity, about 2-fold with arachidonoyl-CoA and about 50% with oleoyl-CoA. The authors therefore could not rule out that the recombinant protein carries both GPAT and AGPAT activity [cattaneo-2012-gpat2-arachidonic-fulltext]. The AGPAT activity with oleoyl-CoA may also explain the earlier result that oleate incorporation into TAG rose even though no oleoyl-CoA GPAT activity could be detected [cattaneo-2012-gpat2-arachidonic-fulltext; wang-2007-gpat2-cloning-abstract]. In cells, the enzyme raised [14C]arachidonate incorporation into TAG by 40%, enlarged lipid droplets and made arachidonate detectable in TAG (about 6% of TAG fatty acids), which it was not in control cells [cattaneo-2012-gpat2-arachidonic-fulltext]. For the donkey orthologue, the best-supported molecular function is therefore glycerol-3-phosphate *O*-acyltransferase activity (sn-glycerol 3-phosphate + acyl-CoA → 1-acyl-sn-glycero-3-phosphate + CoA) with a preference for arachidonoyl-CoA. A secondary acylation of LPA to PA is possible. Both are inferred from rodent orthologues. A caveat applies: every activity measurement so far comes from crude membranes of overexpressing cells, with no purified protein and no full kinetic analysis. This is one reason one study describes GPAT2 as "originally annotated as encoding a glycerol-3-phosphate acyltransferase by sequence homology" [garcia-fabiani-2015-gpat2-methylation-fulltext].

## 4. Subcellular localisation and membrane topology

Mitochondrial localisation is established by several lines of evidence. The original activity co-fractionated with mitochondria and not with microsomes [lewin-2004-mtgpat2-abstract], and confocal microscopy of tagged mouse GPAT2 confirmed a mitochondrial location [wang-2007-gpat2-cloning-abstract]. Later work placed GPAT2 on the mitochondrial outer membrane of germ cells, consistent with its partner PIWIL2 [shiromoto-2013-gpat2-pirna-abstract; shiromoto-2019-gpat2-pirna-abstract]. A recent survey of piRNA machinery counts GPAT2 among five mitochondria-anchored piRNA biogenesis proteins, alongside TDRKH, ASZ1, mitoPLD and PNLDC1 [gao-2025-piwi-mito-tether-fulltext]. GFP-tagged GPAT2 expressed alone in HeLa cells colocalises completely with MitoTracker. This shows that its transmembrane regions anchor it to mitochondria without help from any germ-cell partner [yan-2026-piwi-scaffolds-fulltext]. A topology study in HEK293 cells showed that mouse GPAT2 is an integral membrane protein: it resists carbonate extraction, has two transmembrane segments, and has both its N- and C-termini facing the cytosol. Acyltransferase motifs I–III sit on the cytosolic side and motif IV lies within the membrane [nakagawa-2012-gpat2-topology-abstract]. With its active site facing the cytosol, the enzyme can reach the cytosolic acyl-CoA pool. There, like GPAT1, it competes with carnitine palmitoyltransferase-1 for acyl-CoAs that could otherwise be sent to β-oxidation [wendel-2009-gpat-review-fulltext]. The electronic GO term "mitochondrial membrane" on the donkey entry agrees with this. On the evidence, the more precise term is mitochondrial outer membrane, with the protein oriented toward the cytosol.

## 5. Biochemical pathway context: glycerolipid synthesis and arachidonate handling in germ cells

In the glycerol-3-phosphate (Kennedy) pathway, a GPAT makes LPA, an AGPAT converts LPA to PA, lipin phosphatases make diacylglycerol, and diacylglycerol acyltransferases make TAG. PA and diacylglycerol are also the branch points for glycerophospholipid synthesis [wendel-2009-gpat-review-fulltext]. Mammals have four GPAT isoforms: GPAT1 and GPAT2 in the outer mitochondrial membrane, GPAT3 and GPAT4 in the endoplasmic reticulum. They differ in tissue distribution, acyl-CoA preference and NEM sensitivity, and are thought to send fatty acids toward different metabolic fates [gimeno-2008-gpat-review-abstract; wendel-2009-gpat-review-fulltext]. GPAT2 stands out because it is barely expressed in lipogenic tissues and is not regulated by nutrition. Its mRNA is about 50-fold higher in testis than in liver or brown fat, and fasting or refeeding does not change it [wang-2007-gpat2-cloning-abstract]. It is also not induced when adipocytes differentiate [garcia-fabiani-2015-gpat2-methylation-fulltext].

Its physiological substrate and its tissue therefore match. In rat and mouse testis, *Gpat2* mRNA is found only in primary spermatocytes. During rat sexual maturation, testicular TAG content and the arachidonate content of TAG both peak at 30 days, together with the highest GPAT2 mRNA and protein levels [cattaneo-2012-gpat2-arachidonic-fulltext]. The leading model is that GPAT2 esterifies arachidonate into a TAG store in meiotic germ cells. Work in cancer cells supports a protective, buffering role for this activity. In MDA-MB-231 breast cancer cells, silencing GPAT2 changed the arachidonate content of glycerolipids and led to compensatory up-regulation of another arachidonate-using acyltransferase, AGPAT11/LPCAT2 [cattaneo-2017-gpat2-afm-fulltext]. Exogenous arachidonic acid killed only GPAT2-silenced cells, through BNIP3-associated apoptosis, and up-regulating other eicosanoid-pathway genes did not compensate [ferremi-2024-gpat2-apoptosis-fulltext]. This fits a model in which GPAT2 takes up free arachidonate, which is pro-apoptotic, and stores it in neutral lipid. That role could plausibly protect spermatocytes during meiosis, but it has not been tested directly in germ cells.

## 6. A non-catalytic role in piRNA biogenesis and germline genome defence

A separate line of research shows that GPAT2 is a component of the PIWI-interacting RNA (piRNA) pathway. Using germline stem (GS) cells that were MILI-null or rescued with MILI, Shiromoto and colleagues found that GPAT2 binds MILI (PIWIL2) and that knocking down GPAT2 impairs primary piRNA production. They concluded that GPAT2 is essential for primary piRNA biogenesis [shiromoto-2013-gpat2-pirna-abstract]. In a follow-up, the same group reported that this function is independent of GPAT2's LPA-generating activity. *Gpat2*-deficient mice had defective piRNA production, de-silencing of IAP and LINE-1 retrotransposons in fetal testes and apoptosis of pachytene spermatocytes, the same phenotype as *Piwil2*/*Mili* mutants. They also had neonatal spermatogonial apoptosis, which *Piwil2* mutants do not, pointing to an extra GPAT2-specific survival function [shiromoto-2019-gpat2-pirna-abstract]. In vivo knockdown of *Gpat2* in mouse testis by lentiviral shRNA likewise arrested spermatogenesis at pachytene, activated apoptotic genes and reduced reproductive fitness [garcia-fabiani-2017-gpat2-spermatogenesis-abstract]. Outside the germline, silencing GPAT2 in breast cancer cells changed the abundance and length distribution of piRNAs, tRNA-derived fragments and miRNAs [lacunza-2018-gpat2-smallrna-fulltext]. This suggests that GPAT2 can affect small-RNA biogenesis wherever it is expressed.

How GPAT2 supports piRNA processing is still unknown. piRNA biogenesis takes place in the intermitochondrial cement (IMC), where outer-membrane anchors recruit PIWI proteins. In a systematic HeLa-cell recruitment assay, ASZ1 recruited PIWIL2 to mitochondria and TDRKH recruited PIWIL1 and PIWIL4, whereas GPAT2 (like mitoPLD) did not visibly recruit any of 19 piRNA pathway proteins tested [gao-2025-piwi-mito-tether-fulltext]. An independent study confirmed that GPAT2 does not recruit MILI to mitochondria in HeLa cells, while ASZ1 does. In adult mouse testis, however, immunoprecipitation of ASZ1 followed by mass spectrometry significantly enriched GPAT2 together with MOV10L1 and MILI, and not the other anchor, TDRKH [yan-2026-piwi-scaffolds-fulltext]. GPAT2 therefore sits inside the ASZ1–MILI–MOV10L1 mitochondrial piRNA-processing complex of pachytene spermatocytes, but it is probably not the protein that first recruits MILI. So although GPAT2 associates with PIWIL2 and its partners in germ cells, it does not seem to be the primary scaffold that brings PIWI proteins to mitochondria. Its contribution may lie further downstream, for example in shaping the local lipid environment of the IMC, in an unidentified adaptor function, or in its additional anti-apoptotic role [gao-2025-piwi-mito-tether-fulltext; shiromoto-2019-gpat2-pirna-abstract]. Because the donkey protein conserves the structural core of the rodent orthologue (Section 2), the IEA annotation of the donkey entry to "piRNA processing" is reasonable. It should be treated as an orthology-based inference.

## 7. Regulation of expression: a germ-cell and cancer-testis gene

*Gpat2* has a narrow, stage-specific expression pattern in male germ cells. During the first wave of mouse spermatogenesis, its mRNA and protein peak at 15 days post-partum and are restricted to pachytene spermatocytes [garcia-fabiani-2015-gpat2-methylation-fulltext]. The 2012 study found that GPAT2 protein persists into later stages [cattaneo-2012-gpat2-arachidonic-fulltext]. Bisulfite sequencing of the *Gpat2* promoter in germ cells showed that its methylation falls sharply as meiosis begins (around 11 dpp). In vitro, expression followed DNA demethylation and histone acetylation (it was induced by 5-aza-2′-deoxycytidine and trichostatin A) and was up-regulated by retinoic acid [garcia-fabiani-2015-gpat2-methylation-fulltext]. This on/off epigenetic control is typical of cancer-testis genes. GPAT2 was first proposed as one because its mRNA was selectively found in testis and in multiple myeloma cells in a genome-wide screen for new cancer-testis antigens [condomines-2009-myeloma-ct-abstract; pellon-maison-2014-gpat2-cancer-testis-fulltext]. It is also aberrantly expressed in melanoma and in lung, prostate and breast cancers. In breast tumours, GPAT2 protein correlates with higher histological grade [pellon-maison-2014-gpat2-cancer-testis-fulltext]. In MDA-MB-231 cells, knocking down GPAT2 reduced proliferation, anchorage-independent growth, migration and tumorigenicity and increased apoptosis induced by staurosporine. Overexpression had the opposite effects. In human and mouse testis, GPAT2 is co-expressed with genes for the cell cycle, DNA integrity, piRNA biogenesis and epigenetic regulation [pellon-maison-2014-gpat2-cancer-testis-fulltext]. Expression has not been profiled in donkey tissues. The only data from an ungulate come from pigs: *GPAT2* mRNA was detected in liver but not in longissimus muscle or subcutaneous fat. Its hepatic level did not differ between breeds, and testis was not examined [mitka-2019-pig-gpat-fulltext]. This low-level hepatic expression in a livestock species is consistent with the rodent data [wang-2007-gpat2-cloning-abstract; lewin-2004-mtgpat2-abstract]. Based on the conservation shown in Section 2, a testis-enriched pattern would be expected in the donkey.

## 8. Synthesis: proposed functional annotation for donkey GPAT2

The evidence above supports the following annotation of A0A9L0ILJ0, all inferred from experimentally characterised mouse, rat and human orthologues. Its molecular function is glycerol-3-phosphate *O*-acyltransferase activity (EC 2.3.1.15), which forms 1-acyl-sn-glycerol-3-phosphate (LPA) and prefers arachidonoyl-CoA over saturated, monounsaturated and n-3 polyunsaturated acyl-CoAs, is NEM-sensitive, and may also show 1-acylglycerol-3-phosphate acyltransferase activity [lewin-2004-mtgpat2-abstract; cattaneo-2012-gpat2-arachidonic-fulltext]. Its cellular component is the mitochondrial outer membrane, as a two-pass integral membrane protein with its catalytic motifs facing the cytosol [wang-2007-gpat2-cloning-abstract; nakagawa-2012-gpat2-topology-abstract]. It takes part in the biological processes of de novo glycerolipid synthesis (TAG and phosphatidic acid biosynthesis, especially esterification of arachidonate in spermatocytes) [cattaneo-2012-gpat2-arachidonic-fulltext], primary piRNA biogenesis and retrotransposon silencing through association with PIWIL2 and the ASZ1–MOV10L1 mitochondrial complex [shiromoto-2013-gpat2-pirna-abstract; shiromoto-2019-gpat2-pirna-abstract; yan-2026-piwi-scaffolds-fulltext], and spermatogenesis, including suppression of germ-cell apoptosis [garcia-fabiani-2017-gpat2-spermatogenesis-abstract; shiromoto-2019-gpat2-pirna-abstract]. The donkey sequence keeps the catalytic block I His–Asp dyad and the other conserved blocks [lewin-1999-gpat-motifs-abstract], so it is most likely a functional enzyme. Its C-terminal region is probably mis-modelled, so the full-length sequence needs checking against transcript data.

## Open Questions

Several questions remain open, both for GPAT2 in general and for the donkey protein in particular. First, the enzymology is incomplete. No purified mammalian GPAT2 has been studied kinetically, and whether the extra AGPAT activity seen in overexpressing cells belongs to GPAT2 itself or reflects stimulation of endogenous AGPATs is unresolved [cattaneo-2012-gpat2-arachidonic-fulltext]. Reconstituting the purified protein, including the structural basis of arachidonoyl-CoA selectivity (perhaps by mutagenesis guided by an AlphaFold model, which UniProt lists for A0A9L0ILJ0), would settle this. Second, the mechanism linking GPAT2 to piRNA biogenesis is unknown. The claim that it does not depend on catalysis would benefit from catalytic-dead knock-in mice. The fact that GPAT2 does not recruit PIWI proteins to mitochondria in HeLa cells [gao-2025-piwi-mito-tether-fulltext] raises the question of whether it acts as a lipid-environment regulator of the IMC, a stabiliser of other anchors, or a direct effector of PIWIL2 processing. Its co-purification with ASZ1, MILI and MOV10L1 in adult testis [yan-2026-piwi-scaffolds-fulltext] suggests that mapping its direct binding partner within this complex, and testing whether its lipid products are needed for IMC assembly, would be informative next steps. Third, it is not known whether the arachidonate-buffering role seen in cancer cells [ferremi-2024-gpat2-apoptosis-fulltext] explains the germ-cell apoptosis in *Gpat2*-deficient mice, independently of piRNAs [shiromoto-2019-gpat2-pirna-abstract]. Fourth, for the donkey specifically, the gene model should be checked against testis RNA-seq or long-read transcripts to resolve the divergent C-terminus (residues ~630–718) and to confirm testis-enriched expression. Comparing GPAT2 between donkeys, horses and their sterile hybrid offspring (mules and hinnies) could also be informative, given the gene's importance for meiotic progression and germline transposon control. Finally, whether the epigenetic promoter control described in mouse [garcia-fabiani-2015-gpat2-methylation-fulltext] is conserved in equids has not been examined.

## References

- **cattaneo-2012-gpat2-arachidonic**: Cattaneo ER, Pellon-Maison M, Rabassa ME, Lacunza E, Coleman RA, Gonzalez-Baro MR. Glycerol-3-phosphate acyltransferase-2 is expressed in spermatic germ cells and incorporates arachidonic acid into triacylglycerols. *PLoS One* (2012) 7:e42986. PMID: 22905194; PMCID: PMC3414494; DOI: 10.1371/journal.pone.0042986. https://doi.org/10.1371/journal.pone.0042986
- **cattaneo-2017-gpat2-afm**: Cattaneo ER, Prieto ED, Garcia-Fabiani MB, Montanaro MA, Guillou H, Gonzalez-Baro MR. Glycerol-3-phosphate acyltransferase 2 expression modulates cell roughness and membrane permeability: An atomic force microscopy study. *PLoS One* (2017). PMID: 29211789; PMCID: PMC5718561; DOI: 10.1371/journal.pone.0189031. https://doi.org/10.1371/journal.pone.0189031
- **condomines-2009-myeloma-ct**: Condomines M, Hose D, Rème T, Requirand G, Hundemer M, et al. Gene expression profiling and real-time PCR analyses identify novel potential cancer-testis antigens in multiple myeloma. *J Immunol* (2009) 183:832–840. PMID: 19542363; PMCID: PMC2829428; DOI: 10.4049/jimmunol.0803298. https://doi.org/10.4049/jimmunol.0803298
- **ferremi-2024-gpat2-apoptosis**: Ferremi FJ, Moscoso VV, Montanaro MA, Gonzalez-Baro MR, Cattaneo ER. The protumorigenic enzyme GPAT2 inhibits arachidonic acid-triggered apoptosis in breast cancer. *Lipids Health Dis* (2024). PMID: 39605002; PMCID: PMC11600616; DOI: 10.1186/s12944-024-02344-1. https://doi.org/10.1186/s12944-024-02344-1
- **gao-2025-piwi-mito-tether**: Gao J, Chen C, Shang G, Yu W, Zhao T, Zhang Y, et al. PIWI proteins tether the piRNA biogenesis machinery to mitochondria during mammalian spermatogenesis. *EMBO J* (2025). PMID: 41023308; PMCID: PMC12624062; DOI: 10.1038/s44318-025-00579-x. https://doi.org/10.1038/s44318-025-00579-x
- **garcia-fabiani-2015-gpat2-methylation**: Garcia-Fabiani MB, Montanaro MA, Lacunza E, Cattaneo ER, Coleman RA, Pellon-Maison M, Gonzalez-Baro MR. Methylation of the Gpat2 promoter regulates transient expression during mouse spermatogenesis. *Biochem J* (2015). PMID: 26268560; PMCID: PMC4613502; DOI: 10.1042/BJ20150730. https://doi.org/10.1042/BJ20150730
- **garcia-fabiani-2017-gpat2-spermatogenesis**: Garcia-Fabiani MB, Montanaro MA, Stringa P, Lacunza E, Cattaneo ER, et al. Glycerol-3-phosphate acyltransferase 2 is essential for normal spermatogenesis. *Biochem J* (2017). PMID: 28729426; DOI: 10.1042/BCJ20161018. https://doi.org/10.1042/BCJ20161018
- **gimeno-2008-gpat-review**: Gimeno RE, Cao J. Thematic review series: glycerolipids. Mammalian glycerol-3-phosphate acyltransferases: new genes for an old activity. *J Lipid Res* (2008). PMID: 18658143; DOI: 10.1194/jlr.R800013-JLR200. https://doi.org/10.1194/jlr.R800013-JLR200
- **lacunza-2018-gpat2-smallrna**: Lacunza E, Montanaro MA, Salvati A, Memoli D, Rizzo F, et al. Small non-coding RNA landscape is modified by GPAT2 silencing in MDA-MB-231 cells. *Oncotarget* (2018). PMID: 29963267; PMCID: PMC6021339; DOI: 10.18632/oncotarget.25582. https://doi.org/10.18632/oncotarget.25582
- **lewin-1999-gpat-motifs**: Lewin TM, Wang P, Coleman RA. Analysis of amino acid motifs diagnostic for the sn-glycerol-3-phosphate acyltransferase reaction. *Biochemistry* (1999) 38:5764–5771. PMID: 10231527; DOI: 10.1021/bi982805d. https://doi.org/10.1021/bi982805d
- **lewin-2004-mtgpat2**: Lewin TM, Schwerbrock NM, Lee DP, Coleman RA. Identification of a new glycerol-3-phosphate acyltransferase isoenzyme, mtGPAT2, in mitochondria. *J Biol Chem* (2004) 279:13488–13495. PMID: 14724270; DOI: 10.1074/jbc.M314032200. https://doi.org/10.1074/jbc.M314032200
- **mitka-2019-pig-gpat**: Mitka I, Ropka-Molik K, Tyra M. Functional Analysis of Genes Involved in Glycerolipids Biosynthesis (GPAT1 and GPAT2) in Pigs. *Animals (Basel)* (2019). PMID: 31159297; PMCID: PMC6617006; DOI: 10.3390/ani9060308. https://doi.org/10.3390/ani9060308
- **nakagawa-2012-gpat2-topology**: Nakagawa T, Harada N, Miyamoto A, Kawanishi Y, Yoshida M, et al. Membrane topology of murine glycerol-3-phosphate acyltransferase 2. *Biochem Biophys Res Commun* (2012). PMID: 22285183; DOI: 10.1016/j.bbrc.2012.01.055. https://doi.org/10.1016/j.bbrc.2012.01.055
- **pellon-maison-2014-gpat2-cancer-testis**: Pellon-Maison M, Montanaro MA, Lacunza E, Garcia-Fabiani MB, et al. Glycerol-3-phosphate acyltranferase-2 behaves as a cancer testis gene and promotes growth and tumorigenicity of the breast cancer MDA-MB-231 cell line. *PLoS One* (2014). PMID: 24967918; PMCID: PMC4072688; DOI: 10.1371/journal.pone.0100896. https://doi.org/10.1371/journal.pone.0100896
- **shiromoto-2013-gpat2-pirna**: Shiromoto Y, Kuramochi-Miyagawa S, Daiba A, Chuma S, Katanaya A, et al. GPAT2, a mitochondrial outer membrane protein, in piRNA biogenesis in germline stem cells. *RNA* (2013). PMID: 23611983; PMCID: PMC3683914; DOI: 10.1261/rna.038521.113. https://doi.org/10.1261/rna.038521.113
- **shiromoto-2019-gpat2-pirna**: Shiromoto Y, Kuramochi-Miyagawa S, Nagamori I, Chuma S, et al. GPAT2 is required for piRNA biogenesis, transposon silencing, and maintenance of spermatogonia in mice. *Biol Reprod* (2019). PMID: 30951587; DOI: 10.1093/biolre/ioz056. https://doi.org/10.1093/biolre/ioz056
- **wang-2007-gpat2-cloning**: Wang S, Lee DP, Gong N, Schwerbrock NM, Mashek DG, Gonzalez-Baró MR, Stapleton CM, Li LO, Lewin TM, Coleman RA. Cloning and functional characterization of a novel mitochondrial N-ethylmaleimide-sensitive glycerol-3-phosphate acyltransferase (GPAT2). *Arch Biochem Biophys* (2007) 465:347–358. PMID: 17689486; PMCID: PMC2133398; DOI: 10.1016/j.abb.2007.06.033. https://doi.org/10.1016/j.abb.2007.06.033
- **wang-2020-donkey-genome**: Wang C, Li H, Guo Y, Huang J, Sun Y, et al. Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun* (2020) 11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7. https://doi.org/10.1038/s41467-020-19813-7
- **wendel-2009-gpat-review**: Wendel AA, Lewin TM, Coleman RA. Glycerol-3-phosphate acyltransferases: rate limiting enzymes of triacylglycerol biosynthesis. *Biochim Biophys Acta* (2009). PMID: 19038363; PMCID: PMC2737689; DOI: 10.1016/j.bbalip.2008.10.010. https://doi.org/10.1016/j.bbalip.2008.10.010
- **yan-2026-piwi-scaffolds**: Yan X, Wei C, Mann JM, Shang G, Wang Q, Xie H, Demireva EY, Sun L, Ding D, Chen C. Spatiotemporal control of PIWI compartmentalization by mitochondrial scaffolds defines pachytene piRNA pathway organization. *Proc Natl Acad Sci U S A* (2026). PMID: 42118831; PMCID: PMC13187770; DOI: 10.1073/pnas.2533968123. https://doi.org/10.1073/pnas.2533968123
- **UniProt A0A9L0ILJ0** (donkey GPAT2, TrEMBL, entry version 14) and **UniProt Q6NUI2** (human GPAT2) / **Q14DK4** (mouse Gpat2): https://rest.uniprot.org/uniprotkb/A0A9L0ILJ0.txt ; sequences in `sequence_analysis/gpat2_orthologs.fasta`.


## Citations

1. cattaneo-2012-gpat2-arachidonic-abstract.md
2. cattaneo-2012-gpat2-arachidonic-fulltext.md
3. cattaneo-2012-gpat2-arachidonic-fulltext.xml
4. cattaneo-2012-gpat2-arachidonic-summary.md
5. cattaneo-2017-gpat2-afm-abstract.md
6. cattaneo-2017-gpat2-afm-fulltext.md
7. cattaneo-2017-gpat2-afm-fulltext.xml
8. cattaneo-2017-gpat2-afm-summary.md
9. condomines-2009-myeloma-ct-abstract.md
10. condomines-2009-myeloma-ct-summary.md
11. ferremi-2024-gpat2-apoptosis-abstract.md
12. ferremi-2024-gpat2-apoptosis-fulltext.md
13. ferremi-2024-gpat2-apoptosis-fulltext.xml
14. ferremi-2024-gpat2-apoptosis-summary.md
15. gao-2025-piwi-mito-tether-abstract.md
16. gao-2025-piwi-mito-tether-fulltext.md
17. gao-2025-piwi-mito-tether-fulltext.xml
18. gao-2025-piwi-mito-tether-summary.md
19. garcia-fabiani-2015-gpat2-methylation-abstract.md
20. garcia-fabiani-2015-gpat2-methylation-fulltext.md
21. garcia-fabiani-2015-gpat2-methylation-fulltext.xml
22. garcia-fabiani-2015-gpat2-methylation-summary.md
23. garcia-fabiani-2017-gpat2-spermatogenesis-abstract.md
24. garcia-fabiani-2017-gpat2-spermatogenesis-summary.md
25. gimeno-2008-gpat-review-abstract.md
26. gimeno-2008-gpat-review-summary.md
27. lacunza-2018-gpat2-smallrna-abstract.md
28. lacunza-2018-gpat2-smallrna-fulltext.md
29. lacunza-2018-gpat2-smallrna-fulltext.xml
30. lacunza-2018-gpat2-smallrna-summary.md
31. lewin-1999-gpat-motifs-abstract.md
32. lewin-1999-gpat-motifs-summary.md
33. lewin-2004-mtgpat2-abstract.md
34. lewin-2004-mtgpat2-summary.md
35. mitka-2019-pig-gpat-abstract.md
36. mitka-2019-pig-gpat-fulltext.md
37. mitka-2019-pig-gpat-fulltext.xml
38. mitka-2019-pig-gpat-summary.md
39. nakagawa-2012-gpat2-topology-abstract.md
40. nakagawa-2012-gpat2-topology-summary.md
41. pellon-maison-2014-gpat2-cancer-testis-abstract.md
42. pellon-maison-2014-gpat2-cancer-testis-fulltext.md
43. pellon-maison-2014-gpat2-cancer-testis-fulltext.xml
44. pellon-maison-2014-gpat2-cancer-testis-summary.md
45. shiromoto-2013-gpat2-pirna-abstract.md
46. shiromoto-2013-gpat2-pirna-summary.md
47. shiromoto-2019-gpat2-pirna-abstract.md
48. shiromoto-2019-gpat2-pirna-summary.md
49. wang-2007-gpat2-cloning-abstract.md
50. wang-2007-gpat2-cloning-summary.md
51. wang-2020-donkey-genome-abstract.md
52. wang-2020-donkey-genome-summary.md
53. wendel-2009-gpat-review-abstract.md
54. wendel-2009-gpat-review-fulltext.md
55. wendel-2009-gpat-review-fulltext.xml
56. wendel-2009-gpat-review-summary.md
57. yan-2026-piwi-scaffolds-abstract.md
58. yan-2026-piwi-scaffolds-fulltext.md
59. yan-2026-piwi-scaffolds-fulltext.xml
60. yan-2026-piwi-scaffolds-summary.md