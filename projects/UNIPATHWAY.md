# UniPathway Unique Terms Project

## Overview

This project reviews GO annotations derived from **UniPathway vocabulary mapping**
(`GO_REF:0000041`) where UniPathway provides the only non-redundant support for a
gene-term pair. It follows the same principle used for the SPKW project: a source
is only considered uniquely informative if the annotation is not already supported
by another source for the exact term, or by another source for a more specific
descendant term.

UniPathway-derived annotations are mostly biological-process pathway assertions.
Unlike SPKW, the strongest signal is not broad eukaryotic process conflation; it is
a mix of useful pathway gap-filling, broad parent-process assertions, and a small
number of source-pathway mapping errors where a pathway bucket is too coarse for a
specific gene product.

`GO_REF:0000041` describes UniPathway as an archived, no-longer-maintained pathway
vocabulary. That makes this a legacy-source audit: useful annotations should be
retained, but broad or stale mappings should not be treated as automatically
current.

## Key Findings

- **Closure filtering matters**: in human GOA, 1,129 UniPathway annotations reduce
  to 247 true unique annotations after exact and descendant-term support from other
  sources is removed.
- **Most unique annotations are plausible metabolic or protein-modification pathway
  context**, not obvious over-annotation.
- **The largest human unique term is `protein ubiquitination`** (`GO:0016567`),
  driven by `UniPathway:UPA00143`. This bucket contains clear positives such as
  E3 ligases and CRL adaptors, but also at least one incorrect mapping for ISG15
  conjugation. However, decisions as to pathway boundaries are unclear: UniPathway
  treats E1 activation, E2 transfer, and E3-mediated substrate recognition/transfer
  as children of the same pathway bucket, while GO curation still has to decide
  whether each gene product is directly participating in ubiquitination or only
  regulating, binding, or responding to ubiquitinated proteins.
- **Metabolic pathway terms are usually accurate when the gene catalyzes a step in
  the pathway**, especially in bacteria and yeast.
- **Some UniPathway terms are correct but too broad for the final curated
  representation**, for example parent lipid-metabolism terms where the gene is
  better captured by a more specific enzymatic product or remodeling pathway.
- **The microbial signal is much larger than the vertebrate signal**. Aggregate
  bacterial, fungal, archaeal, and viral scans show that UniPathway is often a
  unique source for pathway-level microbial metabolism.
- **Targeted term-group review is necessary**. Nitrogen-cycle terms show a useful
  positive signal for denitrification and urease-linked urea catabolism, but also
  probable mapping-risk cases such as nrfA genes annotated to nitrate
  assimilation.

## Methods

This project used local GOA DuckDB databases under `~/repos/go-db/db/`.
UniPathway annotations were counted from non-negated `GO_REF:0000041` rows.

A row was treated as **TRUE unique** only when no non-UniPathway source already
supported the same gene-term pair, and no non-UniPathway source supported a more
specific descendant term for the same gene. This prevents parent pathway terms
from looking novel when another source already supports a more specific process.

The nitrogen-cycle audit used the GO:0071941 nitrogen cycle metabolic process
closure. Exemplar rows were then reviewed through the gene-review workflow:
fetch gene data, edit the review YAML, validate, render the gene page, and link
the reviewed result from this project page.

For the pilot rows below, the YAML reviews now include explicit per-annotation
reasons and `supported_by` evidence. Where direct species-level experiments were
not available, the review states the inference basis: enzyme name and EC,
UniProt pathway/reaction text, InterPro/NCBIfam/PANTHER family placement, locus
context, or broader family literature.

## Deep Research Highlights

The deep-research pass was most useful for checking whether broad family-level
summaries matched the specific propagated node, subfamily, or independent
enzyme evidence for each gene:

- NorR-family research supports norR1 and norR2 as NO-responsive sigma-54
  transcription activators, not denitrification enzymes. This supports keeping
  regulatory activity terms while marking the UniPathway denitrification process
  rows as over-annotated.
- The NosZ/Cox2 CuA family report explains why nosZ and Ferp_0128 can carry
  misleading cytochrome-c oxidase annotations. The family has shared CuA-related
  ancestry, but the reviewed proteins sit in nitrous-oxide reductase context, so
  the reviews remove cytochrome-c oxidase activity and keep N2O reduction.
