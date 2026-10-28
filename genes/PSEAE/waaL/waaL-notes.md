# waaL (PA4999, Q9HUG6) notes

No deep-research provider was available; literature research done manually (PubMed MCP + cached
publications).

## Identity

- UniProt Q9HUG6 (Swiss-Prot), 401 aa, *P. aeruginosa* PAO1, locus PA4999. O-antigen ligase,
  EC 2.4.99.26; CAZy GT121; Pfam PF04932 (Wzy_C); PANTHER PTHR37422 (TEICHURONIC ACID BIOSYNTHESIS
  PROTEIN TUAE), SF13. Polytopic inner-membrane protein, 12 TM helices in the PEG-maleimide
  topology (UniProt FT, PMID:30047569); essential periplasmic His303 (HX10G motif).

## Function

- Ligates completed undecaprenyl-PP-linked O antigen (both B-band OSA and A-band CPA) to lipid
  A-core at the periplasmic face [PMID:15838026 "The completed chains are covalently attached to
  lipid A core by the O-antigen ligase, WaaL"; "waaL is required for the attachment of O-antigen
  repeat units to the core"].
- In vitro ligation with purified WaaL [PMID:17697256 "the development of an in vitro O-antigen
  ligase assay"]. That paper proposed ATP-dependence, later refuted: ligation needs no ATP or
  Mg2+, and WaaL does not hydrolyse ATP; WaaL behaves like a metal-independent inverting
  glycosyltransferase [PMID:21983211 "E. coli and Pseudomonas aeruginosa WaaL proteins cannot
  catalyze ATP hydrolysis in vitro"; "share features of metal ion-independent inverting
  glycosyltransferases"]. PMID:30047569 confirmed this for P. aeruginosa WaaL per UniProt.
- GO:0008754 O-antigen ligase activity is defined by the transfer reaction and is_a
  glycosyltransferase activity; GO:0016874 ligase activity (EC 6) requires energy from NTP
  hydrolysis, which WaaL does not use, despite its name.
- Topology: GFP and PhoA-LacZ fusions [PMID:20824106 "Protein orientation in the inner membrane was
  confirmed via C-terminal fusion to green fluorescent protein"]; PEG-Mal labeling of intact
  protein [PMID:30047569 "both ligases share similar membrane topology"].

## Motility and pili

- PMID:15838026 reported the waaL mutation "drastically affected the swimming and twitching
  motilities". This is a pleiotropic consequence of O-antigen-less (rough) LPS / cell-envelope
  defects; WaaL acts in the periplasmic leaflet on LPS and has no known role in pilus or flagellum
  assembly. In PA14 and PAK, waaL deletion did not abolish swimming [PMID:29059582 "ΔwaaL mutation
  in P. aeruginosa did not abrogate swimming motility nor ability of the bacteria to form
  biofilms"]. Annotations to pilus assembly, flagellum assembly and the two motility processes are
  indirect phenotypes.

## Process granularity

- O antigen biosynthetic process (GO:0009243) is the formation of the O side chain; the chain is
  completed (Wzy polymerization) before WaaL acts, and WaaL forms the bond between O antigen and
  core. The step belongs to lipopolysaccharide biosynthesis (GO:0009103), which UniProt/UniPathway
  also use (UPA00030, not the O-antigen pathway UPA00281 used for e.g. WbpD). GO:0009103 is_a
  polysaccharide biosynthetic process (GO:0000271).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN008076295 | GO:0016757 glycosyltransferase activity | 3 (WaaL, P26471, P27243) | 64 (31 taxa) | GO:0016757 glycosyltransferase activity, IDA, PMID:17697256 (plus UniProt EXP O-antigen ligase rows) | SOUND | In vitro ligation assay with purified WaaL; O-antigen ligase activity is_a glycosyltransferase activity, and WaaL is an inverting GT (PMID:21983211). Broad GT term suits a Wzy_C/WaaL-like clade. |
| PTN008076295 | GO:0005886 plasma membrane | 2 (WaaL, P27243) | 64 (31 taxa) | GO:0005886 plasma membrane, IDA, PMID:17697256; GO:0098567 periplasmic side of plasma membrane, IDA, PMID:20824106 (plus UniProt EXP rows) | SOUND | Polytopic inner-membrane protein; topology mapped by reporter fusions and PEG-Mal labeling. |
| PTN008076295 | GO:0000271 polysaccharide biosynthetic process | 1 (sole seed) | 64 (31 taxa) | GO:0009243 O antigen biosynthetic process, IMP, PMID:15838026 | SOUND | The knockout lacks O antigen on LPS and is complemented; WaaL catalyses the step that attaches O antigen to core. The seed term is arguably lateral (ligation is LPS assembly rather than O-chain formation; GO:0009103 would be better), but the node term polysaccharide biosynthetic process holds either way and suits a clade that includes TuaE-like teichuronic acid proteins. Re-seeding with an LPS biosynthetic process row or the EXP ligase evidence would be cleaner. |
