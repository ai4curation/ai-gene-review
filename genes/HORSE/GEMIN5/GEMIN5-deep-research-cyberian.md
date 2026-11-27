---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-26T02:13:52.569906'
end_time: '2026-10-26T02:24:01.252495'
duration_seconds: 608.68
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: HORSE
  gene_id: GEMIN5
  gene_symbol: GEMIN5
  uniprot_accession: A0A9L0R5P7
  protein_description: 'RecName: Full=Gem-associated protein 5 {ECO:0000256|ARBA:ARBA00067669};'
  gene_info: Name=GEMIN5 {ECO:0000313|Ensembl:ENSECAP00000056962.1};
  organism_full: Equus caballus (Horse).
  protein_family: Belongs to the WD repeat gemin-5 family.
  protein_domains: Beta-prop_GEMI5_1st. (IPR056432); Beta-prop_GEMI5_2nd. (IPR056424);
    GEMI5_RBS. (IPR056420); Gemin-5. (IPR052640); TPR_GEMI5. (IPR056421)
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
citation_count: 117
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0R5P7
- **Protein Description:** RecName: Full=Gem-associated protein 5 {ECO:0000256|ARBA:ARBA00067669};
- **Gene Information:** Name=GEMIN5 {ECO:0000313|Ensembl:ENSECAP00000056962.1};
- **Organism (full):** Equus caballus (Horse).
- **Protein Family:** Belongs to the WD repeat gemin-5 family.
- **Key Domains:** Beta-prop_GEMI5_1st. (IPR056432); Beta-prop_GEMI5_2nd. (IPR056424); GEMI5_RBS. (IPR056420); Gemin-5. (IPR052640); TPR_GEMI5. (IPR056421)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GEMIN5" matches the protein description above**
2. **Verify the organism is correct:** Equus caballus (Horse).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GEMIN5' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GEMIN5** (gene ID: GEMIN5, UniProt: A0A9L0R5P7) in HORSE.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GEMIN5 (Gem-associated protein 5) in the Horse, *Equus caballus* (UniProt A0A9L0R5P7)

## 1. Introduction and Summary

GEMIN5 is a large (~170 kDa) multidomain RNA-binding protein that was discovered as a WD-repeat subunit of the survival of motor neurons (SMN) complex, the macromolecular machine that assembles the heptameric Sm protein ring onto small nuclear RNAs (snRNAs) to generate the core of spliceosomal small nuclear ribonucleoproteins (snRNPs) [gubitz-2002-gemin5-wd-repeat-abstract; pellizzoni-2002-smn-specificity-abstract]. Its primary and best-established molecular function is that of the snRNA-recognition subunit of the SMN complex: it binds directly and specifically to the "snRNP code" of snRNA precursors (the Sm site, AU5-6G, plus an adjacent 3' stem-loop) and delivers these pre-snRNAs to the SMN complex for Sm core assembly, thereby allowing the assembly machinery to distinguish snRNAs from the vast excess of other cellular RNAs [battle-2006-gemin5-identifies-snrnas-abstract; yong-2010-gemin5-delivers-snrna-abstract; jin-2016-gemin5-double-wd40-fulltext]. GEMIN5 is not an enzyme; it is an RNA-binding adaptor and scaffold within a chaperone/catalyst system in which the SMN-Gemin2 unit carries the Sm proteins and ATP-dependent steps drive snRNA transfer [chari-2008-assembly-chaperoning-abstract; battle-2007-smn-independent-subunits-abstract]. Beyond snRNP biogenesis, a body of work, largely from one laboratory, has shown that GEMIN5 is a predominantly cytoplasmic protein that binds the 7-methylguanosine (m7G) cap, binds the 60S ribosomal subunit, and regulates translation both globally (as a repressor) and selectively (as an activator of specific mRNA classes such as 5'TOP ribosomal protein mRNAs, histone mRNAs, SMN mRNA, and its own mRNA) [bradrick-2009-gemin5-cap-binding-fulltext; francisco-velilla-2016-gemin5-ribosome-fulltext; embarc-buh-2022-gemin5-polysomes-fulltext; workman-2015-gemin5-smn-mrna-abstract].

No experimental study has been performed on horse GEMIN5. The horse protein is an unreviewed TrEMBL entry (1433 residues) predicted from the Thoroughbred genome assembly by Ensembl, and its subcellular location annotations are purely electronic (ARBA rules) [uniprot-A0A9L0R5P7-entry; wade-2009-horse-genome-abstract]. All functional statements in this report are therefore inferred by orthology from studies of human GEMIN5 (Q8TEQ6, 1508 residues) and, to a lesser extent, from fly, zebrafish and mouse models. This inference is strong: the horse protein carries the same five InterPro domain signatures (two GEMIN5 beta-propellers, a TPR-like domain, an RNA-binding site region, and the Gemin-5 family signature), and a pairwise global alignment performed for this report shows 89.2% identity to human GEMIN5 with conservation of every residue that has been shown structurally and biochemically to contact snRNA, the m7G cap, or the ribosome [uniprot-A0A9L0R5P7-summary; uniprot-Q8TEQ6-human-entry].

## 2. Identity Verification and Domain Architecture of the Horse Protein

