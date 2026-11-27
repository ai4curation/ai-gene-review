# Vcp (rat) review notes

## Session 1 - initial review

- `just fetch-gene rat Vcp` resolved P46462 (TERA_RAT); 230 GOA rows (93 ISO, 74 IEA,
  24 ISS, 10 IPI, 9 IDA, 9 IBA, 7 IMP, 3 EXP, 1 NAS).
- No deep-research provider available; literature synthesis written by hand in
  `Vcp-deep-research-manual.md` from cached publications.
- Rat-specific experimental evidence is strong for: hexameric ATPase activity and
  nucleotide binding [PMID:7806566; PMID:18332143 "We sought to explore nucleotide
  binding to recombinant rat p97 by studying the D1 and D2 domains separately."], the
  p97-p47 and p97-Ufd1-Npl4 complexes [PMID:10811609 "Cytosolic p97 therefore comprises
  at least two alternative complexes: p97/p47 and p97/Ufd1/Npl4."], p97/p47-driven Golgi
  reassembly [PMID:10811609 "Only a combination of p97 and p47 could promote
  reassembly."], and ERAD of IP3 receptors in rat cells [PMID:16103111].
- Most other process terms are ISO/IEA from human/mouse VCP. Accepted where VCP does
  the work (ubiquitin-dependent extraction: autophagosome maturation, chromatin
  extraction, SG disassembly); downgraded where the source shows only a downstream
  phenotype (mitochondrial uncoupling -> NAD/FAD/ATP metabolism, oxidative
  phosphorylation, membrane potential; viral replication; responses to heat/arsenite).
- Regulation-of-catabolism terms (GO:2000060, GO:0032436, GO:0045732) were MODIFIED to
  the direct-participation terms: VCP performs a step of ERAD/proteasomal degradation,
  so "positive regulation of" misdescribes its role.
- Bare protein binding (GO:0005515, IPI with Nsfl1c/p47) removed per policy; the
  interaction is captured by GO:1990730 VCP-NSFL1C complex.
- NEW: GO:0090168 Golgi reassembly (IDA, PMID:10811609). Participation test: p97 is the
  ATPase that drives the p47-dependent cisternal regrowth. Comparator check: VCIP135
  (Vcpip1, rat) carries GO:0090168 by IDA (PMID:15037600); p47 (Nsfl1c, rat) carries
  Golgi organization and membrane fusion by IDA (PMID:12146947) but not GO:0090168.
  No rat/mouse/human VCP carries Golgi reassembly. Flagged for expert check.
- GO:0005515-like identical protein binding kept non-core (homohexamer).
- Organelle policy: ER (GO:0005783) ISS/ISO/IEA rows kept - the protein was purified
  from rat liver transitional ER [PMID:7806566] and is recruited to the cytosolic face of
  the ER membrane; ER membrane rows already exist, so no NEW sub-compartment row.
