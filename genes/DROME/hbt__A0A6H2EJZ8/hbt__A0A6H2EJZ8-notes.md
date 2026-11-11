# hbt isoform E (A0A6H2EJZ8) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. This folder holds the canonical hbt product (isoform E, 1003 aa);
`genes/DROME/hbt/` is keyed to the N-terminally truncated isoform D (Q9VK03), which is identical to
isoform E residues 513-963 [file:DROME/hbt/hbt-bioinformatics/RESULTS.md].

### Deep research
- `just deep-research-falcon DROME hbt__A0A6H2EJZ8 --fallback perplexity-lite` failed: falcon
  "Failed to authenticate"; perplexity-lite HTTP 401 insufficient_quota. No deep-research file was
  produced. The sibling falcon report for the same gene (genes/DROME/hbt/) is known to mis-cite
  PMID:24671768 (Mabiki) as the hbt paper, so it was not used.

### Evidence
- Only gene-specific study: Zhang et al. 2020 Neurosci Bull, PMID:32761438 (PMC7475148), a Letter;
  cache abstract-only. Verbatim excerpts from the PMC HTML are recorded in genes/DROME/hbt/hbt-notes.md
  (screen hit with most severe touch defect; MiMIC, CRISPR KO, trans-het equally severe; reduced
  Ca2+ in TO chordotonal neurons; GFP knock-in in sheath/glial cells wrapping dendrites; "functions in
  the cells surrounding the DO and TO to regulate the neuronal mechanosensitivity").
- Architecture (UniProt A0A6H2EJZ8): Phobius TM helices 553-573, 594-615, 635-657, 669-692, 698-719,
  740-762; Coils 30-59, 94-121; disordered 377-482 and several Gly-rich C-terminal regions;
  Pfam PF21534 Rost; PANTHER PTHR12242:SF49.

### Evolutionary grounding
- QuickGO: PTN001387085 membrane IBA reaches ~500 gene products (animal, plant, protist members of
  PTHR12242), seeded by Rolling stone (O44252, SF46) membrane IDA (PMID:9230076). Rost's IMP to
  myoblast fusion (GO:0007520, PMID:7671823) was NOT propagated by PAINT; treated as deliberate.
  hbt is SF49, not SF46, so no Rost process is transferred.
- AIG1/ADTRP-like hint (PMID:27018888) is HHpred-level across a different PANTHER family; pairwise
  comparison in the sibling analysis was not significant. No activity inferred.

### Decisions
- GO:0016020 membrane IBA: ACCEPT (family-level, six TM helices; membrane type unresolved).
- GO:0051931 regulation of sensory perception IMP: ACCEPT. Experimentally established in
  D. melanogaster and the reference annotation for transfer. Non-neuronal site of action supports a
  regulatory term; GO:1905789 refinement raised as a question, not asserted.
- No NEW terms: no MF evidence; touch-response phenotype is not participation in mechanotransduction.
- Experimental vs inferred: regulation of sensory perception (IMP) and expression in sheath/glia
  (GFP knock-in) are experimental in this species; membrane location is inferred (family/PAINT plus
  sequence prediction); molecular function is unknown.
