# omcS (GSU2504, UniProt Q74A86) — Geobacter sulfurreducens PCA

## Starting point

- Q74A86 is a **reviewed (Swiss-Prot)** entry, integrated 2017, named "C-type cytochrome
  OmcS" with AltName "Outer membrane cytochrome S". 432 aa, signal peptide 1-25, mature
  chain 26-432. **No transmembrane feature, no lipid-anchor feature, no lipobox.**
- Six CXXCH heme motifs, at precursor positions 34, 72, 165, 264, 353 and 425, matching
  the curated "Binds 6 low-spin heme groups per subunit".
- Two cryo-EM filament structures: **PDB 6EF8** (3.70 Å, seven chains, 26-432) and
  **6NEF** (3.42 Å, 26-432).
- GOA carries **10 annotations** (`omcS-goa.tsv`, fetched 2026-11-09): two IBA, and four
  cellular-component terms each asserted once by IEA and three times by EXP.
- Classification is worth noting because the resources disagree in an informative way:
  - **CDD `cd21555` is called "OmcS-like"** — a dedicated conserved domain.
  - **TCDB `5.B.3.1.1`** places it in "the geobacter nanowire electron transfer (g-net)
    family" — again dedicated.
  - **PANTHER puts it in `PTHR30333:SF1` "CYTOCHROME C-TYPE PROTEIN NAPC"**, and InterPro
    gives it only `IPR036280` (multiheme cytochrome superfamily) plus `IPR051174`, which
    is just InterPro's integration of that same PANTHER family.
  - So two resources recognise OmcS as its own thing, and PANTHER files it with the
    NapC/NirT quinol dehydrogenases. See `interpro/panther/PTHR30333/PTHR30333-review.yaml`,
    where this is recorded as the family's heterogeneity: OmcS matches neither PF03264 nor
    IPR005126, the NapC/NirT N-terminal domain that every genuine member of that family has.
- No provider deep-research file exists for this gene; the literature below was assembled
  by hand from the Swiss-Prot reference list plus the OmcZ-review search.

## Biology, with provenance

### What it is
- Purified OmcS is 47015 Da with six low-spin bis-histidinyl hexacoordinated hemes and a
  midpoint potential of -212 mV
  [PMID:21236241 "Purified OmcS had a molecular mass of 47015 Da, and six low-spin bis-histidinyl hexacoordinated heme groups. Its midpoint redox potential was -212 mV."].
- It is **loosely bound, not membrane-integrated**
  [PMID:21236241 "OmcS, an abundant c-type cytochrome that is only loosely bound to the outer surface"],
  and was originally found among proteins "easily sheared from the outer surfaces of intact
  cells" [PMID:16332857].
- Secondary structure is mostly disordered: about 10% alpha-helix (PMID:21236241).

### What it does
- Dithionite-reduced OmcS passes electrons to insoluble Fe(III) oxide, Mn(IV) oxide and
  humic substances
  [PMID:21236241 "Dithionite-reduced OmcS was able to transfer electrons to a variety of substrates of environmental importance including insoluble Fe(III) oxide, Mn(IV) oxide and humic substances."].
  Stopped-flow rates: 25.2 s⁻¹ with AQDS, 2.9 s⁻¹ with Fe(III) citrate, with hyperbolic
  dependence on substrate concentration. **This is oxidation of the pre-reduced protein,
  i.e. stoichiometric electron delivery, not demonstrated catalytic turnover** — the
  distinction matters for whether a metal-reductase term is warranted (see below).
- Deleting omcS abolishes Fe(III) oxide reduction while leaving soluble acceptors intact
  [PMID:16332857 "When either omcS or omcE was deleted, G. sulfurreducens could no longer reduce Fe(III) oxide but could still reduce soluble electron acceptors, including Fe(III) citrate."],
  and expressing omcS in trans restores it. OmcT cannot substitute: Fe(III) oxide is not
  reduced when omcT is expressed but OmcS is absent (PMID:16332857).
- OmcS is essential for direct interspecies electron transfer, and is massively induced in
  DIET cocultures
  [PMID:23377933 "Transcript abundance for the pilus-associated cytochrome OmcS, which is essential for DIET but not for HIT, was 240-fold higher in the cocultures with G. metallireducens than in cocultures with P. carbinolicus."].

### Where it is, and why the answer changed
- 2010: immunogold puts OmcS along the pili
  [PMID:20400557 "Immunogold localization revealed that OmcS, a cytochrome that is required for Fe(III) oxide reduction by Geobacter sulfurreducens, was localized along the pili."].
  The authors read the spacing as OmcS handing electrons *from* pili to Fe(III) oxide
  rather than conducting along them (PMID:20400557).
