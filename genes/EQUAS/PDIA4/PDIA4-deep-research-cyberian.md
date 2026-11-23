---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:38:29.725970'
end_time: '2026-10-26T00:50:57.581529'
duration_seconds: 747.86
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: PDIA4
  gene_symbol: PDIA4
  uniprot_accession: A0A8C4LTV9
  protein_description: 'RecName: Full=Protein disulfide-isomerase {ECO:0000256|RuleBase:RU361130};
    EC=5.3.4.1 {ECO:0000256|RuleBase:RU361130};'
  gene_info: Name=PDIA4 {ECO:0000313|Ensembl:ENSEASP00005012888.2};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the protein disulfide isomerase family.
  protein_domains: KRAB. (IPR001909); KRAB_dom_sf. (IPR036051); PDI_thioredoxin-like_dom.
    (IPR005788); PDIA4_PDI_b. (IPR041866); Prot_disulphide_isomerase. (IPR005792)
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
citation_count: 62
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A8C4LTV9
- **Protein Description:** RecName: Full=Protein disulfide-isomerase {ECO:0000256|RuleBase:RU361130}; EC=5.3.4.1 {ECO:0000256|RuleBase:RU361130};
- **Gene Information:** Name=PDIA4 {ECO:0000313|Ensembl:ENSEASP00005012888.2};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the protein disulfide isomerase family.
- **Key Domains:** KRAB. (IPR001909); KRAB_dom_sf. (IPR036051); PDI_thioredoxin-like_dom. (IPR005788); PDIA4_PDI_b. (IPR041866); Prot_disulphide_isomerase. (IPR005792)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "PDIA4" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'PDIA4' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **PDIA4** (gene ID: PDIA4, UniProt: A0A8C4LTV9) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# PDIA4 (ERp72) in the donkey, *Equus asinus* (UniProt A0A8C4LTV9): function, localization and pathways

## Introduction and summary

UniProt A0A8C4LTV9 is an unreviewed TrEMBL entry for the donkey gene *PDIA4*. It is named "protein disulfide-isomerase" (EC 5.3.4.1) and placed in the protein disulfide isomerase family. Its sequence comes from the chromosome-level genome assembly of a male Dezhou donkey [uniprot-A0A8C4LTV9-record][wang-2020-donkey-genomes-abstract]. There is no experimental literature on donkey PDIA4. Everything known about its function is therefore inferred from orthologs: human PDIA4/ERp72, murine ERp72 and rat CaBP2/ERp72. The donkey PDIA4 region is about 88% identical to human PDIA4 (this work, analysis/NOTES_sequence_analysis.md).

The identity check found that the gene symbol is correct but the protein model is not. Residues ~588–1197 of the 1197-residue entry are a faithful PDIA4 ortholog. The first ~580 residues are a KRAB-type C2H2 zinc-finger protein that matches human ZNF786. ZNF786 lies directly upstream of *PDIA4*, on the same strand, at human 7q36.1. This explains the odd KRAB, C2H2 and "regulation of DNA-templated transcription" annotations on the entry. They almost certainly come from a read-through or merged gene model, and they do not describe a biological property of PDIA4 (this work).

Read as PDIA4, the protein is an ER-luminal thiol–disulfide oxidoreductase of the PDI family. Its domain order is a°–a–b–b′–a′, with three thioredoxin-fold catalytic domains, each carrying a CGHC active site [mazzarella-1990-erp72-active-sites-abstract][kozlov-2009-erp72-structure-abstract][kozlov-2010-erp72-a0a-structure-abstract]. It catalyses the formation, reduction and isomerization (rearrangement) of disulfide bonds in client proteins of the secretory pathway [ellgaard-2005-pdi-family-review-abstract][appenzeller-herzog-2008-pdi-family-review-abstract]. A C-terminal KEEL-type tetrapeptide keeps it in the ER, where it is abundant [mazzarella-1990-erp72-active-sites-abstract][van-1993-cabp2-erp72-abstract]. Its substrate range is narrower than that of PDI or ERp57 [rutkevich-2010-pdi-family-oxidative-folding-fulltext]. It belongs to a BiP/GRP94-centred multichaperone network that is separate from the calnexin/calreticulin cycle [meunier-2002-er-multiprotein-complex-abstract][kozlov-2009-erp72-structure-abstract]. It also has roles in ER quality control and retention of misfolded proteins [forster-2006-retrotranslocation-abstract], in the ER-stress response [hartley-2013-manf-creld2-abstract], and, outside the cell, on the surface of activated platelets, where it supports thrombosis [zhou-2017-erp72-thrombosis-abstract][holbrook-2018-erp72-antibody-thrombosis-abstract].

## Identity verification and the anomalous gene model

The entry is annotated with gene name PDIA4 (Ensembl ENSEASP00005012888.2, gene ENSEASG00005009014.2, donkey chromosome 1). Its catalytic-activity line reads "Catalyzes the rearrangement of -S-S- bonds in proteins", and its family assignments are PANTHER PTHR18929:SF210 (protein disulfide-isomerase A4) and NCBIfam TIGR01130 (ER_PDI_fam). Its CDD hits are PDI_b_ERp72 and PDI_b′_ERp72_ERp57 [uniprot-A0A8C4LTV9-record]. The same record, however, lists a KRAB domain (residues 9–80), ten C2H2 zinc fingers (residues 196–579) and keywords for DNA binding, transcription regulation and nuclear localization. It even has a second SIMILARITY line placing it in the "krueppel C2H2-type zinc-finger protein family" [uniprot-A0A8C4LTV9-record]. Members of the PDI family do not contain these domains.

