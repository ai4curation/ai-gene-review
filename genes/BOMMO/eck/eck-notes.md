# eck (BmEc22K, EcKinase; UniProt Q0PCR8; Bombyx mori) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the closest experimentally characterised relative of
DROME/CG31099 (PTHR11012:SF6). No ProtNLM2 output was consulted.

### Provenance / process

- `just fetch-gene BOMMO Q0PCR8 --alias eck` created the folder (UniProt gene
  name is `eck`; literature name BmEc22K / EcKinase).
- `just deep-research-falcon BOMMO Q0PCR8 --alias eck --fallback perplexity-lite`
  FAILED: falcon "Failed to authenticate"; perplexity fallback returned HTTP 401
  (insufficient quota). No deep-research file exists; review is based on the
  cached literature below, read directly.
- Cached: PMID:16899460 (abstract only; JBC/Elsevier full text returned 403),
  PMID:18828659, PMID:19456376, PMID:19524123 (abstracts),
  PMID:38291829 (full text), PMID:39208453 (abstract), PMID:32540344 (abstract).

### What is experimentally established in B. mori

- Enzyme activity. EcKinase was purified ~1,800-fold from ovary cytosol, the
  cDNA cloned from partial peptide sequence, and the ORF expressed to confirm it
  encodes the functional enzyme [PMID:16899460 "The cloned cDNA was confirmed to
  encode the functional EcKinase using the transformant harboring the open
  reading frame of EcKinase."]. Reaction: free ecdysteroid -> ecdysteroid
  22-phosphate (ATP-dependent) [PMID:19456376 "ecdysteroid 22-kinase (EcKinase)
  has been shown to catalyze the conversion of free ecdysteroids to
  physiologically inactive ecdysteroid 22-phosphates"]. Matches GO:0106389.
  Detailed substrate range/kinetics are in the full text, which I could not read.
- Location. Native activity is cytosolic in ovary [PMID:16899460 "purified from
  the cytosol of the silkworm Bombyx mori ovaries"]. EcKinase mRNA is in nurse
  cells and oocyte; immunoreactivity mainly in the external region of the oocyte
  [PMID:18828659 "EcKinase immunoreactivity localizes mainly in the external
  region of the oocyte, not in nurse cells or follicle cells"].
- Physiological role (biochemical/expression inference, no loss-of-function
  data): with ecdysteroid-phosphate phosphatase (EPPase) it forms a reversible
  phosphoconjugation cycle that stores ovarian ecdysteroids as inactive
  22-phosphates which are reactivated in the early embryo [PMID:16899460; PMID:19524123].
  No knockdown/knockout of eck has been reported in the literature I found, so
  roles in oogenesis/embryogenesis are not process annotations. The enzyme does
  catalyse an ecdysteroid metabolic step itself, so GO:0045455 ecdysteroid
  metabolic process passes the participation test (it is the catalyst, not the
  substrate). GO:0046344 ecdysteroid catabolic process is not appropriate: the
  22-phosphates are a reversible reservoir, not a breakdown product.

### Evolutionary placement (for transfer)

- PANTHER PTHR11012:SF54; Pfam EcKL (PF02958); SMART CHK domain 124-307;
  Brenner motif HADYRTCN 236-243 retained (eck-bioinformatics/RESULTS.md).
- Scanlan & Robin 2024 (PMID:38291829): EcKL family has >=13 subfamilies;
  BmEc22K is in subfamily A, Lepidoptera clade Lep1, and is the only Lep1 member
  in B. mori; AgEcK2 (Anopheles 20E 22-kinase) is in subfamily D. Lep1 clade size
  correlates with host-plant diversity, suggesting some Lep1 paralogs in other
  moths may have shifted to xenobiotic phosphorylation. Hence even within
  subfamily A, ecdysteroid 22-kinase activity should not be blanket-transferred.
- Drosophila orthologs of BmEc22K are Wallflower and Pinkman (subfamily A); null
  mutants are viable and fertile, and Wall misexpression argues it is not an
  ecdysteroid 26-kinase/20E inactivator [PMID:39208453]. So the 22-kinase
  function has not been confirmed for the fly orthologs.
- For DROME/CG31099 (PTHR11012:SF6): different PANTHER subfamily from eck (SF54)
  and no PAINT IBA nodes; the only safe transfer is generic EcKL/CHK small
  molecule kinase fold membership, not ecdysteroid 22-kinase activity.
