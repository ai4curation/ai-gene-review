# OSTC (DC2) review notes

UniProt: Q9NRP0 (OSTC_HUMAN). HGNC:24448. Gene names/synonyms: OSTC, DC2, HDCMD45P,
HSPC307; "Hydrophobic protein HSF-28". 149 aa, ~16.8 kDa. Chromosome 4.

## Summary of function

OSTC (also called DC2) is a small (149 aa) multi-pass ER membrane protein that is a
**non-catalytic accessory subunit** of the oligosaccharyltransferase (OST) complex,
specifically the **STT3A-containing OST-A complex** that carries out **co-translational
N-linked glycosylation**. It is NOT the catalytic subunit (STT3A is), and it does not
possess glycotransferase activity on its own.

- UniProt FUNCTION: "Subunit of STT3A-containing oligosaccharyl transferase (OST-A)
  complex that catalyzes the initial transfer of a defined glycan (Glc(3)Man(9)GlcNAc(2)
  in eukaryotes) from the lipid carrier dolichol-pyrophosphate to an asparagine residue
  within an Asn-X-Ser/Thr consensus motif in nascent polypeptide chains, the first step
  in protein N-glycosylation" [file:human/OSTC/OSTC-uniprot.txt].
- UniProt: "N-glycosylation occurs cotranslationally and the complex associates with the
  Sec61 complex at the channel-forming translocon complex" [file:human/OSTC/OSTC-uniprot.txt].
- UniProt: "Within the OST-A complex, acts as an adapter that anchors the OST-A complex to
  the Sec61 complex (PubMed:28860277)" [file:human/OSTC/OSTC-uniprot.txt].
- UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum ... Membrane; Multi-pass membrane
  protein" [file:human/OSTC/OSTC-uniprot.txt]. Topology (predicted): 3 TM helices
  (33-53, 84-104, 118-138); N- and C-termini cytoplasmic/luminal alternating.
- UniProt SIMILARITY: "Belongs to the OSTC family" [file:human/OSTC/OSTC-uniprot.txt].

## Key primary evidence

- **Shibatani et al. 2005 (PMID:15835887)** — proteomic analysis of mammalian OST first
  identified DC2 as a novel OST subunit: "identified a 17 kDa protein as DC2 which is
  weakly homologous to the C-terminal half of yeast Ost3p and Ost6p" and "Our results
  identify two potential new subunits of mammalian OST" (DC2 and KCP2). Basis for the
  IC/IDA annotations to OST complex (GO:0008250) and, by inference, contributes_to the
  complex glycotransferase activity (GO:0004579).
- **Shrimal, Cherepanova & Gilmore 2017 (PMID:28860277)** — full text available. Shows
  DC2/OSTC (with KCP2) mediates the OST-A–to–translocon interaction. "loss of DC2 causes
  a defect in co-translational N-linked glycosylation of proteins that mimics an STT3A-/-
  phenotype." Critically for the non-catalytic/adapter model: "DC2 (OSTC gene) and KCP2,
  two small membrane proteins, were initially detected as novel OST subunits in
  translocation channel–associated OST complexes" and "STT3A complexes that lack DC2 or
  KCP2 are enzymatically active when assayed using a synthetic peptide acceptor but do not
  form stable complexes with the Sec61 complex" — i.e., OSTC is an adapter, not the
  catalyst. Supports GO:0030674 (adaptor), GO:0006487 (N-glyc), GO:0008250 (OST complex).
- **Ramírez, Kowal & Locher 2019 (PMID:31831667)** — cryo-EM of human OST-A and OST-B.
  "structural differences in the catalytic subunits STT3A and STT3B facilitate contacts
  to distinct OST subunits, DC2 in OST-A and MAGT1 in OST-B." Establishes OSTC/DC2 as a
  defining component of the OST-A complex (GO:0160226). PDB 6S7O; chain H = OSTC.
- **Gemmer et al. 2023 (PMID:36697828)** — cryo-EM/ET of the ER translocon; OSTC modeled
  within the SEC61–OSTA–TRAP translocon ("the luminal OSTC β-hairpin"). Supports
  GO:0160226 membership at the SEC61 interface. PDB 8B6L chain J = OSTC.
- **Lampson et al. 2024 (PMID:38670073)** — CRISPR + cryo-EM of STT3A-containing OST;
  OSTC modeled as an OST-A subunit (PDB 8PN9 chain H = OSTC). Supports GO:0160226.
- **Ma et al. 2024 (PMID:39509507)** — "OST-A, which contains unique subunits (OSTC,
  KRTCAP2) that anchor it to the SEC61 protein channel (6), functions co-translationally"
  — independent corroboration of OSTC's anchor role in OST-A. (Cited in UniProt; added to
  references as supporting.)
- **Wilson et al. 2011 (PMID:21768116)** — DC2/OSTC and KCP2 as OST subunits; ER
  localization (IDA/EXP). Also reports a substrate-specific effect on APP processing and
  gamma-secretase (PSEN1/NCSTN interaction). The APP/gamma-secretase role is a specific,
  non-core downstream/substrate effect, not OSTC's core molecular function. Abstract
  explicitly states DC2/KCP2 "are not core components required for N-glycosylation and OST
  activity per se" — consistent with the non-catalytic-subunit model.

## Curation decisions (high level)

- **Core CC**: OST-A complex (GO:0160226, specific) and OST complex (GO:0008250, parent) —
  both ACCEPT (experimental IDA to GO:0160226; IBA/IDA/NAS to GO:0008250). Model
  `in_complex` with GO:0160226 (OST-A) in core_functions.
- **Core MF**: contributes_to GO:0004579 (dolichyl-diphosphooligosaccharide-protein
  glycotransferase activity) — the complex-level catalytic activity OSTC contributes to
  but does not independently enable. ACCEPT the IC. GO:0030674 (protein-macromolecule
  adaptor activity, IDA/IBA) captures the OSTC-specific adapter/anchor function — ACCEPT;
  use as the subunit-specific `molecular_function`.
- **Core BP**: GO:0006487 (protein N-linked glycosylation) — ACCEPT (IDA/IBA/NAS).
- **Core CC (location)**: GO:0005789 (ER membrane, IDA/TAS/NAS) ACCEPT; GO:0005783 (ER,
  IEA/EXP) ACCEPT as broader parent. GO:0016020 (membrane, IEA) is an uninformative
  parent → MARK_AS_OVER_ANNOTATED (redundant with ER membrane).
- **GO:0009101 (glycoprotein biosynthetic process, IEA/InterPro)** — a broader parent of
  the more precise N-linked glycosylation term; KEEP_AS_NON_CORE (subsumed by GO:0006487).
- **GO:0005515 (protein binding) IPI ×2** (PMID:25416956 vs EDA; PMID:32296183 vs TUSC5) —
  uninformative bare "protein binding" from high-throughput binary interactome screens;
  EDA and TUSC5 are not established functional partners of OSTC. Per policy, never REMOVE a
  bare-protein-binding IPI → MARK_AS_OVER_ANNOTATED.
- Multiple Reactome TAS annotations to GO:0005789 (ER membrane) across specific
  glycosylation reactions — all correct core location; ACCEPT (the first) /
  KEEP_AS_NON_CORE (substrate-specific viral/CDH1/PD-L1 reactions are the same location via
  different reactions; keep to avoid inflating core).
</content>
</invoke>
