---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T03:48:46.185426'
end_time: '2026-10-26T04:02:07.158222'
duration_seconds: 800.97
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: human
  gene_id: ACAD9__A0A7P0T7Z1
  gene_symbol: ACAD9
  uniprot_accession: A0A7P0T7Z1
  protein_description: 'RecName: Full=long-chain-acyl-CoA dehydrogenase {ECO:0000256|ARBA:ARBA00012040};
    EC=1.3.8.8 {ECO:0000256|ARBA:ARBA00012040};'
  gene_info: Name=ACAD9 {ECO:0000313|Ensembl:ENSP00000504886.1};
  organism_full: Homo sapiens (Human).
  protein_family: Belongs to the acyl-CoA dehydrogenase family.
  protein_domains: Acyl-CoA_DH_CS. (IPR006089); Acyl-CoA_Oxase/DH_mid-dom_sf. (IPR046373);
    AcylCo_DH-like_C. (IPR036250); AcylCo_DH/oxidase_C. (IPR009075); AcylCoA_DH/ox_M.
    (IPR006091)
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
citation_count: 67
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A7P0T7Z1
- **Protein Description:** RecName: Full=long-chain-acyl-CoA dehydrogenase {ECO:0000256|ARBA:ARBA00012040}; EC=1.3.8.8 {ECO:0000256|ARBA:ARBA00012040};
- **Gene Information:** Name=ACAD9 {ECO:0000313|Ensembl:ENSP00000504886.1};
- **Organism (full):** Homo sapiens (Human).
- **Protein Family:** Belongs to the acyl-CoA dehydrogenase family.
- **Key Domains:** Acyl-CoA_DH_CS. (IPR006089); Acyl-CoA_Oxase/DH_mid-dom_sf. (IPR046373); AcylCo_DH-like_C. (IPR036250); AcylCo_DH/oxidase_C. (IPR009075); AcylCoA_DH/ox_M. (IPR006091)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "ACAD9" matches the protein description above**
2. **Verify the organism is correct:** Homo sapiens (Human).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'ACAD9' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **ACAD9** (gene ID: ACAD9__A0A7P0T7Z1, UniProt: A0A7P0T7Z1) in human.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# ACAD9 (UniProt A0A7P0T7Z1, *Homo sapiens*): a long-chain acyl-CoA dehydrogenase repurposed as a mitochondrial complex I assembly factor

## 1. Introduction and summary

ACAD9 (acyl-CoA dehydrogenase family member 9) is a nuclear-encoded flavoprotein of the mitochondrial acyl-CoA dehydrogenase (ACAD) family. It works in two separate pathways. As an enzyme, it catalyses the FAD-dependent α,β-dehydrogenation of long-chain acyl-CoA thioesters to (2E)-enoyl-CoA, which is the first step of each turn of mitochondrial fatty acid β-oxidation (FAO). Electrons pass to electron-transfer flavoprotein (ETF). The enzyme is most active on long-chain unsaturated acyl-CoAs (C16:1, C18:1, C18:2, C22:6) [zhang-2002-acad9-cloning-abstract][ensenauer-2005-acad9-unsaturated-abstract]. As a structural chaperone, ACAD9 is a core subunit of the mitochondrial complex I intermediate assembly (MCIA) complex, together with ECSIT, NDUFAF1 and TMEM126B. MCIA is needed to build the membrane-arm ND2 module of respiratory complex I (NADH:ubiquinone oxidoreductase) [nouws-2010-acad9-complexI-abstract][formosa-2020-mcia-dissection-abstract]. The assembly function does not need catalytic activity [nouws-2014-acad9-moonlighting-abstract]. Structural work shows the two roles are mutually exclusive: when the C-terminal domain of ECSIT binds ACAD9, it remodels the FAD-binding loop and expels the flavin, turning the dehydrogenase into an assembly factor [giachin-2021-mcia-deflavination-fulltext][xia-2021-acad9-binding-partners-fulltext][mcgregor-2023-mcia-assembly-fulltext]. ACAD9 acts in the mitochondrial matrix, as a peripheral protein on the matrix face of the inner membrane [ensenauer-2005-acad9-unsaturated-abstract][uniprot-Q9H845-entry]. Biallelic ACAD9 variants cause a common, often riboflavin-responsive form of isolated complex I deficiency (MC1DN20). Its usual features are cardiomyopathy, myopathy and lactic acidosis [haack-2010-exome-acad9-abstract][gerards-2011-riboflavin-acad9-abstract][repp-2018-acad9-70-patients-abstract].

The protein in this report, A0A7P0T7Z1, is an unreviewed alternative isoform. Section 2 describes how it relates to the canonical protein. Its N-terminal 521 residues are identical to canonical ACAD9 (Q9H845), so it keeps the presequence and the whole catalytic dehydrogenase domain. Its C-terminus is different, because the reading frame shifts after a splice-site change. Almost all functional evidence below comes from studies of the canonical 621-residue protein. Applying it to A0A7P0T7Z1 is an inference, and Section 7 sets out where that inference is weak.

