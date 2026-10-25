# RAB8A curation notes

## 2026-10-03 — initial review (primary cilium life cycle module, stage 2 ciliary vesicle/membrane)

Human RAB8A = UniProt P61006. 138 GOA annotations seeded; all reviewed. Pleiotropic Rab GTPase: ciliary and
non-ciliary trafficking roles were separated.

### Deep research status

First falcon run (600 s timeout; perplexity fallback unavailable) did not complete; re-run with `--timeout 2400`
(outcome at end of file). Review based on cached primary literature.

### Biology

Ciliary:
- [PMID:17646400 "is the sole Rab enriched at primary cilia"; "Rab8a specifically interacts with cenexin/ODF2, a basal
  body and microtubule binding protein required for cilium biogenesis"].
- [PMID:17574030 "Rab8(GTP) enters the primary cilium and promotes extension of the ciliary membrane"; "preventing
  Rab8(GTP) production blocks ciliation in cells and yields characteristic BBS phenotypes in zebrafish"].
- [PMID:21273506 "upon serum withdrawal Rab8 is observed to assemble the ciliary membrane in ∼100 min"].
- [PMID:25686250 "only after ciliary vesicle assembly is Rab8 activated for ciliary growth"; "with EHD1 important for CV
  formation and Rab8 functioning in CV extension"; "Rab8 and Smoothened (Smo), largely present in the ciliary membrane"].
- Recruitment depends on CEP290 [PMID:18694559 "Depletion of CEP290 diminishes the localization of Rab8a to centrosomes
  and prevents its entry into the cilium"] and on RPGR GEF-like activity [PMID:20631154 "RPGR primarily associates with
  the GDP-bound form of RAB8A and stimulates GDP/GTP nucleotide exchange"].

Non-ciliary trafficking:
- Recycling endosomes [PMID:22854040 "The activated GTP-bound form of Rab8 is localised to the tubules emanating from the
  endocytic recycling compartment"; PMID:19864458 "endogenous MICAL-L1 can link both EHD1 and Rab8a to these
  structures"].
- Endosomal export [PMID:32344433 "Several proteins transit through endosomes and are exported in a Rab8-, Rab10-, and/or
  Rab11-dependent manner"].
- Myosin V effectors [PMID:21282656 "Myosin Vb (Myo5B) is an effector for Rab8a, Rab10, and Rab11a"; PMID:24006491].
- Golgi [PMID:15837803 "myosin VI and Rab8 colocalize around the Golgi complex and in vesicles at the plasma membrane";
  PMID:26209634 Golgi fragmentation on knockdown].
- Midbody [PMID:22159412], autophagy via C9ORF72 GEF [PMID:27103069], LRRK2 phosphorylation [PMID:26824392 "LRRK2
  directly phosphorylates these both in vivo and in vitro on an evolutionary conserved residue in the switch II domain"].

### Classification (ciliary vs other)

- Core (ACCEPT): GTPase/G protein activity, GTP/GDP binding, myosin V binding; Golgi/TGN/TGN vesicles, endosome and
  recycling endosome membranes, plasma membrane, cytoplasmic vesicle; exocytosis, endocytic recycling, protein
  localization to plasma membrane; cilium, non-motile cilium, ciliary membrane, cilium assembly, protein localization
  to cilium, Golgi vesicle fusion to target membrane.
- Non-core (KEEP_AS_NON_CORE): centrosome/centriole/basal body/ciliary base, cytosol, lysosome, phagosome, midbody,
  exosome, neuronal/synaptic locations, Golgi organization, autophagy, axonogenesis, insulin response, synaptic
  plasticity, neurotransmitter receptor transport, broad regulation terms, kinase binding.
- MODIFY: axoneme -> ciliary membrane; LRRK2 protein binding -> protein kinase binding.
- REMOVE: other bare protein binding rows (policy); small GTPase binding ISS whose source is GDI1 (inverted transfer).

## HPA cilium atlas vs module role

- HPA: **Primary cilium (Uncertain); Basal body (Uncertain); Centriolar satellite (Uncertain)**; main locations
  "Nucleoli; Nucleoplasm; Plasma membrane". GOA HPA row: plasma membrane IDA (GO_REF:0000052), ACCEPTED.
- Module role: ciliary membrane delivery GTPase (stage 2). The HPA ciliary calls are all Uncertain, so the atlas gives
  only weak support, but the literature (IDA ciliary localization in several studies, live imaging, CLEM) strongly
  supports the module role. The plasma-membrane call matches the non-ciliary exocytic role.
- Nuance: as for RAB3IP, Rab8 acts after EHD1-dependent ciliary vesicle formation, in CV extension/ciliary membrane
  growth. core_functions put RAB8A under "ciliary membrane supply" (cilium assembly, protein localization to cilium,
  ciliary membrane) rather than CV formation per se, and record the two non-ciliary core units (molecular switch;
  exocytosis/recycling).

## Deep research outcome

The re-run `just deep-research-falcon human RAB8A --timeout 2400` succeeded and produced
`RAB8A-deep-research-falcon.md` (2026-10-03). I read it after drafting the review. Its summary agrees with the
cached primary literature used here and changes none of the curation decisions. Annotation-level supporting quotes come
from the cached publications. The first core function also cites one sentence from the deep-research file.
