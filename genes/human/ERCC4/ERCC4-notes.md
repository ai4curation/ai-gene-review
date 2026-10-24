# ERCC4 (XPF) — gene review notes

UniProt: Q92889 (XPF_HUMAN); HGNC:3436; Gene: ERCC4 (syn. ERCC11, XPF, FANCQ). 916 aa.
EC=3.1.-.- (Mg2+ dependent hydrolase/endonuclease).

## Core biology (verified against cached publications)

XPF/ERCC4 is the **catalytic subunit** of the ERCC1-XPF structure-specific DNA
endonuclease. It houses the nuclease active site and makes the **5' incision** on the
damaged strand at ss/ds DNA junctions. ERCC1 is the non-catalytic partner that provides
additional DNA binding.

- UniProt FUNCTION: "Catalytic component of a structure-specific DNA repair endonuclease
  responsible for the 5-prime incision during DNA repair, and which is essential for
  nucleotide excision repair (NER) and interstrand cross-link (ICL) repair."
- Cofactor: Mg(2+) [PMID:10413517].
- Heterodimer with ERCC1; C-terminal (HhH)2 domain mediates dimerization; N-terminal
  nuclease/helicase-like region carries the catalytic domain.

### Endonuclease / catalytic subunit
- [PMID:8797827 "The XPF protein was purified from mammalian cells in a tight complex with ERCC1. This complex is a structure-specific endonuclease responsible for the 5' incision during repair."]
- [PMID:8797827 "...solve the catalytic function of the XPF-containing complex."]
- [PMID:10413517 "...determined that it is an endonuclease and can bind DNA in the absence of the ERCC1 subunit."]
- [PMID:10413517 "the N-terminal 378 amino acids of XPF are capable of binding and hydrolyzing DNA, while the C-terminal 214 residues are capable of binding specifically to ERCC1."]
- [PMID:10413517 "We propose that the N-terminal domain of XPF contributes to the junction-specific endonuclease activity observed during DNA repair and recombination events."]
- [PMID:22547097 "ERCC1-XPF is a heterodimeric, structure-specific endonuclease that cleaves single-stranded/double-stranded DNA junctions and has roles in nucleotide excision repair (NER), interstrand crosslink (ICL) repair, homologous recombination, and possibly other pathways."]
- [PMID:22547097 "In NER, ERCC1-XPF is recruited to DNA lesions by interaction with XPA and incises the DNA 5' to the lesion."]
- [PMID:16076955 "Human XPF-ERCC1 is a DNA endonuclease that incises a damaged DNA strand on the 5' side of a lesion during nucleotide excision repair and has additional role(s) in homologous recombination and DNA interstrand crosslink repair."]

### ssDNA binding / substrate recognition (ss/ds junction)
- [PMID:22483113 "Human XPF/ERCC1 is a structure-specific DNA endonuclease that nicks the damaged DNA strand at the 5' end during nucleotide excision repair."]
- [PMID:22483113 "A positively charged region within the second helix of the first HhH motif contacts the ssDNA phosphate backbone. One guanine base is flipped out of register..."]
- [PMID:16076955 "The central domain of ERCC1 binds ssDNA/dsDNA junctions with a defined polarity, preferring a 5' single-stranded overhang."] (ERCC1 side)
- ssDNA binding by XPF: [PMID:10413517] (binds DNA in absence of ERCC1).

### NER
- [PMID:8797827 "Nucleotide excision repair, which is defective in xeroderma pigmentosum (XP), involves incision of a DNA strand on each side of a lesion."]
- [PMID:22547097 "...mutations in the helix-hairpin-helix domain of ERCC1 and the nuclease domain of XPF abolished cleavage activity on model substrates."]
- [PMID:17055345 "...wild type XPF can complement XPF-deficient cells for repair of UV-induced DNA damage whereas the nuclease-inactive XPF proteins fail to do so, indicating that the nuclease activity of XPF is essential for nucleotide excision repair."]

