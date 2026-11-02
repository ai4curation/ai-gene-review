# rig (Q86BY9, FBgn0250850) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

### Setup and provenance

- `just fetch-gene DROME rig` created the UniProt, GOA (33 GOA rows, seeded as 32
  `existing_annotations`; the stub merges per-partner IPI rows by key) and review stub.
- `just fetch-gene-pmids DROME rig` cached all six GOA PMIDs. Full text is available
  for PMID:24391840, PMID:26098872 and PMID:30563832; PMID:14645129, PMID:20452345
  and PMID:21939654 are abstract-only.
- Deep research FAILED: `just deep-research-falcon DROME rig --fallback perplexity-lite`
  exited with an Edison API authentication error ("Failed to authenticate", HTTP 403)
  and the perplexity-lite fallback also failed. No `-deep-research-*.md` file exists.
  The review was written from the cached primary literature listed below, plus
  PMID:18621711 (Kroiss et al. 2008; fetched with `just fetch-pmid`) and
  PMID:33963192 (Kour et al. 2021; already cached).
- ProtNLM2 predictions were not opened or used.

### Evolutionary grounding

- rig is in PANTHER PTHR46362:SF1 (GEM-ASSOCIATED PROTEIN 5), the only subfamily of
  the family, together with human GEMIN5 (Q8TEQ6). UniProt DR line:
  "PANTHER; PTHR46362:SF1; GEM-ASSOCIATED PROTEIN 5; 1."
- rig (FB:FBgn0250850) is an experimental donor to PAINT node PANTHER:PTN005299808,
  which propagates spliceosomal snRNP assembly, mRNA 3'-UTR binding, nucleus and SMN
  complex. PAINT did not propagate snRNA binding (GO:0017069) or m7G cap binding from
  human GEMIN5 to this node, so those are not transferred here (treated as a deliberate
  omission).
- Kroiss et al. 2008: "Rigor mortis displays moderate homology to Gemin5 over the
  entire protein length." [PMID:18621711]
- Bioinformatics (`rig-bioinformatics/RESULTS.md`): global pairwise alignment to human
  GEMIN5 (31% identity over aligned pairs) shows that the human Sm-site stacking pair
  Trp14-Tyr15 and the basic/aromatic 5'-end contacts are not retained at aligned
  positions; the fly protein has no Trp-Tyr dipeptide at all. The m7G-stacking Tyr474
  aligns to fly Tyr660. Pairwise only; supports not transferring snRNA binding.

### What is experimentally established in Drosophila

1. **SMN complex membership (strong).** Endogenous Rig/Gemin5 co-purifies with Flag-SMN
   expressed from its native promoter in embryos: "we also identified Gemin2, Gemin3,
   Gemin5 and CG2941 as highly-enriched SMN binding partners (Figure 5)."
   [PMID:30563832]. UniProt SUBUNIT: core SMN complex = Smn, Gem2, Gem3, rig/Gem5 and
   a Gem4 paralog. Caveat: in S2 cells, "No binding of Rigor mortis to dSMN has been
   observed, arguing against a stable association of this protein with the dSMN
   complex." [PMID:18621711]; the embryo data supersede this for in vivo membership.
2. **Genetic interaction with complex members.** Overexpression of full-length or
   N-terminally truncated Gemin5 enhances the Gemin3 hypomorph (Gem3BART) flight and
   viability defects; Gemin5 knockdown in that background is lethal [PMID:26098872].
3. **Localisation.** U bodies in egg chambers, colocalising with SMN, Gemin2, Gemin3
   [PMID:20452345]; cytoplasm and regulated nuclear shuttling in larval salivary gland
   and midgut [PMID:14645129]; GFP-Gemin5 forms "predominantly nuclear" puncta when
   overexpressed in muscle, interpreted as gems [PMID:24391840], but under rescue
   (near-endogenous) conditions foci are "mostly restricted to the cytoplasm"
   [PMID:26098872].
4. **Organismal requirement.** rig mutants: molting defects, larval lethality,
   defective puparium formation, defective E74 isoform switch [PMID:14645129]. RNAi in
   muscle or neurons: lethality, climbing and flight defects [PMID:24391840];
   pupal lethality, NMJ bouton defects, reduced climbing [PMID:33963192]. These are
   necessity phenotypes; they do not identify the step Rig performs.
5. **Nuclear receptor interactions (in vitro).** GST pull-downs with EcR, USP, DHR3,
   SVP and betaFTZ-F1; LXXLL motif [PMID:14645129]. Single study, abstract only here;
   model "most likely as a cofactor for one or more nuclear receptors" is not
   independently confirmed.

### What is NOT established in Drosophila (inferred only)

- Direct snRNA binding, Sm-site recognition or cap binding (human data; residues not
  conserved; fly SMN complex binds snRNAs without Rig in S2 cells [PMID:18621711]).
  A web-listed CityU grant abstract claims Rig binds U snRNA with high affinity; no
  peer-reviewed paper found, not used.
- A direct snRNP assembly assay after rig depletion has not been reported in the
  literature read here; spliceosomal snRNP assembly is supported by IBA/ISS plus fly
  SMN complex membership.
- mRNA 3'-UTR binding (IBA; donors human and mouse; no fly data).

### Decisions (summary)

- ACCEPT: snRNP assembly (IBA/ISS/NAS), SMN complex (all), U body (all), nucleus,
  cytoplasm.
- KEEP_AS_NON_CORE: mRNA 3'-UTR binding (IBA, inferred only), response to ecdysone
  (IMP), Gemini of Cajal bodies (IEA; overexpression-based).
- MODIFY: 5 protein binding IPI rows (PMID:14645129) -> nuclear receptor binding
  GO:0016922.
- MARK_AS_OVER_ANNOTATED: molting cycle, flight behavior, adult locomotory behavior
  (downstream organismal phenotypes of losing an essential housekeeping complex member).
- No NEW annotations: snRNA binding fails the transfer test (PAINT omission, residue
  divergence, Kroiss biochemistry).
