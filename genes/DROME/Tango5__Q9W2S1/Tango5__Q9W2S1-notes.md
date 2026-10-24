# Tango5 (Q9W2S1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: Q9W2S1 is the 530-residue product of Drosophila Tango5/vmp1 (FBgn0052675).
It is the UniProt entry GO Central uses for the PAINT IBAs on this gene. The benchmark
entry Q7KVQ7 (reviewed in `genes/DROME/Tango5/`) is identical to residues 103-530 of
Q9W2S1 (`file:DROME/Tango5/Tango5-bioinformatics/RESULTS.md`). No ProtNLM2 output was
opened or used for this review.

### Deep research

`just deep-research-falcon DROME Tango5__Q9W2S1 --fallback perplexity-lite` failed:
falcon returned "Failed to authenticate", and the perplexity fallback returned HTTP 401
(insufficient quota). No deep-research file was produced for this folder. The falcon report
written for the same gene under the Q7KVQ7 accession
(`genes/DROME/Tango5/Tango5-deep-research-falcon.md`) was read as background only. Every
claim below is checked against the cached primary papers.

### Evolutionary placement

- PANTHER family PTHR10281 is heterogeneous. It joins the VMP1 subfamilies with
  cytochrome-b5-domain MAPR proteins (PGRMC1/2, neudesin, neuferricin)
  (`interpro/panther/panther.obo`). Assertions at the root node PTN000031541 (membrane,
  endomembrane system) therefore cover both kinds of protein and say little.
- Q9W2S1, Q7KVQ7 and human VMP1 (Q96GC9) are all in PTHR10281:SF1 "VACUOLE MEMBRANE PROTEIN 1"
  (`file:DROME/Tango5/Tango5-bioinformatics/RESULTS.md`). Their global identity is about 55%.
- PAINT nodes (`interpro/panther/PTHR10281/PTHR10281-paint.tsv`):
  - PTN000031590 (eukaryotic VMP1 clade, which includes Arabidopsis KMS1/KMS2):
    ER (seeded by plant, fly, human and Dicty members), phospholipid scramblase activity
    (seeded by human VMP1 only), and endomembrane system organization.
  - PTN000031591: autophagosome assembly (human VMP1, Dicty Vmp1) and Golgi organization
    (fly Tango5, Dicty Vmp1).
  - The fly protein-secretion IMP was **not** propagated to any node. I treat that as a
    deliberate decision.
- UniProt features on Q9W2S1: four Phobius TM helices (171-188, 208-233, 348-364,
  470-491), Pfam KMS1_N (122-219) and VMP1_C (470-501), and a disordered N-terminus
  (1-132). The ARBA-derived CC lines (catalytic activity, subcellular location, "VMP1
  family") are not used as support.

### What is established in Drosophila (experimental)

- ER localization. Endogenous GFP-Vmp1 co-localizes with Sec61beta and SERCA in larval
  intestine [PMID:34019822 "GFP-Vmp1 co-localizes with the ER markers Sec61β and SERCA in intestine cells"].
  The Bard et al. 2006 screen also reported ER localization (IDA; abstract only).
- Essential gene. Lethality is rescued by a duplication [PMID:34019822 "an X chromosome
  duplication containing the vmp1 open reading frame complemented the vmp1(Δ) lethal phenotype"].
- Required for autophagy. With vmp1 loss, Atg8a puncta fail to accumulate and Ref2p
  accumulates [PMID:34019822].
- Genetically upstream of Vps13D and Marf in mitochondrial clearance and in limiting
  mitochondria-ER contact [PMID:34019822]. These are downstream phenotypes and are not
  annotated as process participation.
- S2 RNAi screen: depletion inhibits constitutive secretion and makes Golgi membranes fuse
  with the ER [PMID:16452979, abstract only; details from FlyBase curation of the full text].

### What is inferred (not tested in fly)

- Phospholipid scramblase activity. This rests on reconstituted human VMP1 [PMID:33929485;
  PMID:33850023] and on the PTN000031590 IBD. The fly protein has not been assayed.
- A mechanistic role in phagophore expansion, as the ER-leaflet scramblase partnered with
  ATG2 [PMID:33850023]. Fly data establish only that the gene is required.

### Decisions

- Scramblase IBA: ACCEPT, as the core MF (inferred). ND: MODIFY to scramblase.
- ER rows (IBA, IDA, IEA): MODIFY to ER membrane (GO:0005789).
- Vacuolar membrane (ARBA SubCell): MARK_AS_OVER_ANNOTATED.
- Plasma membrane phospholipid scrambling (IEA from the scramblase MF): wrong membrane. The
  fly protein is in the ER. MODIFY to the location-neutral phospholipid translocation
  (GO:0045332).
- Membrane and endomembrane system (root-node IBAs): TOO_GENERAL, beside ER membrane.
- Autophagosome assembly IBA: ACCEPT. It is supported by fly requirement data plus the
  family mechanism.
- Golgi organization (IBA, IMP), endomembrane system organization (IBA) and protein
  secretion (IMP): KEEP_AS_NON_CORE. These are likely consequences of ER membrane
  homeostasis.
