# Pea15 (mouse, Q62048) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Pea15 is the experimental donor (MGI:104799) at PAINT node PTN008298780 for the
human PEA15 IBA, and shares PANTHER subfamily PTHR48169:SF1 (ASTROCYTIC PHOSPHOPROTEIN PEA-15)
with human PEA15 (Q15121). No ProtNLM2 files or prediction-evidence folders were opened.

### Deep research
`just deep-research-falcon mouse Pea15 --fallback perplexity-lite` failed: falcon returned
"Edison API request failed: Failed to authenticate" and the perplexity-lite fallback also failed
(timeout/exit 1). No deep-research file exists; the review was built from literature cached via
`just fetch-pmid` after a PubMed search for mouse PEA-15 papers.

### Evolutionary grounding
- PANTHER PTHR48169 (DED domain-containing protein) is heterogeneous: SF1 = PEA15, SF3 = CFLAR,
  SF7 = caspase-8/10 and viral DED proteins. Only SF1-specific functions are considered for PEA15.
- Mouse and human PEA-15 are 96% identical [PMID:8662970 "PEA-15-deduced protein sequence (130 amino acids) shared no similarity with known proteins but is 96% identical to its human counterpart"].
- IBA GO:1902042 at PTN008298780 has mouse Pea15 itself as an experimental donor.

### Mouse-specific experimental evidence (what is established in this species)
- Cytosolic localization [PMID:7861130 "PEA-15 was found mainly in the cytosol"].
- Phosphosites Ser104 (PKC) and Ser116 (CaMKII) in astrocytes [PMID:9721757].
- Fas inhibition (overexpression, phosphosite mutants) [PMID:10588860 "the differential effect is evident at the level of caspase-8 activity which is inhibited via Fas activation"]; the same paper reports increased TNFR1 apoptosis, contradicted by knockout data.
- Pea15-null astrocytes are sensitised to TNF; re-expression rescues [PMID:10493725 "our results demonstrate that PEA-15 expression increases astrocyte survival after exposure to TNF"]. In vitro GST pull-down with FADD and caspase-8.
- ERK cytoplasmic sequestration: genetic deletion increases ERK nuclear localization [PMID:11702783 "Genetic deletion of PEA-15 results in increased ERK nuclear localization"]; T cells [PMID:20354143]; testis [PMID:17504918]; endogenous co-IP in SCN, light-induced dissociation [PMID:29383758].
- ERK-to-RSK2 scaffolding; PEA-15-null lymphocytes show impaired RSK2 activation [PMID:18077417].
- Organismal phenotypes (not annotated as process participation): spatial learning [PMID:19917132], T-cell cytokine phenotypes (conflicting directions: PMID:20354143 vs PMID:26317969), spermatocyte apoptosis [PMID:17504918], adipose expansion/insulin sensitivity [PMID:33772049].

### Inferred, not tested in mouse
- Glucose import regulation (human overexpression, PMID:9670003) — kept non-core.
- ERK2 docking structure (PMID:23575685) — ortholog/structural context only.
- Ras/integrin activation (PMID:9852038, PMID:10982386) — species of construct not established from the abstract; not used.

### Decisions
- MAPK cascade, intracellular signal transduction -> MODIFY to GO:0070372.
- cytoplasm -> MODIFY to cytosol; cytosol ACCEPT.
- protein kinase C binding, microtubule associated complex -> MARK_AS_OVER_ANNOTATED (substrate / co-fractionation only).
- apoptotic process, regulation of apoptotic process -> MODIFY to GO:1902042; GO:1902042 rows ACCEPT.
- GO:1902043 (positive, TNFR1) IDA -> KEEP_AS_NON_CORE (context-specific, conflicts with KO).
- NEW: GO:0042308 negative regulation of protein import into nucleus (IMP) and GO:0140311 protein sequestering activity (IMP), PEA-15 itself performs the anchoring.