To resolve this, the donkey sequence was aligned with MAFFT to reviewed human PDIA4 (P13667). The C-terminal ~617 residues align along the full length of human PDIA4, with 569 of 645 aligned positions identical (88.2%) (this work). They include the acidic N-terminal segment typical of ERp72, all three CGHC motifs, and the C-terminal retention motif. The first ~590 residues have no counterpart in PDIA4. They align with human zinc-finger protein 786 (ZNF786, Q8N393) at 63.7% identity over 575 positions (this work), a level typical of orthologous KRAB-ZNFs, which evolve fast. In the human genome (NCBI Gene), *PDIA4* lies at chr7:149,003,050–149,028,504 on the minus strand. *ZNF786* lies about 41 kb upstream on the same strand (chr7:149,069,640–149,090,717), followed by *ZNF425*, *ZNF398* and *ZNF282*. A transcript that starts in *ZNF786* exons and splices into *PDIA4* therefore yields exactly the fused architecture seen in A0A8C4LTV9.

The donkey Ensembl annotation (assembly ASM1607732v2) shows the same structure directly. The PDIA4 gene ENSEASG00005009014 spans chr1:1,023,772–1,078,943 on the plus strand. Its canonical transcript, PDIA4-201, has 13 exons. The first four exons lie between 1,023,772 and 1,036,715, and one of them is a 1,446-bp exon of the size typical of a KRAB-ZNF zinc-finger array. The exons encoding PDIA4 begin only at 1,062,090, more than 25 kb further downstream. Immediately upstream lies ZNF425 (1,004,371–1,014,880, plus strand), followed by ZNF398 and ZNF282. No separate ZNF786 gene is annotated anywhere within 150 kb (this work; analysis/ensembl_donkey_PDIA4_gene.json, analysis/ensembl_donkey_neighbours.json). The donkey gene order ZNF425–[ZNF786]–PDIA4 therefore matches human 7q36.1, and the missing ZNF786 gene has been absorbed into the PDIA4 model.

Three further observations support an annotation artifact rather than a real fusion protein. First, a second donkey entry from the same Ensembl gene, A0A8C4PKQ4 (664 aa), keeps only the first 49 KRAB residues before PDIA4 [uniprot-A0A8C4PKQ4-record]. This matches its transcript, PDIA4-202, which skips the two zinc-finger exons but keeps the two KRAB exons (this work). Second, the horse has a 1248-residue fusion model (F6WGL8) alongside a 645-residue PDIA4 model (A0A3Q2IEH6). The horse 645-residue model begins with a canonical hydrophobic signal peptide (MRPRKACLLLLLLALAQLLAVASA…) that closely resembles human residues 1–20, which UniProt annotates as the signal peptide [uniprot-P13667-record] (this work). Third, both donkey models lack this signal peptide, because the ZNF exons replace the native PDIA4 first exon. A protein without a signal peptide could not enter the ER, where every characterized ERp72 function takes place. The biologically relevant donkey protein is therefore best treated as a ~645-residue PDIA4 with an N-terminal signal peptide, as in horse and human. The KRAB/zinc-finger and nuclear/transcriptional annotations on A0A8C4LTV9 should be disregarded for functional annotation of PDIA4.

## Domain architecture and catalytic mechanism

ERp72 was first cloned as an abundant ER-luminal protein that shares sequence with PDI (ERp59) in three separate regions, each with a CGHC active-site sequence [mazzarella-1990-erp72-active-sites-abstract]. The rat homolog, first described as the calcium-binding glycoprotein CaBP2, was shown independently to have three -EFYAPWCGHCK- thioredoxin motifs and real protein disulfide isomerase activity [van-1993-cabp2-erp72-abstract]. The donkey sequence has the same motif three times: EFYAPWCGHCKQF (a°, Cys643/Cys646), EFYAPWCGHCKKL (a, Cys758/Cys761) and EFYAPWCGHCKQL (a′, Cys1107/Cys1110 in the fusion numbering) [uniprot-A0A8C4LTV9-record].

Structural work on rat ERp72 defined five thioredoxin-like domains in the order a°–a–b–b′–a′. In this arrangement, the catalytic a°, a and a′ flank the non-catalytic b and b′ [kozlov-2009-erp72-structure-abstract][kozlov-2010-erp72-a0a-structure-abstract]. This matches the domain-boundary analysis of the human redox-active PDIs [alanen-2003-pdi-domain-boundaries-abstract]. The a° domain has an extra N-terminal β-strand, and in the a domain a conserved arginine reaches into the core to form a salt bridge near the catalytic site [kozlov-2010-erp72-a0a-structure-abstract]. A conserved arginine of this kind in the β5–α4 loop of PDI-family catalytic domains, including those of ERp72, is needed to reoxidize the enzyme. It does so by modulating the pKa of the active-site cysteines, which lets the domain act as an oxidant and then regenerate [lappi-2004-conserved-arginine-abstract]. SAXS-based models of full-length ERp72 place all three active sites roughly facing each other, next to hydrophobic patches that probably bind substrates [kozlov-2010-erp72-a0a-structure-abstract][kozlov-2009-erp72-structure-abstract].