- The cytochrome c-552/NrfA family report showed why a broad family display
  label should not be treated as the propagation unit. PANTHER is useful when
  the tree, subfamily, and IBA propagation identify the relevant clade; for nrfA,
  the decisive evidence is the gene-specific EC/HAMAP/InterPro nitrite-reductase
  assignment, while the UniPathway nitrate-assimilation row is removed because it
  describes the wrong biological-process endpoint.
- Multicopper-oxidase family research supports copper nitrite reductase calls
  only when the nitrite-reductase subfamily evidence is present. That reinforces
  nirK positives while leaving the singleton fungal AJ80_06654
  denitrification-pathway row undecided.
- Urease-family research supports ureC1 and ureC2 as direct urea-catabolism
  positives, but adds a useful caveat: most ureases are nickel enzymes, yet rare
  iron ureases mean metal-binding annotations should be tied to gene-specific or
  subfamily evidence.
- For BRADI_1g66227v3, Falcon found no direct paper on the Brachypodium gene.
  Plant UXS literature strongly supports UDP-glucuronate decarboxylase activity
  and UDP-D-xylose biosynthesis, but Golgi localization remains a UniProt
  prediction rather than a gene-specific experiment.

## Cross-Organism Scan

| Database | UniPathway annotations | UniPathway genes | TRUE unique annotations | TRUE unique genes | TRUE unique terms |
|----------|------------------------|------------------|-------------------------|-------------------|-------------------|
| human (`goa_human.ddb`) | 1,129 | 1,066 | 247 | 243 | 57 |
| mouse (`goa_mouse.ddb`) | 1,110 | 1,053 | 231 | 223 | 57 |
| MGI (`mgi.ddb`) | 1,110 | 1,053 | 227 | 220 | 57 |
| RGD (`rgd.ddb`) | 967 | 915 | 242 | 234 | 57 |
| Xenopus (`goa_xenopus.ddb`) | 1,687 | 1,611 | 484 | 462 | 54 |
| ZFIN (`zfin.ddb`) | 690 | 656 | 213 | 202 | 50 |
| WormBase (`wb.ddb`) | 476 | 459 | 123 | 118 | 41 |
| ANOGA (`ANOGA.ddb`) | 279 | 270 | 75 | 73 | 38 |
| SGD (`sgd.ddb`) | 551 | 524 | 124 | 116 | 41 |
| PomBase (`pombase.ddb`) | 386 | 373 | 69 | 67 | 24 |
| Brachypodium (`BRADI.ddb`) | 819 | 790 | 228 | 223 | 48 |
| wheat (`goa_wheat.ddb`) | 2,697 | 2,620 | 750 | 738 | 50 |
| PSEPK (`PSEPK.ddb`) | 426 | 395 | 51 | 45 | 30 |
| bacteria aggregate | 1,594,828 | 1,462,204 | 165,344 | 144,244 | 204 |
| Pseudomonadota aggregate | 667,184 | 611,258 | 66,978 | 60,017 | 154 |
| Clostridium aggregate | 94,078 | 86,152 | 9,210 | 8,039 | 88 |
| fungi aggregate | 233,164 | 223,751 | 51,093 | 48,303 | 117 |
| archaea aggregate | 33,403 | 30,381 | 3,140 | 2,615 | 63 |
| virus aggregate | 285 | 278 | 140 | 135 | 25 |

## Broader Species and Clade Patterns

| Scope | Dominant TRUE unique terms | Initial review implication |
|-------|----------------------------|----------------------------|
| Plants: Brachypodium and wheat | `protein ubiquitination`, pectin biosynthesis/catabolism, cinnamic acid biosynthesis, UDP-D-xylose biosynthesis, sucrose metabolism | Plant scans reproduce the eukaryotic ubiquitination bucket, but also add plant-specific cell-wall and phenylpropanoid pathway terms that look more source-specific than the vertebrate lipid-parent terms. |
| Amphibian: Xenopus | `protein ubiquitination`, cAMP catabolism, heparin proteoglycan biosynthesis, UMP/CTP salvage, fatty acid beta-oxidation | Broadly resembles human and mouse. The top list also contains obsolete L-histidine catabolism terms, so Xenopus should be checked for stale GO mappings before accepting pathway rows. |
| Bacteria and Pseudomonadota | oxidative phosphorylation, tetrahydrofolate biosynthesis, thiamine diphosphate biosynthesis, histidine catabolism, malonyl-CoA biosynthesis, Kdo2-lipid A biosynthesis | Strongest positive signal. These terms are often close to operon/pathway membership and are good candidates for `ACCEPT` when gene-level function matches the pathway step. |
| Clostridium aggregate | urea cycle plus core anaerobic amino-acid, cofactor, and energy-metabolism pathways | Useful for clade-specific microbial metabolism, but nitrogen-related parent terms need pathway-context review rather than automatic environmental-process interpretation. |
| Fungi and archaea | large numbers of true-unique metabolic-pathway rows, including nitrogen-related subsets | Useful as a bridge between eukaryotic pathway assertions and microbial metabolism. Fungal edge cases should be checked carefully when the process is better known from bacteria or archaea. |
| Viruses | `protein ubiquitination`, nucleotide biosynthesis/salvage, translational elongation, DNA modification | Small but nontrivial unique set. Viral ubiquitination and nucleotide-process annotations should be reviewed for whether the viral product executes the process or modulates a host pathway. |

