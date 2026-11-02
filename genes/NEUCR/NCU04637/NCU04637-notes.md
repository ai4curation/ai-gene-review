# NCU04637 research notes

Review date: 2026-09-09T03:17:51.839101+00:00. Target: Q7S3B9, NEUCR, 467 residues. Identity is anchored to the frozen current UniProt accession and gene record. The accession-specific fetch seeded all 12 current GOA rows.

## Evidence basis

NCU04637 encodes a fungal Rvs167-family endocytic adaptor with an N-terminal BAR domain and a C-terminal SH3 domain. Comparative evidence supports lipid binding and association with cortical actin patches, where Rvs proteins help organize endocytic membrane invaginations and vesicle scission. The detailed localization dynamics and interaction partners of the Neurospora protein remain to be established.

- file:NEUCR/NCU04637/NCU04637-uniprot.txt: “DR   PANTHER; PTHR47174:SF1; REDUCED VIABILITY UPON STARVATION PROTEIN 167; 1.”
- PMID:20610658: “We show that the purified Rvs161-Rvs167 complex binds to liposomes in a curvature-independent manner and promotes tubule formation in vitro.”
- PMID:20610658: “Rvs161 consists solely of a BAR domain, whereas Rvs167 is composed of a BAR domain followed by a region rich in glycine, proline, and alanine (GPA), and an SH3 (Src-homology 3) domain at its C-terminus”

## Source claim provenance

The full API prediction JSON is preserved without deleting any fields. Function and location reports retain original words, SL identifiers and entire evidence objects. GO sidecars preserve all emitted GO IDs and labels; main reviews assess the independent current GOA rows.

- GO:0005737: [{"evidenceCode": "ECO:0008006", "id": "ProtNLM2", "properties": [{"key": "model_score", "value": "1.00"}, {"key": "string_match_text", "value": "GO:0031097"}, {"key": "string_match_location", "value": "GO"}, {"key": "string_match_type", "value": "hydrated"}], "source": "Google"}]

## Research execution

The original Falcon attempt failed with HTTP 429 (rate limit), and the configured Perplexity-lite fallback failed with HTTP 401 (insufficient quota). No provider report was returned for this gene, and no duplicate provider request was submitted. The companion deep-research-manual.md is an explicitly manual synthesis of inspected sources, not provider output.

## Rvs167 and anatomical scope

The target architecture is BAR 17–269 plus SH3 407–467, not simply an unspecified BAR protein. PTHR47174:SF1 is explicitly Rvs167; the broader InterPro BIN3/RVS161-like label is not itself a specific Rvs161 call. PMID:20610658 distinguishes Rvs161 from Rvs167 by the latter’s SH3-containing architecture. The literal fly-derived paragraph is incompatible with fungal anatomy, while its conserved endocytosis component remains well supported. PMID:19596778 reports Candida RVS167 mutant defects in actin patch polarization, supporting the process annotation. The medial-cortex and mating-projection-tip patterns remain uncertain for the Neurospora protein.

## 2026-10-01 re-review (GOA refresh)

GOA refresh added no new rows and no existing rows vanished from the current snapshot. Existing
judgments were re-audited against current curation rules and left unchanged. Added structured
`propagation_review` blocks (with PANTHER PTN source entities) to the IBA rows reviewed as
UNDECIDED/MODIFY, which previously lacked them.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used. Falcon deep research was re-attempted
(`just deep-research-falcon NEUCR NCU04637 --fallback perplexity-lite`) and failed again
(falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient quota). No provider
report exists; review is based on cached literature, UniProt and PANTHER.

Identity: Q7S3B9 is the full-length 467-aa product (sequence version 2; BAR 17-269,
disordered P/A-rich linker 281-400, SH3 407-467). Not a fragment, isoform or alternative model;
architecture matches yeast RVS167 (482 aa).

Phylogenetic placement: PTHR47174 has three N. crassa members: NCU04637 (SF1, Rvs167
subfamily, with S. cerevisiae RVS167 P39743, C. albicans RVS167 Q59LF3 and S. pombe hob1 O74352),
amph-1/NCU01069 (SF3, BIN3/Rvs161 subfamily) and NCU01883 (SF2). Closest characterised
relative by subfamily: S. cerevisiae RVS167 (P39743). Note that pombe Hob1 (same SF1) is
dispensable for endocytosis (InterPro IPR046982 text), a lineage-specific divergence.

New in-species evidence: PMID:22646057 (abstract only) - N. crassa rvs-161 and rvs-167 deletion
mutants show reduced endocytic PAF26 internalization [PMID:22646057 "Deletion mutants of the
endocytic proteins RVS-161, RVS-167 and RAB-5 exhibited reduced rates of PAF26 internalization and
fungicidal activity."]. NCU04637 is the only SF1 protein, so this RVS-167 is presumably NCU04637.
Also cached PMID:22082017 (yeast Rvs167 SH3 binds Vps1; heterodimer disassembles Vps1 oligomers).

Changes vs previous review:
- cytoplasm (IEA) ACCEPT -> MODIFY to actin cortical patch (GO:0030479 is a part_of descendant).
- actin cytoskeleton (IBA) ACCEPT -> MODIFY to actin cortical patch (is_a descendant).
- medial cortex (IBA) UNDECIDED -> MARK_AS_OVER_ANNOTATED: term defines a pombe nucleus-overlying
  band for contractile ring positioning; donors only pombe hob1/hob3; no counterpart in
  multinucleate hyphae.
- mating projection tip (IBA) UNDECIDED -> MARK_AS_OVER_ANNOTATED: defined for unicellular fungi.
- actin cortical patch localization (IEA) ACCEPT -> MARK_AS_OVER_ANNOTATED: evidence is a
  mutant patch-polarization phenotype (Candida), i.e. necessity, not participation.
- plasma membrane tubulation (IBA) ACCEPT -> KEEP_AS_NON_CORE (in vitro tubulation; in vivo role
  is invagination-neck stabilisation/scission).
- endocytosis, lipid binding (contributes_to), actin cortical patch, Rvs161p-Rvs167p complex: ACCEPT,
  now with Neurospora deletion evidence and amph-1 as the predicted heterodimer partner.
- Core function now uses contributes_to_molecular_function lipid binding, location actin cortical
  patch, in_complex GO:1990528. Description rewritten.

Modules: no fungal endocytosis module exists; modules/synaptic_vesicle_endocytosis.yaml mentions
amphiphysin but is a metazoan neuronal module, not applicable.
