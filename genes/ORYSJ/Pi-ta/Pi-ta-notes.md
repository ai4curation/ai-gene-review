# Pi-ta (ORYSJ, UniProt Q84UB1) curation notes

## 2026-10-10 Identity of the UniProt record

- Q84UB1 is an unreviewed TrEMBL entry (928 aa) translated from EMBL AY196754
  (AAO45178.1), submitted by Jia, Bryan, Farrall & Valent, cv. **Tsuyake**
  (japonica). The GenBank product name is lower-case "pi-ta protein".
- Residue 918 of Q84UB1 is **Ser** (C-terminal `...LPWLLSLPSMHLQPDLMIV`). The
  resistant Pi-ta allele from Bryan et al. 2000 is Q9AY26 (EMBL AF207842,
  taxon 4530 *Oryza sativa*), which has **Ala918** (`...LPWLLSLPAMHLQPDLMIV`).
  Checked by fetching both FASTA sequences from UniProt REST.
- So Q84UB1 is the product of a **susceptible pi-ta(-) allele**. Bryan et al.:
  [PMID:11090207 "Susceptible rice varieties contain pi-ta(-) alleles encoding
  predicted proteins that share a single amino acid difference relative to the
  Pi-ta resistance protein: serine instead of alanine at position 918."]
- Gramene attached the same IMP `defense response` (PMID:11090207) and the same
  IEA set to both Q84UB1 and Q9AY26. GO annotation is gene-level, so this is not
  a mistake as such, but it means the reviewed record is the allele that the
  original paper showed does not trigger resistance.
- Locus: LOC_Os12g18360 (per deep research; PTR is LOC_Os12g18729, a separate
  ARM-repeat gene).

## Domain architecture (UniProt / InterPro)

- Rx_N coiled-coil (13-114), NB-ARC (214-385), winged helix (477-548), two
  R13L4/SHOC2-like LRR blocks (597-857). CC-NB-LRR (CNL). PANTHER
  PTHR23155:SF1094.
- Walker A `GSGGVGKTT` (P-loop, ~236-244), kinase-2 `FIIIEDLW`, GLPL `GGLPLAI`
  are present in the sequence, so the NB-ARC nucleotide pocket looks intact.
  No nucleotide binding has been measured for Pi-ta.

## Historical model (2000-2004)

- Map-based cloning; [PMID:11090207 "Pi-ta encodes a predicted 928-amino acid
  cytoplasmic receptor with a centrally localized nucleotide binding site."]
- Transient co-expression assay: [PMID:11090207 "Transient expression in rice
  cells of a Pi-ta(+) R gene together with AVR-Pita(+) induces a resistance
  response."] and the Ser918 allele does not.
- Direct binding: [PMID:10921881 "AVR-Pita 176 protein is shown to bind
  specifically to the LRD of the Pi-ta protein, both in the yeast two-hybrid
  system and in an in vitro binding assay."] and [PMID:10921881 "Consistent with
  the results obtained from the yeast two-hybrid system, the susceptible LRD
  A918S protein did not bind to AVR-Pita 176 under the same conditions (Figure 6
  C)."]
- Localisation was never measured; "putative cytoplasmic" is inferred from
  architecture [PMID:10921881 "Pi-ta is a single copy gene encoding a putative
  cytoplasmic protein of 928 amino acids"].
- US germplasm association study [PMID:18943978] (abstract only): Pi-ta marker
  co-segregates with resistance to races IB-49 and IC-17. Linkage only; does not
  separate Pi-ta from linked Ptr.

## Ptr and the 2024 revision

- Zhao et al. 2018 cloned Ptr, an ARM-repeat protein next to Pi-ta:
  [PMID:29795191 "These data indicate that Ptr is required for a
  broader-spectrum of blast resistance than Pi-ta alone."] At the time Ptr was
  framed as acting together with Pi-ta.
- Xiao et al. 2024 (abstract only in cache): [PMID:38834685 "we found that
  AVR-Pita recognition relies solely on Ptr and that the NLR Pi-ta has no role
  in it, indicating that it is not the Pi-ta resistance gene."] PtrB confers
  "Pi-ta" resistance, PtrA confers Pi-ta2 resistance. Deep research reports that
  they could not reproduce the yeast two-hybrid interaction and that four
  independent NLR pi-ta mutants in IR64 stayed resistant
  [file:ORYSJ/Pi-ta/Pi-ta-deep-research-falcon.md].
- Contrary data: He et al. 2022 (full text) knocked out the Fuhui 2663 allele:
  [PMID:36050368 "Using CRISPR/Cas9 genome editing technology, we knocked out
  Pita-Fuhui2663 in Fuhui 2663 and found that the knockout mutants lost its
  resistance, indicating that Pita-Fuhui2663 confers blast resistance."] Only
  two lines, one isolate (KJ201), AVR status of KJ201 not tested, and no
  complementation reported. Off-target edits or effects on the linked Ptr
  region were not excluded.

## Assessment

- The NLR's role in AVR-Pita recognition is directly contradicted by the
  locus-resolved 2024 genetics. Any defense role for this NLR now rests on one
  small knockout study. The physiological function of the NLR is therefore
  **unresolved**.
- ADP binding (NB-ARC, intact P-loop) is the only activity that can be inferred
  with confidence, and it is a family-level structural inference.
- `defense response to bacterium` (ARBA): no bacterial data for Pi-ta at all.
  Remove.
- `plant-type hypersensitive response` and `innate immune
  response-activating signaling pathway` (ARBA): generic NLR propagation; the
  only Pi-ta-specific support (Bryan 2000 transient assay, Jia 2000 binding) is
  disputed. Over-annotated.
- IMP `defense response` (Bryan 2000): the curator read the full text; the
  claim is now disputed by PMID:38834685 but partly supported by PMID:36050368.
  Initially marked UNDECIDED; changed to KEEP_AS_NON_CORE so that it agrees
  with the IEA row for the same term. It is not removed (deference to the
  curator plus the 2022 knockout) and not treated as core.
- No NEW terms: no Pi-ta-specific activity or location has been measured.

## Project question relevance (PLANT_FUNGAL_INTERACTIONS)

- Q3 necessity vs participation: here even necessity is in doubt. The
  "Pi-ta" resistance phenotype maps to Ptr, so a fungal-defense annotation on
  the NLR may be attached to the wrong gene of the chr12 cluster.
- Q5 sensor/helper NLR pairs: Pi-ta is not part of a known NLR pair. Whether
  PTR and the Pi-ta NLR interact at all is not known.
