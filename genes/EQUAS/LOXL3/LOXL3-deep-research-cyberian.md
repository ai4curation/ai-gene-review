---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T00:09:56.303615'
end_time: '2026-10-26T00:17:37.291678'
duration_seconds: 460.99
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: LOXL3
  gene_symbol: LOXL3
  uniprot_accession: A0A9L0K7N3
  protein_description: 'RecName: Full=Lysyl oxidase homolog {ECO:0000256|RuleBase:RU367046};
    EC=1.4.3.13 {ECO:0000256|RuleBase:RU367046};'
  gene_info: Name=LOXL3 {ECO:0000313|Ensembl:ENSEASP00005061359.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the lysyl oxidase family.
  protein_domains: Lysyl_oxidase. (IPR001695); Lysyl_oxidase_CS. (IPR019828); SRCR.
    (IPR001190); SRCR-like_dom_sf. (IPR036772); Lysyl_oxidase (PF01186)
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
citation_count: 78
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0K7N3
- **Protein Description:** RecName: Full=Lysyl oxidase homolog {ECO:0000256|RuleBase:RU367046}; EC=1.4.3.13 {ECO:0000256|RuleBase:RU367046};
- **Gene Information:** Name=LOXL3 {ECO:0000313|Ensembl:ENSEASP00005061359.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the lysyl oxidase family.
- **Key Domains:** Lysyl_oxidase. (IPR001695); Lysyl_oxidase_CS. (IPR019828); SRCR. (IPR001190); SRCR-like_dom_sf. (IPR036772); Lysyl_oxidase (PF01186)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "LOXL3" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'LOXL3' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **LOXL3** (gene ID: LOXL3, UniProt: A0A9L0K7N3) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# LOXL3 (Lysyl oxidase homolog 3) in the Donkey, *Equus asinus* (UniProt A0A9L0K7N3): Function, Localization and Pathways

## 1. Introduction and Summary

LOXL3 encodes lysyl oxidase-like 3, one of the five members of the vertebrate lysyl oxidase (LOX) family of copper-dependent amine oxidases (LOX, LOXL1, LOXL2, LOXL3 and LOXL4) [laurentino-2019-loxl3-review-abstract]. The donkey protein A0A9L0K7N3 is an unreviewed TrEMBL entry, predicted from the chromosome-level Dezhou donkey reference genome [wang-2020-donkey-genomes-abstract] by Ensembl gene annotation. Its name, EC number (1.4.3.13, protein-lysine 6-oxidase), copper cofactor, lysine tyrosylquinone (LTQ) cofactor and secreted, cytoplasmic and nuclear locations were all assigned automatically by rule-based annotation [uniprot-A0A9L0K7N3-entry]. No experimental study of donkey LOXL3 was found, and the donkey genome paper does not discuss the gene [wang-2020-donkey-genomes-fulltext]. Its function therefore has to be inferred from close orthologs, mainly human, mouse and zebrafish LOXL3. As shown below, the orthology is unambiguous.

The core function of LOXL3 is enzymatic. It oxidatively deaminates the ε-amino group of peptidyl lysine to give the aldehyde allysine (2-aminoadipate-6-semialdehyde), releasing H2O2 and NH4+ [uniprot-A0A9L0K7N3-entry; serrabardenys-2022-lysine-oxidation-review-abstract]. In the extracellular matrix (ECM), allysine residues on collagen and elastin condense spontaneously into covalent cross-links. Human LOXL3 and its splice variants have β-aminopropionitrile (BAPN)-inhibitable activity toward several collagen types and elastin, and each variant has its own substrate preference [lee-2006-loxl3-variant-substrate-abstract; jeong-2017-loxl3-sv2-abstract]. Loxl3-null mice show a marked loss of collagen cross-links in palate and spine and die perinatally with cleft palate and spinal deformity [zhang-2015-loxl3-cleft-palate-abstract]. In humans, biallelic LOXL3 mutations cause autosomal recessive Stickler syndrome and early-onset high myopia [alzahrani-2015-loxl3-stickler-abstract; li-2016-loxl3-myopia-abstract]. Besides collagen and elastin, LOXL3 oxidizes fibronectin at the myotendinous junction to tune integrin signaling [kraftsheleg-2016-loxl3-fibronectin-abstract]. Inside the cell, its SRCR repeats deacetylate and deacetyliminate nuclear STAT3 [ma-2017-loxl3-stat3-abstract]. It also cooperates with the transcription factor Snail [peinado-2005-loxl2-snail-abstract], supports genome integrity in melanoma cells [santamaria-2018-loxl3-melanoma-abstract], and in cancer cells can move into mitochondria, where it stabilizes DHODH [zhan-2023-loxl3-ferroptosis-dhodh-abstract]. In short, donkey LOXL3 is best described as a secreted, copper/LTQ-dependent protein-lysine 6-oxidase that matures fibrillar collagen (notably collagen II in cartilage and eye) and other ECM proteins, with an additional, less well established intracellular role.

## 2. Gene Identity and Verification of Orthology

The gene symbol LOXL3 is unambiguous in vertebrates. The donkey entry has the family-defining features: a Pfam Lysyl_oxidase domain (PF01186), the lysyl oxidase PROSITE signature (PS00926), and four SRCR domains (PF00530, SMART SM00202). It is assigned to PANTHER subfamily PTHR45817:SF2 (lysyl oxidase homolog 3) and maps to donkey chromosome 6 [uniprot-A0A9L0K7N3-entry]. This architecture of four N-terminal SRCR domains plus a C-terminal catalytic domain is shared only by LOXL2, LOXL3 and LOXL4; LOX and LOXL1 instead have N-terminal propeptides [laurentino-2019-loxl3-review-fulltext]. Because PANTHER assigns the protein specifically to the LOXL3 subfamily, it is a LOXL3 ortholog rather than one of those paralogs.

For this report I aligned the donkey sequence (824 aa) globally against reviewed human LOXL3 (P58215, 753 aa) [uniprot-P58215-entry] using Biopython (BLOSUM62). 720 residues are identical, or about 96% of the human length. The two differences in length are a 52-residue N-terminal extension in the donkey model that precedes a Met aligning with human Met1, followed by the conserved hydrophobic signal peptide (MQPVSVWQWSLWGLLLCLLCSSCLGS…), and an 18-residue Lys/Arg-rich insertion within SRCR domain 2 (…RKLRKRAAKASARRPKP…). Both are probably gene-model artefacts: an upstream start codon in the first case, and possibly retained intronic or alternative-exon sequence in the second. They should be treated with caution, because human LOXL3 is reported with a 25-residue signal peptide [maki-2001-fourth-lox-isoenzyme-abstract; huang-2001-hloxl3-cloning-abstract]. Every catalytically essential residue is conserved. The copper-binding histidines that correspond to human His607, His609 and His611 sit at donkey His678, His680 and His682, within the WHECHGHYH motif. The LTQ-forming Lys634 and Tyr670 correspond to donkey Lys705 and Tyr741 [uniprot-P58215-entry]. Ser704, the regulatory phosphosite in human LOXL3 [zhan-2023-loxl3-ferroptosis-dhodh-abstract], corresponds to donkey Ser775 in an identical local context (FEVAESDFTNNA). Within the alignment, the catalytic C-terminal region differs from human at only a few conservative positions. LOXL3 is conserved even in the jawless lamprey, whose ortholog retains the LOX-family catalytic motifs [pang-2025-loxl3-lamprey-abstract], so strong conservation across mammals is expected.

## 3. Domain Architecture and Catalytic Mechanism

The first cloning studies of human LOXL3 described a 753–754-residue polypeptide [maki-2001-fourth-lox-isoenzyme-abstract; jourdanlesaux-2001-loxl3-expression-abstract; huang-2001-hloxl3-cloning-abstract]. It has an N-terminal signal peptide and four SRCR domains, followed by the C-terminal LOX domain (human residues ~529–729). The LOX domain contains the copper-binding sequence, the lysine and tyrosine residues that form the lysyl-tyrosyl quinone cofactor, and a cytokine receptor-like (CRL) domain [maki-2001-fourth-lox-isoenzyme-abstract; jourdanlesaux-2001-loxl3-expression-abstract]. Human LOXL3 maps to 2p13.3 and has 14 exons [jourdanlesaux-2001-loxl3-expression-abstract]. The N-terminal region also contains a putative bipartite nuclear localization signal [maki-2001-fourth-lox-isoenzyme-abstract], a putative BMP-1 cleavage site, and predicted N- and O-glycosylation sites [laurentino-2019-loxl3-review-fulltext].

The chemistry is shared across the LOX family. Copper is required both for the autocatalytic generation of LTQ from the conserved tyrosine (oxidized to topaquinone and condensed with the conserved lysine) and for the catalytic cycle itself [uniprot-A0A9L0K7N3-entry; serrabardenys-2022-lysine-oxidation-review-abstract]. LTQ then oxidizes the ε-amine of a substrate lysine to an aldehyde (allysine), with O2 reduced to H2O2 and ammonia released [uniprot-A0A9L0K7N3-entry]. UniProt also lists a second, rule-predicted reaction for the donkey protein: oxidation of N6-acetyl-lysyl residues to allysine plus acetamide [uniprot-A0A9L0K7N3-entry]. This mirrors the deacetylation/deacetylimination activity described for LOXL3 below. No LOXL3 structure has been solved. The closest template is the 2.4-Å crystal structure of human LOXL2 (SRCR3–4 plus catalytic domain), which was captured in a zinc-bound precursor state with the LTQ precursor residues 16.6 Å apart. In that study, copper loading activated LOXL2 and supported LTQ formation, which suggests that large conformational rearrangements accompany enzyme activation [zhang-2018-loxl2-crystal-structure-abstract]. Given how conserved the LOXL2/LOXL3 catalytic domains are [santamaria-2022-loxl2-loxl3-redundant-abstract], the donkey enzyme can reasonably be expected to share this copper-dependent maturation.

## 4. Substrate Specificity: Collagens, Elastin and Fibronectin

Recombinant human LOXL3 has BAPN-inhibitable amine oxidase activity toward elastin and several collagen types. A shorter variant, LOXL3-sv1, which lacks SRCR domains 1–3 but keeps the catalytic domain, is also active but prefers different substrates and is expressed in different tissues [lee-2006-loxl3-variant-substrate-abstract]. UniProt's curation of that study records the highest activity of full-length LOXL3 toward collagen type VIII, and of sv1 toward collagen type IV [uniprot-P58215-entry]. A third variant, LOXL3-sv2, lacks SRCR2 and is active against collagen I [jeong-2017-loxl3-sv2-abstract]. The SRCR domains are therefore not needed for catalysis but probably shape substrate preference. The physiologically most important substrate appears to be cartilage collagen II. In vivo, Loxl3 deficiency in mouse embryos sharply reduces both immature (HLNL, DHLNL) and mature pyridinoline (HYL-PYR, LYS-PYR) collagen cross-links in the palate and spine [zhang-2015-loxl3-cleft-palate-fulltext]. Alzahrani and colleagues state that LOXL3 cross-links collagen II and that LOXL3-deficient morphants phenocopy the craniofacial defects of collagen XI deficiency [alzahrani-2015-loxl3-stickler-abstract]. Conditional deletion with Col2a1-Cre disturbs type II collagen in the cochlear spiral ligament [liu-2021-loxl3-hearing-loss-abstract].

Beyond collagen, LoxL3 forms a complex with fibronectin and oxidizes it directly. Fibronectin is the ECM scaffold and integrin ligand enriched at the myotendinous junction (MTJ). LoxL3 secreted locally from myofiber tips oxidizes fibronectin there, which enhances local integrin activation and lets myofibers stretch and anchor at the correct position [kraftsheleg-2016-loxl3-fibronectin-abstract]. Later work by the same group showed that this oxidation has a structural consequence. Treating fibronectin with recombinant human LOXL3 (or LOXL2) induced fibronectin clustering, enlarged cell spreading in a βAPN-sensitive manner and enhanced integrin-mediated force transmission. The authors propose that lysyl oxidase-mediated fibronectin oxidation is a force-independent nucleation step for fibronectin fibrillogenesis. Consistent with this, LoxL3 colocalizes with β1-integrin at the cell periphery, and LoxL3 mutant embryos show abnormal fibronectin fibrils at somite boundaries, cleft palate and fewer neural crest cells [melamed-2023-fibronectin-fibrillogenesis-abstract; melamed-2023-fibronectin-fibrillogenesis-fulltext]. In a cancer setting, LOXL3 purified from liver cancer cells oxidized a peptide containing DHODH Lys344 (ALEK344IRAGAS) in vitro, and phosphorylation at Ser704 accounted for a large share of that activity: the S704A mutant lost about 65% [zhan-2023-loxl3-ferroptosis-dhodh-fulltext]. Together these studies show that LOXL3 is a broad-specificity protein-lysine oxidase. Its substrate choice appears to depend on context, through co-localization and protein–protein association, more than on a strict sequence motif.

## 5. Subcellular and Tissue Localization

The canonical location of LOXL3 is extracellular. The protein has a signal peptide, and recombinant LOXL3 expressed in HT-1080 cells was secreted into the medium. In that study it was not seen in nuclei despite the putative NLS [maki-2001-fourth-lox-isoenzyme-abstract]. The extracellular role is consistent with the cross-linking defects in knockout tissues [zhang-2015-loxl3-cleft-palate-abstract] and with fibronectin oxidation at the MTJ [kraftsheleg-2016-loxl3-fibronectin-abstract]. Several groups, however, also report intracellular pools. LOXL3 has been seen in a perinuclear position in overexpressing HeLa, MDCK and melanoma cells, where it interacts with Snail [laurentino-2019-loxl3-review-fulltext; peinado-2005-loxl2-snail-abstract]. It has been found in the nucleus bound to STAT3 [ma-2017-loxl3-stat3-abstract], and in the nuclear fraction of melanoma cells together with BRCA2, MSH2, SMC1A and NUMA1 [santamaria-2018-loxl3-melanoma-fulltext]. In liver cancer cells under chemotherapy-induced EGFR signaling, it is imported into mitochondria through TOM20 [zhan-2023-loxl3-ferroptosis-dhodh-abstract]. The secreted, cytoplasmic and nuclear assignments in the donkey record are inferred from these mammalian data [uniprot-A0A9L0K7N3-entry]. UniProt notes for human LOXL3 that it is unclear how one protein can be both intracellular and secreted [uniprot-P58215-entry].

LOXL3 is widely expressed. Reported sites in human include placenta, heart, ovary, testis, small intestine and spleen [maki-2001-fourth-lox-isoenzyme-abstract], the central nervous system and neurons, uterus, heart and leukocytes [jourdanlesaux-2001-loxl3-expression-abstract], and spleen and testis [huang-2001-hloxl3-cloning-abstract]. Variant transcripts are distributed differently from the full-length form [lee-2006-loxl3-variant-substrate-abstract]. Even in the lamprey, LOXL3 is expressed in endostyle and liver and responds to immune challenge [pang-2025-loxl3-lamprey-abstract].

## 6. Developmental and Physiological Roles: Cartilage, Palate, Eye, Ear, Lung and Muscle

Genetic studies in mice and humans point to the same core physiology: LOXL3 cross-links collagen in cartilage and connective tissue. Loxl3-/- mice die perinatally with cleft palate, abnormal thoracic vertebral cartilage primordia and mild alveolar shrinkage [zhang-2015-loxl3-cleft-palate-abstract]. The cleft arises from delayed palatal shelf elevation, together with reduced mesenchymal proliferation and reduced collagen fiber deposition [liu-2025-loxl3-palatal-shelf-abstract]. Loxl3-deficient embryos also have smaller lungs and thoracic cavities, with excess elastic fibres that correlate with compensatory LOXL4 and TGF-β1 upregulation [zhang-2016-loxl3-lung-abstract]. A knock-in mouse carrying the Stickler-associated p.Cys676Tyr substitution shows perinatal death, cleft palate, spinal deformity, skeletal dysplasia, damage to Bruch's membrane and progressive retinal degeneration [liu-2023-loxl3-retina-abstract]. Deleting Loxl3 in Col2a1-expressing lineages causes progressive hearing loss with hair-cell and spiral-ganglion degeneration [liu-2021-loxl3-hearing-loss-abstract]. In humans, a homozygous missense variant causes autosomal recessive Stickler syndrome, a collagenopathy with vitreoretinopathy, high myopia, cleft palate and arthropathy [alzahrani-2015-loxl3-stickler-abstract]. Further compound heterozygous variants have since been reported in Stickler syndrome, including p.Trp450Arg. Molecular dynamics simulations predict that this substitution destabilizes the protein and perturbs the copper-binding pocket. A review of reported LOXL3 cases found high myopia to be the most frequent feature, followed by foveal hypoplasia [ye-2026-loxl3-stickler-md-abstract]. Biallelic null alleles cause non-lethal early-onset high myopia, unlike the lethal mouse knockout [li-2016-loxl3-myopia-abstract]. In zebrafish and mouse muscle, LoxL3-dependent oxidation of fibronectin is needed for correct myofiber anchoring and tension at the MTJ [kraftsheleg-2016-loxl3-fibronectin-abstract].

LOXL3 function partly overlaps with that of its closest paralog, LOXL2. Loxl2/Loxl3 double-knockout embryos die before birth, and ubiquitous Loxl2 expression from the ROSA26 locus rescues or strongly alleviates the perinatal lethality of Loxl3 knockouts [santamaria-2022-loxl2-loxl3-redundant-fulltext]. The tissue-specific phenotypes of LOXL3 loss may therefore reflect where LOXL3 is the dominant LOX enzyme more than a unique catalytic ability. These phenotypes match the collagen II-rich tissues (cartilage, vitreous, inner ear) that Stickler syndrome affects. If donkey LOXL3 is likewise central to equine cartilage and ocular collagen maturation, it would be a plausible candidate gene in equid craniofacial or ocular disorders, although no such link has been reported.

## 7. Intracellular Signaling Roles: STAT3, Snail/EMT, Genome Stability and Mitochondria

Several non-canonical intracellular activities have been described, almost entirely in human and mouse cells. Ma et al. found that LOXL3 binds STAT3 in the nucleus and removes acetyl groups from several acetyl-lysine sites, both by deacetylation and by deacetylimination. Surprisingly, most of this activity mapped to the N-terminal SRCR repeats rather than the oxidase domain [ma-2017-loxl3-stat3-abstract]. Modified STAT3 cannot dimerize or activate transcription, so LOXL3 restrains proliferation. In Loxl3-/- mice STAT3 stays constitutively acetylated, and naive CD4+ T cells differentiate more readily into Th17 and Treg cells [ma-2017-loxl3-stat3-abstract]. This is the basis for the donkey entry's annotation to "negative regulation of T-helper 17 cell lineage commitment" [uniprot-A0A9L0K7N3-entry]. The SRCR repeats of other LOX family members can catalyze the same reaction when overexpressed [ma-2017-loxl3-stat3-abstract], which places LOXL3 within a wider LOX-mediated lysine-modification system [serrabardenys-2022-lysine-oxidation-review-abstract].

LOXL3, like LOXL2, also interacts and cooperates with the EMT transcription factor Snail to repress E-cadherin. Snail Lys98 and Lys137 are required for this cooperation, and overexpressing LOXL3 induces EMT in epithelial cells [peinado-2005-loxl2-snail-abstract]. A LOXL3–SNAIL1–PRRX1 axis has since been linked to melanoma cell plasticity, and melanocyte-specific Loxl3 deletion delays Braf/Pten-driven melanoma and reduces metastasis [vazqueznaharro-2022-loxl3-melanoma-abstract]. In human melanoma cells, LOXL3 binds BRCA2, MSH2, SMC1A and NUMA1. Its depletion lowers BRCA2 and MSH2 levels, impairs ATR activation and double-strand-break repair, and leads to aberrant mitosis and apoptosis [santamaria-2018-loxl3-melanoma-abstract; santamaria-2018-loxl3-melanoma-fulltext]. In liver cancer cells under chemotherapy, EGFR signaling sends LOXL3 into mitochondria through TOM20. There, adenylate kinase 2 phosphorylates LOXL3 at Ser704, and phosphorylated LOXL3 blocks ubiquitination of DHODH at Lys344, stabilizing DHODH and suppressing mitochondrial ferroptosis [zhan-2023-loxl3-ferroptosis-dhodh-abstract]. In glioblastoma cells, partial LOXL3 knockout lowers α-tubulin acetylation and causes spindle abnormalities and mitotic defects. Cells with wild-type TP53 undergo apoptosis, while TP53-mutant cells slip through mitosis and become senescent [laurentino-2026-loxl3-microtubule-glioblastoma-abstract]. Oddly for a protein credited with deacetylase activity, loss of LOXL3 reduces rather than increases acetylation here, so the effect is probably indirect. Reviews of LOXL3 in cancer place these activities among broader pro-tumor functions [zhao-2025-loxl3-cancers-review-abstract; laurentino-2019-loxl3-review-abstract]. These intracellular functions are mechanistically interesting but come mostly from transformed or overexpressing cells. Whether they operate in normal tissue, and in equids, is unknown.

## 8. Open Questions

The largest gap is that donkey LOXL3 has never been studied directly. Its existence, splicing and expression are known only from genome annotation, and the 52-residue N-terminal extension and the Lys/Arg-rich insertion in SRCR2 of the predicted protein need to be checked against equid RNA-seq or proteomic evidence. It would help to establish whether the true donkey start codon matches the human Met1 and whether the SRCR2 insertion is a real, perhaps alternatively spliced, exon or an annotation artefact. A second question concerns substrate specificity. The human data on collagen types (VIII vs IV vs I vs II) come from separate assays on different variants [lee-2006-loxl3-variant-substrate-abstract; jeong-2017-loxl3-sv2-abstract], and a systematic, quantitative comparison of collagen, elastin and fibronectin as LOXL3 substrates, with identified target lysines, is still lacking. It is also unclear how LOXL3 loss lowers tubulin acetylation in glioblastoma cells [laurentino-2026-loxl3-microtubule-glioblastoma-abstract] when the protein is credited with removing acetyl groups from STAT3. Third, it remains unclear how the SRCR domains could catalyze deacetylation or deacetylimination without the canonical LTQ site [ma-2017-loxl3-stat3-abstract]. A LOXL3 structure, or a structural explanation built on the LOXL2 precursor structure [zhang-2018-loxl2-crystal-structure-abstract], would help. Fourth, the topology problem is unresolved: how a protein with a signal peptide reaches the nucleus and mitochondria [uniprot-P58215-entry; zhan-2023-loxl3-ferroptosis-dhodh-abstract]. Finally, from an equine veterinary point of view, it would be worth testing whether LOXL3 variants contribute to cleft palate, ocular disease (myopia or vitreoretinopathy), tendon or myotendinous disorders, or hearing loss in horses and donkeys. LOXL3 expression in equine tendon, cartilage and eye could be profiled, and the paralogous redundancy with LOXL2 [santamaria-2022-loxl2-loxl3-redundant-abstract] taken into account.

## 9. References

* **[alzahrani-2015-loxl3-stickler]** Alzahrani F, Al Hazzaa SA, Tayeb H, Alkuraya FS. (2015). LOXL3, encoding lysyl oxidase-like 3, is mutated in a family with autosomal recessive Stickler syndrome. *Human genetics* 134(4), 451-453. PMID: 25663169; DOI: 10.1007/s00439-015-1531-z. https://pubmed.ncbi.nlm.nih.gov/25663169/
* **[huang-2001-hloxl3-cloning]** Huang Y, Dai J, Tang R, Zhao W, Zhou Z, Wang W, Ying K, Xie Y, Mao Y. (2001). Cloning and characterization of a human lysyl oxidase-like 3 gene (hLOXL3). *Matrix biology : journal of the International Society for Matrix Biology* 20(2), 153-157. PMID: 11334717; DOI: 10.1016/s0945-053x(01)00124-x. https://pubmed.ncbi.nlm.nih.gov/11334717/
* **[jeong-2017-loxl3-sv2]** Jeong C, Kim Y. (2017). LOXL3-sv2, a novel variant of human lysyl oxidase-like 3 (LOXL3), functions as an amine oxidase. *International journal of molecular medicine* 39(3), 719-724. PMID: 28112368; DOI: 10.3892/ijmm.2017.2862. https://pubmed.ncbi.nlm.nih.gov/28112368/
* **[jourdanlesaux-2001-loxl3-expression]** Jourdan-Le Saux C, Tomsche A, Ujfalusi A, Jia L, Csiszar K. (2001). Central nervous system, uterus, heart, and leukocyte expression of the LOXL3 gene, encoding a novel lysyl oxidase-like protein. *Genomics* 74(2), 211-218. PMID: 11386757; DOI: 10.1006/geno.2001.6545. https://pubmed.ncbi.nlm.nih.gov/11386757/
* **[kraftsheleg-2016-loxl3-fibronectin]** Kraft-Sheleg O, Zaffryar-Eilot S, Genin O, Yaseen W, Soueid-Baumgarten S, Kessler O, Smolkin T, Akiri G, Neufeld G, Cinnamon Y, Hasson P. (2016). Localized LoxL3-Dependent Fibronectin Oxidation Regulates Myofiber Stretch and Integrin-Mediated Adhesion. *Developmental cell* 36(5), 550-561. PMID: 26954549; DOI: 10.1016/j.devcel.2016.02.009. https://pubmed.ncbi.nlm.nih.gov/26954549/
* **[laurentino-2019-loxl3-review]** Laurentino TS, Soares RDS, Marie SKN, Oba-Shinjo SM. (2019). LOXL3 Function Beyond Amino Oxidase and Role in Pathologies, Including Cancer. *International journal of molecular sciences* 20(14), E3587. PMID: 31340433; PMCID: PMC6678131; DOI: 10.3390/ijms20143587. https://pubmed.ncbi.nlm.nih.gov/31340433/
* **[lee-2006-loxl3-variant-substrate]** Lee JE, Kim Y. (2006). A tissue-specific variant of the human lysyl oxidase-like protein 3 (LOXL3) functions as an amine oxidase with substrate specificity. *The Journal of biological chemistry* 281(49), 37282-37290. PMID: 17018530; DOI: 10.1074/jbc.m600977200. https://pubmed.ncbi.nlm.nih.gov/17018530/
* **[li-2016-loxl3-myopia]** Li J, Gao B, Xiao X, Li S, Jia X, Sun W, Guo X, Zhang Q. (2016). Exome sequencing identified null mutations in LOXL3 associated with early-onset high myopia. *Molecular vision* 22, 161-167. PMID: 26957899; PMCID: PMC4764606. https://pubmed.ncbi.nlm.nih.gov/26957899/
* **[liu-2021-loxl3-hearing-loss]** Liu Z, Bai X, Wan P, Mo F, Chen G, Zhang J, Gao J. (2021). Targeted Deletion of Loxl3 by Col2a1-Cre Leads to Progressive Hearing Loss. *Frontiers in cell and developmental biology* 9, 683495. PMID: 34150778; PMCID: PMC8212933; DOI: 10.3389/fcell.2021.683495. https://pubmed.ncbi.nlm.nih.gov/34150778/
* **[liu-2023-loxl3-retina]** Liu Z, Mo F, Dong X, Chen G, Gao J, Zhang J. (2023). Progressive degeneration of the retina in Loxl3 mutant mouse model of Stickler syndrome. *Developmental biology* 495, 54-62. PMID: 36610533; DOI: 10.1016/j.ydbio.2023.01.002. https://pubmed.ncbi.nlm.nih.gov/36610533/
* **[liu-2025-loxl3-palatal-shelf]** Liu Z, Mo F, Dong X, Chen G, Gao J, Zhang J. (2025). Loxl3 Affects Palatal Shelf Elevation by Regulating Cell Proliferation and Collagen Deposition. *International journal of molecular sciences* 26(10), 4815. PMID: 40429955; PMCID: PMC12111807; DOI: 10.3390/ijms26104815. https://pubmed.ncbi.nlm.nih.gov/40429955/
* **[ma-2017-loxl3-stat3]** Ma L, Huang C, Wang XJ, Xin DE, Wang LS, Zou QC, Zhang YS, Tan MD, Wang YM, Zhao TC, Chatterjee D, Altura RA, Wang C, Xu YS, Yang JH, Fan YS, Han BH, Si J, Zhang X, Cheng J, Chang Z, Chin YE. (2017). Lysyl Oxidase 3 Is a Dual-Specificity Enzyme Involved in STAT3 Deacetylation and Deacetylimination Modulation. *Molecular cell* 65(2), 296-309. PMID: 28065600; DOI: 10.1016/j.molcel.2016.12.002. https://pubmed.ncbi.nlm.nih.gov/28065600/
* **[maki-2001-fourth-lox-isoenzyme]** Mäki JM, Kivirikko KI. (2001). Cloning and characterization of a fourth human lysyl oxidase isoenzyme. *The Biochemical journal* 355(Pt 2), 381-387. PMID: 11284725; PMCID: PMC1221749; DOI: 10.1042/0264-6021:3550381. https://pubmed.ncbi.nlm.nih.gov/11284725/
* **[pang-2025-loxl3-lamprey]** Pang Y, Yan Z, Gao Y, Li D, Zhao L, Ma G, Zhao Y, Du M, Sun F, Han Y. (2025). Evolutionary conservation and Immunoregulatory function of LOXL3 gene in lamprey. *Fish & shellfish immunology* 166, 110645. PMID: 40816690; DOI: 10.1016/j.fsi.2025.110645. https://pubmed.ncbi.nlm.nih.gov/40816690/
* **[peinado-2005-loxl2-snail]** Peinado H, Del Carmen Iglesias-de la Cruz M, Olmeda D, Csiszar K, Fong KS, Vega S, Nieto MA, Cano A, Portillo F. (2005). A molecular role for lysyl oxidase-like 2 enzyme in snail regulation and tumor progression. *The EMBO journal* 24(19), 3446-3458. PMID: 16096638; PMCID: PMC1276164; DOI: 10.1038/sj.emboj.7600781. https://pubmed.ncbi.nlm.nih.gov/16096638/
* **[santamaria-2018-loxl3-melanoma]** Santamaría PG, Floristán A, Fontanals-Cirera B, Vázquez-Naharro A, Santos V, Morales S, Yuste L, Peinado H, García-Gómez A, Portillo F, Hernando E, Cano A. (2018). Lysyl oxidase-like 3 is required for melanoma cell survival by maintaining genomic stability. *Cell death and differentiation* 25(5), 935-950. PMID: 29229995; PMCID: PMC5907912; DOI: 10.1038/s41418-017-0030-2. https://pubmed.ncbi.nlm.nih.gov/29229995/
* **[santamaria-2022-loxl2-loxl3-redundant]** Santamaría PG, Dubus P, Bustos-Tauler J, Floristán A, Vázquez-Naharro A, Morales S, Cano A, Portillo F. (2022). Loxl2 and Loxl3 Paralogues Play Redundant Roles during Mouse Development. *International journal of molecular sciences* 23(10), 5730. PMID: 35628534; PMCID: PMC9144032; DOI: 10.3390/ijms23105730. https://pubmed.ncbi.nlm.nih.gov/35628534/
* **[serrabardenys-2022-lysine-oxidation-review]** Serra-Bardenys G, Peiró S. (2022). Enzymatic lysine oxidation as a posttranslational modification. *The FEBS journal* 289(24), 8020-8031. PMID: 34535954; PMCID: PMC10078733; DOI: 10.1111/febs.16205. https://pubmed.ncbi.nlm.nih.gov/34535954/
* **[vazqueznaharro-2022-loxl3-melanoma]** Vázquez-Naharro A, Bustos-Tauler J, Floristán A, Yuste L, Oltra SS, Vinyals A, Moreno-Bueno G, Fabra À, Portillo F, Cano A, Santamaría PG. (2022). Loxl3 Promotes Melanoma Progression and Dissemination Influencing Cell Plasticity and Survival. *Cancers* 14(5), 1200. PMID: 35267510; PMCID: PMC8909883; DOI: 10.3390/cancers14051200. https://pubmed.ncbi.nlm.nih.gov/35267510/
* **[wang-2020-donkey-genomes]** Wang C, Li H, Guo Y, Huang J, Sun Y, Min J, Wang J, Fang X, Zhao Z, Wang S, Zhang Y, Liu Q, Jiang Q, Wang X, Guo Y, Yang C, Wang Y, Tian F, Zhuang G, Fan Y, Gao Q, Li Y, Ju Z, Li J, Li R, Hou M, Yang G, Liu G, Liu W, Guo J, Pan S, Fan G, Zhang W, Zhang R, Yu J, Zhang X, Yin Q, Ji C, Jin Y, Yue G, Liu M, Xu J, Liu S, Jordana J, Noce A, Amills M, Wu DD, Li S, Zhou X, Zhong J. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nature communications* 11(1), 6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7. https://pubmed.ncbi.nlm.nih.gov/33293529/
* **[zhan-2023-loxl3-ferroptosis-dhodh]** Zhan M, Ding Y, Huang S, Liu Y, Xiao J, Yu H, Lu L, Wang X. (2023). Lysyl oxidase-like 3 restrains mitochondrial ferroptosis to promote liver cancer chemoresistance by stabilizing dihydroorotate dehydrogenase. *Nature communications* 14(1), 3123. PMID: 37253718; PMCID: PMC10229567; DOI: 10.1038/s41467-023-38753-6. https://pubmed.ncbi.nlm.nih.gov/37253718/
* **[zhang-2015-loxl3-cleft-palate]** Zhang J, Yang R, Liu Z, Hou C, Zong W, Zhang A, Sun X, Gao J. (2015). Loss of lysyl oxidase-like 3 causes cleft palate and spinal deformity in mice. *Human molecular genetics* 24(21), 6174-6185. PMID: 26307084; PMCID: PMC4599675; DOI: 10.1093/hmg/ddv333. https://pubmed.ncbi.nlm.nih.gov/26307084/
* **[zhang-2016-loxl3-lung]** Zhang J, Liu Z, Zhang T, Lin Z, Li Z, Zhang A, Sun X, Gao J. (2016). Loss of Lysyl Oxidase-like 3 Attenuates Embryonic Lung Development in Mice. *Scientific reports* 6, 33856. PMID: 27645581; PMCID: PMC5029289; DOI: 10.1038/srep33856. https://pubmed.ncbi.nlm.nih.gov/27645581/
* **[zhang-2018-loxl2-crystal-structure]** Zhang X, Wang Q, Wu J, Wang J, Shi Y, Liu M. (2018). Crystal structure of human lysyl oxidase-like 2 (hLOXL2) in a precursor state. *Proceedings of the National Academy of Sciences of the United States of America* 115(15), 3828-3833. PMID: 29581294; PMCID: PMC5899467; DOI: 10.1073/pnas.1720859115. https://pubmed.ncbi.nlm.nih.gov/29581294/
* **[zhao-2025-loxl3-cancers-review]** Zhao D, Su P, Peng X, Cheng X, Li B, Tang XM, Huang S, Li Z, Cao H, Xiong W. (2025). The function and mechanisms of action of lysyl oxidase-like 3 (LOXL3) in cancers. *PeerJ* 13, e20274. PMID: 41250755; PMCID: PMC12619944; DOI: 10.7717/peerj.20274. https://pubmed.ncbi.nlm.nih.gov/41250755/
* **[laurentino-2026-loxl3-microtubule-glioblastoma]** Laurentino TS, Soares RDS, Lerario AM, Cintra RC, Marie SKN, Oba-Shinjo SM. (2026). Reduced LOXL3 Expression Disrupts Microtubule Acetylation and Drives TP53-Dependent Cell Fate in Glioblastoma. *Cells* 15(3), 219. PMID: 41677586; PMCID: PMC12896791; DOI: 10.3390/cells15030219. https://pubmed.ncbi.nlm.nih.gov/41677586/
* **[melamed-2023-fibronectin-fibrillogenesis]** Melamed S, Zaffryar-Eilot S, Nadjar-Boger E, Aviram R, Zhao H, Yaseen-Badarne W, Kalev-Altman R, Sela-Donenfeld D, Lewinson O, Astrof S, Hasson P, Wolfenson H. (2023). Initiation of fibronectin fibrillogenesis is an enzyme-dependent process. *Cell reports* 42(5), 112473. PMID: 37148241; PMCID: PMC10323212; DOI: 10.1016/j.celrep.2023.112473. https://pubmed.ncbi.nlm.nih.gov/37148241/
* **[ye-2026-loxl3-stickler-md]** Ye M, Li S, Li R, Zhang W, He X, Ma L, Li Q, Zhuang W. (2026). Integrated genetic identification and molecular dynamics simulations in a novel &lt;i&gt;LOXL3&lt;/i&gt; genetic mutation associated with Stickler syndrome. *Frontiers in genetics* 17, 1813104. PMID: 42598702; PMCID: PMC13472571; DOI: 10.3389/fgene.2026.1813104. https://pubmed.ncbi.nlm.nih.gov/42598702/
* **[uniprot-A0A9L0K7N3-entry]** UniProt Consortium. UniProtKB/TrEMBL entry A0A9L0K7N3 (A0A9L0K7N3_EQUAS), Lysyl oxidase homolog, *Equus asinus*; entry version 15 (02-SEP-2026). https://rest.uniprot.org/uniprotkb/A0A9L0K7N3.txt
* **[uniprot-P58215-entry]** UniProt Consortium. UniProtKB/Swiss-Prot entry P58215 (LOXL3_HUMAN), Lysyl oxidase homolog 3, *Homo sapiens*. https://rest.uniprot.org/uniprotkb/P58215.txt


## Citations

1. alzahrani-2015-loxl3-stickler-abstract.md
2. alzahrani-2015-loxl3-stickler-summary.md
3. donkey_LOXL3.fasta
4. huang-2001-hloxl3-cloning-abstract.md
5. huang-2001-hloxl3-cloning-summary.md
6. human_LOXL3.fasta
7. jeong-2017-loxl3-sv2-abstract.md
8. jeong-2017-loxl3-sv2-summary.md
9. jourdanlesaux-2001-loxl3-expression-abstract.md
10. jourdanlesaux-2001-loxl3-expression-summary.md
11. kraftsheleg-2016-loxl3-fibronectin-abstract.md
12. kraftsheleg-2016-loxl3-fibronectin-summary.md
13. laurentino-2019-loxl3-review-abstract.md
14. laurentino-2019-loxl3-review-fulltext.txt
15. laurentino-2019-loxl3-review-summary.md
16. laurentino-2026-loxl3-microtubule-glioblastoma-abstract.md
17. laurentino-2026-loxl3-microtubule-glioblastoma-fulltext.txt
18. laurentino-2026-loxl3-microtubule-glioblastoma-summary.md
19. lee-2006-loxl3-variant-substrate-abstract.md
20. lee-2006-loxl3-variant-substrate-summary.md
21. li-2016-loxl3-myopia-abstract.md
22. li-2016-loxl3-myopia-fulltext.txt
23. li-2016-loxl3-myopia-summary.md
24. liu-2021-loxl3-hearing-loss-abstract.md
25. liu-2021-loxl3-hearing-loss-fulltext.txt
26. liu-2021-loxl3-hearing-loss-summary.md
27. liu-2023-loxl3-retina-abstract.md
28. liu-2023-loxl3-retina-summary.md
29. liu-2025-loxl3-palatal-shelf-abstract.md
30. liu-2025-loxl3-palatal-shelf-fulltext.txt
31. liu-2025-loxl3-palatal-shelf-summary.md
32. ma-2017-loxl3-stat3-abstract.md
33. ma-2017-loxl3-stat3-summary.md
34. maki-2001-fourth-lox-isoenzyme-abstract.md
35. maki-2001-fourth-lox-isoenzyme-summary.md
36. melamed-2023-fibronectin-fibrillogenesis-abstract.md
37. melamed-2023-fibronectin-fibrillogenesis-fulltext.txt
38. melamed-2023-fibronectin-fibrillogenesis-summary.md
39. metadata.json
40. pang-2025-loxl3-lamprey-abstract.md
41. pang-2025-loxl3-lamprey-summary.md
42. peinado-2005-loxl2-snail-abstract.md
43. peinado-2005-loxl2-snail-summary.md
44. santamaria-2018-loxl3-melanoma-abstract.md
45. santamaria-2018-loxl3-melanoma-fulltext.txt
46. santamaria-2018-loxl3-melanoma-summary.md
47. santamaria-2022-loxl2-loxl3-redundant-abstract.md
48. santamaria-2022-loxl2-loxl3-redundant-fulltext.txt
49. santamaria-2022-loxl2-loxl3-redundant-summary.md
50. serrabardenys-2022-lysine-oxidation-review-abstract.md
51. serrabardenys-2022-lysine-oxidation-review-fulltext.txt
52. serrabardenys-2022-lysine-oxidation-review-summary.md
53. uniprot-A0A9L0K7N3-entry.txt
54. uniprot-P58215-entry.txt
55. vazqueznaharro-2022-loxl3-melanoma-abstract.md
56. vazqueznaharro-2022-loxl3-melanoma-fulltext.txt
57. vazqueznaharro-2022-loxl3-melanoma-summary.md
58. wang-2020-donkey-genomes-abstract.md
59. wang-2020-donkey-genomes-fulltext.txt
60. wang-2020-donkey-genomes-summary.md
61. ye-2026-loxl3-stickler-md-abstract.md
62. ye-2026-loxl3-stickler-md-fulltext.txt
63. ye-2026-loxl3-stickler-md-summary.md
64. zhan-2023-loxl3-ferroptosis-dhodh-abstract.md
65. zhan-2023-loxl3-ferroptosis-dhodh-fulltext.txt
66. zhan-2023-loxl3-ferroptosis-dhodh-summary.md
67. zhang-2015-loxl3-cleft-palate-abstract.md
68. zhang-2015-loxl3-cleft-palate-fulltext.txt
69. zhang-2015-loxl3-cleft-palate-summary.md
70. zhang-2016-loxl3-lung-abstract.md
71. zhang-2016-loxl3-lung-fulltext.txt
72. zhang-2016-loxl3-lung-summary.md
73. zhang-2018-loxl2-crystal-structure-abstract.md
74. zhang-2018-loxl2-crystal-structure-fulltext.txt
75. zhang-2018-loxl2-crystal-structure-summary.md
76. zhao-2025-loxl3-cancers-review-abstract.md
77. zhao-2025-loxl3-cancers-review-fulltext.txt
78. zhao-2025-loxl3-cancers-review-summary.md