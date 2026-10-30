---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:05:54.865338'
end_time: '2026-10-26T00:15:11.236113'
duration_seconds: 556.37
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: KDM4C
  gene_symbol: KDM4C
  uniprot_accession: A0A9L0K3L6
  protein_description: 'RecName: Full=[histone H3]-trimethyl-L-lysine(9) demethylase
    {ECO:0000256|ARBA:ARBA00012900}; EC=1.14.11.66 {ECO:0000256|ARBA:ARBA00012900};'
  gene_info: Name=KDM4C {ECO:0000313|Ensembl:ENSEASP00005055940.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the JHDM3 histone demethylase family.
  protein_domains: EPHD. (IPR034732); JmjC_dom. (IPR003347); JmjN. (IPR003349); KDM4-like_Tudor.
    (IPR040477); Tudor. (IPR002999)
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
citation_count: 64
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0K3L6
- **Protein Description:** RecName: Full=[histone H3]-trimethyl-L-lysine(9) demethylase {ECO:0000256|ARBA:ARBA00012900}; EC=1.14.11.66 {ECO:0000256|ARBA:ARBA00012900};
- **Gene Information:** Name=KDM4C {ECO:0000313|Ensembl:ENSEASP00005055940.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the JHDM3 histone demethylase family.
- **Key Domains:** EPHD. (IPR034732); JmjC_dom. (IPR003347); JmjN. (IPR003349); KDM4-like_Tudor. (IPR040477); Tudor. (IPR002999)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "KDM4C" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'KDM4C' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **KDM4C** (gene ID: KDM4C, UniProt: A0A9L0K3L6) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# KDM4C (UniProt A0A9L0K3L6) in the donkey, *Equus asinus*: a JmjC-domain histone H3K9/H3K36 trimethyl demethylase

## 1. Introduction and summary

The donkey protein A0A9L0K3L6 is an unreviewed UniProtKB/TrEMBL entry of 1,052 residues. It was predicted by Ensembl (gene ENSEASG00005010714, chromosome 23) from the chromosome-level donkey reference genome [wang-2020-donkey-genomes-abstract; uniprot-A0A9L0K3L6-entry]. The entry names the gene *KDM4C*, assigns it to the JHDM3 histone demethylase family, and gives it the activity [histone H3]-trimethyl-L-lysine(9) demethylase (EC 1.14.11.66) with Fe(2+) as cofactor and a nuclear location. All of these annotations were transferred automatically (ARBA, PROSITE, TreeGrafter) and none comes from experiments on the donkey protein [uniprot-A0A9L0K3L6-entry]. I found no published study of donkey or other equid KDM4C. The symbol is not ambiguous, however. KDM4C (also called GASC1 and JMJD2C) is a well-defined vertebrate orthology group, and it has been studied extensively in human and mouse. A global alignment I made between the donkey sequence and human KDM4C (Q9H3R0) gives 91.1% identity over the full length. The JmjN–JmjC catalytic region (residues 1–350) is 99.7% identical, and every iron-binding and 2-oxoglutarate-binding residue is conserved (H190, E192 and H278 for Fe(II); Y134, K208 and K243 for 2-OG/substrate) [notes_alignment_donkey_vs_human_KDM4C; uniprot-Q9H3R0-entry]. The function of the donkey protein can therefore be inferred with high confidence from its human and mouse orthologues.

On that basis, donkey KDM4C is expected to be a nuclear, chromatin-associated Fe(II)/2-oxoglutarate-dependent dioxygenase. Its main reaction is the oxidative removal of methyl groups from tri- and dimethylated lysine 9 of histone H3 (H3K9me3/me2). It also acts on H3K36me3/me2 and on linker histone H1.4K26me3, and it releases formaldehyde and succinate [cloos-2006-gasc1-demethylates-abstract; whetstine-2006-jmjd2-reversal-abstract; hillringhaus-2011-kdm4-selectivity-fulltext; trojer-2009-h1-4-demethylation-fulltext]. The C-terminal double PHD and hybrid Tudor reader domains target the enzyme to H3K4me3-marked transcription start sites. There it erases the repressive H3K9me3 mark, keeping promoters transcriptionally competent [pedersen-2014-jmjd2c-tss-abstract; pedersen-2016-jmjd2-esc-abstract]. KDM4C also works as a coactivator for several DNA-binding transcription factors: the androgen receptor (together with LSD1), HIF-1α, ATF4 and, indirectly, Oct4/Nanog circuitry [wissmann-2007-jmjd2c-lsd1-ar-abstract; luo-2012-jmjd2c-hif1-abstract; zhao-2016-kdm4c-atf4-abstract; loh-2007-jmjd1a-jmjd2c-esc-abstract]. Unlike its paralogues KDM4A and KDM4B, it stays on chromosomes during mitosis, and it is needed for faithful chromosome segregation [kupershmit-2014-kdm4c-mitosis-fulltext].

## 2. Identity, domain architecture and evolutionary context

*KDM4C* was first cloned as *GASC1* ("gene amplified in squamous cell carcinoma 1") from a 9p23–24 amplicon in oesophageal squamous carcinoma cell lines. At that time its PHD-finger motifs were recognized, but its catalytic domain was not [yang-2000-gasc1-amplicon-abstract]. Later work placed it in the JMJD2 (now KDM4) subfamily of Jumonji proteins [cloos-2006-gasc1-demethylates-abstract]. KDM4A, KDM4B and KDM4C are proteins of about 130 kDa that share one architecture: an N-terminal JmjN domain and a JmjC catalytic domain, followed by a long, mostly disordered linker, two PHD fingers and two Tudor domains. KDM4D is about half that size and lacks the reader domains [berry-2013-kdm4-review-abstract; kupershmit-2014-kdm4c-mitosis-fulltext]. The donkey entry matches this layout. UniProt maps JmjN to residues 16–58, JmjC to 144–310 and a PHD-type zinc finger to 748–861, and marks disordered regions at 367–388 and 418–582. InterPro records the extended PHD (IPR034732), the KDM4-like Tudor (IPR040477) and Tudor (IPR002999) signatures, and CDD hits name the domains specifically as JMJD2C PHD, ePHD and Tudor repeats 1 and 2 [uniprot-A0A9L0K3L6-entry]. The PANTHER subfamily assignment (PTHR10694:SF104, "lysine-specific demethylase 4C") also places the protein in the KDM4C orthology group, not in a paralogous one.

The sequence differences between the donkey and human proteins sit almost entirely in the linker (residues 351–700, 76.6% identity). The PHD region (97.2%) and Tudor region (96.6%) are nearly invariant, as is the catalytic core [notes_alignment_donkey_vs_human_KDM4C]. This pattern fits a strongly constrained enzymatic and reader function with a fast-evolving, low-complexity spacer. Phylogenetic analysis supports the picture. Hillringhaus et al. found KDM4A–C orthologues in all vertebrates with sequenced genomes, whereas earlier-branching animals have a single KDM4 enzyme. KDM4D is restricted to eutherian mammals [hillringhaus-2011-kdm4-selectivity-abstract]. As a eutherian, the donkey should therefore have the full KDM4A–D set, and its KDM4C is a 1:1 orthologue of the human gene.

## 3. Catalytic mechanism and substrate specificity

KDM4C was identified as an enzyme by Cloos and colleagues. They were looking for proteins that bind H3K9me3 and recovered GASC1. They then showed that three JMJD2 members, GASC1 among them, demethylate H3K9me3 and H3K9me2 in vitro by a hydroxylation reaction that needs iron and α-ketoglutarate (2-oxoglutarate) [cloos-2006-gasc1-demethylates-abstract]. In the general JmjC mechanism, Fe(II) and 2-OG activate O2 to hydroxylate the methyl carbon, and the unstable carbinolamine then breaks down to formaldehyde. UniProt captures this as Rhea:60200, in which H3K9me3 plus 2 2-OG and 2 O2 gives H3K9me1, 2 formaldehyde, 2 succinate and 2 CO2 [uniprot-A0A9L0K3L6-entry]. Whetstine et al. reported at the same time that JMJD2 subfamily members are trimethyl-selective demethylases. The products they leave differ by member: KDM4A stops at the dimethyl state, while other members take H3K9me3 down to me2 and me1. The authors proposed that this lets the family fine-tune methylation states at the same lysine [whetstine-2006-jmjd2-reversal-abstract]. In cells, ectopic GASC1 lowers H3K9me3/me2 and raises H3K9me1, so the enzyme stops at the monomethyl state [cloos-2006-gasc1-demethylates-abstract].

KDM4C is a dual-specificity enzyme. Hillringhaus et al. produced the catalytic domains of human KDM4A–E and assayed them by mass spectrometry. KDM4A, KDM4B and KDM4C demethylate the tri- and dimethylated forms of both H3K9 and H3K36, whereas KDM4D and KDM4E act only on H3K9. Activity on H3K36 peptides was too low for reliable kinetic parameters. On H3K9, the KDM4A–C enzymes had higher k_cat for me3 than for me2, with similar K_m values [hillringhaus-2011-kdm4-selectivity-fulltext]. The same study solved the crystal structure of the KDM4C catalytic domain bound to Ni(2+) (standing in for Fe(2+)) and the 2-OG analogue N-oxalylglycine at 2.55 Å (PDB 2XML). The fold is very similar to KDM4A [hillringhaus-2011-kdm4-selectivity-fulltext]. Building on the JMJD2A core structure, which showed that JmjN, JmjC, a C-terminal domain and a zinc-finger motif together form the substrate pocket [chen-2006-jmjd2-structure-abstract], Hillringhaus et al. showed that H3K9 versus H3K36 selectivity is set by several contacts inside the catalytic domain but outside the active site [hillringhaus-2011-kdm4-selectivity-abstract]. The donkey sequence is 99.7% identical to human across this region, so it should share both the H3K9 and H3K36 activities.

KDM4C also has a non-core-histone substrate. G9a methylates linker histone H1.4 at K26, creating a binding site for HP1 and L3MBTL1. Trojer et al. found that recombinant catalytic fragments of mouse Jmjd2a, Jmjd2b and Jmjd2c demethylate H1K26me3 peptides in vitro, and that the activity is blocked by an iron chelator [trojer-2009-h1-4-demethylation-fulltext]. Reviews now list H3K9, H3K36 and H1.4K26 as the KDM4A–C substrate set [berry-2013-kdm4-review-abstract]. One annotation discrepancy should be noted. The Swiss-Prot function text for human KDM4C (Q9H3R0) says the enzyme has no activity on dimethylated residues [uniprot-Q9H3R0-entry]. That is inconsistent with the direct biochemical data showing H3K9me2 demethylation by GASC1 and measurable k_cat on H3K9me2 for KDM4C [cloos-2006-gasc1-demethylates-abstract; hillringhaus-2011-kdm4-selectivity-fulltext]. The GO term transferred to the donkey entry, "histone H3K9me2/H3K9me3 demethylase activity," agrees with the primary literature [uniprot-A0A9L0K3L6-entry].

## 4. Reader domains, chromatin targeting and subcellular localization

KDM4C is a nuclear protein. The donkey entry's nuclear location comes from the JmjN ProRule [uniprot-A0A9L0K3L6-entry], and the experimental work below shows that the protein acts on chromatin. Its C-terminal hybrid Tudor domain controls where it binds in the genome. The structural template comes from KDM4A. There, the two Tudor motifs interdigitate into a "double" or hybrid Tudor domain that binds H3K4me3 in an aromatic cage, with sequence specificity supplied by Tudor-1 residues [huang-2006-jmjd2a-tudor-abstract]. The KDM4A domain binds H4K20me3 through a completely different mode [lee-2008-jmjd2a-tudor-binding-abstract]. KDM4C's double Tudor differs. Pedersen et al. showed that it binds H3K4me3 but not H4K20me2/me3 in vitro, a specificity distinct from the KDM4A and KDM4B Tudors. Genome-wide, JMJD2C localizes to H3K4me3-positive transcription start sites in primary cells and in the KYSE150 carcinoma line, which carries a *JMJD2C* amplification, and this binding depends on the double Tudor domain [pedersen-2014-jmjd2c-tss-abstract]. Mouse Jmjd2a and Jmjd2c both occupy H3K4me3-positive promoters, where they redundantly prevent H3K9me3 and H3K36me3 from accumulating [pedersen-2016-jmjd2-esc-abstract]. The resulting model has KDM4C read the active H3K4me3 mark and erase the repressive H3K9me3 mark at the same promoters. This self-reinforcing loop protects transcriptional competence.

KDM4C also behaves differently from its paralogues during mitosis. Kupershmit et al. imaged EGFP fusions in U2OS cells and found that KDM4A and KDM4B are excluded from chromatin from prometaphase to telophase, while KDM4C stays on mitotic chromatin. Its presence coincides with lower mitotic H3K9me3. Domain swaps showed that the C-terminal Tudor-containing region is necessary and sufficient for mitotic chromatin association, and the point mutation R919 in the proximal Tudor domain abolished it [kupershmit-2014-kdm4c-mitosis-fulltext; kupershmit-2014-kdm4c-mitosis-abstract]. Both depleting and overexpressing KDM4C, but not KDM4B, raised the frequency of misaligned and lagging chromosomes and anaphase bridges more than threefold. A catalytically dead mutant had no such effect, which implicates demethylase activity in segregation fidelity [kupershmit-2014-kdm4c-mitosis-abstract]. The Tudor region is 96.6% identical between the two species, and human R919 aligns to a conserved arginine at donkey position 915 within an identical local motif (DGSFSRDTFPE) [notes_alignment_donkey_vs_human_KDM4C]. The donkey protein very likely shares this mitotic localization.

The cellular localization terms supported for donkey KDM4C are therefore nucleus and chromatin, specifically euchromatic promoters and transcription start sites in interphase and condensed mitotic chromosomes. The demethylation of heterochromatic H3K9me3 seen when JMJD2 proteins are overexpressed shows that the enzyme can also act on pericentric heterochromatin [cloos-2006-gasc1-demethylates-abstract; fodor-2006-jmjd2b-heterochromatin-abstract].

## 5. Transcriptional coactivator function and pathways

Because it removes H3K9me3, which recruits HP1 and KAP1, KDM4C generally acts as a transcriptional coactivator, and several DNA-binding factors recruit it. The first example was the androgen receptor. JMJD2C binds ligand-bound AR in vitro and in vivo, and the two assemble on AR target genes, where H3K9me3 is removed and transcription is stimulated. JMJD2C also binds the flavin-dependent demethylase LSD1, which removes only me2/me1, and the two cooperatively demethylate H3K9me3/me2/me1 at AR targets. Knocking down JMJD2C blocks androgen-induced H3K9me3 removal, target activation and tumour cell proliferation [wissmann-2007-jmjd2c-lsd1-ar-abstract]. This is a clear case of two demethylases with different product specificities working in sequence to erase a lysine methylation mark completely.

In hypoxia signalling, JMJD2C binds HIF-1α selectively (not HIF-2α) and is recruited by it to hypoxia response elements. There it lowers H3K9me3 and increases HIF-1 occupancy, activating glycolytic and metabolic genes (*SLC2A1*, *LDHA*, *PDK1*, *BNIP3*) and pro-metastatic genes (*LOXL2*, *L1CAM*) [luo-2012-jmjd2c-hif1-abstract]. In the amino acid stress response, KDM4C keeps *ATF4* expressed by binding its promoter. It also binds ATF4 and co-occupies serine–glycine synthesis gene promoters such as *PHGDH*, where it removes H3K9me3 under both normal and serine-deprived conditions. ATF4 is needed for KDM4C's effect on these genes [zhao-2016-kdm4c-atf4-fulltext; zhao-2016-kdm4c-atf4-abstract]. Other reported targets include the *Mdm2* P2 promoter, where Jmjd2c demethylates H3K9 and raises Mdm2 expression in a catalysis-dependent way, lowering p53 levels [ishimura-2009-jmjd2c-mdm2-abstract]. In 9p24-amplified lymphomas, JMJD2C cooperates with JAK2, which is encoded in the same amplicon and phosphorylates H3Y41, to keep MYC and other loci free of heterochromatin [rui-2010-amplicon-jak2-jmjd2c-abstract]. These studies come largely from cancer cell models and describe recruitment by transcription factors. They show that KDM4C's main molecular role is the same in every context, removing H3K9me3 at specific promoters, while the pathway it serves is set by its binding partner.

## 6. Regulation of KDM4C: chromatin release, protein stability and partner complexes

A few studies show how KDM4C itself is controlled, separately from its recruitment by transcription factors. Burton et al. found that inositol hexakisphosphate kinase 1 (IP6K1), which makes the inositol pyrophosphate IP7, is associated with chromatin and binds JMJD2C. When IP6K1 is expressed, JMJD2C dissociates from chromatin and H3K9me3 rises, and this depends on IP6K1 kinase activity. Conversely, lowering IP7 (by RNAi or in *ip6k1*-null fibroblasts) reduces H3K9me3 and raises H3K9 acetylation, which changes transcription of JMJD2C target genes [burton-2013-inositol-pyrophosphates-jmjd2c-abstract]. This links a small-molecule metabolic signal to how long KDM4C stays on chromatin. The structural basis of the effect is still unknown. At the protein level, a tandem-affinity purification and mass-spectrometry screen in lung cancer cells identified the deubiquitinase USP9X as a KDM4C partner that removes ubiquitin from KDM4C and stabilizes it. Depleting USP9X destabilizes KDM4C and weakens KDM4C-dependent activation of *TGFB2*, which KDM4C induces by removing H3K9me3 from its promoter [jie-2021-usp9x-kdm4c-fulltext; jie-2021-usp9x-kdm4c-abstract]. KDM4C abundance is therefore set at least partly by ubiquitin-dependent turnover. KDM4C also forms specific partnerships with other chromatin enzymes. Besides its cooperation with LSD1 (Section 5), KDM4C is recruited together with the H4R3 methyltransferase PRMT1 by leukaemogenic chimeric transcription factors. A co-immunoprecipitation screen across several demethylases found that MOZ-TIF2 binds KDM4C and none of the others tested, through the first 79 residues of the MOZ moiety. Endogenous Kdm4c recruited to the *Hoxa9* promoter coincides with low H3K9me3 and high H3K9 acetylation [cheung-2016-prmt1-kdm4c-aml-fulltext; cheung-2016-prmt1-kdm4c-aml-abstract]. These results fit the general picture: KDM4C is a modular eraser whose genomic targets are set by its Tudor reader domain and by DNA-binding partners, and whose activity is further tuned by chromatin release and by protein stability.

## 7. Developmental and physiological roles from genetic studies

Mouse genetics clarifies which phenotypes need KDM4C. Knockdown in mouse ES cells first suggested that Jmjd2c, an Oct4-regulated gene, is needed for self-renewal, because it removes H3K9me3 from the *Nanog* promoter and keeps HP1 and KAP1 away [loh-2007-jmjd1a-jmjd2c-esc-abstract]. Constitutive *Jmjd2c* knockout mice, however, are viable, and knockout cells proliferate and self-renew normally [pedersen-2014-jmjd2c-tss-abstract]. The two results are reconciled by redundancy. Conditional combined loss of *Jmjd2a* and *Jmjd2c*, but not other combinations, causes early embryonic lethality and loss of ESC self-renewal with drift toward primitive endoderm. Catalytic activity is required, and H3K9me3 builds up at shared Jmjd2a/c target promoters, including self-renewal genes [pedersen-2016-jmjd2-esc-abstract]. The physiological role of KDM4C in mammals is therefore best described as continual, partly redundant (with KDM4A) removal of H3K9me3 from active promoters to keep cell identity stable. Its dispensability on its own is notable given how often it is amplified and required in cancer cells [berry-2013-kdm4-review-abstract; pedersen-2014-jmjd2c-tss-abstract]. Nothing is known about KDM4C function specifically in equids, and I found no donkey or horse phenotype or expression data in the literature.

## 8. Synthesis: functional annotation of donkey KDM4C

Taken together, the orthology, domain and conservation evidence supports annotating A0A9L0K3L6 with the following. Its molecular function is histone H3K9me3/me2 demethylase activity (EC 1.14.11.66), with secondary H3K36me3/me2 and H1.4K26me3 demethylase activity, Fe(II) and 2-oxoglutarate dependence, and methylated-histone (H3K4me3) binding through the hybrid Tudor domain. Its locations are the nucleus and chromatin, including transcription start sites and mitotic chromosomes. Its biological roles are positive regulation of transcription by RNA polymerase II through promoter H3K9 demethylation, transcription coactivator activity downstream of nuclear receptors and stress-responsive transcription factors (AR, HIF-1α, ATF4) and in partnership with LSD1 and PRMT1, maintenance of pluripotency gene expression redundantly with KDM4A, and mitotic chromosome segregation [cloos-2006-gasc1-demethylates-abstract; hillringhaus-2011-kdm4-selectivity-fulltext; trojer-2009-h1-4-demethylation-fulltext; pedersen-2014-jmjd2c-tss-abstract; pedersen-2016-jmjd2-esc-abstract; wissmann-2007-jmjd2c-lsd1-ar-abstract; luo-2012-jmjd2c-hif1-abstract; zhao-2016-kdm4c-atf4-fulltext; kupershmit-2014-kdm4c-mitosis-fulltext]. Every one of these is an inference by orthology. The 99.7% identity in the catalytic domain makes the enzymatic annotations very reliable. The pathway-level annotations are less certain, because they rest on human cancer cell models and on mouse.

## Open Questions

Several gaps remain. The donkey gene model itself has not been checked experimentally. UniProt lists it as protein-existence level unknown, derived only from Ensembl annotation of the 2020 assembly [uniprot-A0A9L0K3L6-entry; wang-2020-donkey-genomes-abstract], so RNA-seq support for the exon structure, the 1,052-residue length, the N-terminus (which differs from human at residue 3, E versus V) and possible alternative isoforms (human has four) would be worth examining. Biochemically, how much KDM4C prefers H3K9 over H3K36 and H1.4K26 on nucleosomal rather than peptide substrates is still not well quantified. The conflict between the Swiss-Prot statement that KDM4C has no activity on dimethylated lysines and the primary kinetic data should be resolved and corrected in the curated record [uniprot-Q9H3R0-entry; hillringhaus-2011-kdm4-selectivity-fulltext]. One of the two papers that Swiss-Prot cites for that statement is a KDM5 inhibitor study in which KDM4C served only as a selectivity counter-screen, so it does not bear on substrate specificity [tumber-2017-kdm5-inhibitor-fulltext]. How IP7 releases KDM4C from chromatin (direct binding, or modification of a partner) and which E3 ligase opposes USP9X are also unresolved [burton-2013-inositol-pyrophosphates-jmjd2c-abstract; jie-2021-usp9x-kdm4c-abstract]. Mechanistically, the Kupershmit study leaves open which mitotic substrate and which reader interaction (the R919-dependent Tudor contact) underlie KDM4C's role in chromosome segregation [kupershmit-2014-kdm4c-mitosis-fulltext]. The linker region is the only part that diverges between donkey and human; whether it carries species-specific interaction motifs or post-translational modification sites is unknown. Finally, no data exist on KDM4C expression or function in equid tissues. Equine and asinine expression atlases would be a useful next step, as would checking whether donkey-specific coding variants affect conserved residues.

## References

- **berry-2013-kdm4-review**: Berry WL, Janknecht R. (2013). KDM4/JMJD2 histone demethylases: epigenetic regulators in cancer cells. *Cancer Research* 73(10):2936-2942. PMID: 23644528; PMCID: PMC3655154; DOI: [10.1158/0008-5472.can-12-4300](https://doi.org/10.1158/0008-5472.can-12-4300). https://pubmed.ncbi.nlm.nih.gov/23644528/
- **chen-2006-jmjd2-structure**: Chen Z, Zang J, Whetstine J, Hong X, Davrazou F, Kutateladze TG, Simpson M, Mao Q, Pan CH, Dai S, Hagman J, Hansen K, Shi Y, Zhang G. (2006). Structural insights into histone demethylation by JMJD2 family members. *Cell* 125(4):691-702. PMID: 16677698; DOI: [10.1016/j.cell.2006.04.024](https://doi.org/10.1016/j.cell.2006.04.024). https://pubmed.ncbi.nlm.nih.gov/16677698/
- **cloos-2006-gasc1-demethylates**: Cloos PA, Christensen J, Agger K, Maiolica A, Rappsilber J, Antal T, Hansen KH, Helin K. (2006). The putative oncogene GASC1 demethylates tri- and dimethylated lysine 9 on histone H3. *Nature* 442(7100):307-311. PMID: 16732293; DOI: [10.1038/nature04837](https://doi.org/10.1038/nature04837). https://pubmed.ncbi.nlm.nih.gov/16732293/
- **fodor-2006-jmjd2b-heterochromatin**: Fodor BD, Kubicek S, Yonezawa M, O'Sullivan RJ, Sengupta R, Perez-Burgos L, Opravil S, Mechtler K, Schotta G, Jenuwein T. (2006). Jmjd2b antagonizes H3K9 trimethylation at pericentric heterochromatin in mammalian cells. *Genes & development* 20(12):1557-1562. PMID: 16738407; PMCID: PMC1482475; DOI: [10.1101/gad.388206](https://doi.org/10.1101/gad.388206). https://pubmed.ncbi.nlm.nih.gov/16738407/
- **hillringhaus-2011-kdm4-selectivity**: Hillringhaus L, Yue WW, Rose NR, Ng SS, Gileadi C, Loenarz C, Bello SH, Bray JE, Schofield CJ, Oppermann U. (2011). Structural and evolutionary basis for the dual substrate selectivity of human KDM4 histone demethylase family. *The Journal of biological chemistry* 286(48):41616-41625. PMID: 21914792; PMCID: PMC3308871; DOI: [10.1074/jbc.m111.283689](https://doi.org/10.1074/jbc.m111.283689). https://pubmed.ncbi.nlm.nih.gov/21914792/
- **huang-2006-jmjd2a-tudor**: Huang Y, Fang J, Bedford MT, Zhang Y, Xu RM. (2006). Recognition of histone H3 lysine-4 methylation by the double tudor domain of JMJD2A. *Science (New York, N.Y.)* 312(5774):748-751. PMID: 16601153; DOI: [10.1126/science.1125162](https://doi.org/10.1126/science.1125162). https://pubmed.ncbi.nlm.nih.gov/16601153/
- **ishimura-2009-jmjd2c-mdm2**: Ishimura A, Terashima M, Kimura H, Akagi K, Suzuki Y, Sugano S, Suzuki T. (2009). Jmjd2c histone demethylase enhances the expression of Mdm2 oncogene. *Biochemical and biophysical research communications* 389(2):366-371. PMID: 19732750; DOI: [10.1016/j.bbrc.2009.08.155](https://doi.org/10.1016/j.bbrc.2009.08.155). https://pubmed.ncbi.nlm.nih.gov/19732750/
- **klose-2006-jhdm3a-demethylates**: Klose RJ, Yamane K, Bae Y, Zhang D, Erdjument-Bromage H, Tempst P, Wong J, Zhang Y. (2006). The transcriptional repressor JHDM3A demethylates trimethyl histone H3 lysine 9 and lysine 36. *Nature* 442(7100):312-316. PMID: 16732292; DOI: [10.1038/nature04853](https://doi.org/10.1038/nature04853). https://pubmed.ncbi.nlm.nih.gov/16732292/
- **kupershmit-2014-kdm4c-mitosis**: Kupershmit I, Khoury-Haddad H, Awwad SW, Guttmann-Raviv N, Ayoub N. (2014). KDM4C (GASC1) lysine demethylase is associated with mitotic chromatin and regulates chromosome segregation during mitosis. *Nucleic acids research* 42(10):6168-6182. PMID: 24728997; PMCID: PMC4041427; DOI: [10.1093/nar/gku253](https://doi.org/10.1093/nar/gku253). https://pubmed.ncbi.nlm.nih.gov/24728997/
- **lee-2008-jmjd2a-tudor-binding**: Lee J, Thompson JR, Botuyan MV, Mer G. (2008). Distinct binding modes specify the recognition of methylated histones H3K4 and H4K20 by JMJD2A-tudor. *Nature structural & molecular biology* 15(1):109-111. PMID: 18084306; PMCID: PMC2211384; DOI: [10.1038/nsmb1326](https://doi.org/10.1038/nsmb1326). https://pubmed.ncbi.nlm.nih.gov/18084306/
- **loh-2007-jmjd1a-jmjd2c-esc**: Loh YH, Zhang W, Chen X, George J, Ng HH. (2007). Jmjd1a and Jmjd2c histone H3 Lys 9 demethylases regulate self-renewal in embryonic stem cells. *Genes & development* 21(20):2545-2557. PMID: 17938240; PMCID: PMC2000320; DOI: [10.1101/gad.1588207](https://doi.org/10.1101/gad.1588207). https://pubmed.ncbi.nlm.nih.gov/17938240/
- **luo-2012-jmjd2c-hif1**: Luo W, Chang R, Zhong J, Pandey A, Semenza GL. (2012). Histone demethylase JMJD2C is a coactivator for hypoxia-inducible factor 1 that is required for breast cancer progression. *Proceedings of the National Academy of Sciences of the United States of America* 109(49):E3367-76. PMID: 23129632; PMCID: PMC3523832; DOI: [10.1073/pnas.1217394109](https://doi.org/10.1073/pnas.1217394109). https://pubmed.ncbi.nlm.nih.gov/23129632/
- **pedersen-2014-jmjd2c-tss**: Pedersen MT, Agger K, Laugesen A, Johansen JV, Cloos PA, Christensen J, Helin K. (2014). The demethylase JMJD2C localizes to H3K4me3-positive transcription start sites and is dispensable for embryonic development. *Molecular and cellular biology* 34(6):1031-1045. PMID: 24396064; PMCID: PMC3958041; DOI: [10.1128/mcb.00864-13](https://doi.org/10.1128/mcb.00864-13). https://pubmed.ncbi.nlm.nih.gov/24396064/
- **pedersen-2016-jmjd2-esc**: Pedersen MT, Kooistra SM, Radzisheuskaya A, Laugesen A, Johansen JV, Hayward DG, Nilsson J, Agger K, Helin K. (2016). Continual removal of H3K9 promoter methylation by Jmjd2 demethylases is vital for ESC self-renewal and early development. *The EMBO journal* 35(14):1550-1564. PMID: 27266524; PMCID: PMC4899663; DOI: [10.15252/embj.201593317](https://doi.org/10.15252/embj.201593317). https://pubmed.ncbi.nlm.nih.gov/27266524/
- **rui-2010-amplicon-jak2-jmjd2c**: Rui L, Emre NC, Kruhlak MJ, Chung HJ, Steidl C, Slack G, Wright GW, Lenz G, Ngo VN, Shaffer AL, Xu W, Zhao H, Yang Y, Lamy L, Davis RE, Xiao W, Powell J, Maloney D, Thomas CJ, Möller P, Rosenwald A, Ott G, Muller-Hermelink HK, Savage K, Connors JM, Rimsza LM, Campo E, Jaffe ES, Delabie J, Smeland EB, Weisenburger DD, Chan WC, Gascoyne RD, Levens D, Staudt LM. (2010). Cooperative epigenetic modulation by cancer amplicon genes. *Cancer cell* 18(6):590-605. PMID: 21156283; PMCID: PMC3049192; DOI: [10.1016/j.ccr.2010.11.013](https://doi.org/10.1016/j.ccr.2010.11.013). https://pubmed.ncbi.nlm.nih.gov/21156283/
- **trojer-2009-h1-4-demethylation**: Trojer P, Zhang J, Yonezawa M, Schmidt A, Zheng H, Jenuwein T, Reinberg D. (2009). Dynamic Histone H1 Isotype 4 Methylation and Demethylation by Histone Lysine Methyltransferase G9a/KMT1C and the Jumonji Domain-containing JMJD2/KDM4 Proteins. *The Journal of biological chemistry* 284(13):8395-8405. PMID: 19144645; PMCID: PMC2659197; DOI: [10.1074/jbc.m807818200](https://doi.org/10.1074/jbc.m807818200). https://pubmed.ncbi.nlm.nih.gov/19144645/
- **wang-2020-donkey-genomes**: Wang C, Li H, Guo Y, Huang J, Sun Y, Min J, Wang J, Fang X, Zhao Z, Wang S, Zhang Y, Liu Q, Jiang Q, Wang X, Guo Y, Yang C, Wang Y, Tian F, Zhuang G, Fan Y, Gao Q, Li Y, Ju Z, Li J, Li R, Hou M, Yang G, Liu G, Liu W, Guo J, Pan S, Fan G, Zhang W, Zhang R, Yu J, Zhang X, Yin Q, Ji C, Jin Y, Yue G, Liu M, Xu J, Liu S, Jordana J, Noce A, Amills M, Wu DD, Li S, Zhou X, Zhong J. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications* 11(1):6014. PMID: 33293529; PMCID: PMC7723042; DOI: [10.1038/s41467-020-19813-7](https://doi.org/10.1038/s41467-020-19813-7). https://pubmed.ncbi.nlm.nih.gov/33293529/
- **whetstine-2006-jmjd2-reversal**: Whetstine JR, Nottke A, Lan F, Huarte M, Smolikov S, Chen Z, Spooner E, Li E, Zhang G, Colaiacovo M, Shi Y. (2006). Reversal of histone lysine trimethylation by the JMJD2 family of histone demethylases. *Cell* 125(3):467-481. PMID: 16603238; DOI: [10.1016/j.cell.2006.03.028](https://doi.org/10.1016/j.cell.2006.03.028). https://pubmed.ncbi.nlm.nih.gov/16603238/
- **wissmann-2007-jmjd2c-lsd1-ar**: Wissmann M, Yin N, Müller JM, Greschik H, Fodor BD, Jenuwein T, Vogler C, Schneider R, Günther T, Buettner R, Metzger E, Schüle R. (2007). Cooperative demethylation by JMJD2C and LSD1 promotes androgen receptor-dependent gene expression. *Nature cell biology* 9(3):347-353. PMID: 17277772; DOI: [10.1038/ncb1546](https://doi.org/10.1038/ncb1546). https://pubmed.ncbi.nlm.nih.gov/17277772/
- **yang-2000-gasc1-amplicon**: Yang ZQ, Imoto I, Fukuda Y, Pimkhaokham A, Shimada Y, Imamura M, Sugano S, Nakamura Y, Inazawa J. (2000). Identification of a novel gene, GASC1, within an amplicon at 9p23-24 frequently detected in esophageal cancer cell lines. *Cancer research* 60(17):4735-4739. PMID: 10987278. https://pubmed.ncbi.nlm.nih.gov/10987278/
- **zhao-2016-kdm4c-atf4**: Zhao E, Ding J, Xia Y, Liu M, Ye B, Choi JH, Yan C, Dong Z, Huang S, Zha Y, Yang L, Cui H, Ding HF. (2016). KDM4C and ATF4 Cooperate in Transcriptional Control of Amino Acid Metabolism. *Cell reports* 14(3):506-519. PMID: 26774480; PMCID: PMC4731315; DOI: [10.1016/j.celrep.2015.12.053](https://doi.org/10.1016/j.celrep.2015.12.053). https://pubmed.ncbi.nlm.nih.gov/26774480/
- **burton-2013-inositol-pyrophosphates-jmjd2c**: Burton A, Azevedo C, Andreassi C, Riccio A, Saiardi A. (2013). Inositol pyrophosphates regulate JMJD2C-dependent histone demethylation. *Proceedings of the National Academy of Sciences of the United States of America* 110(47):18970-18975. PMID: 24191012; PMCID: PMC3839729; DOI: [10.1073/pnas.1309699110](https://doi.org/10.1073/pnas.1309699110). https://pubmed.ncbi.nlm.nih.gov/24191012/
- **cheung-2016-prmt1-kdm4c-aml**: Cheung N, Fung TK, Zeisig BB, Holmes K, Rane JK, Mowen KA, Finn MG, Lenhard B, Chan LC, So CW. (2016). Targeting Aberrant Epigenetic Networks Mediated by PRMT1 and KDM4C in Acute Myeloid Leukemia. *Cancer Cell* 29(1):32-48. PMID: 26766589; PMCID: PMC4712026; DOI: [10.1016/j.ccell.2015.12.007](https://doi.org/10.1016/j.ccell.2015.12.007). https://pubmed.ncbi.nlm.nih.gov/26766589/
- **jie-2021-usp9x-kdm4c**: Jie X, Fong WP, Zhou R, Zhao Y, Zhao Y, Meng R, Zhang S, Dong X, Zhang T, Yang K, Wu G, Xu S. (2021). USP9X-mediated KDM4C deubiquitination promotes lung cancer radioresistance by epigenetically inducing TGF-β2 transcription. *Cell Death and Differentiation* 28(7):2095-2111. PMID: 33558705; PMCID: PMC8257660; DOI: [10.1038/s41418-021-00740-z](https://doi.org/10.1038/s41418-021-00740-z). https://pubmed.ncbi.nlm.nih.gov/33558705/
- **tumber-2017-kdm5-inhibitor**: Tumber A, Nuzzi A, Hookway ES, et al. (2017). Potent and Selective KDM5 Inhibitor Stops Cellular Demethylation of H3K4me3 at Transcription Start Sites and Proliferation of MM1S Myeloma Cells. *Cell Chemical Biology* 24(3):371-380. PMID: 28262558; PMCID: PMC5361737; DOI: [10.1016/j.chembiol.2017.02.006](https://doi.org/10.1016/j.chembiol.2017.02.006). https://pubmed.ncbi.nlm.nih.gov/28262558/
- **uniprot-A0A9L0K3L6**: UniProt Consortium. UniProtKB/TrEMBL entry A0A9L0K3L6_EQUAS, [histone H3]-trimethyl-L-lysine(9) demethylase, *Equus asinus* (entry version 15, 02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0K3L6.txt (saved as `citations/uniprot-A0A9L0K3L6-entry.txt`)
- **uniprot-Q9H3R0**: UniProt Consortium. UniProtKB/Swiss-Prot entry Q9H3R0 (KDM4C_HUMAN), Lysine-specific demethylase 4C, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q9H3R0.txt (saved as `citations/uniprot-Q9H3R0-entry.txt`)
- **notes_alignment_donkey_vs_human_KDM4C**: Pairwise global alignment (Biopython PairwiseAligner, BLOSUM62, gap open −10, extend −0.5) of A0A9L0K3L6 against Q9H3R0, computed for this report (`notes_alignment_donkey_vs_human_KDM4C.txt`).


## Citations

1. berry-2013-kdm4-review-abstract.md
2. berry-2013-kdm4-review-fulltext.txt
3. berry-2013-kdm4-review-summary.md
4. burton-2013-inositol-pyrophosphates-jmjd2c-abstract.md
5. burton-2013-inositol-pyrophosphates-jmjd2c-summary.md
6. chen-2006-jmjd2-structure-abstract.md
7. chen-2006-jmjd2-structure-summary.md
8. cheung-2016-prmt1-kdm4c-aml-abstract.md
9. cheung-2016-prmt1-kdm4c-aml-fulltext.txt
10. cheung-2016-prmt1-kdm4c-aml-summary.md
11. cloos-2006-gasc1-demethylates-abstract.md
12. cloos-2006-gasc1-demethylates-summary.md
13. fodor-2006-jmjd2b-heterochromatin-abstract.md
14. fodor-2006-jmjd2b-heterochromatin-summary.md
15. hillringhaus-2011-kdm4-selectivity-abstract.md
16. hillringhaus-2011-kdm4-selectivity-fulltext.txt
17. hillringhaus-2011-kdm4-selectivity-summary.md
18. huang-2006-jmjd2a-tudor-abstract.md
19. huang-2006-jmjd2a-tudor-summary.md
20. internal_citations.json
21. ishimura-2009-jmjd2c-mdm2-abstract.md
22. ishimura-2009-jmjd2c-mdm2-summary.md
23. jie-2021-usp9x-kdm4c-abstract.md
24. jie-2021-usp9x-kdm4c-fulltext.txt
25. jie-2021-usp9x-kdm4c-summary.md
26. klose-2006-jhdm3a-demethylates-abstract.md
27. klose-2006-jhdm3a-demethylates-summary.md
28. kupershmit-2014-kdm4c-mitosis-abstract.md
29. kupershmit-2014-kdm4c-mitosis-fulltext.txt
30. kupershmit-2014-kdm4c-mitosis-summary.md
31. lee-2008-jmjd2a-tudor-binding-abstract.md
32. lee-2008-jmjd2a-tudor-binding-summary.md
33. loh-2007-jmjd1a-jmjd2c-esc-abstract.md
34. loh-2007-jmjd1a-jmjd2c-esc-summary.md
35. luo-2012-jmjd2c-hif1-abstract.md
36. luo-2012-jmjd2c-hif1-summary.md
37. metadata.json
38. pedersen-2014-jmjd2c-tss-abstract.md
39. pedersen-2014-jmjd2c-tss-summary.md
40. pedersen-2016-jmjd2-esc-abstract.md
41. pedersen-2016-jmjd2-esc-summary.md
42. rui-2010-amplicon-jak2-jmjd2c-abstract.md
43. rui-2010-amplicon-jak2-jmjd2c-fulltext.txt
44. rui-2010-amplicon-jak2-jmjd2c-summary.md
45. trojer-2009-h1-4-demethylation-abstract.md
46. trojer-2009-h1-4-demethylation-fulltext.txt
47. trojer-2009-h1-4-demethylation-summary.md
48. tumber-2017-kdm5-inhibitor-abstract.md
49. tumber-2017-kdm5-inhibitor-fulltext.txt
50. tumber-2017-kdm5-inhibitor-summary.md
51. uniprot-A0A9L0K3L6-entry.txt
52. uniprot-Q9H3R0-entry.txt
53. wang-2020-donkey-genomes-abstract.md
54. wang-2020-donkey-genomes-fulltext.txt
55. wang-2020-donkey-genomes-summary.md
56. whetstine-2006-jmjd2-reversal-abstract.md
57. whetstine-2006-jmjd2-reversal-summary.md
58. wissmann-2007-jmjd2c-lsd1-ar-abstract.md
59. wissmann-2007-jmjd2c-lsd1-ar-summary.md
60. yang-2000-gasc1-amplicon-abstract.md
61. yang-2000-gasc1-amplicon-summary.md
62. zhao-2016-kdm4c-atf4-abstract.md
63. zhao-2016-kdm4c-atf4-fulltext.txt
64. zhao-2016-kdm4c-atf4-summary.md