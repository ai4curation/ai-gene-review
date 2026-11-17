# omcZ (GSU2076, UniProt Q74BG5) — Geobacter sulfurreducens PCA

## Starting point

- UniProt Q74BG5 is an unreviewed (TrEMBL) entry named only "Cytochrome c",
  473 aa, PE 1 (two cryo-EM structures: PDB 7LQ5, residues 25-282, and 8D9M).
  SignalP signal peptide 1-24; Pfam IPT/TIG domain 392-455 (in the part that is
  later cut off). No PANTHER family is assigned in the UniProt record.
- **GOA has no annotations at all for this protein** (`omcZ-goa.tsv` is header only,
  checked 2026-11-09). Every annotation in the review is therefore a `NEW` row.
- No provider deep-research file was generated for this gene; the literature search
  below was done by hand from PubMed (query `OmcZ[Title/Abstract] AND Geobacter`,
  41 hits on 2026-11-09) plus the paper supplied by the user,
  Wissink et al. 2026 (DOI:10.1038/s41467-026-78976-x, not yet indexed in PubMed;
  cached from the CC-BY PDF as `publications/DOI_10.1038_s41467-026-78976-x.md`).

## Residue numbering — read before quoting a residue

The structure papers (Gu et al. 2023 PMID:36732469; Wissink et al. 2026) number
residues on the **mature** protein, i.e. UniProt position minus 24 (the SignalP
signal peptide). Checked against the Q74BG5 sequence:

| paper (mature) | UniProt Q74BG5 | residue |
|---|---|---|
| H40-H41 (heme II/III HH motif) | H64-H65 | His-His |
| C53 ... C68-H69 (CX14CH, heme II) | C77 ... C92-H93 | the non-canonical motif |
| R85 | R109 | Arg |
| H96-H97 (heme I/IV HH motif) | H120-H121 | His-His |
| H182-H183 (heme VI/VII HH motif) | H206-H207 | His-His |
| N258 (OzpA cleavage region) | N282 | Asn |

The 258-residue nanowire-forming OmcZ30 (Gu 2023, Wissink 2026) corresponds to
UniProt 25-282, matching the PDB 7LQ5 chain range. The review YAML avoids stating
residue numbers for this reason.

## Biology, with provenance

### Identity, hemes and processing
- OmcZ is made as a 50 kDa precursor (OmcZL) and a 30 kDa mature form (OmcZS);
  OmcZS keeps all eight hemes, one bound by an unusual CX14CH motif
  [PMID:20400562 "OmcZ(S) is a cleaved product of OmcZ(L) retaining all 8 hemes, including 1 heme with the unusual c-type heme-binding motif CX(14)CH"].
- OmcZS is very thermostable (Tm 94.2 °C) and its hemes span -420 to -60 mV, midpoint
  about -220 mV vs SHE [PMID:20400562 "the midpoint reduction potential of OmcZ(S) is approximately -220 mV (versus the standard hydrogen electrode [SHE]) with nonequivalent heme groups that cover a large reduction potential range (-420 to -60 mV)"].
- Cleavage is done by the subtilisin-like serine protease OzpA (GSU2075, immediately
  downstream); ozpA mutants accumulate OmcZL, make no OmcZS and produce as little
  current as omcZ mutants
  [PMID:33837010 "the ozpA mutant accumulated OmcZL and did not produce OmcZS, which is thought to be a mature form that is essential for the extracellular electron transfer to the electrode"].
  Cleavage activity is found only in the culture supernatant fraction, so maturation
  happens outside the cell [PMID:33837010 "only the culture supernatant protein fraction showed OmcZL cleavage activity"].
- omcZ, ozpA and a peptidyl-prolyl cis-trans isomerase gene (GSU2074) form an operon;
  OzpA cleaves native and recombinant OmcZ50 into OmcZ30, which self-assembles into
  filaments indistinguishable from native ones
  [PMID:36732469 "We found that purified OzpA cleaves both native and recombinant OmcZ50 into OmcZ30 which then self-assembled into nanowires"].
- AlphaFold models of the cleaved C-terminal region show Ig-like beta-sandwich domains
  (two in OmcZ of G. sulfurreducens), which agrees with the Pfam IPT/TIG hit at 392-455
  [DOI:10.1038/s41467-026-78976-x "the cleaved C-terminal regions adopt β-sandwich folds resembling immunoglobulin-like domains, with three such domains in OmcZ2Mv and two in OmcZGs"].
  Gu 2023 describes the same extra domain as resembling a sugar-binding domain and
  proposes that it blocks polymerization until it is removed.

