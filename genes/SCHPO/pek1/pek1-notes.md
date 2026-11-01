# pek1 (Q9Y884, SPBC543.07; synonyms skh1, mkk1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of
NEUCR/mek-1 (Q7RYZ6). No ProtNLM2 output was consulted.

### Deep research
- `just deep-research-falcon SCHPO pek1 --fallback perplexity-lite` failed: Edison API
  "Failed to authenticate" (403), and the perplexity-lite fallback also failed. No
  deep-research file exists; review is based on cached publications.

### Evolutionary placement
- PANTHER: UniProt places Pek1 in PTHR47448:SF5 (with fungal Mkk1/Mkk2 orthologs incl.
  Aspergillus, Pyricularia, Verticillium; `interpro/panther/PTHR47448/PTHR47448-entries.csv`);
  the PAINT family is PTHR48013 (MAPKK family).
- PAINT `interpro/panther/PTHR48013/PTHR48013-paint.tsv`:
  - PTN000684494 (taxon:2759): GO:0004708 MAPKK activity and GO:0000165 MAPK cascade,
    Pek1 (PomBase:SPBC543.07) among donors.
  - PTN001220604 (taxon:451864, Dikarya): GO:0000196 cell integrity MAPK cascade
    (donors Pek1, SGD Mkk1 S000005757, Mkk2 S000006061) and GO:0060237 regulation of
    fungal-type cell wall organization (donors CGD:CAL0000192384 + Mkk1/Mkk2; Pek1 not a donor).
- GO-CAM 671ae02600003478 (`gocams/index.tsv`): Pek1 MAPKK activity, part of cell
  integrity MAPK cascade, occurs in cytosol.

### Experimental evidence in S. pombe
- Identified as MAPKK for Pmk1; unphosphorylated Pek1 inhibits, Mkh1-phosphorylated
  Pek1 activates [PMID:10365961 "Mkh1, an upstream MAPKK kinase (MAPKKK), converts Pek1 from being an inhibitor to an activator."]
- Skh1 = Pek1; two-hybrid ternary complex Mkh1-Skh1-Spm1; identical deletion phenotypes;
  Skh1-DD drives Spm1 Tyr phosphorylation [PMID:10591634 "We also show that HA-Spm1 is hyper-phosphorylated on tyrosine residues in cells co-expressing the activated HA-Skh1(DD) protein."]
- Stress-induced Pmk1 activation fully Pek1-dependent; Pek1 cytoplasmic + septum
  [PMID:16291757 "Mkh1 and Pek1 were also found at the septum"]
- In vitro: purified Pek1-DD stimulates GST-Pmk1 [PMID:17881729 "The results clearly showed that the addition of purified Pek1 DD markedly stimulated the kinase activity of GST-Pmk1"]
- Calcineurin/Ca2+ effects are Pmk1-dependent outputs [PMID:16928959 "Knockout of the pmk1 + gene also abolished the effect of Pek1 DD overexpression"]
- TEY sites T186/Y188 of Pmk1 [PMID:35049972 review].

### Established in S. pombe vs inferred
- Experimental: MAPKK activity toward Pmk1 (in vivo and in vitro), cell integrity MAPK
  cascade, cytoplasm/septum localization, Pmk1 binding (Y2H), phosphorylation-dependent
  inhibitory/activating switch, downstream cell wall/Ca2+ outputs.
- Inferred only: ATP binding (sequence), cytosol/nucleus (HDA), activation-loop
  phosphosites S234/T238 (UniProt by similarity), GO:0060237 (IBA; supported indirectly
  by beta-glucanase sensitivity data).

### Decisions
- Serine kinase (Rhea) marked over-annotated: substrate sites are Thr/Tyr.
- Protein binding: Mkh1 row REMOVE; Pmk1 row MODIFY to GO:0051019 MAPK binding.
- Generic MAPK cascade / protein kinase activity MODIFY to the specific terms.
