# NDUFAF8 (A1L188) review notes

Human NADH dehydrogenase [ubiquinone] 1 alpha subcomplex assembly factor 8;
synonym C17orf89; gene HGNC:33551 on chromosome 17.

## Summary of function

NDUFAF8 is a small (74 aa, ~7.8 kDa) soluble mitochondrial protein that functions as an
assembly factor for respiratory chain Complex I (NADH:ubiquinone oxidoreductase). It is
NOT a structural subunit of the mature holoenzyme and has no known catalytic activity. Its
demonstrated molecular role is to bind and stabilize the early Complex I assembly factor
NDUFAF5; loss of NDUFAF8 leads to loss of NDUFAF5, a stalled Q-module intermediate, and
isolated Complex I deficiency.

## Structural / domain evidence (from UniProt A1L188)

- 74 aa; CHCH domain (residues 22–69) with two Cx9C motifs (25–35, 51–61) and two disulfide
  bonds (25↔61, 35↔51). [file:human/NDUFAF8/NDUFAF8-uniprot.txt "DOMAIN 22..69 /note=\"CHCH\""]
- Keyword "Disulfide bond"; the twin-Cx9C/CHCH architecture is the hallmark of a MIA40/CHCHD4
  disulfide-relay import substrate.
- No enzymatic/EC annotation; despite the RecName "NADH dehydrogenase [ubiquinone] 1 alpha
  subcomplex assembly factor 8", the name refers to its assembly-factor role, not a
  dehydrogenase/oxidoreductase catalytic activity.

## Functional evidence

- Floyd et al. 2016 (PMID:27499296): AE-MS mitochondrial interaction mapping. Validated
  C17orf89 (= NDUFAF8) as a Complex I assembly factor. "we validated C17orf89 as a complex I
  (CI) assembly factor. Disruption of C17orf89 markedly reduced CI activity, and its depletion
  is found in an unresolved case of CI deficiency." Establishes: FUNCTION (CI assembly),
  SUBCELLULAR LOCATION (mitochondrion), and INTERACTION WITH NDUFAF5 (UniProt: "Required to
  stabilize NDUFAF5"; SUBUNIT "Interacts with NDUFAF5"). IntAct A1L188–Q5TEU4, NbExp=11.
- Alston et al. 2020 (PMID:31866046, not cached; cited in UniProt): bi-allelic NDUFAF8
  mutations cause Leigh syndrome with isolated Complex I deficiency (MC1DN34, MIM:618776);
  variant Phe55Leu. Confirms the assembly-factor role is physiologically essential.
- Peker et al. 2023 (PMID:37159021): characterises the two-step import pathway. NDUFAF8 has a
  weak MTS driving TIM23-dependent matrix import while en route being oxidised by the IMS
  disulfide relay (MIA40/CHCHD4). In the matrix, NDUFAF8 "interacts with its partner NDUFAF5
  to stabilize and activate it". "loss of NDUFAF8 results in NDUFAF5 degradation and causes a
  stalled Q module assembly, leading to the accumulation of an assembly intermediate containing
  NDUFS2, NDUFS3, and NDUFA5 and consequently an isolated complex I deficiency." Establishes
  mitochondrial matrix localization (IDA in GOA).

## Localization

- Mitochondrion (UniProt SUBCELLULAR LOCATION, PubMed:27499296; IDA in GOA).
- Mitochondrial matrix — final destination after two-step import (PMID:37159021, IDA in GOA).
  The protein transits the IMS (where it is oxidised by the disulfide relay) but its functional
  site is the matrix, where it stabilizes NDUFAF5.
- HTP mitochondrial-proteome detection (PMID:34800366, mitochondrion) corroborates.

## Interaction annotations (IPI, GO:0005515 protein binding)

Three IPI "protein binding" annotations all record the with/from partner UniProtKB:Q5TEU4
(= NDUFAF5):
- PMID:27499296 (Floyd et al., IntAct/UniProt) — the biologically meaningful, focused
  interaction underlying NDUFAF8 function (NbExp=11).
- PMID:28514442 (BioPlex, Huttlin 2017) — large-scale AP-MS interactome.
- PMID:33961781 (BioPlex 3.0, Huttlin 2021) — large-scale AP-MS interactome.
These support NDUFAF5 binding but the bare "protein binding" (GO:0005515) term is
uninformative; kept as non-core / over-annotated per policy (never REMOVE an IPI).

## Curation decisions

- Core BP: mitochondrial respiratory chain complex I assembly (GO:0032981). IMP from
  PMID:27499296 = ACCEPT (core). IBA and IEA duplicates = ACCEPT / KEEP_AS_NON_CORE.
- Mitochondrion (GO:0005739) IDA (PMID:27499296) = ACCEPT. Matrix (GO:0005759) IDA
  (PMID:37159021) is the more specific/accurate location.
- Do NOT assign NADH-dehydrogenase / oxidoreductase catalytic MF — NDUFAF8 is an accessory
  assembly factor with no demonstrated catalytic activity.
