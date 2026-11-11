---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T01:35:50.226049'
end_time: '2026-10-26T01:43:56.121471'
duration_seconds: 485.9
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: CC2D2A
  gene_symbol: CC2D2A
  uniprot_accession: A0A5F5PJ44
  protein_description: 'SubName: Full=Coiled-coil and C2 domain containing 2A {ECO:0000313|Ensembl:ENSECAP00000048367.2};'
  gene_info: Name=CC2D2A {ECO:0000313|VGNC:VGNC:16103};
  organism_full: Equus caballus (Horse).
  protein_family: Not specified in UniProt
  protein_domains: C2_dom. (IPR000008); C2_domain_sf. (IPR035892); CC2D2AN-C2. (IPR028928);
    CEP76_C. (IPR056288); CEPT76/DRC7_peptidase-like_dom. (IPR056290)
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
citation_count: 75
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A5F5PJ44
- **Protein Description:** SubName: Full=Coiled-coil and C2 domain containing 2A {ECO:0000313|Ensembl:ENSECAP00000048367.2};
- **Gene Information:** Name=CC2D2A {ECO:0000313|VGNC:VGNC:16103};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Not specified in UniProt
- **Key Domains:** C2_dom. (IPR000008); C2_domain_sf. (IPR035892); CC2D2AN-C2. (IPR028928); CEP76_C. (IPR056288); CEPT76/DRC7_peptidase-like_dom. (IPR056290)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "CC2D2A" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'CC2D2A' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **CC2D2A** (gene ID: CC2D2A, UniProt: A0A5F5PJ44) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# CC2D2A (coiled-coil and C2 domain-containing protein 2A) in the horse, *Equus caballus* (UniProt A0A5F5PJ44)

## 1. Introduction and summary

UniProt A0A5F5PJ44 is an unreviewed TrEMBL entry for horse CC2D2A. It has protein-existence level 4 ("predicted"), is 1480 residues long, and was annotated automatically from the Thoroughbred reference genome (Ensembl ENSECAG00000025115, chromosome 3, VGNC:16103). The entry carries no curated functional annotation [uniprot-A0A5F5PJ44-record]. The identity check passed. The gene symbol, the protein name and the domain architecture all match the well-studied vertebrate gene CC2D2A, also called MKS6 (Meckel syndrome 6). The domains are an N-terminal CC2D2AN-C2 module, coiled-coil segments, a C2 domain (residues 902–1062), and a CEP76-like transglutaminase/peptidase-like region. The PANTHER family is "tectonic-like complex component" [uniprot-A0A5F5PJ44-record]. I aligned the horse sequence globally with human CC2D2A (Q9P2K1, 1620 aa). 1335 of the 1480 horse residues are identical (about 90%). Horse residues 99–1480 line up without gaps against human residues 239–1620, so every annotated domain is conserved. The horse model lacks the first ~49 human residues and an internal stretch of about 93 residues (human 146–239). This most likely reflects a difference in isoform or gene-model prediction rather than a real protein difference. My PubMed search for CC2D2A together with horse, equine or *Equus* found no publications. Nothing in this report therefore comes from experiments on the horse protein. The functional account below is inferred from orthologs in human, mouse, zebrafish, *Caenorhabditis elegans* and other ciliated eukaryotes. Given the conservation and the fact that CC2D2A is present in nearly every ciliated lineage [barker-2014-tz-evolution-abstract], that inference is well founded.

Across these organisms the picture is consistent. CC2D2A is a non-enzymatic, membrane-associated scaffold of the ciliary **transition zone** (TZ). The TZ is the short region at the base of the cilium where Y-shaped links tie the axonemal microtubule doublets to the ciliary membrane. CC2D2A is a core subunit of the MKS module, also called the tectonic or B9 complex. Together with TCTN1–3, MKS1, B9D1/B9D2, TMEM67, TMEM216, TMEM231 and others, this complex forms a diffusion barrier and gate that keeps the ciliary membrane separate from the plasma membrane [garciagonzalo-2011-tectonic-abstract; chih-2011-mks-b9-complex-abstract; williams-2011-mks-nphp-modules-abstract]. Without CC2D2A, cilia form poorly or not at all in a tissue-dependent way. Where cilia do form, they lose signalling membrane proteins such as Arl13b, adenylyl cyclase 3, polycystin-2 and Smoothened, and Hedgehog signalling is disrupted [garciagonzalo-2011-tectonic-fulltext; veleri-2014-subdistal-abstract]. Further studies give CC2D2A two more roles: assembling the subdistal appendages of the mother centriole [veleri-2014-subdistal-abstract], and organizing the vesicle-docking and fusion machinery at the periciliary membrane. That second role links Rab8-dependent delivery of cargo such as opsin to the ciliary gate [bachmanngagescu-2015-ninl-abstract; ojedanaharros-2017-snare-abstract]. In humans, null alleles cause the lethal Meckel syndrome and hypomorphic alleles cause Joubert syndrome and related disorders [tallila-2008-meckel-abstract; gorden-2008-joubert-cep290-abstract; mougouzerelli-2009-genotype-abstract].

## 2. Gene identity, domain architecture and evolutionary conservation

CC2D2A was first named as a disease gene in 2008, in a consanguineous family with intellectual disability and retinitis pigmentosa. A splice mutation there causes exon 19 to be skipped and yields a truncated protein without the C2 domain. Conservation analysis in the same study pointed to a functional C-terminal region in addition to the C2 domain [noor-2008-retinitis-abstract]. C2 domains are classically Ca²⁺- and phospholipid-binding membrane-targeting modules. This led to early suggestions that CC2D2A takes part in Ca²⁺-dependent signal transduction [noor-2008-retinitis-abstract; tallila-2008-meckel-abstract]. No later study has shown that CC2D2A binds calcium or specific lipids, so that idea remains a hypothesis.

