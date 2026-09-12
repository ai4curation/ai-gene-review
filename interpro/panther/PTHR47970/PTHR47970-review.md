# PANTHER Family Review: PTHR47970

## Family Overview

| Property | Value |
|----------|-------|
| **Family ID** | PTHR47970 |
| **Family Name** | KINESIN-LIKE PROTEIN KIF11 |
| **InterPro Entry** | IPR047149 |
| **Total Proteins** | 14,455 |
| **Taxonomic Breadth** | 9,896 taxa |
| **Subfamilies** | 21 |
| **Representative Structure** | 3zcw (Eg5 - new allosteric binding site) |
| **Anchor gene** | *S. pombe* cut7 (P24339), subfamily PTHR47970:SF12 |

## Executive Summary

PTHR47970 is the **kinesin-5 (BimC/Eg5/KIF11) family** of plus-end-directed, microtubule-based motor proteins, together with the related KIF20 (mitotic kinesin-like, MKLP) and plant kinesin-5 clades. Canonical kinesin-5 motors assemble into **bipolar homotetramers** that crosslink antiparallel interpolar (spindle) microtubules and slide them apart, generating the outward pushing force that **separates spindle poles and establishes/maintains spindle bipolarity** during mitosis and meiosis. The conserved molecular function is **plus-end-directed microtubule motor activity** (a microtubule-stimulated ATPase).

The fission yeast anchor gene **cut7** (P24339) is in subfamily **PTHR47970:SF12 (KINESIN FAMILY MEMBER 11)**, the core kinesin-5 subfamily that also contains *Aspergillus* bimC (P17120), *S. cerevisiae* CIN8 (P27895), *Drosophila* Klp61F (P46863), and human KIF11/Eg5 is the namesake of the adjacent SF26. Cut7 is the sole kinesin-5 of *S. pombe*: it crosslinks and slides antiparallel interpolar microtubules to drive spindle pole body separation and bipolar spindle assembly, opposing the inward force of the kinesin-14 motors Pkl1 and Klp2 (P24339 review; PMID:1538784; PMID:24239120; PMID:30659798; PMID:27834216).

## Subfamily Analysis

Subfamily assignments below are drawn from the curated representative members in `PTHR47970-entries.csv`.

### PTHR47970:SF12 - KINESIN FAMILY MEMBER 11 (anchor subfamily)
**Representative members** (largest curated subfamily):
- *S. pombe* cut7 (P24339)
- *Aspergillus (Emericella) nidulans* bimC (P17120)
- *S. cerevisiae* CIN8 (P27895)
- *Candida glabrata* CIN8 (Q6FXI5)
- *Eremothecium gossypii* CIN8 (Q8J1G7)
- *Drosophila* Klp61F (P46863)
- *Leishmania chagasi* K39 (P46865)
- *Dictyostelium discoideum* kif13 (Q6RZZ9)
- Plant kinesin-5 KIN-5C: *Arabidopsis* (P82266), rice (B7EJ91), tobacco (O23826)

**Function**: Core kinesin-5/BimC motors. Bipolar tetrameric, plus-end-directed; crosslink and slide antiparallel spindle microtubules to separate poles and assemble the bipolar spindle. This is the anchor subfamily for cut7 and is broadly conserved across fungi, animals, protists, and plants.

### PTHR47970:SF26 - KINESIN-LIKE PROTEIN KIF11
**Representative members**:
- Human KIF11/Eg5 (P52732)
- Mouse Kif11 (Q6P9P6)
- *Xenopus* KIF11-A (Q91783), KIF11-B (P28025)
- *Xenopus tropicalis* kif11 (B2GU58)

**Function**: The vertebrate KIF11/Eg5 clade — the canonical anti-mitotic drug target. Same core kinesin-5 mechanism (spindle bipolarity, pole separation) as SF12. Seeds from this subfamily contribute to the spindle-microtubule and mitotic-spindle-assembly transfers reaching cut7 (CROSS_SUBFAMILY).

### PTHR47970:SF29 - KINESIN FAMILY MEMBER 20B (KIF20)
**Representative members**:
- Human KIF20A (O95235), KIF20B (Q96Q89)
- Mouse Kif20a (P97329), Kif20b (Q80WE4)
- Bovine KIF20A (Q29RT6)

**Function**: KIF20/MKLP-type mitotic kinesins involved in cytokinesis/midbody function rather than classical kinesin-5 pole separation — a functionally divergent clade within the family.

### PTHR47970:SF19 - KINESIN-LIKE PROTEIN KIP1
**Representative members**:
- *S. cerevisiae* KIP1 (P28742)
- *Eremothecium gossypii* KIP1 (Q8J1G4)

**Function**: Fungal kinesin-5 (Kip1), redundant with Cin8 in budding yeast spindle pole separation.

### Plant kinesin-5 subfamilies (SF1, SF6, SF9, SF30, SF32)
**Representative members**: *Arabidopsis* KIN-5A (F4IIS5), KIN-5B (Q0WQJ7), KIN-5D (Q9LZU5), KIN-UA/UB/UC (Q9FZ06, Q9LPC6, Q9SV36); rice KIN-5A/5B/UA/UB (Q5W7C6, B9F7C8, Q0DV28, Q5VQ09).

