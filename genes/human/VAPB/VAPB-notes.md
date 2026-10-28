# VAPB (human, O95292) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was opened or used. This review was made in its own right, and its
experimental findings will later serve as the reference for transfer to VAPA-family genes.

### Provenance and limits
- `just fetch-gene human VAPB` seeded 130 GOA rows; `just fetch-gene-pmids` cached all 37 PMIDs.
- Deep research failed. Falcon gave "Exception: Failed to authenticate", and the perplexity-lite
  fallback gave HTTP 401 insufficient_quota. No deep-research file exists. The review uses the
  cached literature and the UniProt record only.
- Extra papers were cached and cited: PMID:24893131 (Stoica 2014, VAPB-PTPIP51 ER-mitochondria
  tether) and PMID:19515777 (VAP-C isoform negatively regulates HCV). PMID:16895911 (CERT FFAT)
  was already cached. It was consulted but not cited.

### Evolutionary grounding
- PANTHER PTHR10809:SF12 (VAPB_C). Paralog VAPA is the sister subfamily SF155. Mouse/rat Vapb are the
  one-to-one SF12 orthologs, so the ISS rows from mouse Vapb (PITPNM1, ER-PM contacts) and the Ensembl
  Compara synapse rows sit inside the same subfamily.
- All IBA rows come from the family root node PTN000087323: ER membrane, plasma membrane,
  protein-membrane adaptor activity and ER membrane organization. PAINT gave VAPA (SF155) the
  term "neuron projection development" but did not give it to VAPB. That omission is treated as
  deliberate, and the term is not added.
- Experimental support for FFAT motif binding comes from VAPB itself. Human VAPB MSP domain plus FFAT
  and phospho-FFAT peptides, with K43L mutagenesis [PMID:33124732 "Similarly to VAP‐A K50L, VAP‐B K43L
  interacted with the conventional FFAT of ORP1, but not with the Phospho‐FFAT of STARD3, while
  wild‐type VAP‐B interacted equally with the two types of FFAT motifs."].
- What is shown experimentally for human VAPB and what is inferred:
  - Experimental: ER membrane; FFAT/phospho-FFAT binding; binding of STARD3, WDR44, PTPIP51 and
    protrudin; ER-mitochondria tethering and MAM enrichment [PMID:24893131, PMID:22131369];
    recruitment to ER-endosome contacts [PMID:33124732]; HCV replication host factor
    [PMID:16227268]; UPR/IRE1 potentiation (overexpression only).
  - Inferred: ER-PM contact sites through PITPNM1 (ISS from mouse); sterol transfer, where the
    in vitro reconstitution used VAP-A only [PMID:33124732].

### Key decisions
- Protein binding (75 rows). 9 rows were changed to GO:0033149 FFAT motif binding, where the partner
  binds through an FFAT or phospho-FFAT motif (ZFYVE27 x2, RMDN3, STARD3, OSBPL1A, VPS13A, WDR44, and the
  33124732 multi-partner row). 1 row was changed to protein heterodimerization (VAPA). 1 row was changed
  to ephrin receptor binding (EphA4, secreted MSP domain). The rest were removed as screen-only or
  uninformative.
- Lipid transfer, cholesterol transport and Ca2+ homeostasis are kept as non-core. VAPB is the
  scaffold (tether), and the recruited ORP/STARD3/PTPIP51 partners do the transfer work.
  PI(4,5)P2 metabolic process (ISS) is marked over-annotated, because VAPB does not do any step of
  that process.
- COPII vesicle budding is marked over-annotated. The same study states that VAPB, unlike VAPA,
  did not inhibit ER export. Plasma membrane (IBA) is marked over-annotated: VAPB acts from
  cortical ER, and the contact-site row captures that.
- Viral release (ARBA IEA) is removed. Host-mediated suppression of viral genome replication is kept
  as non-core, because the VAP-C isoform inhibits HCV replication [PMID:19515777].
- NEW annotations:
  - GO:0140474 mitochondrion-ER membrane tether activity. VAPB does the binding work of the tether.
  - GO:0170016 ER-endosome tether activity.
  - GO:0140284 ER-endosome contact site.
  - GO:0044233 MAM contact site.