## 2. Identity of the target and relation to canonical ACAD9

The UniProt record A0A7P0T7Z1 is a TrEMBL (unreviewed) entry of 626 residues. Its gene name is ACAD9, its organism is *Homo sapiens*, and it is translated from Ensembl ENSP00000504886. Automatic (ARBA) rules annotate it as long-chain-acyl-CoA dehydrogenase (EC 1.3.8.8) in the acyl-CoA dehydrogenase family, with the family's N-terminal, middle (β-sheet) and C-terminal α-helical domains (IPR013786, IPR006091, IPR009075) and the ACAD signature motif (IPR006089) [uniprot-A0A7P0T7Z1-entry]. This matches the published description of ACAD9 as a 621-residue VLCAD homologue on chromosome 3q26 that contains both ACAD family signatures [zhang-2002-acad9-cloning-abstract]. Gene symbol, organism and protein family all agree, so the symbol is not ambiguous here. The literature on human ACAD9 applies to this gene product.

I aligned A0A7P0T7Z1 pairwise against the reviewed canonical entry Q9H845 ("Complex I assembly factor ACAD9, mitochondrial", 621 aa) and compared the two Ensembl transcripts. The two proteins are identical over residues 1–521. A0A7P0T7Z1 comes from transcript ENST00000680636 (ACAD9-219, a HAVANA non-canonical protein-coding model). This transcript has the same 18 exons as the canonical ENST00000308982 except for exon 16. There it uses a splice acceptor 94 nt upstream, which shifts the frame after codon 521 and adds a new ~105-residue C-terminal tail [uniprot-A0A7P0T7Z1-summary][ensembl-ACAD9-isoforms-summary]. The tail is rich in glycine, proline and histidine and does not look like any known domain.

The cryo-EM structure of canonical ACAD9 shows what is lost. Residues 38–453 form the catalytic dehydrogenase domain (an α-helical, a β-sheet and a second α-helical subdomain). A poorly ordered linker of about 35 residues (~454–486) follows. Residues 487–587 form a C-terminal α-helical vestigial domain. The C-terminal helix-loops (residues ~588/600–621) wrap round the neighbouring protomer and stabilise the dimer [mcgregor-2023-mcia-assembly-fulltext][giachin-2021-mcia-deflavination-fulltext]. A0A7P0T7Z1 therefore keeps the complete dehydrogenase domain, the linker and the first ~35 residues of the vestigial domain. It lacks most of the vestigial helical bundle and the dimer-stabilising C-terminal helix. The ECSIT-binding site lies at the junction of the dehydrogenase and vestigial domains [mcgregor-2023-mcia-assembly-fulltext], so it is unclear whether this isoform can dimerise, bind ECSIT or work in MCIA. No study has addressed it directly. The transcript evidence is also weaker than for the canonical form. The canonical ENST00000308982 is the MANE Select, Ensembl-canonical, GENCODE-primary transcript with transcript support level 1. ENST00000680636 carries only the GENCODE basic tag and has no transcript support level assigned [ensembl-ACAD9-transcript-tags-summary]. I found no published protein-level evidence that this isoform is expressed. One prediction does follow from the sequence. The catalytic proton acceptor Glu426 lies inside the shared region, so the isoform keeps the residue needed for dehydrogenase chemistry [uniprot-Q9H845-entry][xia-2021-acad9-binding-partners-fulltext]. Some patient missense variants map to the region it replaces, such as R532W, which was shown not to rescue complex I in patient fibroblasts. Others map to the shared region, such as R127Q, R469W and R518H [gerards-2011-riboflavin-acad9-abstract][uniprot-Q9H845-entry].

## 3. Enzymatic function: long-chain acyl-CoA dehydrogenation

ACAD9 was first identified by random sequencing of a dendritic-cell cDNA library as the ninth human ACAD, about 47% identical to very-long-chain acyl-CoA dehydrogenase (VLCAD/ACADVL). Recombinant protein dehydrogenated palmitoyl-CoA (C16:0) and stearoyl-CoA (C18:0) [zhang-2002-acad9-cloning-abstract]. Ensenauer and colleagues purified mature ACAD9 from *E. coli* and profiled its substrates systematically. Activity was highest with long-chain unsaturated acyl-CoAs: palmitoleoyl- (C16:1), oleoyl- (C18:1), linoleoyl- (C18:2) and docosahexaenoyl-CoA (C22:6) [ensenauer-2005-acad9-unsaturated-abstract]. UniProt cites this work for apparent Km values of 2.8 µM for hexadecanoyl-CoA and 0.7 µM for (9Z)-hexadecenoyl-CoA, and records FAD as the cofactor [uniprot-Q9H845-entry]. The reaction follows the ACAD mechanism. A long-chain 2,3-saturated acyl-CoA is oxidised to the (2E)-enoyl-CoA, and two electrons pass through the FAD to oxidised ETF. This corresponds to Rhea:17721 / EC 1.3.8.8, with lower activity on medium-chain substrates (EC 1.3.8.7) [uniprot-Q9H845-entry]. As in most ACADs, the catalytic base that removes the α-proton is a glutamate, Glu426 in ACAD9. An E426Q mutant had no dehydrogenase activity at all but still formed the ACAD9–ECSIT–NDUFAF1 ternary complex [xia-2021-acad9-binding-partners-fulltext]. This agrees with the cell-based finding that catalytically dead ACAD9 still supports complex I assembly [nouws-2014-acad9-moonlighting-abstract]. In this way ACAD9 feeds long-chain fats into the β-oxidation spiral and the ETF–ETF:ubiquinone oxidoreductase branch of the respiratory chain [houten-2016-fao-review-abstract].