The gene symbol GEMIN5 is unambiguous: the UniProt record names the protein "Gem-associated protein 5", assigns it to the WD repeat gemin-5 family, and maps it to Ensembl gene ENSECAG00000020479 on horse chromosome 14 [uniprot-A0A9L0R5P7-entry]. To test orthology directly, the horse and human sequences were aligned (BioPython global alignment, BLOSUM62). Of 1431 aligned positions, 1277 were identical (89.2%). The N-terminal 714 residues are essentially co-linear with the human protein, and the residues identified in crystal structures as mediating base stacking with the Sm site (Trp14, Tyr15, Phe381, Trp422), hydrogen bonding to Sm-site bases (Arg335, Met357, Arg359) and the alternative/cap-related binding mode and ribosome binding (Tyr474) are all present at identical positions in the horse sequence [jin-2016-gemin5-double-wd40-fulltext; xu-2016-gemin5-pre-snrna-selection-fulltext; francisco-velilla-2016-gemin5-ribosome-abstract]. The only notable difference at a characterized position is Lys641, a residue mutated in cap-binding studies, which is a conservative arginine in the horse model [xu-2016-gemin5-pre-snrna-selection-fulltext]. The most significant structural difference is that the horse gene model lacks a 76-residue segment corresponding to human residues ~722-797, a lysine-rich, low-complexity linker situated between the end of the second WD40 propeller (~residue 739) and the start of the TPR-like dimerization domain (~residue 807-845) [moreno-morcillo-2020-gemin5-dimerization-fulltext; guo-2022-gemin5-decamer-fulltext]. NCBI's independent RefSeq annotation of the horse genome resolves much of this uncertainty: all four predicted horse GEMIN5 isoforms (XP_005599323, 1509 aa; XP_023473111, 1508 aa; XP_023473114, 1471 aa; XP_023473115, 1470 aa) contain this lysine-rich linker, share the TrEMBL N-terminal sequence verbatim, and are ~89% identical to human GEMIN5 over their full length, with isoforms X3/X4 differing from X1/X2 by a shorter alternative segment just downstream of the linker [ncbi-refseq-horse-gemin5-isoforms-summary]. The A0A9L0R5P7 sequence is therefore best regarded as an Ensembl gene model (or a minor isoform) that skips the linker exon(s), while the canonical horse protein is predicted to be a ~1508-residue polypeptide colinear with human GEMIN5. Because it falls outside every structurally characterized domain, it is unlikely to affect the core functions described below, but it could influence any nuclear-targeting or interaction role played by that basic stretch.

The domain organization of GEMIN5, established for the human protein, consists of three structured modules joined by flexible regions. The N-terminal half (~residues 1-739) folds into two juxtaposed seven-bladed WD40 beta-propellers (the "13-14 WD repeats" originally predicted) that are rigidly held together to form a contiguous RNA-binding surface [gubitz-2002-gemin5-wd-repeat-abstract; jin-2016-gemin5-double-wd40-abstract]. The middle region (~807-1097) forms an extended tetratricopeptide-repeat (TPR)-like domain that self-associates into a canoe-shaped homodimer [moreno-morcillo-2020-gemin5-dimerization-abstract]. The C-terminal region contains a helical "pentamer region" that drives assembly of a homodecamer (a dimer of pentamers) together with the TPR dimer, and an intrinsically disordered, non-canonical RNA-binding site (RBS1, ~1297-1412; with a weaker RBS2, ~1383-1508) [guo-2022-gemin5-decamer-abstract; fernandez-chamorro-2014-noncanonical-rbs-abstract; embarc-buh-2021-rbs1-unstructured-abstract]. These correspond to the InterPro entries Beta-prop_GEMI5_1st, Beta-prop_GEMI5_2nd, TPR_GEMI5 and GEMI5_RBS listed for the horse entry [uniprot-A0A9L0R5P7-entry].

## 3. Primary Function: snRNA Recognition and Delivery in snRNP Core Assembly

The canonical role of GEMIN5 lies in the cytoplasmic phase of spliceosomal snRNP biogenesis. Newly transcribed Sm-class snRNAs (U1, U2, U4, U5, U11, U12, U4atac) are exported to the cytoplasm, where the SMN complex assembles a ring of seven Sm proteins on their Sm site. The SMN complex is necessary and sufficient for ATP-dependent Sm core assembly in vitro and, crucially, ensures that Sm cores assemble only on correct RNA targets rather than promiscuously on other RNAs [pellizzoni-2002-smn-specificity-abstract]. Upstream, the PRMT5-associated chaperone pICln kinetically traps Sm proteins in a ring-like intermediate; the SMN complex then accepts these Sm units, displaces pICln and catalyzes ring closure on snRNA [chari-2008-assembly-chaperoning-abstract; neuenkirchen-2015-reconstitution-snrnp-abstract].

Within this machine, GEMIN5 is the subunit that supplies RNA specificity. Battle and colleagues showed that Gemin5 binds directly and specifically to snRNA features including the Sm site, and that reducing Gemin5 decreases the SMN complex's capacity to bind snRNAs and assemble Sm cores, establishing it as the factor that allows the complex to distinguish snRNAs from other cellular RNAs [battle-2006-gemin5-identifies-snrnas-abstract]. Lau and colleagues then demonstrated that the WD-repeat domain alone is necessary and sufficient for sequence-specific, high-affinity snRNA binding, revealing the WD-repeat fold as a bona fide RNA-binding domain [lau-2009-gemin5-snrna-wd-repeat-abstract]. Gemin5 can bind snRNA in sub-complexes lacking SMN (a Gemin3-Gemin4-Gemin5 module and free Gemin5) without exogenous ATP, whereas ATP hydrolysis is required to displace the snRNA from these Gemin5-containing subunits into assembled snRNPs, indicating a modular, stepwise mechanism [battle-2007-smn-independent-subunits-abstract]. In cells, inhibiting the SMN complex trapped a pre-snRNA-Gemin5 intermediate; sequencing its RNAs revealed precursors of all snRNAs and mapped Gemin5-binding sites, leading to the model that Gemin5 captures pre-snRNAs (bearing 3' extensions) and delivers them as substrates for Sm core assembly and processing [yong-2010-gemin5-delivers-snrna-abstract]. Interaction mapping places Gemin5 at the periphery of the complex, attached through Gemin2/Gemin3-Gemin4 and SMN, yet contributing an essential activity [otter-2007-smn-interaction-map-abstract; gubitz-2002-gemin5-wd-repeat-abstract]. More recent domain-dissection work shows that association with SMN, Gemin2 and Gemin4 depends primarily on the TPR dimerization module rather than the WD40 domain [francisco-velilla-2024-oligomerization-abstract], and that the SMN Tudor domain binds the GEMIN5 C-terminus [fortuna-2023-smn-regulates-gemin5-abstract].

