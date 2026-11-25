# dnaN: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P0A988 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **topological tethering and polymerase processivity**. DnaN is the beta sliding clamp of Escherichia coli. A head-to-tail homodimer encircles DNA and tethers DNA polymerases, increasing processivity and coordinating exchanges between replication and repair enzymes. The clamp loader opens and deposits beta on primed DNA. DnaN also recruits Hda in regulatory inactivation of DnaA and supports translesion synthesis. It is a processivity factor, not a DNA polymerase or proofreading exonuclease.

Primary anchor: [PMID:10924523](https://pubmed.ncbi.nlm.nih.gov/10924523/), “the circular beta sliding clamp facilitates processive DNA replication by tethering the polymerase to primer-template DNA.”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI dnaN` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 61; current rows: 61; inherited NEW: 0; added NEW: 0. Actions: {'ACCEPT': 15, 'REMOVE': 31, 'MODIFY': 6, 'UNDECIDED': 1, 'KEEP_AS_NON_CORE': 8}.

Unresolved claims remain explicit despite COMPLETE review status:

- GO:0006974 (PMID:11967071): The expression-screen annotation is compatible with DNA-damage regulation, but the exact dnaN expression result in the cited study has not been independently verified here. Damage-tolerance functions do not alone establish this specific expression result.

## 2026-11-13: GO:0006974 DNA damage response (IEP, PMID:11967071)

Resolved the remaining UNDECIDED row as KEEP_AS_NON_CORE. Khil & Camerini-Otero 2002 is
abstract-only in the cache and the Wiley full text returned HTTP 403, so its dnaN table entry
was not seen. The claim itself is independently supported: lacZ fusions show mitomycin C
induction of dnaN [PMID:2515428 "the mitomycin C induction of dnaN and dnaQ is not a simple
lexA-regulated process"], and dnaN is listed among DNA damage-inducible replication genes
[PMID:7476872 "In contrast to other DNA damage-inducible replication genes, such as dnaA, dnaN,
dnaQ, and polA"]. The expression response is peripheral to clamp function, hence non-core.