Zhang and Aravind used sensitive sequence-profile and structural analysis to find two more features. The first is a transglutaminase-like (TGL) peptidase domain shared with CEP76, CC2D2B and CCDC135. The second is a set of additional C2 domains that are widespread in TZ proteins [zhang-2012-tgl-peptidase-abstract]. In all members of the CC2D2A/MKS6 clade, the catalytic residues of the TGL domain are missing ("all representatives of the CC2D2A/MKS6 clade are inactive"). In CEP76, by contrast, some animal sequences keep an intact active site [zhang-2012-tgl-peptidase-fulltext]. The authors proposed that the inactive TGL domains bind peptides and mediate interactions during ciliogenesis, while the C2 domains contact the membrane within the Y-link [zhang-2012-tgl-peptidase-abstract]. Veleri and colleagues likewise describe the CC2D2A TGL domain as catalytically inactive, perhaps "a peptide-binding interface for microtubules" [veleri-2014-subdistal-fulltext]. The horse entry's "CEP76_C" and "CEPT76/DRC7 peptidase-like" InterPro domains [uniprot-A0A5F5PJ44-record] correspond to this inactive module. The answer to the question "what reaction does it catalyse" is therefore that CC2D2A is not expected to be an enzyme. It is a structural and adaptor protein.

Comparative genomics across eukaryotic supergroups shows that CC2D2A belongs to a core of six TZ proteins: TMEM67, CC2D2A, B9D1, B9D2, AHI1 and one tectonic. These proteins are found in most ciliated organisms and not in non-ciliated ones. Their loss in non-seed land plants coincides with loss of the TZ Y-links, which suggests that the MKS module builds or regulates the Y-links [barker-2014-tz-evolution-abstract]. In *C. elegans*, CC2D2A co-evolves with the MKS core [lambacher-2016-tmem107-fulltext]. The deep conservation, and the 90% identity between horse and human, make it very likely that horse CC2D2A works the same way as its well-characterized orthologs.

## 3. Localization: the ciliary transition zone and the mother centriole

The main site of action is the ciliary base. Recombinant human CC2D2A localizes to the basal body in ciliated cells and colocalizes with CEP290 [gorden-2008-joubert-cep290-abstract]. In mouse cells, endogenous Cc2d2a sits at the transition zone together with the tectonic-complex proteins Tctn1–3, Mks1, Tmem67, Cep290 and B9d1. It still reaches the TZ in Tctn1⁻/⁻ fibroblasts, so its targeting does not depend on Tctn1 [garciagonzalo-2011-tectonic-fulltext]. In zebrafish, Cc2d2a localizes to the photoreceptor connecting cilium, which corresponds to the TZ, and to the TZ of other ciliated cells [bachmanngagescu-2011-zebrafish-rab8-abstract]. In *C. elegans* sensory neurons, MKS-6::GFP marks the TZ and lies apart from the intraflagellar transport (IFT) proteins concentrated at the basal body and transition fibres [williams-2011-mks-nphp-modules-fulltext]. Photobleaching shows that MKS-6 is immobile at the TZ, anchored to the TZ membrane as a membrane-associated, non-transmembrane protein [lambacher-2016-tmem107-fulltext]. Within the worm MKS-module hierarchy, MKS-6 sits in the outermost "Layer 3". It needs upstream factors to localize but is not itself required to recruit other MKS proteins [lambacher-2016-tmem107-fulltext]. In mammalian cells, by contrast, TMEM231, B9D1 and CC2D2A depend on each other and on Septin 2 to reach the TZ [chih-2011-mks-b9-complex-abstract]. Super-resolution (STORM) imaging shows that MKS- and NPHP-module proteins form nested rings with nine-fold symmetry at the TZ, matching the arrangement of the Y-links [shi-2017-superres-abstract]. The TZ location is also conserved in insects. In *Drosophila*, Cc2d2a sits at the TZ at the base of chordotonal sensory cilia. In spermatocytes it colocalizes with Tctn, B9d1 and Mks1 at the tips of the centrioles, and in elongating spermatids it spreads along the ciliary membrane cap [vieillard-2016-drosophila-tz-fulltext]. Its recruitment there depends on other MKS-module members: a combined B9d2/tctn null allele causes loss of all other MKS components from the TZ. MKS proteins in turn act downstream of Cby and Dila (Azi1), which together build the fly TZ [vieillard-2016-drosophila-tz-fulltext; vieillard-2016-drosophila-tz-abstract].

There is also a second, centriolar location. Immuno-electron microscopy in mouse fibroblasts placed CC2D2A on the subdistal appendages of the mother centriole, with a staining pattern resembling that of centriolin and Odf2 [veleri-2014-subdistal-fulltext]. The broader NPHP-JBTS-MKS proteomic network connects the MKS module, with CC2D2A copurifying with Mks1, to Hedgehog signalling [sang-2011-network-fulltext].

## 4. Molecular complexes and interaction partners

