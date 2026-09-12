# HMBS (P08397) review notes

Human hydroxymethylbilane synthase / porphobilinogen deaminase (PBGD). EC 2.5.1.61.
Deep research: falcon out of credits (HTTP 402); no `-deep-research-falcon.md` generated.
Review grounded in `HMBS-uniprot.txt`, `HMBS-goa.tsv`, cached `publications/PMID_*.md`,
and cached Reactome entries R-HSA-189406 / R-HSA-189451.

## Core function

- Catalyses the **third step of heme biosynthesis**: the head-to-tail polymerization
  (sequential condensation) of **four molecules of porphobilinogen (PBG)** into the
  linear tetrapyrrole **hydroxymethylbilane (HMB)**, also called **preuroporphyrinogen**,
  releasing 4 NH4+. RHEA:13185; EC 2.5.1.61.
  - UniProt FUNCTION: "As part of the heme biosynthetic pathway, catalyzes the
    sequential polymerization of four molecules of porphobilinogen to form
    hydroxymethylbilane, also known as preuroporphyrinogen".
  - [PMID:18936296 abstract, "porphobilinogen deaminase (PBGD), which catalyzes the sequential condensation of 4 molecules of porphobilinogen to yield preuroporphyrinogen"]
  - [PMID:23815679 full text, "The enzyme catalyses the assembly of four PBG molecules into the linear precursor of uroporphyrinogen III, HMB (hydroxymethylbilane, also called preuroporphyrinogen)"]
- Uses a self-derived **dipyrromethane (DPM) cofactor**, covalently bound at Cys261,
  that acts as a **primer** onto which the four PBG units are sequentially added; the
  cofactor is not turned over and HMBS leaves as a holoenzyme.
  - UniProt: "Catalysis begins with the assembly of the dipyrromethane cofactor by the
    apoenzyme ... The covalently linked cofactor acts as a primer, around which the
    tetrapyrrole product is assembled".
  - COFACTOR: "Name=dipyrromethane ... Binds 1 dipyrromethane group covalently."
  - [PMID:18936296 abstract, "a dipyrromethane cofactor molecule covalently linked to C261"]
- **Cytosol / cytoplasm** localization (SUBCELLULAR LOCATION: Cytoplasm, cytosol).
  Reactome R-HSA-189406: "Cytosolic porphobilinogen deaminase catalyzes the
  polymerization of four molecules of porphobilinogen (PBG) to generate
  hydroxymethylbilane (HMB)".
- Monomer (SUBUNIT: Monomer). Two isoforms via alternative transcription/splicing:
  ubiquitous housekeeping (isoform 1) and erythroid-specific (isoform 2).

## Disease

- **Acute intermittent porphyria (AIP)** [MIM:176000], autosomal dominant hepatic
  porphyria — the most common acute hepatic porphyria. >385 mutations reported.
  Also recessive ENCEP / LENCEP (porphyria-related [leuko]encephalopathy).

## GOA MF term

- GOA carries **GO:0004418 hydroxymethylbilane synthase activity** (multiple lines:
  IBA, IEA/EC:2.5.1.61, TAS Reactome, EXP, IDA, TAS). Confirmed current label in go.db.

## Annotation notes / decisions

- **GO:0004418 (all lines): ACCEPT.** Well-supported experimental MF (IDA/EXP: PMID:18936296,
  18004775, 19138865, 23815679; TAS Reactome + PMID:2025226; IBA; IEA EC mapping). Core.
- **GO:0006783 heme biosynthetic process (IBA, TAS Reactome, IDA PMID:18936296, IC): ACCEPT.**
  Core BP. Third step of heme synthesis.
- **GO:0005829 cytosol (IEA SubCell, ISS, TAS Reactome): ACCEPT.** Core location.
- **GO:0005737 cytoplasm (IBA is_active_in): ACCEPT** but broader than cytosol; keep (parent of cytosol).
- **GO:0006779 porphyrin-containing compound biosynthetic process (IEA ARBA): ACCEPT** —
  correct but more general than heme biosynthesis.
- **GO:0033014 tetrapyrrole biosynthetic process (IEA InterPro): ACCEPT** — correct, more general.
- **GO:0006785 heme B biosynthetic process (IDA PMID:18004775): KEEP_AS_NON_CORE / MODIFY consideration.**
  HMBS makes HMB, a precursor upstream of both heme b and other tetrapyrroles; "heme B"
  is overly specific for HMBS's direct step. Mark as over-annotated relative to the generic
  heme biosynthetic process. IDA reference PMID:18004775 is titled for UROS but is annotated
  to HMBS for the shared heme-biosynthesis pathway; do not REMOVE (full text not verifiable,
  experimental). Use MARK_AS_OVER_ANNOTATED (heme B is more specific than the reaction warrants).
- **GO:0005515 protein binding (IPI x2, PMID:32296183 PICK1/Q9NRD5; PMID:32814053 HTT/P42858):
  MARK_AS_OVER_ANNOTATED.** Bare "protein binding" is uninformative; both are high-throughput
  interactome screens (Y2H reference interactome; neurodegenerative-disease interactome).
  Per policy, do NOT REMOVE bare protein-binding IPIs — mark as over-annotated.
