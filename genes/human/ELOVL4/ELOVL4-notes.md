# ELOVL4 (human, UniProt Q9GZR5) — review notes

## Summary of function

ELOVL4 (Elongation of Very Long chain Fatty acids protein 4; "3-keto acyl-CoA
synthase ELOVL4"; EC 2.3.1.199) is a multipass endoplasmic-reticulum membrane
enzyme of the ELO family (ELOVL4 subfamily). It catalyzes the first and
rate-limiting condensation step of the four-reaction microsomal fatty-acid
elongation cycle, condensing an acyl-CoA with malonyl-CoA to give a 3-oxoacyl-CoA
(+ CO2 + CoA); the remaining three steps of each cycle are carried out by
HSD17B12/KAR, HACD1/2, and TECR.

- UniProt FUNCTION: "Catalyzes the first and rate-limiting reaction of the four
  reactions that constitute the long-chain fatty acids elongation cycle. This
  endoplasmic reticulum-bound enzymatic process allows the addition of 2 carbons
  to the chain of long- and very long-chain fatty acids (VLCFAs) per cycle.
  Condensing enzyme that catalyzes the synthesis of very long chain saturated
  (VLC-SFA) and polyunsaturated (PUFA) fatty acids ... May play a critical role in
  early brain and skin development."
  [file:human/ELOVL4/ELOVL4-uniprot.txt CC FUNCTION; ECO:0000269|PubMed:20937905, PubMed:23479632]
- Reaction (Rhea:RHEA:32727): "a very-long-chain acyl-CoA + malonyl-CoA + H(+) =
  a very-long-chain 3-oxoacyl-CoA + CO2 + CoA"; EC=2.3.1.199.
  [file:human/ELOVL4/ELOVL4-uniprot.txt CATALYTIC ACTIVITY]

The distinguishing feature of ELOVL4 among the seven mammalian elongases
(ELOVL1-7) is that it uniquely produces **ultra-long-chain fatty acids** (>=C26,
up to ~C38):
- Saturated and monounsaturated ULCFAs (C28-C38) required for epidermal
  omega-O-acylceramides and the skin permeability barrier, and for meibomian
  gland lipids.
- Ultra-long-chain polyunsaturated fatty acids (VLC-PUFA, e.g. C28-C38) enriched
  in retinal photoreceptor phosphatidylcholines, and present in brain and sperm.

## Substrate range (UniProt CATALYTIC ACTIVITY entries)

The UniProt record lists many elongation reactions on progressively longer acyl-CoA
substrates. Human-experimental / physiological-direction evidence
(ECO:0000269 or ECO:0000305 | PubMed:20937905, PubMed:23479632) covers e.g.
tetracosanoyl-CoA (C24)->3-oxohexacosanoyl-CoA (C26) [RHEA:36515] and
hexacosanoyl-CoA (C26)->C28 [RHEA:36519]; longer saturated and the VLC-PUFA
reactions (C28+ and the polyunsaturated series) are by similarity to mouse
Q9EQC4 (ECO:0000250) or ECO:0000305|PubMed:23479632.
[file:human/ELOVL4/ELOVL4-uniprot.txt CATALYTIC ACTIVITY lines]

## Localization

- UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ... Multi-pass
  membrane protein." Seven TRANSMEM helices (42-62, 78-98, 127-147, 165-185,
  188-208, 217-237, 247-267). C-terminal di-lysine motif (310-314) confers ER
  localization.
  [file:human/ELOVL4/ELOVL4-uniprot.txt SUBCELLULAR LOCATION / DOMAIN / FT]
- ER membrane localization is experimentally supported: Grayson & Molday 2005
  (PMID:16036915) show WT ELOVL4 with an ER-retention sequence localizes to the
  ER; Ohno et al. 2010 (PMID:20937905) is the source for the EXP/IDA ER and
  ER-membrane annotations in GOA.

## Oligomerization / interactions

- UniProt SUBUNIT: "Oligomer." [ECO:0000269|PubMed:16036915]. Grayson & Molday
  (PMID:16036915) show WT and mutant ELOVL4 co-purify / form a complex; the
  dominant-negative disease mechanism (STGD3, SCA34) is co-aggregation of WT with
  C-terminally truncated mutant that mislocalizes the WT protein to
  aggresome-like inclusions.
