# EME1 (OsEME1) — Oryza sativa subsp. japonica — research notes

UniProt: Q0J9J6 | Gene: EME1 / OsEME1 | Locus: Os04g0648700, LOC_Os04g55500
"Crossover junction endonuclease EME1" / "Essential meiotic endonuclease 1"; EC 3.1.22.-
Family: EME1/MMS4 family; PANTHER PTHR21077:SF5 (CROSSOVER JUNCTION ENDONUCLEASE MMS4)

## 1. What EME1/MUS81 is — conserved biology

EME1 (Eme1 in fission yeast; Mms4 in budding yeast; EME1/EME2 in humans) is the
non-catalytic regulatory subunit of a heterodimeric, structure-specific DNA
endonuclease whose catalytic subunit is MUS81. EME1 itself lacks endonuclease
activity in yeast and human; the interaction with MUS81 stimulates and regulates
MUS81's endonucleolytic activity.

[PMID:40333587 "Eme1 [methyl methanesulfonate 4 (Mms4) in ...] forms a heterodimeric endonuclease with Mus81 in ..., cleaving branched DNA substrates such as HJs, 3′-DNA flaps and replication forks"]
[PMID:40333587 "Eme1 (EME1) lacks endonuclease activity; its interaction with Mus81 (MUS81) regulates the endonucleolytic activity of Mus81 in yeast and human cells."]

MUS81-EME1 is one of three structure-selective endonuclease systems
(MUS81-EME1/MMS4, SLX1-SLX4, GEN1/Yen1) that resolve branched DNA
intermediates ("Holliday junction resolvases" in the broad sense). MUS81-EME1
has substrate preference for **nicked Holliday junctions, 3'-flaps, D-loops and
replication-fork structures** — i.e. branched substrates with a 5'-end at the
branch — and resolves intact HJs only with reduced efficiency.

[PMID:24008669 "In eukaryotes, multiple structure-specific nucleases, including Mus81-Mms4/MUS81-EME1, Yen1/GEN1, and Slx1-Slx4/SLX1-SLX4 (FANCP) have been implicated in the resolution of branched DNA intermediates."]
[PMID:24008669 "RuvC is also known to cut branched DNA intermediates that originate directly from blocked replication forks, targeting them for origin-independent replication restart."]

UniProt FUNCTION (Q0J9J6, by similarity): "Interacts with MUS81 to form a DNA
structure-specific endonuclease with substrate preference for branched DNA
structures with a 5'-end at the branch nick. Typical substrates include 3'-flap
structures, D-loops, replication forks, nicked Holliday junctions and also
intact Holliday junctions with a reduced efficiency. May be required in mitosis
for the processing of stalled or collapsed replication fork intermediates.
Plays a role in DNA repair and in genotoxic stress-induced homologous
recombination (HR) in somatic cells. Mediates a subset of meiotic recombination
events that are insensitive to crossover interference."

This dual mitotic/meiotic role is key: MUS81-EME1 functions in BOTH (a) somatic
(mitotic) replication-fork rescue and DSB repair AND (b) meiotic crossover
formation (the interference-insensitive / "class II" CO pathway). It is NOT a
meiosis-restricted enzyme.

### DNA-damage-responsive regulation
MUS81-EME1 activity is cell-cycle and DNA-damage regulated. In fission yeast,
DNA-damage-induced activation of Mus81-Eme1 requires Cdc2(CDK1)- and
Rad3(ATR)-dependent phosphorylation of Eme1; the complex is activated at G2/M.
[PMID:23584455 "we uncover DNA damage-induced activation of Mus81-Eme1 Holliday junction resolvase in fission yeast. This new regulation requires both Cdc2(CDK1)- and Rad3(ATR)-dependent phosphorylation of Eme1."]
[PMID:40333587 "In ..., the upregulation of Mus81–Eme1 depends on the phosphorylation of Eme1 by cell division cycle 2 (Cdc2) and Eme1 is further phosphorylated by DNA damage checkpoint factors such as Rad3 in response to DNA damage"]

