---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:46:28.955075'
end_time: '2026-10-26T00:55:09.185780'
duration_seconds: 520.23
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: SAT1
  gene_symbol: SAT1
  uniprot_accession: A0A9L0KCT9
  protein_description: 'RecName: Full=Diamine acetyltransferase 1 {ECO:0000256|ARBA:ARBA00017209};
    EC=2.3.1.57 {ECO:0000256|ARBA:ARBA00013209}; AltName: Full=Polyamine N-acetyltransferase
    1 {ECO:0000256|ARBA:ARBA00031435}; AltName: Full=Putrescine acetyltransferase
    {ECO:0000256|ARBA:ARBA00029790}; AltName: Full=Spermidine/spermine N(1)-acetyltransferase
    1 {ECO:0000256|ARBA:ARBA00031532};'
  gene_info: Name=SAT1 {ECO:0000313|Ensembl:ENSEASP00005059060.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the acetyltransferase family.
  protein_domains: Acyl_CoA_acyltransferase. (IPR016181); Diverse_Substrate_AcTransf.
    (IPR051016); GNAT_dom. (IPR000182); Acetyltransf_1 (PF00583)
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
citation_count: 45
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0KCT9
- **Protein Description:** RecName: Full=Diamine acetyltransferase 1 {ECO:0000256|ARBA:ARBA00017209}; EC=2.3.1.57 {ECO:0000256|ARBA:ARBA00013209}; AltName: Full=Polyamine N-acetyltransferase 1 {ECO:0000256|ARBA:ARBA00031435}; AltName: Full=Putrescine acetyltransferase {ECO:0000256|ARBA:ARBA00029790}; AltName: Full=Spermidine/spermine N(1)-acetyltransferase 1 {ECO:0000256|ARBA:ARBA00031532};
- **Gene Information:** Name=SAT1 {ECO:0000313|Ensembl:ENSEASP00005059060.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the acetyltransferase family.
- **Key Domains:** Acyl_CoA_acyltransferase. (IPR016181); Diverse_Substrate_AcTransf. (IPR051016); GNAT_dom. (IPR000182); Acetyltransf_1 (PF00583)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "SAT1" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'SAT1' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **SAT1** (gene ID: SAT1, UniProt: A0A9L0KCT9) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# SAT1 (Diamine acetyltransferase 1 / SSAT1) in the donkey, *Equus asinus* (UniProt A0A9L0KCT9)

## 1. Introduction and summary

The donkey gene *SAT1* (UniProt A0A9L0KCT9; Ensembl ENSEASG00005026493; NCBI GeneID 106848136) encodes a 171-residue protein. UniProt classes it as diamine acetyltransferase 1, also called spermidine/spermine N1-acetyltransferase 1 (SSAT or SSAT1; EC 2.3.1.57). The entry is unreviewed (TrEMBL), its gene model was predicted from the donkey genome assemblies [wang-2020-donkey-genomes-abstract], and every functional annotation on it was transferred by automatic rules (ARBA) [uniprot-A0A9L0KCT9-entry]. No experimental study of the donkey protein itself was found. Its function therefore has to be inferred by orthology from the mammalian SSAT1 enzymes, chiefly human, mouse and rat, which have been studied in depth. That inference is unusually safe here. The donkey sequence is 97.1% identical to human SAT1 (P21673): 166 of 171 positions match, and the five differences (I35M, W64Q, R119K, S123R, T169A) are not at any residue known to matter for catalysis, substrate binding or regulated turnover (Section 3).

In summary, SSAT1 is a cytosolic GNAT-family acetyltransferase that works as a homodimer. It moves the acetyl group of acetyl-CoA onto the N1 (aminopropyl-end) primary amine of spermidine and spermine, producing N1-acetylspermidine and N1-acetylspermine [hegde-2007-ssat-mechanism-abstract; montemayor-2008-spermine-complex-abstract]. This reaction is the rate-limiting, highly regulated step of polyamine catabolism. The acetylated products are either exported from the cell or oxidised by peroxisomal N1-acetylpolyamine oxidase (PAOX/APAO) back to spermidine or putrescine [casero-2018-polyamine-cancer-fulltext]. SSAT1 therefore acts as the "turning point" that sets intracellular polyamine levels [casero-1993-turning-point-abstract; pegg-2008-ssat-key-regulator-abstract; casero-2009-polyamine-catabolism-disease-fulltext]. Its substrate preference is norspermidine = spermidine >> spermine > N1-acetylspermine > putrescine [chen-2003-ssat2-abstract].

SSAT1 is controlled at almost every level: transcription, splicing, translation and, above all, very rapid ubiquitin/proteasome-dependent turnover. Binding of polyamines, or of polyamine analogues, blocks that turnover [coleman-1997-proteasomal-degradation-abstract; casero-2009-polyamine-catabolism-disease-fulltext]. Beyond its housekeeping role, SSAT1 acetylates the hypusine residue of eIF5A [lee-2011-eif5a-acetylation-abstract]. It also binds integrin α9 and HIF-1α [chen-2004-integrin-alpha9-abstract; baek-2007-hif1a-abstract], and it is a p53 target gene that promotes ferroptosis [ou-2016-sat1-ferroptosis-abstract].

**Identity check.** The symbol *SAT1* is ambiguous across taxa. In plants it names a serine acetyltransferase, and the human sulfate anion transporter SLC26A1 has also been called "SAT-1". Neither is related to the donkey protein, and literature on them was excluded. The donkey protein's 171-residue length, its GNAT domain (PF00583, PROSITE PS51186 across residues 4–170), its PANTHER subfamily (PTHR10545:SF36, "Diamine acetyltransferase 1") and its near-identity to human SAT1 all confirm that it is the polyamine-catabolic SSAT1 ortholog [uniprot-A0A9L0KCT9-entry].

## 2. Gene and protein identity, orthology and paralogy

Human SSAT was first cloned as a cDNA whose 513-nucleotide open reading frame encodes a 171-amino-acid polypeptide of about 20 kDa [xiao-1991-human-cdna-abstract]. That is the same length as the donkey protein. In mammals the gene lies on the X chromosome (human Xp22.1) [casero-2009-polyamine-catabolism-disease-fulltext]. The donkey UniProt record cross-references human gene ID 6303 through its CTD link and sits in the Ensembl gene tree with other SAT1 genes [uniprot-A0A9L0KCT9-entry], which supports one-to-one orthology.

Mammals also carry a paralog, SSAT2 (SAT2; human 17p13.1), which shares 46% identity with SSAT1. The two differ in substrate preference and inducibility. SSAT2 prefers norspermidine and acetylates spermidine and spermine about equally. Unlike SSAT1, it does not lower cellular polyamine pools when overexpressed and is not induced by polyamine analogues [chen-2003-ssat2-abstract]. Later work showed that the main substrate of SSAT2 is thialysine (S-(2-aminoethyl)-L-cysteine), so SSAT2 is better described as a thialysine Nε-acetyltransferase [casero-2009-polyamine-catabolism-disease-fulltext]. Structural sequence signatures also place SSAT1 in a group with thialysine acetyltransferase-like proteins [bewley-2006-ssat-structure-abstract]. The near-identity of the donkey sequence to human SAT1, set against the much lower identity between the two paralogs, makes clear that A0A9L0KCT9 is SSAT1 and not SSAT2.

## 3. Structure and catalytic mechanism

SSAT1 has the classic GCN5-related N-acetyltransferase (GNAT) fold. Crystal structures of human SSAT1 have been solved as the free dimer and in binary and ternary complexes with CoA, acetyl-CoA, spermine and the analogue inhibitor N1,N11-bis(ethyl)norspermine (BE-3-3-3). They show the enzyme as a dimer whose substrate- and cofactor-binding channels sit at the subunit interface. Two dimer conformations were seen: a symmetric form with two functional channels, and an asymmetric form in which only one channel seems able to acetylate polyamines. In the absence of polyamine, SSAT1 also acetylated its own Lys26, which may have a regulatory role [bewley-2006-ssat-structure-abstract].

Steady-state kinetics of recombinant human SSAT1 support a random sequential mechanism through a ternary complex. The bisubstrate analogue N1-spermine-acetyl-CoA is a competitive inhibitor against both substrates with a true Ki of 6 nM. The pH–activity profile is bell-shaped, governed by groups with apparent pKa values of 7.27 and 8.87 [hegde-2007-ssat-mechanism-abstract]. From the structure with the bisubstrate inhibitor, Hegde and colleagues proposed that Tyr140 acts as the general acid (protonating the CoA thiolate leaving group) and that Glu92 acts as the general base through one or more water molecules [hegde-2007-ssat-mechanism-abstract]. Montemayor and Hoffman independently solved an SSAT1–CoA–spermine complex. It showed a water "proton wire" linking the Glu92 side chain to the spermine N1 amine, and a further water bridging Glu92, Asp93 and the spermine N4 amine. The Glu92Gln mutation impaired binding and catalysis and shifted the pH optimum upward, while Asp93Asn impaired binding and catalysis without changing pH dependence. This supports Glu92 as the catalytic base that drives deprotonation of the substrate amine at physiological pH [montemayor-2008-spermine-complex-abstract].

All of these residues (Lys26, Glu92, Asp93, Tyr140) are conserved in the donkey protein. So are the residues needed for polyamine/analogue binding and the resulting stabilisation, namely Arg7, Cys14, Arg19, Cys122, His126, Lys141, Glu152, Arg155 and Met167 [coleman-1997-proteasomal-degradation-abstract], and the two C-terminal glutamates, Glu170 and Glu171 (sequence comparison in this study; see Section 5). On structural grounds the donkey enzyme should therefore share the human enzyme's chemistry and substrate selectivity.

## 4. Reaction, substrate specificity and the polyamine catabolic pathway

The physiological reaction is acetyl-CoA + spermidine (or spermine) → CoA + N1-acetylspermidine (or N1-acetylspermine) [montemayor-2008-spermine-complex-abstract; uniprot-A0A9L0KCT9-entry]. Assays with alternative substrates in extracts of transfected cells gave the order norspermidine = spermidine >> spermine > N1-acetylspermine > putrescine for SSAT1 [chen-2003-ssat2-abstract]. UniProt's automatic annotation also lists 1,3-diaminopropane and 1,5-diaminopentane (cadaverine) as substrates and adds putrescine acetylation to the pathway line. These alkane-α,ω-diamine activities are weak, and the database itself treats spermidine and spermine as the principal physiological substrates [uniprot-A0A9L0KCT9-entry].

Acetylation removes a positive charge from the polyamine, which loosens its binding to nucleic acids and other anionic sites. It also marks the polyamine for one of two fates [pegg-2008-ssat-key-regulator-abstract; casero-2009-polyamine-catabolism-disease-fulltext]. In the first, the N1-acetylated products are oxidised by the constitutively expressed N1-acetylpolyamine oxidase (APAO/PAOX). This produces spermidine (from N1-acetylspermine) or putrescine (from N1-acetylspermidine), together with 3-acetamidopropanal and H2O2 [casero-2018-polyamine-cancer-fulltext]. APAO acts poorly on non-acetylated polyamines, so flux through this "back-conversion" pathway is limited by how much acetylated substrate SSAT1 supplies [casero-2009-polyamine-catabolism-disease-fulltext]. In the second, the acetylated polyamines are exported from the cell. Uemura and colleagues identified SLC3A2, part of an arginine transporter, as a component of a diamine/polyamine exporter: knocking SLC3A2 down reduced polyamine export from cells. The same study found that SAT1 and SLC3A2 co-immunoprecipitated in both directions and colocalised at the plasma membrane, suggesting the two proteins work together to excrete acetylated polyamines [uemura-2008-diamine-exporter-abstract; casero-2009-polyamine-catabolism-disease-fulltext]. In practice, N1-acetylated polyamines in urine or extracellular fluids are a sign of increased SSAT activity [casero-2009-polyamine-catabolism-disease-fulltext].

Because the products are removed by oxidation or export, raising SSAT1 activity lowers spermidine and spermine and raises putrescine. Transfecting SSAT1 into HEK-293 cells cut spermidine and spermine pools by about 30% and raised putrescine and acetylated polyamines [chen-2003-ssat2-abstract]. Transgenic mice overexpressing SSAT accumulated N1-acetylspermidine, which is normally absent from mouse tissues, along with large amounts of putrescine and lower spermidine and/or spermine [pietila-1997-transgenic-mice-abstract]. SSAT1 activity is also linked to central carbon and lipid metabolism. Its induction triggers a compensatory rise in polyamine biosynthesis, setting up a futile cycle that consumes ATP (to make S-adenosylmethionine) and acetyl-CoA. Transgenic models show the resulting effects on acetyl-CoA, malonyl-CoA and fatty-acid metabolism [pegg-2008-ssat-key-regulator-abstract; casero-2009-polyamine-catabolism-disease-fulltext].

Loss-of-function genetics shows which of these roles cannot be done without. Mice with a targeted disruption of *Sat1* kept nearly normal tissue polyamine pools. The main change was a higher spermidine-to-spermine ratio in most tissues, which shows that SSAT1 is indispensable for back-converting spermine to spermidine but that basal polyamine levels can be maintained without it. The knockout mice did not deplete polyamines in response to the analogue N1,N11-diethylnorspermine (DENSPM), unlike wild-type mice, which places SSAT1 at the centre of analogue-induced catabolism in vivo. Yet liver polyamines fell equally in both genotypes after carbon tetrachloride injury, so SSAT1-independent routes can deplete polyamines under some stresses. With age the knockout mice became insulin resistant, the mirror image of the improved glucose tolerance seen in SSAT-overexpressing mice [niiranen-2006-sat1-knockout-abstract].

## 5. Regulation: a rapidly turning-over, highly inducible enzyme

SSAT1 is among the most tightly regulated enzymes in mammalian metabolism. Its levels track changes in polyamine content and so keep polyamines in balance. It is also induced by toxins, hormones, cytokines, non-steroidal anti-inflammatory drugs, natural products, stress pathways and ischaemia-reperfusion injury [pegg-2008-ssat-key-regulator-abstract].

Transcription is switched on in response to polyamines when the Nrf-2 leucine zipper binds polyamine-modulated factor-1 (PMF-1). Thioredoxin-1 lowers SSAT expression by disrupting the PMF-1/Nrf-2 interaction [casero-2009-polyamine-catabolism-disease-fulltext]. Other inputs include p53, for which *SAT1* is a direct transcriptional target [ou-2016-sat1-ferroptosis-abstract], and PPARγ, whose activation of *SAT1* is antagonised by oncogenic KRAS [casero-2018-polyamine-cancer-fulltext]. After transcription, control comes from mRNA stability, alternative splicing (inclusion of a 110-bp exon between exons 3 and 4 gives the "SSAT-X" mRNA, which carries premature stop codons and is a target for nonsense-mediated decay), translational control, and protein stabilisation [casero-2009-polyamine-catabolism-disease-fulltext].

Protein turnover is the strongest of these controls. SSAT1 is normally ubiquitinated and rapidly degraded by the proteasome. Binding of polyamines, or of analogues such as N1,N12-bis(ethyl)spermine (BE-3-4-3), changes the protein's conformation and blocks degradation [coleman-1997-proteasomal-degradation-abstract]. This extends the half-life to well over 12 h and greatly amplifies the effect of higher mRNA and translation [casero-2009-polyamine-catabolism-disease-fulltext]. Fast degradation needs the C-terminal region. In human SSAT the terminal glutamates (Glu170 and Glu171, in the sequence MATEE) are essential: truncating them, or changing either to glutamine or lysine, abolished rapid proteasomal turnover [coleman-1997-proteasomal-degradation-abstract]. The same MATEE segment is needed for full activity and for protection by BE-3-4-3, and analogue binding shields residues 141–171 from protease attack [coleman-1995-matee-abstract].

The donkey C-terminus reads MAAEE. Thr169 is replaced by alanine, but Met167 and the critical Glu170/Glu171 are retained. Mutagenesis singled out the two glutamates as decisive and did not implicate Thr169 [coleman-1997-proteasomal-degradation-abstract], so the donkey enzyme is predicted to share the rapid, polyamine-sensitive turnover. That prediction is an inference and has not been tested experimentally.

## 6. Subcellular localisation

SSAT1 is mainly a cytosolic enzyme, although a mitochondrial form of unknown function has also been described [casero-2009-polyamine-catabolism-disease-fulltext]. UniProt's automatic annotation for the donkey protein ("Cytoplasm"; GO:0005737) agrees [uniprot-A0A9L0KCT9-entry]. The downstream oxidase PAOX, by contrast, is peroxisomal [casero-2018-polyamine-cancer-fulltext]. The pathway therefore spans compartments: SSAT1 acetylates polyamines in the cytosol, and the acetylated products are then oxidised or exported. Several reported protein partners point to particular places within the cytoplasm. SSAT1 binds the cytoplasmic tail of integrin α9 near the plasma membrane, through its N-terminal region [chen-2004-integrin-alpha9-abstract; casero-2009-polyamine-catabolism-disease-fulltext]. It also associates with the SLC3A2-containing efflux machinery at the plasma membrane, where the two proteins colocalise [uemura-2008-diamine-exporter-abstract]. So although SSAT1 is a soluble cytosolic enzyme, at least part of the cellular pool appears to sit at the inner face of the plasma membrane, where acetylation can be coupled to export or to integrin-dependent migration.

## 7. Non-canonical substrates, protein partners and links to cell fate

Several studies extend SSAT1 beyond free polyamines. SSAT1 specifically acetylates the hypusine (and deoxyhypusine) residue of eukaryotic translation initiation factor 5A (eIF5A). Free hypusine is not a substrate, which points to a direct protein–protein interaction, confirmed by pull-down. Acetylated eIF5A was inactive in a methionyl-puromycin synthesis assay. eIF5A is thus the first protein substrate described for SSAT1, and the finding suggests a possible acetylation/deacetylation switch on hypusinated eIF5A [lee-2011-eif5a-acetylation-abstract].

SSAT1 was found in a yeast two-hybrid screen as a specific binding partner of the integrin α9 cytoplasmic domain. Overexpression enhanced α9β1-dependent cell migration and siRNA knockdown reduced it, without affecting adhesion or migration driven by other integrins. A catalytically inactive mutant did not enhance migration, so the effect depends on local acetyltransferase activity [chen-2004-integrin-alpha9-abstract]. SSAT1 also binds HIF-1α and the scaffold RACK1. By stabilising the HIF-1α–RACK1 interaction it promotes oxygen-independent ubiquitination and degradation of HIF-1α, a mechanism distinct from that of its paralog SSAT2, which stabilises VHL–Elongin C [baek-2007-hif1a-abstract].

*SAT1* is also a transcriptional target of p53. Raising SAT1 expression induces lipid peroxidation and sensitises cells to ferroptosis under reactive-oxygen stress. This depends substantially on arachidonate 15-lipoxygenase (ALOX15), since the ALOX15 inhibitor PD146176 blocks it. SAT1 knockout partly abrogates p53-mediated ferroptosis, and SAT1 induction suppressed xenograft tumour growth [ou-2016-sat1-ferroptosis-abstract]. More broadly, induction of SSAT1 by polyamine analogues such as BENSpm and BESpm, often together with spermine oxidase (SMOX), depletes polyamines and generates ROS. This has made the pathway a target for anticancer strategies [casero-2018-polyamine-cancer-fulltext; casero-1993-turning-point-abstract].

In vivo, sustained SSAT1 overexpression in mice caused permanent hair loss with dermal follicular cysts, attributed to putrescine accumulation, and female infertility from ovarian hypofunction [pietila-1997-transgenic-mice-abstract]. Further transgenic phenotypes include pancreatitis, blocked tissue regeneration and behavioural changes, and in humans *SAT1* dysregulation has been linked to keratosis follicularis spinulosa decalvans [pegg-2008-ssat-key-regulator-abstract]. These pleiotropic effects mainly reflect the enzyme's central role in setting polyamine pools.

## 8. Inferred functional annotation for donkey SAT1

Taken together, the evidence supports the following annotation of A0A9L0KCT9, transferred from experimentally characterised mammalian orthologs because the donkey protein is 97% identical to them and keeps every functional residue. Its molecular function is diamine N-acetyltransferase activity (spermidine/spermine N1-acetyltransferase, EC 2.3.1.57), using acetyl-CoA as donor, with spermidine and spermine binding [hegde-2007-ssat-mechanism-abstract; montemayor-2008-spermine-complex-abstract; chen-2003-ssat2-abstract]. It may also have protein-hypusine acetylation activity toward eIF5A [lee-2011-eif5a-acetylation-abstract]. Its biological process is polyamine catabolism and homeostasis (spermidine and spermine catabolic processes; back-conversion to putrescine together with PAOX) and polyamine export [pegg-2008-ssat-key-regulator-abstract; casero-2009-polyamine-catabolism-disease-fulltext; niiranen-2006-sat1-knockout-abstract; uemura-2008-diamine-exporter-abstract]. Its cellular component is the cytosol [casero-2009-polyamine-catabolism-disease-fulltext], and it acts as a homodimer [bewley-2006-ssat-structure-abstract].

Secondary roles in integrin α9-mediated migration, HIF-1α degradation and p53-driven ferroptosis are documented in human and mouse cells [chen-2004-integrin-alpha9-abstract; baek-2007-hif1a-abstract; ou-2016-sat1-ferroptosis-abstract]. They are plausible in the donkey but have not been tested there. The only donkey-specific evidence is genomic: a gene model from the donkey genome project [wang-2020-donkey-genomes-abstract], annotated through Ensembl and UniProt automated pipelines [uniprot-A0A9L0KCT9-entry].

## Open Questions

No direct experimental data exist for donkey SSAT1. The first and most useful follow-up would be to express and purify recombinant donkey SAT1 and measure its kinetic constants for spermidine, spermine and acetyl-CoA. That would confirm that the five substitutions from the human protein, including the Thr169Ala change inside the C-terminal degron, leave catalysis and polyamine-protected turnover intact. A half-life assay in cultured equid cells, with and without BENSpm, would test the degron directly.

Second, equid tissue expression and inducibility are unknown. Public equine and donkey RNA-seq atlases could be checked for SAT1 levels and for the SSAT-X splice variant. Third, the reported mitochondrial form of SSAT has never been well characterised in any species, and whether donkey SAT1 carries a usable alternative start site or targeting signal is open. Fourth, the non-canonical roles (eIF5A hypusine acetylation, integrin α9 binding, the HIF-1α/RACK1 effect, and p53–SAT1–ALOX15 ferroptosis) all depend on protein–protein interfaces that have not been mapped at residue level. Finding out whether the variable donkey positions (35, 64, 119, 123, 169) fall on any of these interfaces would sharpen the orthology-based inference. Finally, given SSAT's links to hair growth and fertility in transgenic mice, whether natural *SAT1* variation contributes to coat or reproductive traits under selection in donkeys could be explored in the donkey resequencing data [wang-2020-donkey-genomes-abstract].

## References

- **[uniprot-A0A9L0KCT9-entry]** UniProtKB/TrEMBL entry A0A9L0KCT9_EQUAS, Diamine acetyltransferase 1 (SAT1), *Equus asinus*. https://rest.uniprot.org/uniprotkb/A0A9L0KCT9.txt (sequence: citations/uniprot-A0A9L0KCT9.fasta; human comparison: UniProt P21673, https://rest.uniprot.org/uniprotkb/P21673.fasta).
- **[wang-2020-donkey-genomes]** Wang C, Li H, Guo Y, et al. Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun.* 2020;11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7.
- **[xiao-1991-human-cdna]** Xiao L, Celano P, Mank AR, Pegg AE, Casero RA Jr. Characterization of a full-length cDNA which codes for the human spermidine/spermine N1-acetyltransferase. *Biochem Biophys Res Commun.* 1991;179(1):407-15. PMID: 1652956; DOI: 10.1016/0006-291x(91)91385-p.
- **[casero-1993-turning-point]** Casero RA Jr, Pegg AE. Spermidine/spermine N1-acetyltransferase—the turning point in polyamine metabolism. *FASEB J.* 1993;7(8):653-61. PMID: 8500690.
- **[coleman-1995-matee]** Coleman CS, Huang H, Pegg AE. Role of the carboxyl terminal MATEE sequence of spermidine/spermine N1-acetyltransferase in the activity and stabilization by the polyamine analog N1,N12-bis(ethyl)spermine. *Biochemistry.* 1995;34(41):13423-30. PMID: 7577929; DOI: 10.1021/bi00041a020.
- **[coleman-1997-proteasomal-degradation]** Coleman CS, Pegg AE. Proteasomal degradation of spermidine/spermine N1-acetyltransferase requires the carboxyl-terminal glutamic acid residues. *J Biol Chem.* 1997;272(18):12164-9. PMID: 9115288; DOI: 10.1074/jbc.272.18.12164.
- **[pietila-1997-transgenic-mice]** Pietilä M, Alhonen L, Halmekytö M, Kanter P, Jänne J, Porter CW. Activation of polyamine catabolism profoundly alters tissue polyamine pools and affects hair growth and female fertility in transgenic mice overexpressing spermidine/spermine N1-acetyltransferase. *J Biol Chem.* 1997;272(30):18746-51. PMID: 9228047; DOI: 10.1074/jbc.272.30.18746.
- **[chen-2003-ssat2]** Chen Y, Vujcic S, Liang P, Diegelman P, Kramer DL, Porter CW. Genomic identification and biochemical characterization of a second spermidine/spermine N1-acetyltransferase. *Biochem J.* 2003;373(Pt 3):661-7. PMID: 12803540; PMCID: PMC1223561; DOI: 10.1042/BJ20030734.
- **[chen-2004-integrin-alpha9]** Chen C, Young BA, Coleman CS, Pegg AE, Sheppard D. Spermidine/spermine N1-acetyltransferase specifically binds to the integrin alpha9 subunit cytoplasmic domain and enhances cell migration. *J Cell Biol.* 2004;167(1):161-70. PMID: 15479742; PMCID: PMC2172529; DOI: 10.1083/jcb.200312166.
- **[bewley-2006-ssat-structure]** Bewley MC, Graziano V, Jiang J, Matz E, Studier FW, Pegg AE, Coleman CS, Flanagan JM. Structures of wild-type and mutant human spermidine/spermine N1-acetyltransferase, a potential therapeutic drug target. *Proc Natl Acad Sci USA.* 2006;103(7):2063-8. PMID: 16455797; PMCID: PMC1360125; DOI: 10.1073/pnas.0511008103.
- **[hegde-2007-ssat-mechanism]** Hegde SS, Chandler J, Vetting MW, Yu M, Blanchard JS. Mechanistic and structural analysis of human spermidine/spermine N1-acetyltransferase. *Biochemistry.* 2007;46(24):7187-95. PMID: 17516632; PMCID: PMC2518666; DOI: 10.1021/bi700256z.
- **[baek-2007-hif1a]** Baek JH, Liu YV, McDonald KR, Wesley JB, Zhang H, Semenza GL. Spermidine/spermine N1-acetyltransferase-1 binds to hypoxia-inducible factor-1alpha (HIF-1alpha) and RACK1 and promotes ubiquitination and degradation of HIF-1alpha. *J Biol Chem.* 2007;282(46):33358-66. PMID: 17875644; DOI: 10.1074/jbc.M705627200.
- **[pegg-2008-ssat-key-regulator]** Pegg AE. Spermidine/spermine-N1-acetyltransferase: a key metabolic regulator. *Am J Physiol Endocrinol Metab.* 2008;294(6):E995-1010. PMID: 18349109; DOI: 10.1152/ajpendo.90217.2008.
- **[montemayor-2008-spermine-complex]** Montemayor EJ, Hoffman DW. The crystal structure of spermidine/spermine N1-acetyltransferase in complex with spermine provides insights into substrate binding and catalysis. *Biochemistry.* 2008;47(35):9145-53. PMID: 18690703; DOI: 10.1021/bi8009357.
- **[casero-2009-polyamine-catabolism-disease]** Casero RA Jr, Pegg AE. Polyamine catabolism and disease. *Biochem J.* 2009;421(3):323-38. PMID: 19589128; PMCID: PMC2756025; DOI: 10.1042/BJ20090598.
- **[niiranen-2006-sat1-knockout]** Niiranen K, Keinänen TA, Pirinen E, Heikkinen S, Tusa M, Fatrai S, Suppola S, Pietilä M, Uimari A, Laakso M, Alhonen L, Jänne J. Mice with targeted disruption of spermidine/spermine N1-acetyltransferase gene maintain nearly normal tissue polyamine homeostasis but show signs of insulin resistance upon aging. *J Cell Mol Med.* 2006;10(4):933-45. PMID: 17125596; DOI: 10.1111/j.1582-4934.2006.tb00536.x.
- **[uemura-2008-diamine-exporter]** Uemura T, Yerushalmi HF, Tsaprailis G, Stringer DE, Pastorian KE, Hawel L 3rd, Byus CV, Gerner EW. Identification and characterization of a diamine exporter in colon epithelial cells. *J Biol Chem.* 2008;283(39):26428-35. PMID: 18660501; PMCID: PMC2546529; DOI: 10.1074/jbc.M804714200.
- **[lee-2011-eif5a-acetylation]** Lee SB, Park JH, Folk JE, Deck JA, Pegg AE, Sokabe M, Fraser CS, Park MH. Inactivation of eukaryotic initiation factor 5A (eIF5A) by specific acetylation of its hypusine residue by spermidine/spermine acetyltransferase 1 (SSAT1). *Biochem J.* 2011;433(1):205-13. PMID: 20942800; PMCID: PMC3003598; DOI: 10.1042/BJ20101322.
- **[ou-2016-sat1-ferroptosis]** Ou Y, Wang SJ, Li D, Chu B, Gu W. Activation of SAT1 engages polyamine metabolism with p53-mediated ferroptotic responses. *Proc Natl Acad Sci USA.* 2016;113(44):E6806-E6812. PMID: 27698118; PMCID: PMC5098629; DOI: 10.1073/pnas.1607152113.
- **[casero-2018-polyamine-cancer]** Casero RA Jr, Murray Stewart T, Pegg AE. Polyamine metabolism and cancer: treatments, challenges and opportunities. *Nat Rev Cancer.* 2018;18(11):681-695. PMID: 30181570; PMCID: PMC6487480; DOI: 10.1038/s41568-018-0050-3.


## Citations

1. baek-2007-hif1a-abstract.md
2. baek-2007-hif1a-summary.md
3. bewley-2006-ssat-structure-abstract.md
4. bewley-2006-ssat-structure-summary.md
5. casero-1993-turning-point-abstract.md
6. casero-1993-turning-point-summary.md
7. casero-2009-polyamine-catabolism-disease-abstract.md
8. casero-2009-polyamine-catabolism-disease-fulltext.txt
9. casero-2009-polyamine-catabolism-disease-summary.md
10. casero-2018-polyamine-cancer-abstract.md
11. casero-2018-polyamine-cancer-fulltext.txt
12. casero-2018-polyamine-cancer-summary.md
13. chen-2003-ssat2-abstract.md
14. chen-2003-ssat2-summary.md
15. chen-2004-integrin-alpha9-abstract.md
16. chen-2004-integrin-alpha9-fulltext.txt
17. chen-2004-integrin-alpha9-summary.md
18. coleman-1995-matee-abstract.md
19. coleman-1995-matee-summary.md
20. coleman-1997-proteasomal-degradation-abstract.md
21. coleman-1997-proteasomal-degradation-summary.md
22. hegde-2007-ssat-mechanism-abstract.md
23. hegde-2007-ssat-mechanism-summary.md
24. lee-2011-eif5a-acetylation-abstract.md
25. lee-2011-eif5a-acetylation-fulltext.txt
26. lee-2011-eif5a-acetylation-summary.md
27. montemayor-2008-spermine-complex-abstract.md
28. montemayor-2008-spermine-complex-summary.md
29. niiranen-2006-sat1-knockout-abstract.md
30. niiranen-2006-sat1-knockout-summary.md
31. ou-2016-sat1-ferroptosis-abstract.md
32. ou-2016-sat1-ferroptosis-summary.md
33. pegg-2008-ssat-key-regulator-abstract.md
34. pegg-2008-ssat-key-regulator-summary.md
35. pietila-1997-transgenic-mice-abstract.md
36. pietila-1997-transgenic-mice-summary.md
37. uemura-2008-diamine-exporter-abstract.md
38. uemura-2008-diamine-exporter-summary.md
39. uniprot-A0A9L0KCT9-entry.txt
40. uniprot-A0A9L0KCT9.fasta
41. uniprot-P21673-human.fasta
42. wang-2020-donkey-genomes-abstract.md
43. wang-2020-donkey-genomes-summary.md
44. xiao-1991-human-cdna-abstract.md
45. xiao-1991-human-cdna-summary.md