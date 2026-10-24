# MSC2 (YDR205W, Q03455) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: MSC2 was reviewed as the closest experimentally characterised relative of
fission-yeast cis4 (Q9HGQ3). This review treats MSC2 in its own right. No ProtNLM2
output was opened or used.

### Deep research

`just deep-research-falcon yeast MSC2 --fallback perplexity-lite` failed: Falcon
returned "Edison API request failed: Failed to authenticate" (HTTP 403), and the
perplexity-lite fallback timed out after 600 s. There is no deep-research file. The
review rests on the cached primary literature below, the UniProt record and the
local site analysis in `MSC2-bioinformatics/`.

### Evolutionary placement

- UniProt: CDF transporter family (TC 2.A.4), PANTHER PTHR45755:SF4 (PANTHER name
  "ZINC TRANSPORTER 7"), InterPro IPR045316 Msc2-like. S. pombe Cis4 is in the same
  subfamily (PTHR45755:SF4).
- PAINT: MSC2 (SGD:S000002613) is one of the experimental donors to PTN000169508,
  together with Cis4 (PomBase:SPAC17D4.03c) and vertebrate ZnT5/ZnT7. That node carries
  zinc ion transmembrane transporter activity, intracellular zinc ion homeostasis, zinc
  ion import into Golgi lumen and Golgi cis cisterna membrane. Golgi apparatus and
  cytoplasmic vesicle come from a deeper node, PTN000169412.
- 14 predicted TM helices (UniProt TRANSMEM 7..584): an N-terminal extension plus the
  six-TM CDF core, the same architecture as ZnT5.
- Site A (`MSC2-bioinformatics/RESULTS.md`): Msc2 keeps the complete His-Asp-His-Asp
  transmembrane zinc site (H420, D424, H531, D535), as do Cis4 and ZnT5. Its partner
  Zrg17 (F/D/T/N) and human ZnT6 (L/D/F/D) have lost it. So Msc2 is predicted to be
  the subunit that carries zinc in the Msc2-Zrg17 heteromer.

### What is established experimentally in S. cerevisiae

1. Zinc distribution and homeostasis (Li & Kaplan 2001, abstract only).
   [PMID:11058603 "Regardless of the concentration of Zn2+ in the media, the msc2 strain had a higher Zn2+ content than wild type cells."]
   [PMID:11058603 "An epitope-tagged Msc2p was localized to the endoplasmic reticulum/nucleus."]
   The authors proposed that Msc2 moves zinc out of the nucleus/ER. That direction of
   transport was later revised (point 2). The UniProt FUNCTION text still gives the old
   direction ("moving zinc from the nucleus/endoplasmic reticulum to the cytoplasm").
2. Zinc import into the ER (Ellis et al. 2004, full text).
   [PMID:15277543 "Our results indicate that Msc2 is one route of zinc entry into the ER."]
   With expression from its own promoter on a low-copy plasmid, Msc2 cofractionates with
   the ER and shows the Mg2+-dependent ER density shift.
   [PMID:15277543 "Because Msc2 colocalizes with an ER marker protein and shows the characteristic ER Mg2+ shift, these studies strongly support the localization of Msc2 to that compartment."]
   Some protein is also seen in lighter fractions:
   [PMID:15277543 "suggests that some protein may also be found in later compartments of the secretory pathway, perhaps the Golgi"]
   In msc2 mutants, the UPR is induced more strongly and ERAD (CPY*) is defective in
   low zinc. These are downstream consequences of low lumenal zinc and are not
   annotated as Msc2 process participation.
3. Heteromeric complex with Zrg17 (Ellis et al. 2005, abstract only).
   [PMID:15961382 "Msc2p and Zrg17p physically interact with each other, as determined by co-immunoprecipitation."]
   High-throughput IPI rows (Y2H, split-ubiquitin, PCA) confirm the interaction.
4. Regulation. ZRG17 is a Zap1 target. MSC2 mRNA rises about 1.5-fold in zinc-limited
   cells [PMID:27657924]. Complex activity matters mainly under zinc limitation
   [PMID:21250939].
5. Caveat: no direct transport assay exists.
   [PMID:21250939 "Direct assays of Zrg17/Msc2 complex activity, e.g. 65Zn transport assays, have not yet been developed."]
   The transporter MF therefore rests on genetics, family membership, the retained
   site A, and the PAINT node, not on biochemistry.

### What is inferred, not established, in this species

- Golgi zinc import, Golgi cis cisterna membrane and cytoplasmic vesicle (IBA). These
  reflect the localization of Cis4 (cis-Golgi, PMID:18199682) and of mammalian
  ZnT5/ZnT7. In S. cerevisiae the evidence places the active pool in the ER. The
  inherited activity (zinc import into the early secretory pathway) is kept, with
  GO:0140209 zinc ion import into endoplasmic reticulum as the compartment term.
  GO:0140209 is a descendant of GO:0006829, GO:0055085 and GO:0006812 (checked with
  OLS hierarchicalAncestors). In GOA it is currently carried only by S. pombe zhf1
  (IMP/IDA) and by some IEA-annotated fungal proteins. The SGD row (zinc ion transport,
  IMP, 2004) predates the term, so the MODIFY is a refinement, not a reversal of a
  curator decision.
- Task context says that MSC2+ZRG17 coexpression complements cis4 (Fang 2008). The
  cached Fang et al. record (PMID:18199682) is abstract-only and the abstract does not
  mention this, so it was not used as evidence.

### Decisions summary

- Accepted: zinc ion transmembrane transporter activity (IBA/IEA/IMP), intracellular
  zinc ion homeostasis (IBA/IEA/IMP), ER membrane (IEA).
- MODIFY to GO:0140209: zinc ion transport (IEA, IMP), transmembrane transport (IEA,
  IMP), monoatomic cation transport (IEA), zinc ion import into Golgi lumen (IBA,
  lateral compartment correction).
- MODIFY to GO:0005789 ER membrane: ER (HDA, IDA), membrane (IEA).
- MODIFY to GO:0005385: monoatomic cation transmembrane transporter activity (IEA).
- MODIFY to GO:0006882: ARBA homeostasis terms.
- Non-core: zinc ion binding (RCA), nuclear membrane (IEA).
- Over-annotated: Golgi apparatus, Golgi cis cisterna membrane, cytoplasmic vesicle (IBA).
- REMOVE: four GO:0005515 rows (protein-binding policy; the Msc2-Zrg17 interaction
  itself is real).