CC2D2A is a stoichiometric subunit of the MKS/tectonic complex. Tandem-affinity purification of Tctn1 recovered Cc2d2a among the most abundant partners, alongside Mks1, Cep290, Tctn2 and B9d1. Size fractionation showed these proteins co-migrating in a high-molecular-weight complex [garciagonzalo-2011-tectonic-fulltext]. An independent RNAi, proteomics and genetics study described the same nine-protein assembly, which contains TMEM231, B9D1 and CC2D2A [chih-2011-mks-b9-complex-abstract]. Mks1 pulldowns also recovered CC2D2A [sang-2011-network-fulltext]. In *C. elegans*, MKS-6 belongs genetically to the MKS/MKSR module. It acts redundantly with the NPHP module (NPHP-1, NPHP-4), and MKS-5/RPGRIP1L connects the two modules [williams-2011-mks-nphp-modules-fulltext]. Consistent with this, mutations within the MKS module show no added effect in worms or mice, whereas combining MKS- and NPHP-module mutations is synergistic [yee-2015-genetic-interactions-abstract]. The worm *nphp-2*/inversin gene is a further modifier of *mks-6* [warburtonpitt-2012-nphp2-abstract].

CC2D2A also has direct binary partners. It binds CEP290 in yeast two-hybrid and GST pull-down assays, and the two genes interact genetically in zebrafish pronephros [gorden-2008-joubert-cep290-abstract]. A targeted ciliary yeast two-hybrid screen found that coiled-coil domains 1 and 2 of CC2D2A bind both isoforms of the centrosomal protein NINL (Ninein-like) [bachmanngagescu-2015-ninl-fulltext]. NINL in turn binds MICAL3, a Rab8-interacting protein that acts in vesicle docking and fusion. This creates a chain of physical links, CC2D2A–NINL–MICAL3–RAB8A, from the TZ to incoming cargo vesicles. *ninl* knockdown in zebrafish phenocopies the loss of *cc2d2a* and enhances it [bachmanngagescu-2015-ninl-abstract].

## 5. Biological role I: gating ciliary membrane composition and Hedgehog signalling

The best-supported function of CC2D2A is to maintain the cilium as a separate membrane compartment. Disrupting the MKS/B9 complex in cultured cells reduced cilia formation, sped up diffusion of membrane proteins into the cilium, and raised the amount of plasma-membrane protein inside it. The complex therefore acts as a diffusion barrier [chih-2011-mks-b9-complex-abstract]. Fibroblasts lacking Cc2d2a can still build cilia, but those cilia lack adenylyl cyclase 3 and polycystin-2. After Hedgehog agonist treatment, Smoothened enters these cilia even less well than in Tctn1 or Tctn2 mutants [garciagonzalo-2011-tectonic-fulltext]. A rod-photoreceptor-specific Tctn1 knockout removed the whole tectonic complex, Cc2d2a included, from the TZ while barely changing TZ ultrastructure. Non-resident membrane proteins then built up in the cilium and rhodopsin crossed the TZ faster. This is direct evidence that the complex physically slows membrane-protein diffusion [truong-2023-tectonic-photoreceptor-abstract]. In *C. elegans*, MKS-6 together with NPHP-4 is needed to attach the basal body and TZ to the membrane and to establish the ciliary gate [williams-2011-mks-nphp-modules-fulltext].

Hedgehog signalling needs Smoothened to accumulate in the cilium, so CC2D2A loss interferes with this pathway. Cc2d2a⁻/⁻ mouse embryos show randomized left–right axes, holoprosencephaly, microphthalmia and loss of neural-tube cilia [garciagonzalo-2011-tectonic-fulltext]. A second knockout shows exencephaly that is attributed to defective cilia-dependent Shh signalling [veleri-2014-subdistal-abstract]. In the pathway, then, CC2D2A acts as a structural gatekeeper upstream of Smoothened. It is not a signalling component in its own right.

## 6. Biological role II: ciliogenesis, subdistal appendages and vesicle fusion at the ciliary base

CC2D2A is clearly required for cilium assembly in some contexts, though how strongly varies with cell type and model. Fibroblasts from Meckel fetuses lack cilia [tallila-2008-meckel-abstract]. In one Cc2d2a-null mouse, cilia are absent from the embryonic node, from other somatic tissues and from fibroblasts. Those fibroblasts keep their mother centrioles but lose the subdistal-appendage markers Odf2 and trichoplein and show less ninein, and electron microscopy shows missing or abnormal subdistal appendages. From this the authors conclude that CC2D2A is needed to assemble the subdistal appendages that anchor microtubules and prepare the mother centriole for axoneme growth [veleri-2014-subdistal-abstract; veleri-2014-subdistal-fulltext]. The two mouse studies disagree on whether Cc2d2a-null fibroblasts can make cilia: one finds normal ciliogenesis with altered membrane composition, the other complete absence [garciagonzalo-2011-tectonic-fulltext; bachmanngagescu-2015-ninl-fulltext]. Conditional Mks6 (Cc2d2a) mouse mutants show cilia loss restricted to particular cell types, cystic kidneys and severe retinal degeneration with mislocalized phototransduction proteins, but no anosmia or obesity. This points to tissue-specific roles [lewis-2019-mks6-abstract]. In zebrafish and *C. elegans*, cilia largely form without CC2D2A [bachmanngagescu-2011-zebrafish-rab8-abstract; williams-2011-mks-nphp-modules-fulltext]. Removing the MKS module in *Drosophila* likewise causes only mild TZ and axoneme defects [vieillard-2016-drosophila-tz-abstract]. Outside vertebrates, then, CC2D2A and its MKS-module partners seem to tune TZ function more than they are needed to build cilia. Knockdown of the C2-domain region in kidney IMCD-3 cells changes cilia morphology and the expression of genes for IFT and Hedgehog signalling [jayarajan-2024-c2-abstract].

