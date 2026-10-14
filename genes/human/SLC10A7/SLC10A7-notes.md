# SLC10A7 (Q0GE19) — curation notes

> Deep research was **not available** in this container (Falcon returned HTTP 402, OpenAI 401,
> perplexity not registered), so no `-deep-research-*.md` file was generated. This file holds the
> literature synthesis, assembled from the cached publications in `publications/` plus UniProt
> (`SLC10A7-uniprot.txt`), QuickGO and OLS lookups.

## 1. What the protein is

SLC10A7 (originally C4orf13) is the seventh and most divergent member of the SLC10
("sodium/bile acid cotransporter") family. Its only published molecular characterization is
Godoy et al. 2007: a 340–343 residue protein, >85% identity between human, mouse, rat and frog,
with a membrane topology unlike the rest of the family
[PMID:17628207 "we established a topology of 10 transmembrane domains with an intracellular cis orientation of the N-terminal and C-terminal ends"].
Unlike every other SLC10 member it has pre-vertebrate relatives
[PMID:17628207 "SLC10A7-related proteins exist also in yeasts, plants, and bacteria, making SLC10A7 taxonomically the most widespread member of this carrier family"].

**It is not a bile acid or steroid sulfate carrier.** The only transport assays ever reported were
negative [PMID:17628207 "When expressed in Xenopus laevis oocytes and HEK293 cells, SLC10A7 was detected in the plasma membrane but revealed no transport activity for bile acids and steroid sulfates"],
and UniProt records this explicitly ("Does not show transport activity towards bile acids or steroid
sulfates"). As of 2026 **the substrate is still unknown**
[PMID:30082715 "SLC10A7 is a 10-transmembrane-domain transporter located at the plasma membrane, with a yet unidentified substrate14."].

Consistent with its divergence, SLC10A7 does not associate with the family's prototype: NTCP
co-immunoprecipitates and co-localizes with SLC10A4 and SLC10A6 but
[PMID:22029531 "NTCP co-localized in U2OS cells with SLC10A4 and SLC10A6, but not with SLC10A3, SLC10A5 or SLC10A7."].

## 2. Where it is — the localization conflict

Three compartments are annotated, from three papers, and they are not of equal weight:

- **Plasma membrane** comes only from heterologous over-expression of epitope-tagged protein.
  Godoy detected HA/FLAG-tagged SLC10A7 at the surface of transfected HEK293 cells and Xenopus
  oocytes [PMID:17628207 as quoted above]. Dubail et al. re-asserted it from c-myc-tagged protein
  transfected into HEK293F cells, with no plasma-membrane co-marker, and the staining they describe
  is punctate rather than rim-like
  [PMID:30082715 "C-myc immunolabelling demonstrated a uniform punctate staining following transfection with wild-type SLC10A7, consistent with a cell membrane localization."],
  and they cite Godoy for the claim
  [PMID:30082715 "SLC10A7, previously named C4orf1317, is a 340-amino acid 10-transmembrane-domain protein localized at the plasma membrane (confirmed by the immunocytofluorescence assay performed in this study)."].
- **Golgi** is where the protein sits when asked about the human protein directly, and it is the
  compartment the functional data point to
  [PMID:29878199 "In contrast to yeast, human SLC10A7 localized to the Golgi."],
  with loss of SLC10A7 producing a secretory-pathway defect
  [PMID:29878199 "Cell biology studies in fibroblasts of affected individuals showed intracellular mislocalization of glycoproteins and a defect in post-Golgi transport of glycoproteins to the cell membrane."].
  Note that Ashikov et al. frame this as a human/yeast **difference**, which also tells us the
  fungal orthologs (Rch1p, CaRch1p) are the plasma-membrane ones.
- **Endoplasmic reticulum / ER membrane** is attributed by UniProt and GOA to PMID:17628207
  (`ECO:0000269|PubMed:17628207`), but that paper is abstract-only in our cache and its abstract
  mentions only the plasma membrane. The ER data must be in the full text (Godoy's figures), which
  I could not read. Per SKILL.md this is exactly the `UNDECIDED` case — not a removal.

**Resolution adopted:** Golgi is the physiological site (ACCEPT); plasma membrane is real but an
over-annotation of the endogenous protein, driven by over-expression of tagged constructs
(MARK_AS_OVER_ANNOTATED, including the IBA, whose donor set is fungal/bacterial — see §5); the two
ER rows are UNDECIDED pending Godoy's full text. GAG assembly begins at the ER exit and continues
through the Golgi [PMID:30082715 "The GAG biosynthesis, initiated at the exit of endoplasmic reticulum"],
so an early-secretory-pathway pool is biologically plausible; it is simply unverifiable here.

## 3. Calcium

The yeast and Candida orthologs are calcium regulators, which is what prompted the human experiment
[PMID:30082715 "two studies performed with SLC10A7 homologues in yeast, CaRch1p and Rch1p, suggest a possible role as a negative regulator of cytosolic calcium homoeostasis15,16."].
Patient fibroblasts behave the same way:
[PMID:30082715 "After addition of extracellular CaCl2, SLC10A7-deficient patient fibroblasts showed a significantly increased Ca2+ influx compared with control fibroblasts"],
i.e. loss of SLC10A7 **raises** Ca2+ entry, so the wild-type protein is a negative regulator of
Ca2+ influx. This is the one mechanistic function that is both conserved from yeast to human and
directly measured in human cells, so `GO:0006874 intracellular calcium ion homeostasis` is accepted
as core. (A more specific "negative regulation of calcium ion import" term was considered but not
proposed: the measurement is a whole-cell influx readout in a patient line, and the transported
species is unknown, so the directionality is inferred from a loss-of-function phenotype only.)

## 4. The GAG phenotype — necessity vs participation

What was measured in Dubail et al.:
- [PMID:30082715 "Furthermore, we identify decreased heparan sulfate levels in Slc10a7-/- mouse cartilage and patient fibroblasts."]
- [PMID:30082715 "the proportion of heparan sulfate (HS) was significantly reduced by ~2-fold in SLC10A7-deficient patient fibroblasts compared with control fibroblasts and by about 2.5-fold in Slc10a7−/− mouse cartilage compared with wild-type mouse cartilage"]
- Sulfation itself is **normal**: [PMID:30082715 "indicating that HS decrease in Slc10a7−/− is mostly related to the number of HS chains, rather than to their sulfation and length."]
- And the authors' own mechanism is indirect: [PMID:30082715 "This deregulation of Ca2+ homoeostasis due to SLC10A7 deficiency is most likely responsible for defects in GAG synthesis and glycosylation."]

So: **heparin was never assayed** (heparin is the hypersulfated, mast-cell/serglycin GAG;
`GO:0030210` is defined as formation of heparin proteoglycans specifically), and SLC10A7 catalyses
no step of chain initiation, elongation, epimerization or sulfation. It supplies a permissive
lumenal ion environment.

Comparator check (QuickGO, human+mouse):
- `GO:0030210` holds 47 annotations, essentially all of them the HS/heparin biosynthetic **enzymes**
  — EXT1, EXT2, NDST1-4, GLCE, B3GALT6, B4GALT7, CSGALNACT1 — plus SLC10A7 itself. No other
  transporter is there.
- **TMEM165** is the closest comparator of all: a Golgi Ca2+/Mn2+ transporter whose loss causes a
  congenital disorder of glycosylation. GO gives it `GO:0032472` Golgi calcium ion transport,
  `GO:0032468` Golgi calcium ion homeostasis, `GO:0071421` manganese ion transmembrane transport —
  and **no** glycosylation or glycan-biosynthesis process term. The agent-of-the-step convention is
  being applied.
- **SLC35D1** (Golgi UDP-GlcA/UDP-GalNAc transporter, Schneckenbecken dysplasia) likewise carries
  only transport terms.
- **SLC35B2** (Golgi PAPS transporter) *is* annotated `GO:0050650` chondroitin sulfate proteoglycan
  biosynthetic process by IMP — so the convention is not absolute, and a transporter that delivers
  the actual donor substrate into the lumen can carry the biosynthetic term.

Verdict: do not REMOVE (the requirement is solid and reproduced in two species), but the term as
written is wrong on specificity. **MODIFY to `GO:0015012` heparan sulfate proteoglycan biosynthetic
process** — the GAG that was actually measured — and treat it as a permissive/upstream contribution
rather than a core catalytic role. If a curator prefers the strict TMEM165 convention, the
alternative would be to drop the biosynthesis term entirely and keep only the calcium term; that is
noted as a question for experts rather than acted on, because SLC10A7's substrate is unknown and it
may yet turn out to be a donor transporter in the SLC35B2 mould.

## 5. Bone

Human: short stature, skeletal dysplasia with multiple dislocations, scoliosis, decreased bone
mineral density, amelogenesis imperfecta
[PMID:29878199 "The patients' phenotype consisted of amelogenesis imperfecta, skeletal dysplasia, and decreased bone mineral density compatible with osteoporosis."].
Mouse: [PMID:30082715 "We generate a Slc10a7-/- mouse model, which displays shortened long bones, growth plate disorganization and tooth enamel anomalies, recapitulating the human phenotype."]
and [PMID:30082715 "There was a strong reduction of Safranin O staining, a marker of sulfated GAG chains, in Slc10a7−/− mice compared with wild-type mice, which was associated with disorganization of the growth plate"].
Zebrafish: [PMID:29878199 "Furthermore, alizarin red staining of calcium deposits in zebrafish morphants showed a strong reduction in bone mineralization."]

SLC10A7 is widely expressed (UniProt TISSUE SPECIFICITY; liver highest), and the skeletal
phenotype is the tissue in which a general cartilage/bone ECM defect becomes visible. This is the
textbook pleiotropic-developmental-consequence case, so `GO:0060348 bone development` is kept but
marked **non-core** rather than accepted as a core function.

## 6. Interactors

All three `GO:0005515 protein binding` rows are the same interactor, Q7Z388 = **DPY19L4** (UniProt
`INTERACTION: Q0GE19; Q7Z388: DPY19L4; NbExp=4`), reported by three high-throughput AP-MS surveys:
BioPlex 2.0 [PMID:28514442], BioPlex 3.0 [PMID:33961781] and the RESOLUTE SLC interactome
[PMID:40355756]. None of the three cached full texts mentions SLC10A7 by name, and none assigns it
a molecular function. DPY19L4 is annotated by UniProt as a "Probable C-mannosyltransferase that mediates
C-mannosylation of tryptophan residues on target proteins" (multi-pass membrane protein), so the
pairing is suggestive for the glycosylation story, but an AP-MS co-precipitation supports no informative
MF. Per SKILL.md "Quality Standards", these are REMOVE as uninformative (not
MARK_AS_OVER_ANNOTATED); removal does not assert the interaction is false.

## 7. Open questions

- What does SLC10A7 transport? Nothing has been tested since the 2007 bile-acid/steroid-sulfate
  panel. Candidates worth testing in a Golgi-oriented assay: Ca2+, Mn2+, sulfate, PAPS, nucleotide
  sugars.
- Is the Ca2+ effect at the plasma membrane (store-operated entry, the yeast Rch1 model) or inside
  the Golgi (the TMEM165 model)? The published measurement cannot distinguish them.
- Is the PM pool real at endogenous levels, or an over-expression artefact? Needs an endogenous
  tag / validated antibody with surface biotinylation.
