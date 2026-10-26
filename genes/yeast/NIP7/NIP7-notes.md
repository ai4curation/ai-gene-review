# NIP7 (yeast, Q08962, YPL211W) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: this is a full review of budding-yeast Nip7 in its own right. It is the closest
experimentally characterised relative of fission-yeast nip7 (Q1MTQ9); both sit in PANTHER
PTHR23415:SF4, and yeast NIP7 (SGD:S000006132) is a PAINT donor at the eukaryote-level node
PTN000602113. ProtNLM2 predictions were not opened or used.

### Deep research

`just deep-research-falcon yeast NIP7 --fallback perplexity-lite` failed: falcon returned
"Failed to authenticate" and the perplexity fallback returned HTTP 401 (insufficient quota).
No deep-research file exists. The review is based on the cached publications listed below
and the UniProt record.

### Evidence, by species

Experimental in S. cerevisiae:

- Essential gene; ts allele nip7-1 gives halfmer polysomes, reduced 60S subunits, and
  delayed 27S pre-rRNA processing with reduced 25S rRNA
  [PMID:9271378 "Delayed processing of 27S pre-rRNA appeared to be the cause of reduced synthesis of 25S rRNA relative to 18S rRNA"].
- Cosediments with free 60S subunits, not 80S/polysomes, so it is a non-ribosomal factor
  [PMID:9271378 "A fraction of Nip7p cosedimented through sucrose gradients with free 60S ribosomal subunits but not with 80S monosomes or polysomal ribosomes, indicating that it is not a ribosomal protein"].
- Localisation: immunofluorescence throughout cytoplasm and nucleus; GFP fusion mostly nuclear,
  "most probably in the nucleolus" [PMID:9271378]; GFP-Nip7p nucleolar [PMID:9891085
  "both green fluorescent protein (GFP)-Nop8p and GFP-Nip7p localized to nucleoli"].
- Two-hybrid and co-purification partners Nop8 and the exosome subunit Rrp43 [PMID:9891085].
  These are the basis of all six GO:0005515 rows (PMID:25888478 used them only as two-hybrid
  positive controls).
- RNA binding: yeast and Pyrococcus Nip7 bind polyuridine in vitro, via the C-terminal PUA
  domain; yeast IVAF(161-164)AVAA reduces binding [PMID:18001138]. In vitro only, homopolymer
  substrate, so I do not propose poly(U) RNA binding (GO:0008266) as a biological activity.
- Nip7 forms a subcomplex with the rRNA m5C methyltransferase Nop2; Nop2 and Nip7 are
  interdependent for entry into pre-60S particles and are needed for stable association of at
  least six other "B-factors" (Rpf2, Tif6, Rlp24, Nog1, Nsa2, Nog2) that drive 27SB pre-rRNA
  (C2 site) processing [PMID:22735702 "We conclude that Nop2 and Nip7 form a subcomplex and that both are important for association of at least six other B-factors, as well as each other, with nascent ribosomes"].
  This is the best evidence that Nip7 does structural work in pre-60S assembly (a recruitment
  scaffold), rather than only being required for it.
- High-throughput presence in pre-60S particles (PMID:11583614, PMID:17443350, PMID:23212245).

Inferred, not established in yeast:

- Any catalytic activity. None is known; the PUA domain is an RNA-binding module, and Nip7 has
  no pseudouridine synthase or transglycosylase catalytic domain.
- The specific RNA site bound in vivo. Pre-60S cryo-EM structures exist (UniProt lists PDB
  6ELZ, 7NAC, 8V83 etc.), but I did not cache the corresponding papers, so I make no residue-
  or helix-level claim.

### Evolutionary grounding

- PANTHER PTHR23415 is a mixed family (CKS kinase regulatory subunits plus NIP7); only the
  NIP7 subfamilies are relevant. Yeast NIP7 and pombe nip7 share PTHR23415:SF4. Human NIP7
  (Q9Y221) is in SF34; its knockdown phenotype is reported (per the campaign brief; I did not
  re-read the human papers here) as ITS1/18S-related rather than 27S/60S, so yeast-specific process detail (27SB/C2 processing, Nop2 subcomplex hierarchy)
  should not be transferred to the human protein without its own evidence.
- PAINT node PTN000602113 (taxon:2759) IBDs: nucleolus (seeded by Q389E3, Q9Y221),
  preribosome LSU precursor (seeded by SGD:S000006132 = yeast NIP7), and ribosomal large
  subunit biogenesis (seeded by yeast NIP7 and pombe nip7). PAINT did NOT propagate yeast's
  more specific terms (GO:0000463 maturation of LSU-rRNA from tricistronic transcript;
  GO:1902626 assembly of LSU precursor of preribosome), nor nucleus/cytoplasm. I treat that as
  a deliberate decision to state the eukaryote-wide claim at the LSU-biogenesis level, which
  fits the human phenotype difference. For yeast itself, the specific terms are directly
  supported by yeast experiments.

### Decisions summary

- ACCEPT: LSU precursor (all 4 rows), nucleolus (3), GO:1902626 (2), GO:0000463 IMP,
  RNA binding IEA.
- MODIFY: ND molecular_function -> RNA binding; nucleus (3 rows) -> nucleolus;
  ribosome assembly IEA and LSU biogenesis (IBA, IMP) -> GO:1902626 / GO:0000463.
- KEEP_AS_NON_CORE: cytoplasm (IDA, IEA): a diffuse immunofluorescence signal, likely a free
  pool; the functional pool is nucleolar.
- REMOVE: six GO:0005515 protein binding rows (uninformative; the Nop8/Rrp43 interactions are
  real and are described in the review text).
