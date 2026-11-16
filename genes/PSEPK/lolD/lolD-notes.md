# LolD curation notes

- OpenScientist completed after 6602 seconds and confirmed Q88KY4/PP_2155 as a
  227-residue, NBD-only LolD ATPase in the PP_2154-PP_2156 lolC-lolD-lolE
  cluster [file:PSEPK/lolD/lolD-deep-research-openscientist.md].
- ATP hydrolysis is assigned directly to LolD. Lipoprotein extraction and
  release are modeled on the assembled LolCDE complex, not as a LolD
  transmembrane-transporter MF.
- Direct KT2440 kinetics and coupling measurements remain unavailable.


## 2026-11-07 independent Lol consultation

Q88KY4/PP_2155 is the curated LolD ATPase (HAMAP MF_01708, TIGR02211), located between PP_2154/lolC and PP_2156/lolE. Assignment to KT2440 is an ortholog inference; the cited E. coli experiments are not assays of this target.

All original rows, source payloads and historical NEW rows remain in their original order. The current review supersedes older action prose above where different. No additional NEW annotation was introduced.

The full E. coli structural study describes a LolC/LolE heterodimer and LolD nucleotide-binding dimer [PMID:30012603, "The LolCDE complex is an ABC transporter that comprises a heterodimer of the transmembrane proteins LolC and LolE, and a homodimer of cytoplasmic LolD, which forms the nucleotide binding domain that hydrolyzes ATP."]. The complete recognition/release activity is therefore represented as a coupled contribution; ATP hydrolysis itself is assigned to LolD. This uses positive functional architecture, not the absence of an isolated-subunit assay. PMID:17509078 reports a reconstituted LolD/LolE partial machinery in vitro; it does not demonstrate native KT2440 LolC dispensability.

ATP binding is now ACCEPT as essential substrate binding. It is not an is_a/part_of ancestor of ATP hydrolysis. The transmembrane-transport rejection is supported by the full comparative study [PMID:29109272, "LolCDE and FtsEX do not transport substrates across the inner membrane, but instead use cytoplasmic ATP hydrolysis to perform work in the periplasm"], not by an abstract-only failure to detect activity.

GO ancestry was queried live from QuickGO (is_a and part_of, 2026-11-07). GO:0042953 and GO:0044874 are neither ancestors nor descendants of each other. Historical transport proposals remain active; no new proposal is needed to suppress coverage warnings. Query responses are preserved in the consultation artifacts.

PAINT-loss inspection: the target accession is absent from the cached family tree, so lineage losses could not be checked; the tool's concluding no-loss line is not proof of absence. This panel contains electronic TreeGrafter/InterPro/curated-rule annotations rather than IBA rows; no unsupported PAINT-node judgment was added.


## PR6188 follow-up (2026-11-07)

Replace copied cross-gene and repeated generic caveats with annotation-specific reasoning; keep shared ortholog scope in notes and source assessments. Target KT2440 roles are conserved-function inferences from specific identity/architecture and ortholog experiments; no cited E. coli assay is represented as a measurement of this target. Original annotation payloads, qualifiers and proposal lifecycle are unchanged. See analysis/module_audits/bacterial_lol_lipoprotein_trafficking/review-followup/decisions.md for source and ontology adjudication.