Work in zebrafish photoreceptors shows a role in delivering membrane to the cilium. Without *cc2d2a*, rod and cone outer segments are disorganized, opsins are mislocalized, vesicles pile up near the connecting cilium, and Rab8 is mislocalized. Partial *rab8* knockdown makes the retinal and kidney phenotypes worse [bachmanngagescu-2011-zebrafish-rab8-abstract]. Live imaging and correlative light/electron microscopy narrowed the defect to the final step of opsin-carrier-vesicle trafficking, fusion. Loss of Cc2d2a disorganizes the fusion machinery at the periciliary membrane. The t-SNAREs SNAP25 and Syntaxin3 and the exocyst subunit Exoc4 are mislocalized or lost. SNAP25 at the synapse is unaffected, and the SNAP25 defect does not occur in *ift88* mutants, so it is specific to Cc2d2a loss rather than to cilia loss [ojedanaharros-2017-snare-abstract; ojedanaharros-2017-snare-fulltext]. The Rab8 defects appear to be secondary [ojedanaharros-2017-snare-abstract]. Taken with the NINL–MICAL3–RAB8A chain, these data suggest that CC2D2A provides a docking platform where ciliary-directed vesicles can be captured and fused just below the gate [bachmanngagescu-2015-ninl-abstract].

## 7. Disease relevance and genotype–phenotype relationships

Studies of human disease also shed light on how the protein works. CC2D2A is the MKS6 locus, and truncating alleles cause Meckel syndrome [tallila-2008-meckel-abstract; mougouzerelli-2009-genotype-abstract]. It is one of the most common causes of Joubert syndrome [gorden-2008-joubert-cep290-abstract; bachmanngagescu-2015-ninl-fulltext] and a minor cause of COACH syndrome [doherty-2010-coach-abstract]. Null alleles cause the lethal Meckel phenotype, while missense or hypomorphic alleles cause the survivable Joubert phenotype [mougouzerelli-2009-genotype-abstract]. Truncating alleles are linked to more severe disease, and basal exon skipping in kidney may partly rescue function [barrosogil-2021-variants-abstract]. Missense variants cluster in the coiled-coil and C2 domains and in the C-terminal region. This identifies those regions as functionally important, consistent with the NINL-binding coiled coils and the membrane-binding C2 domain [bachmanngagescu-2012-genotype-abstract]. Large cohorts give differing pictures of the clinical spectrum. One reports ventriculomegaly and seizures [bachmanngagescu-2012-genotype-abstract]. Another reports generally good neurodevelopmental outcomes, with the homozygous p.Arg950* allele being more severe [harion-2023-jbts-abstract]. Many photoreceptor and kidney features in patients follow from the TZ and vesicle-fusion roles described above. No naturally occurring CC2D2A variant has been reported in horses in the literature I searched.

## 8. Synthesis for functional annotation of horse CC2D2A

Based on orthology, horse CC2D2A (A0A5F5PJ44) should be annotated as follows. **Molecular function:** a non-catalytic structural and adaptor protein. Its TGL/peptidase-like domain is predicted to be inactive [zhang-2012-tgl-peptidase-fulltext]. It binds CEP290 and NINL [gorden-2008-joubert-cep290-abstract; bachmanngagescu-2015-ninl-fulltext] and associates with membranes through its C2 domains [zhang-2012-tgl-peptidase-abstract; lambacher-2016-tmem107-fulltext]. **Cellular component:** the ciliary transition zone, as part of the MKS/tectonic complex [garciagonzalo-2011-tectonic-abstract; chih-2011-mks-b9-complex-abstract], and the subdistal appendages of the mother centriole [veleri-2014-subdistal-abstract]. **Biological process:** maintaining the ciliary diffusion barrier and controlling which proteins reach the ciliary membrane [chih-2011-mks-b9-complex-abstract; truong-2023-tectonic-photoreceptor-abstract]; cilium assembly, in a tissue-dependent way [garciagonzalo-2011-tectonic-abstract; veleri-2014-subdistal-abstract]; protein transport to the cilium through fusion of Rab8-dependent vesicles at the periciliary membrane [ojedanaharros-2017-snare-abstract]; and, as a consequence, smoothened/Hedgehog signalling [garciagonzalo-2011-tectonic-fulltext]. Annotations of a Ca²⁺-dependent signalling role [noor-2008-retinitis-abstract] or of peptidase activity are not supported by experiment and should be avoided.

## Open Questions

