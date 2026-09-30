---
title: "Innate Immune System Pathways Across Animals"
maturity: SCOPING
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
sea anemone to human. It is scoped, not yet started: a candidate list of
**202 gene products** with UniProt accessions resolved programmatically
([candidates-resolved.tsv](INNATE_IMMUNITY/candidates-resolved.tsv)) is in
place, and **28 already have complete reviews** from other projects (14 human,
13 *C. elegans*, 1 *Anopheles*; 2,387 existing annotations between them). None
of the Toll-like receptors themselves, none of the Drosophila Toll or Imd
pathway genes and none of the non-human vertebrate genes have been reviewed.
The first batch is the TLR axis (see [TLR family sub-page](INNATE_IMMUNITY/TLR_FAMILY.md)).

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
| mouse | *Mus musculus* | Mammalia | Rodent-specific TLR11/12/13; NAIP/NLRC4 and NLRP1B genetics |
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
including the lineage-specific TLR11, 12, 13, 15 and 21, but none for fish TLR22.
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
| 60418ffa00001019 | NLRP3 inflammasome in pyroptosis via nlrp3, caspa, caspb etc. (zebrafish) |
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

2026-09-30 — scoped. 202 candidates, 28 reviewed (from other projects).
Accessions come from `scripts/resolve_candidates.py`, which queries UniProt by
primary gene name per taxon (Swiss-Prot preferred) or verifies a pinned
accession; rerun it after editing `candidates.tsv`. "TrEMBL" marks
unreviewed entries, where the chosen accession is the highest annotation-score
hit and should be checked before `just fetch-gene`. Species codes NEMVE and
TACTR have no gene folders yet; for those, the accession is the folder name.

## Batch 1: TLR axis (priority)

Human TLR1–TLR10 with CD14, LY96, MYD88, TIRAP, TICAM1, IRAK4 and UNC93B1;
mouse Tlr11, Tlr12, Tlr13; chicken TLR15, TLR21; zebrafish tlr5b, tlr21,
tlr22; Drosophila spz, Tl, 18w, Toll-7, Myd88, tub, pll, cact, dl, Dif;
*C. elegans* tol-1; Nematostella MyD88.

## Full checklist by module

### Toll-like receptor signaling (3/51 reviewed)

- [ ] human: TLR1 (Q15399)
- [ ] human: TLR2 (O60603)
- [ ] human: TLR3 (O15455)
- [ ] human: TLR4 (O00206)
- [ ] human: TLR5 (O60602)
- [ ] human: TLR6 (Q9Y2C9)
- [ ] human: TLR7 (Q9NYK1)
- [ ] human: TLR8 (Q9NR97)
- [ ] human: TLR9 (Q9NR96)
- [ ] human: TLR10 (Q9BXR5)
- [ ] human: CD14 (P08571)
- [ ] human: LY96 (Q9Y6Y9)
- [ ] human: LBP (P18428)
- [ ] human: UNC93B1 (Q9H1C4)
- [ ] human: MYD88 (Q99836)
- [ ] human: TIRAP (P58753)
- [ ] human: TICAM1 (Q8IUC6)
- [ ] human: TICAM2 (Q86XR7)
- [ ] human: SARM1 (Q6SZW1)
- [ ] human: IRAK1 (P51617)
- [ ] human: IRAK2 (O43187)
- [x] human: IRAK3 (Q9Y616)
- [ ] human: IRAK4 (Q9NWZ3)
- [x] human: TRAF3 (Q13114)
- [x] human: TRAF6 (Q9Y4K3)
- [ ] mouse: Tlr11 (Q6R5P0)
- [ ] mouse: Tlr12 (Q6QNU9)
- [ ] mouse: Tlr13 (Q6R5N8)
- [ ] mouse: Tlr4 (Q9QUK6)
- [ ] CHICK: TLR15 (Q2XQ10, TrEMBL)
- [ ] CHICK: TLR21 (A0A8V0ZYL3, TrEMBL)
- [ ] CHICK: TLR3 (A0A8V0YT51, TrEMBL)
- [ ] CHICK: TLR4 (C4PCF3, TrEMBL)
- [ ] CHICK: TLR7 (A0A1L4FML6, TrEMBL)
- [ ] CHICK: MYD88 (A5HNF6)
- [ ] DANRE: tlr3 (Q32PW5, TrEMBL)
- [ ] DANRE: tlr4ba (A0A8M3B7X7, TrEMBL)
- [ ] DANRE: tlr5a (F8W4F1, TrEMBL)
- [ ] DANRE: tlr5b (F8W3J5, TrEMBL)
- [ ] DANRE: tlr22 (A0A2R8RTN4, TrEMBL)
- [ ] DANRE: tlr21 (F1QMN8, TrEMBL)
- [ ] DANRE: tlr18 (A3KH14, TrEMBL)
- [ ] DANRE: tlr19.1 (A0A8M1RKQ4, TrEMBL)
- [ ] DANRE: tlr20.2 (F1QRG0, TrEMBL)
- [ ] DANRE: myd88 (Q5XJ85)
- [ ] DANRE: ticam1 (Q1LUQ2, TrEMBL)
- [ ] DANRE: irak4 (A0AC58IUN4, TrEMBL)
- [ ] DANRE: traf6 (Q6IWL4)
- [ ] XENTR: myd88 (Q28DJ2)
- [ ] XENTR: tlr5 (A0A803K1J2, TrEMBL)
- [ ] NEMVE: MyD88 (A7RHZ4, TrEMBL)

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
- [ ] NEMVE: NF-kappaB (A7UNT2, TrEMBL)

