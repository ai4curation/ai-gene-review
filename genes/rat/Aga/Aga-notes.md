# Aga (rat, P30919) notes

## Re-review 2026-10-04

**GOA changes (refresh in commit a3cf70b6d):**
- New ISO rows (donor splits of already-reviewed terms): GO:0003948 N4-(beta-N-acetylglucosaminyl)-L-asparaginase activity from pig AGA (RGD:13972209; RGD REST API reports speciesTypeKey 9 = pig) and from human AGA (UniProtKB:P20933); GO:0005764 lysosome from human AGA.
- Retired: GO:0006517 protein deglycosylation (ISO). Human AGA still carries IDA/IMP protein deglycosylation (QuickGO: PMID:1281977, PMID:1904874), so core_functions keeps GO:0006517 as the process.

**Actions:**
- PENDING resolved: both GO:0003948 ISO donor splits -> ACCEPT (rat enzyme has direct activity data [PMID:2775174 "The purified enzyme had a specific activity of 3.8 mumol of N-acetylglucosamine/min per mg with N4-(beta-N-acetylglucosaminyl)-L-asparagine as substrate."]); lysosome ISO (human donor) -> KEEP_AS_NON_CORE, consistent with the IBA/IEA/MGI-ISO lysosome rows.
- GO:0042802 identical protein binding (IDA, PMID:2775174): action unchanged (MARK_AS_OVER_ANNOTATED) but the rationale was corrected. The earlier reason claimed an alpha2beta2 homotetramer, but the rat abstract says the native enzyme is a heterodimer [PMID:2775174 "The native enzyme had a molecular mass of 49 kDa and was composed of two non-identical subunits joined by strong non-covalent forces"; PMID:1554372 "The native enzyme appeared as a heterodimer among the mammals"]. The alpha and beta chains both come from the P30919 precursor, which probably explains the curator's choice. Full text not cached.
- GO:0008150 biological_process (ND): REMOVE kept; replaced the boilerplate reason with a specific one (the rat enzyme has direct biochemical data, so "no data" is outdated).
- EXP GO:0003948 (PMID:1554372) and IDA GO:0003948 (PMID:2775174): added activity-bearing quotes; actions unchanged (ACCEPT).
- All other rows re-audited; no change. IBA cytoplasm stays KEEP_AS_NON_CORE (lysosome is part_of cytoplasm).

**Open questions:**
- Does the full text of PMID:2775174 show self-association of whole alpha/beta units in rat (which would support GO:0042802 as stated), or does the annotation just record alpha-beta chain association?
- Why did the rat ISO protein deglycosylation row get withdrawn while the human IDA remains? Possibly an RGD pipeline change. Aga acts on free glycoasparagines (it needs a free alpha-amino and alpha-carboxyl on the Asn), so GO:0006516 glycoprotein catabolic process may fit better than protein deglycosylation.