**Function**: Plant-lineage expansion of kinesin-5/kinesin-like motors with roles in spindle and phragmoplast microtubule organization.

## Functional Diversity Assessment

The dominant conserved function across SF12, SF26, SF19, and the plant kinesin-5 subfamilies is bipolar, plus-end-directed kinesin-5 motor activity driving spindle bipolarity. The principal functional divergence is the **KIF20/SF29 clade**, which has a distinct cytokinesis/midbody role. Subfunctionalization is otherwise mostly by lineage (fungal Cin8/Kip1, vertebrate KIF11/Eg5, plant KIN-5) rather than by changed core biochemistry.

## IBA Annotation Assessment

IBA (`GO_REF:0000033`) annotations propagated to cut7 (P24339, subfamily PTHR47970:SF12). Flags and actions from `iba_propagation.tsv`.

| GO ID | Label | Aspect | Flags | Our action |
|-------|-------|--------|-------|------------|
| GO:0008574 | plus-end-directed microtubule motor activity | MF | NO_UNIPROT_SEEDS | ACCEPT |
| GO:0072686 | mitotic spindle | CC | LOCALIZATION; NO_UNIPROT_SEEDS | ACCEPT |
| GO:0005876 | spindle microtubule | CC | CROSS_SUBFAMILY; LOCALIZATION | ACCEPT |
| GO:0090307 | mitotic spindle assembly | BP | (seeds in SF12 + SF26) | ACCEPT |
| GO:0051231 | spindle elongation | BP | (seed in SF12) | ACCEPT |
| GO:0000073 | initial mitotic spindle pole body separation | BP | (node PTN001189565) | ACCEPT |
| GO:0005634 | nucleus | CC | LOCALIZATION; NO_UNIPROT_SEEDS | KEEP_AS_NON_CORE |

**Assessment**:

- **GO:0008574 (plus-end-directed microtubule motor activity)** — ACCEPT. The conserved core kinesin-5 molecular function and directly supported for cut7 (PMID:30659798 docked neck-linker consistent with plus-end-directed movement; PMID:27834216 crowding converts the motor to plus-end-directed stepping). Correct family-level transfer.

- **GO:0090307 / GO:0051231 / GO:0000073 (mitotic spindle assembly / spindle elongation / initial SPB separation)** — ACCEPT. These are the defining biological roles of kinesin-5 and of cut7 specifically (cut7 mutants fail SPB separation and form two half-spindles; PMID:1538784). Note these carry **UniProt and PomBase seeds within SF12** (n_seed_in_fam ≥ 1), so they are well-supported within the anchor's own subfamily, not just distant transfers.

- **GO:0072686 / GO:0005876 (mitotic spindle / spindle microtubule)** — ACCEPT. Both carry the `LOCALIZATION` triage flag, and GO:0005876 is additionally `CROSS_SUBFAMILY` (seeded from SF26, the vertebrate KIF11 clade). Despite triage, these localizations are CORRECT for cut7: kinesin-5 motors act on and localize to spindle/interpolar microtubules, and cut7 is documented to associate with spindle (polar) microtubules. The cross-subfamily transfer here is between two clades (SF12 and SF26) that share the same bipolar spindle mechanism, so the spindle-microtubule localization is a conserved family property, not a paralog-specific one. CROSS_SUBFAMILY is triage, not a verdict.

- **GO:0005634 (nucleus)** — KEEP_AS_NON_CORE. A `LOCALIZATION` transfer with no UniProt seeds, propagated from node PTN000649235 (seed includes *Drosophila* FBgn0004378). In *S. pombe* nuclear division is closed, so the spindle and motor reside within the nuclear envelope; a generic "nucleus" CC is plausible but uninformative relative to the spindle-microtubule terms, so it is retained as non-core rather than promoted.

**Summary**: All motor-activity and spindle-assembly/elongation/pole-separation terms transfer correctly to cut7 and are partly seeded within its own subfamily. The localization terms (mitotic spindle, spindle microtubule) are correct despite triage flags because the spindle association is a conserved kinesin-5 property; the generic nucleus term is kept as non-core.

## Key Literature

| PMID | Key Finding |
|------|-------------|
| PMID:1538784 | In bimC and cut7 mutants microtubule interdigitation fails; two unconnected half-spindles form and chromosome separation fails |
| PMID:24239120 | Cut7 is an active force producer, sliding interpolar microtubules apart as the outward pushing force on the spindle |
| PMID:30659798 | Cryo-EM neck-linker docking consistent with plus-end-directed motor movement |
| PMID:27834216 | Crowding converts the motor from minus-end- to plus-end-directed stepping |

## Review Status

- **Date**: 2026-06-07
- **Reviewer**: AI-assisted review
- **Status**: DRAFT
- **Based on**: PANTHER metadata/entries, UniProt, cut7 ai-review.yaml, GOA IBA rows, iba_propagation.tsv