### Structure of the filament
- Two independent cryo-EM structures of OmcZ filaments: Wang et al. 2022
  (PMID:36062910, Bond/Egelman labs, PDB 8D9M) and Gu et al. 2023 (PMID:36732469,
  Malvankar lab, PDB 7LQ5, 3.5 Å). Both are helical homopolymers of OmcZ30 with eight
  hemes per subunit. Hemes I-V and VII form a linear chain and heme VI branches off,
  fully exposed to solvent
  [PMID:36732469 "In OmcZ, haems I–V and VII form a linear, central, electron transport chain whereas haem VI is surface exposed"].
- Unlike OmcS and OmcE, there is no heme coordination between subunits, and the heme
  packing differs, which led Wang et al. to propose that cytochrome polymers evolved
  more than once [PMID:36062910 "conductive cytochrome polymers arose independently on more than one occasion from different ancestral multiheme proteins"].
- The heme II CX14CH loop is solvent exposed. Deleting it from reconstituted OmcZ
  lowers the rate of electron transfer to extracellular acceptors (PMID:36732469).
- Both structures were solved at pH 10.5 in ethanolamine buffer to stop the filaments
  aggregating; the archaeal OmcZ2 structure in Wissink 2026 was the first one solved
  at near-neutral pH [DOI:10.1038/s41467-026-78976-x "Previous structural studies of OmcZGs required alkaline conditions (ethanolamine buffer, pH 10.5) to prevent extensive filament aggregation in vitro27,28."].
  Gu 2023 report that CD spectra at pH 7 and pH 10.5 are similar.

### Function: long-range electron transfer to electrodes
- omcZ deletion cuts maximum current about ten-fold (14.4 to 1.3 mA), and plasmid
  complementation restores it (13.4 mA)
  [PMID:19461962 "When these mutations were complemented by expressing pilA or omcZ on a plasmid, wild type levels of current production were restored (Table 4)."].
  The mutant did not adapt even after more than 50 days.
- The same deletion has **no effect on growth with fumarate, Fe(III) citrate or Fe(III)
  oxide** [PMID:19461962 "Deletion of omcZ had no impact on growth with any of these electron acceptors (data not shown)."],
  and no effect on biofilm formation when fumarate is the acceptor. So the phenotype is
  specific to electrodes and is not a general growth defect.
- Purified OmcZS reduces Fe(III) citrate, U(VI), Cr(VI), Au(III), Mn(IV) oxide and
  AQDS in vitro, but not Fe(III) oxide [PMID:20400562].
  This is single-turnover electron delivery by the reduced cytochrome, not shown to be
  catalytic; together with the lack of an Fe(III)-citrate growth phenotype I treat it as
  evidence of electron transfer activity and **not** as a metal reductase activity.
  Gu 2023 report that OmcZ nanowires do reduce Fe(III) oxide, but more slowly than OmcS,
  and that OmcZ is not essential for Fe(III) oxide reduction.
- Immunogold labelling puts OmcZ in the extracellular matrix, and concentrated at the
  biofilm-electrode interface in electrode-grown biofilms
  [PMID:23761253 "OmcZ was highly concentrated at the biofilm-electrode interface"].
  The omcZ promoter is active uniformly through the biofilm (PMID:22577044), so this
  localization is not explained by where the gene is expressed.
- The matrix that anchors OmcZ is polysaccharide-dependent: a xap (GSU1501) mutant's
  sheared matrix is "nearly devoid of c-type cytochromes such as OmcZ" (PMID:21169487).
- Secretion of OmcZ needs the PilA-N/PilA-C pilus. In ΔpilA-N cells OmcZ stays in the
  periplasm (PMID:34471289), so a ΔpilA-N current phenotype can be explained by OmcZ
  and OmcS never reaching the outside of the cell.
- Ye et al. 2022 (PMID:35164556): OmcZ contributes both structurally (to the biofilm)
  and conductively, as opposed to pili (structural only) and OmcS (conductive only).
- Jiang et al. 2023 (PMID:37881251): ΔomcZ was impaired in ferrihydrite and anode
  reduction and in co-culture with G. metallireducens; in a ΔhybL background, omcZ
  deletion alone abolished DIET-based co-culture. **The ferrihydrite result conflicts
  with Nevin 2009 and with Gu 2023's statement that OmcZ is not essential for Fe(III)
  oxide reduction**; both papers come from the same field, so I record the conflict
  rather than resolving it.
