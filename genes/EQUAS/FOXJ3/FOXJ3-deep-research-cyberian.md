---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:38:29.152743'
end_time: '2026-10-25T23:45:25.735287'
duration_seconds: 416.58
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: FOXJ3
  gene_symbol: FOXJ3
  uniprot_accession: A0A9L0JKH1
  protein_description: 'SubName: Full=Forkhead box J3 {ECO:0000313|Ensembl:ENSEASP00005053836.1};'
  gene_info: Name=FOXJ3 {ECO:0000313|Ensembl:ENSEASP00005053836.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Not specified in UniProt
  protein_domains: Fork_head_dom. (IPR001766); FOXJ2/3-like. (IPR045912); TF_fork_head_CS_1.
    (IPR018122); TF_fork_head_CS_2. (IPR030456); WH-like_DNA-bd_sf. (IPR036388)
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
citation_count: 74
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JKH1
- **Protein Description:** SubName: Full=Forkhead box J3 {ECO:0000313|Ensembl:ENSEASP00005053836.1};
- **Gene Information:** Name=FOXJ3 {ECO:0000313|Ensembl:ENSEASP00005053836.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** Fork_head_dom. (IPR001766); FOXJ2/3-like. (IPR045912); TF_fork_head_CS_1. (IPR018122); TF_fork_head_CS_2. (IPR030456); WH-like_DNA-bd_sf. (IPR036388)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "FOXJ3" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'FOXJ3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **FOXJ3** (gene ID: FOXJ3, UniProt: A0A9L0JKH1) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# FOXJ3 (Forkhead box J3) in the donkey, *Equus asinus* (UniProt A0A9L0JKH1)

## 1. Introduction and summary

UniProt A0A9L0JKH1 is an unreviewed (TrEMBL) protein of 580 amino acids. It was predicted by Ensembl (ENSEASP00005053836.1, gene ENSEASG00005001210, chromosome 5) from the donkey reference genome [uniprot-A0A9L0JKH1-entry], which was assembled and published by Wang and colleagues as part of a study of donkey domestication [wang-2020-donkey-genomes-abstract]. The entry has a single Fork-head DNA-binding domain (residues 78–173) and two long disordered regions. It belongs to the FOXJ2/3-like (IPR045912; PANTHER PTHR46078:SF3) subfamily. Its only annotations are electronic: nuclear localization and RNA polymerase II-specific DNA-binding transcription factor activity [uniprot-A0A9L0JKH1-entry].

The identity check is straightforward. The gene symbol, the protein description ("Forkhead box J3"), the domain composition and the subfamily all agree. In my own pairwise alignment, the donkey protein shares 97.9% identity with human FOXJ3 (Q9UPW0) and 94.8% with mouse Foxj3 (Q8BUR3), and its forkhead domain is identical across the three species (see `sequence/NOTES.md`). The symbol is not ambiguous: no other gene called FOXJ3 exists, although FOXJ3 must not be confused with its paralogue FOXJ1, the ciliogenesis factor. I found no published experimental work on the donkey or horse FOXJ3 protein itself. Every functional statement below is therefore inferred by orthology from studies of mouse, human, *Xenopus* and zebrafish FOXJ3, and is labelled as such.

Taken together, this literature shows that FOXJ3 is a nuclear, sequence-specific forkhead transcription factor. It binds GTAAACA-type forkhead motifs, with somewhat more relaxed specificity than other FOX proteins [chen-2016-forkhead-binding-fulltext]. In most well-characterized settings it acts as a transcriptional activator of specific target genes. The best-supported targets are *Mef2c* in skeletal muscle [alexander-2010-foxj3-mef2c-abstract], *Pten* and *Tsc1* in cortical neural progenitors [cheng-2026-foxj3-epilepsy-fulltext], *Ppargc1a* (PGC-1α) and *Ucp1* in thermogenic fat [huang-2024-foxj3-thermogenesis-abstract], and meiotic DNA-repair genes in spermatocytes [ni-2016-foxj3-spermatogenesis-abstract]. These targets connect FOXJ3 to four physiological roles: muscle fibre-type identity and regeneration, male germ-cell survival and meiosis, adaptive thermogenesis and mitochondrial biogenesis, and cortical development through the PTEN–mTOR pathway. In other contexts FOXJ3 also represses transcription, for example of TGF-β/Nodal-responsive genes in *Xenopus* [yoon-2025-foxj3-xenopus-tgfb-abstract] and of GABA_A receptor genes in zebrafish [he-2026-terfa-foxj3-zebrafish-abstract].

## 2. Gene identity, protein architecture and evolutionary conservation

The forkhead (FOX) family of winged-helix transcription factors has at least 43 members in humans. FOXJ3 belongs to the J subfamily with FOXJ1 and FOXJ2 [katoh-2004-fox-family-abstract]. Landgren and Carlsson first described mammalian FoxJ3 as a gene found by the genome projects whose closest relative is FoxJ2. Mouse *Foxj3* is a 13-exon, roughly 100 kb gene that encodes a protein of about 623 residues, and the human protein is a similar length [landgren-2004-foxj3-expression-abstract]. Like the human and mouse orthologues, the donkey protein has its forkhead DNA-binding domain near the N-terminus. The rest of the sequence, roughly 400 residues, is largely low-complexity and predicted to be intrinsically disordered [uniprot-A0A9L0JKH1-entry]. Such regions typically carry transactivation or repression functions and mediate protein–protein contacts.

The donkey model is 42 residues shorter than human FOXJ3. In the alignment, the donkey sequence lacks a block corresponding to about human residues 211–253. This block differs from the segment missing in human isoform 2 (residues 177–210) [uniprot-Q9UPW0-entry], so the donkey model probably reflects a different alternative exon choice or a gene-model artefact rather than true divergence (sequence/NOTES.md). The human disease-associated residue Asn351, described below, is conserved and corresponds to donkey Asn308 in an identical local context (QSSLSNSHG). Mouse knockout data and human variant data therefore bear directly on the conserved donkey sequence.

## 3. Molecular function: sequence-specific DNA binding and transcriptional regulation

Direct molecular evidence that FOXJ3 is a DNA-binding transcription factor comes from several independent approaches. In C2C12 myoblasts, Foxj3 bound an evolutionarily conserved forkhead binding site in the skeletal-muscle 5′ enhancer of *Mef2c* and activated that enhancer in a dose-dependent way [alexander-2010-foxj3-mef2c-abstract]. The full paper adds three findings. Chromatin immunoprecipitation of Foxj3-GFP recovered the enhancer segment containing this site. Point mutation of the site abolished activation of a *Mef2c*-luciferase reporter. And a Gal4 DNA-binding-domain fusion of full-length Foxj3 activated a Gal4 reporter about 12-fold, which shows the protein has its own transactivation capacity independent of its forkhead domain [alexander-2010-foxj3-mef2c-fulltext]. Chen and colleagues mapped FOXJ3 occupancy genome-wide by ChIP-seq of inducible 3×FLAG-FOXJ3 in U2OS cells. FOXJ3 binding centred on the canonical GTAAACA forkhead core motif, but FOXJ3 tolerated more variation in the first three bases than FOXK2 or FOXO3 did. At sites co-bound with FOXO3, the preferred motif carried two A residues before TAAACA [chen-2016-forkhead-binding-fulltext]. More than 60% of FOXJ3-bound regions were also occupied by FOXK2. Overexpressing FOXJ3 did not displace FOXK2, and depleting FOXK2 did not change FOXJ3 binding. The authors concluded that FOX factors share sites through dynamic, partial co-occupancy rather than mutually exclusive competition [chen-2016-forkhead-binding-fulltext]. Cheng and colleagues ran ChIP-seq in Neuro2A cells stably expressing FOXJ3 and found about 40,000 peaks per clone. Of these, 14,341 overlapped the active-chromatin mark H3K27ac, and about 6,200 lay near RNA polymerase II-bound transcription start sites, including at *Pten*, *Tsc1*, *Pafah1b1*, *Cep120* and *Dicer1* [cheng-2026-foxj3-epilepsy-fulltext]. These results support assigning a "DNA-binding transcription activator activity, RNA polymerase II-specific" function, which UniProt records for human FOXJ3 with direct-assay evidence [uniprot-Q9UPW0-entry].

Activation is the main output in mammalian systems. FOXJ3 overexpression increased *Pten*, *Tsc1* and *Pafah1b1* transcripts in cortical progenitors, and FOXJ3 was necessary and sufficient for *Pten* expression [cheng-2026-foxj3-epilepsy-fulltext]. Foxj3 also drives *Ppargc1a*/PGC-1α and *Ucp1* expression in brown adipocytes [huang-2024-foxj3-thermogenesis-abstract]. FOXJ3 is not, however, an obligate activator. In *Xenopus* embryos, Foxj3 overexpression repressed Activin/Nodal- and BMP4-responsive transcription, and knockdown increased Nodal responses. This repression required the E3 ligase RNF152 and was overridden by β-catenin [yoon-2025-foxj3-xenopus-tgfb-abstract]. In zebrafish, Foxj3 represses GABA_A receptor subunit promoters. The telomere-associated protein Terfa, the zebrafish TERF2 orthologue, binds Foxj3 physically and dampens this repression [he-2026-terfa-foxj3-zebrafish-abstract]. In U2OS cells, an extracellular-matrix gene cluster rose after FOXJ3 knockdown, which is consistent with repression of some targets [grant-2012-forkhead-cellcycle-fulltext]. Whether FOXJ3 activates or represses a gene therefore appears to depend on its partner proteins and on chromatin context.

## 4. Subcellular localization

FOXJ3 acts in the nucleus. Gal4–Foxj3 fusion proteins, both full-length and truncated, are also nuclear when overexpressed in C2C12 cells [alexander-2010-foxj3-mef2c-fulltext]. The donkey entry assigns nuclear localization by automatic rule from the forkhead domain [uniprot-A0A9L0JKH1-entry], and experiments support this in the orthologues. In the embryonic mouse cortex, FOXJ3 was localized to the nuclei of cells in both the ventricular zone and the cortical plate. In cultured cortical neurons, mCherry-tagged wild-type FOXJ3 and the N351S variant were both mainly nuclear. The variant's loss of function is therefore not caused by mistargeting [cheng-2026-foxj3-epilepsy-fulltext]. The ChIP-seq evidence above places FOXJ3 on chromatin at promoters and enhancers [chen-2016-forkhead-binding-fulltext; cheng-2026-foxj3-epilepsy-fulltext]. I found no evidence of cytoplasmic, ciliary or extracellular roles. Unlike its paralogue FOXJ1, FOXJ3 has not been linked to ciliogenesis.

## 5. Biological roles and pathways in vertebrates

**Skeletal muscle fibre type and regeneration.** *Foxj3* is expressed in myotomes and the developing body-wall musculature during mouse embryogenesis [landgren-2004-foxj3-expression-abstract] and in adult muscle. *Foxj3* mutant mice are viable but have significantly fewer type I slow-twitch fibres, weaker contractile function and impaired regeneration after severe injury. Their myogenic progenitors show perturbed cell-cycle kinetics and lower *Mef2c* expression [alexander-2010-foxj3-mef2c-abstract]. Both the slow soleus and the fast extensor digitorum longus muscles shifted from type I toward type IIa/b fibres, while satellite-cell numbers were normal. The authors note that their β-geo targeted allele may still produce a truncated protein, so the phenotype could underestimate the effect of complete loss [alexander-2010-foxj3-mef2c-fulltext]. Conditional deletion of *Mef2c* itself also reduces type I fibres, which supports MEF2C as the effector [alexander-2010-foxj3-mef2c-fulltext]. The best-supported pathway in muscle is therefore direct activation of the *Mef2c* enhancer by FOXJ3, with MEF2C in turn sustaining the slow oxidative fibre programme. FOXJ3 also sits within a microRNA-regulated module that controls mitochondrial biogenesis. miR-494 and miR-27b both target the *Foxj3* 3′ UTR, and both fall during myogenic differentiation and after endurance exercise, which releases Foxj3 [yamamoto-2012-mir494-foxj3-abstract; shen-2016-mir27b-mitochondria-abstract]. When miR-27b suppresses Foxj3, its downstream targets Mef2c, PGC-1α, NRF1 and mtTFA fall, and so does mitochondrial content [shen-2016-mir27b-mitochondria-abstract]. Colorectal cancer cells show a similar miR-27a/FOXJ3 axis, which lowers mitochondrial biogenesis and respiration and alters mitochondrial dynamics [barisciano-2021-mir27a-foxj3-abstract].

**Adaptive thermogenesis.** Cold exposure and β-adrenergic agonists induce *Foxj3* in brown and beige fat. Deleting *Foxj3* specifically in adipose tissue whitened brown fat, blocked browning of inguinal white fat, and caused obesity, raised fasting glucose and hepatic steatosis. In primary brown adipocytes the effect was cell-autonomous. Mechanistically, Foxj3 stimulated PGC-1α and UCP1 expression [huang-2024-foxj3-thermogenesis-abstract]. Together with the muscle data, this places FOXJ3 upstream of the PGC-1α-centred oxidative and mitochondrial programme in several tissues.

**Spermatogenesis.** FOXJ3 is highly expressed in mouse spermatogonia and meiotic spermatocytes. Deleting it in spermatogonia (Mvh-Cre) caused Sertoli-cell-only testes: spermatogonia were lost by postnatal day 4 and accumulated DNA double-strand breaks. Deleting it in spermatocytes (Stra8-Cre) caused meiotic arrest and reduced transcripts of meiotic recombination and repair genes, including *Rad51*, *Dmc1*, *Brca1*, *Brca2*, *Hormad1* and *Rnf212*. Both models were completely sterile [ni-2016-foxj3-spermatogenesis-abstract]. UniProt transfers these functions to human FOXJ3 by similarity [uniprot-Q9UPW0-entry]. They are among the strongest in vivo phenotypes reported. Livestock genetics suggests the reproductive role is conserved beyond rodents. In an exome-sequencing study of artificial-insemination bulls with divergent fertility, the most strongly associated variant after validation was a synonymous SNP in *FOXJ3* (rs109065788, on bovine chromosome 3), with a 21% allele-frequency difference between high- and low-fertility bulls [whiston-2017-bull-fertility-foxj3-fulltext]. Because this variant is synonymous and the evidence is only associative, it marks the locus rather than proving a mechanism. Even so, it is the closest evidence available from a large domestic ungulate that FOXJ3 contributes to male fertility, which bears directly on the donkey orthologue.

**Cortical development and the PTEN–mTOR pathway.** The most mechanistically detailed recent study links FOXJ3 to focal cortical dysplasia (FCD) and autosomal-dominant focal epilepsy in humans. In mouse cortex, FOXJ3 levels in neural progenitors fall sharply after embryonic day 15.5. Knocking it down in utero impaired neuronal migration and lamination and shifted fate toward upper-layer neurons at the expense of deep-layer neurons. FOXJ3 directly binds and activates *Pten*; without it, PTEN falls, mTOR becomes hyperactive (increased phospho-S6) and neuronal somata enlarge, a hallmark of FCD. Overexpressing *Pten* rescued the cortical defects. The patient variant p.N351S stayed nuclear but could not activate *Pten* [cheng-2026-foxj3-epilepsy-fulltext]. An accompanying commentary presents this as a transcriptional input upstream of PTEN–mTOR in epilepsy [bedrosian-2026-outfoxed-fulltext]. FOXJ3 therefore acts as a brake on PI3K–AKT–mTOR signalling by sustaining expression of the phosphatase PTEN. Its earlier-described expression in neuroectoderm and neural crest derivatives fits this role [landgren-2004-foxj3-expression-abstract].

**Cell-cycle control.** FOXJ3 was one of three Forkhead factors (with FOXM1 and FOXK1) needed for periodic expression of a G2/M Forkhead-site reporter and the *PLK1* promoter in synchronized human cells. Knocking it down caused G1 accumulation and slower proliferation, and FOXJ3-dependent genes included a notable cluster of zinc-finger proteins [grant-2012-forkhead-cellcycle-fulltext]. The cell-cycle defects in *Foxj3*-mutant myogenic progenitors [alexander-2010-foxj3-mef2c-abstract] and the loss of spermatogonia [ni-2016-foxj3-spermatogenesis-abstract] may reflect this broader proliferative role.

## 6. Other reported associations (lower-confidence and context-specific)

Many cell-line studies, mostly in cancer, report FOXJ3 as a target of microRNAs or as a modulator of oncogenic signalling. The direction of its effect varies by tumour type. It is described as pro-tumorigenic in breast cancer, where it regulates *Snail* [seo-2023-foxj3-snail-breast-abstract], and in hepatocellular carcinoma, where it is associated with FoxO6 [li-2025-foxj3-foxo6-hcc-abstract]. It is described as tumour-suppressive in neuroblastoma, where it inhibits AKT signalling [challagundla-2025-foxj3-neuroblastoma-abstract], and in a SOX2-driven hepatocellular carcinoma model, where it attenuates PI3K/AKT signalling and autophagy [zhang-2026-sox2-foxj3-hcc-abstract]. Several of these tumour-suppressive effects again converge on PI3K–AKT, consistent with the PTEN mechanism above. MicroRNAs reported to repress FOXJ3 include miR-517a-3p in lung cancer [jin-2014-mir517a-foxj3-abstract] and SOX2-induced miR-425-5p in glioblastoma stem cells [delarocha-2020-mir425-foxj3-abstract]. In bone, FOXJ3 promoted osteogenic differentiation of mesenchymal stem cells through Wnt/β-catenin [xiao-2026-foxj3-osteogenesis-abstract]. It was also recruited by an enhancer RNA to activate *RGS1* transcription during osteoclastogenesis in inflammatory arthritis [yuan-2025-rgs1-foxj3-osteoclast-abstract]. Genetic association studies link FOXJ3 polymorphisms with rheumatoid arthritis [ban-2013-foxj3-ra-abstract] and with white-blood-cell count and basophil percentage in Holstein cattle [liu-2026-cattle-leukocyte-gwas-abstract], and a non-canonical RET::FOXJ3 fusion has been reported in lung adenocarcinoma [wang-2026-ret-foxj3-fusion-abstract]. These reports mostly rely on knockdown or overexpression in transformed cells and seldom show direct binding to targets. They should be weighted below the genetic studies in mice and humans.

## 7. Implications for functional annotation of donkey FOXJ3

The donkey protein is nearly identical to human FOXJ3, has an identical forkhead domain, and conserves the residue whose mutation causes loss of function in human patients. Annotating it by orthology is therefore well justified. Its molecular function is best described as sequence-specific DNA-binding transcription factor activity specific to RNA polymerase II, acting mainly as an activator. This rests on enhancer-binding, mutagenesis, Gal4-fusion and ChIP-seq evidence from orthologues [alexander-2010-foxj3-mef2c-fulltext; chen-2016-forkhead-binding-fulltext; cheng-2026-foxj3-epilepsy-fulltext]. Its cellular component is the nucleus, specifically chromatin at active promoters and enhancers [cheng-2026-foxj3-epilepsy-fulltext; uniprot-A0A9L0JKH1-entry].

The biological processes with the strongest support are those backed by in vivo loss-of-function genetics. These are spermatogenesis, including spermatogonial survival and male meiosis [ni-2016-foxj3-spermatogenesis-abstract]; skeletal-muscle fibre-type specification and regeneration through *Mef2c* [alexander-2010-foxj3-mef2c-fulltext]; brown-fat thermogenesis through PGC-1α and UCP1 [huang-2024-foxj3-thermogenesis-abstract]; and neuronal migration and laminar fate specification in the cerebral cortex through PTEN–mTOR [cheng-2026-foxj3-epilepsy-fulltext]. The pathway roles are best stated in terms of the identified targets: an activator of *Mef2c* in the muscle oxidative programme, an inducer of PGC-1α upstream of mitochondrial biogenesis, and an inducer of *Pten* that restrains PI3K–AKT–mTOR signalling. Lower-confidence annotations, such as negative regulation of TGF-β/Nodal-responsive transcription, come from single morpholino studies in non-mammalian embryos [yoon-2025-foxj3-xenopus-tgfb-abstract] and should be treated as provisional. Equids are bred for athletic, oxidative muscle and for male fertility. The FOXJ3–MEF2C–PGC-1α axis and the bovine fertility association [whiston-2017-bull-fertility-foxj3-fulltext] make *FOXJ3* a plausible but untested candidate locus for these traits in donkeys and horses.

## Open Questions

Several questions remain open. No study has examined FOXJ3 in any equid. Its expression atlas in donkey tissues (testis, skeletal muscle, brown fat, brain), its gene structure, and whether the shorter 580-residue Ensembl model is a real isoform or a prediction artefact could all be resolved with donkey RNA-seq and long-read transcript data. At the molecular level, it is not known which parts of the long disordered region carry FOXJ3's activation and repression activities. Its main cofactors are also unidentified. Candidates from the literature include RNF152 and β-catenin [yoon-2025-foxj3-xenopus-tgfb-abstract], TERF2 [he-2026-terfa-foxj3-zebrafish-abstract] and NEK6, an interaction recorded in IntAct [uniprot-Q9UPW0-entry]. It is also unclear why the N351S substitution, which lies outside the DNA-binding domain, abolishes *Pten* activation. A structure of the FOXJ3 forkhead domain bound to DNA, compared with FOXK2 and FOXO3, would explain its relaxed motif specificity [chen-2016-forkhead-binding-fulltext]. Physiologically, it would be useful to know whether FOXJ3 genotype or expression varies with muscle fibre composition or fertility in equids, and whether the miR-494/miR-27 regulatory module [yamamoto-2012-mir494-foxj3-abstract; shen-2016-mir27b-mitochondria-abstract] is conserved in exercising horse and donkey muscle. Finally, the opposite tumour-related roles reported in different cancers need reconciling with the cleaner PTEN-activating mechanism.

## References

- **alexander-2010-foxj3-mef2c**: Alexander MS, Shi X, Voelker KA, Grange RW, Garcia JA, Hammer RE, Garry DJ. Foxj3 transcriptionally activates Mef2c and regulates adult skeletal muscle fiber type identity. *Dev Biol* (2010). PMID: 19914232; DOI: 10.1016/j.ydbio.2009.11.015; PMCID: PMC4540073.
- **ban-2013-foxj3-ra**: Ban JY, Park HJ, Kim SK, Kim JW, Lee YA, Choi IA, Chung JH, Hong SJ. Association of forkhead box J3 (FOXJ3) polymorphisms with rheumatoid arthritis. *Mol Med Rep* (2013). PMID: 23933633; DOI: 10.3892/mmr.2013.1623.
- **barisciano-2021-mir27a-foxj3**: Barisciano G, Leo M, Muccillo L, Pranzini E, Parri M, Colantuoni V, Taddei ML, Sabatino L. The miR-27a/FOXJ3 Axis Dysregulates Mitochondrial Homeostasis in Colorectal Cancer Cells. *Cancers* (2021). PMID: 34638478; DOI: 10.3390/cancers13194994; PMCID: PMC8507763.
- **bedrosian-2026-outfoxed**: Bedrosian TA. OutFOXed: FOXJ3 Variants Disrupt PTEN-mTOR Signaling in Focal Epilepsy. *Epilepsy Curr* (2026). PMID: 42226735; DOI: 10.1177/15357597261455996; PMCID: PMC13222211.
- **challagundla-2025-foxj3-neuroblastoma**: Challagundla KB, Pathania AS, Chava H, Kantem NM, Dronadula VM, Coulter DW, Clarke M. FOXJ3, a novel tumor suppressor in neuroblastoma. *Mol Ther Oncol* (2025). PMID: 39811681; DOI: 10.1016/j.omton.2024.200914; PMCID: PMC11731479.
- **chen-2016-forkhead-binding**: Chen X, Ji Z, Webber A, Sharrocks AD. Genome-wide binding studies reveal DNA binding specificity mechanisms and functional interplay amongst Forkhead transcription factors. *Nucleic Acids Res* (2016). PMID: 26578569; DOI: 10.1093/nar/gkv1120; PMCID: PMC4770209.
- **cheng-2026-foxj3-epilepsy**: Cheng HY, Liu C, Nien CW, et al. (Tsai JW, senior). Epilepsy-associated FOXJ3 variants link a transcriptional program of the PTEN-mTOR pathway to neuronal specification and cortical lamination. *Nat Commun* (2026). PMID: 41803108; DOI: 10.1038/s41467-026-69241-2; PMCID: PMC12972129.
- **delarocha-2020-mir425-foxj3**: de la Rocha AMA, González-Huarriz M, Guruceaga E, et al. miR-425-5p, a SOX2 target, regulates the expression of FOXJ3 and RAB31 and promotes the survival of GSCs. *Arch Clin Biomed Res* (2020). PMID: 32905473; DOI: 10.26502/acbr.50170100; PMCID: PMC7470213.
- **grant-2012-forkhead-cellcycle**: Grant GD, Gamsby J, Martyanov V, Brooks L, George LK, Mahoney JM, Loros JJ, Dunlap JC, Whitfield ML. Live-cell monitoring of periodic gene expression in synchronous human cells identifies Forkhead genes involved in cell cycle control. *Mol Biol Cell* (2012). PMID: 22740631; DOI: 10.1091/mbc.E11-02-0170; PMCID: PMC3418304.
- **he-2026-terfa-foxj3-zebrafish**: He J, Song Z, Zhang J, et al. Terfa Safeguards GABAergic Inhibition and Neuronal Excitability in Zebrafish Through a Foxj3-Linked Transcriptional Mechanism. *Neurosci Bull* (2026). PMID: 42799824; DOI: 10.1007/s12264-026-01714-2.
- **huang-2024-foxj3-thermogenesis**: Huang J, Zhang Y, Zhou X, et al. Foxj3 Regulates Thermogenesis of Brown and Beige Fat Via Induction of PGC-1α. *Diabetes* (2024). PMID: 37939221; DOI: 10.2337/db23-0454.
- **jin-2014-mir517a-foxj3**: Jin J, Zhou S, Li C, Xu R, Zu L, You J, Zhang B. MiR-517a-3p accelerates lung cancer cell proliferation and invasion through inhibiting FOXJ3 expression. *Life Sci* (2014). PMID: 24846831; DOI: 10.1016/j.lfs.2014.05.006.
- **katoh-2004-fox-family**: Katoh M, Katoh M. Human FOX gene family (Review). *Int J Oncol* (2004). PMID: 15492844.
- **landgren-2004-foxj3-expression**: Landgren H, Carlsson P. FoxJ3, a novel mammalian forkhead gene expressed in neuroectoderm, neural crest, and myotome. *Dev Dyn* (2004). PMID: 15366017; DOI: 10.1002/dvdy.20131.
- **li-2025-foxj3-foxo6-hcc**: Li W, Wang J, Chen P, Zhao L, Niu J, Liu J, Liu N. Targeting the FoxJ3/FoxO6 axis suppresses hepatocellular carcinoma growth by inducing cell cycle arrest and apoptosis. *Am J Transl Res* (2025). PMID: 41268239; DOI: 10.62347/PVIG8848; PMCID: PMC12628247.
- **liu-2026-cattle-leukocyte-gwas**: Liu C, Yu J, Zhong Z, et al. Genome-Wide Association Study of Leukocyte Traits Reveals Candidate Genes Associated With Immunity in Holstein Cattle From Southern China. *Vet Med Sci* (2026). PMID: 41729176; DOI: 10.1002/vms3.70858; PMCID: PMC12927994.
- **ni-2016-foxj3-spermatogenesis**: Ni L, Xie H, Tan L. Multiple roles of FOXJ3 in spermatogenesis: A lesson from Foxj3 conditional knockout mouse models. *Mol Reprod Dev* (2016). PMID: 27739607; DOI: 10.1002/mrd.22750.
- **seo-2023-foxj3-snail-breast**: Seo Y, Lee J, Kim J, Shim S, Jang SW. FOXJ3 Regulates Cell Proliferation and Motility Through Modulating Snail Expression in Breast Cancer Cells. *Anticancer Res* (2023). PMID: 37351974; DOI: 10.21873/anticanres.16470.
- **shen-2016-mir27b-mitochondria**: Shen L, Chen L, Zhang S, et al. MicroRNA-27b Regulates Mitochondria Biogenesis in Myocytes. *PLoS One* (2016). PMID: 26849429; DOI: 10.1371/journal.pone.0148532; PMCID: PMC4746119.
- **uniprot-A0A9L0JKH1**: UniProtKB/TrEMBL entry A0A9L0JKH1 (FOXJ3, *Equus asinus*), entry version 14. https://rest.uniprot.org/uniprotkb/A0A9L0JKH1.txt
- **uniprot-Q9UPW0**: UniProtKB/Swiss-Prot entry Q9UPW0 (FOXJ3_HUMAN). https://rest.uniprot.org/uniprotkb/Q9UPW0.txt
- **wang-2020-donkey-genomes**: Wang C, Li H, Guo Y, et al. Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun* (2020). PMID: 33293529; DOI: 10.1038/s41467-020-19813-7; PMCID: PMC7723042.
- **wang-2026-ret-foxj3-fusion**: Wang P, Tang HXL, Song J, Yang Y, Yao Y, Xia L. Identification of a novel RET::FOXJ3 fusion in lung adenocarcinoma associated with lack of response to pralsetinib. *Cancer Lett* (2026). PMID: 41202951; DOI: 10.1016/j.canlet.2025.218100.
- **whiston-2017-bull-fertility-foxj3**: Whiston R, Finlay EK, McCabe MS, et al. (Meade KG, senior). A dual targeted β-defensin and exome sequencing approach to identify, validate and functionally characterise genes associated with bull fertility. *Sci Rep* (2017). PMID: 28947819; DOI: 10.1038/s41598-017-12498-x; PMCID: PMC5613009.
- **xiao-2026-foxj3-osteogenesis**: Xiao H, Li J, Huang W, Qin Y. FOXJ3 drives mesenchymal stem cell osteogenic differentiation via the Wnt/β-catenin pathway. *Mol Med Rep* (2026). PMID: 41268592; DOI: 10.3892/mmr.2025.13760; PMCID: PMC12676519.
- **yamamoto-2012-mir494-foxj3**: Yamamoto H, Morino K, Nishio Y, Ugi S, Yoshizaki T, Kashiwagi A, Maegawa H. MicroRNA-494 regulates mitochondrial biogenesis in skeletal muscle through mitochondrial transcription factor A and Forkhead box j3. *Am J Physiol Endocrinol Metab* (2012). PMID: 23047984; DOI: 10.1152/ajpendo.00097.2012.
- **yoon-2025-foxj3-xenopus-tgfb**: Yoon GH, Kim MS, Choi SC. Foxj3 represses TGF-β signals-responsive transcriptions in Xenopus early development. *Genes Genomics* (2025). PMID: 40522413; DOI: 10.1007/s13258-025-01654-7.
- **yuan-2025-rgs1-foxj3-osteoclast**: Yuan L, Jiang N, Li Y, Wang X, Wang W. RGS1 Enhancer RNA Promotes Gene Transcription by Recruiting Transcription Factor FOXJ3 and Facilitates Osteoclastogenesis. *Inflammation* (2025). PMID: 38904871; DOI: 10.1007/s10753-024-02067-6.
- **zhang-2026-sox2-foxj3-hcc**: Zhang Z, Ren W. SOX2 promotes the progression of hepatocellular carcinoma by targeting FOXJ3 and activating the PI3K/AKT pathway. *CytoJournal* (2026). PMID: 42291103; DOI: 10.25259/Cytojournal_164_2025; PMCID: PMC13255168.


## Citations

1. alexander-2010-foxj3-mef2c-abstract.md
2. alexander-2010-foxj3-mef2c-fulltext.txt
3. alexander-2010-foxj3-mef2c-fulltext.xml
4. alexander-2010-foxj3-mef2c-summary.md
5. ban-2013-foxj3-ra-abstract.md
6. ban-2013-foxj3-ra-summary.md
7. barisciano-2021-mir27a-foxj3-abstract.md
8. barisciano-2021-mir27a-foxj3-fulltext.txt
9. barisciano-2021-mir27a-foxj3-fulltext.xml
10. barisciano-2021-mir27a-foxj3-summary.md
11. bedrosian-2026-outfoxed-abstract.md
12. bedrosian-2026-outfoxed-fulltext.txt
13. bedrosian-2026-outfoxed-fulltext.xml
14. bedrosian-2026-outfoxed-summary.md
15. challagundla-2025-foxj3-neuroblastoma-abstract.md
16. challagundla-2025-foxj3-neuroblastoma-summary.md
17. chen-2016-forkhead-binding-abstract.md
18. chen-2016-forkhead-binding-fulltext.txt
19. chen-2016-forkhead-binding-fulltext.xml
20. chen-2016-forkhead-binding-summary.md
21. cheng-2026-foxj3-epilepsy-abstract.md
22. cheng-2026-foxj3-epilepsy-fulltext.txt
23. cheng-2026-foxj3-epilepsy-fulltext.xml
24. cheng-2026-foxj3-epilepsy-summary.md
25. delarocha-2020-mir425-foxj3-abstract.md
26. delarocha-2020-mir425-foxj3-summary.md
27. grant-2012-forkhead-cellcycle-abstract.md
28. grant-2012-forkhead-cellcycle-fulltext.txt
29. grant-2012-forkhead-cellcycle-fulltext.xml
30. grant-2012-forkhead-cellcycle-summary.md
31. he-2026-terfa-foxj3-zebrafish-abstract.md
32. he-2026-terfa-foxj3-zebrafish-summary.md
33. huang-2024-foxj3-thermogenesis-abstract.md
34. huang-2024-foxj3-thermogenesis-summary.md
35. jin-2014-mir517a-foxj3-abstract.md
36. jin-2014-mir517a-foxj3-summary.md
37. katoh-2004-fox-family-abstract.md
38. katoh-2004-fox-family-summary.md
39. landgren-2004-foxj3-expression-abstract.md
40. landgren-2004-foxj3-expression-summary.md
41. li-2025-foxj3-foxo6-hcc-abstract.md
42. li-2025-foxj3-foxo6-hcc-summary.md
43. liu-2026-cattle-leukocyte-gwas-abstract.md
44. liu-2026-cattle-leukocyte-gwas-summary.md
45. ni-2016-foxj3-spermatogenesis-abstract.md
46. ni-2016-foxj3-spermatogenesis-summary.md
47. seo-2023-foxj3-snail-breast-abstract.md
48. seo-2023-foxj3-snail-breast-summary.md
49. shen-2016-mir27b-mitochondria-abstract.md
50. shen-2016-mir27b-mitochondria-fulltext.txt
51. shen-2016-mir27b-mitochondria-fulltext.xml
52. shen-2016-mir27b-mitochondria-summary.md
53. uniprot-A0A9L0JKH1-entry.txt
54. uniprot-A0A9L0JKH1-summary.md
55. uniprot-Q9UPW0-entry.txt
56. uniprot-Q9UPW0-summary.md
57. wang-2020-donkey-genomes-abstract.md
58. wang-2020-donkey-genomes-summary.md
59. wang-2026-ret-foxj3-fusion-abstract.md
60. wang-2026-ret-foxj3-fusion-summary.md
61. whiston-2017-bull-fertility-foxj3-abstract.md
62. whiston-2017-bull-fertility-foxj3-fulltext.txt
63. whiston-2017-bull-fertility-foxj3-fulltext.xml
64. whiston-2017-bull-fertility-foxj3-summary.md
65. xiao-2026-foxj3-osteogenesis-abstract.md
66. xiao-2026-foxj3-osteogenesis-summary.md
67. yamamoto-2012-mir494-foxj3-abstract.md
68. yamamoto-2012-mir494-foxj3-summary.md
69. yoon-2025-foxj3-xenopus-tgfb-abstract.md
70. yoon-2025-foxj3-xenopus-tgfb-summary.md
71. yuan-2025-rgs1-foxj3-osteoclast-abstract.md
72. yuan-2025-rgs1-foxj3-osteoclast-summary.md
73. zhang-2026-sox2-foxj3-hcc-abstract.md
74. zhang-2026-sox2-foxj3-hcc-summary.md