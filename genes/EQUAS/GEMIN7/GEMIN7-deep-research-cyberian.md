---
provider: cyberian
model: deep-research
cached: false
start_time: '2026-10-25T23:41:41.355204'
end_time: '2026-10-25T23:52:29.114648'
duration_seconds: 647.76
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: EQUAS
  gene_id: GEMIN7
  gene_symbol: GEMIN7
  uniprot_accession: A0A9L0ICL9
  protein_description: 'RecName: Full=Gem-associated protein 7 {ECO:0000256|ARBA:ARBA00067671};'
  gene_info: Name=GEMIN7 {ECO:0000313|Ensembl:ENSEASP00005037966.1};
  organism_full: Equus asinus (Donkey) (Equus africanus asinus).
  protein_family: Belongs to the gemin-7 family.
  protein_domains: Sm. (IPR047575); SMN_gemin7. (IPR020338); Gemin7 (PF11095)
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
citation_count: 69
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** A0A9L0ICL9
- **Protein Description:** RecName: Full=Gem-associated protein 7 {ECO:0000256|ARBA:ARBA00067671};
- **Gene Information:** Name=GEMIN7 {ECO:0000313|Ensembl:ENSEASP00005037966.1};
- **Organism (full):** Equus asinus (Donkey) (Equus africanus asinus).
- **Protein Family:** Belongs to the gemin-7 family.
- **Key Domains:** Sm. (IPR047575); SMN_gemin7. (IPR020338); Gemin7 (PF11095)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "GEMIN7" matches the protein description above**
2. **Verify the organism is correct:** Equus asinus (Donkey) (Equus africanus asinus).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'GEMIN7' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **GEMIN7** (gene ID: GEMIN7, UniProt: A0A9L0ICL9) in EQUAS.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# GEMIN7 (Gem-associated protein 7) in the donkey, *Equus asinus* (UniProt A0A9L0ICL9)

## 1. Introduction and summary

GEMIN7 is a small, non-catalytic subunit of the survival of motor neurons (SMN) complex. This multiprotein machine assembles the heptameric Sm protein ring (the "Sm core") onto spliceosomal U-rich small nuclear RNAs (snRNAs), making it essential for producing spliceosomal snRNPs and so for pre-mRNA splicing [baccon-2002-gemin7-abstract; chari-2008-assembly-chaperone-abstract]. Gemin7 has no enzymatic activity. It works as a structural adaptor and Sm-protein mimic. It forms an obligate heterodimer with Gemin6, and both proteins adopt the canonical Sm fold even though their sequences show no significant similarity to Sm proteins [ma-2005-gemin6-gemin7-structure-abstract]. Gemin7 links Gemin6 to the rest of the SMN complex [baccon-2002-gemin7-abstract]. It provides the docking site for Unrip (STRAP) [grimmler-2005-unrip-abstract], and it is bridged to SMN by Gemin8 [carissimi-2006-gemin8-architecture-abstract; veepaschit-2021-pombe-smn-fulltext]. Gemin7 binds several Sm proteins, SmE most strongly [baccon-2002-gemin7-abstract]. The current model is that the Gemin6–Gemin7 heterodimer stands in for the SmD3–SmB dimer in an assembly intermediate on the SMN complex, and is later exchanged for authentic SmD3–SmB in an Unrip-dependent step that closes the Sm ring on snRNA [ogawa-2009-smn-components-snrnp-fulltext; cauchi-2014-gem-depletion-fulltext]. Reconstitution work in fission yeast adds a second role. Bound to the SMN YG box, the Gemin6/7/8 module is needed to release the assembly chaperone pICln from the Sm-protein precursor complex [hu-2023-pombe-snrnp-core-assembly-fulltext; hu-2026-icln-release-module-fulltext]. In human cells the protein is found in the cytoplasm, where snRNP core assembly happens, and in the nucleus, where it is concentrated in gems (Gemini of Cajal bodies) [baccon-2002-gemin7-abstract].

No experimental study has examined donkey GEMIN7 directly. The donkey entry A0A9L0ICL9 is an unreviewed, automatically annotated gene model from the donkey reference genome [wang-2020-donkey-genomes-fulltext; uniprot-A0A9L0ICL9-summary]. Everything below about function is therefore inferred from orthology, mainly to human GEMIN7 (Q9H840), along with mouse, fission yeast and fly data. The sequence evidence for that inference is strong. The structured Sm-fold region is about 95% identical between donkey and human, which makes it very likely that the donkey protein has the same structure, partners and function.

## 2. Identity of the target and verification of orthology

UniProt entry A0A9L0ICL9 is a 206-residue protein named "Gem-associated protein 7" with gene name GEMIN7. It comes from Ensembl gene ENSEASG00005033816 on donkey chromosome 26 and was predicted from the donkey genome assembly reported by Wang and colleagues [uniprot-A0A9L0ICL9-summary; wang-2020-donkey-genomes-abstract]. Its domain annotations (Pfam PF11095 "Gemin7", InterPro IPR020338 SMN_gemin7, an Sm-type domain PS52002 at residues 140–206, PANTHER family PTHR14679) and its assignment to the gemin-7 family match what is known for vertebrate Gemin7. The symbol is therefore not ambiguous, and the literature on "Gemin7" applies to this protein.