Recent NMR and MS work shows the chemistry may be broader than the classical product. With palmitoyl-CoA, both VLCAD and ACAD9 made the expected (2E)-hexadecenoyl-CoA. They also made E and Z 3-hexadecenoyl-CoA, a β,γ-dehydrogenation product, which points to an alternative catalytic route whose physiological role is unknown [fabbian-2025-beta-gamma-dehydrogenation-abstract].

Whether ACAD9 matters for FAO in vivo depends on cell type. Knockdown in control fibroblasts did not change acylcarnitine profiles after fatty acid loading. In VLCAD-deficient fibroblasts, however, ACAD9 accounted for the C14:1-carnitine made from oleate and the C12-carnitine made from palmitate, which are the diagnostic markers of VLCAD deficiency. So ACAD9 has real enzymatic activity in cells [nouws-2014-acad9-moonlighting-abstract]. In HEK293 cells, which express ACAD9 strongly, knockout lowered long-chain FAO as well as complex I, and wild-type ACAD9 rescued both. Among 16 patient mutations expressed in bacteria, residual ACAD activity correlated inversely with clinical severity [schiff-2015-acad9-dual-function-abstract]. ACAD9 is abundant in the central nervous system and enriched in the granular layer of the cerebellum. There it probably works alongside ACAD11 (C20–C26) to cover the long-chain substrates found in cerebellum, and it may contribute to lipid remodelling as well as energy production [he-2011-new-lcads-fulltext][he-2007-acad9-deficiency-abstract]. Deficiency of ACAD9 and of VLCAD do not compensate for each other despite overlapping substrates, which suggests the two enzymes have different physiological roles [he-2007-acad9-deficiency-abstract].

## 4. Moonlighting function: a core subunit of the MCIA complex in complex I biogenesis

Complex I has 44–45 subunits, and its assembly needs at least 15 known assembly factors [xia-2021-acad9-binding-partners-fulltext]. Nouws et al. showed that ACAD9 binds the assembly factors NDUFAF1 and ECSIT, that it is specifically required for complex I assembly, and that ACAD9 mutations cause complex I deficiency without a clear long-chain FAO defect. VLCAD, its paralog, is not required for complex I. The authors proposed that the two paralogs diverged at the root of the vertebrate lineage and took on separate mitochondrial pathways [nouws-2010-acad9-complexI-abstract]. Exome sequencing and homozygosity mapping independently found ACAD9 mutations in isolated complex I deficiency. In both studies wild-type, but not mutant, ACAD9 restored complex I activity in patient fibroblasts, which establishes causality [haack-2010-exome-acad9-abstract][gerards-2011-riboflavin-acad9-abstract].

Phylogenetic analysis gives a deeper evolutionary context than the vertebrate-root divergence proposed by Nouws et al. The ACAD family dates back to the common ancestor of Archaea, Bacteria and Eukaryota. A duplication unique to eukaryotes produced the VLCAD and ACAD9 paralogs. ACAD9 was later lost from several animal lineages, including Cnidaria, nematodes and arthropods [swigonova-2009-acad-evolution-abstract][swigonova-2009-acad-evolution-fulltext]. The duplication is therefore older than the vertebrates. The vertebrate-specific step proposed by Nouws et al. is better read as the time when the two paralogs took on separate pathway roles, and how ACAD9 orthologs in non-vertebrate eukaryotes function has not been tested. The same analysis found that all nine ACADs studied before 2009 are mitochondrial, consistent with an endosymbiotic origin of the family [swigonova-2009-acad-evolution-abstract].

Complexome profiling placed ACAD9 in the MCIA complex with ECSIT, NDUFAF1, TMEM126B and TIMMDC1 [alston-2016-tmem126b-abstract]. Knockout studies later showed that MCIA is needed to build the ND2 module of the membrane arm. Every core component is essential, and the complex has a hierarchy of stability centred on ACAD9. TMEM186 and COA1 are additional components that associate with newly translated ND3 and ND2 respectively [formosa-2020-mcia-dissection-abstract]. MCIA also interacts with the ATP synthase c-ring assembly factors TMEM70 and TMEM242. Losing these factors lowers complex I as well, which hints at coordinated biogenesis of the two OXPHOS complexes [carroll-2021-tmem70-tmem242-abstract].