### Drosophila Toll pathway (0/19 reviewed)

- [ ] DROME: PGRP-SA (Q9VYX7)
- [ ] DROME: PGRP-SD (Q9VS97)
- [ ] DROME: GNBP1 (Q9NHB0)
- [ ] DROME: GNBP3 (Q9NHA8)
- [ ] DROME: modSP (Q9VER6)
- [ ] DROME: Grass (Q9VB68)
- [ ] DROME: SPE (Q9VCJ8)
- [ ] DROME: psh (Q9VWU1)
- [ ] DROME: nec (Q7JWX3, TrEMBL)
- [ ] DROME: spz (P48607)
- [ ] DROME: Tl (P08953)
- [ ] DROME: 18w (A1ZBR2, TrEMBL)
- [ ] DROME: Toll-7 (Q7KIN0)
- [ ] DROME: Myd88 (Q7K105, TrEMBL)
- [ ] DROME: tub (P22812)
- [ ] DROME: pll (Q05652)
- [ ] DROME: cact (Q03017)
- [ ] DROME: dl (P15330)
- [ ] DROME: Dif (P98149)

### Drosophila Imd pathway (0/11 reviewed)

- [ ] DROME: PGRP-LC (Q9GNK5)
- [ ] DROME: PGRP-LE (Q9VXN9)
- [ ] DROME: imd (Q7K4Z4)
- [ ] DROME: Fadd (Q9V3B4)
- [ ] DROME: Dredd (Q8IRY7)
- [ ] DROME: Diap2 (Q24307)
- [ ] DROME: Tak1 (Q9V3Q6)
- [ ] DROME: Tab2 (A0A0B4KG87, TrEMBL)
- [ ] DROME: IKKbeta (Q9VEZ5)
- [ ] DROME: key (Q9GYV5)
- [ ] DROME: Rel (Q94527)

### C. elegans p38 PMK-1 pathway (8/10 reviewed)

- [ ] worm: tol-1 (Q9N5Z3, TrEMBL)
- [x] worm: tir-1 (Q86DA5)
- [x] worm: nsy-1 (Q21029)
- [x] worm: sek-1 (G5EDF7)
- [x] worm: pmk-1 (Q17446)
- [x] worm: atf-7 (Q86MD3)
- [ ] worm: dkf-2 (O45818)
- [x] worm: nipi-3 (G5EED4)
- [x] worm: zip-2 (Q21148)
- [x] worm: fshr-1 (L8EC40, TrEMBL)

### C. elegans epidermal/TGF-beta immunity (3/4 reviewed)

