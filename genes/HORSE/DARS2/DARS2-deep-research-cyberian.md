---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:26:07.601942'
end_time: '2026-10-26T02:35:22.343103'
duration_seconds: 554.74
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: DARS2
  gene_symbol: DARS2
  uniprot_accession: A0A9L0SB67
  protein_description: 'SubName: Full=Aspartyl-tRNA synthetase 2, mitochondrial {ECO:0000313|Ensembl:ENSECAP00000072097.1};'
  gene_info: Not specified in UniProt
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the class-II aminoacyl-tRNA synthetase family.
  protein_domains: Aa-tRNA-synt_II. (IPR004364); aa-tRNA-synth_II. (IPR006195); aa-tRNA-synth_II/BPL/LPL.
    (IPR045864); Asp-tRNA-ligase_1. (IPR004524); Asp-tRNA-ligase_1_N. (IPR047089)
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
citation_count: 49
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0SB67
- **Protein Description:** SubName: Full=Aspartyl-tRNA synthetase 2, mitochondrial {ECO:0000313|Ensembl:ENSECAP00000072097.1};
- **Gene Information:** Not specified in UniProt
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the class-II aminoacyl-tRNA synthetase family.
- **Key Domains:** Aa-tRNA-synt_II. (IPR004364); aa-tRNA-synth_II. (IPR006195); aa-tRNA-synth_II/BPL/LPL. (IPR045864); Asp-tRNA-ligase_1. (IPR004524); Asp-tRNA-ligase_1_N. (IPR047089)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "DARS2" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'DARS2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **DARS2** (gene ID: DARS2, UniProt: A0A9L0SB67) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# DARS2 (mitochondrial aspartyl-tRNA synthetase) in the horse, *Equus caballus* (UniProt A0A9L0SB67)

## 1. Introduction and summary

The horse protein A0A9L0SB67 is an unreviewed TrEMBL entry, named "Aspartyl-tRNA synthetase 2, mitochondrial" from the Ensembl gene model ENSECAG00000004044 on horse chromosome 5. It has 616 residues and is classified only by homology (protein existence level 3). Its InterPro and Pfam signatures place it in the class II aminoacyl-tRNA synthetases, type 1 (bacterial-type) aspartyl-tRNA synthetase subfamily (IPR004524, HAMAP MF_00044, PANTHER PTHR22594:SF5 "aspartate--tRNA ligase, mitochondrial"). It has an N-terminal OB-fold anticodon-binding domain (PF01336), a GAD insertion domain (PF02938) and a class II catalytic core (PF00152) [uniprot-A0A9L0SB67-entry]. No study has examined this horse protein or the horse *DARS2* gene directly. The gene symbol DARS2 is still unambiguous here: the horse sequence is 90% identical over 607 aligned residues to the experimentally characterized human DARS2 protein (UniProt Q6PI48), and the two share the targeting presequence, the catalytic motifs and the domain organization (see Section 3 and NOTES-sequence-comparison.md) [uniprot-Q6PI48-entry]. NCBI RefSeq annotates a longer canonical horse protein (isoform X1, XP_001493136.2, 652 residues). A0A9L0SB67 is identical to it except that it lacks a 36-residue segment in the insertion domain, so the UniProt entry most likely represents an alternative or truncated gene model of the same gene [ncbi-horse-DARS2-proteins]. Everything below about function is therefore inferred by orthology from work on the human enzyme and the mouse gene. That inference is strong, because the core translational role of this enzyme is conserved across mammals.

In short, DARS2 is the nuclear-encoded, mitochondrially imported aspartate–tRNA ligase (EC 6.1.1.12). It charges mitochondrial tRNA^Asp with L-aspartate in a two-step, ATP-dependent reaction that goes through an aspartyl-adenylate intermediate. This supplies Asp-tRNA^Asp for synthesis of the 13 mitochondrial-DNA-encoded respiratory chain subunits on mitoribosomes [bonnefond-2005-mtaspRS-tyrRS-abstract; neuenfeldt-2013-mtaspRS-structure-fulltext]. The enzyme is a homodimer with a bacterial-type architecture, but it has evolved a more open, flexible and electropositive structure that lets it recognize the structurally degenerate mitochondrial tRNA [neuenfeldt-2013-mtaspRS-structure-fulltext; fender-2012-identity-rules-abstract]. It sits in the mitochondrial matrix, partly free and partly bound electrostatically to the inner membrane [gonzalez-serrano-2018-submito-localization-fulltext]. Loss of the gene in mice abolishes normal mitochondrial translation [dogan-2014-dars2-heart-abstract]. In humans, partial loss causes the white-matter disease LBSL and axonal neuropathy [scheper-2007-lbsl-abstract; estevez-arias-2025-dars2-cmt2-fulltext]. Recent work also reports a non-canonical, extracellular immune-related role for human DARS2 [johnson-2024-extracellular-dars2-fulltext].

