---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:15:13.282297'
end_time: '2026-10-26T00:27:53.104603'
duration_seconds: 759.82
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: MITF
  gene_symbol: MITF
  uniprot_accession: A0A9L0JBN5
  protein_description: 'SubName: Full=Melanocyte inducing transcription factor {ECO:0000313|Ensembl:ENSEASP00005046635.1};'
  gene_info: Name=MITF {ECO:0000313|Ensembl:ENSEASP00005046635.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the MiT/TFE family.
  protein_domains: bHLH_dom. (IPR011598); HLH_DNA-bd_sf. (IPR036638); MiT/TFE_C. (IPR021802);
    MiT/TFE_N. (IPR031867); DUF3371 (PF11851)
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
citation_count: 100
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JBN5
- **Protein Description:** SubName: Full=Melanocyte inducing transcription factor {ECO:0000313|Ensembl:ENSEASP00005046635.1};
- **Gene Information:** Name=MITF {ECO:0000313|Ensembl:ENSEASP00005046635.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the MiT/TFE family.
- **Key Domains:** bHLH_dom. (IPR011598); HLH_DNA-bd_sf. (IPR036638); MiT/TFE_C. (IPR021802); MiT/TFE_N. (IPR031867); DUF3371 (PF11851)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "MITF" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'MITF' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **MITF** (gene ID: MITF, UniProt: A0A9L0JBN5) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# MITF (Melanocyte inducing transcription factor) in the donkey, *Equus asinus* (UniProt A0A9L0JBN5)

## 1. Introduction and summary

UniProt A0A9L0JBN5 is the donkey orthologue of MITF (microphthalmia-associated, or melanocyte inducing, transcription factor). MITF is a basic helix-loop-helix leucine zipper (bHLH-LZ) transcription factor in the MiT/TFE family, alongside TFEB, TFE3 and TFEC. Its main job is to bind DNA, as a homodimer or as a heterodimer with another MiT/TFE member, at E-box (CACGTG) and M-box (TCATGTG) elements in the regulatory regions of its target genes and to activate their transcription by RNA polymerase II [hemesath-1994-mitf-tyrosinase-abstract; aksan-1998-mitf-ebox-targeting-abstract; steingrimsson-2004-melanocytes-mitf-abstract]. MITF is best known as the lineage master regulator of melanocytes. It is needed for melanocytes to develop and survive, and it drives the pigmentation enzymes tyrosinase, TYRP1 and DCT, so it links signals from MC1R/cAMP and KIT to melanin synthesis [levy-2006-mitf-master-regulator-abstract; goding-2019-mitf-first-25-years-fulltext]. Outside melanocytes, MITF also controls the development of the retinal pigment epithelium (RPE), mast cells and osteoclasts, and its non-melanocyte isoforms help regulate lysosome and endolysosome biogenesis [hodgkinson-1993-mi-bhlhzip-abstract; martina-2014-mitf-tfe-organelle-review-abstract; ploper-2015-mitf-endolysosome-wnt-abstract]. Where the protein sits in the cell is tightly regulated. Its site of action is the nucleus. Isoforms that carry the TFEB-like N-terminal region can be held in the cytoplasm and recruited to the lysosomal surface by Rag GTPases, where mTORC1 phosphorylates them [martina-2013-rag-tfeb-mitf-lysosome-fulltext; rocznikferguson-2012-tfeb-mtorc1-abstract].

No experimental study of MITF in the donkey has been published. A0A9L0JBN5 is an unreviewed TrEMBL entry. Ensembl predicted it computationally from the chromosome-level Dezhou donkey genome [uniprot-A0A9L0JBN5-entry; wang-2020-donkey-genomes-abstract], and a recent review of equid coat-colour genetics discusses MITF only in horses [liu-2024-equine-coloration-review-fulltext]. The functional description below therefore rests on three lines of evidence: (i) the near-identity of the donkey sequence to human MITF, including every characterised regulatory residue (my own alignment, `notes_residue_mapping.txt`); (ii) extensive mechanistic work in mouse, human and cell systems; and (iii) in vivo genetics in the domestic horse (*Equus caballus*), a congener of the donkey. In horses, loss-of-function MITF alleles cause "splashed white" depigmentation and deafness, which mirrors human Waardenburg syndrome type 2A [hauswirth-2012-mitf-pax3-splashed-white-fulltext; henkel-2019-mitf-deletion-horse-deafness-abstract; magdesian-2020-mitf-deletion-paint-horse-fulltext; bellone-2023-mitf-structural-variant-thoroughbred-abstract].

## 2. Identity verification and sequence features of the donkey protein

The gene symbol is not ambiguous here. The UniProt record names the gene MITF, describes the protein as "Melanocyte inducing transcription factor", and places it in the MiT/TFE family. It carries the bHLH domain (PROSITE PS50888, residues 395–448), the MiT/TFE N-terminal (IPR031867) and C-terminal (IPR021802/DUF3371) regions, and two coiled-coil segments, one of which (441–482) is the leucine zipper [uniprot-A0A9L0JBN5-entry]. The gene lies on donkey chromosome 21 of the reference proteome UP000694387. In horses MITF maps to ECA16 [liu-2024-equine-coloration-review-fulltext; henkel-2019-mitf-deletion-horse-deafness-abstract], and the difference reflects the different chromosome numbering of the two species' assemblies. The entry has protein-existence level 3 (inferred from homology), and all of its GO terms (nucleus, cytoplasm, RNA polymerase II-specific DNA-binding transcription factor activity, protein dimerization, melanocyte differentiation) are electronic inferences [uniprot-A0A9L0JBN5-entry].

I made a global pairwise alignment (BLOSUM62) of the 610-residue donkey model against reviewed human MITF-A (O75030-1, 526 residues) [uniprot-O75030-human-MITF-entry]. It gave 487 identical positions and 8 substitutions across the aligned region, about 98% identity (`notes_residue_mapping.txt`). The whole bHLH-LZ block (donkey 389–482, human 305–398) is identical. The donkey model differs from human MITF-A in three ways. First, it has a 115-residue N-terminal extension, rich in proline, arginine and glycine, upstream of the conserved "MQSESGIVPDF" start of MITF-A. No human isoform has an equivalent sequence. Second, it lacks 24 residues that correspond to human 139–162 (QVKQYLSTTLANKHANQVLSLPCPN, a region shared with MITF-M). Third, it lacks the six-residue ACIFPT segment (human 294–299) just upstream of the basic region. The third difference matches a known alternative splice: in humans, the A2, B2, C2, H2 and M2 isoforms also lack this hexapeptide [uniprot-O75030-human-MITF-entry]. Hemesath and colleagues showed early on that an alternatively spliced exon outside the bHLH-ZIP region modulates DNA recognition by the basic domain [hemesath-1994-mitf-tyrosinase-abstract]. Neither the N-terminal extension nor the 24-residue gap appears in any annotated human isoform, so I examined both further by comparing all equid MITF entries in UniProt (`notes_equid_isoforms.txt`). The extension is not unique to this entry. It is present, almost identically, in a second donkey model from another assembly (A0A8C4PGB1, 641 residues) and in the Ensembl horse model A0A5F5PRV7 (635 residues) [uniprot-A0A5F5PRV7-entry]. It also has a clear counterpart in human. In the human MITF-A RefSeq mRNA (NM_198159.3), the CDS starts at nucleotide 135 with MQSESG..., and the 5′ untranslated region upstream of it is open in the same reading frame. Translated, it gives "...LGGPRPSYLPSAPGLCSHFPAVEGREAGA", homologous to the end of the equid extension ("LGGPRPDHLPSAPGLCSHFPAIEGREAGA") [ncbi-NM_198159-human-MITF-A-mRNA]. The extension is therefore most likely an Ensembl gene-model artefact: in the equid genomes the open frame is extended to an upstream methionine, while in the human transcript this conserved sequence is treated as untranslated leader. Equally, it could be an unrecognised N-terminally extended isoform that starts at an upstream AUG (or non-AUG) codon. No protein-level evidence supports either view. The 24-residue gap, by contrast, is seen only in A0A9L0JBN5. Every other donkey model (MITF-M, H-type, C-type and the alternative-assembly A-type) contains the QVKQYLSTTL... segment, as do the horse model and an experimentally cloned horse MITF-M cDNA [uniprot-K4FCY0-entry]. The gap therefore probably reflects a rare or mis-predicted splice junction, not the typical donkey protein. Overall, the A0A9L0JBN5 sequence is best read as one predicted isoform of an MITF-A-type transcript ("A2-like"). It should not be taken as the definitive or melanocyte-specific (MITF-M) donkey protein.

Every characterised regulatory site is conserved in the donkey model (human MITF-A numbering → MITF-M numbering → donkey position, from my alignment). These are the phospho-degron serine S5 of MITF-A, which is phosphorylated when nutrients are present and is recognised by β-TrCP (→ donkey S120) [nardone-2023-tfe3-mitf-stability-fulltext]; the ERK site S180/S73 (→ S270) [wu-2000-kit-dual-phosphorylation-abstract]; the 14-3-3/mTORC1 site S280/S173 (→ S370) [bronisz-2006-mitf-14-3-3-abstract; goding-2019-mitf-first-25-years-fulltext]; the SUMO acceptors K289/K182 (→ K379) and K423/K316 (→ K507), together with the glutamate of the ψKxE motif, E425/E318 (→ E509) [murakami-2005-mitf-sumoylation-abstract; bertolotto-2011-mitf-e318k-abstract]; the GSK3 site S405/S298, which is mutated in Waardenburg syndrome type 2 (→ S489) [takeda-2000-mitf-ser298-gsk3-abstract]; the RSK site S516/S409 (→ S600) [wu-2000-kit-dual-phosphorylation-abstract]; and the M-box-contacting I319/I212 (→ I403) [pogenberg-2012-mitf-structure-abstract]. The Rag-binding motif that Martina and Puertollano mapped in MITF isoform 1 (S55/R56, within "SRILLRQQLM") is present at donkey residues 170–179 [martina-2013-rag-tfeb-mitf-lysosome-fulltext]. This degree of conservation is consistent with comparative studies showing that Mitf protein domains are highly conserved across vertebrates [hallsson-2007-mitf-evolution-domains-abstract].

## 3. Gene architecture and isoforms

Like its orthologues, the MITF gene is expected to use several alternative promoters and first exons (1A, 1H, 1B1b, 1C, 1D, 1M and others) spliced onto a common downstream body. This produces isoforms that differ at their N-termini and are expressed in different tissues [goding-2019-mitf-first-25-years-fulltext; hallsson-2007-mitf-evolution-domains-abstract]. MITF-M is driven by the melanocyte-specific promoter. It is the main isoform in neural-crest-derived melanocytes and lacks the long N-terminal region. MITF-A and MITF-H are expressed more widely, including in RPE, osteoclasts and mast cells [martina-2013-rag-tfeb-mitf-lysosome-fulltext]. Mast cells also express a dedicated Mitf-mc isoform, which activates mast-cell but not melanocyte target promoters and can heterodimerise with TFE3 [takemoto-2002-mitf-mast-cell-isoform-abstract]. Mouse genetics shows that the isoforms are partly redundant: in the RPE, loss of exon 1D is compensated by up-regulation of Mitf-H, but other isoforms cannot replace MITF-M in melanocytes [goding-2019-mitf-first-25-years-fulltext]. Horse genetics confirms that the melanocyte promoter matters in equids. The SW1 allele, a 10/11-bp insertion in the proximal MITF-M promoter that disrupts a highly conserved PAX3 binding site, causes splashed white [hauswirth-2012-mitf-pax3-splashed-white-fulltext]. Goding and Arnheiter cite this horse allele as a case where promoter alterations in the major melanocyte isoform cause white spotting [goding-2019-mitf-first-25-years-fulltext]. The donkey reference proteome shows that this isoform architecture is conserved in the donkey. Besides A0A9L0JBN5 (an A-type isoform), the same Ensembl donkey gene (ENSEASG00005002172) gives a 419-residue MITF-M model (A0A9L0JHX8) that starts with the exon-1M peptide MLEMLEYNHY. It also gives an H-type model (A0A9L0IUI7, which starts MEALRVQ...) and a C-type model (A0A9L0KEI8) [uniprot-A0A9L0JHX8-entry; uniprot-A0A9L0JBN5-entry]. The donkey MITF-M model has the same length and N-terminus as a horse MITF-M(+) cDNA (GenBank JN896378, UniProt K4FCY0) that Hauswirth and colleagues cloned in their splashed-white study [uniprot-K4FCY0-entry]. That cDNA gives transcript-level, experimental support for a melanocyte isoform in equids. A0A9L0JBN5 carries the MITF-A-specific N-terminal sequence, so it represents a non-M isoform. Its C-terminal two-thirds, which hold the transactivation, bHLH-LZ and regulatory regions, are shared by all isoforms, MITF-M included.

## 4. Molecular function: DNA recognition, dimerisation and transactivation

MITF was cloned from a transgenic insertional mutation at the mouse *microphthalmia* locus. It turned out to be a new bHLH-ZIP protein, expressed in the developing eye, ear and skin, the tissues affected in *mi* mutants [hodgkinson-1993-mi-bhlhzip-abstract]. Hemesath et al. then showed that it binds DNA either as a homodimer or as a heterodimer with TFEB, TFE3 or TFEC, defining the MiT family, and that it activates transcription through the M box, a highly conserved element in pigmentation gene promoters such as tyrosinase [hemesath-1994-mitf-tyrosinase-abstract]. Steingrímsson and colleagues describe MITF as a member of the Myc supergene family that works through these restricted homo- and heterodimers [steingrimsson-2004-melanocytes-mitf-abstract].

Target specificity comes from DNA sequence recognition beyond the core E-box. Aksan and Goding showed in vitro and in vivo that MITF binds the asymmetric CATGTG E-box only when a 5′ T flanks it (TCATGTG, the M-box), whereas binding to the palindromic CACGTG E-box needs no particular flank. The M-boxes of tyrosinase, TRP-1 (TYRP1), TRP-2 (DCT) and QNR-71 all carry this 5′ T, conserved from human to turtle [aksan-1998-mitf-ebox-targeting-abstract]. Goding and Arnheiter propose keeping the term M-box for CATGTG-core sites, which are frequently associated with differentiation genes. The CACGTG E-box is linked to a much wider set of targets and forms part of the CLEAR element through which TFEB and TFE3 control lysosomal genes [goding-2019-mitf-first-25-years-fulltext].

Crystal structures of the MITF bHLH-LZ, alone and bound to E-box and M-box DNA, explain both selectivity properties at the atomic level [pogenberg-2012-mitf-structure-abstract]. A three-residue shift in the leucine-zipper register kinks one zipper helix. This out-of-register assembly blocks heterodimerisation with MAX and other bHLH-LZ factors, so MITF pairs only within the MiT/TFE family; removing the insertion lets MITF bind MAX. M-box recognition depends on an unusual nonpolar contact made by Ile212 (MITF-M numbering), a residue mutated in mice and humans with Waardenburg syndrome [pogenberg-2012-mitf-structure-abstract]. This residue is conserved in the donkey (I403). Horse genetics independently shows that the DNA-binding region is essential. The de novo N310S substitution in the deaf "macchiato" stallion reduces DNA binding in vitro, and the SW3 frameshift (C280Sfs*20) truncates about half of the protein [hauswirth-2012-mitf-pax3-splashed-white-fulltext]. The SW6 and SW8 structural variants delete exon 9 or the region from intron 7 through exon 9, which encodes the HLH DNA-binding domain [magdesian-2020-mitf-deletion-paint-horse-fulltext; bellone-2023-mitf-structural-variant-thoroughbred-abstract].

Downstream, MITF regulates a broad programme. Pigmentation genes (TYR, TYRP1, DCT and other melanosome components) are its classic targets, but it also controls genes for survival, proliferation, cell-cycle control, invasion, senescence, metabolism and DNA-damage repair [goding-2019-mitf-first-25-years-fulltext; levy-2006-mitf-master-regulator-abstract]. In melanocytes and *Drosophila*, MITF activates all subunits of the V-ATPase, as well as lysosome-biogenesis genes such as the acid ceramidase ASAH1 [goding-2019-mitf-first-25-years-fulltext]. In melanoma cells, MITF expression drives the formation of late endosomes and multivesicular bodies, with more Rab7, LAMP1 and CD63, and this in turn amplifies Wnt signalling [ploper-2015-mitf-endolysosome-wnt-abstract]. Genome-wide studies in melanoma cells place these targets in a chromatin context. Combined ChIP-seq and RNA-seq showed that MITF directly regulates genes needed for DNA replication, repair and mitosis, and that losing MITF causes defective replication, DNA damage and senescence [strub-2011-mitf-replication-mitosis-abstract]. Proteomic analysis of the MITF interactome found the PBAF chromatin-remodelling complex (BRG1, CHD7). MITF and SOX10 recruit BRG1 to MITF-associated regulatory elements at active enhancers, where MITF, SOX10, TFAP2A and YY1 bind between two BRG1-positioned nucleosomes. BRG1 in turn shapes the dynamics of MITF occupancy and is required for melanocyte development in vivo [laurette-2015-mitf-brg1-chromatin-abstract]. MITF therefore acts not as an isolated DNA-binding activator but as a lineage-specific anchor of enhancer complexes that include coactivators and chromatin remodellers.

## 5. Signalling pathways that control MITF

MITF integrates several signalling pathways at two levels: transcription of the MITF gene itself, and post-translational control of the MITF protein. At the transcriptional level, α-MSH binding to MC1R raises cAMP and activates CREB, which binds a CRE (TGACGTCA) in the MITF-M promoter. SOX10 and PAX3 cooperate with CREB, so cAMP signalling induces MITF and, through it, the pigmentation genes [goding-2019-mitf-first-25-years-fulltext; wu-2000-kit-dual-phosphorylation-abstract]. PAX3 is required for melanocyte development and melanocyte stem-cell activation because it controls MITF-M expression, and mutations in either PAX3 or MITF cause Waardenburg syndrome [goding-2019-mitf-first-25-years-fulltext]. The same PAX3–MITF axis operates in equids. In horses, splashed white is caused by PAX3 missense alleles and by an MITF-M promoter insertion that destroys a PAX3 site [hauswirth-2012-mitf-pax3-splashed-white-fulltext]. Upstream components of this pathway also vary among donkey breeds: MC1R and ASIP variants underlie red and black donkey coats, and an ASIP structural variant that raises ASIP expression produces the hypopigmented coat of Hetian gray donkeys, apparently by preventing melanocyte maturation [liu-2024-equine-coloration-review-fulltext; li-2026-donkey-gray-asip-abstract]. Since MITF is the transcriptional output of MC1R–cAMP signalling, it is the expected downstream effector of these donkey alleles. No study has yet measured donkey MITF expression in this setting.

At the protein level, the Steel factor/KIT receptor tyrosine kinase activates MAP kinase, which phosphorylates MITF on a consensus serine and increases its transactivation of the tyrosinase promoter [hemesath-1998-mapk-kit-mitf-abstract]. This explains why *Kit*, *Steel* and *Mitf* mutants share melanocyte and mast-cell phenotypes. KIT signalling actually triggers two phosphorylations: ERK phosphorylates S73 and p90RSK-1 phosphorylates S409 (MITF-M numbering). Together they recruit the p300 coactivator but also target MITF for ubiquitin–proteasome degradation, giving a short burst of activation. An unphosphorylatable double mutant is very stable but transcriptionally inert [wu-2000-kit-dual-phosphorylation-abstract]. ERK phosphorylation of S73 also primes GSK3 phosphorylation of S69, which activates a CRM1-dependent nuclear export signal [goding-2019-mitf-first-25-years-fulltext]. Ngeow and colleagues showed that dual phosphorylation is needed and single phosphorylation is not. GSK3 sits downstream of both PI3K and Wnt signalling, so this hydrophobic export signal lets MITF integrate BRAF/MAPK, PI3K and Wnt inputs to control its flow through the nuclear import–export cycle. Non-melanocyte isoforms such as MITF-A respond poorly to MAPK, and their export is controlled instead by mTOR [ngeow-2018-mitf-nuclear-export-abstract]. This distinction applies directly to A0A9L0JBN5 as an A-type isoform. A second GSK3 site lies downstream of the bHLH-LZ at S298 (MITF-M numbering). Phosphorylation of S298 by GSK3β increases MITF binding to the tyrosinase promoter, and an S298 mutation found in a Waardenburg syndrome type 2 family blocks this phosphorylation and impairs MITF function [takeda-2000-mitf-ser298-gsk3-abstract]. Canonical Wnt signalling stabilises MITF through C-terminal GSK3 sites. MITF-driven multivesicular-body biogenesis then sequesters GSK3 and Axin and boosts Wnt signalling further, a positive-feedback loop [ploper-2015-mitf-endolysosome-wnt-abstract]. SUMO conjugation at K182 and K316 does not affect DNA binding, stability or nuclear localisation, but it restrains synergistic activation of promoters with multiple MITF sites and cooperation with SOX10 on Dct [murakami-2005-mitf-sumoylation-abstract]. The human germline variant E318K disrupts the K316 SUMO motif. It enhances MITF occupancy and transcription of targets such as HIF1A and increases melanoma and renal carcinoma risk more than fivefold [bertolotto-2011-mitf-e318k-abstract]. All of these sites are present in the donkey sequence (Section 2).

## 6. Subcellular localisation: nucleus, cytoplasm and the lysosomal surface

MITF acts in the nucleus, where it binds chromatin. UniProt therefore annotates the donkey protein, by homology, to both nucleus and cytoplasm [uniprot-A0A9L0JBN5-entry]. The reviewed human entry adds the lysosomal membrane, based on experimental evidence [uniprot-O75030-human-MITF-entry]. How MITF is distributed between these compartments depends on isoform and nutrient status. Roczniak-Ferguson et al. found that mTORC1 phosphorylates TFEB at S211, which creates a 14-3-3 binding site and keeps TFEB in the cytoplasm. When lysosomal function is inhibited, TFEB translocates to the nucleus. MITF and TFE3 also localised to lysosomes and accumulated in the nucleus under the same conditions [rocznikferguson-2012-tfeb-mtorc1-abstract]. Martina and Puertollano showed that active Rag GTPase heterodimers bind the N-terminus of TFEB and recruit it to lysosomes for mTORC1 phosphorylation. MITF isoforms with a TFEB-like N-terminal region (isoforms 1 and 7, which include MITF-A) bound Rags, and mutating the conserved S55/R56 pair abolished this binding [martina-2013-rag-tfeb-mitf-lysosome-fulltext]. In fed cells, fewer than 10% of cells had nuclear MITF isoform 1, which was spread diffusely through the cytosol. Inhibiting mTORC1 with Torin-1 moved it into the nucleus in more than 80% of cells and also redistributed it to LAMP1-positive lysosomes [martina-2013-rag-tfeb-mitf-lysosome-fulltext]. MITF-M lacks this N-terminal region, so it is not regulated this way and is mostly nuclear [goding-2019-mitf-first-25-years-fulltext; martina-2013-rag-tfeb-mitf-lysosome-fulltext]. 14-3-3 retention through the S173 site (S280 in MITF-A) was first described in osteoclast precursors. There, phosphorylation-dependent 14-3-3 binding, helped by the kinase C-TAK1 (MARK3), keeps MITF in the cytosol until RANKL/CSF-1 signalling releases it to the nucleus to drive osteoclast genes [bronisz-2006-mitf-14-3-3-abstract]. Nardone and colleagues then showed that nutrients also control MITF-A by regulated proteolysis, not only by sequestration. Amino acids drive Rag-dependent recruitment of TFE3 and MITF-A to the lysosomal surface, where a conserved N-terminal phospho-degron is phosphorylated (S5 in MITF-A). The phosphorylated degron is recognised by CUL1–β-TrCP1/2, which ubiquitinates MITF-A and sends it for proteasomal degradation. This degradative route runs in parallel with 14-3-3 retention via S280 [nardone-2023-tfe3-mitf-stability-fulltext]. The donkey protein contains the MITF-A-type Rag-binding segment and the degron serine (S120, in the conserved MQSESG motif) and the S280/S173-equivalent 14-3-3 site (donkey S370). By homology, it is therefore predicted to shuttle between a cytoplasmic, lysosome-associated pool that mTORC1 restrains under nutrient-replete conditions and an active nuclear pool. In fed cells it would also be continuously degraded via β-TrCP. The predicted 115-residue extension, if it is translated at all (Section 2), would place the degron and the Rag-binding motif internally rather than at the N-terminus. Whether that changes Rag binding or degron recognition is unknown.

## 7. Biological roles in cell lineages, and evidence from equids

Most of what is known about MITF's physiological roles comes from mouse *microphthalmia* mutants, of which more than two dozen alleles exist. Depending on the allele, they show loss of neural-crest melanocytes and coat pigmentation, small eyes from defective RPE, early-onset deafness (melanocytes of the inner-ear stria vascularis are missing), osteopetrosis from defective osteoclasts, and reduced mast cells [hodgkinson-1993-mi-bhlhzip-abstract; steingrimsson-2004-melanocytes-mitf-abstract]. In humans, heterozygous MITF mutations cause Waardenburg syndrome type 2A, a pigmentary and deafness disorder [steingrimsson-2004-melanocytes-mitf-abstract]. MITF is also an amplified lineage oncogene in melanoma, and MiT/TFE family members are translocated oncogenes in renal carcinoma and sarcoma [levy-2006-mitf-master-regulator-abstract; martina-2014-mitf-tfe-organelle-review-abstract]. The family also regulates organelle biogenesis, nutrient sensing and energy homeostasis more broadly [martina-2014-mitf-tfe-organelle-review-abstract].

Equids give the most directly relevant in vivo evidence for the donkey gene. In horses, at least eight MITF alleles (SW1, SW3, SW6, SW7, SW8, the macchiato N310S allele, a large exon 6–9 deletion, and others) cause splashed white or related white-spotting phenotypes. These include extensive white on the face, legs and belly, often with blue eyes, and frequently deafness [hauswirth-2012-mitf-pax3-splashed-white-fulltext; henkel-2019-mitf-deletion-horse-deafness-abstract; magdesian-2020-mitf-deletion-paint-horse-fulltext; bellone-2023-mitf-structural-variant-thoroughbred-abstract; liu-2024-equine-coloration-review-fulltext]. Several of these alleles arose de novo, and heterozygosity is enough to produce the phenotype, consistent with haploinsufficiency or dominant-negative action of truncated proteins [hauswirth-2012-mitf-pax3-splashed-white-fulltext; magdesian-2020-mitf-deletion-paint-horse-fulltext]. In one Paint Horse family, six of eight horses carrying the ~63-kb exon 6–9 deletion were deaf. The authors draw the parallel with Waardenburg syndrome 2A [henkel-2019-mitf-deletion-horse-deafness-abstract], and an SW8 foal confirmed deaf by brainstem auditory evoked response testing supports the same link [bellone-2023-mitf-structural-variant-thoroughbred-abstract]. MITF also acts quantitatively. In 1,077 Franches-Montagnes horses, MITF and KIT were the major loci for white facial and leg markings, together explaining 26% of the genetic variance. They acted additively, and their effects depended on MC1R genotype, so accumulating MITF haplotype mutations progressively increase white markings [haase-2013-kit-mitf-franches-montagnes-abstract]. Together these data show that in equids, as in mice and humans, MITF dosage is needed for melanoblasts to colonise the skin and inner ear and survive there. Because the bHLH-LZ is identical between horse-lineage and human sequences and the donkey retains every functional residue, the same function is predicted for donkey MITF. Horses also provide evidence for MITF as a trans-acting regulator of melanocyte-specific enhancers. Greying with age in horses is caused by a 4.6-kb duplication in intron 6 of STX17. The duplication acts as a cis-regulatory mutation and is associated with melanoma and vitiligo-like depigmentation [rosengren-2008-grey-horse-stx17-abstract]. In reporter assays, a melanocyte-specific enhancer within the duplicated sequence depended on two MITF binding sites, which makes MITF the likely factor behind the melanocyte-restricted effect of the Grey allele [sundstrom-2012-grey-horse-mitf-enhancer-abstract]. Donkey white and white-spotted coats have so far been attributed to KIT rather than MITF [liu-2024-equine-coloration-review-fulltext], and no MITF variant has yet been linked to a donkey phenotype.

## 8. Synthesis: predicted function of donkey MITF

Taking these lines of evidence together, A0A9L0JBN5 is best annotated as an RNA polymerase II-specific, sequence-specific DNA-binding transcriptional activator. It binds E-box (CACGTG) and M-box (TCATGTG) cis-regulatory elements as a homodimer or as a MiT/TFE heterodimer. Its core roles are melanocyte differentiation, pigmentation (activation of TYR, TYRP1 and DCT) and melanocyte survival. In non-melanocyte isoforms, which the donkey entry represents, it also regulates RPE, mast-cell and osteoclast development and lysosome biogenesis. It acts downstream of MC1R–cAMP–CREB, SOX10/PAX3 and KIT–ERK/RSK signalling It is regulated by SUMOylation, by GSK3/Wnt-controlled stability and nuclear export, by mTORC1–Rag–14-3-3 cytoplasmic retention, and by nutrient-regulated β-TrCP-dependent degradation of the A-type isoform. Its functional location is the nucleus. Isoforms with the MITF-A N-terminus also occupy cytoplasmic and lysosomal-surface pools that depend on nutrient status. All of this is inferred from orthology, strong sequence conservation and experimental work in other mammals, with in vivo support from the closely related horse. None of it comes from experiments on the donkey protein, so it fits annotation by sequence similarity (ISS/IBA-type evidence) rather than direct assay.

## 9. Open questions

The most immediate uncertainty is the gene model. The 115-residue N-terminal extension in A0A9L0JBN5 is shared with other donkey and horse Ensembl models and matches the in-frame 5′ leader of human MITF-A mRNA, which suggests the predicted open frame has been extended into untranslated sequence. The 24-residue internal gap is found in no other equid model. Ribosome profiling or N-terminal proteomics would show whether the extension is ever translated. RNA-seq or long-read (e.g., ONT) transcript data from donkey skin, eye and immune tissues should be used to define the real first exons and splice patterns, and to establish whether a donkey MITF-M transcript exists and dominates in skin melanocytes. Multi-omic datasets already generated for donkey coat colour [li-2026-donkey-gray-asip-abstract] could be re-analysed for this purpose. A second question is whether the extension, if real, changes Rag-dependent lysosomal recruitment or mTORC1 control, which could be tested by expressing the donkey isoform with Torin-1 treatment, as in [martina-2013-rag-tfeb-mitf-lysosome-fulltext]. Third, given the many horse splashed-white alleles and their link to deafness, it would be worth asking whether any donkey white-spotting or blue-eyed phenotypes involve MITF or PAX3, or whether KIT explains them all [liu-2024-equine-coloration-review-fulltext]. Auditory testing of white donkeys would help answer this. Fourth, the downstream mechanism of the Hetian gray ASIP allele should be checked by measuring MITF and its targets in donkey skin. Finally, a reviewed (Swiss-Prot) equid MITF entry and experimental GO annotations for an equid protein are still lacking. Expert curation of horse and donkey MITF that takes the horse genetics into account would give better annotations than the current electronic transfers.

## 10. References

- **[uniprot-A0A9L0JBN5-entry]** UniProtKB/TrEMBL entry A0A9L0JBN5_EQUAS, "Melanocyte inducing transcription factor" (MITF), *Equus asinus*; entry version 14 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0JBN5.txt (local copy: `citations/uniprot-A0A9L0JBN5-entry.txt`; sequence `citations/uniprot-A0A9L0JBN5-sequence.fasta`).
- **[uniprot-O75030-human-MITF-entry]** UniProtKB/Swiss-Prot entry O75030 (MITF_HUMAN). https://rest.uniprot.org/uniprotkb/O75030.txt (local copy: `citations/uniprot-O75030-human-MITF-entry.txt`).
- **[aksan-1998-mitf-ebox-targeting]** Aksan I, Goding CR (1998). Targeting the microphthalmia basic helix-loop-helix-leucine zipper transcription factor to a subset of E-box elements in vitro and in vivo. *Mol Cell Biol* 18:6930-8. PMID: 9819381; PMCID: PMC109276; DOI: https://doi.org/10.1128/MCB.18.12.6930; https://pubmed.ncbi.nlm.nih.gov/9819381/
- **[bellone-2023-mitf-structural-variant-thoroughbred]** Bellone RR, Tanaka J, Esdaile E et al. (2023). A de novo 2.3 kb structural variant in MITF explains a novel splashed white phenotype in a Thoroughbred family. *Anim Genet* 54:752-762. PMID: 37697831; DOI: https://doi.org/10.1111/age.13352; https://pubmed.ncbi.nlm.nih.gov/37697831/
- **[bertolotto-2011-mitf-e318k]** Bertolotto C, Lesueur F, Giuliano S et al. (2011). A SUMOylation-defective MITF germline mutation predisposes to melanoma and renal carcinoma. *Nature* 480:94-8. PMID: 22012259; DOI: https://doi.org/10.1038/nature10539; https://pubmed.ncbi.nlm.nih.gov/22012259/
- **[goding-2019-mitf-first-25-years]** Goding CR, Arnheiter H (2019). MITF-the first 25 years. *Genes Dev* 33:983-1007. PMID: 31123060; PMCID: PMC6672050; DOI: https://doi.org/10.1101/gad.324657.119; https://pubmed.ncbi.nlm.nih.gov/31123060/
- **[haase-2013-kit-mitf-franches-montagnes]** Haase B, Signer-Hasler H, Binns MM et al. (2013). Accumulating mutations in series of haplotypes at the KIT and MITF loci are major determinants of white markings in Franches-Montagnes horses. *PLoS One* 8:e75071. PMID: 24098679; PMCID: PMC3787084; DOI: https://doi.org/10.1371/journal.pone.0075071; https://pubmed.ncbi.nlm.nih.gov/24098679/
- **[hallsson-2007-mitf-evolution-domains]** Hallsson JH, Haflidadóttir BS, Schepsky A et al. (2007). Evolutionary sequence comparison of the Mitf gene reveals novel conserved domains. *Pigment Cell Res* 20:185-200. PMID: 17516926; DOI: https://doi.org/10.1111/j.1600-0749.2007.00373.x; https://pubmed.ncbi.nlm.nih.gov/17516926/
- **[hauswirth-2012-mitf-pax3-splashed-white]** Hauswirth R, Haase B, Blatter M et al. (2012). Mutations in MITF and PAX3 cause "splashed white" and other white spotting phenotypes in horses. *PLoS Genet* 8:e1002653. PMID: 22511888; PMCID: PMC3325211; DOI: https://doi.org/10.1371/journal.pgen.1002653; https://pubmed.ncbi.nlm.nih.gov/22511888/
- **[hemesath-1994-mitf-tyrosinase]** Hemesath TJ, Steingrímsson E, McGill G et al. (1994). microphthalmia, a critical factor in melanocyte development, defines a discrete transcription factor family. *Genes Dev* 8:2770-80. PMID: 7958932; DOI: https://doi.org/10.1101/gad.8.22.2770; https://pubmed.ncbi.nlm.nih.gov/7958932/
- **[hemesath-1998-mapk-kit-mitf]** Hemesath TJ, Price ER, Takemoto C et al. (1998). MAP kinase links the transcription factor Microphthalmia to c-Kit signalling in melanocytes. *Nature* 391:298-301. PMID: 9440696; DOI: https://doi.org/10.1038/34681; https://pubmed.ncbi.nlm.nih.gov/9440696/
- **[henkel-2019-mitf-deletion-horse-deafness]** Henkel J, Lafayette C, Brooks SA et al. (2019). Whole-genome sequencing reveals a large deletion in the MITF gene in horses with white spotted coat colour and increased risk of deafness. *Anim Genet* 50:172-174. PMID: 30644113; DOI: https://doi.org/10.1111/age.12762; https://pubmed.ncbi.nlm.nih.gov/30644113/
- **[hodgkinson-1993-mi-bhlhzip]** Hodgkinson CA, Moore KJ, Nakayama A et al. (1993). Mutations at the mouse microphthalmia locus are associated with defects in a gene encoding a novel basic-helix-loop-helix-zipper protein. *Cell* 74:395-404. PMID: 8343963; DOI: https://doi.org/10.1016/0092-8674(93)90429-t; https://pubmed.ncbi.nlm.nih.gov/8343963/
- **[levy-2006-mitf-master-regulator]** Levy C, Khaled M, Fisher DE (2006). MITF: master regulator of melanocyte development and melanoma oncogene. *Trends Mol Med* 12:406-14. PMID: 16899407; DOI: https://doi.org/10.1016/j.molmed.2006.07.008; https://pubmed.ncbi.nlm.nih.gov/16899407/
- **[li-2026-donkey-gray-asip]** Li C, Wang F, Dong H et al. (2026). Multiomics analysis reveals an association of ASIP with the gray coat color pattern in donkeys. *J Anim Sci* 104:None. PMID: 41840757; PMCID: PMC13071404; DOI: https://doi.org/10.1093/jas/skag087; https://pubmed.ncbi.nlm.nih.gov/41840757/
- **[liu-2024-equine-coloration-review]** Liu X, Peng Y, Zhang X et al. (2024). Coloration in Equine: Overview of Candidate Genes Associated with Coat Color Phenotypes. *Animals (Basel)* 14:None. PMID: 38929421; PMCID: PMC11200706; DOI: https://doi.org/10.3390/ani14121802; https://pubmed.ncbi.nlm.nih.gov/38929421/
- **[magdesian-2020-mitf-deletion-paint-horse]** Magdesian KG, Tanaka J, Bellone RR (2020). A De Novo MITF Deletion Explains a Novel Splashed White Phenotype in an American Paint Horse. *J Hered* 111:287-293. PMID: 32242630; PMCID: PMC7238438; DOI: https://doi.org/10.1093/jhered/esaa009; https://pubmed.ncbi.nlm.nih.gov/32242630/
- **[martina-2013-rag-tfeb-mitf-lysosome]** Martina JA, Puertollano R (2013). Rag GTPases mediate amino acid-dependent recruitment of TFEB and MITF to lysosomes. *J Cell Biol* 200:475-91. PMID: 23401004; PMCID: PMC3575543; DOI: https://doi.org/10.1083/jcb.201209135; https://pubmed.ncbi.nlm.nih.gov/23401004/
- **[martina-2014-mitf-tfe-organelle-review]** Martina JA, Diab HI, Li H et al. (2014). Novel roles for the MiTF/TFE family of transcription factors in organelle biogenesis, nutrient sensing, and energy homeostasis. *Cell Mol Life Sci* 71:2483-97. PMID: 24477476; PMCID: PMC4057939; DOI: https://doi.org/10.1007/s00018-014-1565-8; https://pubmed.ncbi.nlm.nih.gov/24477476/
- **[murakami-2005-mitf-sumoylation]** Murakami H, Arnheiter H (2005). Sumoylation modulates transcriptional activity of MITF in a promoter-specific manner. *Pigment Cell Res* 18:265-77. PMID: 16029420; PMCID: PMC1351050; DOI: https://doi.org/10.1111/j.1600-0749.2005.00234.x; https://pubmed.ncbi.nlm.nih.gov/16029420/
- **[ploper-2015-mitf-endolysosome-wnt]** Ploper D, Taelman VF, Robert L et al. (2015). MITF drives endolysosomal biogenesis and potentiates Wnt signaling in melanoma cells. *Proc Natl Acad Sci U S A* 112:E420-9. PMID: 25605940; PMCID: PMC4321275; DOI: https://doi.org/10.1073/pnas.1424576112; https://pubmed.ncbi.nlm.nih.gov/25605940/
- **[pogenberg-2012-mitf-structure]** Pogenberg V, Ogmundsdóttir MH, Bergsteinsdóttir K et al. (2012). Restricted leucine zipper dimerization and specificity of DNA recognition of the melanocyte master regulator MITF. *Genes Dev* 26:2647-58. PMID: 23207919; PMCID: PMC3521630; DOI: https://doi.org/10.1101/gad.198192.112; https://pubmed.ncbi.nlm.nih.gov/23207919/
- **[rocznikferguson-2012-tfeb-mtorc1]** Roczniak-Ferguson A, Petit CS, Froehlich F et al. (2012). The transcription factor TFEB links mTORC1 signaling to transcriptional control of lysosome homeostasis. *Sci Signal* 5:ra42. PMID: 22692423; PMCID: PMC3437338; DOI: https://doi.org/10.1126/scisignal.2002790; https://pubmed.ncbi.nlm.nih.gov/22692423/
- **[steingrimsson-2004-melanocytes-mitf]** Steingrímsson E, Copeland NG, Jenkins NA (2004). Melanocytes and the microphthalmia transcription factor network. *Annu Rev Genet* 38:365-411. PMID: 15568981; DOI: https://doi.org/10.1146/annurev.genet.38.072902.092717; https://pubmed.ncbi.nlm.nih.gov/15568981/
- **[takemoto-2002-mitf-mast-cell-isoform]** Takemoto CM, Yoon YJ, Fisher DE (2002). The identification and functional characterization of a novel mast cell isoform of the microphthalmia-associated transcription factor. *J Biol Chem* 277:30244-52. PMID: 12039954; DOI: https://doi.org/10.1074/jbc.M201441200; https://pubmed.ncbi.nlm.nih.gov/12039954/
- **[wang-2020-donkey-genomes]** Wang C, Li H, Guo Y et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun* 11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: https://doi.org/10.1038/s41467-020-19813-7; https://pubmed.ncbi.nlm.nih.gov/33293529/
- **[wu-2000-kit-dual-phosphorylation]** Wu M, Hemesath TJ, Takemoto CM et al. (2000). c-Kit triggers dual phosphorylations, which couple activation and degradation of the essential melanocyte factor Mi. *Genes Dev* 14:301-12. PMID: 10673502; PMCID: PMC316361; https://pubmed.ncbi.nlm.nih.gov/10673502/
- **[takeda-2000-mitf-ser298-gsk3]** Takeda K, Takemoto C, Kobayashi I et al. (2000). Ser298 of MITF, a mutation site in Waardenburg syndrome type 2, is a phosphorylation site with functional significance. *Hum Mol Genet* 9:125-32. PMID: 10587587; DOI: https://doi.org/10.1093/hmg/9.1.125; https://pubmed.ncbi.nlm.nih.gov/10587587/
- **[bronisz-2006-mitf-14-3-3]** Bronisz A, Sharma SM, Hu R et al. (2006). Microphthalmia-associated transcription factor interactions with 14-3-3 modulate differentiation of committed myeloid precursors. *Mol Biol Cell* 17:3897-906. PMID: 16822840; PMCID: PMC1593166; DOI: https://doi.org/10.1091/mbc.e06-05-0470; https://pubmed.ncbi.nlm.nih.gov/16822840/
- **[nardone-2023-tfe3-mitf-stability]** Nardone C, Palanski BA, Scott DC et al. (2023). A central role for regulated protein stability in the control of TFE3 and MITF by nutrients. *Mol Cell* 83:57-73.e9. PMID: 36608670; PMCID: PMC9908011; DOI: https://doi.org/10.1016/j.molcel.2022.12.013; https://pubmed.ncbi.nlm.nih.gov/36608670/
- **[ngeow-2018-mitf-nuclear-export]** Ngeow KC, Friedrichsen HJ, Li L et al. (2018). BRAF/MAPK and GSK3 signaling converges to control MITF nuclear export. *Proc Natl Acad Sci U S A* 115:E8668-E8677. PMID: 30150413; PMCID: PMC6140509; DOI: https://doi.org/10.1073/pnas.1810498115; https://pubmed.ncbi.nlm.nih.gov/30150413/
- **[sundstrom-2012-grey-horse-mitf-enhancer]** Sundström E, Komisarczuk AZ, Jiang L et al. (2012). Identification of a melanocyte-specific, microphthalmia-associated transcription factor-dependent regulatory element in the intronic duplication causing hair greying and melanoma in horses. *Pigment Cell Melanoma Res* 25:28-36. PMID: 21883983; DOI: https://doi.org/10.1111/j.1755-148X.2011.00902.x; https://pubmed.ncbi.nlm.nih.gov/21883983/
- **[rosengren-2008-grey-horse-stx17]** Rosengren Pielberg G, Golovko A, Sundström E et al. (2008). A cis-acting regulatory mutation causes premature hair graying and susceptibility to melanoma in the horse. *Nat Genet* 40:1004-9. PMID: 18641652; DOI: https://doi.org/10.1038/ng.185; https://pubmed.ncbi.nlm.nih.gov/18641652/
- **[strub-2011-mitf-replication-mitosis]** Strub T, Giuliano S, Ye T et al. (2011). Essential role of microphthalmia transcription factor for DNA replication, mitosis and genomic stability in melanoma. *Oncogene* 30:2319-32. PMID: 21258399; DOI: https://doi.org/10.1038/onc.2010.612; https://pubmed.ncbi.nlm.nih.gov/21258399/
- **[laurette-2015-mitf-brg1-chromatin]** Laurette P, Strub T, Koludrovic D et al. (2015). Transcription factor MITF and remodeller BRG1 define chromatin organisation at regulatory elements in melanoma cells. *Elife* 4:None. PMID: 25803486; PMCID: PMC4407272; DOI: https://doi.org/10.7554/eLife.06857; https://pubmed.ncbi.nlm.nih.gov/25803486/
- **[uniprot-K4FCY0-entry]** UniProtKB/TrEMBL entry K4FCY0 (horse MITF-M(+), from EMBL JN896378 / AFH66983.1, Hauswirth et al. submission). https://rest.uniprot.org/uniprotkb/K4FCY0.txt
- **[uniprot-A0A9L0JHX8-entry]** UniProtKB/TrEMBL entry A0A9L0JHX8 (donkey MITF, 419 aa, Ensembl ENSEASP00005002830.2). https://rest.uniprot.org/uniprotkb/A0A9L0JHX8.txt
- **[uniprot-A0A5F5PRV7-entry]** UniProtKB/TrEMBL entry A0A5F5PRV7 (horse MITF, 635 aa, Ensembl ENSECAP00000051097.2). https://rest.uniprot.org/uniprotkb/A0A5F5PRV7.txt
- **[ncbi-NM_198159-human-MITF-A-mRNA]** NCBI RefSeq NM_198159.3, *Homo sapiens* melanocyte inducing transcription factor (MITF), transcript variant 1 mRNA. https://www.ncbi.nlm.nih.gov/nuccore/NM_198159


## Citations

1. _metadata.json
2. aksan-1998-mitf-ebox-targeting-abstract.md
3. aksan-1998-mitf-ebox-targeting-summary.md
4. bellone-2023-mitf-structural-variant-thoroughbred-abstract.md
5. bellone-2023-mitf-structural-variant-thoroughbred-summary.md
6. bertolotto-2011-mitf-e318k-abstract.md
7. bertolotto-2011-mitf-e318k-summary.md
8. bronisz-2006-mitf-14-3-3-abstract.md
9. bronisz-2006-mitf-14-3-3-summary.md
10. durig-2017-mitf-variant-standardbred-abstract.md
11. durig-2017-mitf-variant-standardbred-summary.md
12. goding-2019-mitf-first-25-years-abstract.md
13. goding-2019-mitf-first-25-years-fulltext.txt
14. goding-2019-mitf-first-25-years-summary.md
15. haase-2013-kit-mitf-franches-montagnes-abstract.md
16. haase-2013-kit-mitf-franches-montagnes-fulltext.txt
17. haase-2013-kit-mitf-franches-montagnes-summary.md
18. hallsson-2007-mitf-evolution-domains-abstract.md
19. hallsson-2007-mitf-evolution-domains-summary.md
20. hauswirth-2012-mitf-pax3-splashed-white-abstract.md
21. hauswirth-2012-mitf-pax3-splashed-white-fulltext.txt
22. hauswirth-2012-mitf-pax3-splashed-white-summary.md
23. hemesath-1994-mitf-tyrosinase-abstract.md
24. hemesath-1994-mitf-tyrosinase-summary.md
25. hemesath-1998-mapk-kit-mitf-abstract.md
26. hemesath-1998-mapk-kit-mitf-summary.md
27. henkel-2019-mitf-deletion-horse-deafness-abstract.md
28. henkel-2019-mitf-deletion-horse-deafness-summary.md
29. hodgkinson-1993-mi-bhlhzip-abstract.md
30. hodgkinson-1993-mi-bhlhzip-summary.md
31. laurette-2015-mitf-brg1-chromatin-abstract.md
32. laurette-2015-mitf-brg1-chromatin-fulltext.txt
33. laurette-2015-mitf-brg1-chromatin-summary.md
34. levy-2006-mitf-master-regulator-abstract.md
35. levy-2006-mitf-master-regulator-summary.md
36. li-2026-donkey-gray-asip-abstract.md
37. li-2026-donkey-gray-asip-summary.md
38. liu-2024-equine-coloration-review-abstract.md
39. liu-2024-equine-coloration-review-fulltext.txt
40. liu-2024-equine-coloration-review-summary.md
41. magdesian-2020-mitf-deletion-paint-horse-abstract.md
42. magdesian-2020-mitf-deletion-paint-horse-fulltext.txt
43. magdesian-2020-mitf-deletion-paint-horse-summary.md
44. martina-2013-rag-tfeb-mitf-lysosome-abstract.md
45. martina-2013-rag-tfeb-mitf-lysosome-fulltext.txt
46. martina-2013-rag-tfeb-mitf-lysosome-summary.md
47. martina-2014-mitf-tfe-organelle-review-abstract.md
48. martina-2014-mitf-tfe-organelle-review-summary.md
49. murakami-2005-mitf-sumoylation-abstract.md
50. murakami-2005-mitf-sumoylation-summary.md
51. nardone-2023-tfe3-mitf-stability-abstract.md
52. nardone-2023-tfe3-mitf-stability-fulltext.txt
53. nardone-2023-tfe3-mitf-stability-summary.md
54. ncbi-NM_198159-human-MITF-A-mRNA-summary.md
55. ncbi-NM_198159-human-MITF-A-mRNA.gb
56. ngeow-2018-mitf-nuclear-export-abstract.md
57. ngeow-2018-mitf-nuclear-export-summary.md
58. pattersonrosa-2022-mitf-nonframeshift-deletion-abstract.md
59. pattersonrosa-2022-mitf-nonframeshift-deletion-summary.md
60. ploper-2015-mitf-endolysosome-wnt-abstract.md
61. ploper-2015-mitf-endolysosome-wnt-summary.md
62. pogenberg-2012-mitf-structure-abstract.md
63. pogenberg-2012-mitf-structure-summary.md
64. rocznikferguson-2012-tfeb-mtorc1-abstract.md
65. rocznikferguson-2012-tfeb-mtorc1-summary.md
66. rosengren-2008-grey-horse-stx17-abstract.md
67. rosengren-2008-grey-horse-stx17-summary.md
68. steingrimsson-2004-melanocytes-mitf-abstract.md
69. steingrimsson-2004-melanocytes-mitf-summary.md
70. strub-2011-mitf-replication-mitosis-abstract.md
71. strub-2011-mitf-replication-mitosis-summary.md
72. sundstrom-2012-grey-horse-mitf-enhancer-abstract.md
73. sundstrom-2012-grey-horse-mitf-enhancer-summary.md
74. takeda-2000-mitf-ser298-gsk3-abstract.md
75. takeda-2000-mitf-ser298-gsk3-summary.md
76. takemoto-2002-mitf-mast-cell-isoform-abstract.md
77. takemoto-2002-mitf-mast-cell-isoform-summary.md
78. uniprot-A0A5F5PRV7-entry.txt
79. uniprot-A0A5F5PRV7-sequence.fasta
80. uniprot-A0A5F5PRV7-summary.md
81. uniprot-A0A8C4PGB1-sequence.fasta
82. uniprot-A0A9L0IUI7-sequence.fasta
83. uniprot-A0A9L0JBN5-entry.txt
84. uniprot-A0A9L0JBN5-sequence.fasta
85. uniprot-A0A9L0JBN5-summary.md
86. uniprot-A0A9L0JHX8-entry.txt
87. uniprot-A0A9L0JHX8-sequence.fasta
88. uniprot-A0A9L0JHX8-summary.md
89. uniprot-A0A9L0KEI8-sequence.fasta
90. uniprot-K4FCY0-entry.txt
91. uniprot-K4FCY0-sequence.fasta
92. uniprot-K4FCY0-summary.md
93. uniprot-O75030-9-human-MITF-M1-sequence.fasta
94. uniprot-O75030-human-MITF-entry.txt
95. uniprot-O75030-human-MITF-sequence.fasta
96. wang-2020-donkey-genomes-abstract.md
97. wang-2020-donkey-genomes-fulltext.txt
98. wang-2020-donkey-genomes-summary.md
99. wu-2000-kit-dual-phosphorylation-abstract.md
100. wu-2000-kit-dual-phosphorylation-summary.md