Several questions are still open. Nobody has studied CC2D2A experimentally in the horse. Equine transcript data are needed to settle whether the horse gene model really lacks the N-terminal and internal segments present in human isoform 1, or whether a full-length isoform was missed [uniprot-A0A5F5PJ44-record]. It is still unknown whether the CC2D2A C2 domains bind Ca²⁺ or particular phosphoinositides; the original Ca²⁺-signalling proposal [noor-2008-retinitis-abstract] has not been tested. The inactive TGL domain is proposed to bind peptides or microtubules [zhang-2012-tgl-peptidase-abstract; veleri-2014-subdistal-fulltext], but its ligand has not been identified. Nor has anyone determined a high-resolution structure showing where CC2D2A sits in the nine-fold TZ rings or the Y-links [shi-2017-superres-abstract; barker-2014-tz-evolution-abstract]. The two mouse knockouts disagree about whether Cc2d2a is needed for ciliogenesis in fibroblasts [garciagonzalo-2011-tectonic-fulltext; veleri-2014-subdistal-abstract], and it is unclear how its subdistal-appendage role fits with its TZ location. Genetic background or allele design might explain the difference. Two models of the photoreceptor defect also need to be reconciled. In one, CC2D2A directly organizes the SNARE and exocyst machinery [ojedanaharros-2017-snare-abstract]. In the other, defects arise because the diffusion barrier fails [truong-2023-tectonic-photoreceptor-abstract]. I also looked for studies of CC2D2A in protists (*Chlamydomonas*, *Paramecium*, *Tetrahymena*, trypanosomes) and found none that tested the protein directly. Recent work on ciliary shedding in *Paramecium*, for example, examined other TZ proteins but not CC2D2A, so evidence from early-branching eukaryotes rests on comparative genomics alone [barker-2014-tz-evolution-abstract]. Useful next steps would be AlphaFold-multimer modelling of horse CC2D2A with MKS-module partners, analysis of equine RNA-seq for isoform structure, and screening of horse populations for CC2D2A variants in cases of congenital retinal, renal or cerebellar disease.

## References

