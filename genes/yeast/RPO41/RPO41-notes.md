# RPO41 (P13433, YFL036W) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: RPO41 is reviewed as the experimentally characterised reference for the
ProtNLM2 benchmark gene SCHPO/rpo41 (O13993). No ProtNLM2 output was consulted.

### Process log

- `just fetch-gene yeast RPO41 --uniprot-id P13433` created the UniProt, GOA and stub
  files (26 GOA rows).
- `just deep-research-falcon yeast RPO41 --fallback perplexity-lite` FAILED: falcon
  "Exception: Failed to authenticate"; perplexity-lite fallback returned HTTP 401
  insufficient_quota. No deep-research file exists; review is based on cached
  literature read directly.
- Additional papers cached with `just fetch-pmid`: PMID:10393945, PMID:33278362,
  PMID:27311715, PMID:15342628, PMID:25654332, PMID:7651397, PMID:3308116
  (PubMed esearch used to find ids; titles verified by esummary).

### Evolutionary grounding

- UniProt: "Belongs to the phage and mitochondrial RNA polymerase family"; PANTHER
  PTHR10102:SF0 (DNA-DIRECTED RNA POLYMERASE, MITOCHONDRIAL), the same subfamily as
  S. pombe rpo41 (O13993) and human POLRMT (O00411)
  (`interpro/panther/PTHR10102/PTHR10102-entries.csv`).
- IBA donors: SGD:S000001858 (this gene) is a donor to PTN000010146 (polymerase
  activity, mitochondrial transcription, mtRNAP complex). The promoter-binding IBA
  (GO:0001018) is placed at a different node, PTN000010147, whose only donor is
  PomBase rpo41; S. cerevisiae is a recipient there. Own-gene donor presence in
  WITH/FROM is expected, not circular.
- Active-site residues 945, 1014, 1189 are annotated by similarity (ECO:0000250).

### Experimental findings in S. cerevisiae

- Sequence: 1351 aa ORF, homologous to T3/T7 RNA polymerases
  [PMID:3308116 "the mitochondrial enzyme is highly homologous to the DNA-directed
  RNA polymerases of bacteriophages T3 and T7"].
- 145 kDa subunit of the purified mitochondrial RNA polymerase; gene isolated by
  immunoscreening [PMID:2426263]. Disruption shows the product is "required for
  transcription and maintenance of the mitochondrial genome" [PMID:3517858].
- Holoenzyme: "a catalytic core (Rpo41p), which resembles the enzymes from
  bacteriophage T7 and T3, and a specificity factor required for promoter
  recognition (Mtf1p)"; Rpo41p and Mtf1p form a holoenzyme before DNA binding; Mtf1p
  released after ~13-nt transcript [PMID:7929382].
- Intrinsic promoter recognition: "the yeast core mitochondrial RNA polymerase
  (Rpo41) has the intrinsic ability to initiate from promoters without its
  specificity factor (Mtf1). Rpo41 requires the mitochondrial promoter sequence
  (ATATAAGTA) for this activity" (supercoiled/premelted templates) [PMID:15342628].
  On duplex DNA, "Rpo41 by itself does not discriminate between promoter and
  non-promoter DNA"; Mtf1-dependent bending drives promoter selection [PMID:21911502].
  So sequence-specific promoter recognition is genuinely an Rpo41 property, but on
  closed duplex promoters it is realised only in the Rpo41-Mtf1 holoenzyme.
  (Aside: the SCHPO/rpo41 review description says S. pombe Rpo41 differs from its
  budding-yeast ortholog in initiating on its own; PMID:15342628 shows S. cerevisiae
  Rpo41 can also do so on supercoiled/premelted templates. Not edited here; flag for
  that gene's curator.)
- Structure: cryo-EM of initiation intermediates (PmIC, IC) of yeast mtRNAP with MTF1
  [PMID:33278362]. Thumb subdomain mutants: processivity, fidelity, Mtf1 binding
  [PMID:25654332].
- Priming: Rpo41 transcripts can be extended by Mip1; primes at origins and promoters
  in vitro [PMID:26184436]; Rpo41-Mtf1 is an efficient primase on Rim1-coated ssDNA
  [PMID:27311715]. In vivo relevance contested: deleting RPO41 did not abolish biased
  inheritance of HS rho- genomes, "priming by transcription is not a universal
  mechanism for mtDNA replication initiation" [PMID:7651397].
- N-terminal extension: required for a mtDNA maintenance function "separable from
  the known RNA polymerization activity of the enzyme" [PMID:10393945]. Mechanism
  unknown (domain itself vs interacting factors). GO:0000002 mitochondrial genome
  maintenance is obsolete, and this is necessity evidence, so no NEW annotation.
- Nucleoid: identified among mtDNA-associated proteins [PMID:15692048].

### Decisions summary

- Accept all polymerase activity, mitochondrial transcription and mtRNAP complex rows.
- Accept GO:0001018 IBA (supported by intrinsic promoter recognition PMID:15342628);
  DNA binding IEA -> MODIFY to GO:0001018.
- GO:0034062 (parent of GO:0003899) -> MODIFY to GO:0003899; DNA-templated
  transcription -> MODIFY to mitochondrial transcription.
- mitochondrion rows (HDA/IEA/NAS) -> MODIFY to mitochondrial matrix (IDA on this gene).
  cytoplasm HDA (GFP screen) -> MODIFY to mitochondrial matrix as well.
- Primer synthesis (GO:0006269 IDA, in vitro) -> KEEP_AS_NON_CORE.
- For transfer to S. pombe rpo41: polymerase activity, holoenzyme membership with
  Mtf1, mitochondrial transcription, matrix/nucleoid localization are experimental
  here. The priming role and the N-terminal mtDNA-maintenance function are
  S. cerevisiae-specific observations whose transfer is not established (the
  N-terminal extension is poorly conserved and PAINT does not propagate either).