Mutagenesis of the three active sites in an insulin-reduction assay showed that each catalytic domain contributes, but in different ways. Domains 1 and 2 (a°, a) contribute mainly to turnover (kcat), and domain 3 (a′) contributes mainly to substrate affinity (Km) [satoh-2005-erp72-thioredoxin-domains-abstract]. Studies with model and viral substrates show that ERp72 can reduce substrate disulfides. Murine polyomavirus is a good example: PDI and ERp72 mainly reduce the virus in vitro, whereas ERp57 mainly isomerizes it [walczak-2011-polyomavirus-pdi-network-abstract]. In cells, cysteine-to-alanine "substrate-trapping" mutants of ERp72 (C-terminal active-site Cys replaced, CXXA) form mixed-disulfide intermediates with client proteins. This confirms that ERp72 forms covalent intermediates with substrates in vivo [hartley-2013-manf-creld2-fulltext]. The reaction is the general PDI reaction: thiol–disulfide exchange between the CGHC dithiol/disulfide and substrate cysteines. It covers net oxidation, reduction and rearrangement of disulfide bonds [ellgaard-2005-pdi-family-review-abstract][appenzeller-herzog-2008-pdi-family-review-abstract].

## Substrate specificity and partners in the ER folding network

PDI is a generalist, and ERp57 is recruited to glycoproteins through calnexin and calreticulin. ERp72 is a specialist. The b–b′ domains of ERp72 resemble those of ERp57, but ERp72 does not bind calnexin, as shown by ITC and NMR [kozlov-2009-erp72-structure-abstract]. The ERp72 bb′ fragment lacks both the positively charged patch that ERp57 uses to bind calnexin and calreticulin and the hydrophobic face thought to mediate PDI's binding of nonnative substrates [rutkevich-2010-pdi-family-oxidative-folding-fulltext]. In human hepatoma cells, depleting ERp72 by more than 95%, alone or together with PDI or ERp57, had minimal effect on the oxidative folding of several well-characterized secretory proteins. Depleting PDI or ERp57 had much larger effects. This points to a narrow substrate specificity for ERp72 [rutkevich-2010-pdi-family-oxidative-folding-abstract][rutkevich-2010-pdi-family-oxidative-folding-fulltext]. The same study notes that ERp72 cannot replace ERp57 in the folding of MHC class I molecules. It also notes that ERp72 has been implicated in the folding of thyroglobulin and apolipoprotein B [rutkevich-2010-pdi-family-oxidative-folding-fulltext].

Systematic substrate trapping in human cells reached a similar conclusion. CXXA mutants of PDI, ERp72, ERp57, ERp46, ERp18 and P5 each trapped distinct but partly overlapping sets of clients, and most of the family, ERp72 included in the comparison, reacted with the oxidase Ero1α [jessop-2009-pdi-family-substrate-specificity-abstract]. Interaction with Ero1α is the expected route by which the active sites are reoxidized after they have oxidized a client. ERp72 can also bind non-native polypeptides without covalent links. When peptides of 8–40 residues are translocated into microsomes by TAP, they bind ERp72 in an ATP-independent manner. ERp72's peptide selectivity is broad and overlaps with, but is not identical to, that of PDI, gp96, calnexin and grp170 [spee-1999-erp72-peptide-binding-abstract].

The best-supported clients are large, disulfide-rich, oligomeric secretory glycoproteins and misfolded proteins. In rat thyroid cells, ERp72 co-immunoprecipitates with BiP, GRP94 and GRP170 on maturing thyroglobulin. It binds stably to thyroglobulin that misfolds after glycosylation is inhibited or ER calcium is perturbed, and it binds thrombospondin in cells that lack thyroglobulin [kuznetsov-1997-chaperone-complexes-abstract]. The disease mutant thyroglobulin G2320R, which causes congenital hypothyroidism in rdw/rdw rats, is retained in the ER with exposed free cysteines. Of all the ER residents, it associates most prominently with ERp72, including through covalent Tg–ERp72 mixed disulfides. Overexpressing ERp72 in thyrocytes increased the fraction of Tg cysteines kept in the reduced state, and an ERAD-resistant pool of mutant Tg was still covalently bound to ERp72 two days after synthesis [menon-2007-erp72-mutant-thyroglobulin-abstract]. This is the most direct cellular evidence for ERp72's client preference, and it fits the reductase and retention activities described below. ERp72 is also part of a large preformed ER multiprotein complex that contains BiP, GRP94, CaBP1 (P5), PDI, ERdj3, cyclophilin B, GRP170, UGGT and SDF2-L1. This complex binds unassembled immunoglobulin heavy chains, while the calnexin/calreticulin system is largely absent from it [meunier-2002-er-multiprotein-complex-abstract]. This complex is the source of the UniProt SUBUNIT annotation for human PDIA4 [uniprot-P13667-record], which is propagated to the donkey entry by rule [uniprot-A0A8C4LTV9-record]. In chondrodysplasia models, ERp72 binds the A-domain of mutant matrilin-3 (V194D), which forms non-native disulfide-bonded aggregates. It does so together with the ER-stress proteins CRELD2 and ARMET/MANF, which explains the "CRELD2–MANF–MATN3–PDIA4" complex annotation [hartley-2013-manf-creld2-abstract][hartley-2013-manf-creld2-fulltext]. Taken together, ERp72 works mainly through the BiP/GRP94 chaperone axis on non-native, disulfide-rich clients, and not through the lectin-chaperone cycle.

