---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:31:21.465485'
end_time: '2026-10-26T02:42:21.227197'
duration_seconds: 659.76
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: DNMT3L
  gene_symbol: DNMT3L
  uniprot_accession: A0A9L0T837
  protein_description: 'SubName: Full=DNA methyltransferase 3 like {ECO:0000313|Ensembl:ENSECAP00000084444.1};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: ADD. (IPR025766); C5-Methyltransferase. (IPR050390); DNMT3_ADD_GATA1-like.
    (IPR040552); DNMT3_ADD_PHD. (IPR049554); SAM-dependent_MTases_sf. (IPR029063)
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
citation_count: 66
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0T837
- **Protein Description:** SubName: Full=DNA methyltransferase 3 like {ECO:0000313|Ensembl:ENSECAP00000084444.1};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** ADD. (IPR025766); C5-Methyltransferase. (IPR050390); DNMT3_ADD_GATA1-like. (IPR040552); DNMT3_ADD_PHD. (IPR049554); SAM-dependent_MTases_sf. (IPR029063)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "DNMT3L" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'DNMT3L' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **DNMT3L** (gene ID: DNMT3L, UniProt: A0A9L0T837) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# DNMT3L (DNA methyltransferase 3-like) in the horse, *Equus caballus* (UniProt A0A9L0T837)

## 1. Introduction and summary

UniProt entry A0A9L0T837 is an unreviewed, computationally predicted 426-residue protein from the Thoroughbred reference genome, named "DNA methyltransferase 3 like" from Ensembl gene ENSECAG00000009690 on horse chromosome 26, with InterPro signatures for an ADD (ATRX-DNMT3-DNMT3L) domain, its GATA1-like and PHD sub-parts, and a SAM-dependent methyltransferase fold [uniprot-A0A9L0T837-entry; wade-2009-horse-genome-abstract]. Identity check: the symbol DNMT3L, the protein description and the domains all agree. My own pairwise alignment found that residues 41-426 of the horse protein are 77.7% identical over their full length to human DNMT3L (Q9UJW3) with no internal gaps, but only 39% identical to human DNMT3A (see `analysis/SEQUENCE_ANALYSIS.md`). The protein is therefore the horse ortholog of DNMT3L, not a catalytically active DNMT3A or DNMT3B paralog.

No published experimental study of DNMT3L function in the horse was found. One equine embryo study designed qPCR assays for equine DNMT3L, but its text reports results only for DNMT1, DNMT3A and DNMT3B [gastal-2021-equine-embryo-methylation-fulltext]. The functional picture below therefore comes from mouse genetics and from biochemical and structural work on mouse and human proteins. It is transferred to the horse on the basis of orthology and conserved sequence.

That picture is consistent. DNMT3L is not an enzyme. It has lost the catalytic motifs of cytosine-C5 DNA methyltransferases [bourchis-2001-dnmt3l-maternal-imprints-abstract; aapola-2002-dnmt3l-repressor-hdac-abstract], and the horse sequence shows the same losses (Section 3). Instead it is a nuclear regulatory cofactor of the de novo methyltransferases DNMT3A and DNMT3B, and it works in two ways. Its C-terminal methyltransferase-like domain binds the catalytic domain of DNMT3A (and DNMT3B), stimulating CpG methylation [suetake-2004-dnmt3l-stimulates-abstract; gowher-2005-mechanism-stimulation-abstract; jia-2007-dnmt3a-dnmt3l-structure-abstract]. Its N-terminal ADD domain reads histone H3 tails that are unmethylated at lysine 4 (H3K4me0) [ooi-2007-dnmt3l-h3k4-abstract]. These activities link chromatin state to de novo DNA methylation in germ cells. There DNMT3L is needed to establish maternal genomic imprints in oocytes [bourchis-2001-dnmt3l-maternal-imprints-abstract; hata-2002-dnmt3l-cooperates-abstract] and to methylate retrotransposons and paternal imprints in fetal prospermatogonia [bourchis-2004-meiotic-catastrophe-abstract; kato-2007-dnmt3-male-germ-abstract].

## 2. Gene identity, domain architecture and evolutionary context

Human DNMT3L was first identified as a DNMT3-related gene on 21q22.3. It encodes a protein of about 387 residues with a cysteine-rich ADD zinc finger, made of a C2C2 part and an imperfect PHD finger, shared with DNMT3A, DNMT3B and ATRX. Its mRNA is scarce and detectable mainly in testis, ovary and thymus [aapola-2000-dnmt3l-cloning-abstract]. The horse protein has the same architecture. PROSITE places its ADD/PHD-type domain at residues 81-213, and the C-terminal part matches the SAM-dependent methyltransferase superfamily [uniprot-A0A9L0T837-entry].

The horse model carries a 40-residue N-terminal extension: horse Met41 aligns with human Met1. This extension is unlikely to be an artefact of the horse gene model. The reviewed mouse protein (Q9CWR8, 421 residues) also extends upstream of the human start, and parts of its N terminus resemble the horse extension (horse "TLSLETLDSWDPD" against mouse "TLETLDLETSDSSSPD"). Overall the horse protein is 66% identical to mouse Dnmt3l (`analysis/SEQUENCE_ANALYSIS.md`). The extension may therefore represent an ancestral mammalian N terminus that the canonical human isoform lacks. No horse transcript evidence was examined to confirm the start codon.

