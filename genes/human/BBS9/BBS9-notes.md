# BBS9 (PTHB1; UniProt Q3SYG4) review notes

## Identity / overview
- Human gene BBS9 (HGNC:30000), aka PTHB1 (Parathyroid hormone-responsive B1 gene). 887 aa, MANE isoform Q3SYG4-1. Chromosome 7. [UniProt Q3SYG4]
- Causes autosomal-recessive Bardet–Biedl syndrome type 9 (BBS9; MIM:615986). The recurrent pathogenic missense G141R severely destabilizes the protein [UniProt; PMID:16380913; PMID:26085087].

## Core function: BBSome subunit / scaffold
- BBS9 is one of the seven/eight core BBSome subunits (BBS1, BBS2, BBS4, BBS5, BBS7, BBS8/TTC8, BBS9, BBIP10/BBIP1). The BBSome is a coat-like adaptor that sorts/traffics specific membrane (signaling-receptor) proteins to and within the primary cilium. [PMID:17574030 "we identify a complex composed of seven highly conserved BBS proteins. This complex, the BBSome, localizes to nonmembranous centriolar satellites in the cytoplasm but also to the membrane of the cilium ... the BBSome is required for ciliogenesis but is dispensable for centriolar satellite function"]
- BBSome assembly is chaperonin-assisted: BBS6/BBS10/BBS12 + CCT/TRiC mediate BBSome assembly; in Mkks(BBS6)-null mice BBS2/BBS7/BBS9 are unstable and degraded, leading to failure of BBSome assembly. [PMID:20080638; PMID:23943788 "in Mkks−/− mice, several BBSome components (e.g. Bbs2, Bbs7 and Bbs9) are unstable and degraded, leading to failure of BBSome assembly"]
- Structural basis: BBS9 N-terminal residues 1–407 form a seven-bladed β-propeller (PDB 4YD8, 1.80 Å). BBS9 also has GAE (gamma-adaptin ear), platform/pf, hairpin (hp) and C-terminal α-helical (CtH) domains. With BBS2 and BBS7 it forms the structural core/scaffold of the BBSome (cryo-EM 6XT9, full-length BBS9 modelled). [UniProt REGION 1..407 "Seven-bladed beta-propeller"; PMID:26085087 (structural characterization of BBS9; G141R abolishes stability; Ser142/Tyr186 mutagenesis)]
- Residue 141 is "critical for protein stability"; the BBS9 G141R disease variant causes severe loss of protein stability / aberrant folding. [UniProt SITE 141; PMID:26085087]

## Localization
- BBSome / BBS9 localizes both to nonmembranous centriolar satellites in the cytoplasm and to the ciliary membrane. [PMID:17574030]
- ComplexPortal/IDA places the BBSome at the ciliary membrane (GO:0060170). [PMID:19081074, ComplexPortal CPX-1908]
- IDA localizations (HPA / GO_Central immunofluorescence and PMID:23943788): cilium (GO:0005929), ciliary transition zone (GO:0035869), ciliary tip (GO:0097542), centriolar satellite (GO:0034451), cytosol (GO:0005829). [GO_REF:0000052; PMID:23943788]
- Pericentriolar material (GO:0000242) and cilium IDA from mouse Bbs imaging (MGI). [PMID:22139371]
- UniProt subcellular location: cytoplasm; cytoskeleton/MTOC/centrosome; centriolar satellite; cilium membrane.

## BBSome trafficking regulation / interactions
- BBS9 (and the BBSome) interacts with LZTFL1/BBS17; the BBS9 region 685–765 mediates LZTL1 interaction; LZTFL1 regulates BBSome ciliary trafficking and Smoothened/Hedgehog. [UniProt REGION 685..765; PMID:22072986]
- ARL6/BBS3 (small GTPase, not a BBSome subunit) physically interacts with the BBSome; both depend on each other for ciliary localization. BBSome forms normally without Bbs3, but Bbs3 loss mislocalizes ciliary GPCR cargo (MCHR1) and affects retrograde transport. [PMID:22139371]
- AZI1/CEP131 (centriolar satellite protein) interacts with BBS4 and regulates BBSome ciliary trafficking. [PMID:24550735]
- NPHP5(IQCB1)/CEP290 regulate BBSome integrity, ciliary trafficking and cargo delivery. [PMID:25552655]
- Rab8/RAB3IP(Rabin8): BBSome binds Rabin8 (GEF for Rab8), promoting ciliary membrane biogenesis. [PMID:17574030; Reactome R-HSA-5617815]