## Targeted Term Group: Nitrogen Cycle

The nitrogen-cycle audit used the GO:0071941 nitrogen cycle metabolic process
closure. In the scanned databases, UniPathway contributes rows for
denitrification pathway, nitrate assimilation, urea catabolic process, and
urea cycle. It did not contribute rows for nitrogen fixation or nitrogenase
activity terms in the scanned datasets, so this source is not currently filling
nitrogenase annotation gaps.

| Scope | GO term | UniPathway rows | TRUE unique rows | TRUE unique taxa | Initial assessment |
|-------|---------|-----------------|------------------|------------------|--------------------|
| bacteria | GO:0019333 denitrification pathway | 615 | 615 | 530 | High-priority microbial set, but review by gene role. Enzymes such as nirK1, nirK2, and nosZ are strong positives; regulator rows such as norR1 and norR2 can be over-annotated if mapped directly to the pathway. |
| Pseudomonadota | GO:0019333 denitrification pathway | 528 | 528 | 446 | Strong clade-specific signal; most bacterial denitrification true-unique rows are in this aggregate. |
| archaea | GO:0019333 denitrification pathway | 19 | 19 | 19 | Plausible but smaller archaeal set; review gene context before accepting, especially for haloarchaeal rows. |
| fungi | GO:0019333 denitrification pathway | 1 | 1 | 1 | Edge case. Fungal denitrification is biologically plausible in some taxa, but a singleton UniPathway row should be reviewed with high scrutiny. |
| bacteria | GO:0042128 nitrate assimilation | 2,767 | 14 | 14 | Mostly redundant after closure filtering. The remaining true-unique examples include nrfA and related cytochrome nitrite reductases, which may indicate a mapping problem rather than assimilatory nitrate use. |
| fungi | GO:0042128 nitrate assimilation | 556 | 0 | 0 | No unique UniPathway signal after closure filtering. |
| PSEPK | GO:0042128 nitrate assimilation | 1 | 0 | 0 | Not a useful unique term in the P. putida pilot. |
| bacteria | GO:0043419 urea catabolic process | 6,688 | 44 | 33 | Low unique fraction but likely useful for urease subunits when the gene product is directly part of urea hydrolysis. |
| archaea | GO:0043419 urea catabolic process | 130 | 10 | 9 | Stronger targeted signal. Examples include ureC1, ureC2 in Nitrososphaera viennensis and ureC in other ammonia-oxidizing or nitrogen-metabolizing archaea. |
| bacteria | GO:0000050 urea cycle | 1,189 | 1,189 | 1,149 | High-volume unique set, but not automatically an environmental nitrogen-cycling annotation. Review as arginine/ornithine/carbamoyl-phosphate pathway context. |
| fungi | GO:0000050 urea cycle | 790 | 682 | 646 | Similar broad pathway-context issue; likely useful for core nitrogen/amino-acid metabolism but not necessarily a nitrogen-cycle headline. |
| Clostridium | GO:0000050 urea cycle | 49 | 49 | 49 | Clade-specific positive candidates, subject to the same term-scope check. |

### Nitrogen-Cycle Pilot Assessments