In meiosis, MUS81-EME1 (with Yen1/GEN1 and SLX1-SLX4) must be kept inactive
during prophase I to allow proper CO patterning; precocious activation disrupts
crossover distribution.
[PMID:29920281 "active suppression of Yen1 function, and by inference also of Mus81-Mms4(EME1) and Slx1-Slx4(BTBD12) resolvases, avoids precocious resolution of recombination intermediates to enable meiotic crossover patterning."]

## 2. OsEME1 — the primary rice paper (Du et al. 2025, Plant Biotechnol J)

PMID:40333587 / DOI:10.1111/pbi.70101 — "ESSENTIAL MEIOTIC ENDONUCLEASE 1 is
required for chloroplast development and DNA repair in rice." This is the
definitive functional characterization of OsEME1 (Q0J9J6).

Key findings:

- **OsEME1 is a single-copy gene in rice.** Unlike Arabidopsis (which has EME1A
  and EME1B), rice has only one EME1.
  [PMID:40333587 "Surprisingly, rice contains only a single ... gene."]

- **OsEME1 is an endonuclease with intrinsic DNA cleavage activity in vitro.**
  Recombinant MBP-OsEME1 and the C-terminal fragment (OsEME1-C, containing the
  ERCC4 domain) both bind and cleave the Y12 branched substrate. This is notable:
  in yeast/human, EME1 is the non-catalytic subunit. In the rice in vitro assay,
  OsEME1 alone produced cleavage products.
  [PMID:40333587 "we measured the endonuclease activity of OsEME1 by performing a nuclease assay ... The major cleavage products were obtained in OsEME1 and OsEME1-C, and their levels gradually increased over time"]
  [PMID:40333587 "OsEME1 directly binds to and cleaves Y12, pre-X12 and X12, which are typical substrates after HR repair of DNA damage"]
  [PMID:40333587 "the C terminus of OsEME1 is responsible for its endonuclease activity"]

- **Four conserved residues required for activity.** Point mutants of four
  conserved residues (modelled on mammalian EME1 catalytic residues) reduced
  binding/cleavage, confirming the ERCC4 domain is the catalytic region.
  [PMID:40333587 "these four conserved amino acids are essential for the endonuclease activity of OsEME1"]

- **OsEME1 binds Mg2+/branched DNA substrates** — substrate Kd ~16 µM for Y12.
  UniProt cofactor: Mg(2+), Ca(2+).

- **OsEME1 interacts with OsMUS81.** Y2H, luciferase complementation (LCI) and
  BiFC all confirm interaction; the ERCC4 domain of OsEME1 and the HhH motif of
  OsMUS81 mediate the interaction.
  [PMID:40333587 "OsEME1 interacts with OsMUS81 and ... the ERCC4 domain of OsEME1 is required for this interaction."]
  [PMID:40333587 "Homologues of EME1 and MUS81 interact to form heterotetramers in mammals, yeasts and Arabidopsis"]

- **OsMUS81 binds X-structure substrates but did not itself add cleavage** in
  the in vitro assay — in the rice system OsEME1-C was the cleaver.
  [PMID:40333587 "OsMUS81 binds to X-structure substrates but is not responsible for the cleavage of junction DNA substrates."]

- **Nuclear localization.** OsEME1-GFP localizes to the nucleus and overlaps with
  the nuclear marker H2B-mCherry.
  [PMID:40333587 "the OsEME1-GFP fusion protein localized to the nucleus and overlapped closely with the nuclear protein H2B-mCherry"]

- **DNA-damage phenotypes.** EMS mutant (pale1) and CRISPR oseme1 mutants are
  hypersensitive to the DNA-damaging agents MMS and Zeocin (reduced shoot/root
  growth). Mutants show increased S/G2 DNA content (cell-cycle arrest), more
  S-phase (EdU+) cells, and increased γH2AX foci (a DSB / DNA-damage marker)
  with or without Zeocin.
  [PMID:40333587 "treatment with 75 µg/mL of MMS or 50 µg/mL of Zeocin strongly inhibited root and shoot growth, especially in the mutants"]
  [PMID:40333587 "The ... and ... mutants exhibited significantly more γ2HAX foci than KY131 with or without Zeocin treatment ... OsEME1 regulates DSB repair and the cell cycle."]

