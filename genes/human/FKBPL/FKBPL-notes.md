# FKBPL (WISp39) research notes

UniProt: Q9UIM3. FK506-binding protein-like. Contains TPR repeats (TPR-like helical domain)
but NO canonical FKBP-type PPIase catalytic domain -> not a bona fide rotamase (no PPIase activity).

## Core biology
- Hsp90-binding TPR co-chaperone that regulates p21(WAF1/CIP1)/CDKN1A protein stability by
  binding both Hsp90 and p21 [uniprot "Regulates p21 protein stability by binding to Hsp90 and
  p21"; PMID:15664193 "Regulation of p21(WAF1/CIP1) stability by WISp39, a Hsp90 binding TPR
  protein"]. Forms ternary complex with CDKN1A/p21 and HSP90AB1 [uniprot "Forms a ternary complex
  with CDKN1A/p21 and HSP90AB1/Hsp90"]. K287A/R291A mutations abolish HSP90AB1 binding.
- Stress/radiation response: novel stress-response gene with potential role in induced radioresistance
  [PMID:10521921 "A novel human stress response-related gene with a potential role in induced
  radioresistance"]; response to radiation (NAS).
- Secreted/extracellular anti-angiogenic factor (extracellular region IDA PMID:25767277); FKBPL
  and its peptide derivatives (e.g. ALM201) have anti-angiogenic activity. Extracellular detection.
- Interactors: HSP90AB1 (P08238, via TPR), CDKN1A/p21, ANKRD49 (Q8WVL7), CALCOCO2/NDP52 (Q13137).

## GOA IPI partners (bare protein binding)
25036637(Q8WVL7 ANKRD49), 25416956(Q13137 CALCOCO2), 28514442(Q8WVL7), 32296183(Q8WVL7),
33961781(Q8WVL7), 40205054(Q8WVL7). Note: HSP90 not directly in these IPI WITH fields; the HSP90
binding is in UniProt FUNCTION/SUBUNIT, not the GOA protein-binding rows.

## Action plan
- protein binding IPI block: KEEP_AS_NON_CORE (ANKRD49, CALCOCO2 are recurrent partners but bare
  protein binding; not the characterized core function). MARK_AS_OVER_ANNOTATED the broad screens.
- extracellular region IDA GO:0005576: KEEP_AS_NON_CORE (secreted anti-angiogenic pool, real but
  context-specific; primary characterized function is intracellular Hsp90/p21).
- cytosol TAS GO:0005829: ACCEPT (site of Hsp90/p21 co-chaperone action).
- response to radiation NAS GO:0009314: KEEP_AS_NON_CORE (stress-response role; NAS).
- Core MF to capture: Hsp90 protein binding (GO:0051879) / heat shock protein binding (TPR co-chaperone
  for p21 stability). Propose this as core (no direct GOA term, but well supported by UniProt).
