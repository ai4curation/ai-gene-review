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