To check orthology, I aligned the donkey sequence with reviewed human GEMIN7 (Q9H840, 131 residues). Donkey residues 76–206 align end to end with human residues 1–131 without gaps, and 115 of 131 positions are identical (87.8%) [uniprot-A0A9L0ICL9-summary]. Most of the substitutions fall in the flexible N-terminal segment. Across the region resolved in the human crystal structures (human residues 47–131, donkey 122–206) seven positions differ, three of them in the first few residues (human 47, 48 and 51). Only four differ within human 52–131 (H76R, R87H, A89T and S126A in human numbering, giving about 95% identity), and none of these are drastic substitutions. The only significant difference is a 75-residue N-terminal extension in the donkey model that has no counterpart in human GEMIN7. Comparing the horse gene models helps here. Horse has three unreviewed GEMIN7 models. One has 131 residues and matches donkey residues 76–206 almost exactly. One has 136 residues and adds a short N-terminal "MLAR" stretch. The third has 179 residues and carries 48 residues of upstream sequence (beginning MEFRRCRRRASQSLRPRALDGLSDLCVDSV…) that are essentially identical to donkey residues 28–75 [uniprot-gemin7-orthologs-summary]. So the extension is not unique to the donkey annotation. It reflects upstream in-frame coding potential that annotation pipelines model in both equid genomes. The AlphaFold model of the donkey protein argues against it being a structured domain. Mean predicted confidence (pLDDT) is 37.5 over residues 1–75, compared with 89–94 over the Sm-fold region (residues 121–206), which means the extension is predicted to be disordered [alphafold-A0A9L0ICL9-summary]. Mouse Gemin7 (129 residues) and the human reviewed protein both begin at the conserved "MQ(T/S)P" start [uniprot-gemin7-orthologs-summary]. The canonical, experimentally characterized form of the protein therefore corresponds to donkey residues 76–206, and whether a longer isoform is expressed is still unknown (see Open Questions). Human Gemin7 has an arginine/glycine-rich N-terminal region that Baccon et al. found to be necessary for binding SMN [baccon-2002-gemin7-abstract]. The corresponding R/G/P-rich stretch is conserved in the donkey sequence (donkey residues ~76–120).

## 3. Discovery and composition of the SMN complex

Gemin7 was found by the Dreyfuss laboratory. They purified native SMN complexes from cell lines expressing tagged SMN or Gemin2 and identified the proteins by mass spectrometry. The same approach had shortly before revealed Gemin6 [pellizzoni-2002-gemin6-abstract; baccon-2002-gemin7-abstract]. Co-immunoprecipitation and immunolocalization confirmed that Gemin7 is a genuine SMN complex component. In vitro binding showed that it interacts directly with both SMN and Gemin6 and that it is required for Gemin6 to join the complex [baccon-2002-gemin7-abstract]. Gemin7 also binds several Sm proteins, with a preference for SmE [baccon-2002-gemin7-abstract], and Gemin6 likewise binds Sm proteins [pellizzoni-2002-gemin6-abstract]. Two further subunits were added later: the WD-repeat protein Unrip (STRAP), which binds Gemin6 and Gemin7 directly [carissimi-2005-unrip-abstract], and Gemin8, which binds the Gemin6–Gemin7 heterodimer directly [carissimi-2006-gemin8-novel-abstract]. The vertebrate SMN complex is now considered to have nine core members: SMN, Gemins 2–8 and Unrip [otter-2007-smn-interaction-map-abstract; cauchi-2014-gem-depletion-fulltext].

The complex is modular. Sedimentation and immunoprecipitation of cell extracts show stable subcomplexes that do not contain SMN. One of these is Gemin6–Gemin7–Unrip, and its levels stay much the same when SMN is depleted [battle-2007-smn-independent-subunits-abstract]. Gemin6, Gemin7 and Unrip form a stable cytoplasmic unit. Its association with SMN requires Gemin8, which binds SMN directly and bridges it to the Gemin6/7 heterodimer. When Gemin8 is knocked down, Gemin6/7/Unrip separate from SMN [carissimi-2006-gemin8-architecture-abstract]. Otter et al. built a full interaction map of the human complex and reconstituted it from recombinant parts. In their map SMN, Gemin8 and Gemin7 form the central building block onto which the other subunits attach [otter-2007-smn-interaction-map-abstract]. Later interpretations of the map describe Gemin8 as interacting with Gemins 4 and 7, Gemin7 as recruiting Unrip and Gemin6, and Gemin7 as also able to associate with Gemin2 [cauchi-2014-gem-depletion-fulltext]. Ogawa et al. confirmed a direct Gemin2–Gemin7 interaction by mammalian two-hybrid and pull-down assays. They found that SMN–Gemin7 binding is stabilized in an SMN–Gemin2–Gemin7 ternary complex [ogawa-2009-smn-components-snrnp-fulltext]. Gemin7 therefore acts as a hub inside the peripheral Gemin6/7/8/Unrip module and connects it to the SMN–Gemin2 core.