The structural basis for snRNA selection was resolved by three independent crystallographic studies in 2016 [wahl-2016-right-pick-abstract]. Jin and colleagues showed that the tandem WD40 domains present a contiguous apical binding surface in which RNA-contacting residues lie on inter-strand loops; four aromatic residues (Trp14, Tyr15, Phe381, Trp422) stack with Sm-site bases and a pair of arginines (Arg335, Arg359) hydrogen-bond to them, and an adenine immediately 5' to the Sm site is required for efficient binding [jin-2016-gemin5-double-wd40-abstract; jin-2016-gemin5-double-wd40-fulltext]. Xu and colleagues used isothermal titration calorimetry and crystallography to show that the WD40 domain is both necessary and sufficient to bind the Sm site and that the Sm site and the m7G cap are recognized at two distinct sites [xu-2016-gemin5-pre-snrna-selection-abstract]. Tang and colleagues similarly localized Sm-RNA recognition to the first beta-propeller and m7G cap recognition to the second, and noted that a trimethylguanosine cap would clash sterically with the cap pocket, implying that Gemin5 selectively engages the immature (m7G-capped) pre-snRNA before cap hypermethylation [tang-2016-gemin5-pre-snrna-fulltext]. Since all of these contact residues are conserved in the horse protein, the same recognition mode is expected.

Two qualifications are important. First, not every Sm-class RNA uses Gemin5: the U1-specific protein U1-70K can bridge pre-U1 to SMN-Gemin2-Sm in a Gemin5-independent pathway that contributes to U1 overabundance [so-2016-u1-snrnp-pathway-abstract], and the non-canonical Sm site of U7 snRNA (which forms an Lsm10/Lsm11-containing ring for histone pre-mRNA processing) is not recognized by Gemin5, with PTBP1, IGF2BP3 and hnRNP A1 proposed as substitutes [yang-2025-u7-snrna-gemin5-abstract]. Second, an early RNAi study found no effect of Gemin5 knockdown on Sm core assembly, in contrast to later work, a discrepancy probably reflecting knockdown efficiency or assay design [shpargel-2005-gemin-proteins-required-abstract]. The weight of evidence, including disease-variant studies showing that GEMIN5 loss impairs snRNP assembly in patient neurons, supports an essential role in snRNP biogenesis in vivo [kour-2021-gemin5-neurodevelopmental-abstract].

## 4. m7G Cap Binding and snRNA Quality Control

An unbiased cap-affinity proteomic screen identified Gemin5 as a direct m7G cap-binding protein, purifying independently of eIF4E and crosslinking to radiolabelled cap; the WD-repeat region was required [bradrick-2009-gemin5-cap-binding-abstract]. Crystal structures subsequently located the cap pocket on the second propeller, with Tyr474 and Lys641 implicated, and showed recognition analogous to that of CBC20, eIF4E, PARN and DcpS [tang-2016-gemin5-pre-snrna-fulltext; xu-2016-gemin5-pre-snrna-selection-fulltext]. Notably, Jin and colleagues interpreted Tyr474-dependent binding as an alternative, minor RNA-binding mode [jin-2016-gemin5-double-wd40-fulltext], so the precise physiological role of cap binding remains debated. Functionally, cap recognition appears to underpin a quality-control role: Gemin5 binds truncated U1 pre-snRNAs that lack an Sm site but retain the cap and shunts them into P bodies for degradation [xu-2016-gemin5-pre-snrna-selection-abstract], and in SMN-deficient cells Gemin5 is required for the accumulation of unassembled U1 snRNA/U1A in P-body-associated granules, its knockdown restoring U1 levels [jiang-2018-gemin5-u1-disposal-abstract].

## 5. Translation Regulation, Ribosome Binding and Selective mRNA Control

A second major line of work positions GEMIN5 as a regulator of mRNA translation that operates independently of the SMN complex. Gemin5 was identified bound to the foot-and-mouth disease virus and hepatitis C virus internal ribosome entry sites (IRESs), and depletion or in vitro supplementation showed that it down-regulates both cap-dependent and IRES-driven initiation; it was found in an IRES-ribonucleoprotein complex and in a separate complex containing eIF4E [pacheco-2009-gemin5-translation-abstract]. IRES binding and translational repression map to the C-terminal region, which protects a hairpin in the IRES and competes with PTB [pineiro-2013-gemin5-ires-abstract]. The C-terminal region carries two non-canonical RNA-binding sites, RBS1 and RBS2; RBS2 is the minimal repressor of IRES-driven translation, whereas RBS1 binds RNA more tightly [fernandez-chamorro-2014-noncanonical-rbs-abstract]. RBS1 is intrinsically disordered even when bound to RNA and recognizes RNA through a conserved arginine/serine/tryptophan/histidine-rich motif using pi-pi and cation-pi contacts, including a coevolving PXSS motif [embarc-buh-2021-rbs1-unstructured-abstract; francisco-velilla-2020-pxss-rbs1-abstract]. Its most abundant cellular target is GEMIN5's own mRNA, where RBS1 binding to a stable stem-loop in the coding region stimulates translation, forming a feedback loop that counterbalances the protein's global repressive effect [francisco-velilla-2018-rbs-feedback-abstract]. During FMDV infection the viral leader protease cleaves Gemin5 to yield a C-terminal p85 fragment, illustrating that the protein is a host target for viral reprogramming of translation [pineiro-2012-gemin5-l-protease-abstract].

Gemin5 also contacts the translation machinery directly. It co-sediments with ribosomes, binds the 60S subunit through its N-terminal WD40 domain and interacts directly with ribosomal proteins L3 and L4; ribosome binding is lost with the F381A and Y474A substitutions but not with W14A or Y15A, separating ribosome binding from Sm-site recognition. Depleting Gemin5 increases, and overexpressing it decreases, global protein synthesis [francisco-velilla-2016-gemin5-ribosome-abstract]. Association with native ribosomes and translational repression require both the WD40 domain and the TPR dimerization module [francisco-velilla-2024-oligomerization-abstract], and phosphorylation of residues in the dimerization domain (T897, S847, S/T852-854) modulates ribosome binding, protein stability and the translation-related interactome [francisco-velilla-2022-t897-phosphorylation-abstract; abellan-2025-phosphoresidues-ribosome-abstract].