DNMT3L is phylogenetically restricted. Orthologs are found in eutherians and in the marsupial opossum, but not in chicken or fish. This led Yokomine and colleagues to propose that DNMT3L arose in a therian ancestor together with genomic imprinting [yokomine-2006-dnmt3-evolution-abstract]. As a eutherian, the horse is expected to have a functional DNMT3L. In rodents, a further Dnmt3b duplicate, Dnmt3C, took over methylation of young retrotransposon promoters in the male germline [barau-2016-dnmt3c-abstract]. Because Dnmt3C is rodent-specific, horse DNMT3L presumably partners only DNMT3A and DNMT3B. That is an inference, not an observation.

## 3. Loss of catalytic activity: DNMT3L is a pseudo-methyltransferase

The founding knockout papers and later biochemistry all stress that DNMT3L lacks the conserved residues needed for DNA cytosine methyltransferase activity [bourchis-2001-dnmt3l-maternal-imprints-abstract; aapola-2002-dnmt3l-repressor-hdac-abstract; hata-2002-dnmt3l-cooperates-abstract]. Gowher and colleagues found that Dnmt3L does not bind the methyl donor S-adenosyl-L-methionine (AdoMet) [gowher-2005-mechanism-stimulation-abstract]. Guo and colleagues describe DNMT3L as "a catalytically inactive paralogue of DNMT3 enzymes" [guo-2015-dnmt3a-autoinhibition-abstract].

I aligned the horse protein against human DNMT3A to check whether the horse ortholog keeps any catalytic determinants. It does not. The motif I sequence (FDGIATG), which forms the AdoMet-binding loop in DNMT3A, is absent: the alignment opens a gap immediately after the conserved "RVLSLF". The catalytic motif IV (PCN), which supplies the nucleophilic cysteine, is replaced by "GSTP" with no cysteine. Motif VI (ENV) is replaced by "VDN". The region matching the DNMT3A target-recognition domain also aligns to a long gap (`analysis/SEQUENCE_ANALYSIS.md`). UniProt likewise flags that the protein "lacks conserved residue(s) required for the propagation of feature annotation" [uniprot-A0A9L0T837-entry].

These sequence features match the inactive mouse and human proteins. Horse DNMT3L should therefore be annotated as a non-catalytic activator of DNA methyltransferase, not as a DNA (cytosine-5-)-methyltransferase (EC 2.1.1.37). The GO annotations in the entry fit this: "enzyme activator activity" (IBA) and "enzyme binding" (IEA) [uniprot-A0A9L0T837-entry].

## 4. Molecular mechanism: allosteric activation of DNMT3A/DNMT3B

The main molecular function of DNMT3L is to stimulate de novo methyltransferases. In human cells, coexpressing DNMT3L with Dnmt3a strongly increased de novo methylation of episomal imprinting centres (SNRPN, Snrpn, Igf2r/Air), of non-imprinted episomal sequences and of endogenous genomic loci. Chedin and colleagues concluded that DNMT3L is a general, sequence-independent stimulator of Dnmt3a [chedin-2002-dnmt3l-stimulates-dnmt3a-abstract].

In vitro, DNMT3L increased Dnmt3a and Dnmt3b activity on every substrate tested but did not stimulate Dnmt1. The C-terminal half of DNMT3L was sufficient for this, and Suetake and colleagues argued that it acts directly on catalysis rather than by guiding the enzyme to particular sequences [suetake-2004-dnmt3l-stimulates-abstract]. Gowher and colleagues measured about 15-fold stimulation through direct binding of the Dnmt3L C-terminal domain to the catalytic domains of Dnmt3A and Dnmt3B. In the complex, Dnmt3A bound DNA 20-fold faster, had a lower K_m for DNA and AdoMet, and bound AdoMet better. They proposed that Dnmt3L acts as a transient "substrate exchange factor" that opens the active site of Dnmt3A [gowher-2005-mechanism-stimulation-abstract].

The two papers disagree on whether DNMT3L itself binds DNA. Suetake and colleagues saw no DNA binding [suetake-2004-dnmt3l-stimulates-abstract], whereas Gowher and colleagues reported direct DNA binding [gowher-2005-mechanism-stimulation-abstract]. Single-molecule work added a further mechanism: DNMT3L increases the processivity of human DNMT3A on promoter DNA about threefold [holzschietinger-2010-processivity-abstract].

Structural studies explain these effects. The crystal structure of the C-terminal domains of DNMT3A and DNMT3L shows a linear 3L-3a-3a-3L heterotetramer. DNMT3L caps each end, and the central DNMT3A-DNMT3A interface creates two active sites about one DNA helical turn apart. Mutating non-catalytic residues at either the 3a-3L or the 3a-3a interface abolished activity [jia-2007-dnmt3a-dnmt3l-structure-abstract]. Analytical ultracentrifugation confirmed the 2:2 stoichiometry in solution. The 3a-3a interface forms the DNA-binding site, both interfaces are needed for AdoMet binding and catalysis, and the tetramers multimerize along DNA into nucleoprotein filaments that produce correlated methylation of CpGs 8-10 bp apart [jurkowska-2008-nucleoprotein-filaments-abstract].