| Example | UniPathway term | Assessment |
|---------|-----------------|------------|
| Rhodopseudomonas palustris CGA009 nirK1, nirK2, nosZ | GO:0019333 denitrification pathway | `ACCEPT` for all three reviewed genes. nirK1 and nirK2 are copper NO-forming nitrite reductases; nosZ is nitrous-oxide reductase. The support is mainly conserved enzyme/family evidence plus UniProt pathway mapping, not direct strain-specific biochemistry. The family research is useful here because it separates true NirK/NosZ pathway enzymes from broader multicopper-oxidase and CuA-like parent families. |
| Cupriavidus necator H16 norR1, norR2 | GO:0019333 denitrification pathway | `MARK_AS_OVER_ANNOTATED` for both reviewed genes. Falcon deep research plus primary NorR literature support an NO-responsive sigma-54 transcription activator role; the generic ATP-binding, regulation, and DNA-binding annotations were refined toward ATP hydrolysis, positive transcriptional regulation, and `GO:0141097` ligand-modulated transcription activator activity. |
| Ferroglobus placidus Ferp_0128 | GO:0019333 denitrification pathway | `ACCEPT`. PANTHER places the archaeal protein in the nitrous-oxide reductase subfamily, and the UniProt EC/pathway text matches terminal denitrification. The cytochrome-c oxidase parent annotation was removed in favor of nitrous-oxide reductase activity after reviewing the NosZ/Cox2 family boundary. |
| Nitrososphaera viennensis EN76 ureC1, ureC2 | GO:0043419 urea catabolic process | `ACCEPT` for both reviewed genes. Both are urease catalytic/alpha-subunit proteins supported by EC 3.5.1.5 plus TIGR01792/PTHR43440 urease-family placement, so urea catabolism is direct reaction context. The reviews keep metal-binding statements tied to available evidence because rare iron ureases make blanket nickel propagation risky. |
| Desulfotalea psychrophila nrfA | GO:0042128 nitrate assimilation | `REMOVE`. nrfA is an ammonia-forming cytochrome c nitrite reductase; the better MF is `GO:0042279` nitrite reductase (cytochrome, ammonia-forming) activity. The UniPathway nitrate-assimilation assertion does not match this dissimilatory nitrite-reduction enzyme, and the cytochrome c-552 family report confirms that broad family names should not be used as a shortcut here. |
| Polytolypa hystricis AJ80_06654 singleton fungal row | GO:0019333 denitrification pathway | `UNDECIDED`. The family evidence supports copper NO-forming nitrite reductase activity, but the fungal denitrification pathway assertion remains a singleton automated UniPathway row without organism-specific pathway evidence. Multicopper-oxidase family breadth makes this a pathway-context question, not just an enzyme-family question. |

## Plant Pathway Pilot Assessments

| Example | UniPathway term | Assessment |
|---------|-----------------|------------|
| Brachypodium distachyon BRADI_1g22147v3 | GO:0045490 pectin catabolic process | `ACCEPT`. The protein is a predicted pectate lyase, supported by EC 4.2.2.2 and PANTHER pectate lyase family placement, so the pathway term is direct cell-wall pectin-degradation context. |
| Brachypodium distachyon LOC100829928 | GO:0009800 cinnamic acid biosynthetic process | `ACCEPT`. The gene encodes phenylalanine ammonia-lyase; InterPro Phe_NH3-lyase plus the PAL reaction support direct trans-cinnamate biosynthesis rather than only a broad ammonia-lyase-family call. |
| Brachypodium distachyon BRADI_1g66227v3 | GO:0033320 UDP-D-xylose biosynthetic process | `ACCEPT`. The gene encodes UDP-glucuronate decarboxylase; PANTHER PTHR43078:SF51 and NAD(P)-binding domains support the one-step UDP-D-xylose biosynthesis annotation. Falcon found no direct BRADI_1g66227v3 paper, so the pathway call is orthology/family-supported and the Golgi localization is treated as predicted rather than experimentally established. |

## Top Human TRUE UniPathway-Unique Terms

| GO term | Label | Unique genes | Initial assessment |
|---------|-------|--------------|--------------------|
| GO:0016567 | protein ubiquitination | 124 | Useful, but only with explicit substrate-adaptor and UBL boundaries |
| GO:0016024 | CDP-diacylglycerol biosynthetic process | 10 | Generally useful lipid-pathway gap filling |
| GO:0042572 | retinol metabolic process | 9 | Generally useful for retinoid enzymes, but broad for xenobiotic CYPs |
| GO:0006198 | cAMP catabolic process | 8 | Good for cAMP phosphodiesterases |
| GO:0008203 | cholesterol metabolic process | 6 | Mixed; direct for steroidogenic components, broad for drug-metabolizing CYPs |
| GO:0006631 | fatty acid metabolic process | 6 | Often correct but broad |
| GO:0019563 | glycerol catabolic process | 5 | Correct for glycerol kinase/dehydrogenase pathway genes |
| GO:0016925 | protein sumoylation | 4 | Mixed; inspect SUMO vs ubiquitin specificity |
| GO:0030210 | heparin proteoglycan biosynthetic process | 4 | Correct pathway context for NDST enzymes |
| GO:0006506 | GPI anchor biosynthetic process | 4 | Correct for GPI transamidase components |

