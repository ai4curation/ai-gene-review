# dnaN curation notes

## Annotation-reviewer pass (2026-09-01)

Consulted the annotation-reviewer workflow against all 10 current GOA rows, reviewed UniProt P0A120, and the orthologous localization source P0A988. Accepted cytoplasmic localization, DNA replication/elongation, polymerase III complex membership, and the duplicate orthology-supported localization; retained generic DNA binding as non-core. Removed DNA polymerase and 3'-5' exonuclease activities because those catalytic functions belong to DnaE and DnaQ, respectively. Marked identical-protein binding and broad DNA biosynthesis as over-annotated. Added the missing specific processivity-factor function from the exact UniProt statement that DnaN confers DNA tethering and processivity. No seeded GOA row remains pending.


## Annotation-reviewer follow-up — 2026-11-06

Reviewed every original annotation against target architecture and the available literature. Original non-review row fields, inherited NEW rows, raw UniProt and GOA remain frozen; baseline is in `.cache/module-audit-logs/chromosomal-replication-20261106/`. Default Falcon was genuinely attempted for this gene and failed HTTP403 authentication; no provider text was fabricated. These are manual research notes.

Target P0A120 is the KT2440 record. Curated HAMAP/RuleBase and domain statements provide conserved-function evidence; no automatic GO cross-reference is used as biological support. P. aeruginosa reconstitution is comparative evidence, not a direct assay of this KT2440 sequence. Existing IEA annotations are assessed on the function, not the evidence code. No IBA rows occur in this target, so a PAINT-loss audit is not applicable.

- GO:0003677 DNA binding: ACCEPT. The beta clamp directly encircles and interacts with DNA. DNA binding is intrinsic to clamp function rather than a peripheral consequence.
- GO:0003887 DNA-directed DNA polymerase activity: REMOVE. The clamp is a non-catalytic processivity factor; polymerase chemistry is performed by DnaE. Pseudomonas reconstitution separates beta from the alpha-epsilon catalytic complex.
- GO:0005737 cytoplasm: ACCEPT. The beta clamp operates on bacterial chromosome DNA in the cytoplasm. The ISS donor supports a conserved location rather than target-specific imaging.
- GO:0006260 DNA replication: MODIFY. The direct processivity contribution supports strand elongation during replication, a descendant already present.
- GO:0006271 DNA strand elongation involved in DNA replication: ACCEPT. The clamp physically tethers polymerase to its DNA template, thereby performing structural work required for processive strand elongation.
- GO:0008408 3'-5' exonuclease activity: REMOVE. The beta clamp lacks the DnaQ proofreading catalytic role; the editing activity of the holoenzyme must not be assigned to this processivity subunit.
- GO:0009360 DNA polymerase III complex: ACCEPT. The beta clamp is a polymerase III holoenzyme component, corroborated by Pseudomonas replicase reconstitution.
- GO:0042802 identical protein binding: ACCEPT. Head-to-tail homodimerization forms the functional DNA-encircling ring. Identical-protein binding therefore describes a specific core assembly property; it is not the uninformative bare GO0005515 term.
- GO:0071897 DNA biosynthetic process: ACCEPT. The clamp contributes the DNA-tethering scaffold that enables processive DNA production. Its non-catalytic status does not exclude structural participation in biosynthesis, and no nonexistent ancestor relationship with replication is assumed.
- GO:0030337 DNA polymerase processivity factor activity: NEW. Retain the inherited proposal and original payload. The target belongs to the beta-clamp family, and Pseudomonas reconstitution directly separates the beta processivity factor from polymerase and loader. The processivity activity adds a distinct regulator function, not polymerization or nuclease chemistry.

Primary sources used: PMID:15611049. Independent frozen support: file:PSEPK/dnaN/dnaN-uniprot.txt.