Later structures added DNA and histone tails. In the DNMT3A-DNMT3L-DNA complex, the two DNMT3A subunits attack two CpGs 14 bp apart, and CpG specificity comes from the DNMT3A target-recognition domain (Arg836) and catalytic loop. DNMT3L stabilizes the tetramer at its ends and does not contact the target cytosines [zhang-2018-dnmt3a-structure-abstract; zhang-2018-dnmt3a-structure-fulltext]. The substrate specificity of the DNMT3L-containing complex (cytosine at CpG and, in oocytes, also non-CpG sites) is therefore set by its catalytic partner. DNMT3L contributes allosteric activation, stability and processivity.

## 5. Chromatin reading: the ADD domain and unmethylated H3K4

The second key activity of DNMT3L is reading histone modifications. When epitope-tagged endogenous Dnmt3L was purified from mouse cells, its main partners were DNMT3A2, DNMT3B and the four core histones. Peptide assays showed that DNMT3L binds the extreme N terminus of histone H3. Methylation at H3K4 strongly inhibited this binding, but modifications at other positions did not. Crystal structures of human DNMT3L showed the H3 tail bound to the N-terminal cysteine-rich ADD domain, and mutating that binding site abolished binding [ooi-2007-dnmt3l-h3k4-abstract]. Ooi and colleagues proposed that DNMT3L recognizes H3K4me0 and directs de novo methylation by recruiting or activating DNMT3A2 [ooi-2007-dnmt3l-h3k4-abstract].

Genetic evidence later showed that this histone-reading activity matters in vivo. A single amino-acid substitution in the mouse Dnmt3L ADD, D124A, abolishes histone H3 binding without changing expression of Dnmt3 complex components. When knocked into the endogenous locus, it impaired spermatogenesis. Prospermatogonia from these mice lost CG methylation at repeats and non-promoter CpG islands, lost non-CG methylation even more severely, and reactivated retrotransposons [vlachogiannis-2015-dnmt3l-add-spermatogenesis-abstract; vlachogiannis-2015-dnmt3l-add-spermatogenesis-fulltext]. This aspartate is conserved in the horse protein as Asp130, within an identical "LFLYDDDG(N/H)QSYC" motif (`analysis/SEQUENCE_ANALYSIS.md`). The H3K4me0-reading surface is therefore predicted to be intact in horse DNMT3L.

Jia and colleagues then described DNMT3L as having "dual functions": binding the unmethylated histone tail and activating the methyltransferase [jia-2007-dnmt3a-dnmt3l-structure-abstract]. DNMT3A has its own H3K4me0-reading ADD domain, which autoinhibits its catalytic domain until an unmethylated H3 tail binds. This release happens independently of DNMT3L [guo-2015-dnmt3a-autoinhibition-abstract]. DNMT3L's chromatin reading therefore reinforces a targeting logic built into DNMT3A itself, so that de novo methylation is directed away from H3K4-methylated active promoters [guo-2015-dnmt3a-autoinhibition-abstract; ooi-2007-dnmt3l-h3k4-abstract].

Earlier work reported a separate repressor activity. Tethered DNMT3L repressed transcription by binding HDAC1 through the PHD-like part of its ADD domain [aapola-2002-dnmt3l-repressor-hdac-abstract]. This was shown in reporter assays, and its physiological importance is still unclear.

## 6. Subcellular localization

All evidence places DNMT3L in the nucleus, on chromatin. Human DNMT3L has a functional nuclear localization signal at residues 156-159 [aapola-2002-dnmt3l-repressor-hdac-abstract]. Mouse Dnmt3L colocalizes with Dnmt3a and Dnmt3b in the nuclei of transfected cells [hata-2002-dnmt3l-cooperates-abstract], and endogenous Dnmt3L co-purifies with core histones [ooi-2007-dnmt3l-h3k4-abstract]. In the horse protein the matching residues (196-199 by the alignment offset) are the same basic motif, RRRK, as the human NLS, inside a conserved "RSGLLQRRRKW" stretch (`analysis/SEQUENCE_ANALYSIS.md`). UniProt annotates the horse protein as nuclear [uniprot-A0A9L0T837-entry].

For the horse there is no protein-level localization data, but bulk RNA-seq expression calls exist. Bgee records horse DNMT3L transcripts in leukocytes and blood, skin, bone marrow, chorionic villus (placenta), synovial membrane, skeletal muscle and testis, with lower-confidence calls in bronchial epithelium and kidney [bgee-ENSECAG00000009690-expression; bgee-ENSECAG00000009690-summary]. The fetal gonads and growing oocytes where DNMT3L acts in mouse are not represented. The somatic signals, including the placental chorionic villus, are low-level calls whose functional meaning in the horse is unknown.

