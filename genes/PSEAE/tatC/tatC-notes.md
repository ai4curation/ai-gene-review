# tatC (PA5070, Q9HUB3) review notes

No deep-research provider was available. Sources: UniProt record (Q9HUB3, HAMAP
MF_00902), cached PMID:16621825 (abstract only; PMC full text body not returned by
the PubMed MCP).

## Function

- Core subunit of the Tat translocon; TatBC receptor recognises twin-arginine
  signal peptides [file:PSEAE/tatC/tatC-uniprot.txt "Part of the twin-arginine
  translocation (Tat) system that transports large folded proteins containing a
  characteristic twin-arginine motif in their signal peptide across membranes.
  Together with TatB, TatC is part of a receptor directly interacting with Tat
  signal peptides"].
- Tat pathway required for PvdN export and pyoverdine [PMID:16621825 "export is Tat
  dependent"; "no Pvd was produced"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000769484 | GO:0033281 TAT protein transport complex | 3 | 129 (76 taxa) | GO:0033281 TAT protein transport complex, IMP, PMID:16621825 (PseudoCAP) | SOUND | PMID:16621825 is a tat-pathway phenotype paper (PvdN export, pyoverdine), so the IMP evidence for complex membership is indirect; but TatC is unambiguously the core subunit of the Tat complex by family assignment (HAMAP MF_00902, NCBIfam tatC, PROSITE TATC), so the membership claim is correct. The node term fits the TatC clade. | E. coli TatC P69423 (canonical, strong experimental grounding), Arabidopsis AT2G01110 | Yes; E. coli TatC anchors the node. No GO_CENTRAL defect. |

The same node correctly carries GO:0009977 (PMF-dependent protein transmembrane
transporter activity), GO:0043953 (protein transport by the Tat complex) and
GO:0065002 (intracellular protein transmembrane transport), all seeded by E. coli
TatC; these were accepted on this gene.

PseudoCAP defects from this gene: none. The seed's evidence is phenotypic rather
than a direct complex assay, but the claim is correct and the IBD is anchored by
E. coli TatC, so no defect is raised (verdict SOUND).