## 4. Structure: an Sm-fold heterodimer that mimics Sm proteins

The key structural result for Gemin7 is the crystal structure of the human Gemin6–Gemin7 complex. Neither protein has significant sequence similarity to Sm proteins, yet both adopt canonical Sm folds. They pair as a heterodimer through an interface like the one that joins neighbouring Sm proteins in the Sm ring [ma-2005-gemin6-gemin7-structure-abstract]. The deposited structure (PDB 1Y96, 2.0 Å) resolves Gemin7 residues 47–131 [uniprot-A0A9L0ICL9-summary]. Recombinant Gemin6/Gemin7 binds Sm proteins, which led the authors to suggest that the SMN complex uses Gemin6 and Gemin7 as tools to arrange Sm proteins before the ring forms on snRNA [ma-2005-gemin6-gemin7-structure-abstract]. A higher-resolution (1.52 Å) structure of a human Gemin6(1–92)/Gemin7(46–131)/Gemin8(190–230) trimer (PDB 7BBL) shows how Gemin8 holds the module. A helix-turn-helix motif at the Gemin8 C-terminus packs against the N-terminal α1 helix of Gemin7 through a cluster of hydrophobic residues. The Gemin7 β5–Gemin6 β4 pairing remains intact and forms a continuous ten-stranded β-barrel across the heterodimer [veepaschit-2021-pombe-smn-fulltext]. So Gemin7 has two faces. One is an Sm-like β-sheet edge that pairs with Gemin6 in the way Sm proteins pair with each other. The other is an N-terminal helix and flanking R/G-rich segment that contact Gemin8 and SMN. The donkey protein is essentially invariant across this region (Section 2), so the same architecture is expected.

## 5. Mechanism: Gemin7 in the snRNP core assembly pathway

The SMN complex is part of a two-stage chaperone/catalyst system. First, the PRMT5-complex chaperone pICln binds newly made SmD1/D2/E/F/G and holds them as a ring-shaped 6S intermediate that cannot bind RNA. The SMN complex then binds this unit, displaces pICln, and catalyzes closure of the Sm ring on snRNA [chari-2008-assembly-chaperone-abstract; grimm-2013-structural-basis-abstract]. Gemin2 wraps around the SmD1/D2/F/E/G pentamer [cauchi-2014-gem-depletion-fulltext], and Gemin5 recognizes the "snRNP code" in snRNAs [battle-2006-smn-assembly-machine-abstract]. In this pathway the Gemin6/7/8/Unrip module recruits Sm proteins. Knocking down Gemin8 separates Gemin6/7/Unrip from SMN and reduces the SMN complex's binding to Sm proteins but not to snRNAs [carissimi-2006-gemin8-architecture-abstract]. Depleting Gemin6, Gemin7's obligate partner, strongly lowers SMN complex activity [feng-2005-gemins-modulate-abstract].

Ogawa et al. tested Gemin7's role directly. siRNA knockdown of Gemin7 lowered snRNP assembly activity and reduced the amount of SmE that co-precipitates with SMN [ogawa-2009-smn-components-snrnp-fulltext]. This fits the "subcore" model, in which Gemin6–Gemin7 occupy the position of the SmD3–SmB dimer in an SMN-bound assembly intermediate next to SmE [ogawa-2009-smn-components-snrnp-fulltext; cauchi-2014-gem-depletion-fulltext]. The same study found that Unrip, but not Gemin8, can pull Gemin7 out of the stable SMN–Gemin2–Gemin7 ternary complex in vitro. During in vitro U1 snRNP assembly in normal extracts, Gemin7 left the SMN complex as SmB/B′ arrived. In extracts depleted of Unrip this exchange did not happen [ogawa-2009-smn-components-snrnp-fulltext]. The authors concluded that Unrip helps exchange the Gemin6–Gemin7 placeholder for SmD3–SmB in the last step of Sm core formation [ogawa-2009-smn-components-snrnp-fulltext]. This model is widely restated in reviews [cauchi-2014-gem-depletion-fulltext]. Even so, the exchange has been inferred from co-immunoprecipitation changes and structural analogy. No structure of a Gemin6/7-bound Sm intermediate has been determined (see Open Questions).