The entry also carries electronically inferred GO terms that fit this picture: condensed nuclear chromosome, heterochromatin and ESC/E(Z) complex. The last is consistent with the Dnmt3L-PRC2 interaction described in ES cells [neri-2013-dnmt3l-bivalent-abstract]. A phylogenetically inferred "cytoplasm" term [uniprot-A0A9L0T837-entry] has no direct experimental support in the literature reviewed here.

## 7. Biological roles: germline imprinting, transposon silencing and pluripotent cells

DNMT3L's physiological function is concentrated in the germline. Two independent mouse knockouts showed it is essential for establishing maternal methylation imprints. Oocytes lacking Dnmt3L do not methylate maternally methylated imprinted sequences. As a result, embryos derived from these oocytes express normally paternal-only genes from both alleles and die before midgestation, while global methylation levels are largely unaffected [bourchis-2001-dnmt3l-maternal-imprints-abstract; hata-2002-dnmt3l-cooperates-abstract]. Dnmt3a-/-;Dnmt3b+/- females have a similar imprinting defect, which places Dnmt3L in the same pathway as the Dnmt3 enzymes [hata-2002-dnmt3l-cooperates-abstract].

In oocytes, Dnmt3L transcripts peak together with Dnmt3a, Dnmt3b and Dnmt1o during postnatal oocyte growth, when imprints are set [lucifero-2007-oogenesis-dnmt-abstract]. Methylome studies extended this picture. Dnmt3L is needed for methylation of most oocyte germline DMRs and for the transcription-coupled intragenic methylation typical of oocytes [kobayashi-2012-gametic-methylomes-abstract]. Loss of Dnmt3a or Dnmt3L, but not Dnmt3b, globally reduces both CG and the abundant non-CG methylation of oocytes, showing that oocyte methylation depends on the Dnmt3a-Dnmt3L complex [shirane-2013-oocyte-methylomes-abstract].

In the male germline, Dnmt3L is expressed briefly in perinatal, non-dividing prospermatogonia, co-expressed with the short Dnmt3a2 isoform [sakai-2004-gonocyte-coexpression-abstract; bourchis-2004-meiotic-catastrophe-abstract]. Without it, LTR and non-LTR retrotransposons are not methylated de novo and are strongly transcribed. Spermatocytes then fail in meiosis even though they no longer express Dnmt3L, causing azoospermia [bourchis-2004-meiotic-catastrophe-abstract; bourchis-2001-dnmt3l-maternal-imprints-abstract]. Paternal DMRs (H19, Dlk1/Gtl2, Rasgrf1), interspersed repeats and satellite repeats are all hypomethylated in Dnmt3L-deficient prospermatogonia, so Dnmt3L acts broadly with both Dnmt3a and Dnmt3b [kato-2007-dnmt3-male-germ-abstract]. By contrast, IAP and LINE-1 methylation is normal in Dnmt3L-null oocytes. This indicates that DNMT3L's role in silencing repeats is specific to the male germline [lucifero-2007-oogenesis-dnmt-abstract].

The horse entry carries an Ensembl-projected annotation to "transposable element silencing by piRNA-mediated DNA methylation" [uniprot-A0A9L0T837-entry]. This is consistent with the male-germline phenotype, but no data on the equine piRNA pathway were found.

Outside the germline, Dnmt3L is highly expressed in mouse ES cells, where it acts in more than one direction. It promotes gene-body methylation of housekeeping genes, but restrains methylation at bivalent, H3K27me3-marked promoters by competing with Dnmt3a/3b for the PRC2 complex. It is also needed for ES-cell differentiation into primordial germ cells [neri-2013-dnmt3l-bivalent-abstract]. Veland and colleagues disputed this model. In their DNMT3L-deficient ES cells, DNMT3A protein, especially DNMT3A2, was reduced and many DNMT3A target regions were hypomethylated. DNMT3L bound DNMT3A2 and prevented its degradation, and restoring DNMT3A partly rescued methylation. They concluded that DNMT3L is a positive regulator, acting in part by stabilizing its catalytic partner [veland-2019-dnmt3l-dnmt3a-stability-abstract]. They also emphasized that, genetically, DNMT3L is essential for DNMT3A-mediated germline methylation but dispensable for the largely DNMT3B-driven methylation of the embryo proper [veland-2019-dnmt3l-dnmt3a-stability-abstract]. Taken together, the best-supported view is that DNMT3L chiefly enables DNMT3A, and that any repressive effects at particular loci depend on context.

DNMT3L has also been reported to act beyond the fetal window in the male germline. In postnatal mouse testis, DNMT3L is expressed in THY1+ spermatogonial stem/progenitor cells. Its loss destabilizes PLZF, linked to raised CDK2; this releases SALL4A, with overactivated ERK and AKT signalling, and leads to premature exhaustion of the stem-cell pool [liao-2014-dnmt3l-spermatogonial-quiescence-abstract]. The route from a chromatin cofactor to these signalling changes is indirect and has not been worked out.

## 8. Relevance to the horse and functional annotation summary

