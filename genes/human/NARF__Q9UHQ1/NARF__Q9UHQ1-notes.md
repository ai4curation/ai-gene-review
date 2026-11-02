# NARF (Q9UHQ1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Folder created for the canonical NARF product Q9UHQ1, because `genes/human/NARF` is keyed to the
truncated alternative gene model J3KS48. No ProtNLM2 output or prediction-evidence file was opened
or used.

Deep research: `just deep-research-falcon human NARF__Q9UHQ1 --fallback perplexity-lite` failed
(Edison API login returned 403 Forbidden; the perplexity-lite fallback also failed). No
deep-research file was written for this folder. The review rests on the cached primary papers.

Evidence used:
- Founding paper [PMID:10514485 "Using the yeast two-hybrid assay, we isolated a novel human protein, Narf, that binds the carboxyl-terminal tail of prelamin A."]
  Binding is farnesylation-dependent [PMID:10514485 "The farnesylation status of prelamin A determines its ability to bind to Narf."]
  Nuclear, partly at the lamina [PMID:10514485 "it is exclusively nuclear and partially co-localizes with the nuclear lamina."]
- Paralog boundary [PMID:18270200 "Knockdown of IOP2, in contrast, had no effect on either."] (aconitase activities), so the NARFL/IOP1 CIA role is not transferred.
- Coactivator function [PMID:36490339 "NARF functions as an essential coactivator by recruiting the histone demethylase KDM6A to OCT4 bound to genes encoding the pluripotency factors NANOG, KLF4, and SOX2"]. ChIP (OCT4-dependent NARF recruitment), co-IP (NARF-OCT4, NARF-KDM6A; OCT4-KDM6A interaction NARF-dependent) and knockdown. Proposed as NEW GO:0003713 (IMP). Breast cancer stem cell and metastasis phenotypes are downstream and not annotated.

Evolutionary grounding: Q9UHQ1 is in PANTHER PTHR11615:SF124 (NUCLEAR PRELAMIN A RECOGNITION FACTOR).
A QuickGO query on withFrom=PTN002614243 (2026-10-21) returned 42 IBA rows on vertebrate NARF
orthologs (fish, Xenopus, chicken, mammals), all for lamin binding and lamin filament, with Q9UHQ1
the only donor. No Fe-S, hydrogenase or CIA term is propagated at this node; consistent with no
evidence for catalytic activity.

Decisions: lamin binding (IBA, IPI) ACCEPT; nuclear lamina TAS ACCEPT; nucleoplasm IDA (HPA) ACCEPT;
lamin filament (IBA, IDA) KEEP_AS_NON_CORE (peripheral, salt-extractable lamina association, not
shown inside filaments); nucleolus IDA (HPA) KEEP_AS_NON_CORE; nucleus IEA and nuclear lumen IDA
MODIFY to nucleoplasm (+ nuclear lamina for nucleus).

Transfer guidance: experimentally established in human = prelamin A (farnesylated tail) binding,
nuclear/lamina localization, coactivator activity (cancer cell lines, one lab). Inferred only =
any Fe-S binding or hydrogenase-like chemistry (not shown; do not assign).
