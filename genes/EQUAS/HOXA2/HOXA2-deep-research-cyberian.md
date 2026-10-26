---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:52:33.450311'
end_time: '2026-10-26T00:05:40.299327'
duration_seconds: 786.85
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: HOXA2
  gene_symbol: HOXA2
  uniprot_accession: A0A9L0JBM7
  protein_description: 'RecName: Full=Homeobox protein Hox-A2 {ECO:0000256|ARBA:ARBA00040119};'
  gene_info: Name=HOXA2 {ECO:0000313|Ensembl:ENSEASP00005047417.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the Antp homeobox family. Proboscipedia
  protein_domains: HD. (IPR001356); HD_metazoa. (IPR020479); Homeobox_Antennapedia_CS.
    (IPR001827); Homeobox_CS. (IPR017970); Homeodomain-like_sf. (IPR009057)
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
citation_count: 95
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0JBM7
- **Protein Description:** RecName: Full=Homeobox protein Hox-A2 {ECO:0000256|ARBA:ARBA00040119};
- **Gene Information:** Name=HOXA2 {ECO:0000313|Ensembl:ENSEASP00005047417.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the Antp homeobox family. Proboscipedia
- **Key Domains:** HD. (IPR001356); HD_metazoa. (IPR020479); Homeobox_Antennapedia_CS. (IPR001827); Homeobox_CS. (IPR017970); Homeodomain-like_sf. (IPR009057)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "HOXA2" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'HOXA2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **HOXA2** (gene ID: HOXA2, UniProt: A0A9L0JBM7) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# HOXA2 (Homeobox protein Hox-A2) in the donkey, *Equus asinus* (UniProt A0A9L0JBM7)

## 1. Introduction and summary

A0A9L0JBM7 is the donkey ortholog of vertebrate HOXA2. It is a 373-residue homeodomain transcription factor of the Antennapedia (Antp) homeobox family, proboscipedia (paralog group 2, PG2) subfamily. It was predicted from the chromosome-level Dezhou donkey reference genome and is so far supported only by automatic annotation (UniProt TrEMBL, Ensembl ENSEASP00005047417.1, RefSeq XP_014696502.1, GeneID 106831026) [wang-2020-donkeygenome-abstract]. The donkey genome paper that produced the sequence does not discuss HOXA2 at all [wang-2020-donkeygenome-fulltext]. A PubMed search for Hoxa2 in *Equus* returned no hits. No experimental study of HOXA2 in donkey or horse therefore exists. The identity of the protein is not in doubt: the gene symbol, the family assignment and the domain composition all match the well-studied HOXA2 orthologs of mouse, human, chick, frog and zebrafish. In particular, the donkey homeodomain is identical to the human one over all 60 residues, and the full proteins are about 96.5% identical (see Section 2 and `NOTES_sequence_analysis.md`). The functional account below is therefore an inference from orthologs, which this degree of conservation strongly supports. Each statement is labelled with the organism in which the evidence was obtained.

In outline, HOXA2 is a nuclear, sequence-specific DNA-binding transcription factor. In the embryo it gives cells a positional ("second segment") identity along the anterior–posterior axis of the head. Its best-characterized job is as the selector gene for the second pharyngeal (hyoid) arch. In cranial neural crest-derived mesenchyme that migrates from rhombomere 4 into this arch, HOXA2 overrides a default, Hox-free, mandibular-like skeletal ground pattern. It thereby specifies hyoid-arch derivatives: the stapes, styloid process and lesser horns of the hyoid, and the external ear (pinna) [rijli-1993-selector-abstract; gendronmaguire-1993-homeotic-abstract; minoux-2013-auricle-abstract]. Molecularly, HOXA2 works with the TALE homeodomain cofactors PBX and MEIS. It binds thousands of genomic sites carrying Hox and Pbx–Hox motifs [donaldson-2012-chipseq-wnt-fulltext] and increases MEIS occupancy at a selected subset of enhancers, which makes it act as a tissue-specific cofactor that modifies a MEIS-defined ground state [amin-2015-meis-fulltext]. Its direct target genes include *Six2* (repressed), *Meox1* (activated), *Robo2*, *Hmx1* and components of the Wnt pathway such as *Fzd4* and *Wnt5a*. Through these targets HOXA2 limits chondrogenesis and dermal ossification, drives Wnt/β-catenin signalling in the outgrowing pinna, and controls guidance-receptor expression in migrating hindbrain neurons [kutejova-2005-six2-abstract; kirilenko-2011-meox1-abstract; geisen-2008-pontine-fulltext; rosin-2016-hmx1-abstract; donaldson-2012-chipseq-wnt-fulltext; kanzler-1998-chondrogenic-abstract]. In humans, heterozygous truncating or biallelic homeodomain mutations in HOXA2 cause microtia with hearing loss, which shows that the gene is dosage-sensitive in mammals [alasti-2008-microtia-abstract; brown-2013-haploinsufficiency-abstract; piceci-2017-microtia-abstract].

## 2. Identity, structure and evolutionary conservation

The UniProt entry assigns the donkey protein to the Antp homeobox family, proboscipedia subfamily. It records InterPro signatures for the homeodomain (IPR001356, IPR020479), the Antennapedia-type homeobox conserved site (IPR001827), the general homeobox conserved site (IPR017970) and the homeodomain-like superfamily (IPR009057). The entry's function and localization comments ("sequence-specific transcription factor ... positional identities on the anterior–posterior axis"; nucleus) are rule-based (ARBA, PROSITE ProRule PRU00108) rather than experimental. The gene sits on donkey chromosome 1 in the reference assembly [wang-2020-donkeygenome-abstract].

I aligned the donkey sequence to human HOXA2 (UniProt P31245) myself. Of the 372 human residues, 359 are identical, and the only differences are two short alanine/glycine-rich indels in the N-terminal low-complexity region and a few conservative substitutions in the C-terminal region. The homeodomain, which UniProt places at residues 139–198 in human and which corresponds to donkey residues 140–199, is identical in sequence. It includes the recognition helix motif WFQNRRMK, which makes base-specific contacts in the DNA major groove. The Antp-type hexapeptide PEYPWM upstream of the homeodomain (human 96–101; donkey 93–98) is also conserved; in Hox proteins this motif mediates the interaction with PBX. This degree of conservation is consistent with the strong functional conservation of PG2 Hox genes across vertebrates. Hoxa2 and Hoxb2 act as second-arch selector genes in zebrafish, *Xenopus*, chick and mouse, although which paralog is required differs between lineages: the two act redundantly in zebrafish, whereas *Hoxa2* alone is required in frog and mouse [hunter-2002-zebrafish-abstract; baltzinger-2005-knockdown-abstract; grammatopoulos-2000-overexpression-abstract]. The neural crest enhancers that drive Hox2 expression are themselves ancient, having been conserved since the divergence of jawed vertebrates from lamprey [parker-2019-hoxtale-abstract]. Since the donkey shares the eutherian body plan, including the hyoid apparatus, middle ear ossicles and an external pinna, it is reasonable to transfer the mammalian (mouse/human) functions described below to the donkey protein.

## 3. Molecular function: a PBX/MEIS-assisted homeodomain transcription factor

HOXA2 binds DNA through its homeodomain. Chromatin immunoprecipitation followed by sequencing (ChIP-seq) of endogenous Hoxa2 in the mouse second branchial arch at E11.5 showed binding at thousands of genomic regions. The bound regions are enriched for two main motif classes, a monomeric Hox site and a composite Pbx–Hox site [donaldson-2012-chipseq-wnt-fulltext]. A considerable fraction of the genes misregulated in *Hoxa2* mutant arches lay next to Hoxa2 peaks. Bound and regulated genes included previously known functional targets (*Robo2*, *Six2*), genes deregulated in the mutant (*Runx2*, *Msx1*), other Hox genes, and the cofactor genes *Meis1* and *Meis2*. The last suggests a positive feedback loop between Hox and Meis [donaldson-2012-chipseq-wnt-fulltext].

Hox proteins bind DNA with low specificity on their own, so how HOXA2 selects its targets has been studied directly in vivo. Amin et al. mapped Meis, Pbx and Hoxa2 occupancy in the Hox-negative first arch and the Hoxa2-positive second arch. Meis binding was largely shared between the two arches and appears to set a ground state. Hoxa2 bound a subset of Meis-prebound sites carrying Hox motifs and strongly increased Meis occupancy at those sites. These sites coincided with active enhancers near genes highly expressed in, and regulated by Hoxa2 in, the second arch [amin-2015-meis-fulltext]. When Hoxa2 was forced into Hox-negative first-arch cells, Meis binding rose specifically at Hoxa2-bound regions. The authors therefore concluded that Hoxa2 acts as a "tissue-specific cofactor" that changes the arch ground state rather than reprogramming it wholesale [amin-2015-meis-fulltext]. Cooperative Hoxa2–Pbx–Meis action at individual enhancers has been shown at the *Hmx1* pinna enhancer, which depends on a 32-bp core [rosin-2016-hmx1-abstract]. It is also seen in cell-based assays, where Hoxa2 suppressed neuronal differentiation of P19 cells only when Pbx and Meis were co-expressed [yang-2008-facialganglia-abstract].

HOXA2 acts as both a repressor and an activator. It binds a 0.9-kb fragment of the *Six2* promoter and represses it [kutejova-2005-six2-abstract], and it activates the *Meox1* proximal promoter through two conserved binding sites [kirilenko-2011-meox1-abstract]. These activities match the Ensembl-projected GO terms on the donkey entry: "DNA-binding transcription repressor activity, RNA polymerase II-specific" and "RNA polymerase II cis-regulatory region sequence-specific DNA binding". The homeodomain mutation found in human recessive microtia (reported as p.Q186K, at a highly conserved residue) is predicted by homology modelling to lose a hydrogen bond to the DNA phosphate backbone and so to impair DNA binding [alasti-2008-microtia-abstract]. This supports the view that DNA binding is essential to HOXA2 function.

In addition to its role as a transcription factor, one study of overexpressed proteins in HEK293T cells reported a non-transcriptional activity. Hoxa2 interacted with 20S proteasome subunits and with the p53-directed E3 ubiquitin ligase RCHY1/PIRH2, and promoted ubiquitin-independent proteasomal degradation of RCHY1, which stabilized p53. The two proteins colocalized in the nucleus, and the activity required an intact homeodomain [bergiers-2013-rchy1-fulltext]. A follow-up study showed that this decay uses both the 19S and 20S proteasome complexes and requires the homeodomain together with the C-terminal region of Hoxa2. Several Hox proteins can bind RCHY1 through their homeodomains, but only some of them trigger its degradation. The activity is conserved among vertebrate Hoxa2 orthologs, which suggests it may be an ancestral Hox property [bridoux-2015-rchy1-abstract]. These findings have not been tested in embryos and should be regarded as secondary, cell-culture-level observations.

HOXA2 also contacts other Hox proteins. In bimolecular fluorescence complementation (BiFC) and co-precipitation assays in cultured cells, HOXA2 formed homodimers and heterodimers with HOXA1, mostly in the nucleus. The homeodomain was not needed for dimerization, but it influenced whether the dimers stayed in the nucleus [marchese-2025-dimerization-fulltext]. The same study cites an earlier report of a HOXA2–HOXA3 interaction in cell culture [marchese-2025-dimerization-fulltext]. That interaction would fit with the genetic synergy between *Hoxa2* and *Hoxa3* in the posterior arches [minoux-2009-groundpattern-abstract], although whether these physical interactions matter in vivo is unknown.

## 4. Subcellular localization, its regulation, and expression domains

HOXA2 is mainly a nuclear protein. The UniProt nucleus annotation for the donkey entry is inferred from the homeodomain rule, and it agrees with experimental immunocytochemistry showing a "classical nuclear staining" for tagged Hoxa2 in mammalian cells [bergiers-2013-rchy1-fulltext]. Its function as a chromatin-bound factor also fits this localization: it occupies enhancers and promoters in ChIP experiments in embryonic tissue [donaldson-2012-chipseq-wnt-fulltext; amin-2015-meis-fulltext].

Nuclear localization is regulated rather than fixed. A proteome-wide yeast two-hybrid screen identified KPC2 (UBAC1), an adapter subunit of the KPC E3 ubiquitin ligase complex, as a HOXA2 partner. Co-precipitation and BiFC confirmed the interaction. KPC2 reduced HOXA2 transcriptional activity and caused HOXA2 to leave the nucleus, and *Kpc2* expression in the mouse embryo overlaps the *Hoxa2* domain [bridoux-2015-kpc2-abstract]. HOXA2 also binds the catalytic PP1 phosphatase subunit PPP1CB, which colocalizes with the HOXA2–KPC2 complex in the cytoplasm. Together, PPP1CB and KPC2 inhibit HOXA2 activity by promoting its nuclear export, yet they also favour de-ubiquitination and stabilization of HOXA2, which creates a cytoplasmic store of the protein [deneyer-2019-cytoplasmic-abstract]. In the model proposed by the same group, KPC2 binds HOXA2 in the nucleus and triggers CRM1-dependent export. Inhibiting CRM1 traps the complex in the nucleus. PPP1CB then stabilizes cytoplasmic HOXA2 as a ready-to-use pool that can return to the nucleus [bridoux-2021-localization-review-fulltext]. These data come from cultured cells. Even so, they mean that the GO annotation "nucleus" describes where HOXA2 is active, while a regulated cytoplasmic pool may also exist.

At the tissue level, mouse *Hoxa2* is the most anteriorly expressed Hox gene. It is the only Hox gene expressed in rhombomere 2 of the hindbrain [lampe-2004-autoregulation-abstract], and it is expressed in r3–r5 and in the cranial neural crest that populates the second and more posterior pharyngeal arches. The first (mandibular) arch remains Hox-free [minoux-2009-groundpattern-abstract; kitazawa-2022-ectopic-abstract]. Within the second-arch mesenchyme, Hoxa2 protein is present throughout but is excluded from the chondrogenic condensations [kanzler-1998-chondrogenic-abstract]. Expression persists in the outgrowing pinna [donaldson-2012-chipseq-wnt-fulltext]. Several regulatory inputs set up this pattern. Krox20 directly activates an r3/r5 enhancer 5' of the gene [nonchev-1996-krox20-abstract]. Hoxa2 autoregulates through a Hox–Pbx site in its r2 enhancer [lampe-2004-autoregulation-abstract]. Hoxb1 acts through an intronic r4 enhancer containing Hox/Pbx and Pbx–Prep/Meis sites [tumpel-2007-r4-abstract]. Neural crest expression depends on a separate enhancer. That enhancer requires an AP-2 binding site, is activated by AP-2 family transcription factors, and is not needed for hindbrain expression, so crest and rhombomere expression are regulated independently [maconochie-1999-ap2-abstract]. Conserved Hox–TALE circuits also contribute to neural crest expression [parker-2019-hoxtale-abstract]. Finally, a cluster of super-enhancers (HIRE1/HIRE2) makes long-range contacts with *Hoxa2* across a TAD boundary specifically in second-arch neural crest [kessler-2023-superenhancer-abstract]. Before and after migration, positional genes in cranial neural crest are held in bivalent H3K27me3/H3K4me2 Polycomb domains, which provide an epigenetic template for this position-specific expression [minoux-2017-bivalency-abstract].

## 5. Biological role I: selector of second pharyngeal arch identity

The defining function of HOXA2 was identified through two independent mouse knockouts published together in 1993. In *Hoxa2*-null mice, segmentation of the rhombomeres and neural crest was normal. However, the neural crest-derived skeletal elements of the second arch were absent and were replaced by a mirror-image duplicate set of first-arch elements, including duplicated Meckel's cartilage, middle-ear ossicles and an atavistic pterygoquadrate-like element. The mutants also had cleft palate and died at birth [rijli-1993-selector-abstract; gendronmaguire-1993-homeotic-abstract]. These results showed that a Hox-free skeletogenic ground pattern is shared by first- and second-arch neural crest and that Hoxa2 acts as a selector gene that modifies it. This was the first direct evidence for a "branchial Hox code" [rijli-1993-selector-abstract; gendronmaguire-1993-homeotic-abstract; trainor-2001-review-abstract]. Removing the entire *Hoxa* cluster from neural crest extended the same principle to arches 3 and 4, where *Hoxa2* and *Hoxa3* act synergistically [minoux-2009-groundpattern-abstract].

Gain-of-function experiments give the reverse transformation, which confirms that HOXA2 is sufficient as well as necessary. Overexpressing Hoxa2 in the chick first arch transforms Meckel's and quadrate cartilages into second-arch elements [grammatopoulos-2000-overexpression-abstract]. Inducing Hoxa2 in *Xenopus* after crest migration transforms a subset of jaw elements toward hyoid morphology [pasqualetti-2000-xenopus-abstract]. In mouse, ectopic Hoxa2 in first-arch neural crest duplicates the pinna [minoux-2013-auricle-abstract]. These effects depend sharply on dose. Ectopic Hoxa2 at about 60% of its physiological level is enough to duplicate the pinna; about 100% is needed for complete homeotic repatterning of first-arch skeletal elements; and about 200% causes near-total loss of craniofacial skeleton. Hoxa5 cannot substitute, which shows that the effect is specific to Hoxa2 [kitazawa-2022-ectopic-fulltext].

Conditional and temporally controlled deletion in mouse showed that Hoxa2 is required in the neural crest cells themselves. Its requirement continues after the crest has migrated into the arch, and deletion at that stage still produces the full homeotic phenotype, with rapid changes in *Alx4*, *Bapx1*, *Six2* and *Msx1* expression. Postmigratory hyoid crest is therefore still plastic and depends on continued Hoxa2 activity [santagati-2005-temporal-abstract]. The same late requirement was seen in *Xenopus* knockdowns, where the jaw-joint gene *Xbap* (Bapx1) was derepressed in the second arch [baltzinger-2005-knockdown-abstract].

## 6. Biological role II: downstream pathways in skeletogenesis and ear morphogenesis

Several downstream pathways have been linked to HOXA2 by direct-target evidence. First, HOXA2 restricts where cartilage and bone form. In normal second-arch mesenchyme it is excluded from chondrogenic condensations. In its absence, the *Sox9* domain expands into the former Hoxa2 domain and ectopic cartilage forms, and misexpressing *Sox9* there mimics the mutant. Hoxa2 also inhibits dermal (intramembranous) bone formation, and the osteogenic regulator *Cbfa1/Runx2* is upregulated in mutant arches [kanzler-1998-chondrogenic-abstract]. This anti-chondrogenic activity can be separated from patterning. When Hoxa2 was forced to stay on in *Col2a1*-expressing cells that had already committed to chondrogenesis, mice developed generalized chondrodysplasia, with delayed chondrocyte hypertrophy, mineralization and ossification. Condensation and skeletal patterning were normal, and the effect occurred regardless of embryonic origin. This indicates that *Hoxa2* must normally be switched off for chondrocytes to differentiate [massip-2007-chondrogenesis-abstract]. Second, HOXA2 directly represses *Six2*. *Six2* is overexpressed in *Hoxa2* mutants, transgenic *Six2* overexpression phenocopies part of the mutant, and Hoxa2 binds the *Six2* promoter [kutejova-2005-six2-abstract]. In vivo genetic interaction showed that derepressed *Six2* contributes to the *Hoxa2* mutant phenotype, possibly through the insulin-like growth factor pathway [kutejova-2008-six2-abstract]. Third, HOXA2 directly activates *Meox1* at an early stage, and *Meox1*/*Meox2* double mutants malform two of the three skeletal elements patterned by Hoxa2 [kirilenko-2011-meox1-abstract].

Fourth, Hoxa2 ChIP-seq unexpectedly placed the Wnt pathway at the top of the enriched biological processes. Eight of eight tested Wnt-associated Hoxa2 peaks were confirmed by ChIP-qPCR. *Fzd4* and *Wnt5a* expression in the second arch and developing outer ear depended on Hoxa2, and canonical Wnt/β-catenin reporter activity (BAT-gal), which is strong in the wild-type second arch and later in the pinna, was lost in *Hoxa2* mutants [donaldson-2012-chipseq-wnt-fulltext]. Fifth, in external ear development, fate mapping in mouse showed that the pinna derives entirely from Hoxa2-expressing second-arch neural crest mesenchyme. Hoxa2 shapes the pinna partly through BMP signalling and *Eya1* [minoux-2013-auricle-abstract] and partly through cooperative Hox–Pbx–Meis activation of *Hmx1*, whose loss also causes external ear defects [rosin-2016-hmx1-abstract].

HOXA2 also controls cell fate in non-skeletal crest derivatives. In *Hoxa2* mutants the facial ganglion contains many neural crest-derived neurons, which suggests that Hoxa2 normally suppresses the neurogenic potential of second-arch crest. Consistent with this, Hoxa2 together with Pbx and Meis lowered neurogenesis in chick trigeminal crest and in P19 cells [yang-2008-facialganglia-abstract].

## 7. Biological role III: hindbrain patterning and neuronal migration

In the central nervous system, Hoxa2 is expressed in rhombomeres 2–5 and helps specify their identity [lampe-2004-autoregulation-abstract; nonchev-1996-krox20-abstract]. The rhombomere-specific *Hoxa2* enhancers are reliable enough to have been used as segmental drivers for fate-mapping brainstem vestibular neurons [pasqualetti-2007-fatemap-abstract]. The clearest mechanistic example of its neural function concerns the precerebellar pontine neurons. These neurons migrate tangentially along the anterior–posterior axis before turning toward the ventral midline. Hoxa2 and Hoxb2 are required, both in the migrating cells and in their environment, to keep subsets of pontine neurons on the correct anterior–posterior course and to stop them from being drawn prematurely to the midline. The mutant phenotype is phenocopied by *Robo1;Robo2*, *Slit1;Slit2* and *Robo2;Slit2* compound mutants. ChIP showed that Hoxa2 binds the *Robo2* locus directly in vivo, and Hoxa2 is needed to keep *Robo2* and *Slit2* expression high. The facial motor nucleus was identified as a major Slit source [geisen-2008-pontine-fulltext]. HOXA2 therefore links positional identity to a defined guidance pathway (Slit–Robo repulsion opposing Netrin-1–Dcc attraction).

## 8. Disease relevance and implications for the donkey

The human phenotypes show that the mouse findings carry over to mammals in general. A homozygous homeodomain missense variant (p.Q186K) causes autosomal-recessive bilateral microtia, mixed hearing loss and partial cleft palate [alasti-2008-microtia-abstract]. Heterozygous nonsense variants (p.Q235* and p.E224*, both truncating the protein shortly after the homeodomain) cause autosomal-dominant non-syndromic microtia with hearing loss or distinctive ear morphology, which defines HOXA2 haploinsufficiency as a cause of dominant microtia [brown-2013-haploinsufficiency-abstract; piceci-2017-microtia-abstract]. HOXA2 coding mutations are nevertheless a rare cause of sporadic microtia [monks-2010-microtia-abstract]. Mouse conditional alleles reproduce both microtia (late loss of function) and auricle duplication (ectopic gain of function) [minoux-2013-auricle-abstract]. Deleting a super-enhancer on a *Hoxa2*-heterozygous background also produces microtia, which shows that sensitivity to regulatory dosage extends to non-coding elements [kessler-2023-superenhancer-abstract]. Downstream of HOXA2, copy-number variants of an enhancer cluster controlling the target gene *HMX1* cause human bilateral constricted ear. The dominant enhancer in that cluster carries a TALE homeodomain motif pattern (HOXA2/MEIS1/PBX1) together with HMG-box and "Coordinator" motifs [xu-2025-auricular-cnv-fulltext]. This places the HOXA2–MEIS–PBX → *HMX1* axis described in mouse [rosin-2016-hmx1-abstract] in human pinna disease. Every residue affected by these human variants lies in regions conserved in the donkey protein, and the donkey homeodomain is identical to the human one. So variation in donkey *HOXA2* or its enhancers would be expected to affect the development of the ear (pinna size and shape), middle-ear ossicles and hyoid apparatus. Pinna morphology is a conspicuous trait in equids, which makes this an interesting, though untested, hypothesis.

Taken together, the best-supported annotations for donkey HOXA2 are as follows. The molecular functions are sequence-specific, RNA polymerase II cis-regulatory region DNA binding, and DNA-binding transcription factor activity with both repressor and activator outputs, exercised together with PBX/MEIS. The cellular component is the nucleus; cell-culture data also point to a regulated cytoplasmic pool controlled by KPC2 and PPP1CB. The biological processes are anterior/posterior pattern specification, pharyngeal (second arch) system development, embryonic skeletal system development including negative regulation of chondrocyte differentiation and ossification, external and middle ear morphogenesis, rhombomere specification, and regulation of neuronal migration through Slit–Robo signalling. All of these are inferred by orthology from mouse and human experimental data.

## Open Questions

Because no equid-specific data exist, the most immediate gap is direct confirmation that donkey HOXA2 is expressed in the expected hindbrain and second-arch domains and binds the expected Hox/Pbx–Hox motifs. Comparative embryology in horse or donkey, or simply mining equine embryonic transcriptomes, would address this. It would also help to test whether the HIRE1/HIRE2 super-enhancer region and the Krox20, r4 and neural crest enhancers of *HOXA2* are conserved in the donkey assembly [kessler-2023-superenhancer-abstract; nonchev-1996-krox20-abstract; tumpel-2007-r4-abstract; parker-2019-hoxtale-abstract]. Given that ectopic Hoxa2 dose alone can determine pinna duplication in mouse [kitazawa-2022-ectopic-fulltext], a natural follow-up would be to ask whether regulatory variation at *HOXA2* or its targets (*HMX1*, *SIX2*, *WNT5A*) contributes to the characteristically long ears of donkeys compared with horses. Population-genomic scans could test this using the 126 donkey genomes described in the reference-genome study [wang-2020-donkeygenome-abstract]. Mechanistically, it is still unclear how HOXA2 raises MEIS occupancy, whether by direct protein–protein contact or through bridging factors [amin-2015-meis-fulltext]. It is also unclear why many HOXA2 peaks lack recognizable Hox motifs and lie near bone-formation genes [donaldson-2012-chipseq-wnt-fulltext]. The non-transcriptional RCHY1/p53 activity reported in HEK293T cells [bergiers-2013-rchy1-fulltext] needs validation in a developmental setting. The same applies to the KPC2/PPP1CB-controlled nuclear export of HOXA2 [bridoux-2015-kpc2-abstract; deneyer-2019-cytoplasmic-abstract]. It would be informative to know whether cytoplasmic HOXA2 can be detected in second-arch or hindbrain cells in vivo, and whether loss of *Kpc2* changes the *Hoxa2* phenotype. Similarly, it is unknown whether HOX–HOX dimers, such as the HOXA2 homodimers and HOXA1–HOXA2 heterodimers seen in cultured cells [marchese-2025-dimerization-fulltext], form in embryos where these genes are co-expressed. Finally, the late, post-migratory requirement for Hoxa2 [santagati-2005-temporal-abstract] raises the question of whether HOXA2 has roles in adult tissues of large mammals, which no current data address.

## References

- **alasti-2008-microtia**: Alasti F, Sadeghi A, Sanati MH et al. (2008). A mutation in HOXA2 is responsible for autosomal-recessive microtia in an Iranian family. *American Journal of Human Genetics* 82:982-91. PMID: 18394579; PMCID: PMC2427268; DOI: 10.1016/j.ajhg.2008.02.015. https://pubmed.ncbi.nlm.nih.gov/18394579/
- **amin-2015-meis**: Amin S, Donaldson IJ, Zannino DA et al. (2015). Hoxa2 selectively enhances Meis binding to change a branchial arch ground state. *Developmental Cell* 32:265-77. PMID: 25640223; PMCID: PMC4333904; DOI: 10.1016/j.devcel.2014.12.024. https://pubmed.ncbi.nlm.nih.gov/25640223/
- **baltzinger-2005-knockdown**: Baltzinger M, Ori M, Pasqualetti M et al. (2005). Hoxa2 knockdown in Xenopus results in hyoid to mandibular homeosis. *Developmental Dynamics* 234:858-67. PMID: 16222714; DOI: 10.1002/dvdy.20567. https://pubmed.ncbi.nlm.nih.gov/16222714/
- **bergiers-2013-rchy1**: Bergiers I, Bridoux L, Nguyen N et al. (2013). The homeodomain transcription factor Hoxa2 interacts with and promotes the proteasomal degradation of the E3 ubiquitin protein ligase RCHY1. *PLoS One* 8:e80387. PMID: 24244684; PMCID: PMC3820564; DOI: 10.1371/journal.pone.0080387. https://pubmed.ncbi.nlm.nih.gov/24244684/
- **bridoux-2015-kpc2**: Bridoux L, Bergiers I, Draime A et al. (2015). KPC2 relocalizes HOXA2 to the cytoplasm and decreases its transcriptional activity. *Biochimica et Biophysica Acta* 1849:1298-311. PMID: 26303204; DOI: 10.1016/j.bbagrm.2015.08.006. https://pubmed.ncbi.nlm.nih.gov/26303204/
- **bridoux-2015-rchy1**: Bridoux L, Deneyer N, Bergiers I et al. (2015). Molecular Analysis of the HOXA2-Dependent Degradation of RCHY1. *PLoS One* 10:e0141347. PMID: 26496426; PMCID: PMC4619689; DOI: 10.1371/journal.pone.0141347. https://pubmed.ncbi.nlm.nih.gov/26496426/
- **bridoux-2021-localization-review**: Bridoux L, Gofflot F, Rezsohazy R (2021). HOX Protein Activity Regulation by Cellular Localization. *Journal of Developmental Biology* 9(4):56. PMID: 34940503; PMCID: PMC8707151; DOI: 10.3390/jdb9040056. https://pubmed.ncbi.nlm.nih.gov/34940503/
- **brown-2013-haploinsufficiency**: Brown KK, Viana LM, Helwig CC et al. (2013). HOXA2 haploinsufficiency in dominant bilateral microtia and hearing loss. *Human Mutation* 34:1347-51. PMID: 23775976; PMCID: PMC3883620; DOI: 10.1002/humu.22367. https://pubmed.ncbi.nlm.nih.gov/23775976/
- **deneyer-2019-cytoplasmic**: Deneyer N, Bridoux L, Bombled C et al. (2019). HOXA2 activity regulation by cytoplasmic relocation, protein stabilization and post-translational modification. *Biochimica et Biophysica Acta – Gene Regulatory Mechanisms* 1862:194404. PMID: 31323436; DOI: 10.1016/j.bbagrm.2019.07.005. https://pubmed.ncbi.nlm.nih.gov/31323436/
- **donaldson-2012-chipseq-wnt**: Donaldson IJ, Amin S, Hensman JJ et al. (2012). Genome-wide occupancy links Hoxa2 to Wnt-β-catenin signaling in mouse embryonic development. *Nucleic Acids Research* 40:3990-4001. PMID: 22223247; PMCID: PMC3351182; DOI: 10.1093/nar/gkr1240. https://pubmed.ncbi.nlm.nih.gov/22223247/
- **geisen-2008-pontine**: Geisen MJ, Di Meglio T, Pasqualetti M et al. (2008). Hox paralog group 2 genes control the migration of mouse pontine neurons through slit-robo signaling. *PLoS Biology* 6:e142. PMID: 18547144; PMCID: PMC2422855; DOI: 10.1371/journal.pbio.0060142. https://pubmed.ncbi.nlm.nih.gov/18547144/
- **gendronmaguire-1993-homeotic**: Gendron-Maguire M, Mallo M, Zhang M et al. (1993). Hoxa-2 mutant mice exhibit homeotic transformation of skeletal elements derived from cranial neural crest. *Cell* 75:1317-31. PMID: 7903600; DOI: 10.1016/0092-8674(93)90619-2. https://pubmed.ncbi.nlm.nih.gov/7903600/
- **grammatopoulos-2000-overexpression**: Grammatopoulos GA, Bell E, Toole L et al. (2000). Homeotic transformation of branchial arch identity after Hoxa2 overexpression. *Development* 127:5355-65. PMID: 11076757; DOI: 10.1242/dev.127.24.5355. https://pubmed.ncbi.nlm.nih.gov/11076757/
- **hunter-2002-zebrafish**: Hunter MP, Prince VE (2002). Zebrafish hox paralogue group 2 genes function redundantly as selector genes to pattern the second pharyngeal arch. *Developmental Biology* 247:367-89. PMID: 12086473; DOI: 10.1006/dbio.2002.0701. https://pubmed.ncbi.nlm.nih.gov/12086473/
- **kanzler-1998-chondrogenic**: Kanzler B, Kuschert SJ, Liu YH et al. (1998). Hoxa-2 restricts the chondrogenic domain and inhibits bone formation during development of the branchial area. *Development* 125:2587-97. PMID: 9636074; DOI: 10.1242/dev.125.14.2587. https://pubmed.ncbi.nlm.nih.gov/9636074/
- **kessler-2023-superenhancer**: Kessler S, Minoux M, Joshi O et al. (2023). A multiple super-enhancer region establishes inter-TAD interactions and controls Hoxa function in cranial neural crest. *Nature Communications* 14:3242. PMID: 37277355; PMCID: PMC10241789; DOI: 10.1038/s41467-023-38953-0. https://pubmed.ncbi.nlm.nih.gov/37277355/
- **kirilenko-2011-meox1**: Kirilenko P, He G, Mankoo BS et al. (2011). Transient activation of meox1 is an early component of the gene regulatory network downstream of hoxa2. *Molecular and Cellular Biology* 31:1301-8. PMID: 21245383; PMCID: PMC3067911; DOI: 10.1128/MCB.00705-10. https://pubmed.ncbi.nlm.nih.gov/21245383/
- **kitazawa-2022-ectopic**: Kitazawa T, Minoux M, Ducret S et al. (2022). Different Ectopic Hoxa2 Expression Levels in Mouse Cranial Neural Crest Cells Result in Distinct Craniofacial Anomalies and Homeotic Phenotypes. *Journal of Developmental Biology* 10(1):9. PMID: 35225962; PMCID: PMC8883995; DOI: 10.3390/jdb10010009. https://pubmed.ncbi.nlm.nih.gov/35225962/
- **kutejova-2005-six2**: Kutejova E, Engist B, Mallo M et al. (2005). Hoxa2 downregulates Six2 in the neural crest-derived mesenchyme. *Development* 132:469-78. PMID: 15634706; DOI: 10.1242/dev.01536. https://pubmed.ncbi.nlm.nih.gov/15634706/
- **kutejova-2008-six2**: Kutejova E, Engist B, Self M et al. (2008). Six2 functions redundantly immediately downstream of Hoxa2. *Development* 135:1463-70. PMID: 18321982; DOI: 10.1242/dev.017624. https://pubmed.ncbi.nlm.nih.gov/18321982/
- **lampe-2004-autoregulation**: Lampe X, Picard JJ, Rezsohazy R (2004). The Hoxa2 enhancer 2 contains a critical Hoxa2 responsive regulatory element. *Biochemical and Biophysical Research Communications* 316:898-902. PMID: 15033486; DOI: 10.1016/j.bbrc.2004.02.138. https://pubmed.ncbi.nlm.nih.gov/15033486/
- **maconochie-1999-ap2**: Maconochie M, Krishnamurthy R, Nonchev S et al. (1999). Regulation of Hoxa2 in cranial neural crest cells involves members of the AP-2 family. *Development* 126:1483-94. PMID: 10068641; DOI: 10.1242/dev.126.7.1483. https://pubmed.ncbi.nlm.nih.gov/10068641/
- **marchese-2025-dimerization**: Marchese D, Evrard L, Bergiers I et al. (2025). Homeodomain Involvement in Nuclear HOX Protein Homo- and Heterodimerization. *International Journal of Molecular Sciences* 26(1):423. PMID: 39796276; PMCID: PMC11721573; DOI: 10.3390/ijms26010423. https://pubmed.ncbi.nlm.nih.gov/39796276/
- **massip-2007-chondrogenesis**: Massip L, Ectors F, Deprez P et al. (2007). Expression of Hoxa2 in cells entering chondrogenesis impairs overall cartilage development. *Differentiation* 75:256-67. PMID: 17359301; DOI: 10.1111/j.1432-0436.2006.00132.x. https://pubmed.ncbi.nlm.nih.gov/17359301/
- **minoux-2009-groundpattern**: Minoux M, Antonarakis GS, Kmita M et al. (2009). Rostral and caudal pharyngeal arches share a common neural crest ground pattern. *Development* 136:637-45. PMID: 19168678; PMCID: PMC4482666; DOI: 10.1242/dev.028621. https://pubmed.ncbi.nlm.nih.gov/19168678/
- **minoux-2013-auricle**: Minoux M, Kratochwil CF, Ducret S et al. (2013). Mouse Hoxa2 mutations provide a model for microtia and auricle duplication. *Development* 140:4386-97. PMID: 24067355; DOI: 10.1242/dev.098046. https://pubmed.ncbi.nlm.nih.gov/24067355/
- **minoux-2017-bivalency**: Minoux M, Holwerda S, Vitobello A et al. (2017). Gene bivalency at Polycomb domains regulates cranial neural crest positional identity. *Science* 355(6332). PMID: 28360266; DOI: 10.1126/science.aal2913. https://pubmed.ncbi.nlm.nih.gov/28360266/
- **monks-2010-microtia**: Monks DC, Jahangir A, Shanske AL et al. (2010). Mutational analysis of HOXA2 and SIX2 in a Bronx population with isolated microtia. *International Journal of Pediatric Otorhinolaryngology* 74:878-82. PMID: 20542577; DOI: 10.1016/j.ijporl.2010.05.004. https://pubmed.ncbi.nlm.nih.gov/20542577/
- **nonchev-1996-krox20**: Nonchev S, Vesque C, Maconochie M et al. (1996). Segmental expression of Hoxa-2 in the hindbrain is directly regulated by Krox-20. *Development* 122:543-54. PMID: 8625806; DOI: 10.1242/dev.122.2.543. https://pubmed.ncbi.nlm.nih.gov/8625806/
- **parker-2019-hoxtale**: Parker HJ, De Kumar B, Green SA et al. (2019). A Hox-TALE regulatory circuit for neural crest patterning is conserved across vertebrates. *Nature Communications* 10:1189. PMID: 30867425; PMCID: PMC6416258; DOI: 10.1038/s41467-019-09197-8. https://pubmed.ncbi.nlm.nih.gov/30867425/
- **pasqualetti-2000-xenopus**: Pasqualetti M, Ori M, Nardi I et al. (2000). Ectopic Hoxa2 induction after neural crest migration results in homeosis of jaw elements in Xenopus. *Development* 127:5367-78. PMID: 11076758; DOI: 10.1242/dev.127.24.5367. https://pubmed.ncbi.nlm.nih.gov/11076758/
- **pasqualetti-2007-fatemap**: Pasqualetti M, Díaz C, Renaud JS, Rijli FM, Glover JC (2007). Fate-mapping the mammalian hindbrain: segmental origins of vestibular projection neurons assessed using rhombomere-specific Hoxa2 enhancer elements in the mouse embryo. *Journal of Neuroscience* 27:9670-81. PMID: 17804628; PMCID: PMC6672974; DOI: 10.1523/JNEUROSCI.2189-07.2007. https://pubmed.ncbi.nlm.nih.gov/17804628/
- **piceci-2017-microtia**: Piceci F, Morlino S, Castori M et al. (2017). Identification of a second HOXA2 nonsense mutation in a family with autosomal dominant non-syndromic microtia and distinctive ear morphology. *Clinical Genetics* 91:774-779. PMID: 27503514; DOI: 10.1111/cge.12845. https://pubmed.ncbi.nlm.nih.gov/27503514/
- **rijli-1993-selector**: Rijli FM, Mark M, Lakkaraju S et al. (1993). A homeotic transformation is generated in the rostral branchial region of the head by disruption of Hoxa-2, which acts as a selector gene. *Cell* 75:1333-49. PMID: 7903601; DOI: 10.1016/0092-8674(93)90620-6. https://pubmed.ncbi.nlm.nih.gov/7903601/
- **rosin-2016-hmx1**: Rosin JM, Li W, Cox LL et al. (2016). A distal 594 bp ECR specifies Hmx1 expression in pinna and lateral facial morphogenesis and is regulated by the Hox-Pbx-Meis complex. *Development* 143:2582-92. PMID: 27287804; PMCID: PMC4958336; DOI: 10.1242/dev.133736. https://pubmed.ncbi.nlm.nih.gov/27287804/
- **santagati-2005-temporal**: Santagati F, Minoux M, Ren SY et al. (2005). Temporal requirement of Hoxa2 in cranial neural crest skeletal morphogenesis. *Development* 132:4927-36. PMID: 16221728; DOI: 10.1242/dev.02078. https://pubmed.ncbi.nlm.nih.gov/16221728/
- **trainor-2001-review**: Trainor PA, Krumlauf R (2001). Hox genes, neural crest cells and branchial arch patterning. *Current Opinion in Cell Biology* 13:698-705. PMID: 11698185; DOI: 10.1016/s0955-0674(00)00273-8. https://pubmed.ncbi.nlm.nih.gov/11698185/
- **tumpel-2007-r4**: Tümpel S, Cambronero F, Ferretti E et al. (2007). Expression of Hoxa2 in rhombomere 4 is regulated by a conserved cross-regulatory mechanism dependent upon Hoxb1. *Developmental Biology* 302:646-60. PMID: 17113575; DOI: 10.1016/j.ydbio.2006.10.029. https://pubmed.ncbi.nlm.nih.gov/17113575/
- **wang-2020-donkeygenome**: Wang C, Li H, Guo Y et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nature Communications* 11:6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7. https://pubmed.ncbi.nlm.nih.gov/33293529/
- **xu-2025-auricular-cnv**: Xu X, Chen Q, Huang Q et al. (2025). Auricular malformations are driven by copy number variations in a hierarchical enhancer cluster and a dominant enhancer recapitulates human pathogenesis. *Nature Communications* 16:4598. PMID: 40382324; PMCID: PMC12085581; DOI: 10.1038/s41467-025-59735-w. https://pubmed.ncbi.nlm.nih.gov/40382324/
- **yang-2008-facialganglia**: Yang X, Zhou Y, Barcarse EA et al. (2008). Altered neuronal lineages in the facial ganglia of Hoxa2 mutant mice. *Developmental Biology* 314:171-88. PMID: 18164701; DOI: 10.1016/j.ydbio.2007.11.032. https://pubmed.ncbi.nlm.nih.gov/18164701/

Database sources: UniProtKB A0A9L0JBM7 (https://rest.uniprot.org/uniprotkb/A0A9L0JBM7.txt) and P31245 (https://rest.uniprot.org/uniprotkb/P31245.txt), retrieved 2026-10-25 and saved locally as `uniprot_A0A9L0JBM7.txt` and `human_P31245.fasta`.


## Citations

1. alasti-2008-microtia-abstract.md
2. alasti-2008-microtia-summary.md
3. amin-2015-meis-abstract.md
4. amin-2015-meis-fulltext.txt
5. amin-2015-meis-summary.md
6. baltzinger-2005-knockdown-abstract.md
7. baltzinger-2005-knockdown-summary.md
8. bergiers-2013-rchy1-abstract.md
9. bergiers-2013-rchy1-fulltext.txt
10. bergiers-2013-rchy1-summary.md
11. bridoux-2015-kpc2-abstract.md
12. bridoux-2015-kpc2-summary.md
13. bridoux-2015-rchy1-abstract.md
14. bridoux-2015-rchy1-fulltext.txt
15. bridoux-2015-rchy1-summary.md
16. bridoux-2021-localization-review-abstract.md
17. bridoux-2021-localization-review-fulltext.txt
18. bridoux-2021-localization-review-summary.md
19. brown-2013-haploinsufficiency-abstract.md
20. brown-2013-haploinsufficiency-summary.md
21. deneyer-2019-cytoplasmic-abstract.md
22. deneyer-2019-cytoplasmic-summary.md
23. donaldson-2012-chipseq-wnt-abstract.md
24. donaldson-2012-chipseq-wnt-fulltext.txt
25. donaldson-2012-chipseq-wnt-summary.md
26. geisen-2008-pontine-abstract.md
27. geisen-2008-pontine-fulltext.txt
28. geisen-2008-pontine-summary.md
29. gendronmaguire-1993-homeotic-abstract.md
30. gendronmaguire-1993-homeotic-summary.md
31. grammatopoulos-2000-overexpression-abstract.md
32. grammatopoulos-2000-overexpression-summary.md
33. hunter-2002-zebrafish-abstract.md
34. hunter-2002-zebrafish-summary.md
35. kanzler-1998-chondrogenic-abstract.md
36. kanzler-1998-chondrogenic-summary.md
37. kessler-2023-superenhancer-abstract.md
38. kessler-2023-superenhancer-fulltext.txt
39. kessler-2023-superenhancer-summary.md
40. kirilenko-2011-meox1-abstract.md
41. kirilenko-2011-meox1-summary.md
42. kitazawa-2022-ectopic-abstract.md
43. kitazawa-2022-ectopic-fulltext.txt
44. kitazawa-2022-ectopic-summary.md
45. kutejova-2005-six2-abstract.md
46. kutejova-2005-six2-summary.md
47. kutejova-2008-six2-abstract.md
48. kutejova-2008-six2-summary.md
49. lampe-2004-autoregulation-abstract.md
50. lampe-2004-autoregulation-summary.md
51. maconochie-1999-ap2-abstract.md
52. maconochie-1999-ap2-summary.md
53. marchese-2025-dimerization-abstract.md
54. marchese-2025-dimerization-fulltext.txt
55. marchese-2025-dimerization-summary.md
56. massip-2007-chondrogenesis-abstract.md
57. massip-2007-chondrogenesis-summary.md
58. meta.json
59. minoux-2009-groundpattern-abstract.md
60. minoux-2009-groundpattern-summary.md
61. minoux-2013-auricle-abstract.md
62. minoux-2013-auricle-summary.md
63. minoux-2017-bivalency-abstract.md
64. minoux-2017-bivalency-summary.md
65. monks-2010-microtia-abstract.md
66. monks-2010-microtia-summary.md
67. nonchev-1996-krox20-abstract.md
68. nonchev-1996-krox20-summary.md
69. parker-2019-hoxtale-abstract.md
70. parker-2019-hoxtale-fulltext.txt
71. parker-2019-hoxtale-summary.md
72. pasqualetti-2000-xenopus-abstract.md
73. pasqualetti-2000-xenopus-summary.md
74. pasqualetti-2007-fatemap-abstract.md
75. pasqualetti-2007-fatemap-summary.md
76. piceci-2017-microtia-abstract.md
77. piceci-2017-microtia-summary.md
78. rijli-1993-selector-abstract.md
79. rijli-1993-selector-summary.md
80. rosin-2016-hmx1-abstract.md
81. rosin-2016-hmx1-summary.md
82. santagati-2005-temporal-abstract.md
83. santagati-2005-temporal-summary.md
84. trainor-2001-review-abstract.md
85. trainor-2001-review-summary.md
86. tumpel-2007-r4-abstract.md
87. tumpel-2007-r4-summary.md
88. wang-2020-donkeygenome-abstract.md
89. wang-2020-donkeygenome-fulltext.txt
90. wang-2020-donkeygenome-summary.md
91. xu-2025-auricular-cnv-abstract.md
92. xu-2025-auricular-cnv-fulltext.txt
93. xu-2025-auricular-cnv-summary.md
94. yang-2008-facialganglia-abstract.md
95. yang-2008-facialganglia-summary.md