## Subcellular localization: ER lumen, quality control and the cell surface

The main site of PDIA4 action is the ER lumen. ERp72 is an abundant luminal ER protein, and its C-terminal KEEL sequence is a working ER-retention signal: removing it causes much more secretion than removing KDEL from PDI [mazzarella-1990-erp72-active-sites-abstract]. Rat CaBP2/ERp72 likewise ends in KEEL [van-1993-cabp2-erp72-abstract]. All equid PDIA4 models end in …LSRTREEL (REEL) rather than the human …LSRTKEEL (this work). This is a conservative K→R substitution at the first position of the retention tetrapeptide (REEL in place of KEEL). It may still be recognized by the KDEL-receptor retrieval system, but this has not been tested.

Inside the ER, ERp72 acts in quality control as well as in folding. In a semipermeabilized-cell assay, PDI promoted retrotranslocation of cholera toxin to the cytosol, whereas ERp72 promoted its retention in the ER. The two proteins changed the toxin's conformation in opposite ways, and the opposing activities also applied to endogenous misfolded ER proteins [forster-2006-retrotranslocation-abstract]. This places ERp72 on the side of ER retention in the triage between retention and ER-associated degradation. Through its reductase activity, ERp72 also helps murine polyomavirus infection in the ER [walczak-2011-polyomavirus-pdi-network-abstract]. Human PDIA4 also binds the capsid spike proteins of human astrovirus serotypes 1 and 8, but not 2. PDIA4 knockdown or the PDI inhibitor 16F16 blocks HAstV-8 infection at genome uncoating, not at attachment or internalization [aguilar-hernandez-2020-pdia4-astrovirus-abstract][aguilar-hernandez-2020-pdia4-astrovirus-fulltext]. This is the source of the microbial-infection SUBUNIT annotation on human PDIA4 [uniprot-P13667-record]. ERp72's retention activity fits its covalent and prolonged binding to misfolded mutant thyroglobulin, part of which resists ERAD [menon-2007-erp72-mutant-thyroglobulin-abstract].

There is good evidence for a second, extracellular site of action on blood cells. ERp72 is present on the surface of resting platelets, and its levels rise on activation. A humanized inhibitory antibody against ERp72 reduced platelet aggregation, granule secretion, calcium mobilization and integrin activation, and protected mice from thrombosis [holbrook-2018-erp72-antibody-thrombosis-abstract]. Conditional deletion of ERp72 in blood and endothelial cells prolonged bleeding and reduced platelet accumulation and fibrin deposition. Rescue experiments showed that the a and a′ CGHC motifs are required, and ERp72 bound integrin αIIbβ3 and generated free thiols in it [zhou-2017-erp72-thrombosis-abstract]. This is consistent with the "cell surface" GO term on the donkey entry [uniprot-A0A8C4LTV9-record].

The "melanosome" annotation comes from mass-spectrometric detection of PDIA4 in melanosome fractions at all stages of melanosome development [uniprot-P13667-record][chi-2006-melanosome-proteomics-abstract]. This is high-throughput organelle proteomics, and given how abundant ERp72 is in the ER, it may reflect ER contamination or transit rather than a melanosome-specific function. The "nucleus" annotation on the donkey entry comes from the fused zinc-finger region and should not be applied to PDIA4 (this work).

## Pathways and physiological roles

**Unfolded protein response.** PDIA4 is a classic ER-stress-inducible gene. Rat CaBP2/ERp72 rises in parallel with BiP when glycosylation is impaired [van-1993-cabp2-erp72-abstract]. In chondrocytes under ER stress from mutant matrilin-3, *Pdia4* was among the 20 most upregulated genes, together with *Pdia3* and *Pdia6* [hartley-2013-manf-creld2-fulltext]. Its role in the UPR is that of an effector: it adds folding and disulfide-handling capacity, and there is no evidence that it acts as a signalling sensor.

**Haemostasis and thrombosis.** The extracellular ERp72 on platelets described above acts on integrin αIIbβ3 and on the coagulation (fibrin) pathway [zhou-2017-erp72-thrombosis-abstract][holbrook-2018-erp72-antibody-thrombosis-abstract]. Of the non-canonical roles, this one has the most precise biochemical evidence.