Recent reconstitution work in fission yeast points to a second, earlier job for the Gemin6/7/8 module: releasing the pICln (ICln) chaperone. Hu et al. reconstituted *S. pombe* Sm core assembly from purified ICln, SMN, Gemin2 and Gemin6–8. They found that these six proteins are necessary and sufficient for Sm core assembly in vitro [hu-2023-pombe-snrnp-core-assembly-abstract]. SMN and Gemin2 alone could not displace ICln from the 6S ICln–SmD1/D2/F/E/G intermediate. Only the complete five-subunit SMN complex, with Gemin6–8 bound to the C-terminal YG box of SMN, accepted the Sm pentamer and removed ICln efficiently [hu-2023-pombe-snrnp-core-assembly-fulltext]. A follow-up study substituted an engineered budding-yeast Brr1 for fission-yeast Gemin2. In that background, an SMN/Gemin6–8 subcomplex with no Gemin2 was enough to release ICln from an ICln/Sm-pentamer/eBrr1 complex in vitro and in vivo, even though SMN/Gemin6–8 did not bind Sm proteins stably on its own [hu-2026-icln-release-module-fulltext]. The authors describe SMN/Gemin6–8 as a stand-alone ICln-release module and suggest that this module existed before Gemin2 became a stable part of the complex [hu-2026-icln-release-module-abstract]. If the same holds in mammals, Gemin7 helps in two places: pICln removal at the entry of the SMN pathway, and Sm ring completion (the SmD3/B exchange) at its exit. The ICln-release finding comes from the yeast system and has not yet been tested directly with mammalian Gemin7.

Gemin7 is therefore best described as a structural adaptor and placeholder, and part of the module that releases pICln. It has no catalytic activity and no substrate in the enzymatic sense. Its "ligands" are Gemin6 (heterodimer partner), Gemin8 and SMN/Gemin2 (anchoring), Unrip (recruitment and exchange), and Sm proteins, especially SmE (cargo positioning) [baccon-2002-gemin7-abstract; grimmler-2005-unrip-abstract; carissimi-2005-unrip-abstract; ogawa-2009-smn-components-snrnp-fulltext]. The process it serves is spliceosomal snRNP assembly (GO:0000387), within the SMN–Sm protein complex (GO:0034719), and these are the annotations transferred to the donkey entry [uniprot-A0A9L0ICL9-summary].

## 6. Subcellular localization

In human cells Gemin7 colocalizes with SMN in the cytoplasm and in nuclear gems [baccon-2002-gemin7-abstract]. Gems are nuclear bodies, often next to Cajal bodies, where SMN complexes concentrate. The SMN complex is found in both cytoplasm and nucleoplasm [pellizzoni-2002-gemin6-abstract; carissimi-2006-gemin8-novel-abstract]. The Sm core assembly reaction that Gemin7 takes part in happens in the cytoplasm, after snRNA export and before the assembled snRNP is re-imported [chari-2008-assembly-chaperone-abstract; carissimi-2006-gemin8-architecture-abstract]. Gemin7's partners differ in where they go. Unrip is mostly cytoplasmic and absent from gems/Cajal bodies, and depleting Unrip increases nuclear accumulation of SMN in gems. This suggests that the Gemin7–Unrip interaction helps set the cytoplasmic versus nuclear distribution of the complex [grimmler-2005-unrip-abstract]. In neuronal cells, GFP-tagged Gemin7, like SMN, Gemin2, Gemin3 and Gemin6, appears in stationary and dynamic granules in neurites [todd-2010-neurite-granules-abstract]. A companion study by the same group used antibodies against most known SMN partners, Gemin7 among them, in SH-SY5Y neuronal cells. It concluded that not all "core" SMN-binding proteins travel in SMN neurite granules, which suggests that the SMN complex changes its composition in neurites [todd-2010-smn-neurite-granules-cajal-abstract]. Together these studies link SMN–Gemin subcomplexes to cytoplasmic RNP transport, but a specific role for Gemin7 there has not been shown. The donkey entry carries the same localizations (cytoplasm, nucleoplasm, gem), transferred automatically [uniprot-A0A9L0ICL9-summary].

## 7. Evolutionary conservation

Comparative genomics by Kroiss et al. suggested that the SMN complex grew by adding Gemins in blocks to an ancestral SMN–Gemin2 core. On their analysis the Gemin6/7/8 block appeared in early metazoans, and Gemin4 appeared later in deuterostomes [kroiss-2008-minimal-smn-fulltext]. They found no Gemin6–8 orthologs in dipterans (*Drosophila*, *Anopheles*), though these genes are present in hymenopterans. A minimal *Drosophila* complex of SMN, Gemin2, Gemin3 and Gemin5 still carried out accurate Sm core assembly in vitro, which suggests that Gemin7 is not strictly needed for the core chemistry of the reaction [kroiss-2008-minimal-smn-fulltext]. This picture has since been revised in two directions. In *Drosophila*, in vivo interaction screens found SMN-complex partners with homology to Gemins 4/6/7/8, with a Gemin6/7/Unrip module recruited through Gemin8 as in humans [lanfranco-2017-drosophila-smn-abstract]. In fission yeast, sequence and secondary-structure searches found divergent Gemin6, Gemin7 and Gemin8 orthologs that co-purify with SMN and Gemin2. Deleting the *S. pombe* Gemin6, Gemin7 or Gemin8 gene is lethal, and without Gemin8 the SMN/Gemin2 and Gemin6/Gemin7 modules do not associate [veepaschit-2021-pombe-smn-fulltext]. The yeast reconstitution studies discussed in Section 5 add an evolutionary idea: SMN/Gemin6–8 may be an ancient ICln-release unit that predates the stable incorporation of Gemin2 [hu-2026-icln-release-module-abstract]. Hu et al. also argue that the conservation of the SMN YG box, which recruits Gemin6/7/8, implies that Gemin6–8 homologs should exist in many species where they have not yet been found [hu-2023-pombe-snrnp-core-assembly-fulltext]. That view directly challenges the older proposal that Gemin6–8 were added only in metazoans [kroiss-2008-minimal-smn-fulltext]. Gemin7 therefore appears to be much older than metazoans. Its sequence is poorly conserved across long distances but its Sm fold and its Gemin8-anchored position are conserved, and in at least one eukaryote it is essential. Against that background, the near-identity between donkey and human Gemin7 is what one would expect for a conserved housekeeping subunit in placental mammals.

