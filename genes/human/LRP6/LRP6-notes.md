# LRP6 reference-review notes

## Scope and source inventory

This reference pass reviewed all 81 sources seeded from the LRP6 GO annotations (8 GO_REF records, 60 PubMed records, and 13 Reactome records) and added only four primary papers highlighted by the reviewed UniProt record as decisive for the receptor mechanism: PMID:15778503, PMID:16341017, PMID:16513652, and PMID:17400545. The final reference inventory therefore contains 85 records. Every record has an exact cached title and a manual `reference_review`; primary findings were included only when an exact, locally cached passage could be quoted verbatim.

The identity boundary is human LRP6, UniProt O75581, a reviewed 1,613-residue type-I membrane receptor. UniProt has no `ALTERNATIVE PRODUCTS` or `VAR_SEQ` section for this entry. NCBI Gene 4040 currently catalogs reviewed RefSeq transcript/protein models a-j, but O75581 maps only to RefSeq isoform b [UniProtKB:O75581; NCBI Gene:4040]. Thus, non-b RefSeq products are transcript/protein models rather than UniProt isoforms, and none of the reviewed references justifies isoform-specific GO function for LRP6. PMID:30824926 concerns GSK3A isoforms in sperm and must not be converted into an LRP6 isoform claim.

## Core receptor mechanism

LRP6 is a single-pass Wnt coreceptor that cooperates with Frizzled; it is not an autonomous ligand-activated receptor and has no intrinsic protein-kinase or other enzyme activity. Early functional work placed LRP6 between the Wnt/Frizzled receptor complex and cytosolic pathway components and showed Wnt binding to its extracellular region [PMID:11029007]. Wnt-induced signalosome formation and Dishevelled-dependent LRP6 phosphorylation are directly supported [PMID:17569865]. AXIN/GSK3 recruitment to the phosphorylated cytoplasmic tail and PPPSP-motif phosphorylation constitute the central signal-transduction step [PMID:16341017; PMID:19107203]. The phosphorylated tail can directly attenuate GSK3 activity [PMID:16365045; PMID:19107203], but that does not make LRP6 a kinase or catalytic enzyme.

The receptor is regulated by context-dependent phosphorylation. GSK3 and CK1 family kinases provide activating phosphorylation in the reported systems [PMID:16341017], whereas CK1epsilon phosphorylation at a distinct site was reported to negatively regulate LRP6 [PMID:16513652]. Cell-cycle-dependent priming peaks at G2/M in the cited experimental systems [PMID:20059949]. These findings describe regulation of the receptor tail; they do not establish a constitutive or autonomous receptor activity.

## Ligands, antagonists, and complexes

The DKK literature directly supports high-affinity binding to LRP6 and inhibition of Wnt-induced Frizzled-LRP6 complex formation [PMID:11357136; PMID:11433302; PMID:11448771]. Sclerostin binding and antagonism are directly supported for LRP5/6 [PMID:15778503; PMID:15908424]. The LRP4-centered sclerostin paper PMID:21471202, however, does not establish an LRP6 interaction and is miscited for the seeded LRP6 IPI.

RSPO1 was historically reported to bind LRP6 and induce receptor phosphorylation [PMID:17400545], and a mouse R-spondin study reported association with FZD8/LRP6 [PMID:16543246]. These older assay-specific findings should be stated as reported interactions rather than generalized into a direct binary mechanism for every R-spondin context. WNT7A signaling through an FZD5-LRP6 complex was tested in PC12 cells [PMID:12857724], so it is not human in-vivo evidence.

## Trafficking and receptor abundance

LRP6 surface abundance and signaling depend on folding, trafficking, endocytosis, and turnover. MESD binds LRP6 and modulates ligand interaction [PMID:16263759; PMID:16989816]. GRP94 supports LRP6 maturation in the reported gut-homeostasis system [PMID:23572575]. MEST inhibits LRP6 glycosylation, maturation, and plasma-membrane localization [PMID:21375506], but the cached abstract does not verify a direct MEST-LRP6 binary interaction. Caveolin-dependent internalization follows WNT3A stimulation [PMID:16890161], whereas DAB2 promotes clathrin-mediated internalization [PMID:22491013]. ZNRF3/RNF43 regulate Wnt-receptor turnover [PMID:22575959]; high-level pathway effects must not be rewritten as a direct catalytic action by LRP6.