## Protein Ubiquitination Boundary Review

UniPathway itself helps explain why this term is hard. `UPA00143` is not just a
generic label; it has three child pathways for the ubiquitination cascade:

| UniPathway term | Scope |
|-----------------|-------|
| `UPA00831` protein ubiquitination (ubiquitin activation) | E1-dependent ubiquitin activation |
| `UPA00832` protein ubiquitination (E2 ubiquitin transfer) | transfer from E1 to E2 |
| `UPA00833` protein ubiquitination (ubiquitin transfer) | E3-mediated transfer to substrates, with E3s described as substrate-recognition modules |

That source boundary supports including E1, E2, and E3 machinery in
`GO:0016567`, and it also explains why substrate-recognition proteins can be
legitimate positives. It does not settle every GO curation boundary, because GO
annotations are made to individual gene products rather than to the pathway as a
whole.

The key boundary problem is therefore how broadly `GO:0016567` should be read
when projected from the UniPathway parent:

| Interpretation | Curation consequence |
|----------------|----------------------|
| Catalysis only | Too narrow. It would incorrectly exclude substrate receptors such as SOCS4, SOCS5, KCTD11, and ZSWIM8 that directly recruit substrates to E3 ligase complexes. |
| Any regulatory connection to ubiquitin-dependent degradation | Too broad. It would include upstream signaling regulators, ubiquitin-binding cargo handlers, deubiquitinases, and non-ubiquitin UBL enzymes. |
| Direct ubiquitination machinery or direct substrate recruitment | Best boundary for these UniPathway rows. Accept `GO:0016567` when the gene product is part of the ubiquitin-transfer machinery or directly brings a substrate together with ubiquitin ligase machinery. |

Under this boundary, `GO:0016567` remains useful as a biological-process
grouping even when we add molecular-function adaptor terms. The BP term says
the gene product is directly involved in the ubiquitination process; the MF term
says what it does in that process. For non-catalytic substrate receptors, the
preferred core MF is `GO:1990756` ubiquitin-like ligase-substrate adaptor
activity, not a generic binding term and not an E3 catalytic activity term.

This means `protein ubiquitination` is not redundant with existing regulation
annotations such as positive regulation of proteasomal ubiquitin-dependent
protein catabolic process. The regulation terms describe the outcome or pathway
effect. `GO:1990756` describes the substrate-adaptor activity. `GO:0016567`
describes direct participation in the ubiquitin-conjugation process.

### Human GO:0016567 Triage

The 124 human TRUE UniPathway-unique `GO:0016567` rows divide into the following
curation buckets:

| Bucket | Count | Decision rule | Examples |
|--------|-------|---------------|----------|
| Substrate receptor or substrate adaptor | 63 | Usually `ACCEPT` for `GO:0016567`; add or prefer `GO:1990756` for the core MF when evidence supports direct substrate-ligase bridging. | ASB family, DCAF family, FBXO family, KCTD11, SOCS1, SOCS2, SOCS3, SOCS4, SOCS5, SOCS7 |
| Catalytic or probable E3 ligase | 45 | `ACCEPT`; prefer catalytic MF terms such as `GO:0061630` when present. | BRCA1, RAD18, RNF2, SYVN1, TRIM38 |
| E2 enzyme | 1 | `ACCEPT`; use E2 conjugating activity as core MF. | UBE2Z |
| Non-ubiquitin UBL specificity | 1 | `MODIFY` to the specific UBL process. | UBA7 to `GO:0032020` ISG15-protein conjugation |
| Deubiquitinase | 1 | Usually `MODIFY` or `REMOVE` unless there is separate ubiquitin-transfer evidence. | USP9Y |
| Ubiquitin-binding or cargo-handling protein | 1 | Usually not `ACCEPT` for `GO:0016567` without direct transfer-machinery evidence; use binding, cargo transport, or catabolic-process terms as appropriate. | HDAC6 |
| Regulatory or complex-module inspect bucket | 12 | Inspect manually; accept direct CRL modules, but do not accept solely from pathway membership or downstream effects. | ELOB, APPBP2, ARMC5, CDCA3, MED8, TULP4, ZBTB16 |