Against this background of global repression, GEMIN5 enhances translation of selected mRNAs. It binds elements in the SMN mRNA 3'UTR that resemble the snRNP code and promotes its association with heavy polysomes, creating an autoregulatory loop between SMN and GEMIN5 [workman-2015-gemin5-smn-mrna-abstract]. Genome-wide polysome profiling showed that Gemin5 promotes polysome association and translation of mRNAs bearing 5' terminal oligopyrimidine (TOP) motifs, which encode ribosomal proteins, and of replication-dependent histone mRNAs bearing the 3' histone stem-loop [embarc-buh-2022-gemin5-polysomes-abstract]. Structural work on the C-terminal half explains how RNA binding is organized: the TPR dimer and a C-terminal pentamerization region assemble a ~750 kDa homodecamer, and an intact decamer is required for binding cognate RNA ligands and regulating translation [guo-2022-gemin5-decamer-abstract; guo-2022-gemin5-decamer-fulltext]. It should be emphasized that most of the translation-related findings come from a single research group and from transformed human cell lines, and their quantitative contribution to physiology in vivo remains less certain than the snRNP-assembly role.

## 6. Subcellular Localization

GEMIN5 is predominantly cytoplasmic but is also found in the nucleus. Its discoverers observed it in the cytoplasm and nucleoplasm, colocalizing with SMN in nuclear gems [gubitz-2002-gemin5-wd-repeat-abstract]. Subsequent fractionation found Gemin5 more abundant in the cytoplasm than other gemins, largely sedimenting separately from the large SMN complexes, and rarely detectable in nuclear gems or Cajal bodies, suggesting that its main site of action is the cytoplasm where it captures pre-snRNAs [hao-2007-gemin5-absent-cajal-bodies-abstract]. Gemin5 relocalizes under cell stress [battle-2007-smn-independent-subunits-abstract], associates with ribosomes and polysomes in the cytoplasm [francisco-velilla-2016-gemin5-ribosome-abstract], and accumulates with P-body components in SMN-deficient cells [jiang-2018-gemin5-u1-disposal-abstract]. Loss of dimerization does not alter its predominantly cytoplasmic distribution [francisco-velilla-2024-oligomerization-abstract]. The horse UniProt entry's electronic annotations (cytoplasm; nucleus, gem; nucleoplasm) are consistent with these human data [uniprot-A0A9L0R5P7-entry]. The 76-residue lysine-rich segment absent from the horse gene model could conceivably bear on nuclear partitioning, but no study has tested a nuclear localization signal in this region.

## 7. Physiological Importance and Disease Relevance

GEMIN5 is essential for development across vertebrates and invertebrates. Knockout of Gemin5 in mice causes early embryonic lethality [rajan-2022-gemin5-ataxia-abstract]; zebrafish null mutants die by two weeks with dysplastic phenotypes [saida-2021-gemin5-cerebellar-atrophy-abstract]; and knockdown of the Drosophila orthologue rigor mortis causes developmental defects, motor dysfunction and shortened lifespan [kour-2021-gemin5-neurodevelopmental-abstract]. In humans, biallelic hypomorphic GEMIN5 variants cause a neurodevelopmental disorder with developmental delay, hypotonia, cerebellar ataxia and cerebellar atrophy; patient iPSC-derived neurons show reduced GEMIN5 stability, perturbed SMN-complex partners and defective snRNP assembly, with a transcriptomic signature distinct from spinal muscular atrophy [kour-2021-gemin5-neurodevelopmental-abstract; saida-2021-gemin5-cerebellar-atrophy-abstract; rajan-2022-gemin5-ataxia-abstract]. Variants in the TPR-like domain disrupt dimerization and ribosome association, whereas an RBS1 variant destabilizes the protein, linking both structural modules to disease [francisco-velilla-2022-gemin5-variants-abstract]. Increasing SMN levels raises GEMIN5 levels and ameliorates snRNP and splicing defects caused by GEMIN5 loss, underscoring the functional interdependence of the two proteins [fortuna-2023-smn-regulates-gemin5-abstract]. No GEMIN5-associated phenotype has been reported in horses.

## 8. Synthesis: Predicted Function of Horse GEMIN5

Taking the orthology evidence together with the human and model-organism literature, horse GEMIN5 (A0A9L0R5P7) is best described as the snRNA-binding subunit of the SMN complex. Its tandem WD40 beta-propellers are predicted to recognize the Sm site and adjacent features of m7G-capped pre-snRNAs in the cytoplasm and deliver them to the SMN-Gemin2-Sm assembly intermediate, thereby conferring RNA specificity on spliceosomal snRNP core assembly (GO-relevant processes: spliceosomal snRNP assembly; molecular functions: snRNA binding, m7G cap binding; component: SMN complex/SMN-Sm protein complex, cytoplasm, with a minor nuclear/gem pool) [battle-2006-gemin5-identifies-snrnas-abstract; jin-2016-gemin5-double-wd40-abstract; xu-2016-gemin5-pre-snrna-selection-abstract]. Secondary, SMN-complex-independent functions are likely conserved and include ribosome (60S) binding and modulation of global and selective translation through its TPR dimerization hub and C-terminal decameric RNA-binding region [francisco-velilla-2016-gemin5-ribosome-abstract; guo-2022-gemin5-decamer-abstract; embarc-buh-2022-gemin5-polysomes-abstract], and quality control of aberrant snRNAs via cap recognition [xu-2016-gemin5-pre-snrna-selection-abstract]. All of these assignments are inferences from orthology; none has been tested in equine cells.

## Open Questions

Several issues would merit follow-up. The most immediate for this specific entry concerns the 76-residue linker missing from A0A9L0R5P7: RefSeq models include it, so direct horse RNA-seq or proteomic evidence would be needed to determine whether a linker-skipping transcript is actually expressed (and in which tissues), and whether the lysine-rich linker contributes to nuclear targeting or protein interactions in any species. More generally, the relative importance of Gemin5 in snRNP biogenesis versus translation regulation in vivo remains unresolved, since most translation studies derive from a single laboratory using transformed cell lines and overexpressed fragments. The physiological role of m7G cap binding is still debated, given that one structural study interpreted the Tyr474 site as an alternative RNA-binding mode rather than a dedicated cap pocket. The mechanism by which ATP hydrolysis releases snRNA from Gemin5 to the Sm ring, and the structure of full-length Gemin5 within the intact SMN complex (including how the WD40 domain, TPR dimer and C-terminal decamer co-exist), have not been determined. Finally, the early report that Gemin5 knockdown did not impair Sm core assembly has not been explicitly reconciled with later findings, and tissue-specific requirements (for example in cerebellum and motor neurons, as suggested by the human disorder) remain to be explored in mammals other than human and mouse.

## References