## Structural boundaries

No cited structure is a full-length membrane-embedded LRP6 structure. PMID:21984209 reports isolated human LRP6 E1E2 and E3E4 extracellular fragments and an E3E4-DKK1 complex. PMID:23791946 combines a WntD N-terminal-fragment structure with biochemical mapping of a Wnt3a linker site to purified LRP6 extracellular fragments. PMID:27524201 uses purified LRP6 extracellular propeller fragments in DKK1-Kremen1 ternary-complex work. Structural interpretations must therefore remain at the fragment/domain level.

## Species, paralog, and interaction-method boundaries

Many mechanistic papers use Xenopus embryos, mouse proteins or tissues, zebrafish, PC12 cells, NIH3T3 cells, or heterologous expression. Their results can inform conserved LRP6 biology but do not by themselves establish a human in-vivo process. The Reactome `R-NUL` records are explicitly non-human or mixed-species experimental events: R-NUL-1458871 uses soluble mouse Fzd8 and human LRP6 ectodomain constructs, while R-NUL-1458902 and R-NUL-209104 involve frog CK1gamma. None independently establishes native plasma-membrane localization of full-length human LRP6.

LRP6 must remain distinct from LRP5, LRP4, and LRP5L. PMID:18721193 is an LRP5 genetic-association paper and provides no LRP6 interaction evidence in the accessible record. PMID:21471202 directly concerns LRP4-sclerostin binding. PMID:14739301 centers LRP1 and uses LRP6-HFz1 only as a comparison. Family-level LRP5/6 findings are acceptable only when described at that family level; they do not establish an LRP6-specific result unless LRP6 was tested.

Interaction evidence was graded by method. PMID:28514442 and PMID:33961781 are affinity-purification/mass-spectrometry maps, so their edges represent co-complex association rather than direct binary binding. PMID:32296183 is a high-throughput yeast-two-hybrid binary map, which does not by itself demonstrate physiological complex formation in native tissue. PMID:40205054 is a multimodal screening resource. These sources are useful as contextual interaction evidence but not as stand-alone core-mechanism proof.

## Disease, toxin, and variant boundaries

Disease associations do not automatically define the normal molecular mechanism. PMID:21245321 reports altered PDGFRbeta-dependent vascular smooth-muscle proliferation for an atherosclerosis-linked LRP6 R611C variant, but that variant phenotype should not be generalized to all LRP6 function. PMID:34896607 has an exact cached identifier/title for familial exudative vitreoretinopathy, but the local cache contains neither abstract nor full text; its disease and variant mechanisms therefore remain unverified here.

Anthrax-toxin evidence is context-dependent. PMID:16564009 reports an LRP6 requirement in its tested mammalian uptake system, whereas PMID:18350154 directly reports that efficient LRP6/LRP5 knockdown did not affect toxin entry in human HeLa cells. The latter supports the explicit NOT annotation in that human cell context and does not erase the former result in a different system.

## Citation audit outcomes

Seven sources were marked `MISCITED` for the seeded assertion they accompany:

- PMID:18721193: LRP5 genetics, not an LRP6 interaction.
- PMID:21471202: LRP4-sclerostin binding, not LRP6 binding.
- Reactome:R-HSA-4641236: USP8/FZD recycling event with no LRP6 in the cached event text.
- Reactome:R-HSA-5340587: RNF43-mutant/FZD event with no LRP6 in the cached event text.
- Reactome:R-NUL-1458871: soluble receptor-fragment association, not native full-length extracellular localization.
- Reactome:R-NUL-1458902: frog CK1gamma phosphorylation, not human LRP6 plasma-membrane localization.
- Reactome:R-NUL-209104: mixed-species phosphorylation event, not independent localization evidence.

Three sources were marked `UNVERIFIED` rather than overruled:

- PMID:20093472: the abstract supports prorenin-receptor/V-ATPase participation in Wnt signaling but not the exact seeded LRP6 interaction/localization tuple.
- PMID:21375506: the abstract supports MEST-dependent effects on LRP6 maturation and localization but not a direct binary IPI.
- PMID:34896607: identifier/title cached, but no abstract or full text is locally available.

GO_REF records were reviewed as annotation-method provenance, not as independent evidence for LRP6 biology. Reactome records were bounded to their cached event participants, species, and wording. No review conclusion relies on title-only inference when the relevant experimental detail is absent.