**Cell survival, cancer and metabolic disease.** PDIA4 is upregulated in several tumors. It promotes tumor growth by binding procaspases 3 and 7 in a CGHC-dependent manner and inhibiting their activation [kuo-2017-pdia4-procaspase-abstract]. Cisplatin-resistant lung adenocarcinoma cells overexpress PDIA4 and PDIA6, and inactivating PDIA4 restores mitochondrial apoptosis [tufo-2014-pdia4-cisplatin-abstract]. In mouse β-cells, Pdia4 is induced by nutrient excess and promotes β-cell failure. It does this by binding and stabilizing Ndufs3 (mitochondrial complex I) and p22phox (the NADPH-oxidase subunit), which raises ROS. Pdia4 ablation or pharmacological inhibition alleviates diabetes in mice [kuo-2021-pdia4-beta-cell-abstract][kuo-2021-pdia4-beta-cell-fulltext]. Unlike *Pdia3*, *Pdia4* is not essential: knockout mice survive without an obvious phenotype [kuo-2021-pdia4-beta-cell-fulltext]. These findings link PDIA4 to apoptosis and redox signalling. However, how an ER-luminal enzyme reaches cytosolic procaspases or mitochondrial complex I is not explained, so these roles are best seen as pleiotropic consequences, not the primary molecular function.

## Evolutionary and bioinformatic inference for the donkey protein

The donkey protein matches human PDIA4 at 88% of aligned positions, and it shares the PDIA4 domain organization and the …LSRTREEL C-terminus with the horse models (this work). It keeps every feature tied to ERp72 function: the acidic N-terminal stretch, three CGHC motifs in the a°, a and a′ domains, the b/b′ domains classified in CDD as ERp72-type, and the C-terminal xEEL retention motif [uniprot-A0A8C4LTV9-record]. Because the PDI family is so well conserved across vertebrates [appenzeller-herzog-2008-pdi-family-review-abstract][ellgaard-2005-pdi-family-review-abstract], all the core activities of mammalian ERp72 can be confidently transferred to the donkey protein: disulfide isomerase activity (GO:0003756), protein folding in the ER, ER lumen localization, and the response to ER stress. Annotations that depend on the fused KRAB/C2H2 region (DNA binding, regulation of transcription, nuclear localization, zinc binding) should not be transferred. They reflect a gene-model artifact. The catalytic-activity statement (EC 5.3.4.1) and the PDI-family classification are appropriate.

## Open Questions

The most urgent open question is the donkey gene structure itself. RNA-seq or long-read evidence should show whether donkey cells make a ZNF786–PDIA4 read-through transcript at all, or whether the Ensembl model ENSEASG00005009014 simply merged two neighbouring genes. The absence of any separate ZNF786 gene in the donkey Ensembl annotation argues for the latter. A corrected model should restore the PDIA4 signal-peptide exon, as the horse model A0A3Q2IEH6 does, and a separate ZNF786 gene model should be created. Feedback to Ensembl and UniProt would remove the transcription-related annotations that this artifact has spread.

The equid C-terminus …REEL, rather than …KEEL, has not been tested experimentally. Expressing equine PDIA4 with and without the tetrapeptide would confirm ER retention. At the level of mechanism, it is still unclear how ERp72 recognizes its narrow set of clients, given that its bb′ region lacks both the PDI-type hydrophobic pocket and the ERp57-type calnexin-binding patch [rutkevich-2010-pdi-family-oxidative-folding-fulltext][kozlov-2009-erp72-structure-abstract]. Client-trapping proteomics with ERp72 CXXA mutants in relevant cell types would address this. The basis of its opposite role to PDI in ER retention versus retrotranslocation [forster-2006-retrotranslocation-abstract] also needs structural explanation.

The extracellular and non-ER roles raise topological questions. How ERp72 escapes KEEL-mediated retention to reach the platelet surface, and how PDIA4 reaches cytosolic procaspases and mitochondrial Ndufs3 [kuo-2017-pdia4-procaspase-abstract][kuo-2021-pdia4-beta-cell-fulltext], remains unexplained. Finally, nothing is known about PDIA4 in equid physiology. Platelet-surface thiol isomerases, PDIA4 induction in equine metabolic syndrome or laminitis, and its role in the high secretory load of donkey milk-producing mammary tissue are all plausible but untested areas for follow-up.

## References

