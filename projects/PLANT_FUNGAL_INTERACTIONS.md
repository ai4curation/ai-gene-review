---
title: "Plant-Fungal Interactions"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [ARATH, ORYSJ, HORVU, MEDTR, LOTJA, PYRO7, FULFL, MYCMD, GIBZE]
genes: [CERK1, LYK5, LYM2, SYP121, BGLU26, ABCG36, CYP71B15, CYP79B2, MLO2, WRKY33, ERF094, MPK3, CEBIP, PIKM1-TS, RGA4, RGA5, MLO, NORK, DMI1, CASTOR, CYCLOPS, RAM1, STR, PT4, PWL2, BAS1, slp1, PMK1, MPG1, AVR9, AVR4, ECP6, CMU1, PIT2, See1, TRI5, CYP79B3, CYP71A13, CYP71A12, GSTF6, LYK4, PBL27, PBL1, MAPKKK5, MKK4, MKK5, RLCK185]
---

# Plant-Fungal Interactions

**Bottom line:** Plants and fungi meet at the cell surface and in the apoplast,
where plant receptors detect fungal chitin, fungal effectors try to hide it or
disarm the host, and in symbiosis the two partners exchange nutrients across a
shared membrane. We reviewed every existing GO annotation on 36 genes from
both sides of these interactions, in 9 species: plant chitin receptors,
penetration-resistance and camalexin genes, rice sensor/executor immune
receptors, the legume mycorrhizal pathway, and fungal effectors, a hydrophobin,
a MAP kinase and a toxin enzyme. All 36 reviews are done: 652 annotations were
assessed, with 333 accepted, 161 kept as non-core, 71 modified, 40 marked
over-annotated, 47 removed and none left undecided, plus 36 new annotations
proposed. All 36 reviews validate and are marked COMPLETE.
The main corrections were separating genes that do the work of a defence
process from genes that are only needed for it, replacing `protein binding`
rows with specific terms, and giving each partner in a receptor pair, and
each of two chitin-binding effectors, its own distinct function.

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

## Results

Counts are taken from the review files. "Rows" is the number of GOA
annotations reviewed; NEW annotations are counted separately.

