# betC (O69787) notes: Sinorhizobium meliloti 1021 choline sulfatase

Reviewed for the `bacterial_choline_o_sulfate_uptake_and_desulfation` module, where
O69787 is the experimentally characterized BetC exemplar.

## Evidence

- betC is in the betICBA operon and encodes a choline sulfatase acting on
  choline-O-sulfate and, more slowly, phosphorylcholine [PMID:9736747 "a new gene
  (betC) was identified as encoding a choline sulfatase catalyzing the conversion of
  choline-O-sulfate and, at a lower rate, phosphorylcholine, into choline."].
- Genetic requirement: [PMID:9736747 "Choline sulfatase activity was absent from betC
  but not from betB mutants"].
- Physiology: choline-O-sulfate is converted to glycine betaine and can serve as a
  sole C, N and S source [PMID:9736747 "S. meliloti also can use this compound as the
  sole carbon, nitrogen, and sulfur source for growth and that depends on a functional
  bet locus."].
- Purified enzyme kinetics and structure [PMID:29458126 "Sinorhizobium meliloti choline
  sulfatase (SmCS) efficiently catalyzes the hydrolysis of alkyl sulfate
  choline-O-sulfate"]; the active-site numbering (Cys54/fGly54, His104) matches the
  O69787 ACT_SITE features [PMID:29458126 "The nucleophile (Cys54/fGly54) is
  coordinated to His104 and the metal ion."].
- The paper's abstract-level kinetics give kcat/KM 4.8e3 s-1 M-1 for
  choline-O-sulfate vs 12 s-1 M-1 for 4-nitrophenyl sulfate (about 400-fold).

## Decisions

- GO:0047753 choline-sulfatase activity: ACCEPT (core).
- GO:0008484 sulfuric ester hydrolase activity: MODIFY to GO:0047753 (correct but
  general; same treatment as the KT2440 BetC sibling Q88RQ2).
- GO:0042425 choline biosynthetic process (UniPathway): KEEP_AS_NON_CORE. The GO
  definition ("formation of choline") is satisfied, there is no more specific
  choline-O-sulfate catabolism term, but the step is desulfation of an exogenous ester.
- GO:0005737 cytoplasm (TreeGrafter): KEEP_AS_NON_CORE.

## Deep research

`just deep-research RHIME betC --provider openscientist` was run on 2026-11-02 and
produced `betC-deep-research-openscientist.md`. Its identity checks, CXPXR motif
location (C54) and no-TM hydropathy scan agree with the UniProt record. It incorrectly
states "Although BetC itself has not been crystallized"; PMID:29458126 reports the
2.8-Angstrom SmCS structure. Recorded as LOW_QUALITY in the review's reference_review.


## 2026-11-06 cross-taxon choline-sulfate audit

Retained all four original row payloads. Cytoplasm and choline-formation BP now ACCEPT as core: GO:0042425 includes formation, not only de novo synthesis. PMID29458126 methods explicitly identify recombinant 1021/O69787; kcat/KM is 4800 for COS and 13 M^-1 s^-1 for phosphorylcholine at pH7.6. The aryl-sulfate comparison uses differing pH conditions. Native 1998 evidence is 102F34R, and 2022 ligand-bound structures are CECT4857/MH208481 (reported F105L versus GR4), not direct 1021 physiology. The later binding model challenges the older Glu386 interpretation; its Asp/Glu386 inconsistency is disclosed. No secondary phosphatase function was proposed from promiscuity alone.

Reviewed the existing OpenScientist provider report and primary/cached sources; preserved the provider report and its PDF/HTML artifacts. A provider report is already present, so no replacement research run was needed. All machine annotation payloads and raw UniProt/GOA files are unchanged. No new annotation rows were added. Generic family labels and locus proximity do not establish COS transport, a BetD-BetE complex, or substrate promiscuity in unassayed homologs.

Normal force-fetches of PMID:17116241 and PMID:21369825 still returned abstract-only caches; their assay limitations remain explicit. PMID:9736747 also remains abstract-only in the cache after the root fetch. PMC methods were independently accessible at https://pmc.ncbi.nlm.nih.gov/articles/PMC21653/ and explicitly name 102F34R; direct HTML retrieval encountered a challenge, Europe PMC XML returned HTTP500, and NCBI BioC returned no result. No publication cache was hand-edited or invented. Existing abstract quotations remain used as such. Full-text PMID:29458126 and PMID:35503214 distinguish recombinant source strains and assay conditions.

Focused gene validation passed. Preservation is reproducibly checked by `.cache/module-audit-logs/choline-sulfate-20261106/check-existing-four.py`, against the frozen original baseline: 16 total rows, one inherited NEW, zero added rows, eight raw and twelve provider/artifact hashes unchanged. PSEPK/betC retains the advisory about not citing its low-quality provider in annotation support; primary and curated family evidence are used instead.


## PR6105 round1 evidence-scope reassessment (2026-11-06)

The TreeGrafter inference is plausible and is not contradicted, but soluble sulfatase architecture and absence of transmembrane segments do not identify which side of the membrane contains active enzyme. PMID:29458126 characterizes recombinant 1021/O69787 enzyme, not its native compartment. Native bet-locus physiology in PMID:9736747 concerns 102F34R and does not supply a compartment-resolving assay for 1021; the CECT4857 structural work in PMID:35503214 likewise does not establish native 1021 localization. Downstream glycine-betaine production cannot locate the preceding sulfatase reaction. Retain the machine-sourced row as UNDECIDED and omit the core location, consistently with Ruegeria; molecular-function and choline-formation claims remain supported.

The cytoplasm row is retained as UNDECIDED, and no activity location is asserted in core_functions. Molecular-function verdicts, original annotation payloads, raw sources and genuine provider research remain unchanged. No publication cache was refreshed.
