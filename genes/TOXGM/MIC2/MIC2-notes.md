# MIC2 (Toxoplasma gondii ME49; UniProt S8F9G8; TGME49_201780) - curation notes

**Note:** automated deep research was unavailable in this environment (Falcon
authentication failed; OpenAI key invalid). These notes are a manual literature review
built from the UniProt record and primary papers cached in `publications/`, identified
by PubMed searches. No `*-deep-research-*.md` file exists for this gene.

## 2026-10-14 - initial review

### Sequence / domain architecture (UniProt S8F9G8, TrEMBL, unreviewed)
- 769 aa; predicted signal peptide 1-26; VWFA (integrin-like A/I) domain 76-263;
  six TSP1 repeats (Pfam PF00090 x6); C-terminal hydrophobic segment
  (~GIAGAIAGGVIGGLILLGAAGGA) followed by a short acidic cytoplasmic tail ending in
  ...DDDSDMWME (penultimate Trp typical of TRAP-family tails). UniProt does not annotate
  a TM segment; its SUBCELLULAR LOCATION "Secreted" is an ARBA rule inference.
- PANTHER places it in PTHR22906 "PROPERDIN" only because of the TSR repeats; MIC2 is
  not a complement regulator. The single GOA row (extracellular region, IEA from
  UniProt SubCell) derives from the ARBA "Secreted" call.