## Curation considerations
- 13 GO:0005515 "protein binding" IPI annotations are uninformative per guidelines; they record specific BBSome subunit / regulator interactions (BBS1, BBS2, BBS4, BBS5, BBS7/TTC8, BBS10, BBS12, LZTFL1, IQCB1, AZI1/CEP131). The informative content is captured by the BBSome part_of (GO:0034464) annotations. Mark protein binding as over-annotated/non-core (keep but not core MF).
- The only true MF annotation is ND (GO:0003674). BBS9 has no catalytic activity; it is a structural/scaffolding subunit. A "structural molecule activity" (GO:0005198) MF could be proposed but is not in existing annotations; the BBSome subunit identity (CC) plus protein localization to cilium (BP) capture the function.
- fat cell differentiation (GO:0045444) is ISS/IEA from mouse ortholog; plausible BBS-related (obesity) downstream phenotype but indirect / non-core for a structural ciliary subunit -> KEEP_AS_NON_CORE.
- cytoplasm (GO:0005737, IEA SubCell) and membrane (GO:0016020) are general/parent terms superseded by more specific IDA terms (centriolar satellite, ciliary membrane). Mark membrane (parent of ciliary membrane) as over-annotated; cytoplasm is acceptable but general.
- GO:0061512 protein localization to cilium (IMP, PMID:23943788) and GO:0060271 cilium assembly capture the BP. protein localization to cilium is the more precise/mechanistic core BP (BBSome traffics cargo INTO cilium); cilium assembly is the broader downstream phenotype.

## Core function summary
1. Structural scaffold subunit of the BBSome (β-propeller + GAE/platform/α-helical core, with BBS2/BBS7). [PMID:17574030; PMID:26085087]
2. BBSome-mediated trafficking of membrane/signaling cargo to and within the primary cilium = protein localization to cilium. [PMID:17574030; PMID:23943788]
3. Required for ciliogenesis/cilium assembly (downstream). [PMID:17574030]


## 2026-09-30 independent BBS9 annotation consultation (prospective)

The normal TMP source projection recovers 21 omitted source objects and 25 supporting-entity lists. All 69 raw records are distinct and match the 69 reviewed source objects. Seven alternative products remain unchanged. The old authored structural-molecule NEW is considered separately and proposed for withdrawal because a specific scaffold replacement is available on the existing ND source.

Selected primary assembly experiments (PMID:22500027 and PMID:22072986) support BBS9 as an integral BBSome scaffold, not merely a protein with a beta-propeller domain. The source ND root and exact canonical BBS1/BBS2/BBS5/TTC8 partner annotations can be refined using that independent evidence. Original screening sources and their limitations remain explicit. The distinct TTC8 accession A0A0C4DGX9 is identified but its construct has not been matched to the mechanistic experiments, so it remains non-core. Other supported generic interactions also remain non-core under the supplied ActionEnum, rather than being rejected solely for informativeness.

The earlier assertion that a molecular function must be catalytic is superseded. The old generic structural-molecule proposal is redundant with the more specific scaffold refinement, and an isolated crystallographic fold does not alone prove the assembly role. The 2015 BBS9 N-terminal structure and the later low-resolution BBS2/7/9 integrative model have distinct scopes.

Ciliary locations and assembly are retained with cell-context and species bounds. The additional primary PMID:22479622 reports mouse IMCD3 and zebrafish knockdown, with human-mRNA rescue in zebrafish; it does not show universal human-cell dependence. Mouse adipogenesis transfers remain unresolved because the traced evidence is an expression timecourse (PMID:17379567), not a verified differentiation perturbation assay.