## 2. Identity verification and gene context

Several checks support the identification. The UniProt description, the PANTHER subfamily (mitochondrial aspartate–tRNA ligase) and the domain composition all match the human *DARS2* gene product, which was identified as the mitochondrial aspartyl-tRNA synthetase when Bonnefond and colleagues assigned the then-missing human mitochondrial aaRS genes [bonnefond-2005-mtaspRS-tyrRS-abstract]. Bonnefond et al. found that, except for lysyl- and glycyl-tRNA synthetases, mammalian mitochondrial and cytosolic aaRSs are encoded by separate genes [bonnefond-2005-mtaspRS-tyrRS-abstract]. This matters for annotation. The horse genome should therefore contain a separate cytosolic aspartyl-tRNA synthetase gene (*DARS1*, eukaryotic-type, type 2 subfamily), and A0A9L0SB67 should not be confused with it. The type 1 / "Asp-tRNA-ligase_1" InterPro signatures on A0A9L0SB67 identify the bacterial lineage, which is typical of mitochondrial enzymes. I found no paper on a different gene that shares the DARS2 symbol. The horse genome assembly from which the entry derives is described by Wade et al. (2009), cited in the UniProt record (PMID 19892987) [uniprot-A0A9L0SB67-entry].

## 3. Domain architecture, structure and horse-specific sequence features

The only crystal structure of a mammalian mitochondrial AspRS is that of human DARS2 (HsaDRS2), solved at 3.7 Å. It shows a homodimer whose fold closely matches *Escherichia coli* AspRS (43% sequence identity, all AspRS signature motifs conserved). Each subunit contains an N-terminal OB-fold anticodon-binding domain, a hinge, the class II catalytic domain with its antiparallel β-sheet, and a bacterial insertion domain (human residues 337–470) [neuenfeldt-2013-mtaspRS-structure-fulltext]. The mitochondrial enzyme differs from the bacterial one in four ways. Its insertion domain is rotated about 26°, which opens the active site and enlarges the catalytic groove. Its surface potential is more electropositive. Its subunit interface uses a different network of interactions. Its thermal stability is about 12 °C lower [neuenfeldt-2013-mtaspRS-structure-fulltext]. The authors argue that this added flexibility, on a conserved architecture, is an evolutionary adaptation that lets a nuclear-encoded protein work with degenerate organelle tRNAs [neuenfeldt-2013-mtaspRS-structure-abstract].

My pairwise alignment of horse A0A9L0SB67 with human Q6PI48 gives 90.3% identity over 607 aligned positions (NOTES-sequence-comparison.md). The N-terminal presequence, the anticodon-binding domain, the catalytic core and the C-terminal motif region (…GGIALGLDRLICLVTG…) are almost invariant. The serine at the position of human Ser45 is conserved; in human this residue lies in the predicted targeting signal, and the LBSL variant S45G blocks import [messmer-2011-import-mutation-abstract]. The most notable difference is that the horse model lacks a contiguous block of about 36 residues, corresponding to human residues ~341–376 (IIDISDVFRNTEIGFLQDALSKPHGTVKAICIPEGA). This block falls inside the bacterial insertion domain that Neuenfeldt et al. showed to be the mobile element that remodels the active-site groove [neuenfeldt-2013-mtaspRS-structure-fulltext]. Comparison with NCBI's horse protein records resolves part of this question. The RefSeq canonical horse protein, isoform X1 (XP_001493136.2, 652 residues, from the 2024 NCBI RefSeq annotation GCF_041296265.1-RS_2024_12), matches A0A9L0SB67 with no mismatches. It also contains the missing segment, as IVDISDVFRNTEVRFLQDVLSKPKGTVKAIRIPEGA (X1 residues 339–374), which aligns with the human block. Full-length horse X1 is 89.9% identical to human DARS2 over 643 aligned residues. A second RefSeq isoform, X2 (XP_014595026.1, 618 residues), keeps this segment but lacks X1 residues 97–130 in the anticodon-binding region [ncbi-horse-DARS2-proteins]. The gaps are clean, in-frame deletions against an otherwise identical sequence. This points to alternative exon use, or to differing gene-model predictions, at a horse *DARS2* locus that encodes a full-length protein like the human one. It does not point to a lineage-specific loss of the insertion domain. A0A9L0SB67 should therefore be annotated as a DARS2 isoform or gene model. It is not the reference horse protein, and it is unknown whether the short form is translated or catalytically active. Human DARS2 is itself subject to alternative splicing: most LBSL patients carry intron 2 mutations that cause exon 3 skipping [vanberge-2012-splicing-abstract].