### Re-review Outcomes

| Gene set | Boundary class | `GO:0016567` outcome | Additional action |
|----------|----------------|----------------------|-------------------|
| BRCA1, RAD18, SYVN1, PEX2, PEX10, PEX12 | Catalytic E3 ligases or E3 ligase complex subunits with direct substrate ubiquitination evidence | `ACCEPT` | No adaptor MF needed for catalytic E3 cases; keep more specific monoubiquitination/polyubiquitination annotations where present. |
| KCTD11, ZSWIM8 | Substrate adaptors already carrying the adaptor MF | `ACCEPT` | Keep `GO:1990756` as the core MF. |
| SOCS4, SOCS5 | Substrate-recognition SOCS-box adaptors | `ACCEPT` | Added `GO:1990756` as `NEW`; changed core MF from substrate-binding-only terms to adaptor activity. |
| ELOB, ELOC | Elongin BC module proteins | `ACCEPT` | Clarified that these are direct CRL modules but not substrate receptors, so `GO:1990756` is not added. ELOB is in the TRUE UniPathway-unique scan; ELOC is a local non-unique comparator with both UniPathway and experimental rows. |
| UBA7 | ISG15-specific E1 activating enzyme | `MODIFY` | Replace `GO:0016567` with `GO:0032020` ISG15-protein conjugation. |

## Reviewed Exemplars

| Gene | Organism | UniPathway term | Action | Assessment |
|------|----------|-----------------|--------|------------|
| SOCS4 | human | `GO:0016567` protein ubiquitination | ACCEPT | Useful unique annotation. SOCS4 acts as a SOCS-box substrate adaptor recruiting Elongin/Cullin ubiquitin ligase machinery to targets such as EGFR. Re-review added `GO:1990756` ubiquitin-like ligase-substrate adaptor activity as the core MF. |
| SOCS5 | human | `GO:0016567` protein ubiquitination | ACCEPT | Same boundary as SOCS4. SOCS5 is a substrate-recognition component of an Elongin BC-CUL2/5-SOCS-box E3 ligase complex; re-review added `GO:1990756`. |
| KCTD11 | human | `GO:0016567` protein ubiquitination | ACCEPT | Useful unique annotation. KCTD11 functions as a CRL3 substrate adaptor and promotes HDAC1 ubiquitination/degradation. This shows that non-catalytic E3-complex adaptors can still be validly involved in ubiquitination. |
| ZSWIM8 | human | `GO:0016567` protein ubiquitination | ACCEPT | Substrate-adaptor positive control. Existing review already has `GO:1990756`, matching the boundary used for SOCS4, SOCS5, and KCTD11. |
| ELOB, ELOC | human | `GO:0016567` protein ubiquitination | ACCEPT | Direct CRL2/CRL5 module examples. These support the ubiquitination process but are not themselves substrate receptors, so the re-review explicitly does not add `GO:1990756`. |
| BRCA1, RAD18, SYVN1, PEX2, PEX10, PEX12 | human | `GO:0016567` protein ubiquitination | ACCEPT | Catalytic E3 or E3-complex positive controls. The UniPathway process term is broad but correct and should coexist with more specific ubiquitin ligase, monoubiquitination, and polyubiquitination terms. |
| UBA7 | human | `GO:0016567` protein ubiquitination | MODIFY | Mapping error. UBA7 is an ISG15-activating E1 enzyme; the correct process is `GO:0032020` ISG15-protein conjugation, not generic protein ubiquitination. This is the clearest human pilot example where `UPA00143` overgeneralizes a ubiquitin-like modifier pathway. |
| COX5B | human | `GO:0006119` oxidative phosphorylation | ACCEPT | Useful unique annotation. COX5B is a structural Complex IV subunit, so UniPathway adds correct OXPHOS context beyond component/localization annotations. |
| GK5 | human | `GO:0019563` glycerol catabolic process | KEEP_AS_NON_CORE | Correct but not core. GK5 phosphorylates glycerol to glycerol-3-phosphate; the pathway term captures catabolic context, while the core review is better centered on glycerol kinase activity and glycerol-3-phosphate biosynthesis. |
| PM20D1 | human | `GO:0006631` fatty acid metabolic process | KEEP_AS_NON_CORE | Correct substrate context but broad. PM20D1 synthesizes/hydrolyzes N-fatty-acyl amino acids; it uses fatty acids but is not primarily a fatty-acid catabolic or biosynthetic enzyme. |
| LPCAT1 | human | `GO:0006644` phospholipid metabolic process | MARK_AS_OVER_ANNOTATED | Broad parent term. The gene is better represented by specific phospholipid remodeling and phosphatidic-acid/phosphatidylcholine-related processes already present in the review. |
| algE | P. putida KT2440 | `GO:0042121` alginic acid biosynthetic process | ACCEPT | Useful unique bacterial annotation. AlgE is an outer-membrane alginate pore/export component; the pathway term correctly captures its alginate production role. |
| catA | P. putida KT2440 | `GO:0042952` beta-ketoadipate pathway | ACCEPT | Useful unique bacterial pathway annotation. CatA catalyzes catechol ring cleavage in the beta-ketoadipate pathway, and the UniPathway row captures the core aromatic-catabolism pathway context. |

