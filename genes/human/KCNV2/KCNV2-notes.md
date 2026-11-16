# KCNV2 (Q8TDN2) review notes

Session 2026-11-16, vision-disorder alignment campaign (dismech: KCNV2_Related_Retinopathy, CDSRR).

## Synthesis

- Kv8.2 is an "electrically silent" Kv alpha subunit (KvS group, subfamily V). Alone it gives no
  current and stays in the ER; with Kv2.1 (KCNB1) it reaches the plasma membrane and forms
  heteromeric channels with altered currents (human subunits in mammalian cells; named Kv11.1
  there) [PMID:12060745 "Co-expression of each of the previously uncharacterized subunits with Kv2.1 resulted in plasma membrane localization with currents that differed from typical Kv2.1 currents."].
- In Xenopus oocytes Kv8.2 shifts Kv2.1 activation negative, creating a -40 to -10 mV window
  current resembling rod IKx; mouse retina photoreceptor layer expresses it [PMID:17652418].
- Pore mutations W467G and G478R give nonconducting heteromers, while T1-domain mutations prevent
  heteromer formation [PMID:23115240]: the Kv8.2 pore region is part of the heteromer pore, so the
  channel activity belongs to the heteromer and Kv8.2 contributes to it (contributes_to).
- Mouse Kv8.2 knockout: Kv2.1/Kv8.2 is in the photoreceptor inner segment and carries IKx, which
  sets the resting membrane potential; KO alters rod and cone ERG signaling [PMID:34652420].
- Human CDSRR family variants fail to express or to interact with Kv2.1 (HEK co-IP) [PMID:34535971].
- Corrections: protein homooligomerization (IEA from T1 domain) contradicts "does not form
  homomultimers"; action potential (IBA) not shown and photoreceptors use graded potentials.
- Enables-qualified voltage-gated K channel activity (InterPro2GO) should be contributes_to.