## 4. Catalytic function and substrate specificity

DARS2 catalyzes the reaction tRNA^Asp + L-aspartate + ATP → L-aspartyl-tRNA^Asp + AMP + diphosphate. As in other class II aaRSs, the reaction has two steps: aspartate is first activated as aspartyl-adenylate (Asp-AMP), and the aspartyl group is then transferred to the 3′ terminal adenosine of tRNA^Asp. UniProt records this for human DARS2 from experimental evidence [uniprot-Q6PI48-entry]. Recombinant human mt-AspRS aminoacylates in vitro transcribed human mitochondrial tRNA^Asp as well as *E. coli* tRNAs [bonnefond-2005-mtaspRS-tyrRS-abstract]. Steady-state kinetics at 25 °C gave a k_cat of 4.0 × 10⁻³ s⁻¹ and a K_M of 1.1 µM for the human mt-tRNA^Asp transcript, and a k_cat of 10.3 × 10⁻³ s⁻¹ and a K_M of 1.2 µM for *E. coli* tRNA^Asp. Its catalytic efficiency is about 35–70-fold lower than that of *E. coli* AspRS on its own tRNA, and *E. coli* AspRS cannot detectably charge the mitochondrial tRNA at all [neuenfeldt-2013-mtaspRS-structure-fulltext]. Isothermal titration calorimetry showed that the mitochondrial enzyme binds both cognate and non-cognate tRNAs about ten times more tightly than the bacterial enzyme. Both enzymes bind an adenylate analog through a cooperative, allosteric mechanism [neuenfeldt-2013-mtaspRS-structure-abstract].

Two lines of evidence explain this asymmetry in tRNA recognition. Fender et al. showed that transplanting the established aspartylation identity elements into human mt-tRNA^Asp, and restoring its D-/T-loop tertiary interactions, still did not make it a good substrate for *E. coli* AspRS. The sequence context and structural instability of the mitochondrial tRNA are the barrier [fender-2012-identity-rules-abstract]. Mitochondrial DARS2 has therefore adapted to recognize a relaxed tRNA scaffold, mainly through the anticodon-binding domain and an open catalytic groove [neuenfeldt-2013-mtaspRS-structure-fulltext]. The amino acid specificity is strict for L-aspartate, as the nonhydrolysable intermediate analogs show. L-aspartol-adenylate is a competitive inhibitor with a micromolar K_i. 5′-O-[N-(L-aspartyl)sulfamoyl]adenosine (Asp-AMS) inhibits the mitochondrial enzyme with a K_i of about 10 nM, roughly 35-fold more potently than it inhibits mammalian cytosolic AspRS [messmer-2009-adenylate-analogs-abstract]. Asp-AMS also stabilizes and solubilizes the enzyme [gaudry-2012-redesigned-nterminus-abstract], which is consistent with tight binding at the adenylate site. Because the horse sequence conserves the catalytic and anticodon-binding regions, the same activity and specificity can be assigned to A0A9L0SB67 with confidence. Whether the possible insertion-domain deletion affects tRNA affinity is unknown.

## 5. Biogenesis, mitochondrial import and sub-mitochondrial localization

DARS2 is encoded in the nucleus, translated in the cytosol and imported into mitochondria. Its N-terminal targeting sequence is removed during maturation. Gaudry et al. found that the predicted cleavage site is probably inaccurate: a mature construct extended by seven residues was expressed, folded and crystallized much better [gaudry-2012-redesigned-nterminus-abstract]. Messmer et al. showed with in vivo and in vitro import assays that the LBSL variant S45G, which lies in the predicted targeting signal, impairs import across the mitochondrial membranes. This directly shows that the presequence is required [messmer-2011-import-mutation-abstract]. In cultured fibroblasts, DARS2 colocalizes with the outer-membrane marker TOMM20, consistent with mitochondrial residence [estevez-arias-2025-dars2-cmt2-fulltext].

