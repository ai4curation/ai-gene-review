# APP (horse, Equus caballus) — A0A3Q2IKB0

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: HORSE partner of the DONKEY40 cohort (donkey target A0A9L0JJJ9, reviewed separately in
`genes/EQUAS/APP/`). No ProtNLM2 files were opened; this review is independent of them.

### Setup

- Folder created with `just fetch-gene HORSE A0A3Q2IKB0 --alias APP`; stub id confirmed as A0A3Q2IKB0. 84 GOA rows, all
  electronic (9 IBA from PAINT, the rest IEA: Ensembl Compara, combined IEA, UniRule, ARBA, SubCell, InterPro2GO,
  GO_REF:0000108).
- Deep research FAILED: `just deep-research-falcon HORSE APP --fallback perplexity-lite` gave "Failed to authenticate"
  for falcon and HTTP 401 (insufficient quota) for perplexity-lite. No deep-research file exists. The review uses the
  curated human Swiss-Prot record (`genes/human/APP/APP-uniprot.txt`), the complete human and mouse reviews, cached
  publications (PMID:25122912, PMID:19726636, PMID:9390996) and my own analyses.

### Identity and gene model (key finding)

Analyses in `APP-bioinformatics/RESULTS.md` (align.py, compare_horse_models.py, fetch_experimental_goa.py).

- A0A3Q2IKB0 (768 aa) is the protein of ENSECAT00000045461, which Ensembl flags as the canonical transcript of horse
  APP (ENSECAG00000021011). No reviewed horse APP entry exists; this is the gene-centric UniProt entry.
- Against human APP770 (P05067): 95.3% identity over 746 aligned pairs. E1 157/162 identical (copper ligands
  His147/His151/Tyr168 kept), Kunitz domain 51/51, E2 192/192, amyloid-beta 1-42 42/42 (human-type peptide), TM
  region identical.
- The 19-residue OX-2 exon (human 345-363) is missing, so the ectodomain is APP751-like (KPI+, OX-2-).
- The cytoplasmic tail diverges completely after human Glu738: human `VDAAVTPEERHLSKMQQNGYENPTYKFFEQMQN` is replaced
  by an unrelated `LCRRSHYTKHPGKQTRLFEMVILLPAHPPEISLFQAVTAVALKPKRRPTK`. The model lacks the Thr743 (APP695 Thr668)
  site, the YENPTY motif and the AICD C-terminus.
- Four other horse APP entries from the same gene (F6XKR3 751 aa, A0A3Q2HIF9 752, A0A5F5PX07 695, A0A5F5PMR9 714) end
  in the conserved APP C-terminus with YENPTY; the donkey model does too. The A0A3Q2IKB0 tail is therefore most likely
  a gene-model artefact (aberrant terminal exon), which Ensembl's choice of canonical transcript has carried into
  UniProt. I did not check transcript support directly.
- So this is an alternative gene model of the canonical gene, not a fragment: full ectodomain, wrong tail.

### Phylogeny

- UniProt places it in PANTHER PTHR23103:SF7 (AMYLOID-BETA PRECURSOR PROTEIN), the vertebrate APP ortholog subfamily.
  This agrees with `interpro/panther/PTHR23103/PTHR23103-review.yaml` (SF7 = clade node PTN002749606). No placement
  disagreement.
- IBA rows: from PTN002749606 (APP orthologs) come plasma membrane, cell surface, early endosome, Golgi, membrane raft,
  signaling receptor binding and signaling receptor activator activity. From PTN000559854 (APP family) come
  axonogenesis and CNS development. PAINT did not propagate heparin binding, PTB domain binding, identical protein
  binding, amyloid-beta-related processes or synaptic plasticity terms. Those horse rows come only from Compara/IEA.

### Decisions

- Accepted the core ectodomain functions: signaling receptor activator activity, signaling receptor binding,
  serine-type endopeptidase inhibitor activity (KPI exon present), heparin binding, identical protein binding
  (dimerization), axonogenesis, synapse organization, plus trafficking compartments.
- Transition metal ion binding: MODIFY to copper ion binding (plus zinc ion binding), since the GFLD/CuBD copper site
  is conserved.
- Tail-dependent claims, judged against the defective model:
  - PTB domain binding: MARK_AS_OVER_ANNOTATED. Needs YENPTY, which is absent.
  - Nucleus: MARK_AS_OVER_ANNOTATED. The AICD reaches the nucleus by FE65 binding.
  - Positive regulation of transcription by RNA polymerase II: MARK_AS_OVER_ANNOTATED. This is the AICD-FE65-KAT5
    pathway.
  - Clathrin-coated pit: KEEP_AS_NON_CORE. Internalization uses YENPxY.
  - Protein serine/threonine kinase binding: KEEP_AS_NON_CORE.
  - Regulation of presynapse assembly: KEEP_AS_NON_CORE. PMID:19726636 needed the intracellular domain.

  In every case the claim stays true of the horse APP gene through its other transcripts.
- Learning, and learning or memory: MARK_AS_OVER_ANNOTATED. They are behavioural readouts of transgenic models, not
  process participation. This is stricter than the human review, which keeps them as non-core.
- Amyloid-beta-driven glial, cytokine, kinase-cascade and plasticity terms: KEEP_AS_NON_CORE. The peptide is identical
  to human and the effects are real, but they are pathological fragment effects.
- ARBA uninformative terms (molecular function activator activity, regulation of protein metabolic process):
  MARK_AS_OVER_ANNOTATED. Membrane, endomembrane system and neuron projection: TOO_GENERAL.
- Core functions leave out PTB domain binding on purpose, because this sequence cannot do it.

### Relative

Human APP (P05067) is the ortholog in the same PANTHER subfamily SF7 / PAINT node PTN002749606. It has a complete
review at `genes/human/APP/APP-ai-review.yaml`. Mouse App (P12023) also has a complete review. The canonical-product
rule does not apply: A0A3Q2IKB0 is itself the gene-centric canonical entry, and no reviewed horse entry exists.
Among the horse models, F6XKR3 would be the best-formed product (APP751 with the conserved tail).

### Modules

No module in `modules/` includes APP. The gamma-secretase and Notch modules mention secretase substrates in general
terms only.