The horse protein is a full-length DNMT3L ortholog, conserved with human DNMT3L across the ADD domain and the methyltransferase-like domain, and it carries the same catalytic-motif losses. On that basis, A0A9L0T837 can be annotated with high confidence as follows. Its molecular function is non-catalytic activation of DNA (cytosine-5)-methyltransferases DNMT3A/DNMT3B, through direct binding of its C-terminal domain to their catalytic domains, together with binding of histone H3 tails unmethylated at K4 through its ADD domain. It acts in the nucleus, on chromatin. Its biological processes are de novo DNA methylation, establishment of genomic imprints (especially maternal imprints in oocytes), and DNA-methylation-dependent silencing of retrotransposons in fetal male germ cells, required for spermatogenesis and meiosis [bourchis-2001-dnmt3l-maternal-imprints-abstract; hata-2002-dnmt3l-cooperates-abstract; bourchis-2004-meiotic-catastrophe-abstract; ooi-2007-dnmt3l-h3k4-abstract; jia-2007-dnmt3a-dnmt3l-structure-abstract]. Two features support transferring these annotations. The horse protein keeps the ADD aspartate needed for H3 binding in vivo [vlachogiannis-2015-dnmt3l-add-spermatogenesis-abstract], and it keeps the conserved NLS motif. In addition, DNMT3L's role in stabilizing DNMT3A2 [veland-2019-dnmt3l-dnmt3a-stability-abstract] supports a more general annotation as a positive regulator of DNA methylation.

It should not be annotated as having DNA methyltransferase catalytic activity. Horse-specific aspects remain unstudied, including expression timing in equine gametogenesis, imprint establishment in mares and stallions, and the role of the N-terminal extension in the gene model. The only equine study touching DNMT3L included it in a qPCR panel without reporting a result [gastal-2021-equine-embryo-methylation-fulltext].

## 9. Open Questions

The most basic open question is which start codon horse DNMT3L uses in vivo. The 40-residue N-terminal extension resembles the longer mouse N terminus, but equine gonadal RNA-seq or 5' RACE is needed to confirm it and to test whether the extension affects localization or interactions. A related question is whether the low-level somatic expression that Bgee records in horse blood, skin, placenta and muscle [bgee-ENSECAG00000009690-summary] reflects functional protein.

A second question is when and where DNMT3L is expressed during equine gametogenesis. Horse folliculogenesis and seasonal spermatogenesis differ markedly from those of mice. Single-cell or staged transcriptomics of fetal and neonatal equine gonads and of growing oocytes would test whether the mouse timing (perinatal prospermatogonia; growing oocytes) holds.

A third concerns imprinting. The horse is unusual among mammals because the mule and hinny reciprocal crosses give natural parent-of-origin comparisons. Which maternal germline DMRs in the horse depend on DNMT3L, and how closely they match the mouse set [kobayashi-2012-gametic-methylomes-abstract], is unknown. Oocyte methylomes from horse could answer this.

Because rodents have the extra enzyme DNMT3C for retrotransposon promoters [barau-2016-dnmt3c-abstract], the horse male germline may rely more heavily on DNMT3L-DNMT3A/B for transposon silencing. Testing this would require equine germ-cell methylomes or, eventually, gene-edited models.

The reported HDAC1-dependent co-repressor activity [aapola-2002-dnmt3l-repressor-hdac-abstract] and the PRC2 competition model in ES cells [neri-2013-dnmt3l-bivalent-abstract] have not been examined outside mouse and human systems. Their relevance to equine embryos and to equine induced pluripotent stem cells is open.

Finally, the published biochemistry disagrees on whether DNMT3L itself binds DNA [suetake-2004-dnmt3l-stimulates-abstract; gowher-2005-mechanism-stimulation-abstract], and this remains to be resolved. So does the conflict between the PRC2-competition model, in which DNMT3L restrains methylation at bivalent promoters in ES cells [neri-2013-dnmt3l-bivalent-abstract], and the DNMT3A-stabilization model [veland-2019-dnmt3l-dnmt3a-stability-abstract]. Mechanistically, it is also unclear how a chromatin cofactor controls PLZF and CDK2 levels in postnatal spermatogonia [liao-2014-dnmt3l-spermatogonial-quiescence-abstract].

## 10. References