Within the mitochondrion, fractionation of HEK293T mitochondria found mt-AspRS in both the soluble fraction (matrix and intermembrane space) and the membrane fraction. Salt released the membrane-bound pool, which indicates electrostatic anchoring. By contrast, mt-ArgRS binds the membrane hydrophobically and LysRS is entirely soluble [gonzalez-serrano-2018-submito-localization-fulltext]. The authors place this in the context of mitochondrial translation occurring at the matrix face of the inner membrane, where mitoribosomes are tethered so that hydrophobic respiratory-chain subunits can be inserted co-translationally [gonzalez-serrano-2018-submito-localization-fulltext]. The electropositive surface seen in the crystal structure [neuenfeldt-2013-mtaspRS-structure-abstract] fits electrostatic membrane anchoring, but that link has not been tested directly. UniProt annotates human DARS2 to "mitochondrion matrix" and "mitochondrion membrane" on the basis of these studies [uniprot-Q6PI48-entry]. The horse entry has only a generic IEA "cytoplasm" GO term [uniprot-A0A9L0SB67-entry]. Orthology supports the more specific mitochondrial matrix (GO:0005759) and mitochondrial (inner) membrane annotations instead.

## 6. Physiological role in mitochondrial translation: genetic evidence

Mouse genetics give in vivo evidence that DARS2 is required for mitochondrial protein synthesis. Conditional deletion of *Dars2* in heart and skeletal muscle caused severe deregulation of mitochondrial protein synthesis and a strong respiratory chain deficit in both tissues. Adaptive stress responses, including induction of the mitokine FGF21, were activated mainly in cardiomyocytes, and this occurred independently of the respiratory chain defect [dogan-2014-dars2-heart-abstract]. Depleting DARS2 in forebrain and hippocampal neurons caused strong mitochondrial dysfunction, progressive neuronal loss and early neuroinflammation. Myelin-producing cells survived despite a robust respiratory chain deficiency [aradjanski-2017-dars2-neurons-abstract]. In the pathway sense, then, DARS2 acts at one step of mitochondrial translation, aminoacyl-tRNA supply. Mitochondrial translation in turn underlies assembly of oxidative phosphorylation complexes I, III, IV and V. Downstream signaling, such as the FGF21 or integrated stress responses, follows from a translational defect and is not a direct DARS2 function [dogan-2014-dars2-heart-abstract]. Two later studies with the same neuronal knockout models support this view. Removing the matrix protease CLPP from DARS2-deficient Purkinje cells or forebrain neurons delayed neurodegeneration, made the oxidative phosphorylation defect milder, reduced neuroinflammation and improved motor function. The authors attribute the rescue to slower turnover of respiratory complex I [rumyantseva-2022-clpp-dars2-abstract]. So much of the harm from DARS2 loss passes through instability of the respiratory complexes that depend on mitochondrial translation. AAV9-mediated *DARS2* gene supplementation improved mitochondrial function, axonal growth and lactate release in LBSL patient-derived neurons. It also reduced cortical neurodegeneration and improved behavior in mice with *Dars2* deleted from CamKIIα-expressing neurons [garofolo-2026-aav9-dars2-abstract]. These results confirm a cell-autonomous loss-of-function mechanism. They also restate the core activity of the protein: an essential, ubiquitously expressed enzyme that attaches aspartate to its cognate tRNA for mitochondrial protein translation [garofolo-2026-aav9-dars2-abstract]. Reviews of the mitochondrial aaRS family suggest that the tissue selectivity of these diseases comes from how mitochondrial translation is integrated with each cell type's program and energy demand, neurons especially. On this view, tissue selectivity is not explained by differences in the catalytic reaction itself [sissler-2017-mtaars-review-abstract; gonzalez-serrano-2019-review-abstract].