## 8. Physiological and disease relevance

Reduced SMN causes spinal muscular atrophy (SMA), and Gemins have been discussed as modifiers of SMA and as candidate therapeutic targets [borg-2014-gemins-sma-fulltext; feng-2005-gemins-modulate-abstract]. Disruption of the SMN–Gemins complex has also been discussed in amyotrophic lateral sclerosis [cauchi-2014-gem-depletion-fulltext]. SMA-causing missense mutations in the SMN YG-domain disrupt SMN oligomerization and binding to Gemin8. Since Gemin8 is the anchor for Gemin6/7, these mutations are expected to detach the Gemin6/7/Unrip module and reduce complex function [veepaschit-2021-pombe-smn-fulltext; otter-2007-smn-interaction-map-abstract]. I found no primary evidence that GEMIN7 variants cause disease in humans or in equids. No donkey or horse phenotype involving GEMIN7 has been reported in the sources reviewed.

## Open Questions

Several points remain unresolved for this protein. The first concerns the gene model itself. The 75-residue N-terminal extension in A0A9L0ICL9 is absent from human and mouse GEMIN7. Horse gene models share part of it, and AlphaFold predicts it to be disordered [uniprot-gemin7-orthologs-summary; alphafold-A0A9L0ICL9-summary]. Donkey or horse RNA-seq (to map transcription start sites) and proteomics (to detect N-terminal peptides) are needed to decide whether a longer protein is actually made from an upstream start, or whether the canonical MQTP start (donkey Met76) is the only one used. If a longer isoform does exist, it would sit N-terminal to the R/G-rich SMN-binding segment and might affect SMN binding or localization.

Second, the structural basis of the proposed Gemin6/7-for-SmD3/B exchange is still unknown. It is also unclear how the yeast finding that SMN/Gemin6–8 releases ICln [hu-2023-pombe-snrnp-core-assembly-fulltext; hu-2026-icln-release-module-fulltext] fits with the human 6S–SMN–Gemin2 structures, in which Gemin2 and the SMN N-terminus were enough to explain pICln elimination [grimm-2013-structural-basis-abstract]. Reconstitution with human Gemin6/7/8 would test whether mammalian Gemin7 is needed for ICln release. A structure of the SMN complex holding Sm proteins together with Gemin6/7 (for example by cryo-EM of a reconstituted SMN–Gemin2–Gemin6/7/8–Unrip–Sm intermediate) would test whether Gemin7 sits against SmE in the position SmB would normally take, as the subcore model predicts [ogawa-2009-smn-components-snrnp-fulltext; ma-2005-gemin6-gemin7-structure-abstract]. It would also show how Unrip triggers release. Third, the minimal *Drosophila* complex can assemble Sm cores without Gemin7 in vitro [kroiss-2008-minimal-smn-fulltext], yet Gemin7 is essential in fission yeast [veepaschit-2021-pombe-smn-fulltext]. It would be useful to find out whether Gemin7 mainly increases assembly speed or specificity, or whether it has another role, for instance in the Unrip-dependent distribution of the complex between compartments [grimmler-2005-unrip-abstract] or in neurite RNP granules [todd-2010-neurite-granules-abstract]. Finally, knockout or conditional loss-of-function data for Gemin7 in a mammal, and screens of human or animal populations for GEMIN7 variants linked to motor neuron disease, would show whether Gemin7 dosage matters in vivo the way SMN dosage does. Useful next steps include checking Ensembl/Bgee expression data for donkey and horse, and running a phylogenetic analysis of the Gemin7 family that includes the divergent *S. pombe* and *Drosophila* orthologs.

## References