- Tang et al. 2019 (PMID:31088920): in strain ACLHF (no H2 uptake), omcZ deletion
  prevented growth on Fe(0), and complementation restored it. This is electron *uptake*
  through OmcZ; in wild-type backgrounds the earlier finding was the opposite (deletion
  did not inhibit uptake).

### Conductivity claims and the controversy
- Yalcin et al. 2020 (PMID:32807967): an electric field applied to biofilms stimulates
  production of OmcZ nanowires with about 30 S/cm conductivity, roughly 1000-fold more
  than OmcS.
- Guberman-Pfeffer 2023 (PMID:37552847) computed that redox conductivity among OmcE,
  OmcS and OmcZ should differ by less than 10^3-fold, with redox currents of at most
  about 3 fA at a 0.1 V bias. Guberman-Pfeffer 2024 (PMID:38633696) argues that the
  reported metallic-like conductivities are artefacts.
- The Lovley group continues to argue that the electrically conductive filaments are
  e-pili (PilA) rather than cytochromes (debate summarised in PMID:38633696 and
  PMID:40740311).
- **Curation consequence:** the mechanism (redox hopping versus band-like conduction)
  and the absolute conductivity are disputed. That OmcZ transfers electrons is not
  disputed: it has eight redox-active hemes and delivers electrons to acceptors in vitro,
  and the genetic phenotype on electrodes is reproducible. The MF annotation is therefore
  GO:0009055 electron transfer activity, with no claim about the conduction mechanism.

### Wissink et al. 2026 (supplied paper) — what it adds for G. sulfurreducens OmcZ
The paper is mainly about the archaeal homologue OmcZ2 of "Ca. Methanoperedens
vercellensis", solved at 3.3 Å from electrode-grown, near-axenic cultures at pH 7.25.
For the Geobacter protein (called OmcZGs in the paper) it adds:
- A structural alignment with an archaeal OmcZ that shares only about 30% sequence
  identity. The fold and heme architecture are conserved across domains, with a
  "core quadrangle" of four conserved short sequence regions around hemes V and VIII,
  and three conserved His-His motifs that link heme pairs.
- Bacterial OmcZ forms its own phylogenetic group, Group VI; Groups I-V are archaeal
  (ANME and Borg elements). Archaeal clusters co-occur with serine peptidases,
  consistent with an OzpA-type maturation step.
- OmcZGs has only three N-glycosylation motifs and no detectable glycan density,
  whereas the archaeal protein is extensively modified.
- In OmcZGs hemes I, III and VI are largely solvent exposed and the nanowires aggregate
  into dense networks, while the archaeal filaments are straighter and their hemes more
  buried.
- Archaea assemble OmcZ nanowires without a prolyl isomerase in the cluster. This makes
  it questionable whether the Geobacter isomerase GSU2074 is needed for OmcZ folding,
  as Gu 2023 proposed; it may instead be a lineage-specific requirement.
- The OmcZ phenotype in G. sulfurreducens is not re-tested here; the paper relies on the
  earlier literature (its refs 27, 30, 33 = PMID:36732469, PMID:32807967, PMID:33837010).

## Annotation decisions (summary)
All rows are NEW, because GOA has nothing for this protein.
- MF GO:0009055 electron transfer activity — IDA (PMID:20400562) — core.
- MF GO:0020037 heme binding — IDA (cryo-EM, PMID:36732469; heme counting, PMID:20400562).
- CC GO:0097311 bacterial biofilm matrix — IDA (immunogold, PMID:23761253) — core location.
- BP GO:0019645 anaerobic electron transport chain — IMP (PMID:19461962). OmcZ is
  itself an electron carrier at the end of the chain, so it does part of the work; this
  matches the term used for OmcA (SHEON), ImcH and CbcL (GEOSL) in this repository.
- BP GO:0051258 protein polymerization — IDA (in vitro self-assembly after OzpA
  cleavage, PMID:36732469).
- Not added:
  - GO:0016722 oxidoreductase activity, acting on metal ions — single-turnover in vitro
    metal reduction with no growth phenotype on Fe(III) citrate.
  - GO:0042710 biofilm formation — the defect is conditional on current-harvesting mode
    and absent on fumarate, so it is probably secondary to failed respiration.
  - GO:0009986 cell surface — the filaments are extracellular and matrix-embedded; there
    is no evidence of an anchoring mechanism.
- Ontology gap: GO has no cellular-component term for an extracellular cytochrome
  filament ("nanowire"), so one is proposed (see `proposed_new_terms`).
