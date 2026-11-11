---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:28:27.525428'
end_time: '2026-10-25T23:38:25.636668'
duration_seconds: 598.11
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: EPS8L2
  gene_symbol: EPS8L2
  uniprot_accession: A0A9L0KBR4
  protein_description: 'SubName: Full=EPS8 signaling adaptor L2 {ECO:0000313|Ensembl:ENSEASP00005062258.1};'
  gene_info: Name=EPS8L2 {ECO:0000313|Ensembl:ENSEASP00005062258.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the EPS8 family.
  protein_domains: EPS8-like. (IPR039801); EPS8_2nd. (IPR055093); EPS8_PTB. (IPR033928);
    PH-like_dom_sf. (IPR011993); PTB. (IPR013625)
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
citation_count: 59
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0KBR4
- **Protein Description:** SubName: Full=EPS8 signaling adaptor L2 {ECO:0000313|Ensembl:ENSEASP00005062258.1};
- **Gene Information:** Name=EPS8L2 {ECO:0000313|Ensembl:ENSEASP00005062258.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the EPS8 family.
- **Key Domains:** EPS8-like. (IPR039801); EPS8_2nd. (IPR055093); EPS8_PTB. (IPR033928); PH-like_dom_sf. (IPR011993); PTB. (IPR013625)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "EPS8L2" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'EPS8L2' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **EPS8L2** (gene ID: EPS8L2, UniProt: A0A9L0KBR4) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# EPS8L2 (EPS8 signaling adaptor L2) in the donkey, *Equus asinus* (UniProt A0A9L0KBR4)

## Introduction and summary

The donkey protein A0A9L0KBR4 is an unreviewed, computationally annotated TrEMBL entry named "EPS8 signaling adaptor L2" (gene symbol EPS8L2), predicted by Ensembl (ENSEASP00005062258.1) from the chromosome-level donkey reference genome; its UniProt protein-existence level is "inferred from homology", and no experiment has been performed on the donkey protein itself [wang-2020-donkey-genomes-abstract]. The identity check required by this task is unambiguous. The symbol EPS8L2 is used in the literature only for the second "EPS8-like" member of the EPS8 family of actin-regulatory signaling adaptors, which was first described alongside EPS8L1 and EPS8L3 as proteins collinear with, and 27-42% identical to, EPS8 [offenhauser-2004-eps8-family-abstract]. The donkey sequence carries the domains that define this family (an N-terminal PTB domain, a central SH3 domain, a SAM-like region and the C-terminal EPS8 effector region), and my global alignment shows that it is about 84% identical to human EPS8L2 (Q9H6S3) and 82% identical to mouse Eps8l2 (Q99K30) (see `NOTES_sequence_analysis.md`). The donkey protein is therefore the ortholog of the well-studied mammalian EPS8L2, and everything said below about its function is inferred from work on the human, mouse and dog orthologs.

On that basis, EPS8L2 is best described as an actin filament barbed-end regulator (a capping and bundling protein) that also acts as a signaling adaptor. In fibroblasts it joins ABI1 and SOS1 in the complex that couples receptor tyrosine kinase signaling to Rac activation and membrane ruffling [offenhauser-2004-eps8-family-abstract]. Its best-established physiological job is in the inner ear. EPS8L2 sits at the tips of hair-cell stereocilia, mainly in the shorter, mechanotransducing rows, and it is needed to keep the stereocilia staircase intact in mature hair cells [furness-2013-eps8l2-hearing-loss-abstract; krey-2023-stereocilia-length-fulltext]. When it is lost, mice, humans (DFNB106) and dogs develop progressive sensorineural hearing loss [furness-2013-eps8l2-hearing-loss-abstract; dahmani-2015-eps8l2-dfnb-fulltext; kawakami-2022-ridgeback-eps8l2-fulltext; owrang-2026-dfnb106-abstract]. Studies in other cell types place EPS8L2 at the distal tips of filopodia and of the long apical actin bundles of intestinal tuft cells [silverman-2024-tuft-cells-fulltext], and in migrating fibroblasts it helps build dorsal perinuclear actin cables through a direct interaction with the nuclear-envelope phosphatase CTDNEP1 [calero-cuenca-2021-ctdnep1-eps8l2-fulltext].

## Identity, domain architecture and conservation of the donkey protein

The donkey EPS8L2 model is 681 residues long, against 715 for human isoform 1. In my alignment the donkey protein lacks roughly 34 N-terminal residues of the human sequence and then becomes almost identical from the region just before the PTB domain onward. This most likely reflects the choice of start codon in the automated gene model rather than real biology. A short divergent stretch just C-terminal to the SH3 domain probably reflects a difference in exon boundaries in the prediction (see `NOTES_sequence_analysis.md`). UniProt's annotation of the donkey entry (cytoplasm; actin binding; ruffle membrane; positive regulation of ruffle assembly; Rho protein signal transduction) is entirely transferred by automated systems (ARBA and PANTHER/TreeGrafter), and it matches the experimentally supported annotation of human EPS8L2, which UniProt describes as stimulating SOS1 guanine-nucleotide exchange activity, associating with F-actin, and being required for stereocilia maintenance in adult cochlear hair cells.

The residues and segments that genetic and biochemical studies have shown to matter are conserved in the donkey protein. The human DFNB106 frameshift at Ser339 [dahmani-2015-eps8l2-dfnb-fulltext] corresponds to donkey Ser306, which lies in the invariant stretch "HIQNPSAAEL". The four-residue segment deleted in deaf Rhodesian Ridgeback dogs (human VHFL344-347, which AlphaFold places in an α-helix) [kawakami-2022-ridgeback-eps8l2-fulltext] is present in the donkey as AHFL, a conservative valine-to-alanine substitution. The two CTDNEP1-binding regions mapped in mouse Eps8L2 (residues 181-299 and 367-496, between the PTB and SH3 domains) [calero-cuenca-2021-ctdnep1-eps8l2-fulltext] and the C-terminal effector region are also highly conserved. In EPS8 itself, structure-function analysis has shown that this effector region contains two separable actin-binding modules: an amphipathic helix that inserts into the hydrophobic pocket at the filament barbed end to block monomer addition (capping), and a compact four-helix bundle that binds the side of the filament across three actin subunits (bundling). The villin-headpiece-like motif within this region is conserved in murine Eps8L1 and Eps8L2 [hertzog-2010-eps8-capping-bundling-fulltext]. These observations support transferring the EPS8 actin-capping and bundling mechanism to EPS8L2 by homology, although, as discussed below, direct biochemical proof for EPS8L2 is still thin.

## Biochemical activities: an actin barbed-end regulator and Rac signaling adaptor

The founding biochemical study showed that all three EPS8-like proteins bind ABI1 and SOS1, the components of the EPS8–ABI1–SOS1 complex that, together with PI3-kinase, is required for Rac activation downstream of growth factor receptors. Only EPS8L1 and EPS8L2, however, stimulate the Rac-GEF activity of SOS1 and bind actin in vivo. EPS8L1 and EPS8L2, but not EPS8L3, localize to PDGF-induced, F-actin-rich membrane ruffles and restore receptor-tyrosine-kinase-driven ruffling when expressed in Eps8-/- fibroblasts [offenhauser-2004-eps8-family-abstract]. The same study found that mouse Eps8 and Eps8l2 have strikingly overlapping expression patterns, which it proposed as the reason Eps8-null mice have no overt phenotype [offenhauser-2004-eps8-family-abstract]. Later work has confirmed the ABI1 interaction directly. In HeLa cells infected with *Listeria monocytogenes*, EPS8 and EPS8L2 were both enriched in ABI1 complexes, co-immunoprecipitation showed that ABI1 binds EPS8L2 through its proline-rich region, and knocking down EPS8 raised EPS8L2 transcript and protein levels. Depleting both proteins reduced bacterial cell-to-cell spread by about half, whereas depleting EPS8L2 alone had no effect, which fits partial functional redundancy within the family [sun-2026-abi1-complex-switching-fulltext]. Reviews and recent primary work describe EPS8L1 and EPS8L2 as the closest relatives of EPS8 and the most likely to compensate for its loss [mulligan-2026-eps8-protrusions-fulltext].

In the hearing field, EPS8L2 is usually called an F-actin barbed-end capper. Krey and colleagues group EPS8L2 with CAPZB and twinfilin-2 as row-2 tip proteins "with actin-filament capping activity" [krey-2023-stereocilia-length-fulltext], and reviews state that EPS8L2 shares the EPS8 C-terminal domain that binds actin filaments and caps barbed ends [park-2023-actin-hair-bundle-review-fulltext; miyoshi-2022-deafness-variants-dynamics-fulltext]. A careful recent paper nonetheless notes that "there is no direct biochemical evidence confirming EPS8L2 as a barbed-end binder" [silverman-2024-tuft-cells-fulltext]. The evidence for EPS8L2 capping activity therefore rests mainly on homology with EPS8 [hertzog-2010-eps8-capping-bundling-fulltext], on F-actin binding in cells [offenhauser-2004-eps8-family-abstract], and on its consistent localization to the barbed (distal) ends of parallel actin bundles. Its F-actin binding and its participation in the SOS1/ABI1/Rac pathway are, by contrast, directly supported by experiment. Work on another paralog warns against assuming identical activities across the family. In epithelial cells, Eps8 mainly bundles microvillar filaments, whereas the ezrin-binding paralog Eps8L1a limits microvillus length through its capping activity, and ezrin modulates the two activities differently [zwaenepoel-2012-ezrin-eps8-microvilli-abstract]. The same authors note that whether ezrin also binds and regulates Eps8L2 has not been examined [zwaenepoel-2012-ezrin-eps8-microvilli-fulltext]. Which balance of capping and bundling EPS8L2 itself favors therefore remains an empirical question.

EPS8L2 is also a phosphoprotein. Several phosphorylation sites have been mapped in the human protein by proteomics, and phosphorylation was confirmed by phosphatase-sensitive mobility shifts and by mass spectrometry of Eps8L2 co-expressed with CTDNEP1. Whether CTDNEP1 dephosphorylates Eps8L2 was not clearly resolved, and the CTDNEP1 interaction itself does not require phosphatase activity [calero-cuenca-2021-ctdnep1-eps8l2-fulltext].

## Subcellular localization: the distal tips of actin protrusions

In every system studied so far, EPS8L2 concentrates where actin filament barbed ends cluster. In fibroblasts stimulated with PDGF it localizes to F-actin-rich ruffles [offenhauser-2004-eps8-family-abstract]. In migrating wound-edge fibroblasts, exogenous Eps8L2 is cytoplasmic but enriched at the leading edge, along actin filaments, in cell projections and in the perinuclear region, and after LPA stimulation it colocalizes with the dorsal actin cables that form transmembrane actin-associated nuclear (TAN) lines [calero-cuenca-2021-ctdnep1-eps8l2-fulltext]. In HeLa cells EGFP-EPS8L2 accumulates strongly at filopodial tips. In the mouse intestine, endogenous EPS8L2 is markedly enriched in tuft cells relative to neighboring enterocytes and localizes specifically to the distal tips of the long apical actin-bundle protrusions, consistent with filaments that run continuously through the core bundle [silverman-2024-tuft-cells-fulltext].

The localization with the most physiological meaning is in the inner ear. Eps8L2 was identified as a new hair-bundle protein at the tips of stereocilia in both cochlear and vestibular hair cells, with a spatiotemporal expression pattern complementary to that of Eps8 [furness-2013-eps8l2-hearing-loss-abstract]. EPS8 mainly marks the tips of the tallest row, while EPS8L2 is distributed to the tips of the shorter, mechanosensitive rows [miyoshi-2022-deafness-variants-dynamics-fulltext]. In mouse inner hair cells EPS8L2 is present at both row-1 and row-2 tips with a modest bias toward row 2. After about postnatal day 10 it shifts, less completely than CAPZB, from the shafts toward row-2 tips. That redistribution fails in mechanotransduction-deficient Pcdh15 and Tmie mutants, where EPS8L2 is found at nearly equal levels in both rows [krey-2023-stereocilia-length-fulltext]. EPS8L2 is almost completely absent from the hair bundles of Myo15 shaker-2 mutants, which implies that delivery to stereocilia depends on myosin XVa or on the structures it builds [krey-2023-stereocilia-length-fulltext]. This MYO15A dependence parallels its paralog. EPS8 binds myosin XVa and whirlin, fails to reach stereocilia tips without myosin XVa, and acts as the actin-regulatory core of the MYO15A–whirlin elongation complex [manor-2011-eps8-myo15-whirlin-abstract]. EPS8L2 tip targeting is also independent of CIB2: in Cib2-knockout inner hair cells at P12, MYO15A overaccumulates at row-1 tips, yet EPS8 and EPS8L2 staining at the tips persists at near-control levels [giese-2025-cib2-whirlin-fulltext]. Whether EPS8L2 is a direct myosin cargo or diffuses passively to the tips remains unresolved [miyoshi-2022-deafness-variants-dynamics-fulltext]. Overall, EPS8L2 is a cytoplasmic protein that acts at the plasma-membrane-apposed distal ends of actin-based protrusions (stereocilia, microvillus-like tuft-cell protrusions, filopodia and ruffles) and on dorsal perinuclear actin cables.

## Physiological role in hair-bundle maintenance and hearing

The clearest in vivo function of EPS8L2 is keeping the mature auditory hair bundle intact. Eps8 is essential for the initial elongation of stereocilia, whereas Eps8L2 is required for their maintenance in adult hair cells. Eps8l2-null mice show late-onset, progressive hearing loss that tracks a gradual deterioration of hair-bundle morphology, and in mice lacking both proteins the ordered staircase of the cochlear hair bundle decays [furness-2013-eps8l2-hearing-loss-abstract]. Reviews of that work describe the defect as thinning, over-elongation and eventual degeneration of the shorter stereocilia rows [park-2023-actin-hair-bundle-review-fulltext]. This fits a model in which the barbed ends of row-2 actin filaments are capped by a combination of TWF2, EPS8L2 and CAPZB [park-2023-actin-hair-bundle-review-fulltext]. Calcium entry through mechanotransduction channels at row-2 tips is thought to control these capping proteins, and filaments that are not capped become susceptible to resorption [krey-2023-stereocilia-length-fulltext]. EPS8L2 therefore appears to act downstream of mechanotransduction as one of the factors that fixes the length and stability of the transducing rows. This is a structural and homeostatic role rather than a classical signaling one.

Human genetics strongly supports this conclusion. A homozygous frameshift, p.(Ser339Alafs*15), was found in two children of a consanguineous family with childhood-onset progressive autosomal recessive nonsyndromic hearing loss, and it segregated with the disease. This was the first evidence that EPS8L2 is a human deafness gene [dahmani-2015-eps8l2-dfnb-fulltext]. A further frameshift was then reported in a Pakistani family [wang-2017-pakistani-hearing-loss-abstract], and the locus was designated DFNB106. A compound-heterozygous case carrying two frameshifts in trans, including p.(Leu440Alafs*63), widened the allelic series [gan-2026-eps8l2-denovo-fulltext]. Owrang and colleagues more than doubled the number of known patients. They described two new frameshifts, the first nonsense variant, p.(Tyr626Ter), and the first missense change, c.767C>G p.(Thr256Arg), which a minigene assay showed causes exon 9 skipping and a frameshift. This supports loss of function as the disease mechanism. Their patients had moderate to moderately severe, mostly progressive hearing loss, sometimes with U-shaped audiograms, and the authors argued that the progressive course offers a therapeutic window [owrang-2026-dfnb106-abstract; owrang-2026-dfnb106-fulltext]. Outside humans and mice, early-onset adult deafness in Rhodesian Ridgeback dogs is associated with a 12-bp in-frame deletion that removes four residues from an EPS8L2 α-helix. The deletion lies only 13 bp from the human Ser339 frameshift site, which points to this region as functionally critical [kawakami-2022-ridgeback-eps8l2-fulltext]. Independent disease alleles in three mammalian orders make it highly likely that donkey EPS8L2 has the same role in maintaining cochlear hair cells.

## Roles outside the ear: migration, nuclear positioning and cancer

Studies in fibroblasts point to a broader role for EPS8L2 in organizing actin. A yeast two-hybrid screen with the nuclear-envelope phosphatase CTDNEP1 (Dullard) found Eps8L2 as its only actin-binding partner. The interaction is direct, maps to the region between the PTB and SH3 domains, and does not need CTDNEP1 phosphatase activity. Depleting Eps8L2 impaired rearward nuclear movement, centrosome reorientation and both wound-edge and random cell migration. Rescue required full-length Eps8L2: the C-terminal fragment 529-715, which does not bind CTDNEP1, failed to rescue, and the N-terminal fragment 1-496 acted as a dominant negative. Mechanistically, CTDNEP1 and Eps8L2 are required for the formation and normal thickness of the dorsal actin cables that engage TAN lines, the connections between dorsal actin cables and the LINC complex through which actin retrograde flow drives nuclear movement [calero-cuenca-2021-ctdnep1-eps8l2-fulltext]. This places EPS8L2 at the interface between the actin cytoskeleton and the LINC complex.

In cancer, EPS8L2 has been reported to be upregulated in colorectal tumors and associated with poor prognosis. In that study EPS8L2 overexpression promoted proliferation, migration and organoid growth, and Eps8l2 knockout reduced tumorigenesis in an AOM/DSS mouse model. The proposed mechanism is that EPS8L2 strengthens the S6K1–YBX1 interaction, YBX1 phosphorylation and nuclear translocation, which drives G3BP2 transcription and MAPK pathway activation [duan-2025-eps8l2-colorectal-abstract]. This axis comes from a single study, has no obvious link to the protein's actin-regulatory domains, and should be treated as a context-specific observation rather than a core function. EPS8L2 also contributes, redundantly with EPS8, to the ABI1-dependent actin protrusions that *Listeria* exploits for cell-to-cell spread [sun-2026-abi1-complex-switching-fulltext].

## Synthesis: functional model for donkey EPS8L2

Combining the orthology evidence with experimental work in other mammals gives a consistent model for donkey EPS8L2. It is a cytoplasmic, multidomain adaptor whose PTB, SH3 and central regions mediate protein interactions (ABI1, SOS1 and CTDNEP1), and whose conserved C-terminal effector region binds F-actin and most likely caps and bundles filament barbed ends, by analogy with EPS8 [offenhauser-2004-eps8-family-abstract; hertzog-2010-eps8-capping-bundling-fulltext; calero-cuenca-2021-ctdnep1-eps8l2-fulltext]. In signaling terms it links growth-factor receptor activation to Rac-dependent actin remodeling through SOS1 Rac-GEF stimulation [offenhauser-2004-eps8-family-abstract]. In structural terms it sits at the distal tips of parallel actin bundles. In the inner ear it acts with CAPZB and TWF2 at the tips of the mechanotransducing shorter stereocilia rows, in a mechanotransduction- and MYO15A-dependent manner, to maintain stereocilia length and the hair-bundle staircase in adulthood [krey-2023-stereocilia-length-fulltext; park-2023-actin-hair-bundle-review-fulltext]. Loss of this function causes progressive hearing loss in mouse, human and dog [furness-2013-eps8l2-hearing-loss-abstract; dahmani-2015-eps8l2-dfnb-fulltext; kawakami-2022-ridgeback-eps8l2-fulltext]. Suitable Gene Ontology terms by orthology would include actin filament binding, barbed-end actin filament capping (homology-based), positive regulation of ruffle assembly, stereocilium tip localization, and stereocilium maintenance / auditory receptor cell stereocilium organization. It is not an enzyme and has no known catalytic activity. Network analyses agree with this picture at a bioinformatic level. A cross-species systematic review of hearing genes found balanced cochlear and vestibular expression of EPS8L2 and placed it as a hub in a predicted stereocilia protein-interaction module, with high-confidence STRING associations to MYO3A and TRIOBP. These are predicted functional links, not demonstrated physical interactions [ayoub-2025-hearing-genes-review-fulltext].

## Open Questions

The largest gap is biochemical. Whether purified EPS8L2 caps barbed ends, bundles filaments, or both, and how its affinities compare with EPS8, has not been shown directly; one group explicitly notes the absence of such evidence [silverman-2024-tuft-cells-fulltext]. Reconstitution assays like those used to separate the EPS8 capping and bundling modules [hertzog-2010-eps8-capping-bundling-fulltext], applied to EPS8L2 and to disease alleles such as the dog VHFL deletion and human Thr256Arg, would test whether the disease mechanism is loss of capping, loss of bundling, or protein instability. How EPS8L2 reaches stereocilia tips is also unclear: it may be a MYO15A cargo, ride with another myosin, or diffuse, and the molecular link that lets mechanotransduction or Ca2+ entry redistribute it toward row 2 is unknown [krey-2023-stereocilia-length-fulltext; miyoshi-2022-deafness-variants-dynamics-fulltext]. The relationship between its Rac/SOS1 signaling function and its structural role at stereocilia tips has not been tested in hair cells. Whether ezrin or another ERM protein regulates EPS8L2, as it regulates EPS8 and Eps8L1a in microvilli [zwaenepoel-2012-ezrin-eps8-microvilli-fulltext], and whether the predicted EPS8L2–MYO3A association [ayoub-2025-hearing-genes-review-fulltext] reflects a real cargo relationship, could both be tested directly. The CTDNEP1 interaction raises the question of whether EPS8L2 phosphorylation regulates its actin activity and whether this pathway works in hair cells or tuft cells [calero-cuenca-2021-ctdnep1-eps8l2-fulltext]. The colorectal-cancer YBX1–G3BP2 axis needs independent replication and a mechanistic connection to the known domains [duan-2025-eps8l2-colorectal-abstract]. For the donkey protein specifically, the N-terminus of the current Ensembl model should be checked against RNA-seq or long-read transcript data, because the predicted protein lacks about 34 residues present in the human and mouse orthologs and has a divergent segment after the SH3 domain. The tissue expression pattern in equids (cochlea, intestine) and any association between EPS8L2 variants and age-related hearing decline in donkeys or horses are also unexplored. Given the human therapeutic-window argument [owrang-2026-dfnb106-abstract], large-animal orthologs could become relevant to comparative studies of gene therapy.

## References

- **[offenhauser-2004-eps8-family]** Offenhäuser N, Borgonovo A, Disanza A, Romano P, Ponzanelli I, Iannolo G, Di Fiore PP, Scita G. The eps8 family of proteins links growth factor stimulation to actin reorganization generating functional redundancy in the Ras/Rac pathway. *Mol Biol Cell* 2004. PMID: 14565974; PMCID: PMC307530; DOI: 10.1091/mbc.e03-06-0427.
- **[hertzog-2010-eps8-capping-bundling]** Hertzog M, Milanesi F, Hazelwood L, Disanza A, Liu H, Perlade E, et al. Molecular basis for the dual function of Eps8 on actin dynamics: bundling and capping. *PLoS Biol* 2010. PMID: 20532239; PMCID: PMC2879411; DOI: 10.1371/journal.pbio.1000387.
- **[manor-2011-eps8-myo15-whirlin]** Manor U, Disanza A, Grati M, et al. Regulation of stereocilia length by myosin XVa and whirlin depends on the actin-regulatory protein Eps8. *Curr Biol* 2011. PMID: 21236676; PMCID: PMC3040242; DOI: 10.1016/j.cub.2010.12.046.
- **[zwaenepoel-2012-ezrin-eps8-microvilli]** Zwaenepoel I, Naba A, Da Cunha MM, et al. Ezrin regulates microvillus morphogenesis by promoting distinct activities of Eps8 proteins. *Mol Biol Cell* 2012. PMID: 22262457; PMCID: PMC3302735; DOI: 10.1091/mbc.e11-07-0588.
- **[furness-2013-eps8l2-hearing-loss]** Furness DN, Johnson SL, Manor U, Rüttiger L, Tocchetti A, Offenhauser N, et al., Marcotti W. Progressive hearing loss and gradual deterioration of sensory hair bundles in the ears of mice lacking the actin-binding protein Eps8L2. *Proc Natl Acad Sci USA* 2013. PMID: 23918390; PMCID: PMC3752214; DOI: 10.1073/pnas.1304644110.
- **[dahmani-2015-eps8l2-dfnb]** Dahmani M, Ammar-Khodja F, Bonnet C, Lefèvre GM, Hardelin JP, et al. EPS8L2 is a new causal gene for childhood onset autosomal recessive progressive hearing loss. *Orphanet J Rare Dis* 2015. PMID: 26282398; PMCID: PMC4539681; DOI: 10.1186/s13023-015-0316-8.
- **[wang-2017-pakistani-hearing-loss]** Wang R, Han S, Khan A, Zhang X. Molecular Analysis of Twelve Pakistani Families with Nonsyndromic or Syndromic Hearing Loss. *Genet Test Mol Biomarkers* 2017. PMID: 28281779; PMCID: PMC5444417; DOI: 10.1089/gtmb.2016.0328.
- **[wang-2020-donkey-genomes]** Wang C, Li H, Guo Y, Huang J, Sun Y, et al., Zhong J. Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun* 2020. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7.
- **[calero-cuenca-2021-ctdnep1-eps8l2]** Calero-Cuenca FJ, Osorio DS, Carvalho-Marques S, Sridhara SC, et al. Ctdnep1 and Eps8L2 regulate dorsal actin cables for nuclear positioning during cell migration. *Curr Biol* 2021. PMID: 33567288; PMCID: PMC8043254; DOI: 10.1016/j.cub.2021.01.007.
- **[kawakami-2022-ridgeback-eps8l2]** Kawakami T, Raghavan V, Ruhe AL, Jensen MK, Milano A, Nelson TC, et al. Early onset adult deafness in the Rhodesian Ridgeback dog is associated with an in-frame deletion in the EPS8L2 gene. *PLoS One* 2022. PMID: 35385474; PMCID: PMC8985935; DOI: 10.1371/journal.pone.0264365.
- **[miyoshi-2022-deafness-variants-dynamics]** Miyoshi T, Belyantseva IA, Kitajiri SI, Miyajima H, Nishio S, et al. Human deafness-associated variants alter the dynamics of key molecules in hair cell stereocilia F-actin cores. *Hum Genet* 2022. PMID: 34232383; PMCID: PMC11351816; DOI: 10.1007/s00439-021-02304-0.
- **[krey-2023-stereocilia-length]** Krey JF, Chatterjee P, Halford J, Cunningham CL, Perrin BJ, et al. Control of stereocilia length during development of hair bundles. *PLoS Biol* 2023. PMID: 37011103; PMCID: PMC10101650; DOI: 10.1371/journal.pbio.3001964.
- **[park-2023-actin-hair-bundle-review]** Park J, Bird JE. The actin cytoskeleton in hair bundle development and hearing loss. *Hear Res* 2023. PMID: 37300948; PMCID: PMC10408727; DOI: 10.1016/j.heares.2023.108817.
- **[silverman-2024-tuft-cells]** Silverman JB, Krystofiak EE, Caplan LR, Lau KS, Tyska MJ. Organization of a cytoskeletal superstructure in the apical domain of intestinal tuft cells. *J Cell Biol* 2024. PMID: 39352498; PMCID: PMC11457492; DOI: 10.1083/jcb.202404070.
- **[duan-2025-eps8l2-colorectal]** Duan Y, Li P, Yang Y, Wu G, Xing H, Chen H, Zhao L, Liu L, et al. EPS8L2 drives colorectal cancer cell proliferation and migration via YBX1-dependent activation of G3BP2 transcription. *Cell Death Dis* 2025. PMID: 40783393; PMCID: PMC12335500; DOI: 10.1038/s41419-025-07929-x.
- **[giese-2025-cib2-whirlin]** Giese APJ, Parker A, Rehman S, Brown SDM, et al. CIB2 function is distinct from that of whirlin in the organization of sterocilia architecture. *Dis Model Mech* 2025. PMID: 40083274; PMCID: PMC11992350; DOI: 10.1242/dmm.052043.
- **[ayoub-2025-hearing-genes-review]** Ayoub C, Paladugu S, Nikitenko N, et al. Genes linked to hearing and vestibular phenotypes in humans and mice: an interspecies systematic review. *Hum Genomics* 2025. PMID: 41430327; PMCID: PMC12751684; DOI: 10.1186/s40246-025-00891-x.
- **[owrang-2026-dfnb106]** Owrang D, Rad A, Alerasool M, Kolb SM, Lin SJ, Doll J, et al. Expansion of Molecular and Clinical Aspects of EPS8L2 (DFNB106)-Associated Hearing Loss Emphasizes a Potential Therapeutic Window. *Mol Neurobiol* 2026. PMID: 41514136; PMCID: PMC12789209; DOI: 10.1007/s12035-025-05615-9.
- **[gan-2026-eps8l2-denovo]** Gan H, Lu Y, Qu S, Lu L, Xu H, Fan M, Tang J, Mo J, Chen R, et al. Identification and phased de novo mutation of the EPS8L2 gene in a patient with progressive hearing loss: A case report. *Medicine (Baltimore)* 2026. PMID: 41578500; PMCID: PMC12851731; DOI: 10.1097/md.0000000000046930.
- **[mulligan-2026-eps8-protrusions]** Mulligan AG, Lehmann ZJ, Robinson KL, Tyska MJ. EPS8 dampens the growth dynamics and prolongs the lifetime of actin-based protrusions. *J Biol Chem* 2026. PMID: 42749257; PMCID: PMC13681995; DOI: 10.1016/j.jbc.2026.113563.
- **[sun-2026-abi1-complex-switching]** Sun H, Wizzard A, Brumell JH, Higgins DE. A pore-forming toxin initiates ABI1 complex switching to promote bacterial cell-to-cell spread. *Nat Commun* 2026. PMID: 41974702; PMCID: PMC13247217; DOI: 10.1038/s41467-026-71510-z.
- UniProtKB entries consulted: A0A9L0KBR4 (donkey EPS8L2, https://rest.uniprot.org/uniprotkb/A0A9L0KBR4.txt), Q9H6S3 (human EPS8L2), Q99K30 (mouse Eps8l2).


## Citations

1. ayoub-2025-hearing-genes-review-abstract.md
2. ayoub-2025-hearing-genes-review-fulltext.txt
3. ayoub-2025-hearing-genes-review-summary.md
4. calero-cuenca-2021-ctdnep1-eps8l2-abstract.md
5. calero-cuenca-2021-ctdnep1-eps8l2-fulltext.txt
6. calero-cuenca-2021-ctdnep1-eps8l2-summary.md
7. dahmani-2015-eps8l2-dfnb-abstract.md
8. dahmani-2015-eps8l2-dfnb-fulltext.txt
9. dahmani-2015-eps8l2-dfnb-summary.md
10. duan-2025-eps8l2-colorectal-abstract.md
11. duan-2025-eps8l2-colorectal-fulltext.txt
12. duan-2025-eps8l2-colorectal-summary.md
13. furness-2013-eps8l2-hearing-loss-abstract.md
14. furness-2013-eps8l2-hearing-loss-summary.md
15. gan-2026-eps8l2-denovo-abstract.md
16. gan-2026-eps8l2-denovo-fulltext.txt
17. gan-2026-eps8l2-denovo-summary.md
18. giese-2025-cib2-whirlin-abstract.md
19. giese-2025-cib2-whirlin-fulltext.txt
20. giese-2025-cib2-whirlin-summary.md
21. hertzog-2010-eps8-capping-bundling-abstract.md
22. hertzog-2010-eps8-capping-bundling-fulltext.txt
23. hertzog-2010-eps8-capping-bundling-summary.md
24. kawakami-2022-ridgeback-eps8l2-abstract.md
25. kawakami-2022-ridgeback-eps8l2-fulltext.txt
26. kawakami-2022-ridgeback-eps8l2-summary.md
27. krey-2023-stereocilia-length-abstract.md
28. krey-2023-stereocilia-length-fulltext.txt
29. krey-2023-stereocilia-length-summary.md
30. manor-2011-eps8-myo15-whirlin-abstract.md
31. manor-2011-eps8-myo15-whirlin-fulltext.txt
32. manor-2011-eps8-myo15-whirlin-summary.md
33. miyoshi-2022-deafness-variants-dynamics-abstract.md
34. miyoshi-2022-deafness-variants-dynamics-fulltext.txt
35. miyoshi-2022-deafness-variants-dynamics-summary.md
36. mulligan-2026-eps8-protrusions-abstract.md
37. mulligan-2026-eps8-protrusions-fulltext.txt
38. mulligan-2026-eps8-protrusions-summary.md
39. offenhauser-2004-eps8-family-abstract.md
40. offenhauser-2004-eps8-family-summary.md
41. owrang-2026-dfnb106-abstract.md
42. owrang-2026-dfnb106-fulltext.txt
43. owrang-2026-dfnb106-summary.md
44. park-2023-actin-hair-bundle-review-abstract.md
45. park-2023-actin-hair-bundle-review-fulltext.txt
46. park-2023-actin-hair-bundle-review-summary.md
47. silverman-2024-tuft-cells-abstract.md
48. silverman-2024-tuft-cells-fulltext.txt
49. silverman-2024-tuft-cells-summary.md
50. sun-2026-abi1-complex-switching-abstract.md
51. sun-2026-abi1-complex-switching-fulltext.txt
52. sun-2026-abi1-complex-switching-summary.md
53. wang-2017-pakistani-hearing-loss-abstract.md
54. wang-2017-pakistani-hearing-loss-summary.md
55. wang-2020-donkey-genomes-abstract.md
56. wang-2020-donkey-genomes-summary.md
57. zwaenepoel-2012-ezrin-eps8-microvilli-abstract.md
58. zwaenepoel-2012-ezrin-eps8-microvilli-fulltext.txt
59. zwaenepoel-2012-ezrin-eps8-microvilli-summary.md