# MNT4 (YNR059W) — curation notes

Gene: **MNT4** / systematic **YNR059W** / UniProt **P53745** (MNT4_YEAST)
Organism: *Saccharomyces cerevisiae* S288C (NCBITaxon:559292)
SGD: S000005342. CAZy: **GT71** (Glycosyltransferase Family 71). PANTHER: **PTHR31392:SF1** (ALPHA-1,3-MANNOSYLTRANSFERASE MNN1-RELATED).

This is an **understudied ("dark") gene**. The deliverable is an honest boundary between what is
domain/orthology-defensible and what is genuinely unknown. Attribute all MNT4-specific evidence
carefully versus the broader MNN1/MNT family.

## Summary judgment (up front)

- MNT4 is a **putative** (probable) alpha-1,3-mannosyltransferase of the **Mnn1p (MNN1/MNT) family**.
  No enzyme assay, no acceptor substrate, no in-vivo product, and no informative deletion phenotype
  have ever been reported *for MNT4 itself*. UniProt evidence level is **PE 3: Inferred from homology**.
- The one primary paper that touches MNT4 experimentally (Romero et al. 1999, PMID:10521541) tested
  it genetically and found MNT4 is **NOT required** for O-glycan synthesis, in contrast to its
  paralogs MNT2 and MNT3.
- Therefore: a **generic family-level mannosyltransferase molecular function** and a **Golgi/secretory
  type-II membrane localization** are domain-defensible; a **specific acceptor substrate / in-vivo
  activity / biological role** is a genuine knowledge gap, and the specific "protein O-linked
  glycosylation" process assignment is not supported (and is arguably contradicted) for MNT4.

## Sequence / domain analysis (done inline; UniProt P53745)

Source: `genes/yeast/MNT4/MNT4-uniprot.txt` (580 aa, MW 68082).

Topology (UniProt, ECO:0000255 predicted):
- TOPO_DOM 1–10 cytoplasmic; **TRANSMEM 11–29 "Signal-anchor for type II membrane protein"**;
  TOPO_DOM 30–580 lumenal. → single-pass **type II membrane protein**, N-terminus in cytosol,
  large C-terminal catalytic domain in the lumen — the canonical topology of Golgi
  glycosyltransferases of the MNN1 family.
- 4 predicted N-glycosylation sites (N132, N167, N223, N349) — consistent with a lumenal domain.

Family / fold:
- Pfam **PF11051 (Mannosyl_trans3)**; InterPro **IPR022751 (Alpha_mannosyltransferase)** +
  **IPR029044 (Nucleotide-diphospho-sugar transferases)**; SUPFAM SSF53448 (nucleotide-diphospho-sugar
  transferases). This is the GT-A-like nucleotide-sugar transferase superfamily used by the MNN1 family.

**Catalytic DXD motif — the load-bearing domain check.**
Wiggins & Munro (1998, PMID:9653120) identified a conserved **two-aspartate (DxD) motif** as essential
for Mnn1p alpha-1,3-mannosyltransferase activity: *"altering either of these aspartates eliminates all
enzymatic activity"* [PMID:9653120 abstract], and they note the DxD is *"flanked by four hydrophobic
residues on the N-terminal side, with the third of these often being an aromatic residue"* (per the
PNAS paper as summarized; the abstract itself states the motif is essential and conserved across GT
families).

I scanned P53745 for DxD-type motifs (script run inline, `/tmp/mnt4_seq.py`):
- Candidate DxD motifs at D114-Q-D116 ("EIRA**DQD**ISLL") and **D300-S-D302 ("PIFL**DSD**TVPF")**.
- The **D300-S-D302** site matches the Wiggins–Munro consensus strikingly well: it is preceded by
  four hydrophobic residues **P-I-F-L** whose **third residue is the aromatic F**, exactly the
  described flanking pattern, and DxD sits at the expected mid-lumenal-domain position.
- Interpretation: the **candidate catalytic DxD motif of the MNN1 family appears intact in MNT4**
  (no obvious pseudogene-style loss of both catalytic aspartates). This supports keeping a
  *generic* mannosyltransferase MF as domain-defensible. It does **not** prove the enzyme is active
  in vivo, and does **not** identify the acceptor substrate.

## Family context — separate MNT4 from its paralogs

