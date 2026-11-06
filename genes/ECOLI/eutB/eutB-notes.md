# eutB (P0AEJ6, E. coli K-12) notes

## Sources and literature search
- No deep-research file was generated for this gene (no provider was run in this session). The review rests on
  the UniProt record (`eutB-uniprot.txt`), the cached publications below, the PTHR39329 PAINT file, and the
  KT2440 shell inventory in `genes/PSEPK/eutC/eutC-bioinformatics/RESULTS.md` (E. coli used as positive control).
- Literature checked (all abstract-only in the cache unless noted): PMID:15466038, PMID:19762342,
  PMID:20519496, PMID:21142024 (fetched this session), PMID:29797764, PMID:6376700, PMID:2197274,
  PMID:23585538, PMID:27450681, PMID:18304323 (full text).

## Biology
- EutB is the large (alpha) subunit of AdoCbl-dependent ethanolamine ammonia-lyase (EAL, EC 4.3.1.7)
  [PMID:19762342 "The eutB and eutC genes in the eut operon encoded the large and small subunits of the enzyme, respectively. The enzyme existed as the heterododecamer alpha(6)beta(6)."]
- Active site is in the EutB TIM barrel; cobalamin sits at the alpha/beta interface
  [PMID:20519496 "The active site is in the (beta/alpha)(8) barrel of the alpha-subunit; the beta-subunit covers the lower part of the cobalamin that is bound in the interface of the alpha- and beta-subunits."]
- Substrate-binding residues (Arg160, Glu287 ...) are in EutB [PMID:20519496 "Argalpha(160) contributes to substrate binding most likely by hydrogen bonding with the O1 atom."]
- UniProt FT BINDING: adenosylcobalamin contacts at EutB 194, 246, 295, 401 and substrate contacts at 160-162,
  193, 287, 362 (ECO:0000269 PMID:20519496/21142024 plus PDB). EutC also has experimental cobalamin contacts
  (207, 228, 258), so both subunits bind the cofactor directly.
- Suicide inactivation and EutA-dependent reactivation [PMID:15466038 "The holoenzyme of adenosylcobalamin-dependent ethanolamine ammonia lyase undergoes suicidal inactivation during catalysis as well as inactivation in the absence of substrate."]
- Strain caveat: in MG1655 the eut operon is split by the CPZ-55 prophage (UniProt CAUTION, PMID:9278503).

## Localization
- E. coli K-12 encodes a full Eut shell set (EutS, EutM, EutN, EutL, EutK; RESULTS.md control).
- Targeting signal is on EutC (Salmonella EutC 1-19) [PMID:27450681 "the signal sequence EutC1-19 targets cargo to the interior of nanocompartments via a hydrophobic interaction with a helix on shell protein EutS"];
  but the genetic model of Huseby & Roth places EutBC outside the shell [PMID:23585538 "The model predicts that EutBC (ethanolamine-ammonia lyase) lies outside the compartment, using external coenzyme B12 and injecting its product, acetaldehyde, into the lumen"].
- Cytosol: IDA from cytosol proteomics (PMID:18304323, MC4100 cytosol; protein table in supplement, not cached) and PAINT IBD.
- Decision: cytosol ACCEPT; GO:0031471 KEEP_AS_NON_CORE (contested, IEA only); GO:0031469 MODIFY to GO:0031471.

## Decisions (orchestrator convention, applied across E. coli and KT2440 eutB/eutC)
- GO:0008851: EutB `enables` (catalytic subunit) -> ACCEPT all rows.
- GO:0031419 cobalamin binding `enables` -> ACCEPT (experimental cobalamin-contact residues in EutB).
- GO:0006520 amino acid metabolic process -> REMOVE (ethanolamine is not an amino acid; GO:0046336 is not
  under GO:0006520).
- GO:0009350 and GO:0046336 -> ACCEPT all rows.
- Core: MF GO:0008851, complex GO:0009350, process GO:0046336.
