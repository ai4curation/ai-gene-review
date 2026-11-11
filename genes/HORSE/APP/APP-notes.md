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

## 2026-10-23 — PR #5309 review follow-up

The review cited `APP-bioinformatics/ortholog_experimental_goa.txt` (a QuickGO listing of human, mouse and
rat APP experimental GO annotations) as supporting_text in 73 annotation rows. A GO annotation listing
records what is annotated, not why it is true, so citing it is citing annotations as evidence for
themselves. Following the treatment already applied to genes/EQUAS/APP, every such citation was removed:

- 27 rows already had other support (human UniProt curated text, the alignment output, PANTHER family
  review, primary papers). The listing quote was dropped, and where the donkey review quotes the donor
  paper for the same term, that verbatim quote was added.
- 46 rows had the listing as their only support. 44 were re-supported with the donor-publication,
  human UniProt or PANTHER family-review quotes used for the same GO term in genes/EQUAS/APP (all verbatim
  and validated there).
- GO:0043204 perikaryon: donor paper PMID:10341243 was cached (full text) and quoted ("APP was detected
  mostly in the cell body and in growth cones"), with the human UniProt line tying Perikaryon to it.
- GO:0005641 nuclear envelope lumen: the only donor (PMID:21989385) is abstract-only in the cache and its
  abstract does not mention the compartment; the human UniProt record has no curated nuclear-envelope
  location. With no independent support the row is now UNDECIDED (was KEEP_AS_NON_CORE).

The listing stays in references with relevance LOW, as provenance for identifying donor papers only.

## 2026-10-23 — PR #5309 second review: quotes that did not support their terms

The reviewer found that many quotes used to replace the ortholog GOA listing were verbatim but did not
state the term they supported. Validation only checks that a quote is a substring of its source, so it
cannot catch this. Every quote added in that pass was re-read against one question: does this sentence
state this term, for this gene product, at this specificity?

**Wrong-gene donor (GO:0008285).** The only donor is a human IDA assigned by UniProt
(P05067, PMID:22944668, 2017-04-25). That paper is about the antimicrobial activity of human islet amyloid
polypeptide (IAPP, amylin) ["Human islet amyloid polypeptide (hIAPP) shows an antimicrobial activity
towards two types of clinically relevant bacteria."]. Its cached abstract never mentions APP or
amyloid-beta and contains no proliferation assay. The row is now UNDECIDED, with a PROBABLE
`WRONG_GENE_PRODUCT` source defect on the upstream UniProt row (requested change CHECK; candidate correct
product IAPP, UniProtKB:P10997, verified by UniProt REST). `genes/human/APP` still ACCEPTs this IDA; that
file is outside this PR and should get the same treatment.

**Re-supported with a quote that states the claim.** Where possible these use the donor paper or a
curated human UniProt line tied to a PubMed id:
- signaling receptor binding: Abeta42 interacts with FPR2 (UniProt), and CD74 interacts with APP while
  "it also serves as a receptor for macrophage migration inhibitory factor" (PMID:19849849, the IPI
  donor, cached in full). These replace "Functions as a cell surface receptor", which states the inverse
  relation, and "Correctly scoped to the APP subfamily.", which states nothing about function.
- early endosome and early endosome membrane: "Early endosome {ECO:0000269|PubMed:20580937}" plus
  "Single-pass type I membrane protein". A type I membrane protein in early endosomes is in their
  membrane; the reason says so. This replaces "colocalize in endosomal and Golgi compartments".
- enzyme binding: direct PSEN1 binding (PMID:30630874) and IDE binding (PMID:17051221) from UniProt,
  replacing the ADAM19 sAPPalpha quote, which reports a processing outcome rather than binding.
- protein serine/threonine kinase binding: LRRK2 binding (PMID:28720718), replacing ROCK2
  phosphorylation of APP.
- membrane raft: "Also binds GPC1 in lipid rafts." (UniProt), replacing a PANTHER scope sentence.
- perinuclear region: the full SORL1 sentence ending "...cytoplasm and perinuclear regions". The
  earlier quote had been cut off before "perinuclear".
- neuron projection: "Cell projection, growth cone {ECO:0000269|PubMed:10341243}."
- positive regulation of synaptic transmission, cholinergic: "oAβ42 activates both homomeric α7- and
  heteromeric α7β2-nAChR subtypes" (PMID:33239400, the donor), added beside the CHRNA7 binding line.
- positive regulation of inflammatory response: Aβ "stimulates the nuclear transcription factor κB
  (NF-κB) signaling, leading to the secretion of inflammatory cytokines" (PMID:29961672, the donor,
  full text).
- positive regulation of ERK1/2 cascade: "chronic activation of the ERK MAPK cascade ... via α7
  nAChRs" (PMID:11404397, full text), replacing a sentence about the generic MAPK cascade.
- amyloid fibril formation: an oligomer that "can form and coexist in parallel with the well-known
  cross-β-sheet fibrils" (PMID:26138908).
- microglial cell activation: the full TLR2 sentence, which names "cultured microglia and macrophages".

**UNDECIDED: the donor text does not state the term.** All of these donors are cached abstract-only,
except PMID:23382219, which is cached in full. The abstracts were read in full, and none mentions the
term's specific entity:
- astrocyte activation and astrocyte activation involved in immune response (PMID:15457210,
  PMID:23152628). The UniProt "mononuclear phagocytes" line is about a different cell type.
- positive and negative regulation of gene expression (PMID:22198949). One TLR2 sentence supported both
  directions while naming no gene.
- positive regulation of chemokine, IL-1β and IL-6 production (PMID:22406537), and of TNF production
  (PMID:22198949). No cytokine is named in either abstract.
- dendritic spine and dendritic shaft (PMID:11988176). The abstract is about ASIC and does not mention
  APP. The 23931995 sentence ("dendritic APP/BACE-1-containing vesicles") still supports dendrite, but
  it cannot tell spines from shafts. This donor may also be mis-keyed, but no source defect was filed
  because the full text was not read.
- signaling receptor complex (PMID:23382219, full text). That paper is a PX-FERM cargo-recognition
  study in which APP appears only as a previously identified SNX17 cargo. It is a possible source defect
  but was not filed.
- positive regulation of the JNK cascade (PMID:23921129). JNK is never mentioned.
- modulation of EPSP (PMID:20974225), regulation of spontaneous synaptic transmission (PMID:15457210)
  and positive regulation of non-canonical NF-κB signalling (PMID:15457210). None of these is measured
  or mentioned.
- cellular response to amyloid-beta (PMID:29518356). In that paper the responding entity is microglia
  expressing TREM2.
- positive regulation of amyloid fibril formation (PMID:19660551). The paper characterises Abeta
  assemblies in J20 mice but does not test regulation.

**Kept as they were, after the check:**
- dendrite: PMID:23931995 places APP vesicles in dendrites.
- Golgi-associated vesicle, growth cone, synapse, axonogenesis, signaling receptor activator activity,
  regulation of presynapse assembly and synapse organization: the reviewer verified these.
- learning and learning or memory: these are MARK_AS_OVER_ANNOTATED, and their quotes support the
  phenotype-not-participation reason.
- negative regulation of LTP and regulation of long-term neuronal synaptic plasticity:
  "Aβ-induced inhibition of long-term potentiation" supports both.
- calcium-mediated signalling (Abeta raises cytosolic Ca2+), amyloid-beta complex (oligomeric states),
  receptor ligand activity (direct TLR2–Aβ42 interaction) and glycolysis.
- positive regulation of protein metabolic process: this is MARK_AS_OVER_ANNOTATED, and its quote
  shows the indirect MAPK coupling that the reason describes.

**Out of scope.** `genes/EQUAS/APP/APP-protnlm-predictions-review.yaml` (and
`genes/EQUAS/HOXA2/HOXA2-protnlm-predictions-review.yaml`) still quote the ortholog GOA listing. There it
backs an LSP verdict about annotation state, not a biological claim. Whether to change that is a separate
decision, and those files were left untouched.

Row tally for this file (HORSE/APP): 13 re-supported, 18 set to UNDECIDED, and 4 moved from KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED. The 4 are microglia development, positive regulation of LTP, neuron projection maintenance and positive regulation of T cell migration. Each uses the reasoning already in EQUAS/APP, which its existing quote does support.
