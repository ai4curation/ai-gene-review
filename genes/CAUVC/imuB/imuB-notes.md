# imuB (CC_3212, Q9A3J2) curation notes

- No provider deep research is available for this gene; no `-deep-research-*.md` file was
  generated in this session. The review rests on the two cached primary papers and UniProt.
- imuB and dnaE2 act in one damage-tolerance pathway; the double mutant is not additive.
  [PMID:15886391, "The imuB dnaE2 double mutant does not exhibit an exacerbated phenotype, indicating again that these genes cooperate in the same pathway of damage tolerance."]
- The UV mutational signature is changed identically in imuB and dnaE2 mutants, which is
  what makes the pathway's output mutagenic rather than merely protective.
  [PMID:15886391, "The mutation signature of UV light is remarkably similar in dnaE2 and imuB strains."]
- DinB is not part of this pathway in C. crescentus: a dinB imuB double mutant is no worse
  than imuB alone.
  [PMID:15886391, "The dinB imuB strain presents the same levels of UV-induced mutagenesis as the imuB single mutant, confirming that DinB is not implicated in error-prone repair in the conditions tested."]
- The adaptor role (GO:0030674) is transferred from the mycobacterial ortholog, where it
  rests on two-hybrid data plus a clamp-binding separation-of-function allele.
  [PMID:20615954, "Yeast two-hybrid analyses indicate that ImuB interacts with both ImuA' and DnaE2, as well as with the beta-clamp."]
  The same paper states the catalytic residues are missing in ImuB proteins generally.
  [PMID:20615954, "Despite retaining structural features characteristic of Y-family members, ImuB homologs lack conserved active-site amino acids required for polymerase activity."]
- The single existing GOA row (GO:0006281, DNA repair) is a UniProt combined-pipeline IEA
  whose basis is the UmuC domain IPR001126 plus TreeGrafter node PANTHER:PTN000118183. It
  is a TreeGrafter route, not a PAINT IBA; PTHR35369's only PAINT node is PTN002176549
  (GO:0006281, seeded by M. tuberculosis O50419).

## 2026-11-07 comparative consultation

All three source payloads remain in order, including both historical NEW rows. The ImuB adaptor assignment is retained explicitly as inference. The 2005 primary places CC3212 in a specific branch distinct from ordinary DinB, while native epistasis links it to DnaE2. Mycobacterial two-hybrid/mutant results and independent direct Myxococcus ImuA-ImuB binding (PMID:38591662) make an interaction-platform role plausible beyond generic fold membership. None of these measures the exact Caulobacter partners, clamp-binding surface, stoichiometry, oligomerization or polymerase chemistry. The core description now states this boundary. No DNA binding is transferred from the Myxococcus N-terminal ImuB truncation.

Mutational spectra support a shared mutagenic pathway, but are not a direct assay of nucleotide insertion opposite a defined lesion. The source NA1000 strain derives from CB15. Native imuB complementation used a cosmid containing imuA and imuB but not dnaE2; the authors explicitly used it to exclude downstream polar effects. No claim of an isolated biochemical Caulobacter mutasome is made.

Current GO:0006281 includes bypass in its definition. Thus the old explanation that DNA repair necessarily removes lesions is superseded. MODIFY to the specific TLS process remains warranted, as a process-specific correction rather than an asserted is_a refinement: the current TLS branch is under DNA damage tolerance, not DNA repair.

A genuine Falcon request failed with HTTP403 authentication; no provider output was invented. The full 2005 and 2010 primary papers and 2024 comparator were inspected. The PANTHER/TreeGrafter identifiers describe source inference; no new PAINT claim is asserted for these non-IBA rows.
