# NCU01540: biological evidence

NCU01540 is a predicted SPX-regulated phosphate transporter of the fungal Pho87/Pho90/Pho91 group. Its SPX regulatory domain and multi-pass permease region support phosphate transport and phosphate/polyphosphate homeostasis. The Pho91 subfamily assignment favors a role in intracellular phosphate handling, but its resident membrane, transport direction, and coupling ion in Neurospora crassa remain unresolved.

- phosphate transmembrane transporter activity: The SPX plus CitMHS permease architecture and Pho91 subfamily assignment support phosphate transport by transfer from experimentally characterized fungal Pho87/Pho90/Pho91 transporters. This supports the curated phosphate-transport IBA without specifying coupling or direction.
- plasma membrane: The IBA derives from PTN000031793 in a broad transporter family. Pho87/Pho90 operate at the plasma membrane whereas the characterized Pho91 is vacuolar, and the target is classified in a Pho91 subfamily. The available evidence does not resolve whether the ancestral plasma-membrane assertion applies to this filamentous-fungal branch; neither location is treated as experimentally established for NCU01540.
- polyphosphate metabolic process: The characterized yeast Pho91 transporter changes vacuolar polyphosphate accumulation through phosphate handling. This supports a conserved indirect contribution to polyphosphate metabolism, not intrinsic polyphosphate synthesis or hydrolysis.
- phosphate ion transport: Phosphate movement is the conserved process of the supported Pho91-like transporter family; the target subfamily assignment and yeast transporter experiments ground this inference.
- membrane: The membrane location is supported by the multi-pass permease architecture independently of whether the resident membrane is plasma or vacuolar.
- transmembrane transporter activity: The supported Pho91 subfamily and characterized fungal phosphate transport justify phosphate transmembrane transporter activity rather than an unspecified solute.
- transmembrane transport: The phosphate substrate is supported by the SPX-Pho91 family assignment and primary characterization of its fungal relatives; phosphate ion transport is the more precise process.

Primary evidence excerpts

- [file:NEUCR/NCU01540/NCU01540-uniprot.txt] “DR   PANTHER; PTHR10283:SF92; LOW-AFFINITY PHOSPHATE TRANSPORTER PHO91; 1.”
- [PMID:17804816] “the low-affinity transporter Pho91 limits poly P accumulation in a strain
lacking PHO85. This phenotype was not caused by a regulatory effect on the PHO
pathway, but can be attributed to the unexpected localization of Pho91 in the
vacuolar membrane.”
- [file:NEUCR/NCU01540/NCU01540-uniprot.txt] “DR   InterPro; IPR004680; Cit_transptr-like_dom.”

Provenance: live API snapshot 2026-09-09T03:00:51.831347+00:00. Complete API prediction JSON and all emitted claim IDs, text, and original evidence are preserved in the source and provenance JSON files. Current sequence/annotation data are separate comparison snapshots. Annotation overlap records known biology, not demonstrated training membership. All seven gene-focused Falcon jobs completed; the provider reports were inspected and useful primary leads checked. Publication retrieval used Europe PMC metadata/XML when the canonical PubMed fetch returned HTTP 429.

## 2026-10-01 re-review (GOA refresh)

GOA refresh added no new rows and no existing rows vanished from the current snapshot. Existing
judgments were re-audited against current curation rules and left unchanged. Added structured
`propagation_review` blocks (with PANTHER PTN source entities) to the IBA rows reviewed as
UNDECIDED/MODIFY, which previously lacked them.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Evidence used: the UniProt record, the PANTHER
PTHR10283 PAINT table and member inventory (`interpro/panther/PTHR10283/`), PMID:17804816
(abstract only), PMID:41324358 (full text), and a reproducible pairwise comparison
(`NCU01540-bioinformatics/compare_sequences_rereview.py`, `RESULTS-rereview.md`; re-run today with
`uv run --script`, output identical).

Identity: Q7RWZ3 is the full-length 844-aa product (SPX 1-260, twelve Phobius TM helices
376-839, CitMHS permease). It is not a fragment, isoform or alternative gene model. It is the only
PTHR10283 member in the N. crassa proteome.

Evolutionary placement: PTHR10283:SF92 (LOW-AFFINITY PHOSPHATE TRANSPORTER PHO91) with
S. cerevisiae Pho91 (P27514) and S. pombe Plt1 (O59712). Pho87/Pho90 are in SF110. Global
identity is 48.6% to Pho91 and 50.2% to Plt1, against about 40% to Pho87/Pho90. Pho91's
inositol-pyrophosphate-binding SPX lysine K237 aligns to NCU01540 K241 (TGFSK motif conserved).
[PMID:41324358 "The pho91K237A allele generates an amino acid substitution in the InsPP-binding patch of the Pho91 SPX domain."]

PAINT nodes: PTN007430421 (phosphate transmembrane transporter activity, seeds = all three yeast
transporters); PTN000815044 (taxon 2759; phosphate ion transport and polyphosphate metabolic
process); PTN000031793 (family root; transmembrane transport, transporter activity, and plasma
membrane). The plasma-membrane seeds are animal SLC13 proteins plus Pho87 (S000000633) and Pho90
(S000003734), not Pho91 (S000005296). No vacuolar-membrane IBD was placed; I took that as
deliberate and proposed no NEW vacuolar term.

Pho91 function [PMID:41324358 "Collectively, our results are consistent with the notion that loss of InsPP binding activates Pho91 to export Pi from vacuoles to the cytosol, enhancing repression of the PHO pathway."]
Flux direction comes from in vivo genetics, not reconstitution.

Changes from the previous review:
- phosphate ion transport (IBA): ACCEPT -> MODIFY to GO:0035435 phosphate ion transmembrane
  transport (OLS ancestors confirm it is_a both GO:0006817 and GO:0055085).
- both transmembrane transport rows (IBA, IEA): replacement changed from GO:0006817, which is not a
  descendant of GO:0055085, to GO:0035435, which is.
- core function directly_involved_in changed to GO:0035435.
- polyphosphate metabolic process kept as non-core. The transporter does no polyP chemistry (VTC
  and the polyphosphatases do); it controls the Pi pool.
- plasma membrane stays UNDECIDED. The root-node PM state conflicts with vacuolar Pho91 in the
  same subfamily. Neurospora lacks an SF110 paralog, so a PM role cannot be excluded.
- Added PMID:41324358 and the RESULTS-rereview.md file reference; added reference_review blocks;
  rewrote the description to be standalone; added suggested questions and experiments.

PANTHER family review (`interpro/panther/PTHR10283/PTHR10283-review.yaml`) agrees on SF92
placement. Its remark that export direction is only a hypothesis predates the in vivo evidence in
PMID:41324358 (which is still not a direct flux assay). There is no disagreement on subfamily
placement. No module in `modules/` covers this family or the fungal phosphate/polyP system.

Relative to review next: S. cerevisiae PHO91 (P27514). It is the experimentally characterized
SF92 member and the PAINT seed (SGD:S000005296). There is no review in the repo (searched by
symbol and accession).
