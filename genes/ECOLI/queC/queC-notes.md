# queC (P77756) review notes

E. coli K-12 QueC, 7-cyano-7-deazaguanine (preQ0) synthase, EC 6.3.4.20. 231 aa,
QueC family (HAMAP MF_01633, NCBIfam TIGR00364), PP-loop ATPase-like fold with a zinc site.

## Literature search (2026-11-24)

No deep-research file was available; the search was done directly in PubMed.

- PubMed `QueC 7-cyano-7-deazaguanine synthase` -> 2 hits: PMID:26391327 (Geobacillus
  QueC biochemistry, relevant), PMID:22032275 (crenarchaeal GAT-QueC, archaeosine; not E. coli
  QueC, not used).
- PubMed `queC preQ0 biosynthesis` -> 7 hits: PMID:19354300 (B. subtilis QueC in vitro, key),
  PMID:16199558 (E. coli genetics, key, GOA EXP), PMID:28208705 (YhhQ preQ0 transporter; context
  only), PMID:41993369 (QueC family SSN, E. coli QueC catalytic residues; 2026 preprint),
  PMID:25353335 (Streptomyces preQ0 natural product; not used), PMID:26391327, PMID:22032275.
- PubMed `Bandarian V[Author] nitrile QueC` -> only PMID:19354300. The Nelp & Bandarian
  2015 amide-intermediate paper (Angew Chem) was not found by the title search I ran
  (`single enzyme transforms carboxylic acid into nitrile`); I did not cite it.
- GOA rows cite PMID:15690043 (Butland 2005 TAP interaction network, abstract only).

## Key findings

- E. coli genetics: queC (ybaX) restores Q to the Q-deficient strain B105 and is needed for a
  step leading to preQ0 [PMID:16199558 "provided the first genetic evidence for the
  involvement of QueC at a step leading to production of preQ0"].
- In vitro (B. subtilis QueC): ATP-dependent conversion of CDG to preQ0 with ammonia as the
  nitrile nitrogen [PMID:19354300 "One can envision that QueC and ToyM catalyze an ATP-dependent
  conversion of CDG to preQ0, with externally derived nitrogen to yield the nitrile group."];
  "ATP (2 mM) was required for the QueC and ToyM."; QueC carries a structural zinc.
- Geobacillus QueC: strict specificity for CDG; AMP and pyrophosphate are co-products
  [PMID:26391327 "determined AMP and pyrophosphate as co-products of preQ0"].
- Step chemistry (RHEA:85175/85179/85183/85187: CDG adenylation, amide formation with NH4+,
  second adenylation, AMP elimination to nitrile): PMID:41993369 summarises the mechanism as
  "two consecutive ATP-dependent reactions via a 7-amido-7-deazaguanine (ADG) intermediate,
  using ammonia as the nitrogen donor". The adenylate intermediates themselves are from the
  Bandarian lab literature that I did not cache; the 2 ATP -> 2 AMP + 2 PPi stoichiometry of the
  overall reaction is consistent with PMID:26391327 (AMP + PPi co-products). The review
  annotates the protein's overall activity, not the steps.
- E. coli queC deletion abolishes Q (complementation assay, PMID:41993369).

## Curation decisions

- GO:0016879 (C-N ligase) IEA: ACCEPT. QueC is EC 6.3.4.20, a carbon-nitrogen ligase
  (EC 6.3.4: other C-N ligases). GO has no specific term (OLS search for
  "7-cyano-7-deazaguanine synthase" returns only the BP GO:0097288), so GO:0016879 is the most
  specific existing MF term. Proposed NTR "7-cyano-7-deazaguanine synthase activity"
  (RHEA:27982), parent GO:0016879. This agrees with the staged RHEA:27982 broadMatch.
- GO:0008616 rows (IBA, IEA, EXP): MODIFY to GO:0160253 de novo tRNA queuosine(34)
  biosynthetic process, following the queE precedent (genes/ECOLI/queE); QueC acts only in de
  novo synthesis from GTP.
- GO:0097288 (7-cyano-7-deazaguanine biosynthetic process): QueC does perform the final step,
  but a QuickGO query for GO:0097288 returned 0 annotations in any species (the same query
  shape returns 28 hits for GO:0008616 in taxon 83333, so it can return positives). The term
  is unused, including for QueD and QueE; not added as NEW, raised as a question instead.
- Protein binding (TufA, PMID:15690043 high-throughput TAP): REMOVE per protein-binding
  policy; no functional consequence shown.
- ATP binding and zinc ion binding IEA: KEEP_AS_NON_CORE (cofactor/cosubstrate of the core
  activity).