Human disease genetics fits a hypomorphic-loss model. Scheper et al. found *DARS2* mutations in all 30 families with leukoencephalopathy with brain stem and spinal cord involvement and lactate elevation (LBSL), and the mutant enzymes had reduced activity. Respiratory chain activities in patient fibroblasts and lymphoblasts were nevertheless normal [scheper-2007-lbsl-abstract]. Most patients carry one leaky intron 2 splice mutation, which causes exon 3 skipping more readily in neural, especially neuronal, cells. This may explain why the disease is so selective for tissue despite ubiquitous expression [vanberge-2012-splicing-abstract]. Missense alleles act in diverse ways: they lower catalytic activity, expression or dimerization [vanberge-2013-lbsl-mutations-abstract], or they lower solubility and thermal stability without changing the overall architecture [sauter-2015-disease-mutants-fulltext]. Severe alleles such as Q184K (solubility) and R263Q (aminoacylation) occur only together with a partially functional splice allele [sauter-2015-disease-mutants-fulltext]. More recently, biallelic *DARS2* variants were linked to childhood-onset axonal Charcot–Marie–Tooth disease without leukoencephalopathy. Patient fibroblasts had reduced DARS2 levels, abnormal mitochondrial networks and impaired respiration, and the p.Pro503Leu variant kept only about 25% of wild-type aminoacylation activity [estevez-arias-2025-dars2-cmt2-fulltext]. Together these studies tie disease severity to residual aspartylation capacity. In horses, no *DARS2*-associated phenotype has been reported in the literature I searched.

## 7. Possible non-canonical functions

Several authors have proposed that mt-AspRS may have functions beyond aminoacylation. One reason is that LBSL mutations hit residues conserved only in mammals and produce individual molecular signatures not fully explained by catalytic loss [sauter-2015-disease-mutants-abstract]. Another is the distinctive sub-mitochondrial partitioning of different mt-aaRSs [gonzalez-serrano-2018-submito-localization-abstract; gonzalez-serrano-2019-review-abstract]. Johnson et al. reported the most concrete non-canonical activity. Human DARS2 is released into the circulation during bacterial pneumonia, and the extracellular protein has innate-immune and cell-repair properties. Intracellularly, DARS2 is ubiquitylated and degraded via the bacterially induced SCF E3 ligase subunit FBXO24, and DARS2 acetylation blocks this degradation. *Fbxo24* knockout mice have more lung DARS2 and stronger inflammatory responses after infection [johnson-2024-extracellular-dars2-fulltext]. These findings are recent, come from a single group, and have not been studied in non-human species. They should be treated as provisional and not transferred to the horse protein without evidence.

## 8. Implications for functional annotation of A0A9L0SB67

Taken together, the evidence supports the following orthology-based annotations for horse A0A9L0SB67. For molecular function: aspartate–tRNA ligase activity (GO:0004815; EC 6.1.1.12), ATP binding, and tRNA binding. For biological process: mitochondrial aspartyl-tRNA aminoacylation (GO:0070146), and more broadly mitochondrial translation. For cellular component: mitochondrial matrix, with a peripheral association to the mitochondrial inner membrane. The protein is expected to function as a homodimer. The functional data come from human enzymology and structure [bonnefond-2005-mtaspRS-tyrRS-abstract; neuenfeldt-2013-mtaspRS-structure-fulltext], human localization studies [gonzalez-serrano-2018-submito-localization-fulltext; messmer-2011-import-mutation-abstract] and mouse knockouts [dogan-2014-dars2-heart-abstract]. Transfer by sequence similarity (ISS/IBA) is well justified at 90% identity. The existing IEA "cytoplasm" component term is technically correct for the precursor before import, but it misrepresents where the mature protein acts. Because the entry is a shorter gene model that lacks part of the insertion domain, the most defensible practice is to annotate it as a product of the horse *DARS2* gene, with these terms, and to note that the full-length RefSeq isoform X1 is the closer counterpart of the characterized human enzyme [ncbi-horse-DARS2-proteins; neuenfeldt-2013-mtaspRS-structure-fulltext].

## Open Questions