The key mechanistic point is that ACAD9 does not need its catalytic activity to assemble complex I. A catalytically inactive mutant rescued complex I biogenesis partly or fully in ACAD9-deficient cells and was incorporated into high-molecular-weight assembly intermediates. The enzymatic activity therefore looks like a remnant of the gene duplication rather than a requirement for assembly [nouws-2014-acad9-moonlighting-abstract].

## 5. Structural basis of the switch between FAO and complex I assembly

Biochemical reconstitution has explained how one protein carries out two exclusive functions. ECSIT is the bridging node of the MCIA core. NDUFAF1 binds both halves of ECSIT, while only the ECSIT C-terminal domain binds ACAD9 [giachin-2021-mcia-deflavination-fulltext]. Xia et al. found the same arrangement with full-length proteins. Binary complexes were unstable and prone to aggregate, whereas the ACAD9–ECSIT–NDUFAF1 ternary complex was soluble and stable [xia-2021-acad9-binding-partners-fulltext]. Both groups found that ECSIT binding removes the 450 nm flavin absorbance of ACAD9 and releases free FAD, a process called deflavination [giachin-2021-mcia-deflavination-fulltext][xia-2021-acad9-binding-partners-fulltext]. Xia et al. modelled ECSIT on the ETF-docking surface of ACAD9. This explains why bound ACAD9 cannot work as a dehydrogenase, and shows the two functions are mutually exclusive [xia-2021-acad9-binding-partners-fulltext].

A higher-resolution cryo-EM structure of dimeric ACAD9 bound to ECSIT (residues 221–431) has since given the atomic detail (PDB 8PHE/8PHF) [mcgregor-2023-mcia-assembly-fulltext][uniprot-Q9H845-entry]. ECSIT residues 320–334 bind in a positively charged cleft at the junction of the dehydrogenase and vestigial domains. A 3₁₀-helix (ECSIT 322–328) contacts the ACAD9 β1–β2 loop (residues 178–195), and an extended segment (329–334) lies between helices α16 and η6. Binding causes a large conformational change in the FAD-binding loop that releases FAD, and no flavin density was seen in the complex [mcgregor-2023-mcia-assembly-fulltext]. The same study proposed a regulatory layer. Phosphorylation of ECSIT weakens its association with ACAD9. The authors showed that p38α MAPK phosphorylates ECSIT in vitro and that a phosphomimetic T320E mutation disrupts the fit of the ECSIT segment in the ACAD9 cavity. They also found that ECSIT phosphorylation fell in neuronal cells exposed to amyloid-β oligomers. Together these suggest a way to rebalance FAO against OXPHOS [mcgregor-2023-mcia-assembly-fulltext]. The authors themselves called these observations preliminary. A hypothesis paper has gone further. It suggests that the FAD released on ECSIT binding might be recycled into FMN, the flavin cofactor of complex I, and that ACAD9 couples the reactive oxygen species made at complex I during high-FADH₂/NADH fatty acid oxidation to complex I renewal. This idea has not been tested experimentally [speijer-2022-acad9-fadh2-nadh-abstract].

These structures matter for the target isoform. The ECSIT cleft involves helices from both the dehydrogenase and vestigial domains, and the dimer depends on C-terminal helices (588–621). A0A7P0T7Z1 replaces both regions after residue 521 (Section 2), so its MCIA function cannot simply be assumed, even though its catalytic core is intact.

## 6. Subcellular localisation and tissue expression

ACAD9 is made with a 37-residue N-terminal mitochondrial presequence. Two mitochondrial peptidases remove it in sequence, giving a mature subunit of about 65 kDa. Native ACAD9 fractionates with mitochondrial membranes, and gel filtration shows it is a homodimer like VLCAD, unlike the tetrameric short- and medium-chain ACADs [ensenauer-2005-acad9-unsaturated-abstract]. UniProt summarises this as a peripheral protein of the mitochondrial inner membrane on the matrix side [uniprot-Q9H845-entry]. That location fits both roles: the β-oxidation machinery and ETF sit in the matrix, and MCIA assembles the membrane arm of complex I in the inner membrane [formosa-2020-mcia-dissection-abstract]. A0A7P0T7Z1 has the same N-terminus, including the presequence, so it is predicted to be imported into mitochondria in the same way.

A 2026 study described a second, cytosolic pool of ACAD9 in osteoclast-lineage cells. There ACAD9 binds TRAF6, competes with the UBC13/UEV1A E2 complex, blocks K63-linked TRAF6 polyubiquitination and RANK–TRAF6–TAK1–NFATc1 signalling, and promotes K48-linked TRAF6 degradation. Osteoclast-specific *Acad9* knockout mice had more osteoclasts and lower bone mass. The same study reported that ACAD9 helps form respiratory supercomplexes [wang-2026-acad9-cytosolic-traf6-abstract]. This extramitochondrial function comes from one recent study and has not been reproduced independently.