### Identity and microneme localization
- [PMID:9084040 "These results demonstrate that c50 encodes for MIC2, a previously
  characterised microneme protein of T. gondii."]
- [PMID:9084040 "exclusively labeled the micronemes of T. gondii by cryo-immunoelectron
  microscopy"]
- TSR and integrin-A-like domains noted at cloning: [PMID:9084040 "five copies of the
  conserved thrombospondin (TSP)-like motif present in a number of molecules with
  adhesive properties"]
- Domain architecture from crystal structures: [PMID:24639528 "With a von Willebrand
  factor A (VWA) domain and six thrombospondin repeat domains (TSR1-6) in its
  ectodomain, MIC2 connects to the parasite actomyosin system through its cytoplasmic
  tail."]

### Type I transmembrane adhesin; complex with M2AP
- [PMID:14670959 "microneme protein 2 (MIC2), is a type one transmembrane protein that
  binds to an accessory protein known as MIC2-associated protein (M2AP)."]
- Stoichiometry disputed: hexamer (native gels) [PMID:14670959 "MIC2 and M2AP proteins
  form stable hexamers consisting of three alphabeta dimers"] versus 1:1 ectodomain
  monomer [PMID:24639528 "the MIC2-M2AP ectodomain complex is a highly elongated 1:1
  monomer with M2AP bound to the TSR6 domain"].
- M2AP is needed for MIC2 trafficking and secretion [PMID:12727875 "M2AP knockout
  parasites were also unable to rapidly secrete MIC2, an event that normally accompanies
  parasite attachment to a target cell."]; conversely MIC2 loss mistraffics M2AP
  [PMID:16933991 "Reduced MIC2 expression resulted in mistrafficking of M2AP"].

### Secretion, surface translocation, shedding (localization dynamics)
- Apical secretion, rearward translocation and rhomboid cleavage:
  [PMID:15753289 "Upon microneme secretion, as occurs during invasion, the MIC2 adhesin
  was secreted to the apical end and translocated to the posterior, the site of
  cleavage, where it colocalized only with TgROM5."]
- Intramembrane shedding: [PMID:14982962 "MIC2 is shed by intramembrane cleavage within
  its anchoring domain"]; MPP1/MPP2 processing [PMID:10799515 "the C-terminal domain of
  MIC2 is removed by a protease, termed MPP1, when MIC2 is released into the culture
  supernatant."]
- Hence the ectodomain does end up in the extracellular milieu (the "excreted-secreted
  antigen" fraction; [PMID:16933991 "When levels of MIC2 in cell lysates or in the
  excreted-secreted antigen fraction are examined by quantitative immunoblotting"]), but
  the functional locations are the microneme (storage) and the parasite cell surface
  (adhesion). "Extracellular region" is therefore true but peripheral.

### Molecular function: adhesin
- A-domain binds heparin: [PMID:15003840 "the MIC2 A-domain binds specifically to
  heparin, a ubiquitous sulfated proteoglycan found in the extracellular matrix (ECM)"];
  binding is MIDAS-independent and multimeric.
- Binds host ICAM-1: [PMID:15760456 "human ICAM-1 immunoprecipitated the mature form of
  the parasite adhesin MIC2 present on the parasite surface"]
- Cytoplasmic tail binds aldolase, linking adhesin to F-actin/motor:
  [PMID:12718875 "a complex of parasite proteins, including the actin binding protein
  aldolase, which specifically interacts with the C-terminal domains of several parasite
  adhesins belonging to the thrombospondin-related anonymous protein (TRAP) family"];
  acidic clusters needed [PMID:16923803 "two separate acidic residue clusters in the
  cytoplasmic domain of MIC2 that are essential for parasite survival"].
- Best GO MF: GO:0098631 cell adhesion mediator activity (binding by a surface
  adhesion protein to a molecule on another cell or substrate to mediate adhesion).
  GO:0008201 heparin binding is directly shown for the recombinant A-domain (in vitro).

### Biological process: attachment, gliding, invasion
- Conditional knockdown (Huynh & Carruthers 2006): [PMID:16933991 "markedly defective
  host-cell attachment and invasion, the loss of helical gliding motility, and the
  inability to support lethal infection in a murine model of acute toxoplasmosis"];
  [PMID:16933991 "Therefore, the entry defect is principally due to an inability to
  adhere properly to the target cell, although we cannot rule out an additional defect in
  the penetration step that follows attachment."]
- Clean conditional KO (Andenmatten 2013): MIC2 not essential [PMID:23263690 "we
  achieved isolation of a clonal mic2 KO parasite line, demonstrating for the first time
  that neither myoA nor mic2 are essential for parasite survival."]
- Null mutant analysis (Gras 2017) revises the model: role mainly in attachment, not in
  sustaining motility/penetration; mild virulence attenuation only.
  [PMID:28630943 "In summary, we find here that MIC2 acts as important, but not
  essential, attachment factor, and that reduced invasion and gliding rates are due to a
  decreased ability to initiate rather than to sustain motility."]
  [PMID:28630943 "mic2KO parasites show impaired attachment to host cells and collagen
  IV."]
- Interpretation: MIC2 itself performs the adhesion step (it is the adhesin, binding
  host ligands while gripping the motor via aldolase), so "adhesion of symbiont to host
  cell" (GO:0044650) is a participation annotation, not mere necessity. Gliding
  motility: GO:0071980 "cell surface adhesin-mediated gliding motility" is defined by
  exactly this mechanism; MIC2 contributes to helical gliding/twirling (both knockdown
  and KO). Invasion (GO:0085017): MIC2 contributes via attachment at the start of entry;
  the KO shows invasion still occurs, so non-core.
- Virulence: knockdown claimed avirulent (PMID:16933991) but KO remains lethal in mice
  (PMID:28630943). Do not annotate virulence.

### Curation decisions
- GO:0005576 extracellular region (IEA, SubCell): KEEP_AS_NON_CORE - shed ectodomain is
  released into the medium, but primary locations are microneme and cell surface.
- NEW: GO:0020009 microneme (IDA PMID:9084040); GO:0009986 cell surface (IDA
  PMID:15753289); GO:0098631 cell adhesion mediator activity (PMID:15760456,
  PMID:15003840); GO:0008201 heparin binding (IDA PMID:15003840); GO:0044650 adhesion of
  symbiont to host cell (IMP PMID:28630943, PMID:16933991); GO:0071980 cell surface
  adhesin-mediated gliding motility (IMP PMID:16933991, PMID:28630943).
- GO:0085017 entry into host cell by a symbiont-containing vacuole: considered; added as
  NEW but flagged non-core because KO invasion defect is secondary to attachment.
- No host-process ("symbiont-mediated perturbation of host ...") terms: MIC2 does not
  modulate host processes; ICAM-1 engagement is adhesion.
- PANTHER PTHR22906 "properdin" family membership should not be propagated to complement
  terms (none present now).
