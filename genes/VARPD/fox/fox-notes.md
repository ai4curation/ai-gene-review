# Curatorial Notes for `fox` (`A0A0H2M811`, `VPARA_05580`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2M811` (`A0A0H2M811_VARPD`)
- **Gene Symbol:** `fox`
- **Locus Tag / EMBL CDS:** `VPARA_05580` / `KLN58443.1` on contig `JZWI01000003` (`RefSeq:WP_047783193.1`)
- **Protein Length:** 474 aa (50,739 Da); FAD-dependent oxidoreductase Fox (`EC=1.-.-.-`, `DE SubName: Full=FAD-dependent oxidoreductase Fox`).
- **Domain Architecture:**
  - N-terminal PCMH-type (`p`-cresol methylhydroxylase / vanillyl-alcohol oxidase family) FAD-binding domain at residues 36–217 (`PROSITE:PS51387` `FAD_PCMH`, `Pfam:PF01565` `FAD_binding_4`, `InterPro:IPR016166` `FAD-bd_PCMH`, `InterPro:IPR006094` `Oxid_FAD_bind_N`).
  - C-terminal FAD-linked oxidase cap/substrate-binding domain (`Pfam:PF02913` `FAD-oxidase_C`, `InterPro:IPR004113` `FAD-bd_oxidored_4_C`, `InterPro:IPR016164` `FAD-linked_Oxase-like_C`, `SUPFAM:SSF55103`).

## 2. Genomic & Pathway Context on Contig `JZWI01000003`
- *Variovorax paradoxus* strain TBEA6 was isolated for its ability to utilize the thioether 3,3'-thiodipropionic acid (TDP) as a sole source of carbon and energy (`PMID:19001372`).
- On genomic contig `JZWI01000003`, `fox` (`VPARA_05580`, `KLN58443.1`) is encoded two ORFs upstream of `mdo` (`VPARA_05600`, `KLN58445.1`, `UniProtKB:B9U5L8`, 3-mercaptopropionate dioxygenase) and ~13 ORFs from `acd` (`VPARA_05440`, `KLN58429.1`, `UniProtKB:B9U6P5`, 3-sulfinopropionyl-CoA desulfinase, curated in Tranche 1) and `act` (`VPARA_05450`, `KLN58430.1`, `UniProtKB:B9U6P4`, 3-sulfinopropionate CoA-transferase).
- Although `fox` is encoded near `mdo` (`VPARA_05600`), neither `PMID:19001372` nor `PMID:24317404` experimentally characterizes `fox` (`VPARA_05580`), and its physiological substrate and whether it participates directly in 3,3'-thiodipropionic acid or 2-hydroxy-acid catabolism remain unestablished.

## 3. Annotation Review Decisions
- `GO:0003824` (`catalytic activity`, IEA `GO_REF:0000002`, `enables`, `InterPro:IPR004113|InterPro:IPR016164`): **MODIFY** -> `GO:0016491` (`oxidoreductase activity`) — `fox` encodes an FAD-dependent oxidoreductase (`DE SubName: Full=FAD-dependent oxidoreductase Fox; EC=1.-.-.-`, `PROSITE:PS51387` `FAD_PCMH`, `Pfam:PF01565` `FAD_binding_4`, `Pfam:PF02913` `FAD-oxidase_C`); because its physiological substrate is uncharacterized, the broader `GO:0016491` is chosen rather than `GO:0016614`.
- `GO:0022904` (`respiratory electron transport chain`, IEA `GO_REF:0000118`, `involved_in`, `PANTHER:PTN008117839`): **REMOVE** — TreeGrafter over-propagation from distantly related membrane-associated respiratory D-lactate / D-2-hydroxyglutarate dehydrogenases (`PANTHER:PTHR43716`). In *V. paradoxus* TBEA6, `fox` (`VPARA_05580`) is a soluble cytoplasmic FAD-dependent oxidoreductase encoded two ORFs upstream of `mdo` (`VPARA_05600`), not a respiratory electron transport chain complex subunit.
- `GO:0050660` (`flavin adenine dinucleotide binding`, IEA `GO_REF:0000002`, `enables`): **TOO_GENERAL** — parent of `GO:0071949` (`FAD binding`) already accepted in this review.
- `GO:0071949` (`FAD binding`, IEA `GO_REF:0000002`, `enables`, `InterPro:IPR016166`): **ACCEPT** — core cofactor-binding activity (`PROSITE:PS51387` `FAD_PCMH` domain at `36..217`).
- `GO:0016491` (`oxidoreductase activity`, IC from `file:VARPD/fox/fox-uniprot.txt`): **NEW** — asserted alongside the modified `GO:0003824` row.
- `GO:0005829` (`cytosol`, IC from `file:VARPD/fox/fox-uniprot.txt`): **NEW** — soluble 474-aa cytoplasmic enzyme lacking signal peptides or transmembrane helices.
