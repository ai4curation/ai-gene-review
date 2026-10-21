# DRS1 (Q9SAI7, At1g80710) notes

## Identity

- Q9SAI7 is the single UniProt entry for At1g80710 (DRS1, DROUGHT SENSITIVE 1), 516 aa, RefSeq NP_178186.1.
  UniProt lists no alternative products; the benchmark accession is the canonical full-length product,
  not an isoform or fragment. It contains the WD40 repeats of the family (Pfam PF00400 x2, SMART x4) and an
  N-terminal disordered region (31-102, MobiDB-lite).
- PANTHER PTHR14773 has a single subfamily, SF0 (WD REPEAT-CONTAINING PROTEIN 76), which contains DRS1,
  yeast CMR1 (Q12510, YDL156W), human WDR76 (Q9H967) and many fungal/vertebrate members. All three IBA rows
  descend from PAINT node PTN000381277 with CMR1 and/or WDR76 as experimental donors. There is no subfamily
  split to argue with; the family review (interpro/panther/PTHR14773/PTHR14773-review.yaml) agrees on SF0.
- The UniProt FUNCTION comment (5hmC reader) is ARBA-only and is not used as evidence.

## Target-specific evidence

- [PMID:20118918 "We designate At1g80710 as Drs1 (drought sensitive 1)"]: drs1-1 retained ~80% of WT water
  under drought; detached leaves insensitive to ABA for water loss; independent allele drs1-2 same phenotype;
  ABA-dependent germination unaffected ["ABA showed no effect on germination rate in the mutant (data not shown)"].
- Same paper: "Drs1 is a WD-40 repeat family protein containing a DWD (DDB1 binding WD40) motif". DDB1 binding
  is not tested for DRS1.

## Evolutionary (ortholog) evidence

- Yeast CMR1: "higher affinity for UV-damaged DNA and had increased localization to chromatin upon UV treatment";
  linked to a DNA damage checkpoint [PMID:27248496, review of prior yeast work].
- Human WDR76: co-localizes with CBX1/CBX5, recruited to UV-laser damage, associates with Cul4-DDB1 [PMID:27248496].
- PAINT propagated generic DNA binding, nucleus, heterochromatin and regulation of DNA damage checkpoint, not
  damaged-DNA binding or 5hmC binding; I treat the omission as deliberate. Arabidopsis DNA has no appreciable
  5hmC [PMID:25380728], a further reason not to transfer a 5hmC-reader role.

## Decisions (2026-10-20 full re-review)

- ACCEPT: DNA binding (IBA), nucleus (IBA, ISM), response to water deprivation (IMP), response to ABA (IMP).
- KEEP_AS_NON_CORE: heterochromatin (IBA; single human donor), Cul4-RING E3 complex (ISS via DWD motif; PRL1 is not
  an ortholog), regulation of DNA damage checkpoint (IBA; untested in plants).
- Removed prediction-derived file references from the review; this review is independent of computational
  name/function predictions.
- Deep research (falcon) missed the primary DRS1 paper; its "no target-specific study" conclusion is not adopted.

## Closest characterised relative

- Human WDR76 (Q9H967), same PANTHER subfamily SF0 and PAINT node; yeast CMR1 (Q12510) is equally close
  phylogenetically. Neither has a review in the repo (no genes/human/WDR76 or genes/yeast/CMR1).
- No modules in modules/ reference DRS1, WDR76 or PTHR14773.
