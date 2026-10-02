---
title: "Plant-Fungal Interactions"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [ARATH, ORYSJ, HORVU, SOLLC, MEDTR, LOTJA, PYRO7, FULFL, MYCMD, GIBZE]
genes: [CERK1, LYK5, LYM2, SYP121, BGLU26, ABCG36, CYP71B15, CYP79B2, MLO2, WRKY33, ERF094, MPK3, CEBIP, PIKM1-TS, RGA4, RGA5, MLO, NORK, DMI1, CASTOR, CYCLOPS, RAM1, STR, PT4, PWL2, BAS1, slp1, PMK1, MPG1, AVR9, AVR4, ECP6, CMU1, PIT2, See1, TRI5]
---

# Plant-Fungal Interactions

**Bottom line:** This project will review the GO annotations on genes from
both sides of plant-fungal interactions. On the plant side that means chitin
perception, penetration resistance, camalexin, NLR recognition of fungal
effectors and arbuscular mycorrhizal symbiosis. On the fungal side it means
secreted effectors, the appressorium machinery and toxins. The project is at
the scoping stage. A first list of 36 new genes in 10 species is below, each
checked against a reviewed UniProt entry. Thirteen related reviews already in
the repo (mostly *Arabidopsis* immune signalling and legume symbiosis) are listed for cross-checking.
No new reviews have been started yet.

The main reason to group these genes is that GO describes the interaction from
two directions. Plant genes carry terms such as `defense response to fungus`,
while fungal genes carry the multi-organism terms for symbionts, such as
effector-mediated suppression of host defenses or modulation of host processes.
Reviewing both partners together tests whether the two sides are annotated
consistently. It also tests whether mutant phenotypes on a pathogen, which only
show that a gene is needed, get turned into process annotations that claim the
gene does part of the work (see the `NEW` guidance in `CLAUDE.md`).

**Project Start Date:** 2026-10-02
**Organisms:** *Arabidopsis thaliana*, rice, barley, tomato, *Medicago truncatula*,
*Lotus japonicus*, *Pyricularia oryzae* (rice blast), *Fulvia fulva* (tomato leaf
mould), *Ustilago maydis* (corn smut), *Fusarium graminearum* (head blight)

## Scope

In scope:

- **Plant perception of fungal molecules (PTI):** chitin receptor complexes
  (CEBiP/LYM2, CERK1, LYK5) and their immediate signalling outputs.
- **Penetration and post-invasion resistance:** the PEN1/PEN2/PEN3 pathways,
  MLO susceptibility genes, and tryptophan-derived phytoalexins (camalexin).
- **Recognition of fungal effectors (ETI):** NLRs and receptor-like proteins
  that recognise fungal avirulence proteins, reviewed in pairs with their
  effectors where possible (RGA4/RGA5 with blast AVRs; Cf-9 with Avr9).
- **Arbuscular mycorrhizal symbiosis:** the common symbiosis signalling pathway
  (SYMRK, CASTOR/POLLUX/DMI1, CCaMK, CYCLOPS) and arbuscule-specific genes.
- **Fungal virulence factors:** secreted effectors (LysM chitin-masking
  effectors, translocated effectors, enzyme effectors), appressorium
  development, and mycotoxins.

Out of scope for now: oomycetes (not fungi), bacterial-only PRRs such as FLS2
and EFR (already reviewed), and generic hormone signalling that is not specific
to fungal interactions.

## Curation questions

1. **Multi-organism process terms on effectors.** Do the effector annotations
   use the symbiont-side terms (e.g. effector-mediated suppression of host
   pattern-triggered immunity) rather than plant-side `defense response` terms?
   Are they backed by experiments on the effector itself, or only by IEA from
   domain mappings?
2. **LysM effectors vs LysM receptors.** ECP6, Slp1, CEBiP and LYM2 all bind
   chitin. Check that the effectors are annotated for chitin binding and
   chitin-triggered immunity suppression, and the receptors for chitin
   perception and signalling, without the two sets of terms leaking into each
   other through InterPro2GO.