- **[aguilar-hernandez-2020-pdia4-astrovirus]** Aguilar-Hernández N, Meyer L, López S, DuBois RM, Arias CF. Protein Disulfide Isomerase A4 Is Involved in Genome Uncoating during Human Astrovirus Cell Entry. Viruses. 2020;13. PMID:33396308; PMCID:PMC7824429; DOI:10.3390/v13010053. https://pubmed.ncbi.nlm.nih.gov/33396308/
- **[alanen-2003-pdi-domain-boundaries]** Alanen HI, Salo KE, Pekkala M, Siekkinen HM, Pirneskoski A, Ruddock LW. Defining the domain boundaries of the human protein disulfide isomerases. Antioxid Redox Signal. 2003;5:367-74. PMID:13678523; DOI:10.1089/152308603768295096. https://pubmed.ncbi.nlm.nih.gov/13678523/
- **[appenzeller-herzog-2008-pdi-family-review]** Appenzeller-Herzog C, Ellgaard L. The human PDI family: versatility packed into a single fold. Biochim Biophys Acta. 2008;1783:535-48. PMID:18093543; DOI:10.1016/j.bbamcr.2007.11.010. https://pubmed.ncbi.nlm.nih.gov/18093543/
- **[chi-2006-melanosome-proteomics]** Chi A, Valencia JC, Hu ZZ, Watabe H, Yamaguchi H, Mangini NJ, Huang H, Canfield VA, Cheng KC, Yang F, Abe R, Yamagishi S, Shabanowitz J, Hearing VJ, Wu C, Appella E, Hunt DF. Proteomic and bioinformatic characterization of the biogenesis and function of melanosomes. J Proteome Res. 2006;5:3135-44. PMID:17081065; DOI:10.1021/pr060363j. https://pubmed.ncbi.nlm.nih.gov/17081065/
- **[ellgaard-2005-pdi-family-review]** Ellgaard L, Ruddock LW. The human protein disulphide isomerase family: substrate interactions and functional properties. EMBO Rep. 2005;6:28-32. PMID:15643448; PMCID:PMC1299221; DOI:10.1038/sj.embor.7400311. https://pubmed.ncbi.nlm.nih.gov/15643448/
- **[forster-2006-retrotranslocation]** Forster ML, Sivick K, Park YN, Arvan P, Lencer WI, Tsai B. Protein disulfide isomerase-like proteins play opposing roles during retrotranslocation. J Cell Biol. 2006;173:853-9. PMID:16785320; PMCID:PMC2063911; DOI:10.1083/jcb.200602046. https://pubmed.ncbi.nlm.nih.gov/16785320/
- **[hartley-2013-manf-creld2]** Hartley CL, Edwards S, Mullan L, Bell PA, Fresquet M, Boot-Handford RP, Briggs MD. Armet/Manf and Creld2 are components of a specialized ER stress response provoked by inappropriate formation of disulphide bonds: implications for genetic skeletal diseases. Hum Mol Genet. 2013;22:5262-75. PMID:23956175; PMCID:PMC3842181; DOI:10.1093/hmg/ddt383. https://pubmed.ncbi.nlm.nih.gov/23956175/
- **[holbrook-2018-erp72-antibody-thrombosis]** Holbrook LM, Sandhar GK, Sasikumar P, Schenk MP, Stainer AR, Sahli KA, Flora GD, Bicknell AB, Gibbins JM. A humanized monoclonal antibody that inhibits platelet-surface ERp72 reveals a role for ERp72 in thrombosis. J Thromb Haemost. 2018;16:367-377. PMID:29052936; PMCID:PMC5838528; DOI:10.1111/jth.13878. https://pubmed.ncbi.nlm.nih.gov/29052936/
- **[jessop-2009-pdi-family-substrate-specificity]** Jessop CE, Watkins RH, Simmons JJ, Tasab M, Bulleid NJ. Protein disulphide isomerase family members show distinct substrate specificity: P5 is targeted to BiP client proteins. J Cell Sci. 2009;122:4287-95. PMID:19887585; PMCID:PMC2779130; DOI:10.1242/jcs.059154. https://pubmed.ncbi.nlm.nih.gov/19887585/
- **[kozlov-2009-erp72-structure]** Kozlov G, Määttänen P, Schrag JD, Hura GL, Gabrielli L, Cygler M, Thomas DY, Gehring K. Structure of the noncatalytic domains and global fold of the protein disulfide isomerase ERp72. Structure. 2009;17:651-9. PMID:19446521; DOI:10.1016/j.str.2009.02.016. https://pubmed.ncbi.nlm.nih.gov/19446521/
- **[kozlov-2010-erp72-a0a-structure]** Kozlov G, Azeroual S, Rosenauer A, Määttänen P, Denisov AY, Thomas DY, Gehring K. Structure of the catalytic a(0)a fragment of the protein disulfide isomerase ERp72. J Mol Biol. 2010;401:618-25. PMID:20600112; DOI:10.1016/j.jmb.2010.06.045. https://pubmed.ncbi.nlm.nih.gov/20600112/
- **[kuo-2017-pdia4-procaspase]** Kuo TF, Chen TY, Jiang ST, Chen KW, Chiang YM, Hsu YJ, Liu YJ, Chen HM, Yokoyama KK, Tsai KC, Yeh HH, Chen YR, Yang MT, Yang CY, Yang WC. Protein disulfide isomerase a4 acts as a novel regulator of cancer growth through the procaspase pathway. Oncogene. 2017;36:5484-5496. PMID:28534513; DOI:10.1038/onc.2017.156. https://pubmed.ncbi.nlm.nih.gov/28534513/
- **[kuo-2021-pdia4-beta-cell]** Kuo TF, Hsu SW, Huang SH, Chang CL, Feng CS, Huang MG, Chen TY, Yang MT, Jiang ST, Wen TN, Yang CY, Huang CY, Kao SH, Tsai KC, Yang G, Yang WC. Pdia4 regulates β-cell pathogenesis in diabetes: molecular mechanism and targeted therapy. EMBO Mol Med. 2021;13:e11668. PMID:34542937; PMCID:PMC8495450; DOI:10.15252/emmm.201911668. https://pubmed.ncbi.nlm.nih.gov/34542937/
- **[kuznetsov-1997-chaperone-complexes]** Kuznetsov G, Chen LB, Nigam SK. Multiple molecular chaperones complex with misfolded large oligomeric glycoproteins in the endoplasmic reticulum. J Biol Chem. 1997;272:3057-63. PMID:9006956; DOI:10.1074/jbc.272.5.3057. https://pubmed.ncbi.nlm.nih.gov/9006956/
- **[lappi-2004-conserved-arginine]** Lappi AK, Lensink MF, Alanen HI, Salo KE, Lobell M, Juffer AH, Ruddock LW. A conserved arginine plays a role in the catalytic cycle of the protein disulphide isomerases. J Mol Biol. 2004;335:283-95. PMID:14659757; DOI:10.1016/j.jmb.2003.10.051. https://pubmed.ncbi.nlm.nih.gov/14659757/
- **[mazzarella-1990-erp72-active-sites]** Mazzarella RA, Srinivasan M, Haugejorden SM, Green M. ERp72, an abundant luminal endoplasmic reticulum protein, contains three copies of the active site sequences of protein disulfide isomerase. J Biol Chem. 1990;265:1094-101. PMID:2295602. https://pubmed.ncbi.nlm.nih.gov/2295602/
- **[menon-2007-erp72-mutant-thyroglobulin]** Menon S, Lee J, Abplanalp WA, Yoo SE, Agui T, Furudate S, Kim PS, Arvan P. Oxidoreductase interactions include a role for ERp72 engagement with mutant thyroglobulin from the rdw/rdw rat dwarf. J Biol Chem. 2007;282:6183-91. PMID:17200118; PMCID:PMC2542443; DOI:10.1074/jbc.M608863200. https://pubmed.ncbi.nlm.nih.gov/17200118/
- **[meunier-2002-er-multiprotein-complex]** Meunier L, Usherwood YK, Chung KT, Hendershot LM. A subset of chaperones and folding enzymes form multiprotein complexes in endoplasmic reticulum to bind nascent proteins. Mol Biol Cell. 2002;13:4456-69. PMID:12475965; PMCID:PMC138646; DOI:10.1091/mbc.e02-05-0311. https://pubmed.ncbi.nlm.nih.gov/12475965/
- **[rutkevich-2010-pdi-family-oxidative-folding]** Rutkevich LA, Cohen-Doyle MF, Brockmeier U, Williams DB. Functional relationship between protein disulfide isomerase family members during the oxidative folding of human secretory proteins. Mol Biol Cell. 2010;21:3093-105. PMID:20660153; PMCID:PMC2938376; DOI:10.1091/mbc.E10-04-0356. https://pubmed.ncbi.nlm.nih.gov/20660153/
- **[satoh-2005-erp72-thioredoxin-domains]** Satoh M, Shimada A, Keino H, Kashiwai A, Nagai N, Saga S, Hosokawa M. Functional characterization of 3 thioredoxin homology domains of ERp72. Cell Stress Chaperones. 2005;10:278-84. PMID:16333982; PMCID:PMC1283873; DOI:10.1379/csc-116r.1. https://pubmed.ncbi.nlm.nih.gov/16333982/
- **[spee-1999-erp72-peptide-binding]** Spee P, Subjeck J, Neefjes J. Identification of novel peptide binding proteins in the endoplasmic reticulum: ERp72, calnexin, and grp170. Biochemistry. 1999;38:10559-66. PMID:10441153; DOI:10.1021/bi990321r. https://pubmed.ncbi.nlm.nih.gov/10441153/
- **[tufo-2014-pdia4-cisplatin]** Tufo G, Jones AW, Wang Z, Hamelin J, Tajeddine N, Esposti DD, Martel C, Boursier C, Gallerne C, Migdal C, Lemaire C, Szabadkai G, Lemoine A, Kroemer G, Brenner C. The protein disulfide isomerases PDIA4 and PDIA6 mediate resistance to cisplatin-induced cell death in lung adenocarcinoma. Cell Death Differ. 2014;21:685-95. PMID:24464223; PMCID:PMC3978299; DOI:10.1038/cdd.2013.193. https://pubmed.ncbi.nlm.nih.gov/24464223/
- **[van-1993-cabp2-erp72]** Van PN, Rupp K, Lampen A, Söling HD. CaBP2 is a rat homolog of ERp72 with proteindisulfide isomerase activity. Eur J Biochem. 1993;213:789-95. PMID:8477750; DOI:10.1111/j.1432-1033.1993.tb17821.x. https://pubmed.ncbi.nlm.nih.gov/8477750/
- **[walczak-2011-polyomavirus-pdi-network]** Walczak CP, Tsai B. A PDI family network acts distinctly and coordinately with ERp29 to facilitate polyomavirus infection. J Virol. 2011;85:2386-96. PMID:21159867; PMCID:PMC3067762; DOI:10.1128/JVI.01855-10. https://pubmed.ncbi.nlm.nih.gov/21159867/
- **[wang-2020-donkey-genomes]** Wang C, Li H, Guo Y, et al. (52 authors; full list in citations/wang-2020-donkey-genomes-abstract.md). Donkey genomes provide new insights into domestication and selection for coat color. Nat Commun. 2020;11:6014. PMID:33293529; PMCID:PMC7723042; DOI:10.1038/s41467-020-19813-7. https://pubmed.ncbi.nlm.nih.gov/33293529/
- **[zhou-2017-erp72-thrombosis]** Zhou J, Wu Y, Chen F, Wang L, Rauova L, Hayes VM, Poncz M, Li H, Liu T, Liu J, Essex DW. The disulfide isomerase ERp72 supports arterial thrombosis in mice. Blood. 2017;130:817-828. PMID:28576878; PMCID:PMC5553574; DOI:10.1182/blood-2016-12-755587. https://pubmed.ncbi.nlm.nih.gov/28576878/
- **[uniprot-A0A8C4LTV9-record]** UniProtKB/TrEMBL entry A0A8C4LTV9_EQUAS, Protein disulfide-isomerase (PDIA4), Equus asinus; entry version 23 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A8C4LTV9.txt
- **[uniprot-A0A8C4PKQ4-record]** UniProtKB/TrEMBL entry A0A8C4PKQ4_EQUAS, Protein disulfide-isomerase (PDIA4), Equus asinus. https://rest.uniprot.org/uniprotkb/A0A8C4PKQ4.txt
- **[uniprot-P13667-record]** UniProtKB/Swiss-Prot entry P13667 (PDIA4_HUMAN), Protein disulfide-isomerase A4, Homo sapiens. https://rest.uniprot.org/uniprotkb/P13667.txt
- **(this work)** Sequence alignments and locus analysis in analysis/ (MAFFT v7.526 alignments all.aln, znf.afa; NCBI Gene coordinates in human_7q36_neighbours.txt; Ensembl REST donkey gene/locus JSON files; notes in NOTES_sequence_analysis.md).