| Gene | Rows | Accept | Non-core | Modify | Over-annot. | Remove | Undecided | New | Main correction |
|------|-----:|-------:|---------:|-------:|------------:|-------:|----------:|----:|-----------------|
| ARATH/LYK5 | 17 | 10 | 1 | 0 | 3 | 3 | 0 | 2 | Kinase domain is inactive, so ATP binding is over-annotated; added pattern recognition receptor activity |
| ARATH/LYM2 | 10 | 7 | 2 | 0 | 0 | 1 | 0 | 1 | Mitochondrion (HDA) removed; added cellular response to chitin |
| ORYSJ/CEBIP | 3 | 2 | 0 | 1 | 0 | 0 | 0 | 2 | `protein binding` to pattern recognition receptor activity |
| ORYSJ/CERK1 | 20 | 16 | 0 | 2 | 0 | 2 | 0 | 1 | Chitin binding removed (OsCEBiP binds chitin, not OsCERK1); added arbuscular mycorrhizal association |
| ARATH/SYP121 | 58 | 28 | 18 | 8 | 1 | 3 | 0 | 1 | `protein binding` to SNARE / transporter binding; added potassium channel regulator activity |
| ARATH/BGLU26 | 21 | 8 | 8 | 2 | 2 | 1 | 0 | 1 | Core activity is thioglucosidase (myrosinase); generic beta-glucosidase kept as non-core |
| ARATH/ABCG36 | 108 | 40 | 39 | 9 | 18 | 2 | 0 | 0 | `protein binding` to calmodulin binding; processes inferred only from mutant phenotypes marked over-annotated |
| ARATH/MLO2 | 12 | 4 | 3 | 3 | 0 | 2 | 0 | 2 | Defense rows to negative regulation of defense response; added calcium channel activity |
| HORVU/MLO | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | `defense response` had the wrong sign; changed to negative regulation |
| ARATH/CYP79B2 | 30 | 6 | 17 | 5 | 1 | 1 | 0 | 0 | Sulfur compound biosynthesis to indole glucosinolate biosynthesis; membrane to ER membrane |
| ARATH/CYP71B15 | 32 | 13 | 8 | 3 | 4 | 4 | 0 | 0 | Membrane and ER lumen rows to ER membrane (single N-terminal anchor; cytosol-facing P450) |
| ARATH/WRKY33 | 40 | 20 | 11 | 2 | 0 | 7 | 0 | 0 | Camalexin biosynthesis to positive regulation of camalexin biosynthesis |
| ARATH/MPK3 | 65 | 24 | 20 | 2 | 1 | 18 | 0 | 0 | Camalexin biosynthesis to positive regulation; 18 `protein binding` rows removed |
| ARATH/ERF094 | 19 | 14 | 2 | 3 | 0 | 0 | 0 | 2 | Systemic resistance to defense response to fungus; added transcription activator activity |
| ORYSJ/RGA5 | 16 | 7 | 4 | 2 | 2 | 1 | 0 | 0 | Metal ion binding removed (broken HMA motif); RGA4 binding to inhibitor activity |
| ORYSJ/RGA4 | 14 | 9 | 0 | 2 | 3 | 0 | 0 | 1 | PRR-signalling term replaced; kept as the cell-death executor |
| ORYSJ/PIKM1-TS | 4 | 1 | 1 | 1 | 0 | 1 | 0 | 2 | Metal ion binding removed; added innate immune receptor activity |
| MEDTR/NORK | 9 | 8 | 0 | 1 | 0 | 0 | 0 | 3 | Added nodulation and arbuscular mycorrhizal association as separate terms |
| MEDTR/DMI1 | 7 | 3 | 0 | 4 | 0 | 0 | 0 | 3 | CNGC15 `protein binding` to ion channel regulator activity |
| LOTJA/CASTOR | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | Added cation channel activity (kept general: K+ vs Ca2+ is disputed) |
| LOTJA/CYCLOPS | 14 | 10 | 1 | 3 | 0 | 0 | 0 | 0 | Transcription factor activity narrowed to activator; CCaMK binding to protein kinase binding |
| MEDTR/RAM1 | 20 | 11 | 4 | 4 | 1 | 0 | 0 | 0 | Detection of phosphate over-annotated; partner binding to heterodimerization |
| MEDTR/STR | 16 | 10 | 5 | 1 | 0 | 0 | 0 | 0 | Transporter kept at ABC-type level (lipid cargo not proven) |
| MEDTR/PT4 | 27 | 11 | 8 | 5 | 2 | 1 | 0 | 0 | Plasma membrane to periarbuscular membrane; phosphate:proton symporter activity |
| PYRO7/slp1 | 3 | 2 | 0 | 1 | 0 | 0 | 0 | 1 | Added chitin binding; reference behind the PHI-base row was miscited |
| PYRO7/PWL2 | 15 | 15 | 0 | 0 | 0 | 0 | 0 | 1 | Added effector-mediated suppression of host pattern-triggered immunity |
| PYRO7/BAS1 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | No change; molecular function unknown |
| PYRO7/PMK1 | 13 | 10 | 3 | 0 | 0 | 0 | 0 | 0 | No change needed |
| PYRO7/MPG1 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 2 | Added spore wall and asexual spore wall assembly |
| FULFL/ECP6 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | No change needed |
| FULFL/AVR4 | 10 | 3 | 5 | 1 | 1 | 0 | 0 | 2 | PAMP receptor decoy activity over-annotated (that is ECP6's mechanism) |
| FULFL/AVR9 | 5 | 2 | 0 | 3 | 0 | 0 | 0 | 1 | Perturbation of host immunity to activation of plant hypersensitive response |
| MYCMD/CMU1 | 11 | 9 | 1 | 0 | 1 | 0 | 0 | 0 | Aromatic amino acid biosynthesis over-annotated (it acts in the host) |
| MYCMD/PIT2 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | Added cysteine-type endopeptidase inhibitor activity |
| MYCMD/See1 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | No change needed |
| GIBZE/TRI5 | 4 | 3 | 0 | 1 | 0 | 0 | 0 | 1 | Sesquiterpenoid biosynthesis to vomitoxin (deoxynivalenol) biosynthesis |
| **Total** | **652** | **333** | **161** | **71** | **40** | **47** | **0** | **36** | |

## Modules

Two pathway modules tie the gene reviews together:

- [Camalexin biosynthesis](../modules/camalexin_biosynthesis.html)
  (`modules/camalexin_biosynthesis.yaml`). Tryptophan is converted to IAOx
  (CYP79B2/B3). CYP71A13 (with a minor role for CYP71A12) then oxygenates
  IAOx to a cyanohydrin and dehydrates it to a reactive intermediate; IAN may
  be a side product (Klein et al. 2013). The intermediate is conjugated to
  glutathione (GSTF6, implicated; many GSTs can do it and it also happens
  without an enzyme) and trimmed by GGP1, and PAD3 makes dihydrocamalexic acid and then camalexin. MPK3/MPK6 and
  WRKY33 are modelled as a separate regulatory part that positively regulates
  the CYP71A13 and PAD3 steps, matching the enzyme-versus-regulator split in
  the gene reviews. GSTU4 binds the enzyme complex but is not a pathway enzyme,
  so it is left out.
- [Chitin perception](../modules/chitin_perception.html)
  (`modules/chitin_perception.yaml`). The receptor complex is modelled as two
  variants: rice CEBiP binds chitin and OsCERK1 is the kinase, while in
  *Arabidopsis* the LYK5 pseudokinase binds chitin, LYK4 acts as a co-receptor
  and CERK1 is the kinase. Two branches follow. In one, PBL27 (OsRLCK185 in
  rice) feeds a MAPKKK5-MKK4/5-MPK3/6 relay (reusing `mapk_relay`). The PBL27
  step is disputed in *Arabidopsis*, where other RLCKs may phosphorylate
  MAPKKK5, but it is well supported in rice, where OsRLCK185 phosphorylates
  OsMAPKKKε and OsMAPKKK18. In the other branch, BIK1 activates RBOHD for the
  ROS burst. PBL1 was dropped from this step because nothing shows it acting
  alone there. LYM2's plasmodesmal branch does not need
  CERK1, and the fungal chitin-masking effectors act from outside the plant,
  so both are recorded as notes rather than parts.

Every protein member of both modules now has a completed gene review. The 11
members added for the modules are summarised below; counts are taken from the
review files.

| Gene | Module | Rows | Accept | Non-core | Modify | Over-annot. | Remove | Undecided | New | Main correction |
|------|--------|-----:|-------:|---------:|-------:|------------:|-------:|----------:|----:|-----------------|
| ARATH/CYP79B3 | camalexin | 25 | 4 | 14 | 5 | 2 | 0 | 0 | 0 | Same fixes as CYP79B2: indole glucosinolate biosynthesis, ER membrane |
| ARATH/CYP71A13 | camalexin | 24 | 8 | 8 | 2 | 1 | 4 | 1 | 0 | Membrane to ER membrane; ER lumen left undecided |
| ARATH/CYP71A12 | camalexin | 17 | 5 | 5 | 2 | 3 | 1 | 1 | 1 | Induced systemic resistance over-annotated (the response depends on salicylic acid) |
| ARATH/GSTF6 | camalexin | 26 | 9 | 6 | 0 | 8 | 1 | 2 | 0 | Metal binding and proteomics locations over-annotated; no camalexin term added |
| ARATH/LYK4 | chitin | 19 | 11 | 0 | 0 | 4 | 4 | 0 | 2 | Kinase activity removed (pseudokinase); added coreceptor activity |
| ARATH/PBL27 | chitin | 25 | 14 | 4 | 1 | 0 | 6 | 0 | 1 | Added regulation of stomatal closure (phosphorylates SLAH3) |
| ARATH/PBL1 | chitin | 15 | 9 | 1 | 1 | 1 | 3 | 0 | 0 | Bacterial defence regulation over-annotated |
| ARATH/MAPKKK5 | chitin | 27 | 13 | 7 | 1 | 0 | 6 | 0 | 0 | PRR signalling refined to cell surface PRR signalling |
| ARATH/MKK4 | chitin | 40 | 11 | 14 | 1 | 0 | 13 | 1 | 0 | Serine kinase row to MAP kinase kinase activity |
| ARATH/MKK5 | chitin | 39 | 10 | 17 | 2 | 0 | 10 | 0 | 0 | Serine kinase rows to MAP kinase kinase activity |
| ORYSJ/RLCK185 | chitin | 9 | 8 | 0 | 1 | 0 | 0 | 0 | 1 | Added positive regulation of MAPK cascade |
| **Total** | | **266** | **102** | **76** | **16** | **19** | **48** | **5** | **5** | |

Both modules list their open questions as knowledge gaps. The MPK6 review
(previously DRAFT) was updated to match MPK3: its camalexin biosynthesis row now
reads "positive regulation of camalexin biosynthetic process", and the review is
COMPLETE.

### Findings by curation question

1. **Process terms on effectors.** The effector annotations already use the
   pathogen-side terms rather than plant-side `defense response` terms, and
   most rest on experiments on the effector itself. The gaps ran the other
   way: several effectors had no function or process term at all. Slp1 lacked
   chitin binding, PIT2 lacked its protease inhibitor activity, and PWL2 had
   locations only. GO also has no term for the biotrophic interfacial complex,
   the structure where blast cytoplasmic effectors collect. So cytoplasmic
   effectors (PWL2, BAS1) and apoplastic ones end up on the same
   `extracellular region` term.
2. **LysM effectors vs LysM receptors.** No receptor terms reached the
   effectors through InterPro2GO. The leaks found were different. OsCERK1 had
   chitin binding copied from *Arabidopsis* CERK1, although in rice CEBiP binds
   the chitin. AVR4 carried the PAMP-decoy (sequestration) term, which
   describes ECP6. Each of the four chitin-binding proteins now has its own
   mechanism.
3. **Necessity vs participation.** This was the most common correction. It is
   applied consistently: a gene keeps `defense response to fungus` when it
   does part of the work. Examples are SYP121 doing the vesicle fusion,
   BGLU26 and CYP71B15 making the antifungal compounds, ABCG36 exporting them,
   and WRKY33 and ERF094 switching on defence genes. Genes known only from
   mutant phenotypes (LYM2, CYP79B2, TRI5) did not get the term. Two
   regulators had a biosynthesis term changed to "positive regulation of
   camalexin biosynthesis", which leaves the biosynthesis term on the enzyme
   (MPK3, WRKY33). The two MLO reviews changed `defense response` to its
   opposite, negative regulation of defense response, because MLO is a
   susceptibility factor.
4. **Symbiosis vs defense.** GOA had no symbiosis term on rice CERK1.
   Arbuscular mycorrhizal association was added as a separate core function
   from chitin immunity. The common symbiosis genes (NORK, DMI1, CASTOR,
   CYCLOPS) carry no defence terms and now have nodulation and mycorrhizal
   association as separate entries. A kinase-dead NORK allele blocks
   nodulation but not mycorrhization.
5. **Sensor/executor receptor pairs.** GOA gave RGA4 and RGA5 almost the same
   annotations, drawn from the same two papers. RGA5 now carries receptor
   activity, inhibitor activity (it holds RGA4 in check) and regulation of
   the hypersensitive response. RGA4 carries execution of the hypersensitive
   response and ADP binding. The Pikm-1 sensor follows the RGA5 pattern.

### Suggested GO ontology changes

- `GO:0080185` (effector-mediated activation of plant hypersensitive response)
  sits under a term defined as suppressing host immunity. Every avirulence
  effector annotated to it therefore also gets a suppression claim (AVR4,
  AVR9).
- No GO term for the biotrophic interfacial complex.
- No pathogen-side term for suppressing host salicylic acid biosynthesis
  (CMU1), and no camalexin-export activity (ABCG36).
- Proposed new terms: dihydrocamalexate synthase activity (CYP71B15), and
  negative regulation of plasmodesmata-mediated intercellular transport
  (LYM2).
- The periarbuscular membrane is not under plasma membrane, so plant-side
  annotations to it do not count as plasma membrane annotations (PT4, STR).

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

- [x] ARATH/LYK5 (O22808): main chitin-binding LysM receptor kinase, partners CERK1
- [x] ARATH/LYM2 (O23006): GPI-anchored CEBiP homologue, plasmodesmal chitin response
- [x] ORYSJ/CEBIP (Q8H8C7): rice chitin elicitor-binding protein
- [x] ORYSJ/CERK1 (A0A0P0XII1): rice chitin receptor kinase, also needed for AM symbiosis
- [x] ARATH/SYP121 (Q9ZSD4): PEN1 syntaxin, focal secretion at penetration sites
- [x] ARATH/BGLU26 (O64883): PEN2 myrosinase, indole glucosinolate hydrolysis
- [x] ARATH/ABCG36 (Q9XIE2): PEN3 ABC transporter
- [x] ARATH/MLO2 (Q9SXB6): powdery mildew susceptibility gene
- [x] HORVU/MLO (P93766): barley *Mlo*, the original powdery mildew susceptibility gene

### Tier 2: Defense outputs (plant)

- [x] ARATH/CYP79B2 (O81346): tryptophan N-monooxygenase, entry step to camalexin and indole glucosinolates
- [x] ARATH/CYP71B15 (Q9LW27): PAD3 camalexin synthase
- [x] ARATH/WRKY33 (Q8S8P5): transcription factor for camalexin and anti-*Botrytis* defense
- [x] ARATH/MPK3 (Q39023): MAPK that phosphorylates WRKY33
- [x] ARATH/ERF094 (Q9LND1): ORA59, JA/ET integrator for necrotroph defense

### Tier 3: Recognition of fungal effectors (plant NLRs)

- [x] ORYSJ/RGA5 (F7J0N2): sensor NLR with integrated HMA domain, recognises AVR-Pia and AVR1-CO39
- [x] ORYSJ/RGA4 (F7J0M4): executor NLR paired with RGA5
- [x] ORYSJ/PIKM1-TS (B5UBC1): Pikm sensor NLR, recognises AVR-Pik through its HMA domain

### Tier 4: Arbuscular mycorrhizal symbiosis (plant)

- [x] MEDTR/NORK (Q8L4H4): SYMRK/DMI2 symbiosis receptor kinase
- [x] MEDTR/DMI1 (Q6RHR6): nuclear-envelope ion channel for calcium spiking
- [x] LOTJA/CASTOR (Q5H8A6): DMI1-related nuclear-envelope ion channel
- [x] LOTJA/CYCLOPS (A9XMT3): CCaMK substrate, transcriptional activator
- [x] MEDTR/RAM1 (G7L166): GRAS transcription factor for arbuscule development
- [x] MEDTR/STR (D3GE74): periarbuscular ABC transporter
- [x] MEDTR/PT4 (Q8GSG4): periarbuscular phosphate transporter

### Tier 5: Fungal effectors and virulence factors

- [x] PYRO7/slp1 (G4N906): LysM effector that sequesters chitin oligomers
- [x] PYRO7/PWL2 (G5EI71): host-specificity effector
- [x] PYRO7/BAS1 (G5EHI7): biotrophy-associated secreted protein
- [x] PYRO7/PMK1 (G4N0Z0): MAPK needed for appressorium formation and invasive growth
- [x] PYRO7/MPG1 (P52751): class I hydrophobin
- [x] FULFL/ECP6 (B3VBK9): LysM effector, the reference chitin-masking effector
- [x] FULFL/AVR4 (Q00363): chitin-binding effector that protects hyphae from plant chitinases
- [x] FULFL/AVR9 (P22287): avirulence protein recognised through Cf-9
- [x] MYCMD/CMU1 (A0A0D1DWQ2): secreted chorismate mutase that redirects host salicylic acid synthesis
- [x] MYCMD/PIT2 (A0A0D1EAR7): inhibitor of host apoplastic cysteine proteases
- [x] MYCMD/See1 (A0A0D1C8C8): effector that drives leaf tumour formation
- [x] GIBZE/TRI5 (Q00909): trichodiene synthase, first step in deoxynivalenol synthesis

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

## 2026-10-03

- MPK6: changed the camalexin biosynthesis row (IMP, PMID:18378893) to
  positive regulation of camalexin biosynthetic process (GO:1901183), matching
  MPK3 and WRKY33. Fixed the two warnings that kept it at DRAFT, both from core
  functions that used terms the review marks non-core: defense response to
  bacterium was replaced by GO:1901183, and cell cortex was dropped from the
  developmental core function. Now COMPLETE. Closed the matching knowledge gap
  in the camalexin module.

- Reviewed the 11 module members that had no gene review (falcon deep research
  for each; all COMPLETE). CYP71A13 and CYP71A12 also cited the deleted
  duplicate PMID:33831160 and were remapped the same way as CYP71B15. Then
  updated both modules to match: Klein et al. 2013 chemistry for the CYP71A
  step, LYK4 as co-receptor, BIK1 alone in the ROS branch, and the disputed
  PBL27 step.
- Kept the MAPK-cascade members consistent. MKK4, MKK5 and MPK3 carry no new
  cell surface PRR signalling term, because the same-role comparators lack it
  (MAPKKK5 has it only from an existing curator IGI row). An MKK5 proposal for
  this term was dropped on those grounds and raised as a question.

- Built two modules, `camalexin_biosynthesis` (concrete, Arabidopsis) and
  `chitin_perception` (abstract, flowering plants), each with falcon module
  deep research. Both pass `linkml-validate` and `module_validator` and are
  rendered. No other module covered this biology: `nlr_signaling` is
  animal-only, and `aliphatic_glucosinolate_myrosinase_defense` excludes the
  indole branch.

- PubMed's redirection notice shows PMID:33831160 was deleted as a duplicate
  of PMID:31511315 (Mucha et al. 2019, camalexin metabolon). Recorded the
  mapping on the CYP71B15 reference (`replacement`, DUPLICATE_RECORD) and kept
  the GOA identifier. The two protein binding rows went from undecided to
  removed, and the ER row stays accepted. The ER lumen row stays undecided
  because the full text is not retrievable and the location conflicts with
  the enzyme's cytosol-facing topology. CYP71B15 is now COMPLETE. The
  remaining fetch warning for the old PMID is the advisory one described in
  `docs/reference_curation.md`.

## 2026-10-02 (reviews)

- Fetched UniProt/GOA data for all 36 genes and ran falcon deep research for
  each (about 20-40 minutes per gene, all 36 succeeded).
- Reviewed each gene with the annotation-reviewer workflow, one agent per gene,
  and checked each against `just validate` and `just validate-history`.
- One agent proposal was dropped after checking it against the `NEW` rules in
  `CLAUDE.md`. MPK3: "pattern recognition receptor signaling pathway" was
  removed because the other MAP kinases in the same cascade (MPK6, MKK4,
  MKK5) do not carry it. It is now a suggested question.
- Consistency was checked across pairs reviewed at the same time: RGA4/RGA5,
  CASTOR/DMI1, MLO/MLO2, slp1/ECP6, and MPK3/WRKY33/CYP71B15.
- PMID:33831160 (cited by four TAIR rows on CYP71B15) returns no record from
  NCBI eutils. These rows were left undecided until the 2026-10-03 fix below.
- Many key papers are cached as abstract only. Agents deferred to curators
  where the full text was needed, rather than removing experimental
  annotations.

## 2026-10-02 (setup)

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