### Interstrand crosslink (ICL) repair — 5' and 3' unhooking incisions
- [PMID:11790111 "XPF forms a heterodimeric complex with ERCC1 and is required for the repair of DNA interstrand cross-links. In association with ERCC1, it is involved in production of the 5' incision at the site of a psoralen interstrand cross-link as well as the 3' incision."]
- [PMID:14728600 "These results suggest that the XPF protein has important roles in the psoralen ICL-mediated DNA repair and mutagenesis."]
- [PMID:16678501 "These results indicate that XPF is required to form gamma-H2AX and likely double strand breaks in response to interstrand crosslinks in human cells."]
- [PMID:32034146 "The XPF-ERCC1 heterodimer is a structure-specific endonuclease that is essential for nucleotide excision repair (NER) and interstrand crosslink (ICL) repair in mammalian cells."]
- FANCA/spectrin recruitment to ICL foci: [PMID:12571280 "...FANCA and the known DNA repair protein XPF localize to the same nuclear foci."]

### Homologous recombination / single-strand annealing (SSA)
- [PMID:14734547 "The XPF/ERCC1 heterodimer is a DNA structure-specific endonuclease that participates in nucleotide excision repair and homology-dependent recombination reactions, including DNA single strand annealing and gene targeting."]
- [PMID:14734547 "Complex formation between hRad52 and XPF/ERCC1 concomitantly stimulates the DNA structure-specific endonuclease activity of XPF/ERCC1..."]
- Meiotic recombination (phylogenetic, yeast Rad1/Rad16/Mei-9): [PMID:10644440 "...support a distinct role for the XPF/ERCC1 junction-specific endonuclease during meiosis, most likely in the resolution of heteroduplex intermediates that arise during recombination."]

### SLX4 (FANCP) coordination
- [PMID:19596235 "Human SLX4 forms a multiprotein complex with the ERCC4(XPF)-ERCC1, MUS81-EME1, and SLX1 endonucleases..."]
- [PMID:24012755 "SLX4 assembles a telomere maintenance toolkit by bridging multiple endonucleases with telomeres."] and maps SLX4 interactions with SLX1, XPF, MUS81.
- Also PMID:19596236, PMID:19595721, PMID:19595722 (SLX4/BTBD12 binds XPF-ERCC1).

### Telomere functions (3' overhang removal; specialized/non-core)
- [PMID:14690602 "ERCC1/XPF-deficient cells retained the telomeric overhang after TRF2 inhibition, identifying this nucleotide excision repair endonuclease as the culprit in overhang removal."]
- [PMID:14690602 "...overhang processing is a prerequisite for NHEJ of telomeres."] and represses Telomeric DNA-containing Double Minute chromosomes (TDMs).
- [PMID:18812185 "overexpression of XPF induces telomere shortening... XPF-ERCC1 can function as a negative mediator of telomere length maintenance."]
- [PMID:18812185] shows two distinct mechanisms: TRF2 control (nuclease-dependent) vs telomere-length modulation (nuclease-independent). Establishes the NOT annotation for telomerase inhibitor activity — XPF does NOT act as a telomerase inhibitor.
- [PMID:17055345 "...both wild type XPF and nuclease-inactive XPF proteins... are able to rescue TRF2-mediated telomere shortening... reveal an unanticipated nuclease-independent function of XPF in TRF2-mediated telomere shortening."]

### Regulation / PTM
- Acetylation at Lys911 by KAT5/TIP60 promotes XPF-ERCC1 assembly by disrupting the
  Glu907-Lys911 salt bridge, exposing a second ERCC1 binding site; deacetylated by SIRT1
  [PMID:32034146].

## Disease (all reflect the same endonuclease deficiency)
- Xeroderma pigmentosum group F (XP-F, MIM:278760)
- XFE progeroid syndrome (XFEPS, MIM:610965) — R153P [PMID:17183314]
- XPF/Cockayne syndrome (XPF/CS) [PMID:23623389]
- Fanconi anemia complementation group Q (FANCQ, MIM:615272) — L230P, R689S, S786F
  [PMID:23623386, PMID:24027083]

