# sen15 evidence notes

Sen15 is a small, conserved noncatalytic subunit of the heterotetrameric tRNA-splicing endonuclease complex. Together with Sen2, Sen34 and Sen54 it supports recognition and excision of introns from precursor tRNAs before the cleaved exons are ligated. The catalytic splice-site cleavage centers reside in Sen2 and Sen34. Nuclear and cytosolic pools have been reported in fission yeast localization screens.

## Identity and prediction provenance

PomBase primary symbol sen15, locus SPAC959.10, current UniProt Q7LKV3. The supplied pre-release post-processed-2026_02_28k.xml is the source of the reviewed claims; its placeholder sequence, taxonomy and dates are not biological metadata. The current UniProt sequence is not established as the model input. Current API availability and published-list inclusion are separate properties; all biological judgments here concern the preserved original claims.

## Primary evidence inspected

- [PMID:9200603 The yeast tRNA splicing endonuclease: a tetrameric enzyme with two active site subunits homologous to the archaeal tRNA endonucleases.] "Our results demonstrate that the eucaryal tRNA splicing endonuclease contains two functionally independent active sites for cleavage of the 5' and 3' splice sites, encoded by SEN2 and SEN34, respectively."
- [PMID:16823372 ORFeome cloning and global analysis of protein localization in the fission yeast Schizosaccharomyces pombe.] "Next, we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein."

## Evidence limits and adjudication

- GO:0003676 (UNDECIDED): The Sen15 subunit supports an RNA-processing complex, but specific RNA contacts by the target or conserved contacts in a characterized Sen15 ortholog have not been established in the primary evidence inspected here. Complex membership alone does not resolve whether this particular subunit binds nucleic acid. Binding within an assembled complex would be sufficient; an isolated-subunit assay is not required.
- GO:0005634 (KEEP_AS_NON_CORE): Retain the PomBase localization observation from the fission yeast tagged-ORFeome screen. The accessible abstract documents the assay but not the individual localization image; the screen is not sufficient to identify which detected pool executes tRNA cleavage.

Primary reports are interpreted at the species, assay and subunit level. Abstract-only experimental annotations are not rejected because a title foregrounds another subunit. PAINT asserts inheritance from a curated ancestral node; donor count and target self-inclusion are not objections. ARBA overlap is recorded only as provenance, never as biological validation. CNN and LSP reflect established biological knowledge, without asserting training-data membership.

## Provider report appraisal

The Falcon report supports a noncatalytic architecture and highlights human TSEN15 structures lacking detectable direct RNA contacts. Its generic claim that no target localization data exist is incomplete because PomBase retains tagged-ORFeome observations. No compartment was inferred from budding-yeast mitochondrial localization.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used.

### Identity
- Q7LKV3 (SEN15_SCHPO), 143 aa, Swiss-Prot reviewed, sequence version 1, PE 3 (inferred from homology). This is the canonical and only product of sen15/SPAC959.10; it is not a fragment, isoform or alternative gene model. Length is comparable to fungal family members in PTHR28518:SF1 (S. cerevisiae SEN15 Q04675 128 aa, Eremothecium Q759Y8 118 aa; Neurospora tsp-1 Q7RY78 223 aa).
- Sen15 has no catalytic triad: the 5' and 3' splice-site active sites are in Sen2 and Sen34 [PMID:9200603 "Our results demonstrate that the eucaryal tRNA splicing endonuclease contains two functionally independent active sites for cleavage of the 5' and 3' splice sites, encoded by SEN2 and SEN34, respectively."]. Sen15 retains only the C-terminal part of the archaeal endonuclease fold [PMID:17166513 "Sen15 and Sen54, which are otherwise non-homologous, contain C-terminal sequences similar to the stretch of MJ_endo that spans the last two β -strands"], which explains the IPR011856/IPR036167 superfamily matches.

### Evolutionary placement
- PANTHER: Q7LKV3 in PTHR28518:SF1 (fungal Sen15; the only subfamily in panther.obo). S. cerevisiae SEN15 (Q04675, SGD:S000004663) is in the same subfamily and is the PAINT donor (node PTN002003396) for both IBA rows.
- Human TSEN15 (Q8WW01) is in a different PANTHER family, PTHR28582, though it shares Pfam PF09631 and IPR018593 (checked via UniProt REST). Human structural data are therefore used only for the conserved, complex-architecture level (Sen15-Sen34 pairing, noncatalytic role), not for subfamily-specific functions. Song & Markley report only 23% identity between human and S. pombe Sen15 [PMID:17166513 "it shows only 23% and 20% sequence identities, respectively, to two yeast orthologs, Sp Sen15 from Schizosaccharomyces pombe and Sc Sen15 from Saccharomyces cerevisiae."].
- QuickGO check of SEN15 (Q04675): SGD has contributes_to GO:0000213 tRNA-intron endonuclease activity (IDA, PMID:9200603), but PAINT propagated only GO:0000214 and GO:0000379 from PTN002003396. The MF omission is treated as deliberate; no NEW MF was added (raised as a suggested question).

### Changes from previous review
- GO:0003676 nucleic acid binding (IEA, IPR011856): UNDECIDED -> MARK_AS_OVER_ANNOTATED. Superfamily mapping; in human TSEN-pre-tRNA cryo-EM, recognition is by the other three subunits [PMID:37028420 "The mature domain of pre-tRNA is recognized by conserved structural elements of TSEN34, TSEN54, and TSEN2."]. Not REMOVE because this is indirect negative evidence from a different PANTHER family.
- GO:0006388 tRNA splicing via endonucleolytic cleavage and ligation (IEA): ACCEPT -> MODIFY to GO:0000379 (part_of child, already carried); Sen15 does not take part in ligation.
- Complex and splice-site-cleavage rows (IBA+IEA) kept ACCEPT, with added support (UniProt SUBUNIT, Sen34-Sen15 two-hybrid, human TSEN15-34 heterodimer [PMID:34584079]).
- Nucleus/cytosol HDA kept as non-core. S. cerevisiae endonuclease is mitochondrial-surface associated, so localization is not transferred between yeasts.
- Description rewritten; core function now names the Sen34 partnership; suggested questions/experiment added.

### Family review / modules
- interpro/panther/PTHR28518/PTHR28518-review.yaml: single subfamily SF1 with sen15 as representative; no disagreement about placement. Its FAMILY_WIDE GO:0006388 assessment is compatible with the MODIFY here (the term is true; the gene-level row is just refined to the specific step).
- No module in modules/ covers tRNA splicing or the TSEN complex.

### Relative to review next
- S. cerevisiae SEN15 (Q04675), same PANTHER subfamily PTHR28518:SF1 and PAINT donor; experimentally characterized (PMID:9200603). No review exists in genes/yeast/.