Citation keys in the text carry a suffix (-abstract, -fulltext, -summary, -entry) indicating which file in `citations/` supports the statement.

- [abellan-2025-phosphoresidues-ribosome] Abellan S, Escos A, Francisco-Velilla R, et al. Impact of Gemin5 in protein synthesis: phosphoresidues of the dimerization domain regulate ribosome binding. RNA biology (2025). PMID:40734649; PMCID:PMC12323416; DOI:10.1080/15476286.2025.2540654. https://pubmed.ncbi.nlm.nih.gov/40734649/
- [battle-2006-gemin5-identifies-snrnas] Battle DJ, Lau CK, Wan L, et al. The Gemin5 protein of the SMN complex identifies snRNAs. Molecular cell (2006). PMID:16857593; DOI:10.1016/j.molcel.2006.05.036. https://pubmed.ncbi.nlm.nih.gov/16857593/
- [battle-2007-smn-independent-subunits] Battle DJ, Kasim M, Wang J, et al. SMN-independent subunits of the SMN complex. Identification of a small nuclear ribonucleoprotein assembly intermediate. The Journal of biological chemistry (2007). PMID:17640873; DOI:10.1074/jbc.M702317200. https://pubmed.ncbi.nlm.nih.gov/17640873/
- [bradrick-2009-gemin5-cap-binding] Bradrick SS, Gromeier M. Identification of gemin5 as a novel 7-methylguanosine cap-binding protein. PloS one (2009). PMID:19750007; PMCID:PMC2736588; DOI:10.1371/journal.pone.0007030. https://pubmed.ncbi.nlm.nih.gov/19750007/
- [chari-2008-assembly-chaperoning] Chari A, Golas MM, Klingenhäger M, et al. An assembly chaperone collaborates with the SMN complex to generate spliceosomal SnRNPs. Cell (2008). PMID:18984161; DOI:10.1016/j.cell.2008.09.020. https://pubmed.ncbi.nlm.nih.gov/18984161/
- [embarc-buh-2021-rbs1-unstructured] Embarc-Buh A, Francisco-Velilla R, Camero S, et al. The RBS1 domain of Gemin5 is intrinsically unstructured and interacts with RNA through conserved Arg and aromatic residues. RNA biology (2021). PMID:34424823; PMCID:PMC8677033; DOI:10.1080/15476286.2021.1962666. https://pubmed.ncbi.nlm.nih.gov/34424823/
- [embarc-buh-2022-gemin5-polysomes] Embarc-Buh A, Francisco-Velilla R, Garcia-Martin JA, et al. Gemin5-dependent RNA association with polysomes enables selective translation of ribosomal and histone mRNAs. Cellular and molecular life sciences : CMLS (2022). PMID:35987821; PMCID:PMC9392717; DOI:10.1007/s00018-022-04519-4. https://pubmed.ncbi.nlm.nih.gov/35987821/
- [fernandez-chamorro-2014-noncanonical-rbs] Fernandez-Chamorro J, Piñeiro D, Gordon JM, et al. Identification of novel non-canonical RNA-binding sites in Gemin5 involved in internal initiation of translation. Nucleic acids research (2014). PMID:24598255; PMCID:PMC4027194; DOI:10.1093/nar/gku177. https://pubmed.ncbi.nlm.nih.gov/24598255/
- [fortuna-2023-smn-regulates-gemin5] Fortuna TR, Kour S, Chimata AV, et al. SMN regulates GEMIN5 expression and acts as a modifier of GEMIN5-mediated neurodegeneration. Acta neuropathologica (2023). PMID:37369805; PMCID:PMC11348892; DOI:10.1007/s00401-023-02607-8. https://pubmed.ncbi.nlm.nih.gov/37369805/
- [francisco-velilla-2016-gemin5-ribosome] Francisco-Velilla R, Fernandez-Chamorro J, Ramajo J, et al. The RNA-binding protein Gemin5 binds directly to the ribosome and regulates global translation. Nucleic acids research (2016). PMID:27507887; PMCID:PMC5041490; DOI:10.1093/nar/gkw702. https://pubmed.ncbi.nlm.nih.gov/27507887/
- [francisco-velilla-2018-rbs-feedback] Francisco-Velilla R, Fernandez-Chamorro J, Dotu I, et al. The landscape of the non-canonical RNA-binding site of Gemin5 unveils a feedback loop counteracting the negative effect on translation. Nucleic acids research (2018). PMID:29771365; PMCID:PMC6101553; DOI:10.1093/nar/gky361. https://pubmed.ncbi.nlm.nih.gov/29771365/
- [francisco-velilla-2020-pxss-rbs1] Francisco-Velilla R, Embarc-Buh A, Rangel-Guerrero S, et al. RNA-protein coevolution study of Gemin5 uncovers the role of the PXSS motif of RBS1 domain for RNA binding. RNA biology (2020). PMID:32476560; PMCID:PMC7549667; DOI:10.1080/15476286.2020.1762054. https://pubmed.ncbi.nlm.nih.gov/32476560/
- [francisco-velilla-2022-gemin5-variants] Francisco-Velilla R, Embarc-Buh A, Del Caño-Ochoa F, et al. Functional and structural deficiencies of Gemin5 variants associated with neurological disorders. Life science alliance (2022). PMID:35393353; PMCID:PMC8989681; DOI:10.26508/lsa.202201403. https://pubmed.ncbi.nlm.nih.gov/35393353/
- [francisco-velilla-2022-t897-phosphorylation] Francisco-Velilla R, Embarc-Buh A, Abellan S, et al. Phosphorylation of T897 in the dimerization domain of Gemin5 modulates protein interactions and translation regulation. Computational and structural biotechnology journal (2022). PMID:36420152; PMCID:PMC9676205; DOI:10.1016/j.csbj.2022.11.018. https://pubmed.ncbi.nlm.nih.gov/36420152/
- [francisco-velilla-2024-oligomerization] Francisco-Velilla R, Abellan S, Embarc-Buh A, et al. Oligomerization regulates the interaction of Gemin5 with members of the SMN complex and the translation machinery. Cell death discovery (2024). PMID:38942768; PMCID:PMC11213948; DOI:10.1038/s41420-024-02057-5. https://pubmed.ncbi.nlm.nih.gov/38942768/
- [gubitz-2002-gemin5-wd-repeat] Gubitz AK, Mourelatos Z, Abel L, et al. Gemin5, a novel WD repeat protein component of the SMN complex that binds Sm proteins. The Journal of biological chemistry (2002). PMID:11714716; DOI:10.1074/jbc.M109448200. https://pubmed.ncbi.nlm.nih.gov/11714716/
- [guo-2022-gemin5-decamer] Guo Q, Zhao S, Francisco-Velilla R, et al. Structural basis for Gemin5 decamer-mediated mRNA binding. Nature communications (2022). PMID:36056043; PMCID:PMC9440017; DOI:10.1038/s41467-022-32883-z. https://pubmed.ncbi.nlm.nih.gov/36056043/
- [hao-2007-gemin5-absent-cajal-bodies] Hao le T, Fuller HR, Lam le T, et al. Absence of gemin5 from SMN complexes in nuclear Cajal bodies. BMC cell biology (2007). PMID:17640370; PMCID:PMC1939999; DOI:10.1186/1471-2121-8-28. https://pubmed.ncbi.nlm.nih.gov/17640370/
- [jiang-2018-gemin5-u1-disposal] Jiang D, Zou X, Zhang C, et al. Gemin5 plays a role in unassembled-U1 snRNA disposal in SMN-deficient cells. FEBS letters (2018). PMID:29537490; DOI:10.1002/1873-3468.13031. https://pubmed.ncbi.nlm.nih.gov/29537490/
- [jin-2016-gemin5-double-wd40] Jin W, Wang Y, Liu CP, et al. Structural basis for snRNA recognition by the double-WD40 repeat domain of Gemin5. Genes & development (2016). PMID:27881601; PMCID:PMC5131779; DOI:10.1101/gad.291377.116. https://pubmed.ncbi.nlm.nih.gov/27881601/
- [kour-2021-gemin5-neurodevelopmental] Kour S, Rajan DS, Fortuna TR, et al. Loss of function mutations in GEMIN5 cause a neurodevelopmental disorder. Nature communications (2021). PMID:33963192; PMCID:PMC8105379; DOI:10.1038/s41467-021-22627-w. https://pubmed.ncbi.nlm.nih.gov/33963192/
- [lau-2009-gemin5-snrna-wd-repeat] Lau CK, Bachorik JL, Dreyfuss G. Gemin5-snRNA interaction reveals an RNA binding function for WD repeat domains. Nature structural & molecular biology (2009). PMID:19377484; DOI:10.1038/nsmb.1584. https://pubmed.ncbi.nlm.nih.gov/19377484/
- [martinez-salas-2020-emerging-roles-review] Martinez-Salas E, Embarc-Buh A, Francisco-Velilla R. Emerging Roles of Gemin5: From snRNPs Assembly to Translation Control. International journal of molecular sciences (2020). PMID:32485878; PMCID:PMC7311978; DOI:10.3390/ijms21113868. https://pubmed.ncbi.nlm.nih.gov/32485878/
- [martinez-salas-2025-gemin5-interactions-review] Martinez-Salas E, Abellan S, Francisco-Velilla R. Understanding GEMIN5 Interactions: From Structural and Functional Insights to Selective Translation. Wiley interdisciplinary reviews. RNA (2025). PMID:40176294; PMCID:PMC11965781; DOI:10.1002/wrna.70008. https://pubmed.ncbi.nlm.nih.gov/40176294/
- [moreno-morcillo-2020-gemin5-dimerization] Moreno-Morcillo M, Francisco-Velilla R, Embarc-Buh A, et al. Structural basis for the dimerization of Gemin5 and its role in protein recruitment and translation control. Nucleic acids research (2020). PMID:31799608; PMCID:PMC6954437; DOI:10.1093/nar/gkz1126. https://pubmed.ncbi.nlm.nih.gov/31799608/
- [neuenkirchen-2015-reconstitution-snrnp] Neuenkirchen N, Englbrecht C, Ohmer J, et al. Reconstitution of the human U snRNP assembly machinery reveals stepwise Sm protein organization. The EMBO journal (2015). PMID:26069323; PMCID:PMC4547896; DOI:10.15252/embj.201490350. https://pubmed.ncbi.nlm.nih.gov/26069323/
- [otter-2007-smn-interaction-map] Otter S, Grimmler M, Neuenkirchen N, et al. A comprehensive interaction map of the human survival of motor neuron (SMN) complex. The Journal of biological chemistry (2007). PMID:17178713; DOI:10.1074/jbc.M608528200. https://pubmed.ncbi.nlm.nih.gov/17178713/
- [pacheco-2009-gemin5-translation] Pacheco A, López de Quinto S, Ramajo J, et al. A novel role for Gemin5 in mRNA translation. Nucleic acids research (2009). PMID:19066202; PMCID:PMC2632916; DOI:10.1093/nar/gkn979. https://pubmed.ncbi.nlm.nih.gov/19066202/
- [pellizzoni-2002-smn-specificity] Pellizzoni L, Yong J, Dreyfuss G. Essential role for the SMN complex in the specificity of snRNP assembly. Science (New York, N.Y.) (2002). PMID:12459587; DOI:10.1126/science.1074962. https://pubmed.ncbi.nlm.nih.gov/12459587/
- [pineiro-2012-gemin5-l-protease] Piñeiro D, Ramajo J, Bradrick SS, et al. Gemin5 proteolysis reveals a novel motif to identify L protease targets. Nucleic acids research (2012). PMID:22362733; PMCID:PMC3367203; DOI:10.1093/nar/gks172. https://pubmed.ncbi.nlm.nih.gov/22362733/
- [pineiro-2013-gemin5-ires] Piñeiro D, Fernández N, Ramajo J, et al. Gemin5 promotes IRES interaction and translation control through its C-terminal region. Nucleic acids research (2013). PMID:23221641; PMCID:PMC3553989; DOI:10.1093/nar/gks1212. https://pubmed.ncbi.nlm.nih.gov/23221641/
- [rajan-2022-gemin5-ataxia] Rajan DS, Kour S, Fortuna TR, et al. Autosomal Recessive Cerebellar Atrophy and Spastic Ataxia in Patients With Pathogenic Biallelic Variants in GEMIN5. Frontiers in cell and developmental biology (2022). PMID:35295849; PMCID:PMC8918504; DOI:10.3389/fcell.2022.783762. https://pubmed.ncbi.nlm.nih.gov/35295849/
- [saida-2021-gemin5-cerebellar-atrophy] Saida K, Tamaoki J, Sasaki M, et al. Pathogenic variants in the survival of motor neurons complex gene GEMIN5 cause cerebellar atrophy. Clinical genetics (2021). PMID:34569062; DOI:10.1111/cge.14066. https://pubmed.ncbi.nlm.nih.gov/34569062/
- [shpargel-2005-gemin-proteins-required] Shpargel KB, Matera AG. Gemin proteins are required for efficient assembly of Sm-class ribonucleoproteins. Proceedings of the National Academy of Sciences of the United States of America (2005). PMID:16301532; PMCID:PMC1297697; DOI:10.1073/pnas.0508947102. https://pubmed.ncbi.nlm.nih.gov/16301532/
- [so-2016-u1-snrnp-pathway] So BR, Wan L, Zhang Z, et al. A U1 snRNP-specific assembly pathway reveals the SMN complex as a versatile hub for RNP exchange. Nature structural & molecular biology (2016). PMID:26828962; PMCID:PMC4834709; DOI:10.1038/nsmb.3167. https://pubmed.ncbi.nlm.nih.gov/26828962/
- [tang-2016-gemin5-pre-snrna] Tang X, Bharath SR, Piao S, et al. Structural basis for specific recognition of pre-snRNA by Gemin5. Cell research (2016). PMID:27834343; PMCID:PMC5143419; DOI:10.1038/cr.2016.133. https://pubmed.ncbi.nlm.nih.gov/27834343/
- [wade-2009-horse-genome] Wade CM, Giulotto E, Sigurdsson S, et al. Genome sequence, comparative analysis, and population genetics of the domestic horse. Science (New York, N.Y.) (2009). PMID:19892987; PMCID:PMC3785132; DOI:10.1126/science.1178158. https://pubmed.ncbi.nlm.nih.gov/19892987/
- [wahl-2016-right-pick] Wahl MC, Fischer U. The right pick: structural basis of snRNA selection by Gemin5. Genes & development (2016). PMID:27881598; PMCID:PMC5131775; DOI:10.1101/gad.293084.116. https://pubmed.ncbi.nlm.nih.gov/27881598/
- [workman-2015-gemin5-smn-mrna] Workman E, Kalda C, Patel A, et al. Gemin5 Binds to the Survival Motor Neuron mRNA to Regulate SMN Expression. The Journal of biological chemistry (2015). PMID:25911097; PMCID:PMC4505476; DOI:10.1074/jbc.M115.646257. https://pubmed.ncbi.nlm.nih.gov/25911097/
- [xu-2016-gemin5-pre-snrna-selection] Xu C, Ishikawa H, Izumikawa K, et al. Structural insights into Gemin5-guided selection of pre-snRNAs for snRNP assembly. Genes & development (2016). PMID:27881600; PMCID:PMC5131778; DOI:10.1101/gad.288340.116. https://pubmed.ncbi.nlm.nih.gov/27881600/
- [yang-2025-u7-snrna-gemin5] Yang XC, Dominski Z. Proteins that recognize unique features of U7 snRNA and may substitute for Gemin5 in the assembly of U7-specific Sm ring. RNA (New York, N.Y.) (2025). PMID:40592581; PMCID:PMC12360213; DOI:10.1261/rna.080491.125. https://pubmed.ncbi.nlm.nih.gov/40592581/
- [yong-2010-gemin5-delivers-snrna] Yong J, Kasim M, Bachorik JL, et al. Gemin5 delivers snRNA precursors to the SMN complex for snRNP biogenesis. Molecular cell (2010). PMID:20513430; PMCID:PMC2901871; DOI:10.1016/j.molcel.2010.03.014. https://pubmed.ncbi.nlm.nih.gov/20513430/
- [ncbi-refseq-horse-gemin5-isoforms] NCBI Protein RefSeq records XP_005599323, XP_023473111, XP_023473114, XP_023473115 (gem-associated protein 5 isoforms X1-X4, Equus caballus); sequences in citations/ncbi-refseq-horse-gemin5-isoforms.fasta. https://www.ncbi.nlm.nih.gov/protein/XP_005599323
- [uniprot-A0A9L0R5P7-entry] UniProtKB/TrEMBL A0A9L0R5P7 (GEMIN5, Equus caballus), entry version 15. https://rest.uniprot.org/uniprotkb/A0A9L0R5P7.txt
- [uniprot-Q8TEQ6-human-entry] UniProtKB/Swiss-Prot Q8TEQ6 (human GEMIN5). https://rest.uniprot.org/uniprotkb/Q8TEQ6.txt