ACAD9 mRNA is found in most tissues, with high levels in heart, skeletal muscle, brain, kidney and liver [zhang-2002-acad9-cloning-abstract]. In human cerebellum the protein is most abundant in the granular layer [he-2011-new-lcads-fulltext]. Expression is high in liver, neurons and HEK293 cells and very low in skin fibroblasts. This pattern helps explain why FAO defects are hard to detect in patient fibroblasts [schiff-2015-acad9-dual-function-abstract].

## 7. In vivo models and disease relevance as functional evidence

Mouse genetics shows that ACAD9 is essential. When heterozygous *Acad9* knockout mice were crossed, no homozygous null pups were born (55 pups genotyped: 40% wild type, 60% heterozygous), so complete loss is embryonic lethal. This differs from other ACAD deficiencies in mice. Cardiac-specific deletion caused severe cardiomyopathy that was already present on day 3 after birth, with severe mitochondrial dysfunction and death before three weeks of age. Skeletal-muscle-specific mutants were viable but weak, although deletion in muscle was less efficient. ECSIT protein fell sharply in ACAD9-deficient hearts, which matches the ACAD9-centred stability hierarchy of the MCIA complex seen in human cells [sinsheimer-2021-acad9-mouse-abstract][sinsheimer-2021-acad9-mouse-fulltext][formosa-2020-mcia-dissection-abstract].

Disease genetics mostly supports the complex I role. Among 70 ACAD9-deficient patients, none carried two loss-of-function alleles, which implies that complete loss is lethal. The commonest features were cardiomyopathy (85%), muscle weakness (75%) and exercise intolerance (72%). Riboflavin, the FAD precursor, improved complex I activity in most patient fibroblasts, and early-onset patients treated with it survived significantly better [repp-2018-acad9-70-patients-abstract]. The response to riboflavin was first seen in the R532W family [gerards-2011-riboflavin-acad9-abstract]. It suggests that flavin binding stabilises ACAD9 even though FAD is released when ACAD9 joins MCIA. How these two observations fit together is still an open mechanistic question. The early reports framed ACAD9 deficiency as an FAO disorder, with Reye-like episodes, hepatic dysfunction and cardiomyopathy [he-2007-acad9-deficiency-abstract]. The finding that residual FAO activity tracks with severity indicates that both functions contribute to disease [schiff-2015-acad9-dual-function-abstract]. Treatment attempts that target both pathways are reported only as single cases. In one riboflavin-unresponsive infant, bezafibrate and nicotinamide riboside brought only temporary stabilisation [vanhove-2024-acad9-bezafibrate-abstract].

## 8. Open Questions

The most direct gap for this entry is that the A0A7P0T7Z1 isoform (ACAD9-219) has never been studied. Useful next steps would be to check for transcript-specific RNA-seq or long-read support for the upstream exon-16 acceptor, and to look for peptides from the frameshifted C-terminal tail in proteomics datasets. Its oligomeric state, FAD content and acyl-CoA dehydrogenase activity could be measured after recombinant expression, and its ability to bind ECSIT or rescue complex I in ACAD9-knockout cells could be tested. One could also ask whether it is mainly a nonsense-mediated decay escapee with no function. Since it has no transcript support level and is not MANE Select, the first step should be to establish that it is expressed at all before giving it functional annotations beyond those inherited from the shared catalytic domain.

For canonical ACAD9, several mechanistic questions remain. How does FAD release relate to riboflavin responsiveness? Does riboflavin stabilise the free enzyme pool or speed up MCIA turnover? What triggers ACAD9 to leave MCIA once the ND2 module is built, and does it then take up FAD again? Which kinases and phosphatases control ECSIT–ACAD9 association in vivo? The proposed amyloid-β link needs testing in physiological models. The physiological substrates of ACAD9 in brain, and the significance of the β,γ-dehydrogenation products, are still unknown. It is not known how ACAD9 orthologs in invertebrate and non-animal eukaryotes divide their work between FAO and complex I assembly. Another open question is whether the FAD released from ACAD9 is reused, for example as FMN for complex I. Finally, the reported cytosolic TRAF6-regulating function and the supercomplex role need independent confirmation, including a clear explanation of how a protein with a mitochondrial presequence comes to be in the cytosol.

## 9. References