The normal PMID:23943788 extraction lacks Results/Methods even though its metadata says full text is available. Selected original Results were read separately: BBS9 localizes to cilia, transition zones and satellites; BBS9 knockdown perturbs the satellite pool of CEP290 while transition-zone localization remains. Neither a complete-paper read nor loss of CEP290 transition-zone localization is claimed. HPA localization text and cell-line tables were read without reanalyzing image pixels. No source/cache file or canonical gene file was changed, no provider report was fabricated, and no new quotations were added.

Source91 subsequently completed the normal PMID:22479622 import. Its relevant available primary evidence was reassessed before this integrated proposal; cache and external reading limits are recorded separately. The source-complete decisions are 22 ACCEPT, 24 KEEP_AS_NON_CORE, 21 MODIFY and two UNDECIDED, with one BBSome scaffold core. The old authored generic structural-molecule NEW is withdrawn without removing any source object. All 69 distinct raw sources and seven alternative products remain preserved. All MODIFY decisions have structured source/primary references; no new direct quotation is added.

The subsequently imported normal PMID:22479622 XML cache was read for its abstract, Results, main Discussion and available Methods. Mouse IMCD3 shRNA and zebrafish Kupffer-vesicle experiments support the existing cilium-assembly decisions in those contexts; the Discussion contrasts an earlier weaker RPE-cell phenotype. Wild-type human mRNA rescue was measured in zebrafish eye development, not a direct human-cell ciliogenesis assay. Heart looping and laterality markers were explicitly not tested. Main captions were read as text, while figure pixels and supplemental files were not inspected. The three cilium-assembly reasons now record these limits; all decisions and the scaffold core remain unchanged.

## 2026-09-30 validation and application

The independently reviewed proposal was applied with all 69 source objects and seven alternative products preserved. Focused validation passed with 14 generic protein-binding advisories, and the review rendered successfully. These evidence-supported interactions remain non-core under the supplied ActionEnum: REMOVE denotes an unlikely-correct assertion, whereas KEEP_AS_NON_CORE retains supported context. More specific scaffold activity is already assigned where independent primary evidence supports the exact partner scope. No direct quotations, source-cache changes or provider-report changes were introduced in this application.

## 2026-09-30 first-review source-specific follow-up (prospective)

The six screening-derived scaffold refinements at zero-based rows 15, 18, 19, 59, 61 and 67 are superseded by KEEP_AS_NON_CORE. These retain curator-attributed BBS9 associations with BBS1, BBS2 or BBS5 and their exact partner accessions. PMID:27173435 uses ciliary affinity proteomics, PMID:33961781 comparative AP-MS networks, and PMID:40205054 multimodal U2OS mapping. Their broad assay designs permit co-complex recovery; the exact BBS9 supplementary records were not reanalyzed. Independent mechanistic work establishes BBS9 scaffold activity, but does not make each screening record a binary-contact or organizing-function assay. Targeted structural/assembly refinements elsewhere are unchanged.

The single scaffold core now explicitly carries the existing ciliary process and location terms. PMID:22500027 provides targeted subunit-contact and assembly evidence, and PMID:22072986 shows human-cell BBSome disintegration and impaired ciliary entry after BBS9 depletion. PMID:17574030 supports complex-level ciliary-membrane localization. The selected original Results of PMID:23943788 describe BBS9 in human hTERT-RPE1 cilia, transition zones and satellites; its normal extraction lacks Results/Methods, so that gene-specific observation is explicitly an external-primary read. The cached anchor is complex-level context. CEP290 satellite mislocalization is not described as abolished transition-zone localization. PMID:22479622 supplies mouse IMCD3 and zebrafish ciliogenesis evidence; no universal human-cell requirement or autonomous cargo-recognition mechanism is asserted. The three existing cilium-assembly reasons already distinguish the earlier weaker RPE experiment from the paper's own IMCD3 assay and remain unchanged after independent consultation.

