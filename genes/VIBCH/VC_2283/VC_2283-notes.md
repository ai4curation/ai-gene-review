# aatX (Q9KPS9, VC_2283) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NZ_NMTP01000136.1_1` (*Vibrio cholerae*, 452 aa), https://gene-annotate-dashboard.kbase.us/review/NZ_NMTP01000136.1_1
- Identical to N16961 VC_2283 / Q9KPS9 over all 451 residues; the dashboard model has one extra N-terminal Val (alternative start). Mapping: hackathon run `20261030T212629Z-finalize-vibch-mapping`.
- Dashboard page and GO terms come from run `20261030T212648Z-dashboard-page-nz-nmtp01000136-1-1` and are frozen in `VC_2283-dashboard-prediction-evidence/`.
- **Naming:** The directory is named by locus tag because UniProt gives no gene symbol, only `OrderedLocusNames=VC_2283` (project rule: use the UniProt gene symbol when there is one, else the locus tag). An earlier draft filed it as `aatX`; it was moved back on 2026-10-30. The published name *aatX* (Jugder et al. 2022, PMID:36130487: "We named this gene aatX (aromatic amino acid transporter X).") is kept as an alias, together with `VC2283` and the dashboard id.

## Dashboard call

> Sodium-dependent tryptophan symporter AatX mediating tryptophan uptake across the inner membrane. (Tier A; GO:0005886, GO:0015196, GO:0015827)

Verdict: **supported**. All three GO terms are COR (GOA has only GO:0016020 membrane, IEA).

Caveats on the call:
- "Sodium-dependent" is a family inference; it has not been measured for AatX.
- The experimental evidence is indirect. A ΔhapR ΔtrpT ΔaatX triple mutant consumes less tryptophan than ΔhapR. A single aatX deletion has no significant effect. No labelled-substrate uptake assay and no substrate-range test exist.
- The paper does not name a strain in the cached text. The VC2283 tag is the N16961 locus tag.

## Paralog question (shared with VC_1669)

See `../VC_1669/VC_1669-bioinformatics/RESULTS.md` (BERIL run `20261030T213758Z-vc2283-vc1669-nss-paralog-comparison`).
- VC2283 and VC1669 are 55.5% identical. Both are 32-48% identical to every characterized NSS transporter (TnaT, MhsT, LeuT, SO_4339, YocR), so identity cannot assign substrate to either.
- VC2283 has a near-consensus TrpR operator (`TGTACTAGTTAACTAGTGTG`, 3/20 mismatches to the *E. coli* trpO). It is the only CDS outside the trp operon with such a site. VC1669 has none (9 mismatches, the genome median).
- **Conclusion:** VC2283/AatX is the characterized tryptophan transporter. The VC_1669 call transferred the AatX tryptophan assignment to a paralog; it is scored PLI in the VC_1669 sidecar.

## Literature checks

- No other paper names VC2283 or aatX. Europe PMC full-text search for "VC2283" returns PMID:36130487 and two unrelated hits (an immunostimulatory-protein screen PMID:19696891, and a sensor review).
- Two PubMed searches found nothing else: (Mey AR / Payne SM / Mourino) AND *V. cholerae* AND (tryptophan / indole / amino acid transport), and *V. cholerae* tryptophan transporter/uptake/permease AND indole. The Mey/Payne hits are about CsrA, Feo, siderophores and porins. No other study assigns a *V. cholerae* tryptophan transporter. The indole/biofilm literature concerns tryptophanase (VCA0161, beside VCA0160, "aromatic amino acid transporter" in RefSeq). That transporter was not analysed here. The paper's `trpT` locus is not given in the cached text; VCA0160 and VCA0772 ("aromatic amino acid transport family protein") are candidates, but this is unverified.
- Both deep-research reports (claude-code provider) missed PMID:36130487 and call the substrate undetermined.

## Tooling

- `just fetch-fitness VIBCH aatX`: failed with "No FEBA organism mapping for 'VIBCH'" and "no FEBA data source was reachable". *V. cholerae* has no Fitness Browser mapping here.
- `just fetch-pmid 36130487` first cached the abstract only. `just fetch-pmid 36130487 --force` retrieved the PMC full text (XML), which the verbatim quotes need.
- `just fetch-pmid` hit HTTP 429 (NCBI rate limit) several times; retrying with a delay worked.
- `just validate-terms` on the PredictionReview sidecar fails on `locus_tag`, because it validates against GeneReview. This is expected; `validate-predictions` (which runs `validate-prediction-terms`) passes.
