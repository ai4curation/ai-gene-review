# lolA curation notes

- Q88FS9 is the reviewed KT2440 LolA ortholog, annotated as a periplasmic outer-membrane lipoprotein carrier [file:PSEPK/lolA/lolA-uniprot.txt, "RecName: Full=Outer-membrane lipoprotein carrier protein"].
- UniProt places LolA between the inner and outer membranes and records the canonical +2 Asp retention rule [file:PSEPK/lolA/lolA-uniprot.txt, "Only forms a complex with a lipoprotein if the residue after the N-terminal Cys is not an aspartate"].
- GO:0030288 is retained as the specific diderm-bacterial periplasm location; GO:0042597 is biologically true but redundant.
- OpenScientist was allowed to run for the full configured 7200 seconds on
  2026-09-01 and returned no report. No provider-named deep-research file was
  synthesized manually; the review remains grounded in the exact target
  UniProt record and the module-level primary/retrieval evidence.


## 2026-11-07 independent Lol consultation

Q88FS9 is assigned to LolA by curated HAMAP MF_00240 and NCBIfam TIGR00547; its cleavable signal peptide and curated periplasmic location support the compartment. Assignment to KT2440 is an ortholog inference; the cited E. coli experiments are not assays of this target.

All original rows, source payloads and historical NEW rows remain in their original order. The current review supersedes older action prose above where different. No additional NEW annotation was introduced.

The carrier role is supported by the curated HAMAP rule and the original E. coli soluble-complex experiment [PMID:7628437, "p20 formed a soluble complex only with outer membrane-directed lipoproteins such as Lpp"]. The historical carrier proposal is retained. The Asp+2 retention rule remains a target-specific experimental question; general rule text is not a KT2440 substrate-panel assay. A real Falcon attempt on 2026-11-07 exited 1 with HTTP 403 authentication failure (cache log lolA-falcon.log); no provider report was fabricated.

GO ancestry was queried live from QuickGO (is_a and part_of, 2026-11-07). GO:0042953 and GO:0044874 are neither ancestors nor descendants of each other. Historical transport proposals remain active; no new proposal is needed to suppress coverage warnings. Query responses are preserved in the consultation artifacts.

PAINT-loss inspection: the target accession is absent from the cached family tree, so lineage losses could not be checked; the tool's concluding no-loss line is not proof of absence. This panel contains electronic TreeGrafter/InterPro/curated-rule annotations rather than IBA rows; no unsupported PAINT-node judgment was added.


## PR6188 follow-up (2026-11-07)

Replace copied cross-gene and repeated generic caveats with annotation-specific reasoning; keep shared ortholog scope in notes and source assessments. Target KT2440 roles are conserved-function inferences from specific identity/architecture and ortholog experiments; no cited E. coli assay is represented as a measurement of this target. Original annotation payloads, qualifiers and proposal lifecycle are unchanged. See analysis/module_audits/bacterial_lol_lipoprotein_trafficking/review-followup/decisions.md for source and ontology adjudication.
