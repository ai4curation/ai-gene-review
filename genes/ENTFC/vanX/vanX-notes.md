# vanX (Enterococcus faecium, Q06241) — curation notes

## Literature search record

No deep-research provider key exists here and there is no model organism
database description for Enterococcus. `just fetch-fitness ENTFC vanX` was not
attempted; no fitness data set exists for this organism.

Sources checked:

- `genes/ENTFC/vanX/vanX-uniprot.txt` (Swiss-Prot Q06241): FUNCTION, CATALYTIC
  ACTIVITY (RHEA:20661, EC 3.4.13.22), COFACTOR, ACTIVITY REGULATION,
  BIOPHYSICOCHEMICAL PROPERTIES (K_m, V_max and k_cat for four substrates),
  SUBUNIT, INDUCTION, MISCELLANEOUS, the peptidase M15D family note, the
  ACT_SITE at residue 181 and the three zinc-binding residues. The record has no
  SUBCELLULAR LOCATION block and no transmembrane or signal-peptide feature.
- GOA cites no publication for this gene: all five rows are electronic. The
  primary literature was therefore found through the UniProt evidence tags and
  fetched: PMID:7873524 (purification and kinetics), PMID:1556077 (operon
  control), PMID:8852545 (review). PMID:7854121 and PMID:9702193, also cited by
  UniProt, were not needed beyond what the record states.
- Context read but not edited: a glycopeptide-resistance pathway module and a
  review of the vanA-operon GO-CAM, both proposed in
  ai4curation/ai-gene-review#5904 and not part of this branch; nothing in this
  review rests on them.
- GO relations checked against the local GO build, 2026-11-04: `GO:0016805
  dipeptidase activity` is an `is_a` ancestor of `GO:0160237 D-Ala-D-Ala
  dipeptidase activity`; `GO:0008237 metallopeptidase activity` is **not**;
  `GO:0006508 proteolysis` is defined as "The hydrolysis of proteins into smaller
  polypeptides and/or amino acids by cleavage of their peptide bonds", and
  `GO:0043171 peptide catabolic process` covers "compounds of 2 or more (but
  usually less than 100) amino acids".

## What VanX does

VanX is the enzyme that makes the resistance switch clean. VanA's depsipeptide
has to compete with the cell's own D-Ala-D-Ala for the D-Ala-D-Ala-adding
enzyme, and VanX removes the competitor:

[PMID:7873524 "VanX has been characterized as a metal-activated D-, D-dipeptidase with an optimal pH range of 7-9."]
[PMID:7873524 "However, in the presence of metal cations, kcat can be as high as 788 s-1."]

Its selectivity is the point:
[PMID:7873524 "The more than 10(5)-fold differential in catalytic efficiency of VanX for hydrolysis of D-Ala-D-Ala vs D-Ala-D-lactate leaves D-Ala-D-lactate intact for subsequent incorporation into peptidoglycan."]
and UniProt states the same as a MISCELLANEOUS note. With VanY it forms a series
that clears both the free dipeptide and precursors that already carry it
[PMID:8852545 "These two proteins act in series to eliminate D-Ala-D-Ala-containing precursors."].
Unlike VanY, VanX is indispensable
[PMID:8852545 "VanX is required for resistance whereas VanY only slightly increases the level of resistance mediated by VanH, VanA and VanX."]
[PMID:1556077 "The distal part of the van cluster encodes VanH, VanA, and a third enzyme, VanX, all of which are necessary for resistance."]

## Annotation issues

All five GOA rows are electronic, with no publication cited, so each was judged
against the primary literature and the curated record rather than against the
row's own evidence.

- `GO:0160237 D-Ala-D-Ala dipeptidase activity` is the core function and matches
  the curated reaction and EC number exactly: accepted.
- `GO:0016805 dipeptidase activity` is its `is_a` parent, so the row is modified
  to the specific child the gene already carries.
- `GO:0008237 metallopeptidase activity` is not an ancestor of `GO:0160237`, so
  it is an independent and true claim: VanX is a zinc enzyme of the peptidase
  M15D family whose k_cat rises more than a hundredfold in the presence of
  divalent cations. Accepted.
- `GO:0008270 zinc ion binding` is supported by three curated zinc-binding
  residues and by the cofactor statement, which carries experimental evidence.
  Accepted.
- `GO:0006508 proteolysis` is the problem row. It comes from the peptidase-domain
  signature, but VanX hydrolyses a **free dipeptide**, not a protein, and the GO
  definition of proteolysis is restricted to the hydrolysis of proteins. The
  aspect and the region of the ontology are right and the essence of the claim is
  sound, so the row is modified to `GO:0043171 peptide catabolic process` rather
  than removed. The same issue arises on vanY, where the substrate is a
  UDP-MurNAc-peptide precursor and the replacement chosen there is a
  peptidoglycan term instead.

Nothing in GOA connects vanX to antibiotic resistance, and the record has no
cellular-component annotation at all. `GO:0046677 response to antibiotic` and
`GO:0005829 cytosol` are added as `NEW` rows; the cytosol inference rests on the
absence of any membrane-targeting feature together with the compartment of the
substrate pool, and `GO:0046677` is the most specific resistance-response term GO
offers.