Several points remain unresolved and are worth following up. First, the RefSeq comparison shows that the full-length horse protein contains the insertion-domain segment that A0A9L0SB67 lacks [ncbi-horse-DARS2-proteins]. It is still unknown whether horse tissues actually express the shorter transcript behind A0A9L0SB67, or the X2 variant that lacks part of the anticodon-binding region. Horse RNA-seq (for example FAANG data) and exon-level mapping could settle this. If a short form is translated, structural modeling and biochemical tests could show whether it can dimerize and charge tRNA^Asp, or whether it acts as an inactive or regulatory variant. This is worth asking because the common human disease alleles also act through mis-splicing of *DARS2* [vanberge-2012-splicing-abstract]. Second, the precise mitochondrial targeting-sequence cleavage site has not been determined experimentally in any species [gaudry-2012-redesigned-nterminus-abstract]. N-terminal proteomics of mammalian mitochondria would settle the mature N-terminus. Third, the role of the electrostatically membrane-bound pool of DARS2, and whether it couples directly to inner-membrane-tethered mitoribosomes, is unknown [gonzalez-serrano-2018-submito-localization-fulltext]. Fourth, the reported extracellular, immune-related role of DARS2 and its control by FBXO24 and acetylation [johnson-2024-extracellular-dars2-fulltext] needs independent replication, a defined secretion route, and testing in other mammals. Finally, there are no data on DARS2 variation or disease in horses. Equine neurogenetic disorders with long-tract white-matter or axonal pathology could be screened for *DARS2* variants, given the LBSL and CMT2 spectrum seen in humans [scheper-2007-lbsl-abstract; estevez-arias-2025-dars2-cmt2-fulltext].

## References