* **zhang-2002-acad9-cloning** — Zhang J, Zhang W, Zou D, Chen G, Wan T, Zhang M, Cao X. (2002). Cloning and functional characterization of ACAD-9, a novel member of human acyl-CoA dehydrogenase family. Biochem Biophys Res Commun 297:1033-1042. PMID: 12359260; DOI: 10.1016/s0006-291x(02)02336-7; https://pubmed.ncbi.nlm.nih.gov/12359260/
* **ensenauer-2005-acad9-unsaturated** — Ensenauer R, He M, Willard JM, Goetzman ES, Corydon TJ, Vandahl BB, Mohsen AW, Isaya G, Vockley J. (2005). Human acyl-CoA dehydrogenase-9 plays a novel role in the mitochondrial beta-oxidation of unsaturated fatty acids. J Biol Chem 280:32309-32316. PMID: 16020546; DOI: 10.1074/jbc.m504460200; https://pubmed.ncbi.nlm.nih.gov/16020546/
* **he-2007-acad9-deficiency** — He M, Rutledge SL, Kelly DR, Palmer CA, Murdoch G, Majumder N, Nicholls RD, Pei Z, Watkins PA, Vockley J. (2007). A new genetic disorder in mitochondrial fatty acid beta-oxidation: ACAD9 deficiency. Am J Hum Genet 81:87-103. PMID: 17564966; PMCID: PMC1950923; DOI: 10.1086/519219; https://pubmed.ncbi.nlm.nih.gov/17564966/
* **nouws-2010-acad9-complexI** — Nouws J, Nijtmans L, Houten SM, et al. (2010). Acyl-CoA dehydrogenase 9 is required for the biogenesis of oxidative phosphorylation complex I. Cell Metab 12:283-294. PMID: 20816094; DOI: 10.1016/j.cmet.2010.08.002; https://pubmed.ncbi.nlm.nih.gov/20816094/
* **haack-2010-exome-acad9** — Haack TB, Danhauser K, Haberberger B, et al. (2010). Exome sequencing identifies ACAD9 mutations as a cause of complex I deficiency. Nat Genet 42:1131-1134. PMID: 21057504; DOI: 10.1038/ng.706; https://pubmed.ncbi.nlm.nih.gov/21057504/
* **gerards-2011-riboflavin-acad9** — Gerards M, van den Bosch BJ, Danhauser K, et al. (2011). Riboflavin-responsive oxidative phosphorylation complex I deficiency caused by defective ACAD9: new function for an old gene. Brain 134:210-219. PMID: 20929961; DOI: 10.1093/brain/awq273; https://pubmed.ncbi.nlm.nih.gov/20929961/
* **he-2011-new-lcads** — He M, Pei Z, Mohsen AW, Watkins P, Murdoch G, Van Veldhoven PP, Ensenauer R, Vockley J. (2011). Identification and characterization of new long chain acyl-CoA dehydrogenases. Mol Genet Metab 102:418-429. PMID: 21237683; PMCID: PMC3073726; DOI: 10.1016/j.ymgme.2010.12.005; https://pubmed.ncbi.nlm.nih.gov/21237683/
* **nouws-2014-acad9-moonlighting** — Nouws J, Te Brinke H, Nijtmans LG, Houten SM. (2014). ACAD9, a complex I assembly factor with a moonlighting function in fatty acid oxidation deficiencies. Hum Mol Genet 23:1311-1319. PMID: 24158852; DOI: 10.1093/hmg/ddt521; https://pubmed.ncbi.nlm.nih.gov/24158852/
* **schiff-2015-acad9-dual-function** — Schiff M, Haberberger B, Xia C, et al. (2015). Complex I assembly function and fatty acid oxidation enzyme activity of ACAD9 both contribute to disease severity in ACAD9 deficiency. Hum Mol Genet 24:3238-3247. PMID: 25721401; PMCID: PMC4424958; DOI: 10.1093/hmg/ddv074; https://pubmed.ncbi.nlm.nih.gov/25721401/
* **houten-2016-fao-review** — Houten SM, Violante S, Ventura FV, Wanders RJ. (2016). The Biochemistry and Physiology of Mitochondrial Fatty Acid β-Oxidation and Its Genetic Disorders. Annu Rev Physiol 78:23-44. PMID: 26474213; DOI: 10.1146/annurev-physiol-021115-105045; https://pubmed.ncbi.nlm.nih.gov/26474213/
* **alston-2016-tmem126b** — Alston CL, Compton AG, Formosa LE, et al. (2016). Biallelic Mutations in TMEM126B Cause Severe Complex I Deficiency with a Variable Clinical Phenotype. Am J Hum Genet 99:217-227. PMID: 27374774; PMCID: PMC5005451; DOI: 10.1016/j.ajhg.2016.05.021; https://pubmed.ncbi.nlm.nih.gov/27374774/
* **repp-2018-acad9-70-patients** — Repp BM, Mastantuono E, Alston CL, et al. (2018). Clinical, biochemical and genetic spectrum of 70 patients with ACAD9 deficiency: is riboflavin supplementation effective? Orphanet J Rare Dis 13:120. PMID: 30025539; PMCID: PMC6053715; DOI: 10.1186/s13023-018-0784-8; https://pubmed.ncbi.nlm.nih.gov/30025539/
* **formosa-2020-mcia-dissection** — Formosa LE, Muellner-Wong L, Reljic B, et al. (2020). Dissecting the Roles of Mitochondrial Complex I Intermediate Assembly Complex Factors in the Biogenesis of Complex I. Cell Rep 31:107541. PMID: 32320651; DOI: 10.1016/j.celrep.2020.107541; https://pubmed.ncbi.nlm.nih.gov/32320651/
* **giachin-2021-mcia-deflavination** — Giachin G, Jessop M, Bouverot R, et al. (2021). Assembly of The Mitochondrial Complex I Assembly Complex Suggests a Regulatory Role for Deflavination. Angew Chem Int Ed Engl 60:4689-4697. PMID: 33320993; PMCID: PMC7986633; DOI: 10.1002/anie.202011548; https://pubmed.ncbi.nlm.nih.gov/33320993/
* **carroll-2021-tmem70-tmem242** — Carroll J, He J, Ding S, Fearnley IM, Walker JE. (2021). TMEM70 and TMEM242 help to assemble the rotor ring of human ATP synthase and interact with assembly factors for complex I. Proc Natl Acad Sci U S A 118:e2100558118. PMID: 33753518; PMCID: PMC8020751; DOI: 10.1073/pnas.2100558118; https://pubmed.ncbi.nlm.nih.gov/33753518/
* **xia-2021-acad9-binding-partners** — Xia C, Lou B, Fu Z, Mohsen AW, Shen AL, Vockley J, Kim JP. (2021). Molecular mechanism of interactions between ACAD9 and binding partners in mitochondrial respiratory complex I assembly. iScience 24:103153. PMID: 34646991; PMCID: PMC8497999; DOI: 10.1016/j.isci.2021.103153; https://pubmed.ncbi.nlm.nih.gov/34646991/
* **mcgregor-2023-mcia-assembly** — McGregor L, Acajjaoui S, Desfosses A, et al. (2023). The assembly of the Mitochondrial Complex I Assembly complex uncovers a redox pathway coordination. Nat Commun 14:8248. PMID: 38086790; PMCID: PMC10716376; DOI: 10.1038/s41467-023-43865-0; https://pubmed.ncbi.nlm.nih.gov/38086790/
* **fabbian-2025-beta-gamma-dehydrogenation** — Fabbian S, Masciovecchio B, Schievano E, Giachin G. (2025). Hidden β-γ Dehydrogenation Products in Long-Chain Fatty Acid Oxidation Unveiled by NMR: Implications on Lipid Metabolism. ACS Bio Med Chem Au 5:262-267. PMID: 40255280; PMCID: PMC12006827; DOI: 10.1021/acsbiomedchemau.4c00140; https://pubmed.ncbi.nlm.nih.gov/40255280/
* **wang-2026-acad9-cytosolic-traf6** — Wang M, Yuan C, Zhang Y, et al. (2026). Moonlighting cytosolic function of ACAD9: suppression of TRAF6-mediated osteoclastogenesis and protection against osteoporosis. Cell Death Dis 17:362. PMID: 41888097; PMCID: PMC13039524; DOI: 10.1038/s41419-026-08626-z; https://pubmed.ncbi.nlm.nih.gov/41888097/
* **uniprot-A0A7P0T7Z1-entry** — UniProtKB/TrEMBL A0A7P0T7Z1 (ACAD9, *Homo sapiens*), entry version 24. https://rest.uniprot.org/uniprotkb/A0A7P0T7Z1.txt
* **uniprot-Q9H845-entry** — UniProtKB/Swiss-Prot Q9H845 (ACAD9_HUMAN, Complex I assembly factor ACAD9, mitochondrial). https://rest.uniprot.org/uniprotkb/Q9H845.txt
* **ensembl-ACAD9-isoforms** — Ensembl REST lookups for ENST00000680636 (ACAD9-219) and ENST00000308982 (ACAD9-201), gene ENSG00000177646. https://rest.ensembl.org/lookup/id/ENST00000680636 ; https://rest.ensembl.org/lookup/id/ENST00000308982 (saved as citations/ensembl-*-lookup.json; isoform comparison in citations/ensembl-ACAD9-isoforms-summary.md and citations/uniprot-A0A7P0T7Z1-summary.md)
* **swigonova-2009-acad-evolution** — Swigonová Z, Mohsen AW, Vockley J. (2009). Acyl-CoA dehydrogenases: Dynamic history of protein family evolution. J Mol Evol 69:176-193. PMID: 19639238; PMCID: PMC4136416; DOI: 10.1007/s00239-009-9263-0; https://pubmed.ncbi.nlm.nih.gov/19639238/
* **sinsheimer-2021-acad9-mouse** — Sinsheimer A, Mohsen AW, Bloom K, et al. (2021). Development and characterization of a mouse model for Acad9 deficiency. Mol Genet Metab 134:156-163. PMID: 34556413; PMCID: PMC8588265; DOI: 10.1016/j.ymgme.2021.09.002; https://pubmed.ncbi.nlm.nih.gov/34556413/
* **speijer-2022-acad9-fadh2-nadh** — Speijer D. (2022). Molecular characteristics of the multi-functional FAO enzyme ACAD9 illustrate the importance of FADH(2)/NADH ratios for mitochondrial ROS formation. Bioessays 44:e2200056. PMID: 35708204; DOI: 10.1002/bies.202200056; https://pubmed.ncbi.nlm.nih.gov/35708204/
* **vanhove-2024-acad9-bezafibrate** — Van Hove JLK, Friederich MW, Hock DH, et al. (2024). ACAD9 treatment with bezafibrate and nicotinamide riboside temporarily stabilizes cardiomyopathy and lactic acidosis. Mitochondrion 78:101905. PMID: 38797357; PMCID: PMC11390326; DOI: 10.1016/j.mito.2024.101905; https://pubmed.ncbi.nlm.nih.gov/38797357/
* **ensembl-ACAD9-transcript-tags** — Ensembl REST overlap/id/ENSG00000177646 (feature=transcript), tags and transcript support levels for ENST00000680636 and ENST00000308982. https://rest.ensembl.org/overlap/id/ENSG00000177646?feature=transcript (saved as citations/ensembl-ACAD9-transcript-tags.json)


