# MSP1 (Plasmodium falciparum 3D7, Q8I0U8, PF3D7_0930300) — curation notes

**Provenance note:** automated deep research was **not available** in this environment
(Falcon authentication failed and the OpenAI key was invalid), so no
`*-deep-research-*.md` file was generated. The notes below are my own **manual
literature review**, built from the UniProt flat file, the cached publications in
`publications/`, and additional PMIDs I fetched into that cache
(`uv run ai-gene-review fetch-pmid`). Every assertion carries an inline citation with a
verbatim quote where possible.

## 1. What the protein is

MSP1 is the most abundant GPI-anchored protein of the *P. falciparum* merozoite surface
coat, made as a ~190–200 kDa precursor (1720 aa in 3D7) during schizogony
[file:PLAF7/MSP1/MSP1-uniprot.txt "RecName: Full=Merozoite surface protein 1"].
It has no orthologues outside *Plasmodium*
[PMID:26468747 "MSP1 has no orthologs outside Plasmodium and structural information is sparse"],
so electronic family-based transfer has little to offer here — the annotation base is
almost entirely direct experimental work on the parasite itself.

GPI anchoring is established biochemically rather than merely predicted
[PMID:8992312 "Detailed structural analysis of the core-glycans showed that the GPI-anchors of both proteins possess an extra alpha 1-2 linked mannose at the conserved trimannosyl-core-glycan"].

## 2. Proteolytic maturation defines its states

Two ordered processing steps generate the functional forms:

- **Primary processing by SUB1**, in the parasitophorous vacuole minutes before egress,
  cuts the precursor into p83/p30/p38/p42, which stay non-covalently associated on the
  merozoite surface
  [PMID:19214190 "We show that just before egress, all undergo proteolytic maturation by PfSUB1."].
  The order of cleavage matters for viability
  [PMID:20735778 "Our findings show that correct spatiotemporal regulation of MSP1 maturation is crucial for the function of the protein and for maintenance of the parasite asexual blood-stage life cycle."].
- **Secondary processing by SUB2** during invasion cleaves p42 into p33 + p19; the whole
  complex is shed except GPI-anchored p19
  [PMID:16322767 "Erythrocyte invasion by merozoites of the malaria parasite Plasmodium falciparum requires the shedding of ectodomain components of two essential surface proteins, called MSP1 and AMA1."]
  [PMID:1694225 "During erythrocyte invasion only a small fragment from this complex is retained on the parasite surface and carried into the newly infected red cell."].

Note for review purposes: in the SUB1/SUB2 papers MSP1 is the **substrate**, not the
protease — those references support MSP1's *location* (surface, then shed/extracellular),
not any peptidase activity of MSP1.

## 3. Core function 1 — egress via host spectrin

The best-defined mechanistic role. SUB1 processing converts MSP1 into a spectrin-binding
form, and loss of surface MSP1 blocks egress:

- [PMID:26468747 "Processing modifies the secondary structure of MSP1 and activates its capacity to bind spectrin, a molecular scaffold protein that is the major component of the host erythrocyte cytoskeleton."]
- [PMID:26468747 "Parasites expressing an inefficiently processed MSP1 mutant show delayed egress, and merozoites lacking surface-bound MSP1 display a severe egress defect."]
- [PMID:26468747 "Our results indicate that interactions between SUB1-processed merozoite surface MSP1 and the spectrin network of the erythrocyte cytoskeleton facilitate host erythrocyte rupture to enable parasite egress."]
- Direct binding, with affinity, confirmed structurally:
  [PMID:34078606 "KD values of 31 ± 5 nM (n = 4, red squares) and 100 ± 10 nM (n = 2, blue triangles) were found for the hdMSP-1–spectrin and MSP-1–spectrin complexes, respectively."]
  and [PMID:34078606 "MSP-1 also interacts with the erythrocyte cytoskeleton protein spectrin (24, 25) and plays a role in egress (25)."]

So MSP1 itself does work in egress (it binds and perturbs the host cytoskeletal lattice);
it is not merely required for it. This passes the participation test for a process term,
and the host-directed nature of the act makes the symbiont/host branch
(`GO:0052039`, `GO:0035891`) the right place for it.

## 4. Core function 2 — adhesion to host erythrocyte during invasion

- MSP1-42/19 binds the exofacial 5ABC segment of host band 3 (SLC4A1), sialic
  acid-independently
  [PMID:12692305 "A major segment of the band 3 receptor (5ABC) bound to native MSP1(42) and blocked the interaction of native MSP1(42) with intact RBCs in vitro."]
  [PMID:12692305 "These findings suggest that the chymotrypsin-sensitive MSP1-band 3 interaction plays a role in a sialic acid-independent invasion pathway and reveal the function of MSP1 in the Plasmodium invasion of RBCs."]
- MSP9 and MSP1-42 form a co-ligand complex on the same receptor
  [PMID:14630931 "Native MSP9 and MSP1(42), the two ligands binding to the 5ABC receptor, existed as a stable complex."]
- The N-terminus binds host glycophorin A
  [PMID:25778531 "Mapping of the binding domains established a direct interaction between malaria MSP1 and human GPA within a region of MSP1 known to potently inhibit P falciparum invasion of human RBCs."]
- Band 3 engagement also involves rhoptry RhopH3 in complex with MSP1-19
  [PMID:25157665 "RhopH3 formed a complex with MSP119 and the 5ABC region of band 3, and a recombinant segment of RhopH3 inhibited parasite invasion in human erythrocytes."]
