# grpE manual review notes

- Deep research and FEBA fitness summaries were unavailable for this review; the synthesis below is based on the cached UniProtKB record and the cached publications cited by the seeded GOA rows.
- GrpE's core biochemical activity is adenyl-nucleotide exchange on the DnaK Hsp70 ATPase cycle. Liberek et al. showed that GrpE alone increases release of DnaK-bound ATP or ADP, and Gamer et al. showed that GrpE stimulates nucleotide release from DnaK-DnaJ-sigma32 complexes. The IBA and InterPro2GO nucleotide-exchange rows are therefore accepted.
- GrpE is also a direct DnaK co-chaperone. The Harrison et al. DnaK ATPase-domain structure contains an asymmetric DnaK:GrpE2 complex, and the Johnson et al. coimmunoprecipitation paper supports DnaK-GrpE binding in vivo and in vitro. Generic GO:0005515 rows whose WITH/FROM partner is DnaK are modified to GO:0051087 protein-folding chaperone binding; GroEL and MntH rows from broad interaction screens are removed rather than promoted to GrpE chaperone biology.
- Homodimerization and DnaK-GrpE complex formation are true structural facts for GrpE, but they are implementation details of the nucleotide-exchange reaction, so they are kept as non-core rather than represented as core molecular functions.
- The Hsp70-Hsp40-NEF unfoldase row is accepted for GrpE because GrpE is the E. coli nucleotide exchange factor that recycles DnaK in this ATP-dependent misfolded-protein remodeling system.
- GrpE is cytosolic and heat inducible; its reversible thermal transition around the heat-shock range suggests that it can bias DnaK toward the high-affinity ADP state at elevated temperature.


## 2026-11-06 comparative DnaK-cycle audit

Retained the directly supported nucleotide-exchange function and DnaK binding. GrpE accelerates nucleotide release; increased steady-state ATP turnover is not an assertion that GrpE catalyzes ATP hydrolysis. Retained homodimerization as structural non-core context and refined cytoplasm to cytosol. The thermal transition and sigma32 effects are E. coli findings, not assumed universal properties of all GrpE proteins.

All historical annotation rows, including inherited NEW proposals, were preserved outside their review fields; no new annotation rows were added. Source UniProt/GOA, genuine research and prediction artifacts were protected against the pre-edit baseline. PAINT-loss checks found no applicable IRD or IKR.

Primary scope: [PMID:1826368] separates DnaJ stimulation of DnaK-bound ATP hydrolysis from GrpE-mediated nucleotide release. [PMID:7937953] follows denatured firefly luciferase through the E. coli DnaK-DnaJ-GrpE cycle. [PMID:20953191] measures remodeling of a tested misfolded luciferase species; its ATP cost is assay-specific, not a universal per-client constant. Normal forced fetches of those papers and PMID:11162122 and PMID:9103205 succeeded but remained abstract-only. Exact assay construct and E. coli substrain details not stated in those abstracts are not invented. Existing curator assignments are retained where independently supported; the particular complex-assembly process rows citing PMID:9103205 remain UNDECIDED because a structural complex does not alone resolve the assembly-process assertion.

Comparative boundary: [PMID:11162122, abstract] states "Here, DnaJ does not stimulate the DnaK-mediated ATP hydrolysis" for Thermus thermophilus. This is not negative evidence for the E. coli or KT2440 proteins, but rules out treating J-domain identity alone as a universal kinetic guarantee. Official QuickGO definitions were retrieved on 2026-11-06; GO:0051082 and GO:0003767 are obsolete, while GO:0044183 describes folding assistance and GO:0051087 binding to a chaperone protein. Client binding is not chaperone-partner binding.

No genuine provider report was present. The normal Falcon command was attempted and returned HTTP403 authentication/access failure. These are manual audit notes, not a fabricated provider report.


## 2026-11-06 — PR6125 evidence/action follow-up

7: align GrpE homodimerization with its core functional architecture. Original machine rows and source bytes were frozen before edits. Published PMID and raw-source evidence remain separate from native target-specific experiments. Core location changes, where made, retain cytoplasm when finer cytosol resolution was not independently supported. Physiological uncertainty is not treated as automatic disproof of a directly measured molecular activity.