- **OsEME1 is involved in HR repair.** The proposed model: under high light or
  genotoxic stress, DSBs form, the DNA-damage response is activated, repair
  proceeds via HR, double Holliday junctions accumulate, and OsEME1 is recruited
  to bind and cleave the HJ substrates, maintaining genome stability.
  [PMID:40333587 "we discovered a biochemical role for OsEME1 in HR repair ... The MUS81–EME complex directly binds to and cleaves typical DNA substrates produced after HR repair, a process conserved in yeasts, mammals, dicots and monocots."]

- **Chloroplast / striped-leaf phenotype.** oseme1 mutants have a striped-albino
  leaf phenotype, defective chloroplast development, reduced chlorophyll/
  carotenoids, low PSII efficiency; the phenotype is strongly enhanced by
  high-light stress. OsEME1 globally regulates expression of photosynthesis and
  DNA-repair genes. Mechanistic model: OsEME1 maintains genome/transcription
  integrity of nuclear chloroplast-development genes (e.g. OsGLK1/OsGLK2), which
  in turn drive chloroplast development. The chloroplast phenotype is a
  downstream consequence of genome-maintenance failure, not a direct chloroplast
  function (OsEME1 is nuclear).
  [PMID:40333587 "OsEME1 regulates chloroplast development by modulating homologous recombination repair in response to damage to double-stranded DNA."]
  [PMID:40333587 "OsEME1 cleaves damaged double-stranded DNA substrates such as ...GLK1 and GLK2 DNA and maintains gene transcription."]

- **High-light sensitivity is real and experimentally demonstrated** in this
  paper (oseme1 mutants are hypersensitive to high light, with severe leaf
  striping and cell death after HL treatment). This is genuine functional
  evidence — but note this paper is PMID:40333587, NOT the IEP reference
  PMID:12869764.

## 3. Rice OsMUS81 — meiosis (Mu et al. 2022, New Phytol)

PMID:36495065 / DOI:10.1111/nph.18668 — "MUS81 is required for atypical
recombination intermediate resolution but not crossover designation in rice."

- Rice mus81 mutants have **normal chiasma numbers and normal HEI10 foci** (the
  interference-sensitive / class I CO pathway). MUS81 does NOT contribute
  substantially to crossover designation in rice.
  [PMID:36495065 "the total chiasma numbers in mus81 mutants were indistinguishable from wild-type. The numbers of HEI10 foci ... in mus81 were also similar to that of wild-type."]
  [PMID:36495065 "rice MUS81 did not function in crossover designation"]
- Instead, MUS81 resolves **atypical / aberrant meiotic recombination
  intermediates** — mus81 zep1 and mus81 fancm double mutants show chromosome
  fragments and bridges.
  [PMID:36495065 "MUS81 functions in atypical recombination intermediate resolution rather than crossover designation in rice"]
  [PMID:36495065 "MUS81 may resolve atypical recombination intermediates ... MUS81 ... plays a crucial role in the resolution of atypical meiotic intermediates by working together with other anti-crossover factors."]
- FANCM-dependent extra (interference-insensitive) COs in rice fancm mutants
  **require MUS81** for resolution.
  [PMID:37632767 "the meiotic extra COs are not marked with HEI10 and require MUS81 resolvase for resolution"]

So the rice MUS81-EME1 complex has a meiotic role — but it is a minor/atypical-
intermediate-resolution role, NOT a meiosis-restricted "essential meiotic
endonuclease" role. The "Essential meiotic endonuclease" name is historical
(from S. pombe Eme1) and is somewhat misleading for the plant ortholog.

## 4. Other plant context

- OsGEN1 (rice GEN1/Yen1 ortholog): a canonical HJ resolvase of the RAD2/XPG
  family; works alongside MUS81-EME1 and SLX1-SLX4 in HR-mediated DNA repair.
  osgen1 mutants show ~6% reduced chiasma frequency and persistent DSBs in
  microspores leading to male sterility.
  [PMID:28049740 "Yen1/GEN1 work together with Mus81-Mms4/MUS81-EME1 and Slx1-Slx4/SLX1-SLX4 in DNA repair by homologous recombination to maintain genome stability."]
