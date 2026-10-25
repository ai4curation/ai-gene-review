# NCU12035: biological evidence

NCU12035 is a predicted GNAT-family acetyltransferase with an acyl-CoA-binding fold. It is expected to transfer an acetyl group to an unidentified acceptor. Its substrate class, physiological pathway, and cellular location remain unresolved; the shared GNAT fold encompasses enzymes that modify proteins and diverse small molecules.

- acetyltransferase activity: The complete GNAT acetyltransferase domain supports broad acetyl-transfer chemistry. Primary classification of eukaryotic GNATs documents the shared acyl-CoA-dependent catalytic scaffold but substantial substrate diversity; no particular acceptor is assigned here.
- transferase activity: The GNAT domain supports acetyltransferase activity as a more informative family-level function than generic transferase or acyltransferase activity. The acceptor substrate remains unresolved.
- acyltransferase activity, transferring groups other than amino-acyl groups: The GNAT domain supports acetyltransferase activity as a more informative family-level function than generic transferase or acyltransferase activity. The acceptor substrate remains unresolved.

Primary evidence excerpts

- [file:NEUCR/NCU12035/NCU12035-uniprot.txt] “DR   InterPro; IPR000182; GNAT_dom.”
- [PMID:33362253] “GNAT enzymes transfer an acyl moiety from acyl coenzyme A to a
wide range of substrates including aminoglycosides, serotonin,
glucosamine-6-phosphate, protein N-termini and lysine residues of histones and
other proteins.”

Provenance: live API snapshot 2026-09-09T03:00:51.831347+00:00. Complete API prediction JSON and all emitted claim IDs, text, and original evidence are preserved in the source and provenance JSON files. Current sequence/annotation data are separate comparison snapshots. Annotation overlap records known biology, not demonstrated training membership. All seven gene-focused Falcon jobs completed; the provider reports were inspected and useful primary leads checked. Publication retrieval used Europe PMC metadata/XML when the canonical PubMed fetch returned HTTP 429.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Sources: the UniProt record, the falcon deep-research report, PMID:33362253 (full text), and new checks in `NCU12035-bioinformatics/` (`gnat_motif_check.py`, `RESULTS.md`).

Identity: V5ILC0 is the only UniProt entry for NCU12035. It has 232 aa, and the PROSITE GNAT domain covers residues 3-184. It is a full-length single-domain GNAT, not a fragment, isoform or alternative gene model. The C-terminal tail (185-232) is S/T/P-rich and has no recognised domain.

Evidence:
- The acetyl-CoA pyrophosphate-binding motif A is conserved: RRMGVG at 107-112 [file:NEUCR/NCU12035/NCU12035-bioinformatics/RESULTS.md "motif A candidate RRMGVG at 107-112 inside_domain=True"].
- In GNATs the donor is "most often acetyl coenzyme A" [PMID:33362253 "The reaction entails transfer of an acetyl group from a substrate donor, most often acetyl coenzyme A, to a substrate acceptor"].
- Acceptor classes are diverse, and many eukaryotic GNAT clusters have no characterised member [PMID:33362253 "We identified 48 clusters with known acetyltransferases and 184 completely uncharacterized clusters."].
- No literature on this gene [file:NEUCR/NCU12035/NCU12035-deep-research-falcon.md "none of the retrieved GNAT literature explicitly mentioned this locus"].

Evolutionary grounding:
- InterPro assigns no PANTHER family or subfamily, only generic GNAT signatures.
- OrthoDB v12 Eukaryota-level group 1321247at2759 has 4 genes, all from Neurospora (N. crassa x2, N. tetrasperma x2). This is a lineage-restricted GNAT with no characterised ortholog.
- There is no PAINT/IBA node. No substrate-specific function can be transferred.
- No characterised relative can be named on phylogenetic grounds. A best-hit paralog was deliberately not chosen.

Decisions (unchanged in substance from the earlier review, rewritten with explicit evidence):
- GO:0016407 acetyltransferase activity (IEA UniRule): ACCEPT. It is as specific as the evidence allows.
- GO:0016740 transferase activity: MODIFY to GO:0016407.
- GO:0016747 acyltransferase activity, transferring groups other than amino-acyl groups: MODIFY to GO:0016407. OLS confirms GO:0016407 is_a GO:0016747.
- No new BP/CC terms. The location is unknown: UniProt records no SignalP or TM feature, and the one hydrophobic window lies in the GNAT core.
- Modules: none relevant in modules/. No PANTHER family review applies.