* **bachmanngagescu-2011-zebrafish-rab8**: Bachmann-Gagescu R, Phelps IG, Stearns G, Link BA, Brockerhoff SE, Moens CB, Doherty D. The ciliopathy gene cc2d2a controls zebrafish photoreceptor outer segment development through a role in Rab8-dependent vesicle trafficking. *Hum Mol Genet* 2011;20:4041-55. PMID: 21816947. DOI: 10.1093/hmg/ddr332. PMCID: PMC3177654. https://pubmed.ncbi.nlm.nih.gov/21816947/
* **bachmanngagescu-2012-genotype**: Bachmann-Gagescu R, Ishak GE, Dempsey JC, Adkins J, O'Day D, Phelps IG, Gunay-Aygun M, Kline AD, Szczaluba K, Martorell L, Alswaid A, Alrasheed S, Pai S, Izatt L, Ronan A, Parisi MA, Mefford H, Glass I, Doherty D. Genotype-phenotype correlation in CC2D2A-related Joubert syndrome reveals an association with ventriculomegaly and seizures. *J Med Genet* 2012;49:126-37. PMID: 22241855. DOI: 10.1136/jmedgenet-2011-100552. https://pubmed.ncbi.nlm.nih.gov/22241855/
* **bachmanngagescu-2015-ninl**: Bachmann-Gagescu R, Dona M, Hetterschijt L, Tonnaer E, Peters T, de Vrieze E, Mans DA, van Beersum SE, Phelps IG, Arts HH, Keunen JE, Ueffing M, Roepman R, Boldt K, Doherty D, Moens CB, Neuhauss SC, Kremer H, van Wijk E. The Ciliopathy Protein CC2D2A Associates with NINL and Functions in RAB8-MICAL3-Regulated Vesicle Trafficking. *PLoS Genet* 2015;11:e1005575. PMID: 26485645. DOI: 10.1371/journal.pgen.1005575. PMCID: PMC4617701. https://pubmed.ncbi.nlm.nih.gov/26485645/
* **barker-2014-tz-evolution**: Barker AR, Renzaglia KS, Fry K, Dawe HR. Bioinformatic analysis of ciliary transition zone proteins reveals insights into the evolution of ciliopathy networks. *BMC Genomics* 2014;15:531. PMID: 24969356. DOI: 10.1186/1471-2164-15-531. PMCID: PMC4092220. https://pubmed.ncbi.nlm.nih.gov/24969356/
* **barrosogil-2021-variants**: Barroso-Gil M, Olinger E, Ramsbottom SA, Molinari E, Miles CG, Sayer JA. Update of genetic variants in CEP120 and CC2D2A-With an emphasis on genotype-phenotype correlations, tissue specific transcripts and exploring mutation specific exon skipping therapies. *Mol Genet Genomic Med* 2021;9:e1603. PMID: 33486889. DOI: 10.1002/mgg3.1603. PMCID: PMC8683696. https://pubmed.ncbi.nlm.nih.gov/33486889/
* **chih-2011-mks-b9-complex**: Chih B, Liu P, Chinn Y, Chalouni C, Komuves LG, Hass PE, Sandoval W, Peterson AS. A ciliopathy complex at the transition zone protects the cilia as a privileged membrane domain. *Nat Cell Biol* 2011;14:61-72. PMID: 22179047. DOI: 10.1038/ncb2410. https://pubmed.ncbi.nlm.nih.gov/22179047/
* **doherty-2010-coach**: Doherty D, Parisi MA, Finn LS, Gunay-Aygun M, Al-Mateen M, Bates D, Clericuzio C, Demir H, Dorschner M, van Essen AJ, Gahl WA, Gentile M, Gorden NT, Hikida A, Knutzen D, Ozyurek H, Phelps I, Rosenthal P, Verloes A, Weigand H, Chance PF, Dobyns WB, Glass IA. Mutations in 3 genes (MKS3, CC2D2A and RPGRIP1L) cause COACH syndrome (Joubert syndrome with congenital hepatic fibrosis). *J Med Genet* 2010;47:8-21. PMID: 19574260. DOI: 10.1136/jmg.2009.067249. PMCID: PMC3501959. https://pubmed.ncbi.nlm.nih.gov/19574260/
* **garciagonzalo-2011-tectonic**: Garcia-Gonzalo FR, Corbit KC, Sirerol-Piquer MS, Ramaswami G, Otto EA, Noriega TR, Seol AD, Robinson JF, Bennett CL, Josifova DJ, García-Verdugo JM, Katsanis N, Hildebrandt F, Reiter JF. A transition zone complex regulates mammalian ciliogenesis and ciliary membrane composition. *Nat Genet* 2011;43:776-84. PMID: 21725307. DOI: 10.1038/ng.891. PMCID: PMC3145011. https://pubmed.ncbi.nlm.nih.gov/21725307/
* **gorden-2008-joubert-cep290**: Gorden NT, Arts HH, Parisi MA, Coene KL, Letteboer SJ, van Beersum SE, Mans DA, Hikida A, Eckert M, Knutzen D, Alswaid AF, Ozyurek H, Dibooglu S, Otto EA, Liu Y, Davis EE, Hutter CM, Bammler TK, Farin FM, Dorschner M, Topçu M, Zackai EH, Rosenthal P, Owens KN, Katsanis N, Vincent JB, Hildebrandt F, Rubel EW, Raible DW, Knoers NV, Chance PF, Roepman R, Moens CB, Glass IA, Doherty D. CC2D2A is mutated in Joubert syndrome and interacts with the ciliopathy-associated basal body protein CEP290. *Am J Hum Genet* 2008;83:559-71. PMID: 18950740. DOI: 10.1016/j.ajhg.2008.10.002. PMCID: PMC2668034. https://pubmed.ncbi.nlm.nih.gov/18950740/
* **harion-2023-jbts**: Harion M, Qebibo L, Riquet A, Rougeot C, Afenjar A, Garel C, Louha M, Lacaze E, Audic-Gérard F, Barth M, Berquin P, Bonneau D, Bourdain F, Busa T, Colin E, Cuisset JM, Des Portes V, Dorison N, Francannet C, Héron B, Laroche C, Lebrun M, Métreau J, Odent S, Pasquier L, Trujillo YP, Perrin L, Pinson L, Rivier F, Sigaudy S, Thauvin-Robinet C, Louvier UW, Labayle O, Rodriguez D, Valence S, Burglen L. New insights into CC2D2A-related Joubert syndrome. *J Med Genet* 2023;60:578-586. PMID: 36319078. DOI: 10.1136/jmg-2022-108754. https://pubmed.ncbi.nlm.nih.gov/36319078/
* **jayarajan-2024-c2**: Jayarajan RO, Chakraborty S, Raghu KG, Purushothaman J, Veleri S. Joubert syndrome causing mutation in C2 domain of CC2D2A affects structural integrity of cilia and cellular signaling molecules. *Exp Brain Res* 2024;242:619-637. PMID: 38231387. DOI: 10.1007/s00221-023-06762-y. https://pubmed.ncbi.nlm.nih.gov/38231387/
* **lambacher-2016-tmem107**: Lambacher NJ, Bruel AL, van Dam TJ, Szymańska K, Slaats GG, Kuhns S, McManus GJ, Kennedy JE, Gaff K, Wu KM, van der Lee R, Burglen L, Doummar D, Rivière JB, Faivre L, Attié-Bitach T, Saunier S, Curd A, Peckham M, Giles RH, Johnson CA, Huynen MA, Thauvin-Robinet C, Blacque OE. TMEM107 recruits ciliopathy proteins to subdomains of the ciliary transition zone and causes Joubert syndrome. *Nat Cell Biol* 2016;18:122-31. PMID: 26595381. DOI: 10.1038/ncb3273. PMCID: PMC5580800. https://pubmed.ncbi.nlm.nih.gov/26595381/
* **lewis-2019-mks6**: Lewis WR, Bales KL, Revell DZ, Croyle MJ, Engle SE, Song CJ, Malarkey EB, Uytingco CR, Shan D, Antonellis PJ, Nagy TR, Kesterson RA, Mrug MM, Martens JR, Berbari NF, Gross AK, Yoder BK. Mks6 mutations reveal tissue- and cell type-specific roles for the cilia transition zone. *FASEB J* 2019;33:1440-1455. PMID: 30133325. DOI: 10.1096/fj.201801149R. PMCID: PMC6355093. https://pubmed.ncbi.nlm.nih.gov/30133325/
* **mougouzerelli-2009-genotype**: Mougou-Zerelli S, Thomas S, Szenker E, Audollent S, Elkhartoufi N, Babarit C, Romano S, Salomon R, Amiel J, Esculpavit C, Gonzales M, Escudier E, Leheup B, Loget P, Odent S, Roume J, Gérard M, Delezoide AL, Khung S, Patrier S, Cordier MP, Bouvier R, Martinovic J, Gubler MC, Boddaert N, Munnich A, Encha-Razavi F, Valente EM, Saad A, Saunier S, Vekemans M, Attié-Bitach T. CC2D2A mutations in Meckel and Joubert syndromes indicate a genotype-phenotype correlation. *Hum Mutat* 2009;30:1574-82. PMID: 19777577. DOI: 10.1002/humu.21116. PMCID: PMC2783384. https://pubmed.ncbi.nlm.nih.gov/19777577/
* **noor-2008-retinitis**: Noor A, Windpassinger C, Patel M, Stachowiak B, Mikhailov A, Azam M, Irfan M, Siddiqui ZK, Naeem F, Paterson AD, Lutfullah M, Vincent JB, Ayub M. CC2D2A, encoding a coiled-coil and C2 domain protein, causes autosomal-recessive mental retardation with retinitis pigmentosa. *Am J Hum Genet* 2008;82:1011-8. PMID: 18387594. DOI: 10.1016/j.ajhg.2008.01.021. PMCID: PMC2427291. https://pubmed.ncbi.nlm.nih.gov/18387594/
* **ojedanaharros-2017-snare**: Ojeda Naharros I, Gesemann M, Mateos JM, Barmettler G, Forbes A, Ziegler U, Neuhauss SCF, Bachmann-Gagescu R. Loss-of-function of the ciliopathy protein Cc2d2a disorganizes the vesicle fusion machinery at the periciliary membrane and indirectly affects Rab8-trafficking in zebrafish photoreceptors. *PLoS Genet* 2017;13:e1007150. PMID: 29281629. DOI: 10.1371/journal.pgen.1007150. PMCID: PMC5760100. https://pubmed.ncbi.nlm.nih.gov/29281629/
* **sang-2011-network**: Sang L, Miller JJ, Corbit KC, Giles RH, Brauer MJ, Otto EA, Baye LM, Wen X, Scales SJ, Kwong M, Huntzicker EG, Sfakianos MK, Sandoval W, Bazan JF, Kulkarni P, Garcia-Gonzalo FR, Seol AD, O'Toole JF, Held S, Reutter HM, Lane WS, Rafiq MA, Noor A, Ansar M, Devi AR, Sheffield VC, Slusarski DC, Vincent JB, Doherty DA, Hildebrandt F, Reiter JF, Jackson PK. Mapping the NPHP-JBTS-MKS protein network reveals ciliopathy disease genes and pathways. *Cell* 2011;145:513-28. PMID: 21565611. DOI: 10.1016/j.cell.2011.04.019. PMCID: PMC3383065. https://pubmed.ncbi.nlm.nih.gov/21565611/
* **shi-2017-superres**: Shi X, Garcia G, Van De Weghe JC, McGorty R, Pazour GJ, Doherty D, Huang B, Reiter JF. Super-resolution microscopy reveals that disruption of ciliary transition-zone architecture causes Joubert syndrome. *Nat Cell Biol* 2017;19:1178-1188. PMID: 28846093. DOI: 10.1038/ncb3599. PMCID: PMC5695680. https://pubmed.ncbi.nlm.nih.gov/28846093/
* **tallila-2008-meckel**: Tallila J, Jakkula E, Peltonen L, Salonen R, Kestilä M. Identification of CC2D2A as a Meckel syndrome gene adds an important piece to the ciliopathy puzzle. *Am J Hum Genet* 2008;82:1361-7. PMID: 18513680. DOI: 10.1016/j.ajhg.2008.05.004. PMCID: PMC2427307. https://pubmed.ncbi.nlm.nih.gov/18513680/
* **truong-2023-tectonic-photoreceptor**: Truong HM, Cruz-Colón KO, Martínez-Márquez JY, Willer JR, Travis AM, Biswas SK, Lo WK, Bolz HJ, Pearring JN. The tectonic complex regulates membrane protein composition in the photoreceptor cilium. *Nat Commun* 2023;14:5671. PMID: 37704658. DOI: 10.1038/s41467-023-41450-z. PMCID: PMC10500017. https://pubmed.ncbi.nlm.nih.gov/37704658/
* **veleri-2014-subdistal**: Veleri S, Manjunath SH, Fariss RN, May-Simera H, Brooks M, Foskett TA, Gao C, Longo TA, Liu P, Nagashima K, Rachel RA, Li T, Dong L, Swaroop A. Ciliopathy-associated gene Cc2d2a promotes assembly of subdistal appendages on the mother centriole during cilia biogenesis. *Nat Commun* 2014;5:4207. PMID: 24947469. DOI: 10.1038/ncomms5207. PMCID: PMC4096663. https://pubmed.ncbi.nlm.nih.gov/24947469/
* **vieillard-2016-drosophila-tz**: Vieillard J, Paschaki M, Duteyrat JL, Augière C, Cortier E, Lapart JA, Thomas J, Durand B. Transition zone assembly and its contribution to axoneme formation in Drosophila male germ cells. *J Cell Biol* 2016;214:875-89. PMID: 27646273. DOI: 10.1083/jcb.201603086. PMCID: PMC5037411. https://pubmed.ncbi.nlm.nih.gov/27646273/
* **warburtonpitt-2012-nphp2**: Warburton-Pitt SR, Jauregui AR, Li C, Wang J, Leroux MR, Barr MM. Ciliogenesis in Caenorhabditis elegans requires genetic interactions between ciliary middle segment localized NPHP-2 (inversin) and transition zone-associated proteins. *J Cell Sci* 2012;125:2592-603. PMID: 22393243. DOI: 10.1242/jcs.095539. PMCID: PMC3403231. https://pubmed.ncbi.nlm.nih.gov/22393243/
* **williams-2011-mks-nphp-modules**: Williams CL, Li C, Kida K, Inglis PN, Mohan S, Semenec L, Bialas NJ, Stupay RM, Chen N, Blacque OE, Yoder BK, Leroux MR. MKS and NPHP modules cooperate to establish basal body/transition zone membrane associations and ciliary gate function during ciliogenesis. *J Cell Biol* 2011;192:1023-41. PMID: 21422230. DOI: 10.1083/jcb.201012116. PMCID: PMC3063147. https://pubmed.ncbi.nlm.nih.gov/21422230/
* **yee-2015-genetic-interactions**: Yee LE, Garcia-Gonzalo FR, Bowie RV, Li C, Kennedy JK, Ashrafi K, Blacque OE, Leroux MR, Reiter JF. Conserved Genetic Interactions between Ciliopathy Complexes Cooperatively Support Ciliogenesis and Ciliary Signaling. *PLoS Genet* 2015;11:e1005627. PMID: 26540106. DOI: 10.1371/journal.pgen.1005627. PMCID: PMC4635004. https://pubmed.ncbi.nlm.nih.gov/26540106/
* **zhang-2012-tgl-peptidase**: Zhang D, Aravind L. Novel transglutaminase-like peptidase and C2 domains elucidate the structure, biogenesis and evolution of the ciliary compartment. *Cell Cycle* 2012;11:3861-75. PMID: 22983010. DOI: 10.4161/cc.22068. PMCID: PMC3495828. https://pubmed.ncbi.nlm.nih.gov/22983010/
* **uniprot-A0A5F5PJ44**: UniProt Consortium. UniProtKB/TrEMBL entry A0A5F5PJ44_HORSE (Coiled-coil and C2 domain containing 2A, Equus caballus), entry version 25 (10-JUN-2026). https://rest.uniprot.org/uniprotkb/A0A5F5PJ44.txt
* **uniprot-Q9P2K1**: UniProt Consortium. UniProtKB/Swiss-Prot entry Q9P2K1 (C2D2A_HUMAN). https://rest.uniprot.org/uniprotkb/Q9P2K1.txt