- Arabidopsis: AtMUS81 with AtEME1A/AtEME1B. MUS81 defines a DNA-repair pathway
  parallel to RECQ4A; recq4A mus81 double mutants are lethal (rescued by
  blocking HR), showing MUS81 processes recombination-induced intermediates
  during replication. MUS81 is required for efficient synthesis-dependent strand
  annealing (SDSA).
  [PMID:20971895 "MUS81 and RECQ4A are required for processing recombination-induced aberrant intermediates during replication"]
  [PMID:20971895 "MUS81 and RECQ4A are required for efficient synthesis-dependent strand annealing (SDSA)"]
  [PMID:24635147 "FANCM has an MHF1-independent function in replicative repair in a parallel pathway to the endonuclease MUS81"]
- AtEME1A/AtEME1B are recruited to Holliday junction substrates and cleave at
  nicks in the DNA strands.
  [PMID:40333587 "The homologous proteins AtEME1A and AtEME1B are recruited to Holliday junction substrates in Arabidopsis; these proteins bind to and cleave their substrates at nicks in the DNA strands"]

## 5. Assessment of the IEP annotations from PMID:12869764

PMID:12869764 (Kikuchi et al. 2003, Science) is "Collection, mapping, and
annotation of over 28,000 cDNA clones from japonica rice." It is a large-scale
full-length cDNA sequencing/annotation consortium paper. Its abstract describes
ONLY cDNA collection, sequencing, mapping to genomic DNA, and InterPro-based
function assignment. There is NO gene-specific expression-profiling experiment
for EME1 and NO experiment testing response to UV, gamma radiation or high
light.

The three IEP annotations (response to UV GO:0009411, response to high light
intensity GO:0009644, response to gamma radiation GO:0010332) all cite
PMID:12869764 as the IEP (Inferred from Expression Pattern) reference. This is
almost certainly a curation artefact: the rice FL-cDNA consortium built cDNA
libraries from many tissues and stress conditions, and a clone for this gene may
have come from a stress-treated library (UV-/gamma-/high-light-treated tissue).
The presence of a cDNA clone in a stress library is library-of-origin
information, NOT an expression-response measurement, and certainly not evidence
of biological "involvement in" a stress response. IEP from this kind of source
is not appropriate functional evidence. Expression ≠ function.

Note: high-light sensitivity of OsEME1 IS genuinely demonstrated — but in
PMID:40333587 (oseme1 mutants hypersensitive to high light), as a downstream
consequence of a genome-maintenance defect, not a primary "response to high
light" function. The IEP annotations remain unsupported by their cited
reference.

## 6. Summary of SPKW-retired annotation assessment

The six retired SPKW (GO_REF:0000043) annotations were keyword-to-GO mappings:
- meiotic cell cycle (GO:0051321) <- KW "Meiosis" — OVER-SPECIFIC. EME1/MUS81 is
  not meiosis-restricted; its dominant role in rice is somatic DSB/replication
  repair. Removal justified.
- cell division (GO:0051301) <- KW "Cell division" — weakly supported, generic;
  EME1 acts in cell-cycle-coupled repair but "cell division" per se is not its
  function. Removal justified (over-annotation).
- DNA recombination (GO:0006310) <- KW "DNA recombination" — correct in essence
  (EME1 resolves HR intermediates) but generic; better captured by HR-repair /
  resolution terms. Removal acceptable; correct biology retained by current
  IBA/IEA terms.
- endonuclease activity (GO:0004519) <- KW "Endonuclease/Nuclease" — GENUINELY
  CORRECT. EME1 IS an endonuclease (EC 3.1.22.-), demonstrated biochemically in
  rice (PMID:40333587). Current GOA has NO catalytic MF term — only "DNA
  binding". Removing endonuclease activity LOST a correct, core annotation. This
  removal was NOT justified; a NEW catalytic MF term should be added.
- hydrolase activity (GO:0016787) <- KW "Hydrolase" — correct but vague parent
  of endonuclease activity. Removal of the vague term is acceptable IF a
  specific endonuclease MF is present (it is not — see above).
- metal ion binding (GO:0046872) <- KW "Metal-binding" — correct (Mg2+/Ca2+
  cofactor) but the keyword mapping is generic. MUS81-EME1 nuclease chemistry is
  Mg2+-dependent. Removal of the generic term is acceptable; magnesium ion
  binding (GO:0000287) would be the accurate specific term if retained.
