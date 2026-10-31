# GEMIN7 (human, Q9H840) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human GEMIN7 is the experimentally characterised reference for the horse
GEMIN7 benchmark gene (A0A9L0T0I7). This review was written without consulting any
ProtNLM2 output.

### Deep research

`just deep-research-falcon human GEMIN7 --fallback perplexity-lite` failed: the
Edison (falcon) API returned `403 Forbidden` at `/auth/login`, and the
perplexity-lite fallback also exited non-zero. No deep-research file was produced.
The review below rests on the cached publications (GOA-cited papers plus
PMID:33754639 and PMID:16314521) and the UniProt record.

### Evolutionary grounding

- PANTHER: PTHR14679 (GEM-ASSOCIATED PROTEIN 7) has a single subfamily,
  PTHR14679:SF1; human Q9H840, mouse Q9CWY4, bovine Q17QA0 and fission yeast
  G2TRR1 (gem7) are all SF1 members (`interpro/panther/PTHR14679/PTHR14679-entries.csv`).
- PAINT node PANTHER:PTN001027441 propagates only two terms to human GEMIN7:
  GO:0000387 spliceosomal snRNP assembly and GO:0120114 Sm-like protein family
  complex, with donors PomBase:SPBC32F12.16 and UniProtKB:Q9H840 itself. The
  curators did NOT propagate GO:0032797 SMN complex or GO:0034719 SMN-Sm protein
  complex, although human GEMIN7 carries both by IDA. The node spans fission yeast,
  whose SMN complex has only SMN, Gemin2, 6, 7 and 8 (no Gemin3/4/5)
  [PMID:33754639 "consisting of SMN, Gemin2, 6, 7, 8 and Sm proteins"], so the
  broader complex term is a defensible deliberate choice at that depth. For
  transfer to horse, only the IBA-level claims (snRNP assembly, Sm-like protein
  family complex) are phylogenetically sanctioned; the human-specific complex
  terms are grounded in human IDA data.
- The Gemin6-Gemin7-Gemin8 interface is conserved from fission yeast to human
  [PMID:33754639 "Our results thus demonstrate a conserved modular architecture of
  the SpG6/SpG7/SpG8 sub-complex."].

### Experimentally established in human (directly on GEMIN7)

- Component of the SMN complex; co-IP and colocalisation with SMN in cytoplasm and
  gems [PMID:12065586 "Coimmunoprecipitation and immunolocalization experiments
  demonstrate that Gemin7 is a component of the SMN complex and colocalizes with SMN
  in the cytoplasm and in gems."].
- Direct binding to Gemin6 (and SMN) and bridging of Gemin6 into the complex
  [PMID:12065586 "Binding experiments show that Gemin7 interacts directly with SMN
  and Gemin6 and mediates the association of Gemin6 with the SMN complex."].
- Sm-fold heterodimer with Gemin6 (crystal structure, PDB 1Y96)
  [PMID:15939020 "Gemin6 and Gemin7 exist as a heterodimer, and interact with each
  other via an interface similar to that which mediates interactions among the Sm
  proteins."].
- Binding to Sm proteins, especially SmE [PMID:12065586 "Gemin7 interacts with
  several Sm proteins of spliceosomal small nuclear ribonucleoproteins, in
  particular, with SmE."].
- Central position in the complex with SMN and Gemin8 [PMID:17178713 "Our studies
  reveal a modular composition of the SMN complex with the three proteins SMN,
  Gemin8, and Gemin7 in its center."]; Gemin8 recruits the Gemin6/7 heterodimer
  to SMN (PDB 7BBL) [PMID:33754639 "The C-terminus of HsSMN, termed the YG-domain,
  establishes the connection to HsG8, which in turn recruits the HsG6/HsG7
  heterodimer."].
- Direct interaction with unrip/STRAP [PMID:15848170].
- Nuclear pool with SMN upon translation inhibition [PMID:20513430 "SMN, Gemins 2,
  6, 7 and 8 accumulated in the nucleus, whereas Gemins 3, 4, 5 and unrip remained
  in the cytoplasm"].

### Not established

- No direct RNA binding by GEMIN7 has been demonstrated; the RNA binding IEA comes
  from the generic Sm-domain InterPro signature (IPR047575). The Sm fold is used for
  protein-protein (Sm-like) interactions here.
- No catalytic activity. The assembly "catalysis" is a property of the whole SMN
  complex [PMID:18984161].
- GEMIN7 does not act in the spliceosome; its link to mRNA splicing is indirect,
  via snRNP biogenesis.

### Decisions

- Protein binding IPI rows: GEMIN6 partner rows MODIFY to GO:0046982 protein
  heterodimerization activity (crystal-structure-established heterodimer); other
  partners REMOVE as uninformative (the interactions are real and are captured by
  SMN complex / SMN-Sm protein complex membership).
- Sm-like protein family complex IBA: TOO_GENERAL (entailed by accepted SMN
  complex), not a challenge to the PAINT node.
- cytoplasm -> cytosol; nuclear body -> Gemini of Cajal bodies (MODIFY).
- mRNA splicing, via spliceosome TAS: MARK_AS_OVER_ANNOTATED (indirect).
- RNA binding IEA: MARK_AS_OVER_ANNOTATED.