3. **Necessity vs participation.** Many plant genes (e.g. MLO, PEN genes,
   PAD3) are defined by infection phenotypes. Check whether `defense response
   to fungus` rows are justified, and where a more mechanistic term
   (e.g. camalexin biosynthesis, exocytosis) is the real core function.
4. **Symbiosis vs defense.** CERK1 orthologues in rice and *Medicago* work in
   both chitin immunity and mycorrhizal signalling. Check that annotations keep
   the two roles distinct.
5. **Sensor/helper NLR pairs.** RGA5 (sensor, binds AVR-Pia/AVR1-CO39 through an
   integrated HMA domain) and RGA4 (executor) should not end up with identical
   annotations.

---

# STATUS

Last updated: 2026-10-02

## Existing reviews to cross-check (not re-reviewed here)

These reviews already exist in `genes/` and overlap with this project's scope.
They are listed so new reviews stay consistent with them.

- [x] ARATH/CERK1: chitin co-receptor kinase
- [x] ARATH/BAK1, ARATH/BIK1: PRR co-receptor and receptor-like cytoplasmic kinase
- [x] ARATH/RBOHD: apoplastic ROS burst
- [x] ARATH/MPK6: MAPK cascade downstream of chitin perception
- [x] ARATH/EDS1, ARATH/PAD4: TIR-NLR signalling and resistance to biotrophic fungi
- [x] ARATH/COI1, ARATH/JAZ1, ARATH/EIN2: JA/ET defense against necrotrophic fungi
- [x] ORYSJ/CCAMK: common symbiosis signalling kinase
- [x] MEDTR/NSP1, MEDTR/NFP: symbiosis transcription factor and Nod factor receptor

## New reviews

UniProt accessions below were looked up in UniProtKB/Swiss-Prot (reviewed
entries) on 2026-10-02. Species codes are UniProt mnemonics.

### Tier 1: Chitin perception and penetration resistance (plant)

- [ ] ARATH/LYK5 (O22808): main chitin-binding LysM receptor kinase, partners CERK1
- [ ] ARATH/LYM2 (O23006): GPI-anchored CEBiP homologue, plasmodesmal chitin response
- [ ] ORYSJ/CEBIP (Q8H8C7): rice chitin elicitor-binding protein
- [ ] ORYSJ/CERK1 (A0A0P0XII1): rice chitin receptor kinase, also needed for AM symbiosis
- [ ] ARATH/SYP121 (Q9ZSD4): PEN1 syntaxin, focal secretion at penetration sites
- [ ] ARATH/BGLU26 (O64883): PEN2 myrosinase, indole glucosinolate hydrolysis
- [ ] ARATH/ABCG36 (Q9XIE2): PEN3 ABC transporter
- [ ] ARATH/MLO2 (Q9SXB6): powdery mildew susceptibility gene
- [ ] HORVU/MLO (P93766): barley *Mlo*, the original powdery mildew susceptibility gene

### Tier 2: Defense outputs (plant)

- [ ] ARATH/CYP79B2 (O81346): tryptophan N-monooxygenase, entry step to camalexin and indole glucosinolates
- [ ] ARATH/CYP71B15 (Q9LW27): PAD3 camalexin synthase
- [ ] ARATH/WRKY33 (Q8S8P5): transcription factor for camalexin and anti-*Botrytis* defense
- [ ] ARATH/MPK3 (Q39023): MAPK that phosphorylates WRKY33
- [ ] ARATH/ERF094 (Q9LND1): ORA59, JA/ET integrator for necrotroph defense

### Tier 3: Recognition of fungal effectors (plant NLRs)

- [ ] ORYSJ/RGA5 (F7J0N2): sensor NLR with integrated HMA domain, recognises AVR-Pia and AVR1-CO39
- [ ] ORYSJ/RGA4 (F7J0M4): executor NLR paired with RGA5
- [ ] ORYSJ/PIKM1-TS (B5UBC1): Pikm sensor NLR, recognises AVR-Pik through its HMA domain

### Tier 4: Arbuscular mycorrhizal symbiosis (plant)

