# ORC5 (human, O43913) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human ORC5 is reviewed as the experimentally characterised reference for
the horse ortholog (HORSE/ORC5, A0A3Q2KSP7; same PANTHER subfamily PTHR12705:SF0,
human ORC5 is a PAINT donor at PTN000295037). ProtNLM2 output was not consulted.

### Deep research

`just deep-research-falcon human ORC5 --fallback perplexity-lite` failed: the
Edison (falcon) API returned `403 Forbidden` at `/auth/login`, and the
perplexity-lite fallback also failed. No deep-research file exists. The review is
built from the cached publications (four with full text: PMID:31160578,
PMID:32808929, PMID:20932478, PMID:22398447; the rest abstract-only) and the
UniProt record.

### Evolutionary grounding

- UniProt: "Belongs to the ORC5 family"; InterPro ORC5 (IPR020796), ORC5_C,
  ORC5_lid, AAA_16 P-loop NTPase. PANTHER PTHR12705:SF0 (the family has a single
  subfamily, containing yeast Orc5, fly Orc5, fission yeast orc5 and human ORC5).
- PAINT node PTN000295037 propagates three terms: DNA replication origin binding
  (donor SGD Orc5 only), nuclear ORC and DNA replication initiation (donors include
  human ORC5 itself, fly, fission yeast and budding yeast). The target appearing in
  its own WITH/FROM is expected.

### Experimental evidence in human (what is established in this species)

- Complex membership: ORC5 co-precipitates with ORC2 and ORC4
  [PMID:9765232 "HsORC5p is precipitated from cell extracts with HsORC2p and HsORC4p,
  indicating that it is part of the putative human ORC"]; recombinant human ORC
  assembly requires ATP binding by ORC4 and ORC5
  [PMID:17716973 "Mutations in the ATP-binding sites of Orc4 or Orc5 impair complex
  assembly, whereas Orc1 ATP binding is not required."].
- Structure: cryoEM of human ORC1-5 places ATP sites at the ORC1·4, ORC4·5 and
  ORC5·3 interfaces; the ORC5 β-hairpin (H398) lies close to DNA
  [PMID:32808929 "The β-hairpin loop in ORC5 of HsORC also consists of a
  positively-charged residue H398 in close proximity to DNA"]. ORC4·5 and ORC5·3
  sites are not thought to hydrolyse ATP; ATP there is structural.
- Localisation: nuclear, largely in an insoluble (chromatin/matrix) fraction
  [PMID:9765232]; chromatin-bound ORC5 is the OBI1 substrate [PMID:31160578].
- Regulation: OBI1 multi-mono-ubiquitylates chromatin-bound ORC3 and ORC5 in
  S phase; lysine-less ORC3/5 still bind chromatin and support pre-RC formation but
  impair origin firing [PMID:31160578].
- Chromatin recruitment of ORC5 depends on ORCA/LRWD1 tethering [PMID:20932478]
  and on the ORC1 BAH–H4K20me2 interaction [PMID:22398447].
- Isoform 2 (ORC5T) binds ORC4 but not ORC2 [PMID:9765232].

### What is inferred rather than shown in human

- Direct, sequence-specific origin DNA binding by ORC5 alone is not shown; the DNA
  contact is structural within the ORC1-5 assembly, so origin binding is a complex
  property (contributes_to).
- MCM2-7 loading (pre-RC assembly) by human ORC is supported by the general ORC
  literature, but no cached paper tests the human ORC5 subunit in MCM loading
  specifically, so no NEW pre-RC assembly term was proposed.
- ORC5 is not an ATPase: the only demonstrated ORC ATPase site is ORC1·4.

### Decisions

- All bare GO:0005515 protein binding rows REMOVE (policy); the interactions are
  intra-ORC and with OBI1, captured by the complex term.
- GO:0000808 ORC → MODIFY to GO:0005664 nuclear ORC (is_a child, already carried).
- GO:0005694 chromosome → MODIFY to GO:0000785 chromatin (part_of child, carried).
- GO:0006260 DNA replication → MODIFY to GO:0006270 DNA replication initiation.
- GO:0000166 nucleotide binding → MODIFY to GO:0005524 ATP binding.
- GO:0000781 telomeric region (PICh HDA) and GO:0006275 regulation of DNA
  replication (OBI1 ubiquitylation) kept as non-core.
