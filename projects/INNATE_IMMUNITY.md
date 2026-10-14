---
title: "Innate Immune System Pathways Across Animals"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN, FLAGSHIP]
species: [human, mouse, CHICK, DANRE, XENTR, DROME, ANOGA, worm, NEMVE, TACTR]
---

# Innate Immune System Pathways Across Animals

**Bottom line:** this project reviews the GO annotation of the innate immune
signaling machinery of animals — Toll and Toll-like receptors, their TIR-domain
adaptors and kinase relays, NLRs and inflammasomes, cytosolic nucleic-acid
sensors (RIG-I-like receptors, cGAS-like receptors and STING), C-type lectin and
complement-type recognition, and the Rel/NF-kappaB and IRF transcriptional
outputs — organised by **gene family** and compared across ten species from
sea anemone to human. **Batch 1, the Toll/TLR axis, is reviewed:** 37 gene
products in six species (all ten human TLRs with their co-receptors and
adaptors, mouse, chicken and zebrafish lineage-specific TLRs, the Drosophila
Toll pathway from Spätzle to Dorsal, *C. elegans* TOL-1 and Nematostella
MyD88), covering 2,734 existing annotations (plus 14 proposed new ones). Together with 28 genes reviewed
earlier by other projects, 65 of the 202 candidates
([candidates-resolved.tsv](INNATE_IMMUNITY/candidates-resolved.tsv)) are done.
The main results: the fly Toll-pathway term has leaked onto human IRAK4 and
MYD88 by phylogenetic inference; LPS and lipopeptide receptor terms were
spread across TLR partners that do not bind those ligands; and one mis-cited
paper (PMID:19593445) supports a "response to mechanical stimulus" row on six
TLR-axis genes. Details are in [Batch 1 results](#batch-1-results) and on the
[TLR family sub-page](INNATE_IMMUNITY/TLR_FAMILY.md).

We scoped this because innate immunity is where GO annotation is most exposed
to cross-species over-propagation. The same families (TLRs, NLRs, TIR proteins,
lectins) are massively and independently expanded in some lineages and lost in
others, and the canonical names hide real functional divergence — the
Drosophila Toll receptor binds an endogenous cytokine, not a microbial ligand;
chicken lacks RIG-I; fish TLR22 has no GO pathway term at all. A
family-by-lineage view is the right unit for checking whether IBA, ISO and
InterPro2GO annotations follow the biology.

## Scope

In scope: germline-encoded recognition, signaling and transcriptional output of
the innate immune response in Metazoa (GO:0045087 innate immune response and
its signaling-pathway descendants), plus a small set of effectors used as
end-points.

Out of scope, and handled elsewhere:

| Topic | Where |
|-------|-------|
| cGAS-STING in human detail | [CGAS_STING_PATHWAY](CGAS_STING_PATHWAY.md) |
| NLRP3 inflammasome in human detail | [NLRP3_INFLAMMASOME](NLRP3_INFLAMMASOME.md) |
| *C. elegans* surveillance immunity and the IPR | [CAEEL_SURVEILLANCE_IMMUNITY](CAEEL_SURVEILLANCE_IMMUNITY.md) |
| Prokaryotic immunity (CBASS, Thoeris, CRISPR) | [PROKARYOTIC_IMMUNITY_TERM_PREDICTION](PROKARYOTIC_IMMUNITY_TERM_PREDICTION.md) |
| Autoimmune disease genes | [AUTOIMMUNE](AUTOIMMUNE.md) |
| Adaptive immunity (TCR, BCR, MHC, VLRs) | not covered |
| Plant NLRs and pattern-triggered immunity | not covered; a natural follow-on |

This project overlaps the two human-pathway projects deliberately: here those
genes appear as one member of a family traced across species, not as a pathway
in its own right.

## Species

Chosen to span the main animal lineages that have well-studied innate immune
systems and a usable proteome in UniProt. Species codes follow repository
convention.

| Code | Species | Lineage | Why included |
|------|---------|---------|--------------|
| human | *Homo sapiens* | Mammalia | Reference system; most experimental annotation |
| mouse | *Mus musculus* | Mammalia | `Tlr11`, `Tlr12`, `Tlr13`, which have no counterpart among human TLR1–10; NAIP/NLRC4 and NLRP1B genetics |
| CHICK | *Gallus gallus* | Aves | Bird-specific TLR15 and TLR21 |
| DANRE | *Danio rerio* | Teleostei | Fish-specific TLRs (TLR5b, TLR18–22); inflammasome GO-CAM exists |
| XENTR | *Xenopus tropicalis* | Amphibia | Amphibian comparator (thin coverage) |
| DROME | *Drosophila melanogaster* | Insecta | Toll and Imd pathways; the origin of the Toll paradigm |
| ANOGA | *Anopheles gambiae* | Insecta | Complement-like TEP1 system against malaria parasites |
| worm | *Caenorhabditis elegans* | Nematoda | TLR-independent p38/PMK-1 immunity |
| NEMVE | *Nematostella vectensis* | Cnidaria | Early-branching animal with MyD88, NF-kappaB, cGAS and STING |
| TACTR | *Tachypleus tridentatus* | Chelicerata | LPS- and beta-glucan-triggered protease cascade (factor C, factor G) |

Lineages with very large expansions of innate receptor families — sea urchin
(*Strongylocentrotus purpuratus*), amphioxus (*Branchiostoma floridae*) and
oyster (*Crassostrea gigas*) — are not in the candidate list, because almost all
their entries are unreviewed TrEMBL records without gene names. They are
tracked at the family level instead. A count of UniProt entries carrying the
TIR domain (InterPro IPR000157) or the NACHT domain (IPR007111), taken
2026-09-30, shows the scale:

| Taxon | TIR-domain entries | NACHT-domain entries |
|-------|-------------------:|---------------------:|
| sea urchin (7668) | 271 | 264 |
| oyster (29159) | 234 | 13 |
| amphioxus (7739) | 138 | 103 |
| lamprey (7757) | 40 | 94 |
| Nematostella (45351) | 17 | 15 |

These are entry counts, not gene counts: redundant and fragmentary TrEMBL
entries inflate them. They are shown only to mark where IBA and InterPro2GO
propagation will act on hundreds of paralogs at once.

## Gene families

The organising unit. Each family is listed with the lineage-specific points
that matter for curation; per-gene accessions are in the checklist below.

### Toll and Toll-like receptors (TLR)

Leucine-rich-repeat ectodomain plus a cytoplasmic TIR domain. In vertebrates,
each TLR recognises a class of microbial molecule (lipopeptide, dsRNA, LPS,
flagellin, ssRNA, CpG DNA) and signals through MYD88 and/or TICAM1 (TRIF). In
Drosophila, Toll (Tl) is activated by the cleaved cytokine Spätzle, produced by
a protease cascade downstream of the real pattern recognition proteins (PGRPs,
GNBPs). GO carries a numbered signaling-pathway term for most vertebrate TLRs,
including the lineage-specific `TLR11`, 12, 13, 15 and 21, but none for fish TLR22.
Detail: [TLR family sub-page](INNATE_IMMUNITY/TLR_FAMILY.md).

### TIR-domain adaptors

MYD88, TIRAP (MAL), TICAM1 (TRIF), TICAM2 (TRAM) and SARM1 in human; Myd88 in
Drosophila; TIR-1 (the SARM1 orthologue) in *C. elegans*, which signals to the
p38 MAPK cascade rather than NF-kappaB. SARM1 has NADase activity, so its GO
annotation should reflect an enzyme, not only an adaptor. MYD88 is present in
Nematostella.

### IRAK and Pelle kinases

IRAK1, IRAK2, IRAK3 (IRAK-M, a pseudokinase) and IRAK4 in human; Tube
(adaptor, death domain only) and Pelle (kinase) in Drosophila. IRAK3 is already
reviewed and is a test case for [PSEUDOENZYMES](PSEUDOENZYMES.md): kinase
activity annotations propagated from active paralogs.

### TRAF ubiquitin ligases and kinase relays

TRAF3 and TRAF6 (both reviewed), MAP3K7 (TAK1) with TAB1/TAB2, the IKK complex
(CHUK, IKBKB, IKBKG) and the IKK-related kinases (TBK1 reviewed, IKBKE). The
Drosophila Imd branch uses Tak1, Tab2 and an IKK formed by IKKbeta (ird5) and
Kenny (key); Drosophila IKKepsilon already has a folder from another project.

### Rel/NF-kappaB and IkappaB

RELA and NFKB1 with the inhibitor NFKBIA in human; Dorsal (dl) and Dif with
the inhibitor Cactus (cact) downstream of Toll, and Relish (Rel) downstream of
Imd, in Drosophila; REL2 in *Anopheles*; a single NF-kappaB in Nematostella.
*C. elegans* has no NF-kappaB; its immune transcriptional output runs through
ATF-7, ZIP-2 and others.

### Interferon regulatory factors (IRF)

IRF3, IRF5 and IRF7 as the TLR/RLR/STING outputs in vertebrates. IRFs are a
vertebrate-centred family and serve here as the check that type I interferon
terms are not propagated to invertebrates.

### NOD-like receptors (NLR) and inflammasomes

NOD1, NOD2, NLRP1, NLRP3 (reviewed), NLRC4, NAIP, NLRP6 and CARD8 in human;
mouse Naip5, Nlrp1b and Nlrc4 for the genetics that defined NAIP/NLRC4 and NLRP1
ligand sensing; fish nod1/nod2 and the fish inflammasome caspases caspa and
caspb. Outputs: PYCARD (ASC), `CASP1`, CASP4 (reviewed), gasdermin D (reviewed),
IL1B and IL18. NACHT-domain expansions in sea urchin, amphioxus and lamprey are
tracked at family level only.

### RIG-I-like receptors (RLR)

RIGI (formerly DDX58), IFIH1 (MDA5, reviewed) and DHX58 (LGP2) signal through
MAVS, with TRIM25 as the E3 ligase activator. Chicken has IFIH1 and MAVS but no
RIGI entry, consistent with the reported loss of RIG-I in chicken. The *C.
elegans* RIG-I homologue DRH-1 acts in antiviral RNAi, not via a MAVS pathway,
and is the test case for whether RLR signaling terms are propagated to it.

### cGAS-like receptors (cGLR) and STING

Human CGAS and STING1 (reviewed), with fish, chicken, fly (cGlr1, cGlr2, Sting)
and Nematostella orthologues. Nematostella cGAS and STING are Swiss-Prot entries
(A7SFB5, A7SLZ2). Human biology is covered by
[CGAS_STING_PATHWAY](CGAS_STING_PATHWAY.md); this project asks whether
annotations of the invertebrate members reflect their own biochemistry, since
invertebrate STING proteins are ancestral and signal differently.

### C-type lectin receptors (CLR)

CLEC7A (Dectin-1), CLEC4E (Mincle) and CD209 (DC-SIGN) with the SYK–CARD9
relay (CARD9 also connects to BCL10–MALT1). Lectin domains are among the most
widely propagated domains in GO; *C. elegans* CLEC-60 (reviewed) is a
non-receptor example.

### Complement, thioester proteins and soluble recognition

MBL2 (reviewed), FCN2 and MASP2 (lectin pathway) and C3 in human; the
thioester-containing proteins TEP1 in *Anopheles* (reviewed, with its partners
LRIM1 and APL1C) and `Tep1`/`Tep2` in Drosophila; human PGLYRP1 and PGLYRP2 as the
vertebrate peptidoglycan recognition proteins, compared with the Drosophila
PGRPs.

### Peptidoglycan recognition proteins and GNBPs (insect)

Drosophila PGRP-SA, PGRP-SD, GNBP1 and GNBP3 feed the Toll pathway through the
proteases ModSP, Grass and SPE; Persephone (psh) senses microbial proteases and
Necrotic (nec) inhibits it. PGRP-LC and PGRP-LE are the Imd pathway receptors.
These are the true pattern recognition receptors of the fly, which is why
pattern recognition receptor activity on Toll itself would be an error.

### Horseshoe crab clotting cascade

Factor C (LPS-activated serine protease), factor B, proclotting enzyme and
coagulogen form the LPS-triggered cascade; factor G (alpha and beta subunits)
is the beta-glucan branch. All six entries are Swiss-Prot. Factor C is the
case of a pattern recognition receptor that is itself a protease — a check on
whether GO has an MF for recognition-coupled protease activation.

### Effectors

A small set of end-point genes: antimicrobial peptides (human DEFB4A, CAMP,
LYZ; Drosophila Drosomycin, Diptericin A, Metchnikowin, Attacin A, Cecropin A1,
Defensin; *C. elegans* LYS-7, SPP-1, NLP-29), interferon effectors (OAS1,
RNASEL, EIF2AK2, MX1) and Drosophila JAK-STAT (hop, Stat92E, upd3, TotA). They
are included to check the rule that an effector is not a participant in the
signaling pathway that induces it (see *Do not add what curators deliberately
declined to add* in CLAUDE.md).

## Existing modules and GO-CAMs

Draft pathway modules already exist and should be grounded against these
reviews:

- [Toll-like receptor signaling](../modules/toll_like_receptor_signaling.html) (TLR4, MYD88, IRAK4, TRAF6, MAP3K7)
- [NLR signaling](../modules/nlr_signaling.html)
- [RIG-I signaling](../modules/rig_i_signaling.html)
- [Canonical NF-kappaB signaling](../modules/nfkb_canonical_signaling.html)
- [Type I interferon signaling](../modules/type_i_interferon_signaling.html)
- [TLR2-heterodimer lipopeptide sensing](../modules/tlr2_heterodimer_lipopeptide_signaling.html)
  and [TLR4-MD-2 LPS sensing](../modules/tlr4_md2_lps_signaling.html): curated
  from the batch-1 reviews as reference representations. TLR1-TLR2 and
  TLR2-TLR6 are pattern recognition receptors (GO:0038187) whose partner subunit
  carries the lipopeptide-binding specificity; GO:0001875 lipopolysaccharide
  immune receptor activity appears only on TLR4-MD-2. Each receptor and adaptor
  links to the production GO-CAM activity it corresponds to, with a note where
  the GO-CAM differs.

Two of those GO-CAMs, 5fb9cc0600000727 (TLR1-TLR2) and 5fce9b7300000030
(TLR2-TLR6), have `GoCamReview` files recording why their receptor activity is
wrong; the two TLR4 models (5f46c3b700001031, 6413ac9800000654) type TLR4 only
with generic signaling receptor activity and omit MD-2.

Production GO-CAMs in `gocams/index.tsv` relevant to the first batch
(human unless stated):

| Model | Title |
|-------|-------|
| 5f46c3b700001031 | MYD88-dependent TLR4 signaling pathway leading to NF-kappa-B activation |
| 6413ac9800000654 | MYD88-independent TLR4 signaling pathway leading to interferon production |
| 5fb9cc0600000727 | Triacyl lipopetide activation of TLR1-TLR2 complex |
| 5fce9b7300000030 | Diacyl lipopeptide and bacteriocin activation of TLR6_TLR2 receptor |
| 663d668500002770 | Bacterial flagellin recognition by TLR5 |
| 6918f23700000328 | TLR9 signaling pathway leading to IRF5 activation |
| 5f46c3b700002102 | SPModule-TIRAP-MYDDOSOME |
| 641ce4dc00000050 | NOD2 signaling in response to muramyl dipeptide (MDP) leading to NF-kappa-B and MAPK kinase activation |
| 5fadbcf000001101 | SPModule IFIH1-MAVS |
| 60418ffa00001019 | NLRP3 inflammasome in pyroptosis via `nlrp3`, `caspa`, `caspb` etc. (zebrafish) |
| 568b0f9600000284 | Antibacterial innate immune response in the intestine via MAPK cascade (*C. elegans*) |

No production GO-CAM in the index models the Drosophila Toll or Imd pathway.

## GO terms in play

All ids checked against OLS on 2026-09-30.

| Id | Label | Note |
|----|-------|------|
| GO:0045087 | innate immune response | Root process for the project |
| GO:0002221 | pattern recognition receptor signaling pathway | Parent of the receptor-class pathways |
| GO:0002224 | toll-like receptor signaling pathway | Vertebrate TLRs |
| GO:0008063 | Toll signaling pathway | Drosophila Toll–Spätzle pathway |
| GO:0061057 | peptidoglycan recognition protein signaling pathway | Drosophila Imd pathway |
| GO:0035872 | nucleotide-binding domain, leucine rich repeat containing receptor signaling pathway | NLRs |
| GO:0002753 | cytoplasmic pattern recognition receptor signaling pathway | Cytosolic sensors |
| GO:0039529 | RIG-I signaling pathway | RLRs |
| GO:0140896 | cGAS/STING signaling pathway | cGLR/STING |
| GO:0038187 | pattern recognition receptor activity | MF for PRRs; no TLR-specific MF exists |
| GO:0001875 | lipopolysaccharide immune receptor activity | TLR4 complex |
| GO:0035591 | signaling adaptor activity | TIR adaptors |
| GO:0061702 | canonical inflammasome complex | Inflammasomes |
| GO:0140367 | antibacterial innate immune response | Used in the *C. elegans* GO-CAM |

GO:0039528 (cytoplasmic pattern recognition receptor signaling pathway in
response to virus) is obsolete; any existing annotation to it should be read
against the current replacement.

## Curation questions to test

1. **Is Drosophila Toll a pattern recognition receptor?** Toll binds cleaved
   Spätzle, not a microbial molecule. Check whether GO:0038187 or
   GO:0002224-branch terms reach Tl, 18w or Toll-7 by IBA or InterPro2GO, and
   whether GO:0008063 is kept distinct from GO:0002224 in practice.
2. **Numbered TLR pathway terms across species.** GO has terms for TLR1–13, 15
   and 21, but not TLR14, TLR16–20 or TLR22. Check how fish TLR22 and the
   TLR18–20 genes are annotated and whether a new term, or a general term, is
   right.
3. **No TLR-specific molecular function.** TLRs are annotated to generic PRR
   activity (GO:0038187) or, for TLR4, LPS immune receptor activity
   (GO:0001875). Decide whether ligand-class-specific MFs are needed or whether
   the generic term plus has_input in GO-CAM is the intended pattern (compare
   the *inflammasome sensor activity* proposal in the NLRP3 review).
4. **TIR-domain propagation.** TIR domains occur in adaptors, receptors and the
   NADase SARM1/TIR-1. Check whether InterPro2GO or IBA gives adaptor or
   receptor terms to TIR proteins that are enzymes, and vice versa.
5. **Interferon terms outside vertebrates.** IRFs and type I interferons are
   vertebrate-specific; check for type I interferon terms on invertebrate STING,
   cGLR or NF-kappaB orthologues.
6. **Expanded families.** With hundreds of TLR- and NACHT-domain entries in sea
   urchin and amphioxus, check what ligand-specific terms (e.g. TLR4 signaling)
   are propagated to lineage-specific paralogs that cannot share the ligand.
7. **Effectors versus participants.** Antimicrobial peptides and interferon
   effectors are outputs of these pathways; apply the substrate/output test in
   CLAUDE.md before accepting a signaling-pathway term on them.
8. **Recognition by a protease.** Horseshoe crab factor C recognises LPS and is
   itself the first protease of the cascade; record how GO represents this.

## Deliverables

1. Gene reviews for the candidate list, TLR axis first.
2. A per-family summary of what the reviews changed, by lineage.
3. Grounding of the five draft modules against the reviewed genes.
4. Term requests arising from questions 2, 3 and 8, if the reviews support
   them.

---

# STATUS

2026-09-30 — batch 1 (Toll/TLR axis) reviewed: 37 genes, all `status:
COMPLETE`, all passing `just validate`, each with a history record. 65 of 202
candidates now have reviews. Next: batch 2 (see below).

Accessions come from `scripts/resolve_candidates.py`, which queries UniProt by
primary gene name per taxon (Swiss-Prot preferred, then the reference-proteome
entry) or verifies an accession pinned in `candidates.tsv`; rerun it after
editing `candidates.tsv`. "TrEMBL" marks unreviewed entries.

## Batch 1 results

Actions per gene. "Rows" counts every annotation entry in the review: the
seeded GOA rows (exact duplicates in the GOA file are merged) plus the NEW
proposals added by the reviewer.

| Species | Gene | Accession | Rows | Accept | Keep non-core | Modify | Remove | Over-annot. | Undecided | New |
|---|---|---|---|---|---|---|---|---|---|---|
| human | TLR1 | Q15399 | 81 | 58 | 11 | 4 | 4 | 3 | 0 | 1 |
| human | TLR2 | O60603 | 146 | 86 | 21 | 8 | 20 | 9 | 1 | 1 |
| human | TLR3 | O15455 | 126 | 76 | 32 | 3 | 6 | 6 | 3 | 0 |
| human | TLR5 | O60602 | 33 | 28 | 2 | 2 | 0 | 0 | 1 | 0 |
| human | TLR6 | Q9Y2C9 | 120 | 70 | 32 | 8 | 6 | 4 | 0 | 0 |
| human | TLR7 | Q9NYK1 | 108 | 84 | 15 | 3 | 2 | 3 | 1 | 0 |
| human | TLR8 | Q9NR97 | 54 | 32 | 5 | 8 | 4 | 4 | 1 | 0 |
| human | TLR9 | Q9NR96 | 136 | 74 | 53 | 1 | 2 | 5 | 1 | 0 |
| human | TLR10 | Q9BXR5 | 41 | 21 | 12 | 2 | 4 | 0 | 0 | 2 |
| human | CD14 | P08571 | 151 | 93 | 47 | 6 | 4 | 1 | 0 | 0 |
| human | LY96 | Q9Y6Y9 | 104 | 59 | 32 | 10 | 3 | 0 | 0 | 0 |
| human | UNC93B1 | Q9H1C4 | 65 | 25 | 11 | 2 | 27 | 0 | 0 | 0 |
| human | MYD88 | Q99836 | 229 | 112 | 36 | 41 | 35 | 4 | 1 | 0 |
| human | TIRAP | P58753 | 109 | 41 | 29 | 19 | 15 | 4 | 1 | 0 |
| human | TICAM1 | Q8IUC6 | 120 | 91 | 13 | 8 | 7 | 1 | 0 | 0 |
| human | IRAK4 | Q9NWZ3 | 126 | 51 | 40 | 11 | 21 | 2 | 0 | 1 |
| mouse | Tlr11 | Q6R5P0 | 9 | 1 | 3 | 2 | 0 | 0 | 2 | 1 |
| mouse | Tlr12 | Q6QNU9 | 8 | 2 | 3 | 2 | 0 | 0 | 0 | 1 |
| mouse | Tlr13 | Q6R5N8 | 21 | 10 | 4 | 6 | 0 | 0 | 0 | 1 |
| DROME | spz | P48607 | 89 | 75 | 11 | 1 | 0 | 1 | 1 | 0 |
| DROME | Tl | P08953 | 104 | 73 | 21 | 4 | 3 | 1 | 2 | 0 |
| DROME | Toll-7 | Q7KIN0 | 24 | 18 | 4 | 0 | 0 | 0 | 2 | 0 |
| DROME | tub | P22812 | 55 | 38 | 1 | 10 | 4 | 0 | 1 | 1 |
| DROME | pll | Q05652 | 76 | 56 | 4 | 9 | 3 | 2 | 1 | 1 |
| DROME | cact | Q03017 | 47 | 33 | 5 | 4 | 3 | 0 | 2 | 0 |
| DROME | dl | P15330 | 114 | 79 | 20 | 6 | 7 | 0 | 0 | 2 |
| DROME | Dif | P98149 | 81 | 63 | 11 | 4 | 3 | 0 | 0 | 0 |
| CHICK | TLR15 | A0A8V0Z0H8 | 7 | 2 | 3 | 1 | 1 | 0 | 0 | 0 |
| CHICK | TLR21 | A0A8V0ZKW5 | 6 | 0 | 2 | 3 | 0 | 0 | 0 | 1 |
| DANRE | tlr5b | A0ACM8R384 | 5 | 1 | 2 | 2 | 0 | 0 | 0 | 0 |
| DANRE | tlr21 | F1QMN8 | 10 | 1 | 4 | 3 | 1 | 1 | 0 | 0 |
| DANRE | tlr22 | A0A2R8RTN4 | 4 | 1 | 1 | 1 | 0 | 0 | 1 | 0 |
| DROME | 18w | A1ZBR2 | 20 | 14 | 4 | 0 | 0 | 2 | 0 | 0 |
| DROME | Myd88 | A1Z7T8 | 32 | 25 | 2 | 1 | 3 | 1 | 0 | 0 |
| worm | tol-1 | Q9N5Z3 | 7 | 4 | 1 | 1 | 0 | 0 | 0 | 1 |
| human | TLR4 | O00206 | 275 | 145 | 72 | 5 | 30 | 22 | 1 | 0 |
| NEMVE | MyD88 | A7RHZ4 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 |
| **all** | **37 genes** | | **2748** | **1647** | **569** | **201** | **218** | **76** | **23** | **14** |

### Findings

- **Fly Toll-pathway term on human proteins.** GO:0008063 Toll signaling
  pathway is defined by ligand binding to "the receptor Toll", yet human IRAK4
  and MYD88 carry it by IBA (PAINT nodes PTN000701353 and PTN000386853, fly
  donors). Both reviews change it to GO:0002755 MyD88-dependent toll-like
  receptor signaling pathway and question the node placement. In the other
  direction, no fly Toll receptor carries a vertebrate TLR-pathway term;
  vertebrate-only terms were removed from fly Pelle and Tube (LPS-mediated
  signaling) and fly Myd88 (canonical NF-kappaB signaling, which GO defines as
  IKK-dependent; the fly Toll pathway uses no IKK).
- **Who recognises LPS.** TLR4 keeps GO:0001875 LPS immune receptor activity
  as its core function; MD-2 (LY96) binds lipid A and records the receptor
  activity as contributes_to; CD14 is changed to molecular carrier activity
  because it hands LPS on and cannot signal across the membrane. The same LPS
  term had also reached TLR1, TLR2 and TLR6, which recognise lipopeptides; it
  is modified to pattern recognition receptor activity on all three. The source
  is two GO-CAMs, 5fb9cc0600000727 (TLR1–TLR2) and 5fce9b7300000030
  (TLR2–TLR6): both type the receptor complex as LPS immune receptor activity
  although their own ligands are lipopeptides, and the GOA rows share their
  reference, curator and date. One term choice yields six gene annotations
  (three IDA rows plus three inferred LPS signaling rows). Both models now have
  `GoCamReview` files recording the receptor activity as WRONG and in CONFLICT
  with the gene reviews; GO has no lipopeptide immune receptor term, so the fix
  is GO:0038187 or a new term.
- **A recurring GOA citation error.** PMID:19593445, a prostate-cancer paper
  about BAD that never mentions TLRs, is cited for GO:0071260 cellular response
  to mechanical stimulus on TLR3, TLR4, TLR5, TLR7, TLR8 and MYD88. Each row is
  left UNDECIDED with the reference flagged. A second mis-citation,
  PMID:23382219 (a sorting-nexin structure paper), supports a TLR7 row.
- **Mouse Tlr11/Tlr12 names are swapped** between the literature and
  MGI/UniProt (verified via RefSeq NP_991388.1); the numbered pathway terms are
  therefore not assigned to either entry. See the TLR family sub-page.
- **Wrong chemistry and wrong compartments.** GO:0070305 response to cGMP on
  TLR7 is changed to guanosine binding: the TLR7 ligand is 2',3'-cGMP, not the
  3',5' isomer the term covers (GO has no 2',3'-cGMP term). TLR8 endolysosome
  rows are moved to early endosome membrane, and TLR3, TLR7, TLR8 and TLR9
  plasma-membrane IBA rows are demoted because these receptors signal from
  endosomes.
- **Participation test.** UNC93B1, the trafficking chaperone for endosomal
  TLRs, keeps its TLR-pathway rows only as non-core; its core function is
  protein carrier chaperone activity. Spätzle carries no processing term
  (FlyBase puts those on the proteases). A Dif salivary-gland cell-death IMP
  row is removed because its own paper reports no phenotype in Rel-family null
  mutants.
- **Mouse-sourced errors.** Histone chaperone and chromatin remodeling IEA rows
  on MYD88 came from a mouse annotation of a paper showing only that MyD88
  signaling is needed for nucleosome remodeling; removed here, and the mouse
  source annotation needs the same fix.
- **Twelve NEW annotations in the first pass** (two more came from the deep-research cross-check below), each checked against the participation and
  comparator tests, including IkappaB kinase activity for fly Pelle (Pelle
  itself phosphorylates Cactus), negative regulation of toll-like receptor
  signaling for TLR10, triacyl and diacyl lipopeptide binding for TLR1 and
  TLR2, and signaling adaptor activity for fly Tube and human IRAK4.

### Deep-research cross-check

Most reviews were written before their Falcon deep-research report arrived, so
each was later compared against its report. A report claim could change a
review only after it was verified in a primary paper and quoted from it. The
reports largely agreed with the reviews. Across 37 genes the pass changed no
existing action and added two NEW annotations, both verified and
comparator-checked: positive regulation of interferon-beta production on
chicken TLR21 (PMID:37951324; human and mouse TLR9 carry the term) and defense
response to Gram-positive bacterium on mouse Tlr13 (PMID:32209688,
PMID:38358825; mouse `Tlr2` carries it). Other changes were to descriptions and
supporting references, for example correcting the relationship between worm
TOL-1 and IKB-1 (IKB-1 opposes TOL-1; PMID:26279230). Several report claims
were rejected because cached primary papers contradict them (e.g. that
Spätzle binds Toll with low affinity, that TLR5 and TLR6 signal only through
MyD88, and that TLR4 binds amyloid-beta directly). Reviews whose report adds
nothing citable keep a validator warning that the deep-research file is not
cited; the Tlr11 and Tlr12 reports use the swapped literature names, so they
are deliberately not cited.

## Batch 2 (proposed)

The Drosophila recognition and Imd modules (PGRP-SA, PGRP-SD, GNBP1, GNBP3,
modSP, Grass, SPE, psh, nec; PGRP-LC, PGRP-LE, imd, Fadd, Dredd, Diap2, Tak1,
Tab2, IKKbeta, key, Rel), the remaining human TLR-axis genes (LBP, TICAM2, IRAK1, IRAK2,
MAP3K7, TAB1, TAB2; TRAF3, TRAF6 and TBK1 are already reviewed) and the zebrafish/chicken TLRs not
yet covered (`tlr3`, `tlr4ba`, `tlr5a`, `tlr18`, `tlr19.1`, `tlr20.2`; chicken `TLR3`, `TLR4`,
`TLR7`).

## Full checklist by module

### Toll-like receptor signaling (29/51 reviewed)

- [x] human: TLR1 (Q15399)
- [x] human: TLR2 (O60603)
- [x] human: TLR3 (O15455)
- [x] human: TLR4 (O00206)
- [x] human: TLR5 (O60602)
- [x] human: TLR6 (Q9Y2C9)
- [x] human: TLR7 (Q9NYK1)
- [x] human: TLR8 (Q9NR97)
- [x] human: TLR9 (Q9NR96)
- [x] human: TLR10 (Q9BXR5)
- [x] human: CD14 (P08571)
- [x] human: LY96 (Q9Y6Y9)
- [ ] human: LBP (P18428)
- [x] human: UNC93B1 (Q9H1C4)
- [x] human: MYD88 (Q99836)
- [x] human: TIRAP (P58753)
- [x] human: TICAM1 (Q8IUC6)
- [ ] human: TICAM2 (Q86XR7)
- [ ] human: SARM1 (Q6SZW1)
- [ ] human: IRAK1 (P51617)
- [ ] human: IRAK2 (O43187)
- [x] human: IRAK3 (Q9Y616)
- [x] human: IRAK4 (Q9NWZ3)
- [x] human: TRAF3 (Q13114)
- [x] human: TRAF6 (Q9Y4K3)
- [x] mouse: Tlr11 (Q6R5P0)
- [x] mouse: Tlr12 (Q6QNU9)
- [x] mouse: Tlr13 (Q6R5N8)
- [ ] mouse: `Tlr4` (Q9QUK6)
- [x] CHICK: TLR15 (A0A8V0Z0H8, TrEMBL)
- [x] CHICK: TLR21 (A0A8V0ZKW5, TrEMBL)
- [ ] CHICK: `TLR3` (A0A8V0YT51, TrEMBL)
- [ ] CHICK: `TLR4` (C4PCF3, TrEMBL)
- [ ] CHICK: `TLR7` (A0A1L4FML6, TrEMBL)
- [ ] CHICK: `MYD88` (A5HNF6)
- [ ] DANRE: `tlr3` (A0A8M1N4E3, TrEMBL)
- [ ] DANRE: `tlr4ba` (A0A8M3B7X7, TrEMBL)
- [ ] DANRE: `tlr5a` (F8W4F1, TrEMBL)
- [x] DANRE: tlr5b (A0ACM8R384, TrEMBL)
- [x] DANRE: tlr22 (A0A2R8RTN4, TrEMBL)
- [x] DANRE: tlr21 (F1QMN8, TrEMBL)
- [ ] DANRE: `tlr18` (A3KH14, TrEMBL)
- [ ] DANRE: `tlr19.1` (A0A8M1RKQ4, TrEMBL)
- [ ] DANRE: `tlr20.2` (F1QRG0, TrEMBL)
- [ ] DANRE: `myd88` (Q5XJ85)
- [ ] DANRE: `ticam1` (A0A8M1N991, TrEMBL)
- [ ] DANRE: `irak4` (A0AC58IUN4, TrEMBL)
- [ ] DANRE: `traf6` (Q6IWL4)
- [ ] XENTR: `myd88` (Q28DJ2)
- [ ] XENTR: `tlr5` (A0A803K1J2, TrEMBL)
- [x] NEMVE: MyD88 (A7RHZ4, TrEMBL)

### NF-kappaB / IRF output (3/17 reviewed)

- [ ] human: MAP3K7 (O43318)
- [ ] human: TAB1 (Q15750)
- [ ] human: TAB2 (Q9NYJ8)
- [ ] human: CHUK (O15111)
- [ ] human: IKBKB (O14920)
- [ ] human: IKBKG (Q9Y6K9)
- [x] human: TBK1 (Q9UHD2)
- [ ] human: IKBKE (Q14164)
- [ ] human: RELA (Q04206)
- [ ] human: NFKB1 (P19838)
- [ ] human: NFKBIA (P25963)
- [ ] human: IRF3 (Q14653)
- [ ] human: IRF5 (Q13568)
- [ ] human: IRF7 (Q92985)
- [x] human: TOLLIP (Q9H0E2)
- [x] human: TNFAIP3 (P21580)
- [ ] NEMVE: `NF-kappaB` (A7UNT2, TrEMBL)

### Drosophila Toll pathway (10/19 reviewed)

- [ ] DROME: `PGRP-SA` (Q9VYX7)
- [ ] DROME: `PGRP-SD` (Q9VS97)
- [ ] DROME: `GNBP1` (Q9NHB0)
- [ ] DROME: `GNBP3` (Q9NHA8)
- [ ] DROME: `modSP` (Q9VER6)
- [ ] DROME: `Grass` (Q9VB68)
- [ ] DROME: `SPE` (Q9VCJ8)
- [ ] DROME: `psh` (Q9VWU1)
- [ ] DROME: `nec` (A1Z6V7, TrEMBL)
- [x] DROME: spz (P48607)
- [x] DROME: Tl (P08953)
- [x] DROME: 18w (A1ZBR2, TrEMBL)
- [x] DROME: Toll-7 (Q7KIN0)
- [x] DROME: Myd88 (A1Z7T8, TrEMBL)
- [x] DROME: tub (P22812)
- [x] DROME: pll (Q05652)
- [x] DROME: cact (Q03017)
- [x] DROME: dl (P15330)
- [x] DROME: Dif (P98149)

### Drosophila Imd pathway (0/11 reviewed)

- [ ] DROME: `PGRP-LC` (Q9GNK5)
- [ ] DROME: `PGRP-LE` (Q9VXN9)
- [ ] DROME: `imd` (Q7K4Z4)
- [ ] DROME: `Fadd` (Q9V3B4)
- [ ] DROME: `Dredd` (Q8IRY7)
- [ ] DROME: `Diap2` (Q24307)
- [ ] DROME: `Tak1` (Q9V3Q6)
- [ ] DROME: `Tab2` (A0A0B4KG87, TrEMBL)
- [ ] DROME: `IKKbeta` (Q9VEZ5)
- [ ] DROME: `key` (Q9GYV5)
- [ ] DROME: `Rel` (Q94527)

### C. elegans p38 PMK-1 pathway (9/10 reviewed)

- [x] worm: tol-1 (Q9N5Z3, TrEMBL)
- [x] worm: tir-1 (Q86DA5)
- [x] worm: nsy-1 (Q21029)
- [x] worm: sek-1 (G5EDF7)
- [x] worm: pmk-1 (Q17446)
- [x] worm: atf-7 (Q86MD3)
- [ ] worm: `dkf-2` (O45818)
- [x] worm: nipi-3 (G5EED4)
- [x] worm: zip-2 (Q21148)
- [x] worm: fshr-1 (L8EC40, TrEMBL)

### C. elegans epidermal/TGF-beta immunity (3/4 reviewed)

- [x] worm: dbl-1 (G5EEL5)
- [ ] worm: `sma-3` (P45896)
- [x] worm: sta-2 (Q20977)
- [x] worm: nlp-29 (O44664)

### NLR signaling and inflammasomes (3/24 reviewed)

- [ ] human: NOD1 (Q9Y239)
- [ ] human: NOD2 (Q9HC29)
- [ ] human: NLRP1 (Q9C000)
- [x] human: NLRP3 (Q96P20)
- [ ] human: NLRC4 (Q9NPP4)
- [ ] human: NAIP (Q13075)
- [ ] human: NLRP6 (P59044)
- [ ] human: CARD8 (Q9Y2G2)
- [ ] human: RIPK2 (O43353)
- [ ] human: PYCARD (Q9ULZ3)
- [ ] human: AIM2 (O14862)
- [ ] human: `CASP1` (P29466)
- [x] human: CASP4 (P49662)
- [x] human: GSDMD (P57764)
- [ ] human: IL1B (P01584)
- [ ] human: IL18 (Q14116)
- [ ] mouse: `Naip5` (Q9R016)
- [ ] mouse: `Nlrp1b` (A1Z198)
- [ ] mouse: `Nlrc4` (Q3UP24)
- [ ] DANRE: `nod1` (A0A8M1RMD1, TrEMBL)
- [ ] DANRE: `nod2` (A0A8M1P9S9, TrEMBL)
- [ ] DANRE: `pycard` (Q9I9N6)
- [ ] DANRE: `caspa` (Q9I9L7)
- [ ] DANRE: `caspb` (Q504J1)

### Cytosolic nucleic-acid sensing (4/23 reviewed)

- [ ] human: RIGI (O95786)
- [x] human: IFIH1 (Q9BYX4)
- [ ] human: DHX58 (Q96C10)
- [ ] human: MAVS (Q7Z434)
- [ ] human: TRIM25 (Q14258)
- [ ] human: CGAS (Q8N884)
- [x] human: STING1 (Q86WV6)
- [x] human: ZBP1 (Q9H171)
- [x] human: IFI16 (Q16666)
- [ ] CHICK: `IFIH1` (A0A1D5P5I0, TrEMBL)
- [ ] CHICK: `MAVS` (A0A8V0YPL4, TrEMBL)
- [ ] CHICK: `STING1` (E1C7U0)
- [ ] CHICK: `CGAS` (A0A8V0X930, TrEMBL)
- [ ] DANRE: `rigi` (A0A8M1P6Y9, TrEMBL)
- [ ] DANRE: `mavs` (B8A4W7, TrEMBL)
- [ ] DANRE: `sting1` (E7F4N7)
- [ ] DANRE: `cgasa` (F1QCP4, TrEMBL)
- [ ] DROME: `cGlr1` (A1ZA55)
- [ ] DROME: `cGlr2` (A8DYP7)
- [ ] DROME: `Sting` (A0A0B4LFY9)
- [ ] worm: `drh-1` (G5EDI8, TrEMBL)
- [ ] NEMVE: `STING` (A7SLZ2)
- [ ] NEMVE: `cGAS` (A7SFB5)

### C-type lectin receptors (0/5 reviewed)

- [ ] human: CLEC7A (Q9BXN2)
- [ ] human: CLEC4E (Q9ULY5)
- [ ] human: CD209 (Q9NNX6)
- [ ] human: SYK (P43405)
- [ ] human: CARD9 (Q9H257)

### Complement and soluble PRRs (2/12 reviewed)

- [x] human: MBL2 (P11226)
- [ ] human: FCN2 (Q15485)
- [ ] human: MASP2 (O00187)
- [ ] human: C3 (P01024)
- [ ] human: PGLYRP1 (O75594)
- [ ] human: PGLYRP2 (Q96PD5)
- [ ] DROME: `Tep1` (Q7KT66, TrEMBL)
- [ ] DROME: `Tep2` (Q8IPH5, TrEMBL)
- [x] ANOGA: TEP1 (Q9GYW4)
- [ ] ANOGA: `LRIM1` (A7XBG8, TrEMBL)
- [ ] ANOGA: `APL1C` (L7T8J3, TrEMBL)
- [ ] ANOGA: `REL2` (B2FXG9, TrEMBL)

### Horseshoe crab coagulation cascade (0/6 reviewed)

- [ ] TACTR: `factor C` (P28175)
- [ ] TACTR: `factor B` (Q27081)
- [ ] TACTR: `factor G alpha` (Q27082)
- [ ] TACTR: `factor G beta` (Q27083)
- [ ] TACTR: `proclotting enzyme` (P21902)
- [ ] TACTR: `coagulogen` (P02681)

### Drosophila JAK-STAT (0/4 reviewed)

- [ ] DROME: `hop` (Q24592)
- [ ] DROME: `Stat92E` (Q24151)
- [ ] DROME: `upd3` (Q59E38, TrEMBL)
- [ ] DROME: `TotA` (Q8IN44)

### Interferon effectors (0/4 reviewed)

- [ ] human: OAS1 (P00973)
- [ ] human: RNASEL (Q05823)
- [ ] human: EIF2AK2 (P19525)
- [ ] human: MX1 (P20591)

### Antimicrobial effectors (2/12 reviewed)

- [ ] human: DEFB4A (O15263)
- [ ] human: CAMP (P49913)
- [ ] human: LYZ (P61626)
- [ ] DROME: `Drs` (P41964)
- [ ] DROME: `DptA` (P24492)
- [ ] DROME: `Mtk` (Q24395)
- [ ] DROME: `AttA` (P45884)
- [ ] DROME: `CecA1` (C0HKQ7)
- [ ] DROME: `Def` (P36192)
- [x] worm: clec-60 (Q23564, TrEMBL)
- [x] worm: lys-7 (O16202)
- [ ] worm: `spp-1` (Q22291, TrEMBL)

# NOTES

## 2026-09-30

- Created the project page, the candidate list and the resolver script.
- The resolver first matched synonyms (mouse `Tlr11` resolved to the `TLR12`
  entry; chicken TLR15 to a "Toll-like receptor 2" record); it now requires
  a primary gene-name match. Zebrafish symbols were corrected to the current
  UniProt names (`cgasa`, `tlr19.1`, `tlr20.2`). No *X. tropicalis* `tlr4` entry was
  found, so it was dropped.
- Chicken TLR15 still resolves to a TrEMBL entry whose protein name reads
  "Toll-like receptor 2" (Q2XQ10, primary gene TLR15); another TLR15 entry
  (E5L3Q3) is named "Toll-like receptor 15". Pick deliberately before fetching.
- No Nematostella entry is named as a Toll-like receptor, although 17 carry a
  TIR domain; no accession is asserted for it.

## 2026-09-30 — batch 1

- Reviewed the 37 batch-1 genes with 21 parallel reviewer agents, each
  following the annotation-reviewer skill; every review validates and has a
  history record.
- Falcon deep research was unreliable: the wrapper's default 600 s timeout
  killed most first attempts, the perplexity-lite fallback has no key in this
  environment, and some Edison calls returned "no answer". A rerun with a
  2,700 s timeout and one Falcon retry produced reports for 36 genes; the Asta
  fallback returned unrelated papers for LY96 and was not used. Reviews were
  written from UniProt and cached primary papers, and a second pass
  cross-checked each finished review against its report once it arrived.
- Accessions: the resolver now prefers reference-proteome entries (fly Myd88
  is A1Z7T8, zebrafish tlr5b A0ACM8R384); chicken TLR15 (A0A8V0Z0H8) and TLR21
  (A0A8V0ZKW5) are pinned to the entry GOA annotates most.
- `just validate-references` prints "Total checks: 0" on clean files; it
  counts issues, not checks. An invented quote does fail it, so quote checking
  works.