* **baccon-2002-gemin7**: Baccon J, Pellizzoni L, Rappsilber J, Mann M, Dreyfuss G (2002). Identification and characterization of Gemin7, a novel component of the survival of motor neuron complex. *J Biol Chem* 277(35):31957-62. PMID: 12065586; DOI: 10.1074/jbc.M203478200. https://doi.org/10.1074/jbc.M203478200
* **battle-2006-smn-assembly-machine**: Battle DJ, Kasim M, Yong J, Lotti F, Lau CK, Mouaikel J, et al. (2006). The SMN complex: an assembly machine for RNPs. *Cold Spring Harb Symp Quant Biol* 71:313-20. PMID: 17381311; DOI: 10.1101/sqb.2006.71.001. https://doi.org/10.1101/sqb.2006.71.001
* **battle-2007-smn-independent-subunits**: Battle DJ, Kasim M, Wang J, Dreyfuss G (2007). SMN-independent subunits of the SMN complex. Identification of a small nuclear ribonucleoprotein assembly intermediate. *J Biol Chem* 282(38):27953-9. PMID: 17640873; DOI: 10.1074/jbc.M702317200. https://doi.org/10.1074/jbc.M702317200
* **borg-2014-gemins-sma**: Borg R, Cauchi RJ (2014). GEMINs: potential therapeutic targets for spinal muscular atrophy? *Front Neurosci* 8:325. PMID: 25360080; PMCID: PMC4197776; DOI: 10.3389/fnins.2014.00325. https://doi.org/10.3389/fnins.2014.00325
* **carissimi-2005-unrip**: Carissimi C, Baccon J, Straccia M, Chiarella P, Maiolica A, Sawyer A, et al. (2005). Unrip is a component of SMN complexes active in snRNP assembly. *FEBS Lett* 579(11):2348-54. PMID: 15848170; DOI: 10.1016/j.febslet.2005.03.034. https://doi.org/10.1016/j.febslet.2005.03.034
* **carissimi-2006-gemin8-architecture**: Carissimi C, Saieva L, Gabanella F, Pellizzoni L (2006). Gemin8 is required for the architecture and function of the survival motor neuron complex. *J Biol Chem* 281(48):37009-16. PMID: 17023415; DOI: 10.1074/jbc.M607505200. https://doi.org/10.1074/jbc.M607505200
* **carissimi-2006-gemin8-novel**: Carissimi C, Saieva L, Baccon J, Chiarella P, Maiolica A, Sawyer A, et al. (2006). Gemin8 is a novel component of the survival motor neuron complex and functions in small nuclear ribonucleoprotein assembly. *J Biol Chem* 281(12):8126-34. PMID: 16434402; DOI: 10.1074/jbc.M512243200. https://doi.org/10.1074/jbc.M512243200
* **cauchi-2014-gem-depletion**: Cauchi RJ (2014). Gem depletion: amyotrophic lateral sclerosis and spinal muscular atrophy crossover. *CNS Neurosci Ther* 20(7):574-81. PMID: 24645792; PMCID: PMC6492989; DOI: 10.1111/cns.12242. https://doi.org/10.1111/cns.12242
* **chari-2008-assembly-chaperone**: Chari A, Golas MM, Klingenhäger M, Neuenkirchen N, Sander B, Englbrecht C, et al. (2008). An assembly chaperone collaborates with the SMN complex to generate spliceosomal SnRNPs. *Cell* 135(3):497-509. PMID: 18984161; DOI: 10.1016/j.cell.2008.09.020. https://doi.org/10.1016/j.cell.2008.09.020
* **feng-2005-gemins-modulate**: Feng W, Gubitz AK, Wan L, Battle DJ, Dostie J, Golembe TJ, et al. (2005). Gemins modulate the expression and activity of the SMN complex. *Hum Mol Genet* 14(12):1605-11. PMID: 15843395; DOI: 10.1093/hmg/ddi168. https://doi.org/10.1093/hmg/ddi168
* **grimm-2013-structural-basis**: Grimm C, Chari A, Pelz JP, Kuper J, Kisker C, Diederichs K, et al. (2013). Structural basis of assembly chaperone-mediated snRNP formation. *Mol Cell* 49(4):692-703. PMID: 23333303; DOI: 10.1016/j.molcel.2012.12.009. https://doi.org/10.1016/j.molcel.2012.12.009
* **grimmler-2005-unrip**: Grimmler M, Otter S, Peter C, Müller F, Chari A, Fischer U (2005). Unrip, a factor implicated in cap-independent translation, associates with the cytosolic SMN complex and influences its intracellular localization. *Hum Mol Genet* 14(20):3099-111. PMID: 16159890; DOI: 10.1093/hmg/ddi343. https://doi.org/10.1093/hmg/ddi343
* **hu-2023-pombe-snrnp-core-assembly**: Hu Y, Hou Y, Zhou S, Wang Y, Shen C, Mu L, Su D, Zhang R (2023). Mechanism of assembly of snRNP cores assisted by ICln and the SMN complex in fission yeast. *iScience* 26(9):107604. PMID: 37664592; PMCID: PMC10470402; DOI: 10.1016/j.isci.2023.107604. https://doi.org/10.1016/j.isci.2023.107604
* **hu-2026-icln-release-module**: Hu Y, Zhang J, Xu B, Wang Y, Mu L, Zhang R (2026). A stand-alone ICln release module revealed by deconstructing the SMN complex with engineered Brr1. *Nucleic Acids Res* 54(11). PMID: 42261780; PMCID: PMC13249430; DOI: 10.1093/nar/gkag524. https://doi.org/10.1093/nar/gkag524
* **kroiss-2008-minimal-smn**: Kroiss M, Schultz J, Wiesner J, Chari A, Sickmann A, Fischer U (2008). Evolution of an RNP assembly system: a minimal SMN complex facilitates formation of UsnRNPs in Drosophila melanogaster. *Proc Natl Acad Sci U S A* 105(29):10045-50. PMID: 18621711; PMCID: PMC2481332; DOI: 10.1073/pnas.0802287105. https://doi.org/10.1073/pnas.0802287105
* **lanfranco-2017-drosophila-smn**: Lanfranco M, Cacciottolo R, Borg RM, Vassallo N, Juge F, Bordonné R, et al. (2017). Novel interactors of the Drosophila Survival Motor Neuron (SMN) Complex suggest its full conservation. *FEBS Lett* 591(21):3600-3614. PMID: 28949413; DOI: 10.1002/1873-3468.12853. https://doi.org/10.1002/1873-3468.12853
* **ma-2005-gemin6-gemin7-structure**: Ma Y, Dostie J, Dreyfuss G, Van Duyne GD (2005). The Gemin6-Gemin7 heterodimer from the survival of motor neurons complex has an Sm protein-like structure. *Structure* 13(6):883-92. PMID: 15939020; DOI: 10.1016/j.str.2005.03.014. https://doi.org/10.1016/j.str.2005.03.014
* **ogawa-2009-smn-components-snrnp**: Ogawa C, Usui K, Ito F, Itoh M, Hayashizaki Y, Suzuki H (2009). Role of survival motor neuron complex components in small nuclear ribonucleoprotein assembly. *J Biol Chem* 284(21):14609-17. PMID: 19321448; PMCID: PMC2682908; DOI: 10.1074/jbc.M809031200. https://doi.org/10.1074/jbc.M809031200
* **otter-2007-smn-interaction-map**: Otter S, Grimmler M, Neuenkirchen N, Chari A, Sickmann A, Fischer U (2007). A comprehensive interaction map of the human survival of motor neuron (SMN) complex. *J Biol Chem* 282(8):5825-33. PMID: 17178713; DOI: 10.1074/jbc.M608528200. https://doi.org/10.1074/jbc.M608528200
* **pellizzoni-2002-gemin6**: Pellizzoni L, Baccon J, Rappsilber J, Mann M, Dreyfuss G (2002). Purification of native survival of motor neurons complexes and identification of Gemin6 as a novel component. *J Biol Chem* 277(9):7540-5. PMID: 11748230; DOI: 10.1074/jbc.M110141200. https://doi.org/10.1074/jbc.M110141200
* **raimer-2017-smn-chaperone**: Raimer AC, Gray KM, Matera AG (2017). SMN - A chaperone for nuclear RNP social occasions? *RNA Biol* 14(6):701-711. PMID: 27648855; PMCID: PMC5519234; DOI: 10.1080/15476286.2016.1236168. https://doi.org/10.1080/15476286.2016.1236168 (background reading; not cited in text)
* **todd-2010-neurite-granules**: Todd AG, Shaw DJ, Morse R, Stebbings H, Young PJ (2010). SMN and the Gemin proteins form sub-complexes that localise to both stationary and dynamic neurite granules. *Biochem Biophys Res Commun* 394(1):211-6. PMID: 20188701; DOI: 10.1016/j.bbrc.2010.02.158. https://doi.org/10.1016/j.bbrc.2010.02.158
* **todd-2010-smn-neurite-granules-cajal**: Todd AG, Morse R, Shaw DJ, Stebbings H, Young PJ (2010). Analysis of SMN-neurite granules: Core Cajal body components are absent from SMN-cytoplasmic complexes. *Biochem Biophys Res Commun* 397(3):479-85. PMID: 20515655; DOI: 10.1016/j.bbrc.2010.05.139. https://doi.org/10.1016/j.bbrc.2010.05.139
* **uniprot-A0A9L0ICL9**: UniProtKB entries A0A9L0ICL9 (GEMIN7, *Equus asinus*; unreviewed) and Q9H840 (GEMIN7, *Homo sapiens*; reviewed). https://rest.uniprot.org/uniprotkb/A0A9L0ICL9.txt and https://rest.uniprot.org/uniprotkb/Q9H840.txt (retrieved 2026-10-25; records in citations/uniprot-*-record.txt, sequence comparison in citations/uniprot-A0A9L0ICL9-summary.md)
* **uniprot-gemin7-orthologs**: UniProtKB GEMIN7 ortholog entries A0A9L0T0I7, A0A9L0R044 and F7ABS8 (*Equus caballus*, unreviewed) and Q9CWY4 (*Mus musculus*, reviewed). https://rest.uniprot.org/uniprotkb/A0A9L0R044.fasta (and analogous URLs; retrieved 2026-10-25; sequences in citations/uniprot-gemin7-orthologs.fasta)
* **alphafold-A0A9L0ICL9**: AlphaFold Protein Structure Database model AF-A0A9L0ICL9-F1 (v6, created 2025-03-31). https://alphafold.ebi.ac.uk/api/prediction/A0A9L0ICL9 and https://alphafold.ebi.ac.uk/files/AF-A0A9L0ICL9-F1-model_v6.pdb (files in citations/)
* **veepaschit-2021-pombe-smn**: Veepaschit J, Viswanathan A, Bordonné R, Grimm C, Fischer U (2021). Identification and structural analysis of the Schizosaccharomyces pombe SMN complex. *Nucleic Acids Res* 49(13):7207-7223. PMID: 33754639; PMCID: PMC8287938; DOI: 10.1093/nar/gkab158. https://doi.org/10.1093/nar/gkab158
* **wang-2020-donkey-genomes**: Wang C, Li H, Guo Y, Huang J, Sun Y, Min J, et al. (2020). Donkey genomes provide new insights into domestication and selection for coat color. *Nat Commun* 11(1):6014. PMID: 33293529; PMCID: PMC7723042; DOI: 10.1038/s41467-020-19813-7. https://doi.org/10.1038/s41467-020-19813-7