- Anti-p19 antibodies block invasion
  [PMID:36202833 "Naturally acquired antibodies targeting p19 prevent merozoite invasion of RBCs and are associated with protection from clinical malaria12,23–27 and protection appears to be FcγRI-mediated in a transgenic rodent malaria model for MSP-128."]

These justify a host-directed molecular function term, `GO:0046789 host cell surface
receptor binding`, which GOA currently lacks for this gene (it only has bare
`GO:0005515`).

## 5. Core function 3 — scaffold for the merozoite surface coat

MSP1 nucleates a large peripheral surface complex:

- [PMID:16940297 "Both MSP-6(36) and MSP-7 bind only to MSP-1 subunits that are shed, but although MSP-6(36) contacts just subunit p38, MSP-7 interacts with p83, p30, and p38."]
- [PMID:25074930 "This demonstrates that the MSP1 complex acts as a platform for display of MSPDBL1 and MSPDBL2 on the merozoite surface for binding to receptors on the erythrocyte and invasion."]
  — note MSP1 itself did **not** bind erythrocytes in that assay
  [PMID:25074930 "In addition, MSPDBL1 and MSPDBL2, but not MSP1, bound directly to human erythrocytes."],
  which is a genuine tension with the band 3 / GPA binding literature (different
  fragments, different assay formats) and worth flagging to experts.
- [PMID:29511044 "Among the proteins of MSP-1 complex, PfMSP-6 and PfMSP-9 bound to human erythrocytes."]
- Rhoptry proteins co-purify with MSP1 on the merozoite surface
  [PMID:21175202 "Proteomic analysis identified a major malaria surface protein, PfRhopH3 interacting with PfMSP-1(42)."]

## 6. Accessory activities

- **p33 sequesters host S100P**:
  [PMID:22431641 "MSP1(33) blocks S100P-induced NFκB activation in monocytes and chemotaxis in neutrophils."]
  — host-directed immune dampening; the appropriate branch is
  `GO:0052170 symbiont-mediated suppression of host innate immune response`. Evidence is
  in vitro with recombinant protein, so it is a defensible but non-core addition.
- **p19 marks and may build the food (digestive) vacuole** after invasion:
  [PMID:18769730 "This protein is the first marker for the biogenesis of the food vacuole; it is rapidly endocytosed into small vacuoles in the ring stage, which coalesce to form the single food vacuole containing hemozoin, and persists into the discarded residual body."]
  [PMID:18769730 "The food vacuole is marked by the presence of both MSP1(19) and the chloroquine resistance transporter (CRT) as components of the vacuolar membrane."]
  UniProt is careful here — "May play a role in the biogenesis and/or function of the food
  vacuole" is flagged `ECO:0000305` (Probable). So the **location** (vacuolar membrane) is
  solid; the **process** (food vacuole biogenesis) is not, and I do not propose a process
  term for it.
- **PFD6 (prefoldin subunit 6) interaction** is reported
  [PMID:33145997 "This looks intriguing that how a small prefoldin subunit of molecular mass 13 kDa associates and stabilizes a large protein (MSP1) of mass ~ 200 kDa, which is indispensable for invasion of the red cell by the parasite."]
  but UniProt records it as "May interact", and it is not in GOA; not proposed.

## 7. Protist-specific checks performed

- **No animal/plant-only terms** present in the GOA set — nothing to strip on taxon grounds.
- **Organelles**: the only organellar term is `GO:0005774 vacuolar membrane`, which here
  means the **food/digestive vacuole** membrane (PMID:18769730), a real apicomplexan
  compartment. GO has `GO:0020020 food vacuole` but **no** "food vacuole membrane" term —
  recorded as a `proposed_new_terms` entry rather than forcing a bad id. No apicoplast,
  rhoptry or microneme claim is made for MSP1 (the rhoptry proteins RhopH3/RAP1 are
  *partners*, not evidence that MSP1 is in a rhoptry).
- **Host vs symbiont**: all host-directed activity is annotated to the symbiont/host
  branch (`GO:0085017`, and proposed `GO:0046789`, `GO:0035891`, `GO:0052039`,
  `GO:0052170`), never to the plain host-cell-biology terms.
- **Paralog family**: MSP1 is a single-copy, *Plasmodium*-restricted gene; the MSP3/MSP7
  "families" are distinct genes, not MSP1 paralogs, so there is no paralog-family
  over-annotation risk. The single IEA from InterPro (IPR010901, `GO:0016020 membrane`)
  is merely uninformative, not wrong.

## 8. Curation decisions taken

- `GO:0005886 plasma membrane` kept as the core location (merozoite surface); the one row
  whose evidence is the GPI-anchor structural analysis (PMID:8992312) is refined to
  `GO:0031362 anchored component of external side of plasma membrane`.
- `GO:0005576 extracellular region` kept but non-core: it reflects the shed complex, which
  is a real and well-documented state but not where MSP1 does its work.
- `GO:0016020 membrane` (IEA/InterPro) marked `TOO_GENERAL` — entailed by the accepted
  plasma membrane term.
- Four `GO:0005515 protein binding` rows kept as non-core (per project policy, protein
  binding is neither removed nor marked too-general); the informative partners are
  RhopH3 (Q8I395), RAP1 (Q8ILZ1), CLAG9 (Q8I2G2), MSPDBL1 (PF3D7_1035700) and host S100P
  (P25815), and I add the informative MF terms separately as `NEW` rows.
- No `REMOVE` anywhere: nothing in the GOA set is contradicted by the literature.