- **uniprot-A0A9L0T837**: UniProtKB/TrEMBL entry A0A9L0T837_HORSE, "DNA methyltransferase 3 like", entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0T837.txt (local copy: citations/uniprot-A0A9L0T837-entry.txt). Ensembl ENSECAG00000009690 / ENSECAP00000084444.1.
- **bgee-ENSECAG00000009690**: Bgee gene expression calls for horse DNMT3L (ENSECAG00000009690), retrieved 2026-10-26 from https://www.bgee.org/api/?page=gene&action=expression&gene_id=ENSECAG00000009690&species_id=9796&cond_param=anat_entity&data_type=all&display_type=json (local copy: citations/bgee-ENSECAG00000009690-expression.json).
- **aapola-2000-dnmt3l-cloning**: Aapola U, Kawasaki K, Scott HS et al. (2000). Isolation and initial characterization of a novel zinc finger gene, DNMT3L, on 21q22.3, related to the cytosine-5-methyltransferase 3 gene family. *Genomics* 65:293-8. PMID: 10857753; DOI: 10.1006/geno.2000.6168. https://pubmed.ncbi.nlm.nih.gov/10857753/
- **aapola-2002-dnmt3l-repressor-hdac**: Aapola U, Liiv I, Peterson P (2002). Imprinting regulator DNMT3L is a transcriptional repressor associated with histone deacetylase activity. *Nucleic Acids Res* 30:3602-8. PMID: 12177302; DOI: 10.1093/nar/gkf474; PMCID: PMC134241. https://pubmed.ncbi.nlm.nih.gov/12177302/
- **barau-2016-dnmt3c**: Barau J, Teissandier A, Zamudio N et al. (2016). The DNA methyltransferase DNMT3C protects male germ cells from transposon activity. *Science* 354:909-912. PMID: 27856912; DOI: 10.1126/science.aah5143. https://pubmed.ncbi.nlm.nih.gov/27856912/
- **bourchis-2001-dnmt3l-maternal-imprints**: Bourc'his D, Xu GL, Lin CS et al. (2001). Dnmt3L and the establishment of maternal genomic imprints. *Science* 294:2536-9. PMID: 11719692; DOI: 10.1126/science.1065848. https://pubmed.ncbi.nlm.nih.gov/11719692/
- **bourchis-2004-meiotic-catastrophe**: Bourc'his D, Bestor TH (2004). Meiotic catastrophe and retrotransposon reactivation in male germ cells lacking Dnmt3L. *Nature* 431:96-9. PMID: 15318244; DOI: 10.1038/nature02886. https://pubmed.ncbi.nlm.nih.gov/15318244/
- **chedin-2002-dnmt3l-stimulates-dnmt3a**: Chedin F, Lieber MR, Hsieh CL (2002). The DNA methyltransferase-like protein DNMT3L stimulates de novo methylation by Dnmt3a. *Proc Natl Acad Sci U S A* 99:16916-21. PMID: 12481029; DOI: 10.1073/pnas.262443999; PMCID: PMC139244. https://pubmed.ncbi.nlm.nih.gov/12481029/
- **gastal-2021-equine-embryo-methylation**: Gastal GDA, Scarlet D, Melchert M et al. (2021). Epigenetic Changes in Equine Embryos after Short-Term Storage at Different Temperatures. *Animals (Basel)* 11:1325. PMID: 34066466; DOI: 10.3390/ani11051325; PMCID: PMC8148113. https://pubmed.ncbi.nlm.nih.gov/34066466/
- **gowher-2005-mechanism-stimulation**: Gowher H, Liebert K, Hermann A et al. (2005). Mechanism of stimulation of catalytic activity of Dnmt3A and Dnmt3B DNA-(cytosine-C5)-methyltransferases by Dnmt3L. *J Biol Chem* 280:13341-8. PMID: 15671018; DOI: 10.1074/jbc.M413412200. https://pubmed.ncbi.nlm.nih.gov/15671018/
- **guo-2015-dnmt3a-autoinhibition**: Guo X, Wang L, Li J et al. (2015). Structural insight into autoinhibition and histone H3-induced activation of DNMT3A. *Nature* 517:640-4. PMID: 25383530; DOI: 10.1038/nature13899. https://pubmed.ncbi.nlm.nih.gov/25383530/
- **hata-2002-dnmt3l-cooperates**: Hata K, Okano M, Lei H et al. (2002). Dnmt3L cooperates with the Dnmt3 family of de novo DNA methyltransferases to establish maternal imprints in mice. *Development* 129:1983-93. PMID: 11934864; DOI: 10.1242/dev.129.8.1983. https://pubmed.ncbi.nlm.nih.gov/11934864/
- **holzschietinger-2010-processivity**: Holz-Schietinger C, Reich NO (2010). The inherent processivity of the human de novo methyltransferase 3A (DNMT3A) is enhanced by DNMT3L. *J Biol Chem* 285:29091-100. PMID: 20630873; DOI: 10.1074/jbc.M110.142513; PMCID: PMC2937940. https://pubmed.ncbi.nlm.nih.gov/20630873/
- **jia-2007-dnmt3a-dnmt3l-structure**: Jia D, Jurkowska RZ, Zhang X et al. (2007). Structure of Dnmt3a bound to Dnmt3L suggests a model for de novo DNA methylation. *Nature* 449:248-51. PMID: 17713477; DOI: 10.1038/nature06146; PMCID: PMC2712830. https://pubmed.ncbi.nlm.nih.gov/17713477/
- **jurkowska-2008-nucleoprotein-filaments**: Jurkowska RZ, Anspach N, Urbanke C et al. (2008). Formation of nucleoprotein filaments by mammalian DNA methyltransferase Dnmt3a in complex with regulator Dnmt3L. *Nucleic Acids Res* 36:6656-63. PMID: 18945701; DOI: 10.1093/nar/gkn747; PMCID: PMC2588524. https://pubmed.ncbi.nlm.nih.gov/18945701/
- **kato-2007-dnmt3-male-germ**: Kato Y, Kaneda M, Hata K et al. (2007). Role of the Dnmt3 family in de novo methylation of imprinted and repetitive sequences during male germ cell development in the mouse. *Hum Mol Genet* 16:2272-80. PMID: 17616512; DOI: 10.1093/hmg/ddm179. https://pubmed.ncbi.nlm.nih.gov/17616512/
- **kobayashi-2012-gametic-methylomes**: Kobayashi H, Sakurai T, Imai M et al. (2012). Contribution of intragenic DNA methylation in mouse gametic DNA methylomes to establish oocyte-specific heritable marks. *PLoS Genet* 8:e1002440. PMID: 22242016; DOI: 10.1371/journal.pgen.1002440; PMCID: PMC3252278. https://pubmed.ncbi.nlm.nih.gov/22242016/
- **liao-2014-dnmt3l-spermatogonial-quiescence**: Liao HF, Chen WS, Chen YH et al. (2014). DNMT3L promotes quiescence in postnatal spermatogonial progenitor cells. *Development* 141:2402-13. PMID: 24850856; DOI: 10.1242/dev.105130. https://pubmed.ncbi.nlm.nih.gov/24850856/
- **lucifero-2007-oogenesis-dnmt**: Lucifero D, La Salle S, Bourc'his D et al. (2007). Coordinate regulation of DNA methyltransferase expression during oogenesis. *BMC Dev Biol* 7:36. PMID: 17445268; DOI: 10.1186/1471-213X-7-36; PMCID: PMC1878483. https://pubmed.ncbi.nlm.nih.gov/17445268/
- **neri-2013-dnmt3l-bivalent**: Neri F, Krepelova A, Incarnato D et al. (2013). Dnmt3L antagonizes DNA methylation at bivalent promoters and favors DNA methylation at gene bodies in ESCs. *Cell* 155:121-34. PMID: 24074865; DOI: 10.1016/j.cell.2013.08.056. https://pubmed.ncbi.nlm.nih.gov/24074865/
- **ooi-2007-dnmt3l-h3k4**: Ooi SK, Qiu C, Bernstein E et al. (2007). DNMT3L connects unmethylated lysine 4 of histone H3 to de novo methylation of DNA. *Nature* 448:714-7. PMID: 17687327; DOI: 10.1038/nature05987; PMCID: PMC2650820. https://pubmed.ncbi.nlm.nih.gov/17687327/
- **sakai-2004-gonocyte-coexpression**: Sakai Y, Suetake I, Shinozaki F et al. (2004). Co-expression of de novo DNA methyltransferases Dnmt3a2 and Dnmt3L in gonocytes of mouse embryos. *Gene Expr Patterns* 5:231-7. PMID: 15567719; DOI: 10.1016/j.modgep.2004.07.011. https://pubmed.ncbi.nlm.nih.gov/15567719/
- **shirane-2013-oocyte-methylomes**: Shirane K, Toh H, Kobayashi H et al. (2013). Mouse oocyte methylomes at base resolution reveal genome-wide accumulation of non-CpG methylation and role of DNA methyltransferases. *PLoS Genet* 9:e1003439. PMID: 23637617; DOI: 10.1371/journal.pgen.1003439; PMCID: PMC3630097. https://pubmed.ncbi.nlm.nih.gov/23637617/
- **suetake-2004-dnmt3l-stimulates**: Suetake I, Shinozaki F, Miyagawa J et al. (2004). DNMT3L stimulates the DNA methylation activity of Dnmt3a and Dnmt3b through a direct interaction. *J Biol Chem* 279:27816-23. PMID: 15105426; DOI: 10.1074/jbc.M400181200. https://pubmed.ncbi.nlm.nih.gov/15105426/
- **veland-2019-dnmt3l-dnmt3a-stability**: Veland N, Lu Y, Hardikar S et al. (2019). DNMT3L facilitates DNA methylation partly by maintaining DNMT3A stability in mouse embryonic stem cells. *Nucleic Acids Res* 47:152-167. PMID: 30321403; DOI: 10.1093/nar/gky947; PMCID: PMC6326784. https://pubmed.ncbi.nlm.nih.gov/30321403/
- **vlachogiannis-2015-dnmt3l-add-spermatogenesis**: Vlachogiannis G, Niederhuth CE, Tuna S et al. (2015). The Dnmt3L ADD Domain Controls Cytosine Methylation Establishment during Spermatogenesis. *Cell Rep* 10:944-956. PMID: 25683717; DOI: 10.1016/j.celrep.2015.01.021; PMCID: PMC4534369. https://pubmed.ncbi.nlm.nih.gov/25683717/
- **wade-2009-horse-genome**: Wade CM, Giulotto E, Sigurdsson S et al. (2009). Genome sequence, comparative analysis, and population genetics of the domestic horse. *Science* 326:865-7. PMID: 19892987; DOI: 10.1126/science.1178158; PMCID: PMC3785132. https://pubmed.ncbi.nlm.nih.gov/19892987/
- **yokomine-2006-dnmt3-evolution**: Yokomine T, Hata K, Tsudzuki M et al. (2006). Evolution of the vertebrate DNMT3 gene family: a possible link between existence of DNMT3L and genomic imprinting. *Cytogenet Genome Res* 113:75-80. PMID: 16575165; DOI: 10.1159/000090817. https://pubmed.ncbi.nlm.nih.gov/16575165/
- **zhang-2018-dnmt3a-structure**: Zhang ZM, Lu R, Wang P et al. (2018). Structural basis for DNMT3A-mediated de novo DNA methylation. *Nature* 554:387-391. PMID: 29414941; DOI: 10.1038/nature25477; PMCID: PMC5814352. https://pubmed.ncbi.nlm.nih.gov/29414941/


