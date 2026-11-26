# nuoB (E. coli K-12, P0AFC7) notes

## 2026-10-23 review

Deep-research providers are unavailable in this environment (no API keys), so
the literature was reviewed manually from cached `publications/PMID_*.md` files
and the UniProt record. Most cited complex I papers are cached abstract-only
(checked `full_text_available`); PMID:18316732, PMID:9495756 and PMID:34308841
have full text.

- NuoB is the complex I 20 kDa (PSST/NDUFS7) family subunit
  [file:ECOLI/nuoB/nuoB-uniprot.txt "Belongs to the complex I 20 kDa subunit family."]
  and binds one [4Fe-4S] cluster [file:ECOLI/nuoB/nuoB-uniprot.txt "Binds 1 [4Fe-4S] cluster."].
- Cluster N2 is on NuoB: Cys mutants lose activity and the N2 EPR signal
  [PMID:12975362 "From this we conclude that the Fe/S cluster N2 is located on subunit NuoB."].
- N2 is the terminal centre of the chain and is reduced in ~90 us
  [PMID:18316732 "Center N2 is widely thought to donate electrons directly to ubiquinone."].
- Conserved acidic residues near N2 are catalytically essential and linked to
  redox-coupled protonation [PMID:16807239 "We discuss the possible participation of Glu(67) in a proton pathway coupled with the redox reaction of N2."].
- Q-site lies between NuoD and NuoB [PMID:34308841 "The Q-binding site in complex I is formed at the end of a crevice between NuoD and NuoB subunits"].
  Quinone binding kept as non-core for NuoB (head group mostly coordinated by NuoD).
- NDH-1 is electrogenic, distinct from NDH-2 [PMID:3122832 "an enzyme (NADH dh I) that reacts with deamino-NADH or NADH whose turnover leads to generation of a H+ electrochemical gradient"],
  so GO:0050136 (non-electrogenic) is REMOVEd.

## Decisions

- GO:0008137 rows accepted (complex-level activity; core function uses
  contributes_to). The IEA `enables` row is accepted on the term; a qualifier
  change is not expressible as a term replacement.
- Generic terms (GO:0003954, GO:0016020, GO:0030964, GO:0051536, GO:0005506)
  MODIFY to the specific terms already carried (GO:0008137, GO:0005886,
  GO:0045271, GO:0051539).
- NEW GO:0009055 electron transfer activity (IDA, PMID:18316732) as the
  subunit's own MF, matching the bacterial complex I module leaf function.
- Aerobic respiration kept as non-core (broad physiological context; E. coli
  NDH-1 also serves anaerobic chains).