- 2019: cryo-EM shows the conductive filaments are not pili at all but polymers of OmcS
  [PMID:30951668 "G. sulfurreducens nanowires are assembled by micrometer-long polymerization of the hexaheme cytochrome OmcS, with hemes packed within ∼3.5-6 Å of each other."],
  with inter-subunit heme stacking and heme axial coordination by histidines from the
  neighbouring subunit. WT OmcS filaments are 100-fold more conductive than filaments from
  a ΔomcS strain [PMID:30951668]. The paper states plainly that
  "the conductive extracellular appendages of wild-type G. sulfurreducens strain are primarily OmcS filaments"
  [PMID:30951668].
- 2021: OmcS reaches the extracellular fraction only via the PilA-N/PilA-C filament; in
  ΔpilA-N cells it stays in the periplasm
  [PMID:34471289 "Our subcellular localization experiments revealed that both OmcS and OmcZ are present in the extracellular fraction of wild-type cells but remain in the periplasm for ΔpilA-N cells"].

**Consequence for the CC annotations.** The mature, functional OmcS is a polymerised
extracellular filament attached to the cell surface. It has no transmembrane segment and no
lipid anchor, and it shears off easily. `GO:0009986 cell surface` fits exactly — its GO
definition covers products "attached (integrated or loosely bound) to the plasma membrane
or cell wall". `GO:0009279 cell outer membrane` asserts residence in the outer lipid
bilayer, which nothing shows. That term traces to the protein's 2005 name and to
outer-surface shear fractions, and predates the structure. It is marked over-annotated, not
removed: OmcS genuinely sits at the outer-membrane surface, so the term is imprecise rather
than false.

### Conductivity and the wider dispute
- Ye et al. 2022 separate the roles: OmcS filaments are conductive but not structural,
  pili structural but not conductive
  [PMID:35164556 "the OmcS nanowire played a conductive but not a structural function in facilitating electron transfer in the biofilm"].
- Jiang et al. 2023 find ΔomcS impaired for ferrihydrite and for coculture, but able to
  regain anode reduction [PMID:37881251].
- As with OmcZ, the absolute conductivity values and the conduction mechanism are disputed
  (PMID:37552847, PMID:38633696). That OmcS carries electrons is not in dispute: six
  redox-active hemes, direct in vitro transfer to several acceptors, and a clean genetic
  phenotype. The MF annotation therefore stays at `GO:0009055` and makes no mechanistic claim.

## Annotation decisions

Existing (10 rows):
- `GO:0009055` electron transfer activity, IBA → **ACCEPT**. The node PTN001251186 was
  assessed `SOUND` in the PTHR30333 family review; OmcS also has direct evidence of its own.
- `GO:0019645` anaerobic electron transport chain, IBA → **ACCEPT**, same node.
- `GO:0009986` cell surface, IEA + 3 × EXP → **ACCEPT** (all four rows).
- `GO:0009279` cell outer membrane, IEA + 3 × EXP → **MARK_AS_OVER_ANNOTATED** (all four
  rows, kept consistent). Recorded as a `source_defects` entry against UniProt
  (`OUTDATED_STATEMENT`, `CHECK`) rather than a demand to delete.

New (2 rows):
- `GO:0020037` heme binding — six hemes, curated COFACTOR, two structures.
- `GO:0051258` protein polymerization — OmcS is itself the polymer; the filament is a
  homopolymer whose inter-subunit contacts include heme stacking and cross-subunit axial
  histidine coordination.

Not added, and why:
- `GO:0016722` oxidoreductase activity, acting on metal ions. Declined, as for OmcZ. What
  was measured is the rate at which pre-reduced OmcS is oxidised by a substrate, not
  catalytic turnover; no kcat/Km for a catalysed reaction is reported. The repo does use
  this term for Shewanella OmcA, but there the evidence is different — a measured kcat of
  10.2 s⁻¹ and Km of 41 µM for Cr(VI) reduction.
- `GO:0005576` extracellular region. Its GO comment says it is for products *not* attached
  to the cell surface; OmcS filaments are cell-attached, so `GO:0009986` is the correct term.
- A DIET term. GO has nothing for direct interspecies electron transfer (checked via OLS),
  and the role is a property of the partnership rather than of a step OmcS performs alone.
  Recorded as a question instead.
- A pilus term. OmcS is secreted *through* the PilA-N/PilA-C filament and was once seen
  along pili, but it is not a pilus component.

Ontology gap: GO still has no cellular-component term for an extracellular cytochrome
filament. The same proposal was made in the OmcZ review; it is repeated here deliberately,
because two independent genes needing the term is the strongest argument for creating it.
