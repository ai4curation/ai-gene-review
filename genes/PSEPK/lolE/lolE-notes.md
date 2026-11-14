# LolE curation notes

- OpenScientist confirmed Q88KY3/PP_2156 as the LolE membrane subunit from its
  diagnostic MacB/FtsX-family domains, four-pass topology, and position after
  lolD in the PP_2154-PP_2156 cluster
  [file:PSEPK/lolE/lolE-deep-research-openscientist.md].
- The report's LolE cargo-cleft and LolC/LolE asymmetry claims derive from
  characterized Escherichia coli orthologs. They support the role assignment
  but are not promoted to a target-specific GO MF.
- LolE contributes to assembled LolCDE extraction; it is not assigned generic
  transmembrane transporter activity as an isolated subunit.


## 2026-11-07 independent Lol consultation

Q88KY3 belongs to NCBIfam TIGR02212 and InterPro IPR011925 and has four predicted transmembrane helices. Its distinct PP_2156 locus beside PP_2155/lolD supports the LolE role; the shared PTHR30489:SF0 label alone does not distinguish C from E. Assignment to KT2440 is an ortholog inference; the cited E. coli experiments are not assays of this target.

All original rows, source payloads and historical NEW rows remain in their original order. The current review supersedes older action prose above where different. No additional NEW annotation was introduced.

The full E. coli structural study describes a LolC/LolE heterodimer and LolD nucleotide-binding dimer [PMID:30012603, "The LolCDE complex is an ABC transporter that comprises a heterodimer of the transmembrane proteins LolC and LolE, and a homodimer of cytoplasmic LolD, which forms the nucleotide binding domain that hydrolyzes ATP."]. The complete recognition/release activity is therefore represented as a coupled contribution; ATP hydrolysis itself is assigned to LolD. This uses positive functional architecture, not the absence of an isolated-subunit assay. PMID:17509078 reports a reconstituted LolD/LolE partial machinery in vitro; it does not demonstrate native KT2440 LolC dispensability.

The recent E. coli substrate-complex study supports the LolE interaction role [PMID:41557797, "The lipoproteins make a sequence-independent but structurally conserved interaction with a cleft on the surface of the periplasmic domain of LolE that promotes efficient transport."]. PTHR30489:SF0 also contains LolC; it does not by itself prove this subunit-specific interface in KT2440.

GO ancestry was queried live from QuickGO (is_a and part_of, 2026-11-07). GO:0042953 and GO:0044874 are neither ancestors nor descendants of each other. Historical transport proposals remain active; no new proposal is needed to suppress coverage warnings. Query responses are preserved in the consultation artifacts.

PAINT-loss inspection: the target accession is absent from the cached family tree, so lineage losses could not be checked; the tool's concluding no-loss line is not proof of absence. This panel contains electronic TreeGrafter/InterPro/curated-rule annotations rather than IBA rows; no unsupported PAINT-node judgment was added.


## PR6188 follow-up (2026-11-07)

Replace copied cross-gene and repeated generic caveats with annotation-specific reasoning; keep shared ortholog scope in notes and source assessments. Target KT2440 roles are conserved-function inferences from specific identity/architecture and ortholog experiments; no cited E. coli assay is represented as a measurement of this target. Original annotation payloads, qualifiers and proposal lifecycle are unchanged. See analysis/module_audits/bacterial_lol_lipoprotein_trafficking/review-followup/decisions.md for source and ontology adjudication.