- ELOVL4 physically interacts with TECR (trans-2-enoyl-CoA reductase, Q9NZ01;
  IntAct NbExp=5), consistent with the elongation machinery being an
  ER-membrane complex of ELOVL + KAR + HACD + TECR
  [PMID:38422897 abstract, "the VLCFAs elongation machinery is located in ER
  membrane and consists of four components, FA elongase (ELOVL), 3-ketoacyl-CoA
  reductase (KAR), 3-hydroxyacyl-CoA dehydratase (HACD), and trans-2-enoyl-CoA
  reductase (TECR)"].
- The large set of GO:0005515 "protein binding" IPI annotations (PMID:32296183)
  come from the HuRI human binary-interactome map (systematic Y2H); ELOVL4 is a
  polytopic ER membrane protein and many of the reported partners are other
  small ER/membrane proteins, so most are best treated as non-informative
  large-scale interactions rather than functional partners.
  [PMID:32296183 abstract, "a human 'all-by-all' reference interactome map of
  human binary protein interactions, or 'HuRI'"]

## Disease

- STGD3 (Stargardt disease 3, MIM 600110): autosomal dominant macular dystrophy;
  caused by C-terminal truncating mutations (e.g. the 5-bp deletion of
  Zhang et al. 2001, PMID:11138005) acting by a dominant-negative mechanism
  (PMID:16036915). [file:human/ELOVL4/ELOVL4-uniprot.txt DISEASE STGD3]
- SCA34 (spinocerebellar ataxia 34, MIM 133190): autosomal dominant; cerebellar
  ataxia with erythrokeratodermia variabilis; variant L168F (PMID:24566826).
  [file:human/ELOVL4/ELOVL4-uniprot.txt DISEASE SCA34]
- ISQMR (ichthyosis, spastic quadriplegia, impaired intellectual development,
  MIM 614457): autosomal recessive (biallelic loss); PMID:22100072.
  [file:human/ELOVL4/ELOVL4-uniprot.txt DISEASE ISQMR]

Note: STGD3 and SCA34 arise from *dominant-negative* truncations, whereas
recessive loss-of-function causes the systemic ichthyosis/neurological phenotype
(ISQMR); this is consistent with the ER-membrane elongase being the core
function and the ULCFA products (skin barrier omega-O-acylceramides, retinal /
neural VLC-PUFA) being physiologically essential.

## Curation reasoning highlights

- **Core MF**: GO:0009922 "fatty acid elongase activity" — the correct specific MF
  (there is no finer chain-length-specific elongase MF term in GO). Supported by
  human EXP annotation (PMID:20937905).
- **Core BP**: very-long-chain fatty acid biosynthetic process (GO:0042761;
  human IDA, PMID:20937905), and the general fatty-acid elongation process
  (GO:0030497). The saturated/monounsaturated/polyunsaturated sub-process terms
  (GO:0019367, GO:0034625, GO:0034626) are all real but represent the same
  underlying condensation activity split by product class; kept as non-core /
  accepted as appropriate.
- **Location**: ER membrane (GO:0005789), experimentally supported.
- Ensembl rat-ortholog electronic annotations (circadian rhythm GO:0007623;
  synaptic-potential terms GO:0061886, GO:0097151, GO:1990926) and the
  inter-ontology "detection of visible light" (GO:0009584, inferred from a
  G-protein-coupled-photoreceptor MF that is itself a wrong NAS annotation) are
  over-annotations / wrong-branch for a metabolic elongase and are removed
  (all IEA) or marked over-annotated.
- The NAS annotation to GO:0008020 "G protein-coupled photoreceptor activity"
  (PMID:11138005) is incorrect: that 2001 paper identified ELOVL4 as a
  retina-specific gene homologous to yeast VLCFA-biosynthesis proteins, and did
  NOT show GPCR/photoreceptor activity — the paper's own conclusion is about
  fatty-acid biosynthesis ("the first to implicate the biosynthesis of fatty
  acids in the pathogenesis of inherited macular degeneration"). ELOVL4 is an
  ER-membrane acyltransferase, not a GPCR. This is a legacy mis-annotation and
  is removed (NAS, not experimental).
  [file:human/ELOVL4/ELOVL4-uniprot.txt CC FUNCTION; PMID:11138005 abstract]

## Key references

- PMID:11138005 Zhang et al. 2001, Nat Genet — ELOVL4 identified; STGD3/adMD
  5-bp deletion. (abstract only)
- PMID:16036915 Grayson & Molday 2005, JBC — dominant-negative mechanism; ER
  localization; oligomerization; N-glycosylation at Asn-20. (abstract only)
- PMID:20937905 Ohno et al. 2010, PNAS — in vitro substrate specificities of all
  ELOVL1-7; source of ELOVL4 EXP/IDA MF, BP, and ER annotations. (abstract only;
  full text assays all seven elongases including ELOVL4)
- PMID:23479632 Barabas et al. 2013, PNAS — ELOVL4 and VLC-PUFA in mouse STGD3
  models; source of several catalytic-activity ECO:0000305 entries. (not cached)
- PMID:22100072 Aldahmesh et al. 2011, AJHG — recessive ELOVL4 -> ISQMR. (not cached)
- PMID:24566826 Cadieux-Dion et al. 2014 — SCA34. (not cached)
- PMID:32296183 Luck et al. 2020, Nature — HuRI binary interactome (large-scale
  PPI). (full text available)
- PMID:38422897 Zhou et al. 2024, BBRC — HACD1/2-TECR complex; ELOVL/HACD
  structural similarity; VLCFA elongation machinery composition. (abstract only)
</content>
</invoke>


## 2026-10-21 source-specific reassessment

The entries above are preserved as the historical journal. This reassessment supersedes their blanket rejection of rat physiology and generic interactions, their unqualified MUFA/oligomer claims, their attribution of a shared truncation mechanism to STGD3 and SCA34, and their earlier access/cache status. The current source guide and reviewed YAML state the effective conclusions.

# ELOVL4 evidence notes

The reviewed activity is the ER-membrane condensing step of fatty-acid elongation. Human membrane assays support saturated C24:0/C26:0 elongation-associated output; mouse conditional-loss experiments establish a contribution to retinal polyunsaturated lipid products. These are complementary experiments and do not constitute a purified human substrate-spectrum measurement. Neither other elongation-cycle reactions nor partner functions are transferred to ELOVL4.

The 37 inherited source dictionaries remain exact and collectively cover all 128 current raw and normal contexts. A normal reseeding operation would backfill support fields and create partner-specific rows, but these mechanical output differences were archived rather than silently replacing the inherited boundary. Current support-set changes on rows 8 and 11 and all 92 HuRI partners remain visible in the portable proof. No lifecycle retirement or NEW annotation is proposed.

The final source decisions are 19 ACCEPT, 7 MODIFY, 5 KEEP_AS_NON_CORE, 4 UNDECIDED and 2 REMOVE. The two removals concern the unsupported photoreceptor GPCR/light-detection premise, not a denial of retinal function; source-defect CHECK queries preserve the actual resource, original source and unknown cause. Generic HuRI and CERS2 interactions remain non-core positive evidence. The TECR source remains unresolved because its operative ELOVL4-specific evidence was not recovered.

Three rat-derived physiological annotations require a distinction between observation and the product's normal function. Rhythmic Elovl4 transcript expression does not alone establish participation in the timed process. W246G is a selective disease allele, not a clean null; its opposing excitatory and inhibitory synaptic changes do not fix the normal human protein's signed regulatory effect. Short-term synaptic plasticity remains a supported contextual role. The precise rat assay and access limits are in the source guide.

The 314-aa official natural product is retained. The older disease description conflated C-terminal truncating STGD3 variants with SCA34; their experimental mechanisms are kept distinct. Tagged recombinant constructs, truncations and detergent-associated complexes do not establish additional natural products, a fixed oligomeric stoichiometry or functional equivalence to the current reference insert.

All 32 inherited quotation occurrences are retained exactly. The seven reference-level occurrences remain in place; the three inherited core support objects map explicitly into the independently synthesized integrated core. No new publication quotation is authored. Historical narrow UniProt fragments are preserved as inherited excerpts, with the documented record-format/whitespace normalization audit; they are not expanded into invented text.

Normal caches are immutable. The four-source bibliography gate reuses PMID 20166112 exactly and adds genuine normal caches for 24736612, 32780351 and 37491316. The last remains abstract-only in the normal cache even though genuine PMC main text was separately read. PMID 20166112's body was not read: its use is limited to the verified ELOVL1 donor-record provenance. Genuine provider failures are documented in the private bootstrap; no provider report was fabricated. Article bodies and credential-bearing provider logs are excluded from the public reproducibility package.

The reproducibility directory exposes its code and results directly. Its archive contains only fixed inputs, including database records and source reconciliation data. The offline code checks the complete target path, exact sequence, interaction joins, rule premises and typed term relations; it does not pretend to reproduce biological judgment or unavailable experiments.


## Cache-state access flags

The optional `full_text_unavailable` flags follow the normal-cache convention for PMIDs 11138005, 16036915, 20937905, 37491316 and 38422897. The first four have separately recovered original material with the precise read scopes recorded above; their flags do not negate that access. Only 38422897 still lacks operative ELOVL4-specific evidence. No normal publication cache was edited to reconcile these distinct states.


## ELOVL4 follow-up evidence clarification

The 37 decisions remain 19 ACCEPT, 7 MODIFY, 5 KEEP_AS_NON_CORE, 4 UNDECIDED and 2 REMOVE. Supported HuRI and CERS2 associations remain non-core under the campaign binding policy; neither an unsupported specific function nor a false interaction is inferred from the generic term. The two generic-binding validator advisories are disclosed.

The circadian UNDECIDED decision records scientific uncertainty despite complete original access: rhythmic rat transcript abundance is positive evidence, but the normal protein's contribution to a recurring process and its transfer to human remain unresolved. The W246G sign question records the apparent tension between the two signed terms and the measured miniature-current changes; this selective missense allele is not treated as a null, and no source defect or reversed annotation is asserted.

The seven IBA reviews now link directly, without quotations, to the visible PAINT results. The single condensation core uses the already accepted saturated and polyunsaturated elongation branches in place of their broad elongation ancestor, alongside the nonredundant very-long-chain biosynthesis term. The chemistry, ER membrane location and all core supports remain unchanged.

All 32 inherited quotation values and their published paths remain exact. The family-level lead excerpt is retained as context, not relabeled as an ELOVL4-specific experimental result; the source-scoped human membrane and mouse conditional-loss evidence is identified in the source guide and reference-only supports. The normal caches remain exact. Original text recovered outside the caches is still external to the repository; Figure 1 pixels were inspected for PMID 20937905, whereas its S2/S8 observations are main-text reports with inaccessible supplementary panels. Formatting of the three visible Python modules changes no algorithm, inputs or output hashes; the input-only archive is unchanged.
