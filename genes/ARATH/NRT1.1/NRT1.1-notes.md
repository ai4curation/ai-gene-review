# NRT1.1 (NPF6.3/CHL1; AT1G12110, Q05085) consolidation notes

## Canonical identity and scope — 2026-10-26

NCBI Gene 837763 lists **NRT1.1** as the Official Symbol and TAIR:AT1G12110 as its primary nomenclature source (https://www.ncbi.nlm.nih.gov/gene/837763; checked 2026-10-26). ABRC stock CS6384 independently uses NRT1.1 and calls CHL1 the former name (https://abrc.osu.edu/stocks/number/CS6384). Current UniProt Q05085 instead uses NPF6.3 as its primary name and retains NRT1.1 and CHL1 as synonyms. The canonical review follows the TAIR-sourced species nomenclature; the normally fetched UniProt and GOA records are unchanged. `just fetch-gene ARATH Q05085 --alias NRT1.1` retrieved the exact Q05085 protein and 19 GOA rows.

The older CHL1 review has 14 claims, all contained in the 19-row current GOA. Six legacy rows lack `supporting_entities` metadata supplied by both the newer NPF6.3 review and the fresh normal fetch. The canonical review keeps all 19 current rows verbatim outside `review`, rather than manufacturing six duplicate assertions solely to represent absent historical metadata. `NRT1.1-consolidation/legacy-reviews.json` preserves both exact pre-consolidation parsed reviews and source-file hashes; `payload-projection.json` maps all 33 legacy row occurrences to their canonical counterparts and proves every asserted legacy field is preserved.

The CHL1 directory also contains BioReason predictions for Q9LUJ8/At5g40090, an unrelated immune protein. Those artifacts and their benchmark links remain in place and are not treated as NRT1.1 evidence. The Q05085 Falcon report is genuine and is copied byte-for-byte with its relative artifact directory; no new provider report was fabricated. Legacy raw sources remain untouched for provenance.

## Source reconciliation

- **Auxin is a directly transported substrate, not merely a developmental readout.** PMID:20627075 reports nitrate-inhibited auxin uptake. Full PMID:31431511 Figure 1 compares yeast IAA influx and basipetal lateral-root tracer movement in NRT1.1 phosphovariants, together with DR5 distribution. Thus basipetal auxin transport remains ACCEPT and the conditional auxin influx MF is retained as core. Tissue-level movement out of a lateral-root tip is not evidence for cellular auxin efflux. Broad transporter/transport rows retain both nitrate and auxin replacements. The five extra GOA rows all survive.
- **Flowering remains non-core on corrected independent evidence.** Full PMID:30972097 studies nitrate allocation and cadmium tolerance; it does not support the original flowering citation. Full PMID:33643357 directly compares single/combined transporter mutants under long and short days and supports additive NRT1.1/NRT2.1 contributions to nitrate-sensitive long-day flowering. PMID:31084876 describes a different FLC-associated context. The old source mismatch is retained in reference assessment without using it to deny the independently supported function.
- **Nitrate uptake and sensing both survive.** PMID:10330471 reports biphasic oocyte kinetics near 50 micromolar and 4 millimolar. PMID:19766570 reports uptake/sensing-decoupled mutants and CIPK23/Thr101-dependent response tuning. The separate sensor core is represented as proposed molecular function `nitrate sensor activity`, with direct support, instead of leaving an invalid core without an MF or conflating sensing with transport chemistry. The older nitrate-activated-signaling BP proposal is preserved with a narrower definition and primary support; no NEW annotation is introduced.
- **Oligomeric behavior is not an absolute binary rule.** Full PMID:31431511 reports mixed monomer/dimer populations for both phosphovariants with different proportions. The structural expert question now asks about that ensemble and trafficking, while retaining the older structure-function experiments.
- **Additional findings preserved without title-as-evidence.** PMID:9844028, PMID:10330471, PMID:15319483 and PMID:17148611 now have matched abstract-body quotations. A normal forced PMID:23645597 fetch remains metadata-only; its qualitative root-to-shoot/bidirectional nitrate role is retained through publication-linked curated UniProt statements, not a quotation of its title.

The historical notes below document prior states and are preserved as provenance; the source reconciliation above supersedes their conflicting conclusions and old identity labels.


## Historical CHL1 notes (pre-consolidation)

# CHL1 (At1g12110) - NPF6.3 / NRT1.1 Nitrate Transporter

## Identity

- **UniProt**: Q05085 (PTR7_ARATH)
- **Gene**: CHL1 (CHLORATE RESISTANT 1); NPF6.3; NRT1.1; NRT1
- **Locus**: At1g12110
- **Organism**: Arabidopsis thaliana
- **Protein**: Protein NRT1/PTR FAMILY 6.3 (590 aa)
- **Family**: Major facilitator superfamily (MFS); proton-dependent oligopeptide
  transporter (POT/PTR, TC 2.A.17) family; NPF (NRT1/PTR) family
- **Structures**: PDB 4OH3, 5A2N, 5A2O (X-ray, dimer)

## IMPORTANT: Gene-identity correction (2026-06)

The gene symbol "CHL1" in Arabidopsis is ambiguous. The CANONICAL CHL1 — and the
gene defined by the UniProt record (Q05085), the QuickGO GOA (after re-fetch), the
task brief, and the falcon deep research report in this folder — is **NPF6.3 /
NRT1.1 (At1g12110)**, the dual-affinity nitrate transporter / transceptor.

A previous version of `CHL1-ai-review.yaml` incorrectly reviewed a DIFFERENT gene,
**Q9LUJ8 / At5g40090** ("Disease resistance protein CHL1" / CHS1-LIKE 1, a truncated
TIR-NBS protein). The `CHL1-goa.tsv` had also been fetched for Q9LUJ8. Both were
corrected: the review is now for Q05085 and the GOA was re-fetched for Q05085
(QuickGO, 14 annotations). The BioReason SFT prediction files in this folder target
Q9LUJ8 and are therefore not relevant to the canonical CHL1 nitrate transporter.

## Functional Summary (Q05085 / NRT1.1 / NPF6.3)

CHL1/NRT1.1 is the first cloned plant nitrate transporter and the founding member of
the NPF (NRT1/PTR) family. It is a plasma-membrane, proton-coupled nitrate symporter
in roots (epidermal/vascular cells) and guard cells. It is **dual-affinity** with
biphasic kinetics: high-affinity Km ~50 uM and low-affinity Km ~4 mM
[PMID:10330471]. The affinity mode is switched by phosphorylation of **Thr101** by
the CBL1/CBL9-CIPK23 kinase module [PMID:12606566, PMID:19766570].

Beyond transport, CHL1 acts as a nitrate **sensor ("transceptor")** that initiates
the primary nitrate response and regulates other nitrate genes (e.g., NRT2.1);
sensing is separable from uptake [PMID:19766570, PMID:15319483]. It also facilitates
**basipetal auxin transport**, linking nitrate availability to lateral root
development [PMID:20627075], contributes to **stomatal opening / drought**
[PMID:12509525], and mediates **root-to-shoot nitrate translocation** [PMID:23645597].
Originally identified via chlorate-resistance screens (chlorate is a toxic nitrate
analog) [PMID:8453665].

## Key Literature (nitrate transporter)

- PMID:8453665 - Tsay et al. 1993, Cell. CHL1 = nitrate-inducible nitrate transporter.
- PMID:9844028 - Wang et al. 1998, PNAS. Major role in high-affinity nitrate uptake.
- PMID:10330471 - Liu et al. 1999, Plant Cell. Dual-affinity transporter; kinetics.
- PMID:12606566 - Liu & Tsay 2003, EMBO J. Thr101 phosphorylation affinity switch.
- PMID:12509525 - Guo et al. 2003, Plant Cell. Stomatal opening / drought.
- PMID:15319483 - Munos et al. 2004, Plant Cell. Regulates NRT2.1.
- PMID:17148611 - Remans et al. 2006, PNAS. Nitrate signaling / patch colonization.
- PMID:19766570 - Ho et al. 2009, Cell. CHL1 functions as a nitrate sensor; CIPK23.
- PMID:20627075 - Krouk et al. 2010, Dev Cell. Nitrate-regulated auxin transport.
- PMID:23645597 - Leran et al. 2013, Mol Plant. Bidirectional root-to-shoot transport.
- PMID:24572362 / PMID:24572366 - Sun et al. / Parker & Newstead 2014, Nature.
  Crystal structures; nitrate-binding pocket (His356), proton coupling.

## Falcon deep research (CHL1-deep-research-falcon.md)

Falcon (Edison Scientific) report targets Q05085/NPF6.3/NRT1.1 correctly. Key
synthesized points used to corroborate the review (all verbatim-verified):
- Dual-affinity, biphasic kinetics across a wide nitrate range.
- Transceptor concept: initiates primary nitrate response; regulates NRT2.1.
- Proton-coupled nitrate symporter; ExxER motif, His356.
- Thr101 affinity-mode switch; CBL1/CBL9-CIPK23; ABI2/ABA integration.
- Plasma membrane of root epidermal/vascular cells + guard cells.
- Basipetal auxin transport; lateral root development.
- Contributes roughly 10-80% of whole-plant nitrate uptake.

## GO Annotation Status (Q05085, after GOA re-fetch)

Core: GO:0015112 nitrate transmembrane transporter activity (IMP); GO:0015706
nitrate transmembrane transport (IMP); GO:0005886 plasma membrane (IDA);
GO:0010167 response to nitrate (IMP, transceptor).

Generic/over-annotations addressed: GO:0006857 oligopeptide transport (REMOVE -
family-level; CHL1 does not transport peptides); GO:0016020 membrane,
GO:0022857 transmembrane transporter activity, GO:0055085 transmembrane transport
(MODIFY to specific nitrate terms / plasma membrane); GO:0005515 protein binding
x2 (one MODIFY to protein kinase binding for CIPK23; one REMOVE for generic
AT2G45820 interaction). Non-core developmental/pleiotropic: GO:0010540 basipetal
auxin transport, GO:0048527 lateral root development, GO:0048573 photoperiodism
flowering, GO:0009414 response to water deprivation.

## 2026-10-14 — UNDECIDED rows resolved

Photoperiodism, flowering (IMP, PMID:30972097) is now MARK_AS_OVER_ANNOTATED rather than UNDECIDED. A search of the cached full text found no flowering experiment, so the PMID is probably mis-attributed. The intended source could not be identified, so the row is flagged rather than removed. It should be reported to TAIR.


## Historical NPF6.3 notes (pre-consolidation)

# NPF6.3 review notes


## 2026-10-26 complete source-specific annotation review

NPF6.3/NRT1.1/CHL1 is a nitrate transporter/sensor with conditional auxin uptake (PMID8453665, PMID19766570, PMID20627075). Nitrate sensing can be separated from uptake. PMID31431511 links phosphorylation, membrane dynamics, auxin flux and endosomal signaling to nitrate-dependent lateral-root growth. Cellular uptake and tissue-level basipetal movement are distinct: the latter does not imply auxin efflux by NPF6.3. CIPK23 binding is refined to protein-kinase binding; remorin proximity retains provenance but does not justify an invented functional binding class.

Full PMID24572366 directly tests target recognition: nitrate/chlorate are recognized while the tested dipeptide Ala-Ala is not, and structural comparisons explain divergence from peptide transporters. The broad peptide-family mapping is removed using target-level substrate evidence. This is different from unresolved amino-acid activity of LAX3, for which equivalent substrate exclusion was not recovered.

The original flowering citation PMID30972097 studies cadmium/nitrate allocation, but independent full PMID33643357 directly supports nutrient/long-day flowering effects and PMID31084876 gives a distinct FLC-associated context. Thus the existing flowering role is retained as non-core with corrected support. Guard-cell nitrate uptake promotes stomatal opening/transpiration; the mutant’s greater drought tolerance is not reversed into a claim that NPF6.3 itself promotes drought resistance. Cadmium-response participation is nitrate-allocation regulation, not direct Cd transport.

Reviewed all 19 original rows without changing machine-sourced term, evidence, source, qualifier, negation or donor fields. No new annotation rows were added. Decisions: {"ACCEPT": 7, "KEEP_AS_NON_CORE": 3, "MODIFY": 7, "REMOVE": 2}. Description and core functions are standalone biological summaries; proposed activities and uncertainty do not rewrite GOA payloads.

The coordinated real Falcon and perplexity-lite attempts failed (provider authentication/quota errors), while normal gene-publication fetching completed. Logs: `.cache/module-audit-logs/auxin-polar-fetch/ARATH-NPF6.3-provider.log` and `ARATH-NPF6.3-publications.log`; no provider report was fabricated. Manual primary-source reading, normal additional recovery and explicitly recorded access limits supply this review. Publication and UniProt source files were not hand-edited. Source-specific reference assessments, actual quotations, root-organelle retention and NOT semantics were checked.

