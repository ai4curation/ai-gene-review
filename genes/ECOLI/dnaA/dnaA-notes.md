# dnaA: manual annotation review

## 2026-11-06 replication audit

Normal accession-aware fetch seeded P03004 (Escherichia coli K-12); the pristine machine payloads and two raw-source hashes were frozen in `.cache/module-audit-logs/chromosomal-replication-20261106/ecoli-seeded-baseline.json` before editing. This is a new review of an already named module exemplar, not a re-review of pre-existing ECOLI curation.

The central activity is **origin recognition, duplex opening and regulated helicase recruitment**. DnaA is the ATP-regulated initiator of Escherichia coli chromosome replication. It recognizes DnaA boxes at oriC, assembles an oligomeric origin complex, opens the DNA-unwinding element and recruits the DnaB helicase. Conversion of ATP-DnaA to ADP-DnaA helps prevent reinitiation. DnaA also binds other chromosomal regulatory sites and autoregulates its transcription. It is predominantly associated with cytoplasmic DNA, with a smaller peripheral inner-membrane-associated population implicated in nucleotide exchange.

Primary anchor: [PMID:19833870](https://pubmed.ncbi.nlm.nih.gov/19833870/), “there is a temporally similar nucleoprotein complex comprising the initiator protein DnaA bound to three high-affinity recognition sites in the unique origin of replication, oriC.”

All seeded annotations were assessed, including repair, regulation, localization and protein-complex claims outside the narrow replication-module steps. Bare protein-binding rows retain their original interaction provenance; REMOVE means the term is uninformative, not that the interaction is false. Experimental assertions are not rejected merely because an abstract omits the individual target. Full-text and abstract-only availability are recorded in references; no inaccessible target table is claimed to have been inspected.

`just paint-losses ECOLI dnaA` reported no applicable IRD or IKR. IBA judgments concern inherited functions and target biology, not donor counts. The default Falcon research command was attempted and failed with HTTP403 authentication/access failure. No provider report was authored or fabricated; these are manual notes.

Original rows: 54; current rows: 54; inherited NEW: 0; added NEW: 0. Actions: {'MODIFY': 8, 'ACCEPT': 28, 'REMOVE': 13, 'KEEP_AS_NON_CORE': 5}.

Membrane association is a minority peripheral population (PMID22574163, about10% in the tested setting), distinct from oriC-associated activity. Negative initiation regulation is supported by DnaA ATP hydrolysis in RIDA (PMID21708944); Dps/L2 inhibition experiments alone would not establish that DnaA executes their inhibitory action.
