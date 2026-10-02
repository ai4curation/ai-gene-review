# prom1a notes (Danio rerio, prominin 1a; UniProt Q9W735)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 4, random TGD_tree sample)

**Deep research:** not available (Edison 402 Payment Required; OpenAI key invalid). Not attempted, per
instructions. Literature found by hand through Europe PMC; pair analysis in `prom1a-bioinformatics/RESULTS.md`.

Accession Q9W735 (Swiss-Prot, 826 aa; alias proml1), ZFIN:ZDB-GENE-030131-1577, Ensembl ENSDARG00000039966,
chr14. Paralog prom1b (chr1). PANTHER TGD_tree pair (PTHR22730, PROM1 co-orthologs); Ensembl Compara places
the duplication at Osteoglossocephalai with one gar ortholog (ENSLOCG00000003057, LG4) for both copies. prom2 is a
separate, older paralog (Vertebrata level).

Nomenclature: [PMID:21407811 "In contrast to other vertebrates, the zebrafish prominin-1 gene is duplicated and consequently, both co-orthologues of mammalian prominin-1 are referred as to prominin-1a and b [27]."]

### Expression
- Embryo: [PMID:20503380 "prominin1a and b show novel complementary and overlapping patterns of expression in proliferating zones in the developing sensory organs and central nervous system."]
- Adult retina, both in the ONL: [PMID:21407811 "Within the ONL of three month-old fish, both prominin-1 molecules were detected (Fig."]
  INL split: [PMID:21407811 "Prominin-1a was strongly expressed along the vitreal side of the INL (Fig."]
  [PMID:21407811 "In contrast, prominin-1b was weakly, but reproducibly, detected at the scleral, but not the vitreal, side of the INL (Fig."]
  Authors' reading: [PMID:21407811 "Interestingly, the expression of the Dr co-orthologues of mammalian prominin-1 at unique sites within the INL suggests a lineage specific sub-functionalization, beside the potential functional redundancy at the overlapping domains within the photoreceptor cells."]
- Adult brain: [PMID:23723983 "Distribution of the two molecules (prominin-1a and prominin-1b) along the rostro-caudal axis of the ventricle system of the zebrafish brain displays a fairly complementary pattern with only a low-degree of overlapping."]
- Bulk data (my scripts): prom1a maternal (11-12 TPM cleavage-blastula) and broad in adult organs, like gar PROM1;
  prom1b zygotic only, restricted to retina/brain. Photoreceptor scRNA: both in rods and cones, prom1b 3-4x higher.

### Function
- [PMID:31362982 "The Prom1 orthologs in zebrafish include prom1a and prom1b, and our results showed that prom1b, rather than prom1a, plays an important role in zebrafish photoreceptors."]
- Full text (PMC6755801, read on the web; not in the publications cache, so not quoted here): TALEN alleles for both
  copies (prom1a c.138_141delTACT, p.Asp46Glufs*15); prom1a mutants had normal ONL and outer-segment thickness up
  to 11 months; no double mutant; prom1a mRNA not significantly changed in its mutant at 2 mpf.
- Corbeil, Fargeas & Jaszai letter (PMID:31704774; text not cached) questioned the conclusion, citing prom1a splice
  variants and prom1a expression in the retina; authors replied (PMID:31704775).

### Annotation decisions
- ER and ERGIC (IEA + ISS): MARK_AS_OVER_ANNOTATED (transit compartments).
- Plasma membrane, apical PM, microvillus, microvillus membrane, cilium, membrane: ACCEPT.
- Microvillus organization, prominosome (IBA): KEEP_AS_NON_CORE (no zebrafish data).
- Camera-type eye photoreceptor cell differentiation (IBA): MARK_AS_OVER_ANNOTATED with propagation review
  (the photoreceptor role went to prom1b).