## Pattern Analysis

### 1. Metabolic Enzyme in Pathway - Usually ACCEPT

Examples: COX5B in oxidative phosphorylation, catA in beta-ketoadipate pathway,
algE in alginate biosynthesis.

These are the strongest UniPathway successes. The source supplies a pathway-level
biological-process annotation that may be missing from InterPro, PAINT, or direct
manual curation, while staying close to the enzyme or complex role.

### 2. Protein Modification Buckets - Inspect Mechanistic Role

Examples: SOCS4, SOCS5, KCTD11, ZSWIM8, ELOB, ELOC, UBA7.

`UPA00143` is valuable for E3 ligases, direct E3-complex modules, and
substrate-adaptor proteins, but it needs the boundary rules above. The key
curation split is catalytic ubiquitin-transfer activity versus substrate-adaptor
activity versus non-ubiquitin UBL specificity.

### 3. Broad Lipid Parent Terms - Often KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED

Examples: PM20D1, LPCAT1.

UniPathway often captures the broad lipid class correctly, but the broad term may
not be the best curated endpoint when specific lipid remodeling, acyltransferase,
or N-acyl-amino-acid chemistry is available.

### 4. Bacterial Pathway Coverage - Strong Positive Signal

The PSEPK pilot resembles the positive-control side of the SPKW bacterial work.
Top TRUE unique terms include beta-ketoadipate pathway, oxidative phosphorylation,
thiamine diphosphate biosynthesis, tetrahydrofolate biosynthesis, histidine
catabolism, and LPS/heptose biosynthesis. These generally map directly to operon
or enzyme-pathway membership and look curatorially useful.

### 5. Term-Group Audits - Better Than Source-Wide Sampling

The nitrogen-cycle scan shows why UniPathway should be reviewed by biologically
coherent term groups, not only by source-wide top terms. Denitrification is a
high-confidence microbial target, while nitrate assimilation is mostly redundant
and its remaining true-unique cases include likely non-assimilatory nrfA rows.
Urea-cycle terms are high volume but need careful scope interpretation in microbes.

### 6. Pathway Regulators - Do Not Treat as Pathway Enzymes

Examples: norR1, norR2.

UniPathway can correctly record that a regulator is associated with a pathway, but
the GO biological-process annotation may become too direct if the row is projected
as `involved_in denitrification pathway`. NorR1 and NorR2 regulate nitric oxide
reductase expression; they should not be curated as denitrification-pathway
enzymes.

## Curation Recommendations

1. **Keep closure filtering as the default**. Naive UniPathway-only queries overstate
   novelty by counting rows already supported by exact or more specific terms from
   other sources.
2. **Prioritize `UPA00143` review**. It is the dominant human unique source and has
   both good positives and clear UBL-specific mapping errors.
3. **Treat bacterial metabolic pathway rows as high-value candidates**. They often
   add real pathway context absent from other GOA sources.
4. **Downgrade broad parent lipid terms when specific processes exist**. Use
   `KEEP_AS_NON_CORE`, `MARK_AS_OVER_ANNOTATED`, or `MODIFY` depending on whether
   the broad term is merely contextual or actually misleading.
5. **Check modifier identity before accepting protein-modification terms**. Do not
   assume that a UniPathway protein-modification bucket is specific enough for GO.