## Citations

1. bachmanngagescu-2011-zebrafish-rab8-abstract.md
2. bachmanngagescu-2011-zebrafish-rab8-fulltext.txt
3. bachmanngagescu-2011-zebrafish-rab8-summary.md
4. bachmanngagescu-2012-genotype-abstract.md
5. bachmanngagescu-2012-genotype-summary.md
6. bachmanngagescu-2015-ninl-abstract.md
7. bachmanngagescu-2015-ninl-fulltext.txt
8. bachmanngagescu-2015-ninl-summary.md
9. barker-2014-tz-evolution-abstract.md
10. barker-2014-tz-evolution-fulltext.txt
11. barker-2014-tz-evolution-summary.md
12. barrosogil-2021-variants-abstract.md
13. barrosogil-2021-variants-fulltext.txt
14. barrosogil-2021-variants-summary.md
15. chih-2011-mks-b9-complex-abstract.md
16. chih-2011-mks-b9-complex-summary.md
17. diener-2016-tz-proteome-abstract.md
18. diener-2016-tz-proteome-summary.md
19. doherty-2010-coach-abstract.md
20. doherty-2010-coach-fulltext.txt
21. doherty-2010-coach-summary.md
22. garciagonzalo-2011-tectonic-abstract.md
23. garciagonzalo-2011-tectonic-fulltext.txt
24. garciagonzalo-2011-tectonic-summary.md
25. gorden-2008-joubert-cep290-abstract.md
26. gorden-2008-joubert-cep290-summary.md
27. harion-2023-jbts-abstract.md
28. harion-2023-jbts-summary.md
29. jayarajan-2024-c2-abstract.md
30. jayarajan-2024-c2-summary.md
31. lambacher-2016-tmem107-abstract.md
32. lambacher-2016-tmem107-fulltext.txt
33. lambacher-2016-tmem107-summary.md
34. lewis-2019-mks6-abstract.md
35. lewis-2019-mks6-summary.md
36. mougouzerelli-2009-genotype-abstract.md
37. mougouzerelli-2009-genotype-fulltext.txt
38. mougouzerelli-2009-genotype-summary.md
39. noor-2008-retinitis-abstract.md
40. noor-2008-retinitis-summary.md
41. ojedanaharros-2017-snare-abstract.md
42. ojedanaharros-2017-snare-fulltext.txt
43. ojedanaharros-2017-snare-summary.md
44. sang-2011-network-abstract.md
45. sang-2011-network-fulltext.txt
46. sang-2011-network-summary.md
47. shi-2017-superres-abstract.md
48. shi-2017-superres-fulltext.txt
49. shi-2017-superres-summary.md
50. tallila-2008-meckel-abstract.md
51. tallila-2008-meckel-summary.md
52. truong-2023-tectonic-photoreceptor-abstract.md
53. truong-2023-tectonic-photoreceptor-fulltext.txt
54. truong-2023-tectonic-photoreceptor-summary.md
55. uniprot-A0A5F5PJ44-record-summary.md
56. uniprot-A0A5F5PJ44-record.txt
57. uniprot-Q9P2K1-record-summary.md
58. uniprot-Q9P2K1-record.txt
59. veleri-2014-subdistal-abstract.md
60. veleri-2014-subdistal-fulltext.txt
61. veleri-2014-subdistal-summary.md
62. vieillard-2016-drosophila-tz-abstract.md
63. vieillard-2016-drosophila-tz-fulltext.txt
64. vieillard-2016-drosophila-tz-summary.md
65. warburtonpitt-2012-nphp2-abstract.md
66. warburtonpitt-2012-nphp2-summary.md
67. williams-2011-mks-nphp-modules-abstract.md
68. williams-2011-mks-nphp-modules-fulltext.txt
69. williams-2011-mks-nphp-modules-summary.md
70. yee-2015-genetic-interactions-abstract.md
71. yee-2015-genetic-interactions-fulltext.txt
72. yee-2015-genetic-interactions-summary.md
73. zhang-2012-tgl-peptidase-abstract.md
74. zhang-2012-tgl-peptidase-fulltext.txt
75. zhang-2012-tgl-peptidase-summary.md