## Citations

1. _metadata.json
2. aapola-2000-dnmt3l-cloning-abstract.md
3. aapola-2000-dnmt3l-cloning-summary.md
4. aapola-2002-dnmt3l-repressor-hdac-abstract.md
5. aapola-2002-dnmt3l-repressor-hdac-summary.md
6. barau-2016-dnmt3c-abstract.md
7. barau-2016-dnmt3c-summary.md
8. bgee-ENSECAG00000009690-expression.json
9. bgee-ENSECAG00000009690-summary.md
10. bourchis-2001-dnmt3l-maternal-imprints-abstract.md
11. bourchis-2001-dnmt3l-maternal-imprints-summary.md
12. bourchis-2004-meiotic-catastrophe-abstract.md
13. bourchis-2004-meiotic-catastrophe-summary.md
14. chedin-2002-dnmt3l-stimulates-dnmt3a-abstract.md
15. chedin-2002-dnmt3l-stimulates-dnmt3a-summary.md
16. gastal-2021-equine-embryo-methylation-abstract.md
17. gastal-2021-equine-embryo-methylation-fulltext.txt
18. gastal-2021-equine-embryo-methylation-summary.md
19. gowher-2005-mechanism-stimulation-abstract.md
20. gowher-2005-mechanism-stimulation-summary.md
21. guo-2015-dnmt3a-autoinhibition-abstract.md
22. guo-2015-dnmt3a-autoinhibition-summary.md
23. hata-2002-dnmt3l-cooperates-abstract.md
24. hata-2002-dnmt3l-cooperates-summary.md
25. holzschietinger-2010-processivity-abstract.md
26. holzschietinger-2010-processivity-summary.md
27. jia-2007-dnmt3a-dnmt3l-structure-abstract.md
28. jia-2007-dnmt3a-dnmt3l-structure-summary.md
29. jurkowska-2008-nucleoprotein-filaments-abstract.md
30. jurkowska-2008-nucleoprotein-filaments-fulltext.txt
31. jurkowska-2008-nucleoprotein-filaments-summary.md
32. kato-2007-dnmt3-male-germ-abstract.md
33. kato-2007-dnmt3-male-germ-summary.md
34. kobayashi-2012-gametic-methylomes-abstract.md
35. kobayashi-2012-gametic-methylomes-fulltext.txt
36. kobayashi-2012-gametic-methylomes-summary.md
37. liao-2014-dnmt3l-spermatogonial-quiescence-abstract.md
38. liao-2014-dnmt3l-spermatogonial-quiescence-summary.md
39. lucifero-2007-oogenesis-dnmt-abstract.md
40. lucifero-2007-oogenesis-dnmt-fulltext.txt
41. lucifero-2007-oogenesis-dnmt-summary.md
42. neri-2013-dnmt3l-bivalent-abstract.md
43. neri-2013-dnmt3l-bivalent-summary.md
44. ooi-2007-dnmt3l-h3k4-abstract.md
45. ooi-2007-dnmt3l-h3k4-summary.md
46. sakai-2004-gonocyte-coexpression-abstract.md
47. sakai-2004-gonocyte-coexpression-summary.md
48. shirane-2013-oocyte-methylomes-abstract.md
49. shirane-2013-oocyte-methylomes-fulltext.txt
50. shirane-2013-oocyte-methylomes-summary.md
51. suetake-2004-dnmt3l-stimulates-abstract.md
52. suetake-2004-dnmt3l-stimulates-summary.md
53. uniprot-A0A9L0T837-entry.txt
54. veland-2019-dnmt3l-dnmt3a-stability-abstract.md
55. veland-2019-dnmt3l-dnmt3a-stability-fulltext.txt
56. veland-2019-dnmt3l-dnmt3a-stability-summary.md
57. vlachogiannis-2015-dnmt3l-add-spermatogenesis-abstract.md
58. vlachogiannis-2015-dnmt3l-add-spermatogenesis-fulltext.txt
59. vlachogiannis-2015-dnmt3l-add-spermatogenesis-summary.md
60. wade-2009-horse-genome-abstract.md
61. wade-2009-horse-genome-summary.md
62. yokomine-2006-dnmt3-evolution-abstract.md
63. yokomine-2006-dnmt3-evolution-summary.md
64. zhang-2018-dnmt3a-structure-abstract.md
65. zhang-2018-dnmt3a-structure-fulltext.txt
66. zhang-2018-dnmt3a-structure-summary.md