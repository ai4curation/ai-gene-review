# lolC curation notes

- Q88KY5 is a multi-pass membrane member of the ABC-4 LolC/E subfamily [file:PSEPK/lolC/lolC-uniprot.txt, "Belongs to the ABC-4 integral membrane protein family. LolC/E subfamily"].
- The PSEPK record lacks a direct function comment, so the specific pathway role remains orthology-based pending OpenScientist retrieval.
- LolC is modeled as an integral component of the LolCDE extraction machinery,
  not as an independent pore-forming transporter.
- OpenScientist distinguishes LolCDE from pore-forming ABC transporters:
  membrane conformational changes extract lipoprotein from the outer leaflet
  and transfer it to LolA
  [file:PSEPK/lolC/lolC-deep-research-openscientist.md "LolC operates by mechanotransmission, not by transmembrane substrate passage"].
- The initial generic GO:0022857 contribution was therefore removed from the
  core function and module. The specific biological-process role remains.
- LolA docking through LolC Hook/Pad elements is established in E. coli; no
  direct Q88KY5 experiment was found
  [file:PSEPK/lolC/lolC-deep-research-openscientist.md "No study in the knowledge base characterizes *P. putida* KT2440 LolC"].


## 2026-11-07 independent Lol consultation

Q88KY5 belongs to NCBIfam TIGR02212 and InterPro IPR011925 and has four predicted transmembrane helices. Its distinct PP_2154 locus beside PP_2155/lolD supports the LolC role; the shared PTHR30489:SF0 label alone does not distinguish C from E. Assignment to KT2440 is an ortholog inference; the cited E. coli experiments are not assays of this target.

All original rows, source payloads and historical NEW rows remain in their original order. The current review supersedes older action prose above where different. No additional NEW annotation was introduced.

The full E. coli structural study describes a LolC/LolE heterodimer and LolD nucleotide-binding dimer [PMID:30012603, "The LolCDE complex is an ABC transporter that comprises a heterodimer of the transmembrane proteins LolC and LolE, and a homodimer of cytoplasmic LolD, which forms the nucleotide binding domain that hydrolyzes ATP."]. The complete recognition/release activity is therefore represented as a coupled contribution; ATP hydrolysis itself is assigned to LolD. This uses positive functional architecture, not the absence of an isolated-subunit assay. PMID:17509078 reports a reconstituted LolD/LolE partial machinery in vitro; it does not demonstrate native KT2440 LolC dispensability.

LolA recruitment is established for E. coli [PMID:30012603, "LolC recruits LolA by means of a finger-like protrusion that we term the Hook and a patch of surface residues termed the Pad."]; the target assignment remains an inference and no residue-specific transfer or claim that no KT2440 experiment could exist is made.

GO ancestry was queried live from QuickGO (is_a and part_of, 2026-11-07). GO:0042953 and GO:0044874 are neither ancestors nor descendants of each other. Historical transport proposals remain active; no new proposal is needed to suppress coverage warnings. Query responses are preserved in the consultation artifacts.

PAINT-loss inspection: the target accession is absent from the cached family tree, so lineage losses could not be checked; the tool's concluding no-loss line is not proof of absence. This panel contains electronic TreeGrafter/InterPro/curated-rule annotations rather than IBA rows; no unsupported PAINT-node judgment was added.
