## 2026-11-28 NGF family review

Perplexity deep research was unavailable for this family, so this review used manual
triage of the fetched GOA rows, the human UniProt record, cached publications, Reactome
events, and the PTHR11589 PAINT node file.

NTF3 encodes secreted neurotrophin-3, a PTHR11589 ligand that preferentially activates
NTRK3/TrkC but can also signal through other Trk receptors in some contexts. PMID:23027130
is cached as an abstract and directly supports NT-3-dependent TrkC phosphorylation with
Ras, ERK1/2 and Akt activation in TrkC-expressing U2OS cells; that paper also reports
motility, migration, invasion and soft-agar colony growth.

The accessible PMID:23027130 text did not verify a directional chemotaxis assay, so
GO:0042056 chemoattractant activity, GO:0050918 positive chemotaxis and GO:0050930
induction of positive chemotaxis are UNDECIDED rather than kept from a migration-only
quote. PMID:1542658 supports survival, neurite outgrowth and proliferation of neural
crest and placode-derived neuronal cells, which was used for the broader developmental
and projection-morphogenesis rows.

As in BDNF and NTF4, the GO:0038180 nerve growth factor signaling pathway IBA is scoped to
NGF rather than NTF3 and is removed with the family sidecar as the supporting PAINT
assessment.