6. **Use targeted term-group audits for microbial processes**. For nitrogen-cycle
   terms, denitrification and urease-linked urea catabolism are higher-value review
   targets than nitrate assimilation, which is mostly redundant or potentially
   mis-mapped in the true-unique tail.
7. **Separate pathway enzymes from pathway regulators**. For UniPathway rows on
   transcriptional regulators, inspect whether the source is asserting direct
   pathway membership or only regulatory context.

## Follow-Up Targets

| Target | Rationale |
|--------|-----------|
| Human `UPA00143` audit | 124 TRUE unique genes; likely highest yield for both gap filling and error cleanup, using the protein-ubiquitination boundary rules above |
| Human retinol/cholesterol CYP subset | Several true-unique rows may be broad xenobiotic/steroid context rather than core pathway function |
| PSEPK beta-ketoadipate set | Positive-control set for validating UniPathway as bacterial pathway gap filler |
| Yeast protein glycosylation set | Top SGD unique term (`GO:0006486`, 24 genes); likely useful but should be checked for specificity |
| Bacterial denitrification set | 615 TRUE unique bacterial rows across 530 taxa; likely highest-yield microbial nitrogen-cycle target |
| Bacterial nrfA nitrate-assimilation tail | 14 TRUE unique rows; likely mapping-risk set where GO:0042128 may not match dissimilatory nitrite reduction biology |
| Archaeal urease set | 10 TRUE unique `urea catabolic process` rows across 9 taxa; good targeted archaea exemplar set |
| Plant cell-wall pathway set | Brachypodium and wheat true-unique pectin and UDP-D-xylose rows; useful plant-specific contrast to vertebrate ubiquitination |
| Cupriavidus NorR regulator set | Denitrification true-unique rows can over-annotate regulators as pathway enzymes; useful negative-control set |

## Project Status

- **Started**: 2026-05-21
- **Pilot databases reviewed**: human, mouse, rat, Xenopus, zebrafish, yeast,
  fission yeast, worm, ANOGA, Brachypodium, wheat, PSEPK, aggregate bacteria,
  Pseudomonadota, Clostridium, fungi, archaea, and virus
- **Targeted term group reviewed**: nitrogen-cycle closure under GO:0071941
- **Full exemplar reviews referenced**: SOCS4, SOCS5, KCTD11, ZSWIM8, ELOB,
  ELOC, BRCA1, RAD18, SYVN1, PEX2, PEX10, PEX12, UBA7, COX5B, GK5,
  PM20D1, LPCAT1, algE, catA, nirK1, nirK2, nosZ, ureC1, ureC2, nrfA,
  AJ80_06654, norR1, norR2, Ferp_0128, BRADI_1g22147v3, LOC100829928,
  BRADI_1g66227v3
- **Current conclusion**: UniPathway is a net positive source for unique pathway
  annotations, with a lower apparent over-annotation rate than problematic SPKW
  eukaryotic BP mappings. The main risk is broad pathway-bucket propagation, not
  wholesale process conflation.

## Technical Appendix

The scan uses a closure-filtered uniqueness query. The important curation point is
that exact duplicate support and more-specific descendant support are both removed
before a UniPathway row is called uniquely informative.

<details>
<summary>Closure-filtering SQL used for source-wide counts</summary>

```sql
WITH upa AS (
    SELECT internal_id, db_object_id, db_object_symbol, ontology_class_ref, aspect
    FROM gaf_association
    WHERE supporting_references = 'GO_REF:0000041'
      AND is_negation = false
),
true_unique AS (
    SELECT u.*
    FROM upa u
    WHERE NOT EXISTS (
        SELECT 1
        FROM gaf_association o
        WHERE o.db_object_id = u.db_object_id
          AND o.ontology_class_ref = u.ontology_class_ref
          AND o.supporting_references != 'GO_REF:0000041'
          AND o.is_negation = false
    )
    AND NOT EXISTS (
        SELECT 1
        FROM isa_partof_closure ipc
        JOIN gaf_association o
          ON o.db_object_id = u.db_object_id
         AND o.ontology_class_ref = ipc.subject
         AND o.supporting_references != 'GO_REF:0000041'
         AND o.is_negation = false
        WHERE ipc.object = u.ontology_class_ref
    )
)
SELECT count(*) AS annotations,
       count(DISTINCT db_object_id) AS genes,
       count(DISTINCT ontology_class_ref) AS terms
FROM true_unique;
```

</details>