PMID:26085087 is reconnected through a bounded finding about the isolated human N-terminal beta-propeller. Its abstract does not by itself prove scaffold function or a physiological full-length homodimer. GO_REF:0000015 remains the original ND source at row45, but is removed from biological supporting evidence for its literature-based replacement. All 69 machine-source objects, seven products, raw sources, source IDs and reference titles remain intact; no NEW row is added. The prospective action counts are 22 ACCEPT, 30 KEEP_AS_NON_CORE, 15 MODIFY and two UNDECIDED.

The supplied ActionEnum still governs supported generic interactions; the reviewer's blanket REMOVE request remains a documented policy disagreement rather than evidence that those associations are false. Short source-specific anchors occur once in the proposed YAML and are not repeated here. Historical journal quotations and earlier judgments remain as provenance, with the supersessions above explicit. This TMP proposal makes no canonical, history, validation, rendering or publication claim.

## 2026-09-30: TTC8 interface and reference-assessment clarification

This entry supersedes the earlier non-core treatment of the PMID:29039417 TTC8 interaction and the former use of UNVERIFIED to mean an uninspected supplementary pair. The source accession A0A0C4DGX9 is retained exactly. HPA maps it to a 531-amino-acid TTC8 transcript; it has not been equated with Q8TAM2 or with every TTC8 isoform. The original interaction paper specifically identifies the BBS8 region required for BBS9 binding. Together with BBS9-dependent assembly evidence, this supports refining that existing association to protein complex scaffold activity [PMID:29039417; PMID:22500027]. This is not a new annotation or a claim that the yeast assay alone proves endogenous assembly.

Three existing reasons now correctly identify PMID:22500027 as their own mechanistic source rather than independent corroboration. The BBS4 interaction reason now describes the original binary interaction-perturbation evidence and its mapped BBS9 region, instead of calling it co-complex recovery. Its organizing contribution remains unresolved in the selected assembly evidence, so its non-core action is retained [PMID:29039417].

Six affinity-proteomics reasons retain their assay-specific and supplementary-record limits while dropping repeated policy commentary. The supplied ActionEnum continues to govern supported non-core interactions. The earlier ciliary-role and six screening-row corrections remain unchanged. No new quote is added, and the 69 original source objects, seven products and single core are preserved.

Eight reference assessments now distinguish verified official identity and appropriate study context from uninspected pair-level data. For PMID:25552655, newly read external Results, the Figure 2 caption and Table 1 support tagged HEK293 association and RPE-1 proximity between BBS9 and NPHP5; the normal cache remains abstract-only. For PMID:29039417, the additional reading comprises original publisher figure headings/supplementary captions and selected author-repository Methods, not the full paper, images or complete mutation matrix. Its BBS8/BBS5 mutagenesis was tested in one direction because a full-length BBS9 mutant library could not be generated. Full-paper and supplement access is not inferred from citation verification.

## 2026-10-09: binding-policy authority and final formatting follow-up

The requested scaffold anchor is now quoted once in the existing core citation to PMID:22500027. It is a nine-word verbatim clause from the Results, checked against the cached article, and is not repeated in these notes. Its context distinguishes the direct BBS9 contact list from the downstream assembly experiments; no additional paper, figure or supplemental-data reading is claimed.

Trailing whitespace was removed from 405 YAML lines. Parsing before and after that mechanical cleanup produces identical data, including the escaped newline in the structural finding. The only subsequent YAML content change in that follow-up is the bounded supporting quotation and its Results section label. No original quotation changed.

## 2026-10-09 generic binding cleanup

The 19 GO:0005515 rows that still retained source-attributed interactions as KEEP_AS_NON_CORE after the scaffold-specific follow-up are now marked REMOVE. This supersedes the 2026-09-30 policy-disagreement note: the exact BBSome, BBS-chaperonin and trafficking-regulator interactions remain recorded in the affected row summaries, reasons and supporting_entities, but the bare protein-binding molecular-function term is not retained. The 15 partner rows already refined to GO:0140378 protein complex scaffold activity were left as MODIFY because targeted assembly/interface evidence supports that more informative replacement.
