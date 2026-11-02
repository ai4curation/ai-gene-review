# SLN (sarcolipin) review notes

## 2026-10-08 — MICROPROTEINS Tier 4 (regulin comparator)

**Product.** UniProt O00631, 31 aa, PE1, single-pass type II membrane peptide (cytoplasmic 1-7,
TM 8-26, lumenal 27-31). Canonical protein-coding gene on 11q22-q23; not an alt-ORF, so no
alternative-ORF naming issue. Lumenal RSYQY tail is conserved (human vs rabbit P42532 vs mouse
Q9CQD6) [PMID:9367679 "The cytoplasmic and transmembrane sequences are not well conserved among
the three species, but the lumenal sequence is highly conserved"].

**Core activity: SERCA inhibition.**
- Human and rabbit SLN co-expressed with SERCA1 in HEK-293 lower the apparent Ca2+ affinity but
  raise Vmax [PMID:9575189 "Coexpression of native rabbit SLN or NF-SLN with SERCA1 decreased the
  apparent affinity of SERCA1 for Ca2+ but stimulated maximal Ca2+ uptake rates (Vmax)"]; the
  C-terminal tail is essential [PMID:9575189 "Mutations in the C-terminal domain showed that this
  sequence is critical for SLN function"].
- SLN also inhibits SERCA2a and acts synergistically with PLN; it binds PLN and reduces PLN
  pentamers [PMID:12032137 "NF-SLN binds directly to PLN and that NF-SLN inhibits the formation of
  PLN pentamers"]. Rabbit NF-SLN, HEK-293 microsomes (abstract only cached).
- Crystal structure of rabbit SERCA1a-SLN complex [PMID:23455424] shows SLN in the PLN/regulin
  groove trapping an E1 state.
- Human SLN binds human SERCA2 (ATP2A2) and VMP1 competes it away [PMID:28890335 "VMP1 interacts
  with SERCA and prevents formation of the SERCA/PLN/SLN inhibitory complex"].
- Regulins homo- and hetero-oligomerise (FRET); only monomers bind SERCA [PMID:36523160,
  PMID:31449798].
- Human physiology: SLN protein falls in human atrial fibrillation while SR Ca uptake rises
  [PMID:21640081] (correlative, consistent with inhibitory role).
- Mouse: Sln-/- mice cannot defend core temperature in cold; SLN uncouples SERCA ATP hydrolysis
  from transport (thermogenesis) [PMID:22961106 "sarcolipin (Sln), a newly identified regulator of
  the sarco/endoplasmic reticulum Ca(2+)-ATPase (Serca) pump, is necessary for muscle-based
  thermogenesis"]. No equivalent human data.

**MF term choice.** GO:0042030 ATPase inhibitor activity ("Binds to and stops, prevents or reduces
an ATP hydrolysis activity") vs GO:0141110 transporter inhibitor activity. QuickGO is_a ancestry:
GO:0042030 -> GO:0140678 molecular function inhibitor activity (NOT under GO:0004857 enzyme
inhibitor activity, and not under GO:0030234 enzyme regulator activity); GO:0141110 ->
GO:0141108 transporter regulator activity -> GO:0140678. SERCA is both; SLN's distinctive
uncoupling effect (inhibits Ca transport more than ATP hydrolysis) arguably makes
transporter inhibitor activity the more exact fit, but GO:0042030 is what PLN carries by IDA+IBA
and what the MRLN/ERLN reviews used. Chose GO:0042030 for consistency; question raised.

Regulin comparison (from GOA tsvs and completed reviews, not edited):
- PLN GOA: GO:0042030 (IDA, IBA, IEA, ISS), GO:0141110 (IDA), GO:0004857 (ISS). PLN review is
  still a stub.
- MRLN review core MF: GO:0042030 (GOA had GO:0004857, MODIFY'd).
- ERLN review core MF: GO:0042030 (NEW; GOA had no MF).
- STRIT1 (DWORF) review core MF: GO:0141109 transporter activator activity (activator branch).
- SLN GOA: GO:0004857 (ISS), GO:0030234 (IEA InterPro), GO:0051117 (ISS); no GO:0042030 and no IBA.

**Interaction rows.** HuRI Y2H partners (SYNE4, KASH5, TMEM79) are all membrane proteins; a
hydrophobic 31-aa TM peptide is a classic sticky Y2H prey/bait. Removed as uninformative.
ATP2A2 IPI -> ATPase binding. VMP1 IPI -> removed (no informative MF).

**Literature limits.** Most mechanistic papers use rabbit or mouse SLN; several key ones are
abstract-only in cache (9575189, 12032137, 11781085, 28890335, 23455424).