## Citations

1. alston-2016-tmem126b-abstract.md
2. alston-2016-tmem126b-fulltext.txt
3. alston-2016-tmem126b-summary.md
4. carroll-2021-tmem70-tmem242-abstract.md
5. carroll-2021-tmem70-tmem242-fulltext.txt
6. carroll-2021-tmem70-tmem242-summary.md
7. ensembl-ACAD9-isoforms-summary.md
8. ensembl-ACAD9-transcript-tags-summary.md
9. ensembl-ACAD9-transcript-tags.json
10. ensembl-ENST00000308982-lookup.json
11. ensembl-ENST00000680636-lookup.json
12. ensenauer-2005-acad9-unsaturated-abstract.md
13. ensenauer-2005-acad9-unsaturated-summary.md
14. fabbian-2025-beta-gamma-dehydrogenation-abstract.md
15. fabbian-2025-beta-gamma-dehydrogenation-fulltext.txt
16. fabbian-2025-beta-gamma-dehydrogenation-summary.md
17. formosa-2020-mcia-dissection-abstract.md
18. formosa-2020-mcia-dissection-summary.md
19. gerards-2011-riboflavin-acad9-abstract.md
20. gerards-2011-riboflavin-acad9-summary.md
21. giachin-2021-mcia-deflavination-abstract.md
22. giachin-2021-mcia-deflavination-fulltext.txt
23. giachin-2021-mcia-deflavination-summary.md
24. haack-2010-exome-acad9-abstract.md
25. haack-2010-exome-acad9-summary.md
26. he-2007-acad9-deficiency-abstract.md
27. he-2007-acad9-deficiency-summary.md
28. he-2011-new-lcads-abstract.md
29. he-2011-new-lcads-fulltext.txt
30. he-2011-new-lcads-summary.md
31. houten-2016-fao-review-abstract.md
32. houten-2016-fao-review-summary.md
33. mcgregor-2023-mcia-assembly-abstract.md
34. mcgregor-2023-mcia-assembly-fulltext.txt
35. mcgregor-2023-mcia-assembly-summary.md
36. nouws-2010-acad9-complexI-abstract.md
37. nouws-2010-acad9-complexI-summary.md
38. nouws-2014-acad9-moonlighting-abstract.md
39. nouws-2014-acad9-moonlighting-summary.md
40. repp-2018-acad9-70-patients-abstract.md
41. repp-2018-acad9-70-patients-fulltext.txt
42. repp-2018-acad9-70-patients-summary.md
43. schiff-2015-acad9-dual-function-abstract.md
44. schiff-2015-acad9-dual-function-summary.md
45. sinsheimer-2021-acad9-mouse-abstract.md
46. sinsheimer-2021-acad9-mouse-fulltext.txt
47. sinsheimer-2021-acad9-mouse-summary.md
48. speijer-2022-acad9-fadh2-nadh-abstract.md
49. speijer-2022-acad9-fadh2-nadh-summary.md
50. swigonova-2009-acad-evolution-abstract.md
51. swigonova-2009-acad-evolution-fulltext.txt
52. swigonova-2009-acad-evolution-summary.md
53. uniprot-A0A7P0T7Z1-entry.fasta
54. uniprot-A0A7P0T7Z1-entry.txt
55. uniprot-A0A7P0T7Z1-summary.md
56. uniprot-Q9H845-entry.txt
57. vanhove-2024-acad9-bezafibrate-abstract.md
58. vanhove-2024-acad9-bezafibrate-fulltext.txt
59. vanhove-2024-acad9-bezafibrate-summary.md
60. wang-2026-acad9-cytosolic-traf6-abstract.md
61. wang-2026-acad9-cytosolic-traf6-fulltext.txt
62. wang-2026-acad9-cytosolic-traf6-summary.md
63. xia-2021-acad9-binding-partners-abstract.md
64. xia-2021-acad9-binding-partners-fulltext.txt
65. xia-2021-acad9-binding-partners-summary.md
66. zhang-2002-acad9-cloning-abstract.md
67. zhang-2002-acad9-cloning-summary.md