# SYNE2 (nesprin-2) review notes

## Session 2026-09-27 (claude-code)

Sources: UniProt Q8WXH0, cached GOA publications, PMID:19874786, PMID:32619477,
PMID:39115447 (newly cached; PubMed-verified via eutils), SYNE2-deep-research-falcon.md.

Key biology:
- Giant isoform: CH-domain actin binding [PMID:12118075 "Domain analysis shows that the actin-binding domain binds to Factin in vitro"].
- KASH binds SUN1/SUN2 promiscuously [PMID:18396275 "the KASH domains of Nesprins 1, 2 and 3 interact promiscuously with luminal domains of Sun1 and Sun2."].
- TAN lines with SUN2 couple nucleus to retrograde actin flow [PMID:20724637].
- Motor coupling for neuronal nuclear migration: BICD2-dynein [PMID:32619477]; 2024 work
  [PMID:39115447 "Nesprin-2 recruits dynein-dynactin-BicD2 independently of the nearby kinesin-binding LEWD motif."]
  and "Both motor binding sites are required to rescue nuclear migration defects caused by the loss of function of Nesprin-2."

Decisions of note:
- Meiotic LINC complex (GO:0034993) rows MODIFIED to non-meiotic parent GO:0106094.
- Protein binding: LMNA row MODIFIED to lamin binding; the rest REMOVED (SUN binding is captured
  by GO:0140444 and LINC complex membership).
- NEW GO:0021817 nucleokinesis (ISS from rat/mouse data, PMID:32619477, PMID:19874786, PMID:39115447).
- HPA intermediate filament cytoskeleton row UNDECIDED (image not evaluable; no mechanism).

Points for the nucleokinesis module:
- Module says BICD2 binds the nesprin-2 LEWD motif. PMID:32619477 interpreted the LEWD (LEAA)
  mutation as mainly affecting dynein recruitment, but PMID:39115447 shows LEWD is the
  kinesin-1 (KLC) site and dynein-dynactin-BicD2 binds independently via Spindly/CC1-like motifs.
- Module says kinesin-1 restrains nuclear movement (inhibition accelerates migration; cortex,
  PMID:32619477). In cerebellar granule neurons PMID:39115447 finds both motor-binding sites are
  required and kinesin contributes productively; the relationship appears cell-type dependent.

## 2026-11-03 ORGANELLES batch 4 (mitochondrion rows)

- Rows: GO:0005739 IDA (PMID:15671068) and IEA (GO_REF:0000044, SL-0173), located_in. Both stay KEEP_AS_NON_CORE; reasons extended.
- PMID:15671068 is abstract-only in the cache and Europe PMC has no full text. Immunogold EM with three epitope antibodies [PMID:15671068 "detected nesprin-2 isoforms at multiple locations including intranuclear foci, both membranes of the NE, mitochondria, sarcomeric structures and plasma membrane foci"]. The curator's organelle call is deferred to (rule 2).
- UniProt lists "Mitochondrion." without an evidence tag, beside locations tagged with PMID:15671068; the SL-0173 mapping is sound.
- Outcome: root only. The KASH tail anchor is placed by UniProt in the outer nuclear and SR membranes, not mitochondria; nothing resolves a mitochondrial sub-compartment or the isoform involved.
