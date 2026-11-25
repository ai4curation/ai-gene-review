# boss (P22815) notes

## Provenance of this review (2026-11-07)

- No deep-research provider key was available in the session, and FlyBase has no hand-written
  gene description for boss (`just mod-description-deep-research DROME boss` returned no curated text).
  The literature was searched directly: PubMed `("bride of sevenless"[Title/Abstract] OR boss[Title]) AND Drosophila`
  (42 hits, sorted by date), keeping the papers on BOSS biology and caching them with `fetch-pmid`.
- Reviewed as the positive control for curated rule CR-0006 (projects/RAR_MISANNOTATION.md).

## Key points

- BOSS is the R8-presented ligand of the Sevenless RTK [PMID:3167983 "boss expression is required in the R8 cell for a neighboring cell to become R7"];
  [PMID:7680109 "boss activates tyrosine phosphorylation of the sev receptor"].
- Binding epitope: C-terminal peptide of the BOSS ectodomain and Sev FNIII-3 [PMID:39827240].
  Membrane anchoring, not the 7TM bundle as such, is what activation needs
  [PMID:39510067 "a single-pass transmembrane form of Boss activates Sev"].
- Localization: apical plasma membrane of R8 [PMID:42043338 "the Boss protein is localized on the apical plasma membrane of the R8 cell"].
- Glucose response, metabolic and lifespan phenotypes come from one lab
  (PMID:18832180, PMID:26193363, PMID:28045997); the G-protein mechanism is open
  [PMID:18832180 "Further studies, however, are required to elucidate the mechanism of BOSS-mediated signaling."].
- Evolution: [PMID:42043338 "Thus, the Boss/Sev signaling module appears to be restricted to Dipterans."]
  Outside Diptera the BOSS cognate is recognized by its transmembrane stack
  [PMID:18392882 "The extracellular region, however, is only detectably conserved within but not outside Diptera."];
  the authors attribute this to fast co-evolution with Sevenless and raise the possibility of conserved
  Sevenless signaling in endopterygote insects, which is in tension with the statement above. The CR-0006
  Diptera scope therefore rests on ectodomain detectability and on the absence of functional evidence
  outside Drosophila, not on absence of the gene.

## Consequence for CR-0006

The 2026-11-06 version of CR-0006 used Arthropoda. 135 of its 211 matches are non-dipteran
(bees, wasps, beetles, true bugs, thrips and others), none with evidence of a Sevenless-binding
ectodomain. The rule was narrowed to Diptera (NCBITaxon:7147): 76 matches, including P22815.
UniProt queries: `xref:interpro-IPR002956 AND xref:interpro-IPR050726 AND taxonomy_id:7147` (76)
and the same with `taxonomy_id:6656` (211), 2026-11-07.

## Open points

- GO:0035997 rhabdomere microvillus membrane (FlyBase IDA, PMID:1857416) is left UNDECIDED: abstract only;
  the documented location in the eye disc is the apical R8 membrane, before rhabdomeres form.
- The PTN001173582 IBA for glutamate-activated, cyclase-inhibiting receptor activity is marked over-annotated.