PANTHER PTHR31392:SF1 members in S. cerevisiae + C. albicans
(`interpro/panther/PTHR31392/PTHR31392-entries.csv`): S. cerevisiae **MNN1 (P39106)**,
**MNT3 (P40549)**, **MNT2 (P53059)**, **MNT4 (P53745)**; plus C. albicans MNT4/MNN12/13/14/15 and MNN1.

Family biology (established for the *characterized* members, NOT MNT4):
- The *S. cerevisiae* genome has five type II membrane proteins similar to the
  alpha-1,3-mannosyltransferase Mnn1p [PMID:10521541 abstract: *"The genome of Saccharomyces cerevisiae
  contains five genes that encode type II transmembrane proteins with significant amino acid similarity
  to the alpha-1,3-mannosyltransferase Mnn1p."*].
- **MNN1** adds terminal alpha-1,3-mannose to N- and O-linked glycans in the Golgi.
- **MNT2 and MNT3** (with MNN1) add the 4th and 5th alpha-1,3-linked mannoses of O-linked glycans
  [PMID:10521541 abstract: *"the MNT2 (YGL257c) and MNT3 (YIL014w) genes in combination with MNN1 have
  overlapping roles in the addition of the fourth and fifth alpha-1,3-linked mannose residues to form
  Man4 and Man5 oligosaccharides"*].

## MNT4-specific evidence (all of it)

1. **Not required for O-glycan synthesis.** [PMID:10521541 abstract: *"whereas MNT4 (YNR059w) does not
   appear to be required for O-glycan synthesis."*] This is the *only* functional experimental datum
   for MNT4, and it is a **negative** result for the O-glycosylation role.
2. **No enzyme assay / no acceptor substrate reported.** UniProt lists the name as *"Probable
   alpha-1,3-mannosyltransferase MNT4"* and EC **2.4.1.-** (incomplete), PE **3 (inferred from
   homology)**; SIMILARITY: *"Belongs to the MNN1/MNT family."* The GO MF/BP annotations are all
   IBA/IEA/ISS/IC — none experimental for MNT4.
3. **Localization is uncertain.** UniProt gives only a predicted "Membrane; Single-pass type II
   membrane protein" (ECO:0000305). The IBA/IEA "Golgi apparatus" is a family inference. High-throughput
   fluorescent-tag screens (as summarized on SGD) reported MNT4 fusions to the ER and vacuole rather
   than a clean Golgi signal — i.e. even the compartment is not firmly established for MNT4. (I do not
   have a cached primary publication with a verbatim localization quote, so I record localization
   uncertainty as a knowledge gap rather than citing a specific quote.)

## Provenance for the GOA annotations (what they actually trace to)

From `MNT4-goa.tsv`:
- GO:0000033 alpha-1,3-mannosyltransferase activity — **IBA** (GO_REF:0000033; PANTHER PTN001264810,
  with SGD:S000000803/…001276/…003226 = MNN1/MNT2/MNT3). Family phylogenetic inference.
- GO:0000033 — **ISS** ×3 (PMID:10521541; with SGD:S000000803/001276/003226 = MNN1/MNT2/MNT3). Sequence
  similarity to the characterized paralogs, from the very paper whose genetics say MNT4 is not needed
  for O-glycan synthesis.
- GO:0006493 protein O-linked glycosylation — **IBA** (GO_REF:0000033) and **IC** (PMID:10521541, from
  GO:0000033). The IC is a curator inference *from the MF*, not independent evidence that MNT4 acts in
  O-glycosylation; the same paper's data argue against an O-glycan role for MNT4 specifically.
- GO:0005794 Golgi apparatus — **IBA** + **IEA** (ARBA). Family inference.
- GO:0000030 mannosyltransferase activity — **IEA** (ARBA). Generic parent of GO:0000033.
- GO:0009101 glycoprotein biosynthetic process — **IEA** (ARBA/InterPro).
- GO:0016757 glycosyltransferase activity — **IEA** (InterPro IPR022751). Generic parent.
- GO:0016020 membrane — **IEA** (UniProt SubCell). Matches the predicted TM.
- GO:0005575 cellular_component — **ND** (GO_REF:0000015). Root, placeholder.

## Curation decisions (rationale)

- Keep **generic mannosyltransferase / alpha-1,3-mannosyltransferase MF** as domain-defensible (intact
  DxD, clear family membership) but treat the *specific acceptor substrate* as unknown. Per project
  rules I do not REMOVE the family-level MF: the domain evidence supports a probable mannosyltransferase
  activity, and REMOVE is not warranted for a plausible, homology-supported family activity. I mark the
  MF annotations KEEP_AS_NON_CORE / ACCEPT-with-caveat where appropriate and record the substrate gap.
- **Golgi apparatus (IBA/IEA):** family-level inference; retain as non-core, flag CC uncertainty
  (ER/vacuole in HT screens). Membrane (IEA) matches the predicted type-II TM → ACCEPT (non-core).
- **protein O-linked glycosylation (IBA and IC):** the specific process assignment is **not supported
  for MNT4** and is contradicted by the only genetic test (PMID:10521541). Mark these as
  MARK_AS_OVER_ANNOTATED (family-transferred; the negative genetic result is the key MNT4-specific datum).
- Generic parents (GO:0000030, GO:0016757, GO:0009101): KEEP_AS_NON_CORE (true-but-uninformative IEA
  parents; not core).
- ND root (GO:0005575): ND placeholder, KEEP_AS_NON_CORE.

## Knowledge gaps (the deliverable)

1. **Acceptor substrate + demonstrated catalytic activity of MNT4 is unknown.** No enzyme assay, no
   product, no donor/acceptor pair. Boundary: family membership + intact candidate DxD motif make a
   mannosyltransferase activity *probable*, but the reaction MNT4 catalyzes (if any) in vivo is
   undetermined; EC is 2.4.1.- and PE is 3.
2. **In-vivo biological role + phenotype is unknown, and the family default (O-glycosylation) is
   specifically excluded.** MNT4 is not required for O-glycan synthesis (PMID:10521541); no other
   process, no deletion phenotype, and no genetic partner have been assigned. Possible functional
   redundancy within the MNN1/MNT family is untested for MNT4.
3. **Subcellular compartment of action is uncertain.** Predicted type-II membrane topology is clear,
   but IBA/IEA place MNT4 in the Golgi (family default) while HT fluorescence screens report ER/vacuole
   — the actual site of MNT4 function is unresolved (CC-dark).

## Deep-research status

Automated falcon deep research (`just deep-research-falcon yeast MNT4 --fallback perplexity-lite`)
was attempted multiple times during this review; the Edison/falcon endpoint hung and the runs
exited without producing a `MNT4-deep-research-falcon.md` file (a background retry is left running so
a genuine file can land later). No deep-research file was fabricated. This review is therefore grounded
directly in the UniProt record (P53745), the GOA table, two cached primary abstracts (PMID:10521541,
PMID:9653120), the PANTHER PTHR31392 family membership table, and inline sequence/domain analysis
documented above. Web searches (PubMed/SGD/PNAS listings) were used only to locate and confirm these
primary sources; no web-only claim is used as a supporting_text quote.

## Provenance log (verbatim quotes used)

- PMID:10521541 (abstract, cached, full_text_available: false):
  - *"The genome of Saccharomyces cerevisiae contains five genes that encode type II transmembrane
    proteins with significant amino acid similarity to the alpha-1,3-mannosyltransferase Mnn1p."*
  - *"the MNT2 (YGL257c) and MNT3 (YIL014w) genes in combination with MNN1 have overlapping roles in
    the addition of the fourth and fifth alpha-1,3-linked mannose residues to form Man4 and Man5
    oligosaccharides whereas MNT4 (YNR059w) does not appear to be required for O-glycan synthesis."*
- PMID:9653120 (Wiggins & Munro 1998, abstract, cached, full_text_available: false):
  - *"altering either of these aspartates eliminates all enzymatic activity"*
  - *"a short motif containing two aspartate residues was observed that was conserved in both groups
    of proteins"*
- UniProt P53745: RecName *"Probable alpha-1,3-mannosyltransferase MNT4"*; EC 2.4.1.-; PE 3;
  SIMILARITY *"Belongs to the MNN1/MNT family."*; TRANSMEM 11–29 *"Signal-anchor for type II membrane
  protein"*.
</content>
</invoke>