## Citations

1. aguilar-hernandez-2020-pdia4-astrovirus-abstract.md
2. aguilar-hernandez-2020-pdia4-astrovirus-fulltext.txt
3. aguilar-hernandez-2020-pdia4-astrovirus-summary.md
4. alanen-2003-pdi-domain-boundaries-abstract.md
5. alanen-2003-pdi-domain-boundaries-summary.md
6. appenzeller-herzog-2008-pdi-family-review-abstract.md
7. appenzeller-herzog-2008-pdi-family-review-summary.md
8. chi-2006-melanosome-proteomics-abstract.md
9. chi-2006-melanosome-proteomics-summary.md
10. ellgaard-2005-pdi-family-review-abstract.md
11. ellgaard-2005-pdi-family-review-summary.md
12. forster-2006-retrotranslocation-abstract.md
13. forster-2006-retrotranslocation-fulltext.txt
14. forster-2006-retrotranslocation-summary.md
15. hartley-2013-manf-creld2-abstract.md
16. hartley-2013-manf-creld2-fulltext.txt
17. hartley-2013-manf-creld2-summary.md
18. holbrook-2018-erp72-antibody-thrombosis-abstract.md
19. holbrook-2018-erp72-antibody-thrombosis-fulltext.txt
20. holbrook-2018-erp72-antibody-thrombosis-summary.md
21. jessop-2009-pdi-family-substrate-specificity-abstract.md
22. jessop-2009-pdi-family-substrate-specificity-summary.md
23. kozlov-2009-erp72-structure-abstract.md
24. kozlov-2009-erp72-structure-summary.md
25. kozlov-2010-erp72-a0a-structure-abstract.md
26. kozlov-2010-erp72-a0a-structure-summary.md
27. kuo-2017-pdia4-procaspase-abstract.md
28. kuo-2017-pdia4-procaspase-summary.md
29. kuo-2021-pdia4-beta-cell-abstract.md
30. kuo-2021-pdia4-beta-cell-fulltext.txt
31. kuo-2021-pdia4-beta-cell-summary.md
32. kuznetsov-1997-chaperone-complexes-abstract.md
33. kuznetsov-1997-chaperone-complexes-summary.md
34. lappi-2004-conserved-arginine-abstract.md
35. lappi-2004-conserved-arginine-summary.md
36. mazzarella-1990-erp72-active-sites-abstract.md
37. mazzarella-1990-erp72-active-sites-summary.md
38. menon-2007-erp72-mutant-thyroglobulin-abstract.md
39. menon-2007-erp72-mutant-thyroglobulin-summary.md
40. meunier-2002-er-multiprotein-complex-abstract.md
41. meunier-2002-er-multiprotein-complex-summary.md
42. rutkevich-2010-pdi-family-oxidative-folding-abstract.md
43. rutkevich-2010-pdi-family-oxidative-folding-fulltext.txt
44. rutkevich-2010-pdi-family-oxidative-folding-summary.md
45. satoh-2005-erp72-thioredoxin-domains-abstract.md
46. satoh-2005-erp72-thioredoxin-domains-summary.md
47. spee-1999-erp72-peptide-binding-abstract.md
48. spee-1999-erp72-peptide-binding-summary.md
49. tufo-2014-pdia4-cisplatin-abstract.md
50. tufo-2014-pdia4-cisplatin-summary.md
51. uniprot-A0A8C4LTV9-record.txt
52. uniprot-A0A8C4PKQ4-record.txt
53. uniprot-P13667-record.txt
54. van-1993-cabp2-erp72-abstract.md
55. van-1993-cabp2-erp72-summary.md
56. walczak-2011-polyomavirus-pdi-network-abstract.md
57. walczak-2011-polyomavirus-pdi-network-summary.md
58. wang-2020-donkey-genomes-abstract.md
59. wang-2020-donkey-genomes-fulltext.txt
60. wang-2020-donkey-genomes-summary.md
61. zhou-2017-erp72-thrombosis-abstract.md
62. zhou-2017-erp72-thrombosis-summary.md