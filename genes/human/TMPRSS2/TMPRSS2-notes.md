# TMPRSS2 review notes

Provider-based deep research was not available for this worktree: Falcon and
Perplexity were unavailable, and Claude Code was not logged in. I therefore
reviewed the seeded GOA rows against the cached original publications, Reactome
sidecars, the UniProt record, PAINT-loss output, and the SARS-CoV-2 entry
GO-CAM review.

`just paint-losses human TMPRSS2` could not run through the retained
`UV_PROJECT_ENVIRONMENT` because that environment did not expose
`ai_gene_review`; running the same module with `PYTHONPATH=src` against the
local `.venv` succeeded and reported:

```text
# PAINT losses on the TMPRSS2 (O15393) lineage

- PTHR24252: O15393 is not a leaf of this tree; losses not checked.
No IRD or IKR loss on this gene's lineage.
```

## GO-CAM 6796b94c00004996 context

The TMPRSS2 activity in `gocams/6796b94c00004996` has the right catalyst,
activity, substrate, and plasma-membrane location: UniProtKB:O15393 enables
`GO:0004252` serine-type endopeptidase activity and has SARS-CoV-2 spike as
input. The model's `part_of GO:0098670` edge should be narrowed, though. The
GO-CAM review currently endorses it, but ACE2 is the SARS-CoV-2 receptor that
mediates virion attachment; TMPRSS2 primes SARS-CoV-2 spike downstream of
attachment. TMPRSS2 does support `GO:0098670` for the HKU1 receptor-binding
context, and the SARS-CoV-2 entry model should instead connect the TMPRSS2
activity to positive regulation of viral entry or a spike-S2 priming process.
The model also has a downstream compartment inconsistency: TMPRSS2 at the plasma
membrane points to a single S2 fusogenic activity placed in the endosome and
`part_of GO:0039654`, thereby conflating the TMPRSS2-primed plasma-membrane
route with the cathepsin-dependent endosomal route.

## Evidence accessibility

The cached abstracts for PMID:21068237 and PMID:24227843 were enough to verify
TMPRSS2 plasma-membrane colocalization with ACE2 and proteolysis of ACE2 and
SARS-CoV spike, but not the PMID:21068237 IMP row for protein autoprocessing. I
accepted that row by deferring to the full-text curator and by citing the later
full-text HKU1 structural study, PMID:38964328, whose active recombinant TMPRSS2
construct autoprocessed during expression.

The three `GO:0070062 extracellular exosome` rows remain `UNDECIDED`.
PMID:19056867 is abstract-only, PMID:19199708 and PMID:23533145 are full-text
cached, and all three clearly describe exosome proteomics studies, but the
cached text does not expose TMPRSS2-specific peptide or protein-list evidence.
