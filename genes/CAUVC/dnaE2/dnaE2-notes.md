# dnaE2 (CC_3211, Q9A3J3) curation notes

- No provider deep research is available for this gene; no `-deep-research-*.md` file was
  generated in this session. The review rests on the cached primary papers and UniProt.
- dnaE2 disruption abolishes mitomycin C-induced mutagenesis and reduces UV mutagenesis;
  all three operon genes are required.
  [PMID:15886391, "The results show that the dnaE2 operon is upregulated in response to DNA damage in a recA-dependent manner, and demonstrate that all three genes that compose this expression unit are involved in UV and mitomycin C-induced mutagenesis."]
- The operon-dependent signature indicates a difference in nucleotide incorporation during
  TLS, i.e. the polymerase inserts opposite lesions.
  [PMID:15886391, "This novel mutational signature, dependent on the activity of the imuAB/dnaE2 operon, probably reflects a difference in polymerase preference for nucleotide incorporation during TLS."]
- DnaE2 is the catalytic member of the cassette: active-site substitution phenocopies
  deletion in the mycobacterial system.
  [PMID:20615954, "Point mutations in the DnaE2 active site eliminated induced mutagenesis and damage tolerance, reproducing the dnaE2 deletion phenotype."]
- Why GO:0006260 (DNA replication) is over-annotation: DnaE2 lacks the C-terminal
  clamp-loader-binding region of the replicative alpha subunit.
  [PMID:20615954, "All major DNA polymerase IIIα structural/functional domains ( 23 , 24 ) are readily identified in DnaE2, except for the very C-terminal region which in E. coli has been implicated in the interaction of α with the clamp-loader subunit, τ ( 28 , 29 )."]
- Why GO:0008408 (3'-5' exonuclease) is over-annotation: the PHP residues are absent in
  DnaE2 while DnaE1 retains them.
  [PMID:20615954, "The corresponding domain of Mtb DnaE1 retains all amino acids associated with exonuclease activity ( 34 – 36 ), whereas key residues are absent in DnaE2."]
  No DnaE2 exonuclease assay exists, so the row is marked over-annotated rather than removed.

## 2026-11-07 comparative consultation

The earlier replication rejection is corrected: official current QuickGO places GO:0042276 under GO:0006301 DNA damage tolerance, which is part_of GO:0006260 DNA replication. The path is not pure is_a. The source replication row is MODIFY to the already-proposed TLS term. DnaE2's distinction from essential chromosome-replicative DnaE does not make the ontology ancestor false. Likewise, the DNA-repair definition includes bypass; its TLS correction must not be justified by equating all repair with lesion excision.

The exonuclease row is now UNDECIDED. The 2010 primary's PHP-residue discussion concerns mycobacterial DnaE2; no residue-by-residue target correspondence was established in this consultation. The earlier global/target loss assertion and the claim that an error-prone phenotype excludes proofreading are superseded. Target catalytic-site analysis and biochemical assays could resolve this; no residue identity or negative assay is invented. Cytoplasm is ACCEPT because it is the inferred location of the core DNA activity, not a peripheral role solely because evidence is indirect.

Native NA1000 (CB15-derived) disruption, epistasis and rpoB spectra support mutagenic damage tolerance. The dnaE2 disruption is an insertion/truncation allele; it is not a purified-enzyme assay. Family/HAMAP classification and mycobacterial catalytic mutants support DNA polymerase activity, while insertion versus extension, lesion repertoire and fidelity remain target-specific gaps. The broad polymerase row now quotes the actual catalytic reaction instead of a bare Rhea identifier. Every original source payload and the historical NEW row are preserved.

A genuine Falcon request failed with HTTP403 authentication; no report was fabricated. Official GO definitions/ancestry, source-protection receipts and the complete action ledger are in the consultation audit directory. No family review or selector was changed. The newer 2026 polymerase survey (DOI:10.1093/nar/gkag133) was flagged to the module owner for family-boundary review, without using it to assert a target residue state here.


## 2026-11-07 PR6169 proofreading follow-up

Reassessed GO:0008408 as MARK_AS_OVER_ANNOTATED for the traced broad InterPro mapping, while explicitly retaining uncertainty about target nuclease activity. PMID:20615954 supplies a counterexample to uniform nuclease inference, not a target-specific residue-loss result. Specific DnaE2 evidence supports polymerase synthesis independently. The review does not equate error-prone behavior with absence of proofreading. See `analysis/module_audits/bacterial_imuabc_damage_induced_mutagenesis/round1-gene-consultation/RESULTS.md` and its captured InterPro/GO provenance. Original annotation payload and order remain unchanged; no new row is added.