- **uniprot-A0A9L0SB67-entry** — UniProtKB/TrEMBL entry A0A9L0SB67_HORSE, "Aspartyl-tRNA synthetase 2, mitochondrial", *Equus caballus*; Ensembl ENSECAP00000072097.1 / ENSECAG00000004044. https://rest.uniprot.org/uniprotkb/A0A9L0SB67.txt (retrieved 2026-10-26; entry version 15).
- **uniprot-Q6PI48-entry** — UniProtKB/Swiss-Prot entry Q6PI48 (SYDM_HUMAN), Aspartate--tRNA ligase, mitochondrial, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/Q6PI48.txt (retrieved 2026-10-26).
- **ncbi-horse-DARS2-proteins** — NCBI Protein records for horse DARS2: RefSeq XP_001493136.2 (aspartate--tRNA ligase, mitochondrial isoform X1, 652 aa; mRNA XM_001493086.7), RefSeq XP_014595026.1 (isoform X2, 618 aa; mRNA XM_014739540.3), GenBank KAO2493859.1 and KAO2493860.1. NCBI RefSeq annotation GCF_041296265.1-RS_2024_12. https://www.ncbi.nlm.nih.gov/protein/XP_001493136.2 (retrieved 2026-10-26).
- **bonnefond-2005-mtaspRS-tyrRS** — Bonnefond L, Fender A, Rudinger-Thirion J, Giegé R, Florentz C, Sissler M. Toward the full set of human mitochondrial aminoacyl-tRNA synthetases: characterization of AspRS and TyrRS. *Biochemistry* 2005;44(12):4805-16. PMID: 15779907. DOI: 10.1021/bi047527z.
- **neuenfeldt-2013-mtaspRS-structure** — Neuenfeldt A, Lorber B, Ennifar E, Gaudry A, Sauter C, Sissler M, Florentz C. Thermodynamic properties distinguish human mitochondrial aspartyl-tRNA synthetase from bacterial homolog with same 3D architecture. *Nucleic Acids Res* 2013;41(4):2698-708. PMID: 23275545. PMCID: PMC3575848. DOI: 10.1093/nar/gks1322.
- **messmer-2009-adenylate-analogs** — Messmer M, Blais SP, Balg C, Chênevert R, Grenier L, Lagüe P, Sauter C, Sissler M, Giegé R, Lapointe J, Florentz C. Peculiar inhibition of human mitochondrial aspartyl-tRNA synthetase by adenylate analogs. *Biochimie* 2009;91(5):596-603. PMID: 19254750. DOI: 10.1016/j.biochi.2009.02.005.
- **fender-2012-identity-rules** — Fender A, Gaudry A, Jühling F, Sissler M, Florentz C. Adaptation of aminoacylation identity rules to mammalian mitochondria. *Biochimie* 2012;94(5):1090-7. PMID: 22402012. DOI: 10.1016/j.biochi.2012.02.030.
- **gaudry-2012-redesigned-nterminus** — Gaudry A, Lorber B, Neuenfeldt A, Sauter C, Florentz C, Sissler M. Re-designed N-terminus enhances expression, solubility and crystallizability of mitochondrial protein. *Protein Eng Des Sel* 2012;25(9):473-81. PMID: 22871419. DOI: 10.1093/protein/gzs046.
- **messmer-2011-import-mutation** — Messmer M, Florentz C, Schwenzer H, Scheper GC, van der Knaap MS, Maréchal-Drouard L, Sissler M. A human pathology-related mutation prevents import of an aminoacyl-tRNA synthetase into mitochondria. *Biochem J* 2011;433(3):441-6. PMID: 21121901. DOI: 10.1042/BJ20101902.
- **gonzalez-serrano-2018-submito-localization** — González-Serrano LE, Karim L, Pierre F, Schwenzer H, Rötig A, Munnich A, Sissler M. Three human aminoacyl-tRNA synthetases have distinct sub-mitochondrial localizations that are unaffected by disease-associated mutations. *J Biol Chem* 2018;293(35):13604-13615. PMID: 30006346. PMCID: PMC6120215. DOI: 10.1074/jbc.RA118.003400.
- **gonzalez-serrano-2019-review** — González-Serrano LE, Chihade JW, Sissler M. When a common biological role does not imply common disease outcomes: Disparate pathology linked to human mitochondrial aminoacyl-tRNA synthetases. *J Biol Chem* 2019;294(14):5309-5320. PMID: 30647134. PMCID: PMC6462531. DOI: 10.1074/jbc.REV118.002953.
- **sauter-2015-disease-mutants** — Sauter C, Lorber B, Gaudry A, Karim L, Schwenzer H, Wien F, Roblin P, Florentz C, Sissler M. Neurodegenerative disease-associated mutants of a human mitochondrial aminoacyl-tRNA synthetase present individual molecular signatures. *Sci Rep* 2015;5:17332. PMID: 26620921. PMCID: PMC4664897. DOI: 10.1038/srep17332.
- **scheper-2007-lbsl** — Scheper GC, van der Klok T, van Andel RJ, van Berkel CG, Sissler M, Smet J, et al. Mitochondrial aspartyl-tRNA synthetase deficiency causes leukoencephalopathy with brain stem and spinal cord involvement and lactate elevation. *Nat Genet* 2007;39(4):534-9. PMID: 17384640. DOI: 10.1038/ng2013.
- **vanberge-2012-splicing** — van Berge L, Dooves S, van Berkel CG, Polder E, van der Knaap MS, Scheper GC. Leukoencephalopathy with brain stem and spinal cord involvement and lactate elevation is associated with cell-type-dependent splicing of mtAspRS mRNA. *Biochem J* 2012;441(3):955-62. PMID: 22023289. DOI: 10.1042/BJ20110795.
- **vanberge-2013-lbsl-mutations** — van Berge L, Kevenaar J, Polder E, Gaudry A, Florentz C, Sissler M, van der Knaap MS, Scheper GC. Pathogenic mutations causing LBSL affect mitochondrial aspartyl-tRNA synthetase in diverse ways. *Biochem J* 2013;450(2):345-50. PMID: 23216004. DOI: 10.1042/BJ20121564.
- **dogan-2014-dars2-heart** — Dogan SA, Pujol C, Maiti P, Kukat A, Wang S, Hermans S, Senft K, Wibom R, Rugarli EI, Trifunovic A, et al. Tissue-specific loss of DARS2 activates stress responses independently of respiratory chain deficiency in the heart. *Cell Metab* 2014;19(3):458-69. PMID: 24606902. DOI: 10.1016/j.cmet.2014.02.004.
- **aradjanski-2017-dars2-neurons** — Aradjanski M, Dogan SA, Lotter S, Wang S, Hermans S, Wibom R, Rugarli E, Trifunovic A. DARS2 protects against neuroinflammation and apoptotic neuronal loss, but is dispensable for myelin producing cells. *Hum Mol Genet* 2017;26(21):4181-4189. PMID: 28985337. DOI: 10.1093/hmg/ddx307.
- **johnson-2024-extracellular-dars2** — Johnson BS, Farkas D, El-Mergawy R, Adair JA, Elhance A, Eltobgy M, Coan FM, Chafin L, et al. Targeted degradation of extracellular mitochondrial aspartyl-tRNA synthetase modulates immune responses. *Nat Commun* 2024;15(1):6172. PMID: 39039092. PMCID: PMC11263397. DOI: 10.1038/s41467-024-50031-7.
- **estevez-arias-2025-dars2-cmt2** — Estévez-Arias B, Sarv S, Bonello-Palot N, Carrera-García L, Ortez C, et al. Biallelic Variants in the DARS2 Gene as a Novel Cause of Axonal Charcot-Marie-Tooth Disease. *Ann Neurol* 2025;98(6):1335-1351. PMID: 40814755. PMCID: PMC12682944. DOI: 10.1002/ana.78005.
- **rumyantseva-2022-clpp-dars2** — Rumyantseva A, Popovic M, Trifunovic A. CLPP deficiency ameliorates neurodegeneration caused by impaired mitochondrial protein synthesis. *Brain* 2022;145(1):92-104. PMID: 35240691. DOI: 10.1093/brain/awab303.
- **garofolo-2026-aav9-dars2** — Garofolo I, Lindsay B, Liang Y, Ratajczak B, Janowski M, Walczak P, Fatemi A, Nemeth CL. AAV9-DARS2 Gene Therapy Rescues Phenotype in Leukoencephalopathy with Brainstem and Spinal Cord Involvement and Lactate Elevation Patient Cells and Neuronal Dars2 Deficient Mice. *Ann Neurol* 2026;99(1):59-72. PMID: 40948401. PMCID: PMC13533035. DOI: 10.1002/ana.78037.
- **sissler-2017-mtaars-review** — Sissler M, González-Serrano LE, Westhof E. Recent Advances in Mitochondrial Aminoacyl-tRNA Synthetases and Disease. *Trends Mol Med* 2017;23(8):693-708. PMID: 28716624. DOI: 10.1016/j.molmed.2017.06.002.