## Citations

1. alphafold-A0A9L0ICL9-model.pdb
2. alphafold-A0A9L0ICL9-prediction.json
3. alphafold-A0A9L0ICL9-summary.md
4. baccon-2002-gemin7-abstract.md
5. baccon-2002-gemin7-summary.md
6. battle-2006-smn-assembly-machine-abstract.md
7. battle-2006-smn-assembly-machine-summary.md
8. battle-2007-smn-independent-subunits-abstract.md
9. battle-2007-smn-independent-subunits-summary.md
10. borg-2014-gemins-sma-abstract.md
11. borg-2014-gemins-sma-fulltext.txt
12. borg-2014-gemins-sma-summary.md
13. carissimi-2005-unrip-abstract.md
14. carissimi-2005-unrip-summary.md
15. carissimi-2006-gemin8-architecture-abstract.md
16. carissimi-2006-gemin8-architecture-summary.md
17. carissimi-2006-gemin8-novel-abstract.md
18. carissimi-2006-gemin8-novel-summary.md
19. cauchi-2014-gem-depletion-abstract.md
20. cauchi-2014-gem-depletion-fulltext.txt
21. cauchi-2014-gem-depletion-summary.md
22. chari-2008-assembly-chaperone-abstract.md
23. chari-2008-assembly-chaperone-summary.md
24. feng-2005-gemins-modulate-abstract.md
25. feng-2005-gemins-modulate-summary.md
26. grimm-2013-structural-basis-abstract.md
27. grimm-2013-structural-basis-summary.md
28. grimmler-2005-unrip-abstract.md
29. grimmler-2005-unrip-summary.md
30. hu-2023-pombe-snrnp-core-assembly-abstract.md
31. hu-2023-pombe-snrnp-core-assembly-fulltext.txt
32. hu-2023-pombe-snrnp-core-assembly-summary.md
33. hu-2026-icln-release-module-abstract.md
34. hu-2026-icln-release-module-fulltext.txt
35. hu-2026-icln-release-module-summary.md
36. kroiss-2008-minimal-smn-abstract.md
37. kroiss-2008-minimal-smn-fulltext.txt
38. kroiss-2008-minimal-smn-summary.md
39. lanfranco-2017-drosophila-smn-abstract.md
40. lanfranco-2017-drosophila-smn-summary.md
41. ma-2005-gemin6-gemin7-structure-abstract.md
42. ma-2005-gemin6-gemin7-structure-summary.md
43. ogawa-2009-smn-components-snrnp-abstract.md
44. ogawa-2009-smn-components-snrnp-fulltext.txt
45. ogawa-2009-smn-components-snrnp-summary.md
46. otter-2007-smn-interaction-map-abstract.md
47. otter-2007-smn-interaction-map-summary.md
48. pellizzoni-2002-gemin6-abstract.md
49. pellizzoni-2002-gemin6-summary.md
50. raimer-2017-smn-chaperone-abstract.md
51. raimer-2017-smn-chaperone-fulltext.txt
52. raimer-2017-smn-chaperone-summary.md
53. todd-2010-neurite-granules-abstract.md
54. todd-2010-neurite-granules-summary.md
55. todd-2010-smn-neurite-granules-cajal-abstract.md
56. todd-2010-smn-neurite-granules-cajal-summary.md
57. uniprot-A0A9L0ICL9-record.txt
58. uniprot-A0A9L0ICL9-summary.md
59. uniprot-A0A9L0ICL9.fasta
60. uniprot-Q9H840-human.fasta
61. uniprot-Q9H840-record.txt
62. uniprot-gemin7-orthologs-summary.md
63. uniprot-gemin7-orthologs.fasta
64. veepaschit-2021-pombe-smn-abstract.md
65. veepaschit-2021-pombe-smn-fulltext.txt
66. veepaschit-2021-pombe-smn-summary.md
67. wang-2020-donkey-genomes-abstract.md
68. wang-2020-donkey-genomes-fulltext.txt
69. wang-2020-donkey-genomes-summary.md