- [x] worm: dbl-1 (G5EEL5)
- [ ] worm: sma-3 (P45896)
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
- [ ] mouse: Naip5 (Q9R016)
- [ ] mouse: Nlrp1b (A1Z198)
- [ ] mouse: Nlrc4 (Q3UP24)
- [ ] DANRE: nod1 (A0A8M1RMD1, TrEMBL)
- [ ] DANRE: nod2 (A0A8M1P9S9, TrEMBL)
- [ ] DANRE: pycard (Q9I9N6)
- [ ] DANRE: caspa (Q9I9L7)
- [ ] DANRE: caspb (Q504J1)

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
- [ ] CHICK: IFIH1 (A0A1D5P5I0, TrEMBL)
- [ ] CHICK: MAVS (A0A8V0YPL4, TrEMBL)
- [ ] CHICK: STING1 (E1C7U0)
- [ ] CHICK: CGAS (A0A8V0X930, TrEMBL)
- [ ] DANRE: rigi (A0A0D5W690, TrEMBL)
- [ ] DANRE: mavs (B8A4W7, TrEMBL)
- [ ] DANRE: sting1 (E7F4N7)
- [ ] DANRE: cgasa (F1QCP4, TrEMBL)
- [ ] DROME: cGlr1 (A1ZA55)
- [ ] DROME: cGlr2 (A8DYP7)
- [ ] DROME: Sting (A0A0B4LFY9)
- [ ] worm: drh-1 (G5EDI8, TrEMBL)
- [ ] NEMVE: STING (A7SLZ2)
- [ ] NEMVE: cGAS (A7SFB5)

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
- [ ] ANOGA: LRIM1 (A7XBG8, TrEMBL)
- [ ] ANOGA: APL1C (L7T8J3, TrEMBL)
- [ ] ANOGA: REL2 (B2FXG9, TrEMBL)

### Horseshoe crab coagulation cascade (0/6 reviewed)

- [ ] TACTR: factor C (P28175)
- [ ] TACTR: factor B (Q27081)
- [ ] TACTR: factor G alpha (Q27082)
- [ ] TACTR: factor G beta (Q27083)
- [ ] TACTR: proclotting enzyme (P21902)
- [ ] TACTR: coagulogen (P02681)

### Drosophila JAK-STAT (0/4 reviewed)

- [ ] DROME: hop (Q24592)
- [ ] DROME: Stat92E (Q24151)
- [ ] DROME: upd3 (Q59E38, TrEMBL)
- [ ] DROME: TotA (Q8IN44)

### Interferon effectors (0/4 reviewed)

- [ ] human: OAS1 (P00973)
- [ ] human: RNASEL (Q05823)
- [ ] human: EIF2AK2 (P19525)
- [ ] human: MX1 (P20591)

### Antimicrobial effectors (2/12 reviewed)

- [ ] human: DEFB4A (O15263)
- [ ] human: CAMP (P49913)
- [ ] human: LYZ (P61626)
- [ ] DROME: Drs (P41964)
- [ ] DROME: DptA (P24492)
- [ ] DROME: Mtk (Q24395)
- [ ] DROME: AttA (P45884)
- [ ] DROME: CecA1 (C0HKQ7)
- [ ] DROME: Def (P36192)
- [x] worm: clec-60 (Q23564, TrEMBL)
- [x] worm: lys-7 (O16202)
- [ ] worm: spp-1 (Q22291, TrEMBL)

# NOTES

## 2026-09-30

- Created the project page, the candidate list and the resolver script.
- The resolver first matched synonyms (mouse Tlr11 resolved to the TLR12
  entry; chicken TLR15 to a "Toll-like receptor 2" record); it now requires
  a primary gene-name match. Zebrafish symbols were corrected to the current
  UniProt names (cgasa, tlr19.1, tlr20.2). No *X. tropicalis* tlr4 entry was
  found, so it was dropped.
- Chicken TLR15 still resolves to a TrEMBL entry whose protein name reads
  "Toll-like receptor 2" (Q2XQ10, primary gene TLR15); another TLR15 entry
  (E5L3Q3) is named "Toll-like receptor 15". Pick deliberately before fetching.
- No Nematostella entry is named as a Toll-like receptor, although 17 carry a
  TIR domain; no accession is asserted for it.