## Citations

1. aradjanski-2017-dars2-neurons-abstract.md
2. aradjanski-2017-dars2-neurons-summary.md
3. bonnefond-2005-mtaspRS-tyrRS-abstract.md
4. bonnefond-2005-mtaspRS-tyrRS-summary.md
5. dogan-2014-dars2-heart-abstract.md
6. dogan-2014-dars2-heart-summary.md
7. estevez-arias-2025-dars2-cmt2-abstract.md
8. estevez-arias-2025-dars2-cmt2-fulltext.txt
9. estevez-arias-2025-dars2-cmt2-summary.md
10. fender-2012-identity-rules-abstract.md
11. fender-2012-identity-rules-summary.md
12. garofolo-2026-aav9-dars2-abstract.md
13. garofolo-2026-aav9-dars2-summary.md
14. gaudry-2012-redesigned-nterminus-abstract.md
15. gaudry-2012-redesigned-nterminus-summary.md
16. gonzalez-serrano-2018-submito-localization-abstract.md
17. gonzalez-serrano-2018-submito-localization-fulltext.txt
18. gonzalez-serrano-2018-submito-localization-summary.md
19. gonzalez-serrano-2019-review-abstract.md
20. gonzalez-serrano-2019-review-summary.md
21. johnson-2024-extracellular-dars2-abstract.md
22. johnson-2024-extracellular-dars2-fulltext.txt
23. johnson-2024-extracellular-dars2-summary.md
24. messmer-2009-adenylate-analogs-abstract.md
25. messmer-2009-adenylate-analogs-summary.md
26. messmer-2011-import-mutation-abstract.md
27. messmer-2011-import-mutation-summary.md
28. ncbi-horse-DARS2-proteins-summary.md
29. ncbi-horse-DARS2-proteins.fasta
30. neuenfeldt-2013-mtaspRS-structure-abstract.md
31. neuenfeldt-2013-mtaspRS-structure-fulltext.txt
32. neuenfeldt-2013-mtaspRS-structure-summary.md
33. rumyantseva-2022-clpp-dars2-abstract.md
34. rumyantseva-2022-clpp-dars2-summary.md
35. sauter-2015-disease-mutants-abstract.md
36. sauter-2015-disease-mutants-fulltext.txt
37. sauter-2015-disease-mutants-summary.md
38. scheper-2007-lbsl-abstract.md
39. scheper-2007-lbsl-summary.md
40. sissler-2017-mtaars-review-abstract.md
41. sissler-2017-mtaars-review-summary.md
42. uniprot-A0A9L0SB67-entry.txt
43. uniprot-A0A9L0SB67.fasta
44. uniprot-Q6PI48-entry.txt
45. uniprot-Q6PI48-human-DARS2.fasta
46. vanberge-2012-splicing-abstract.md
47. vanberge-2012-splicing-summary.md
48. vanberge-2013-lbsl-mutations-abstract.md
49. vanberge-2013-lbsl-mutations-summary.md