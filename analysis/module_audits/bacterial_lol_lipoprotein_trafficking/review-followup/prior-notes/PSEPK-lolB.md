# lolB curation notes

- Q88PX4 is the reviewed KT2440 LolB ortholog [file:PSEPK/lolB/lolB-uniprot.txt, "RecName: Full=Outer-membrane lipoprotein LolB"].
- Its role is terminal delivery after LolA, not generic protein transport [file:PSEPK/lolB/lolB-uniprot.txt, "incorporation of lipoproteins in the outer membrane after they are released by the LolA protein"].
- GO:0044874 and cell outer membrane localization capture the core role; broad GO:0015031 is marked over-annotated.
- OpenScientist supports the terminal receptor/insertion role and the
  separation of cargo binding from membrane delivery
  [file:PSEPK/lolB/lolB-deep-research-openscientist.md "Two separable activities"].
- Nearly all mechanistic experiments are on E. coli LolB, and no direct
  KT2440 LolB biochemistry or structure was found
  [file:PSEPK/lolB/lolB-deep-research-openscientist.md "Nearly all mechanistic detail derives from the *E. coli* ortholog"].
- Essentiality in KT2440 is not asserted as established because it was inferred
  from other diderm bacteria rather than a KT2440 knockout.


## 2026-11-07 independent Lol consultation

Q88PX4 is a curated HAMAP MF_00233 LolB-family protein with a signal peptide and lipidated mature N-terminal cysteine; outer-membrane placement and terminal delivery are supported by the curated rule. Assignment to KT2440 is an ortholog inference; the cited E. coli experiments are not assays of this target.

All original rows, source payloads and historical NEW rows remain in their original order. The current review supersedes older action prose above where different. No additional NEW annotation was introduced.

Protein transport is true and is now refined to lipoprotein transport, not marked overannotated. The existing insertion NTR supplies the previously missing core molecular-function descriptor. Positive ortholog transfer is explicit [PMID:9384574, "When the Lpp-LolA complex was incubated with a water-soluble LolB derivative, Lpp was transferred from LolA to LolB."]; this cache is abstract-only, and no KT2440 essentiality or depletion result is asserted.

GO ancestry was queried live from QuickGO (is_a and part_of, 2026-11-07). GO:0042953 and GO:0044874 are neither ancestors nor descendants of each other. Historical transport proposals remain active; no new proposal is needed to suppress coverage warnings. Query responses are preserved in the consultation artifacts.

PAINT-loss inspection: no PANTHER family is present in the LolB source record, so lineage losses could not be checked. This panel contains electronic TreeGrafter/InterPro/curated-rule annotations rather than IBA rows; no unsupported PAINT-node judgment was added.
