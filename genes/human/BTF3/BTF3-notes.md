# BTF3 notes

- 2026-04-20: True human BTF3 for this review is UniProt `P20290`; UniProt
  `gene_exact:BTF3` queries also return `BTN3A3` and `BTN3A2` because `BTF3`
  is carried as a synonym on those entries, so accession pinning was required
  during fetch.

- BTF3/P20290 is the human NAC-beta subunit and the NAC heterodimer associates
  with ribosomes through BTF3. [file:human/BTF3/BTF3-uniprot.txt "Part of the
  nascent polypeptide-associated complex (NAC), which is a heterodimer of NACA
  and BTF3 (via NAC-A/B domains). NAC associates with ribosomes through the
  BTF3/NACB subunit."; PMID:21203952 Crystal structures of NAC domains of human
  nascent polypeptide-associated complex (NAC) and its alphaNAC subunit.,
  "Nascent polypeptide associated complex (NAC) and its two isolated subunits,
  αNAC and βNAC, play important roles in nascent peptide targeting."]

- UniProt summarizes that, when associated with NACA, BTF3 prevents
  inappropriate targeting of non-secretory polypeptides to the ER. The cached
  abstract for PMID:10982809 supports assigning this process to BTF3 directly:
  both subunits contribute to preventing inappropriate interactions, and
  betaNAC alone binds ribosomes and is sufficient to prevent ribosome binding
  to the ER membrane. [file:human/BTF3/BTF3-uniprot.txt "When associated with
  NACA, prevents inappropriate targeting of non-secretory polypeptides to the
  endoplasmic reticulum (ER). Binds to nascent polypeptide chains as they
  emerge from the ribosome and blocks their interaction with the signal
  recognition particle (SRP), which normally targets nascent secretory peptides
  to the ER."; PMID:10982809 The alpha and beta subunit of the nascent
  polypeptide-associated complex have distinct functions., "both subunits are
  in direct contact with nascent polypeptide chains on the ribosome and that
  both contribute to the prevention of inappropriate interactions. However,
  betaNAC alone directly binds to the ribosome and is sufficient to prevent
  ribosome binding to the endoplasmic reticulum membrane."]

- UniProt also reports BTF3 in both cytoplasm and nucleus, while noting that
  the heterodimer with NACA is cytoplasmic. In PN framing, that supports
  keeping the NAC-linked cytoplasmic role as core and the nuclear/transcription
  role as contextual. [file:human/BTF3/BTF3-uniprot.txt "SUBCELLULAR LOCATION:
  Cytoplasm {ECO:0000269|PubMed:10982809}. Nucleus
  {ECO:0000269|PubMed:10982809}. Note=The heterodimer with NACA is
  cytoplasmic."]

- The large-scale RNA interactome and protein-interactome papers support
  association calls but do not, from the accessible text here, define a
  specific core molecular function beyond NAC-linked nascent-chain handling.
  [PMID:22658674 Insights into RNA biology from an atlas of mammalian
  mRNA-binding proteins., "We identify 860 proteins that qualify as RBPs by
  biochemical and statistical criteria"; PMID:22681889 The mRNA-bound proteome
  and its global occupancy profile on protein-coding transcripts., "Application
  to a human embryonic kidney cell line identified close to 800 proteins";
  PMID:25416956 A proteome-scale map of the human interactome network.;
  PMID:33961781 Dual proteome-scale networks reveal cell-specific remodeling of
  the human interactome.]

- PMID:18433331 documents BTF3 interaction with HEPIS (Q86VG3), a SARS
  nsp10-binding repressor, which supports a context-specific physical
  association claim but not a core GO molecular function for human BTF3.
  [PMID:18433331 Identification of a novel transcriptional repressor (HEPIS)
  that interacts with nsp-10 of SARS coronavirus., "we co-immunoprecipitated
  HEPIS with BTF3, a component of the RNA pol II initiation complex"]

- PMID:30242148 supports a contextual transcription-related interaction for BTF3
  rather than the PN core role. The paper links BTF3 to Connexin-43-tail and
  Pol II in an N-cadherin transcriptional mechanism that is separate from
  conserved NAC-mediated nascent-chain sorting. [PMID:30242148 Gap junction
  protein Connexin-43 is a direct transcriptional regulator of N-cadherin in
  vivo., "we identify its mechanism of action, showing that Cx43 regulation of
  N-cadherin is due to a direct interaction with the basic transcription factor
  3 (BTF3)"]