## Curation decisions summary
- Core MF = structure-specific 5' incision endonuclease (ss/ds junction); catalytic subunit.
  Best specific MF ids: GO:0000014 (single-stranded DNA endodeoxyribonuclease activity),
  GO:1990599 (3' overhang ssDNA endonuclease activity, telomere).
- All GO:0005515 "protein binding" (and GO:0042802 identical protein binding) → MARK_AS_OVER_ANNOTATED
  (uninformative; functional partners ERCC1/SLX4/RAD52/TRF2/FANCA captured elsewhere).
- Telomere / recombination / meiotic / NHEJ processes → KEEP_AS_NON_CORE (genuine but specialized).
- Negated GO:0010521 telomerase inhibitor activity → ACCEPT the negation (informative NOT).
- No REMOVE and no UNDECIDED: all key claims verifiable in cached abstracts.
</content>
</invoke>


## 2026-10-24 augmentation: complete annotation checkpoint

All 97 retained contexts have reviewed actions: 96 current imported source contexts and one retired historical authored proposal. All original source key/value pairs, 52 inherited quotation paths and values, and both natural products are preserved. The two prior core objects are carried unchanged for separate review. The original notes above remain intact.

The current source extension adds two official mouse-orthology IEA contexts without rewriting the normal GOA/UniProt files. Database/phylogenetic, direct-original and interaction-screen evidence were assessed separately and reconciled. Generic supported binding is retained as non-core; damaged-DNA binding, TFIID-binding, source-specific HR and the negative telomerase-inhibitor claim retain explicit uncertainty. The TDM-formation annotation is over-annotated because the actual mouse loss-of-ERCC1 phenotype and proposed protective cleavage do not demonstrate a human formation step. Historical authored proposal91 is retired without erasing its source or quotations.

The standalone description now separates the regulatory helicase-like module from the nuclease domain and distinguishes pathway recruitment defects from intrinsic catalytic loss. Reference-review notes now state actual access and correct the earlier domain, direct-binding, telomerase and cleavage overstatements; the disease reference23623386 is explicitly limited to its actually read abstract, with no full-original claim. No new publication quotations were introduced. Later recovered14734547 Methods/Results replace only the earlier abstract-only access clauses in database rows0/5, with their actions unchanged.

See [the source guide](ERCC4-source-guide.md) for exact original links, assay/species/construct boundaries and unresolved source scope.


## 2026-10-24 — core synthesis and explicit row 5 successor

The accepted 97-context annotation checkpoint is retained unchanged in the review archive. Its successor changes only the review of source index 5 from ACCEPT to UNDECIDED and updates the two core entries. Current GO excludes SSA and its nonhomologous-end-removal step from the GO:0000724 ancestry; the earlier row 5 rationale incorrectly used that bridge. The IBD node, target descent, MSA and four experimental descendants are valid. Their exact template-based HR operative assays remain unverified here, so no PAINT node-placement defect or biological absence is asserted.

The two core units share GO:0106332 junction-specific duplex-DNA nuclease activity. They describe repair incision and SSA end processing by the same human ERCC1–XPF enzyme, with the human Reactome catalyst activeUnit and PMID:14734547 assay bounds documented in ERCC4-source-guide.md. The first unit contains nonredundant NER and ICL-repair terms; the second contains the specific SSA nonhomologous-end-removal step. No complete SSA reconstitution, free-ssDNA cleavage, universal ICL incision order or activity equivalence of the 372-aa natural product is asserted. The current action counts are 50 ACCEPT, 33 KEEP_AS_NON_CORE, 6 MODIFY, 7 UNDECIDED and 1 MARK_AS_OVER_ANNOTATED; one UNDECIDED authored proposal is retired, leaving six active unresolved assessments.

All 97 source objects, 55 references, two natural products and 52 inherited quotation paths/values are preserved, including all five quotations embedded in the two cores. Five reference-only core support entries were added; no new publication quotations or NEW annotation contexts were introduced. The earlier telomere quote is retained as historical source context, not as proof of SSA. Public source-guide links now resolve to actual public records; archived derivation filenames are not presented as public links. Original notes remain an unchanged prefix of this journal.


## 2026-10-24 — genuine GOA source-version refresh

Final validation exposed the preserved legacy GOA snapshot's omission of the two current IEA contexts already reviewed at indices 95 and 96. A genuine `just fetch-gene human ERCC4 --uniprot-id Q92889 --force` was run in a separate private workspace. Its untouched normal GOA output contains 100 rows representing 96 imported contexts, versus the legacy 98 rows representing 94 contexts. The complete independent current 100-record QuickGO response equals the earlier accepted official source snapshot; the 97-context review YAML remained byte-for-byte unchanged through the fetch. No new annotation decision was needed. The selected GOA is the genuine refreshed output, not a hand-edited validation fixture. Both source versions and the original failed validation receipt are preserved in the review archive.

The same acquisition refreshed UniProt metadata from entry version 234 to 235, but that unneeded metadata refresh was not selected. Delivery retains the exact legacy UniProt source, whose sequence and CC/FT fields are identical to the refreshed entry. All publication and Reactome cache dependencies are unchanged; shared sources use exact pinned-main bytes. No new publication quotation was introduced.


### Canonical validation — 2026-10-24

The selected review and genuine refreshed GOA were installed against main c55b5dbe40c23cf28a1c7fa37df927d0b803bcfb. Normal validation, strict whole-document term validation, component validation, computed-status checking and rendering all passed. DRAFT retains 29 advisories described above; no warnings were suppressed. All 197 description, annotation-review and core-function narratives occur in the rendered HTML. The generated HTML was retained privately for verification, and the previous tracked HTML was restored. Normal sources and unrelated working changes remained intact.


### Prepublication wording correction — 2026-10-24

Independent review identified an overly restrictive explanation for the unresolved PMID:11790111 damaged-DNA-binding context. Official GO:0003684 defines binding to damaged DNA without requiring preferential affinity over undamaged DNA or an isolated-protein preparation. The review and source guide now state the actual unresolved point: whether the inspected evidence establishes binding attributable to XPF separately from complex assembly and incision. The action remains UNDECIDED, with its inherited quotation, source fields, all action counts and both cores unchanged.


## 2026-10-24 — response to the published review

The specificity correction refines all five broad DNA-endonuclease rows to junction-specific duplex-DNA cleavage. All three broad DNA-repair rows use MODIFY, with the electronic context covering independently established NER, ICL repair and the SSA nonhomologous-end-removal step. The original-paper contexts preserve their narrower assay scopes. The SSA addition is a refinement of existing broad coverage, not a new annotation; the human catalytic participant chain, actual human junction incision, same-role ortholog comparators, current parents and the cached NER GO-CAM were checked. The two core contexts remain the same nuclease, with the first explicitly distinguishing broader ICL repair from the NER-in-ICL branch.

NEF1 and UV-response assessments now use the same whole-gene judgment across their sources while recording each experiment's limits. The positive TDM-formation assertion is removed after rereading the actual deficiency phenotype and protective-cleavage model. The retired historical broad ssDNA proposal is TOO_GENERAL rather than an unresolved active function. Three questions address damaged-DNA contacts, TFIID association and the natural short product.

All 97 source objects, two natural products and all 52 inherited quotation paths and values are unchanged. The SLX4-only quotation remains exactly as inherited and is explicitly identified as complex context; ERCC4-specific human knockdown evidence is cited without a new quotation, with the actual Figure 3E–F/Methods locator in the source guide. The refreshed 100-row GOA, 96 active imported contexts and immutable normal source caches are preserved.

Both standing user overrides are documented in the [ClinGen campaign curation instructions](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions): supported generic binding is NC unless a specific role warrants MODIFY, and no new publication quotations are added while inherited quotations remain exact. The 21 supported generic-binding rows are therefore retained; removing them solely for their uninformative label would violate the campaign instruction. This is an explicit task-specific departure from the default skill, not an unreported repository policy change.

The prior main review was COMPLETE; the published re-review changed it to DRAFT. This follow-up preserves DRAFT rather than describing the historical transition as unchanged. Current action totals are 45 ACCEPT, 32 KEEP_AS_NON_CORE, 12 MODIFY, six UNDECIDED, one REMOVE and one retired TOO_GENERAL. Final canonical validation and any resulting advisory counts are recorded separately by the publication step; this scientific packet does not claim that those checks have already run.

Canonical follow-up validation passed: normal, strict whole-document terms, components, computed status and rendering. DRAFT retains 22 advisories. All 197 description/review/core narratives occur in rendered HTML. All 48 selected normal-source dependencies remain exact.