- [ ] MEDTR/NORK (Q8L4H4): SYMRK/DMI2 symbiosis receptor kinase
- [ ] MEDTR/DMI1 (Q6RHR6): nuclear-envelope ion channel for calcium spiking
- [ ] LOTJA/CASTOR (Q5H8A6): DMI1-related nuclear-envelope ion channel
- [ ] LOTJA/CYCLOPS (A9XMT3): CCaMK substrate, transcriptional activator
- [ ] MEDTR/RAM1 (G7L166): GRAS transcription factor for arbuscule development
- [ ] MEDTR/STR (D3GE74): periarbuscular ABC transporter
- [ ] MEDTR/PT4 (Q8GSG4): periarbuscular phosphate transporter

### Tier 5: Fungal effectors and virulence factors

- [ ] PYRO7/slp1 (G4N906): LysM effector that sequesters chitin oligomers
- [ ] PYRO7/PWL2 (G5EI71): host-specificity effector
- [ ] PYRO7/BAS1 (G5EHI7): biotrophy-associated secreted protein
- [ ] PYRO7/PMK1 (G4N0Z0): MAPK needed for appressorium formation and invasive growth
- [ ] PYRO7/MPG1 (P52751): class I hydrophobin
- [ ] FULFL/ECP6 (B3VBK9): LysM effector, the reference chitin-masking effector
- [ ] FULFL/AVR4 (Q00363): chitin-binding effector that protects hyphae from plant chitinases
- [ ] FULFL/AVR9 (P22287): avirulence protein recognised through Cf-9
- [ ] MYCMD/CMU1 (A0A0D1DWQ2): secreted chorismate mutase that redirects host salicylic acid synthesis
- [ ] MYCMD/PIT2 (A0A0D1EAR7): inhibitor of host apoplastic cysteine proteases
- [ ] MYCMD/See1 (A0A0D1C8C8): effector that drives leaf tumour formation
- [ ] GIBZE/TRI5 (Q00909): trichodiene synthase, first step in deoxynivalenol synthesis

### Candidates without a reviewed UniProt entry (need an accession before fetch)

These are central to the field but no Swiss-Prot entry was found under the
expected gene name. Look up the correct (possibly TrEMBL) accession before
running `fetch-gene`; do not guess one.

- [ ] Barley MLA10 (powdery mildew NLR) with Blumeria AVRa10
- [ ] Rice Pi-ta with *P. oryzae* AVR-Pita
- [ ] *P. oryzae* AVR-Pik, AVR-Pia, AVR1-CO39 (partners for the Tier 3 NLRs)
- [ ] Tomato Cf-9 / Cf-4 (the Cf-9 receptor itself is from *S. pimpinellifolium*)
- [ ] *U. maydis* Pep1 and Tin2
- [ ] *Fusarium oxysporum* SIX1 (Avr3)
- [ ] *Rhizophagus irregularis* SP7

## Workflow per gene

1. `just fetch-gene <SPECIES> <GENE>`, giving the UniProt accession where the
   symbol is ambiguous
2. Deep research (default provider: falcon)
3. Review every existing annotation with the annotation-reviewer agent
4. `just validate <SPECIES> <GENE>`, then add a history record with
   `just new-history`

# NOTES

## 2026-10-02

- Project created. Looked for existing plant immunity and symbiosis reviews in
  `genes/` and listed the overlapping ones above.
- Resolved candidate genes against UniProtKB/Swiss-Prot. Notes from that:
  - Rice blast is under the strain-specific mnemonic **PYRO7** (strain 70-15) in
    Swiss-Prot. The repo already has a `genes/PYROR/` folder (taxon 318829) for
    one non-effector gene. **Decided (2026-10-02): new blast reviews go in
    `genes/PYRO7/`**, matching UniProt. The existing `PYROR` review stays where
    it is.
  - *Fulvia fulva* (*Cladosporium fulvum*) entries use **FULFL**, and *Ustilago
    maydis* entries use **MYCMD** (*Mycosarcoma maydis*).
  - ORA59 is named ERF094 in UniProt, and SYMRK/DMI2 in *Medicago* is NORK.
  - RGA4 and RGA5 each have two Swiss-Prot entries, from the resistant (R) and
    susceptible (S) alleles. The list uses the resistant-allele entries
    (F7J0M4, F7J0N2).