## Citations

1. _metadata.jsonl
2. abellan-2025-phosphoresidues-ribosome-abstract.md
3. abellan-2025-phosphoresidues-ribosome-fulltext.txt
4. abellan-2025-phosphoresidues-ribosome-summary.md
5. battle-2006-gemin5-identifies-snrnas-abstract.md
6. battle-2006-gemin5-identifies-snrnas-summary.md
7. battle-2007-smn-independent-subunits-abstract.md
8. battle-2007-smn-independent-subunits-summary.md
9. bradrick-2009-gemin5-cap-binding-abstract.md
10. bradrick-2009-gemin5-cap-binding-fulltext.txt
11. bradrick-2009-gemin5-cap-binding-summary.md
12. chari-2008-assembly-chaperoning-abstract.md
13. chari-2008-assembly-chaperoning-summary.md
14. embarc-buh-2021-rbs1-unstructured-abstract.md
15. embarc-buh-2021-rbs1-unstructured-fulltext.txt
16. embarc-buh-2021-rbs1-unstructured-summary.md
17. embarc-buh-2022-gemin5-polysomes-abstract.md
18. embarc-buh-2022-gemin5-polysomes-fulltext.txt
19. embarc-buh-2022-gemin5-polysomes-summary.md
20. fernandez-chamorro-2014-noncanonical-rbs-abstract.md
21. fernandez-chamorro-2014-noncanonical-rbs-fulltext.txt
22. fernandez-chamorro-2014-noncanonical-rbs-summary.md
23. fortuna-2023-smn-regulates-gemin5-abstract.md
24. fortuna-2023-smn-regulates-gemin5-summary.md
25. francisco-velilla-2016-gemin5-ribosome-abstract.md
26. francisco-velilla-2016-gemin5-ribosome-fulltext.txt
27. francisco-velilla-2016-gemin5-ribosome-summary.md
28. francisco-velilla-2018-rbs-feedback-abstract.md
29. francisco-velilla-2018-rbs-feedback-fulltext.txt
30. francisco-velilla-2018-rbs-feedback-summary.md
31. francisco-velilla-2020-pxss-rbs1-abstract.md
32. francisco-velilla-2020-pxss-rbs1-summary.md
33. francisco-velilla-2022-gemin5-variants-abstract.md
34. francisco-velilla-2022-gemin5-variants-fulltext.txt
35. francisco-velilla-2022-gemin5-variants-summary.md
36. francisco-velilla-2022-t897-phosphorylation-abstract.md
37. francisco-velilla-2022-t897-phosphorylation-fulltext.txt
38. francisco-velilla-2022-t897-phosphorylation-summary.md
39. francisco-velilla-2024-oligomerization-abstract.md
40. francisco-velilla-2024-oligomerization-fulltext.txt
41. francisco-velilla-2024-oligomerization-summary.md
42. gubitz-2002-gemin5-wd-repeat-abstract.md
43. gubitz-2002-gemin5-wd-repeat-summary.md
44. guo-2022-gemin5-decamer-abstract.md
45. guo-2022-gemin5-decamer-fulltext.txt
46. guo-2022-gemin5-decamer-summary.md
47. hao-2007-gemin5-absent-cajal-bodies-abstract.md
48. hao-2007-gemin5-absent-cajal-bodies-fulltext.txt
49. hao-2007-gemin5-absent-cajal-bodies-summary.md
50. jiang-2018-gemin5-u1-disposal-abstract.md
51. jiang-2018-gemin5-u1-disposal-summary.md
52. jin-2016-gemin5-double-wd40-abstract.md
53. jin-2016-gemin5-double-wd40-fulltext.txt
54. jin-2016-gemin5-double-wd40-summary.md
55. kour-2021-gemin5-neurodevelopmental-abstract.md
56. kour-2021-gemin5-neurodevelopmental-fulltext.txt
57. kour-2021-gemin5-neurodevelopmental-summary.md
58. lau-2009-gemin5-snrna-wd-repeat-abstract.md
59. lau-2009-gemin5-snrna-wd-repeat-summary.md
60. martinez-salas-2020-emerging-roles-review-abstract.md
61. martinez-salas-2020-emerging-roles-review-fulltext.txt
62. martinez-salas-2020-emerging-roles-review-summary.md
63. martinez-salas-2025-gemin5-interactions-review-abstract.md
64. martinez-salas-2025-gemin5-interactions-review-fulltext.txt
65. martinez-salas-2025-gemin5-interactions-review-summary.md
66. moreno-morcillo-2020-gemin5-dimerization-abstract.md
67. moreno-morcillo-2020-gemin5-dimerization-fulltext.txt
68. moreno-morcillo-2020-gemin5-dimerization-summary.md
69. ncbi-refseq-horse-gemin5-isoforms-summary.md
70. ncbi-refseq-horse-gemin5-isoforms.fasta
71. neuenkirchen-2015-reconstitution-snrnp-abstract.md
72. neuenkirchen-2015-reconstitution-snrnp-summary.md
73. otter-2007-smn-interaction-map-abstract.md
74. otter-2007-smn-interaction-map-summary.md
75. pacheco-2009-gemin5-translation-abstract.md
76. pacheco-2009-gemin5-translation-fulltext.txt
77. pacheco-2009-gemin5-translation-summary.md
78. pellizzoni-2002-smn-specificity-abstract.md
79. pellizzoni-2002-smn-specificity-summary.md
80. pineiro-2012-gemin5-l-protease-abstract.md
81. pineiro-2012-gemin5-l-protease-fulltext.txt
82. pineiro-2012-gemin5-l-protease-summary.md
83. pineiro-2013-gemin5-ires-abstract.md
84. pineiro-2013-gemin5-ires-fulltext.txt
85. pineiro-2013-gemin5-ires-summary.md
86. rajan-2022-gemin5-ataxia-abstract.md
87. rajan-2022-gemin5-ataxia-fulltext.txt
88. rajan-2022-gemin5-ataxia-summary.md
89. saida-2021-gemin5-cerebellar-atrophy-abstract.md
90. saida-2021-gemin5-cerebellar-atrophy-summary.md
91. shpargel-2005-gemin-proteins-required-abstract.md
92. shpargel-2005-gemin-proteins-required-summary.md
93. so-2016-u1-snrnp-pathway-abstract.md
94. so-2016-u1-snrnp-pathway-fulltext.txt
95. so-2016-u1-snrnp-pathway-summary.md
96. tang-2016-gemin5-pre-snrna-abstract.md
97. tang-2016-gemin5-pre-snrna-fulltext.txt
98. tang-2016-gemin5-pre-snrna-summary.md
99. uniprot-A0A9L0R5P7-entry.txt
100. uniprot-A0A9L0R5P7-summary.md
101. uniprot-Q8TEQ6-human-entry.txt
102. uniprot-Q8TEQ6-human-summary.md
103. wade-2009-horse-genome-abstract.md
104. wade-2009-horse-genome-summary.md
105. wahl-2016-right-pick-abstract.md
106. wahl-2016-right-pick-fulltext.txt
107. wahl-2016-right-pick-summary.md
108. workman-2015-gemin5-smn-mrna-abstract.md
109. workman-2015-gemin5-smn-mrna-summary.md
110. xu-2016-gemin5-pre-snrna-selection-abstract.md
111. xu-2016-gemin5-pre-snrna-selection-fulltext.txt
112. xu-2016-gemin5-pre-snrna-selection-summary.md
113. yang-2025-u7-snrna-gemin5-abstract.md
114. yang-2025-u7-snrna-gemin5-fulltext.txt
115. yang-2025-u7-snrna-gemin5-summary.md
116. yong-2010-gemin5-delivers-snrna-abstract.md
117. yong-2010-gemin5-delivers-snrna-summary.md