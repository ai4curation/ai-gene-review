# Spot review of annotation-gain candidates

Manual QA of 6 candidate new annotations from `ANNOTATION_GAIN.md` (one per family, including the
broad `relatedMatch` ones), checked against the UniProt record (protein name / EC number / existing
GO) and GO subsumption (OAK). Goal: confirm correct gains and surface false positives.

| # | UniProt | ARO (gene) | candidate GO | verdict |
|---|---------|-----------|--------------|---------|
| 1 | A0A0R6L508 MCR-1 | ARO:3003689 MCR-1.1 | GO:0043838 PE:Kdo2-lipidA pEtN transferase | ✅ **correct, high value** |
| 2 | A0A0M5JP06 RmtE | ARO:3004679 rmtE2 | GO:0070043 rRNA guanine-N7-MTase | ✅ **correct refinement** |
| 3 | A0A0K2B0L6 srm1 | ARO:3004605 ermZ | GO:0052910 23S rRNA A-N6-diMTase | ✅ **correct, more precise** |
| 4 | A0A076UB44 AAC(6')-Ib8 | ARO:3002579 | GO:0034069 aminoglycoside N-acetyltransferase | ⚠️ **redundant (over-general)** |
| 5 | A0A062U9V1 | ARO:3008508 OXA-1090 | GO:0008800 beta-lactamase | ❓ **questionable (PBP vs OXA)** |
| 6 | A0A024FRF7 FosK | ARO:3003207 | GO:0004364 glutathione transferase | ⚠️ **mapping over-generalizes** |

## Details

**1. MCR-1 → GO:0043838 — correct, high value.** UniProt names it "Phosphatidylethanolamine
transferase Mcr-1 (**EC 2.7.8.43**)"; EC 2.7.8.43 *is* GO:0043838. Existing GO has only the broad
`GO:0016776` (phosphotransferase, phosphate acceptor), which is **not** an ancestor of GO:0043838 —
so the specific MF is genuinely missing. Representative of all 79 colistin/MCR gains.

**2. RmtE → GO:0070043 — correct refinement.** UniProt: "16S rRNA (guanine(1405)-N(7))-
methyltransferase (**EC 2.1.1.179**)". Entry currently has `GO:0008649` (general rRNA
methyltransferase); candidate GO:0070043 is a *descendant* of it → a valid, more-specific term. (The
ideal m7G1405 term is the recorded GO gap.)

**3. ermZ/srm1 → GO:0052910 — correct, more precise.** *Streptomyces ambofaciens* spiramycin-
producer resistance methylase. Existing `GO:0000179` is the generic N6,N6-dimethyltransferase (covers
KsgA too); candidate GO:0052910 is the Erm 23S-A2058-specific term and is **not** subsumed by
GO:0000179 → a genuine precision gain.

**4. AAC(6')-Ib8 → GO:0034069 — redundant.** UniProt: "Aminoglycoside N(6')-acetyltransferase
(**EC 2.3.1.82**)". Entry already has `GO:0047663` "aminoglycoside 6'-N-acetyltransferase activity",
which **is a child of** the candidate GO:0034069. So the candidate is *true but over-general* — the
entry already carries a more specific term. **Quantified across the snapshot, this affects the
aminoglycoside families specifically:**

| candidate GO | candidates | already have a more-specific child (redundant) |
|---|---:|---:|
| GO:0034069 aminoglycoside N-acetyltransferase (AAC) | 76 | **51** |
| GO:0034068 aminoglycoside nucleotidyltransferase (ANT) | 35 | **22** |
| GO:0034071 aminoglycoside phosphotransferase (APH) | 31 | **19** |
| GO:0008800 beta-lactamase | 448 | 0 |
| GO:0043838 colistin/MCR pEtN transferase | 79 | 0 |
| GO:0052910 Erm 23S diMTase | 29 | 0 |

≈**92 of 746** candidates are subsumption-redundant — all in the aminoglycoside families (GO has a
well-developed sub-hierarchy there). The β-lactamase/MCR/Erm/FosA/16S gains have **no** such child
term, so the family-level MF is a genuine addition. **Action: the gain filter should suppress a
candidate when the entry already has a more specific (is_a descendant) GO term.**

**5. OXA-1090 → GO:0008800 — questionable.** UniProt names A0A062U9V1 generically as "Penicillin-
binding protein transpeptidase domain-containing protein" in an environmental alphaproteobacterium
(*Hyphomonas beringensis*), with only `GO:0008658` (penicillin binding). Class D (OXA) β-lactamases
and PBPs share the serine-transpeptidase fold; CARD's protein-homolog model can match a genuine **PBP**
that is **not** a β-lactamase. GO:0008800 should not be asserted here without review — illustrates that
the 5,317-descendant β-lactamase family node can over-reach to distant homologs.

**6. FosK → GO:0004364 — mapping over-generalizes.** UniProt: "Integron-mediated fosfomycin-modifying
enzyme (FosK)", *Acinetobacter* (Gram-negative → likely FosA-type/glutathione, so plausibly fine
*here*). But the mapped node `ARO:3000133` "fosfomycin **thiol** transferase" also covers **FosB**,
which uses **bacillithiol/L-cysteine, not glutathione** — so propagating GO:0004364 (glutathione
transferase) family-wide would mis-annotate FosB members. (Existing `GO:0004462` lactoylglutathione
lyase on this entry is itself a VOC/glyoxalase-superfamily over-annotation.) **Action: restrict the
fosfomycin mapping to a FosA-specific ARO node, or keep `relatedMatch` with an explicit FosA-only
caveat.**

## Takeaways / actions

1. **Add a subsumption-aware filter to the gain report**: drop a candidate GO term when the entry
   already has a more specific descendant of it (fixes #4; would cut ~92 redundant rows, 746 → ~654).
2. **Tighten the fosfomycin mapping** (#6): map FosA, not the FosA+FosB "thiol transferase" parent.
   *(DONE — re-anchored ARO:3000133 → glutathione-specific FosA/FosA2/FosA3/fosA5, excluding FosB/FosX.
   Also from PR review: Erm now maps to the family-safe `GO:0008988` (not the di-methyltransferase
   `GO:0052910`) so mono-methylating variants are not over-annotated; AAC(6')-Ib review gained primary
   references PMID:18710261 and PMID:16369542 plus a cytoplasm location.)*
3. **Flag homology over-reach** (#5): family-node candidates for distant/environmental homologs (e.g.
   proteins UniProt names as generic PBP/transpeptidase) warrant curator review before assertion.
4. Net: 2/6 high-confidence correct, 2/6 correct precision gains, 1/6 redundant, 1/6 questionable —
   consistent with treating these as **curator leads, not automatic assertions**.
