# Poz1 (SCHPO) - Research Notes

## Gene Summary
Poz1 (Protection of telomeres protein 1, UniProt O13852) is a core component of the fission yeast shelterin complex in *Schizosaccharomyces pombe*. It serves as a molecular bridge connecting the single-stranded and double-stranded telomeric DNA-binding protein subcomplexes.

## Key Facts

### Protein Function
- Poz1 is the functional analog of mammalian TIN2 in the shelterin complex [PMID:18535244 "Poz1 bridges Pot1-Tpz1 and Taz1-Rap1, thereby connecting the single-stranded and double-stranded telomeric DNA regions"]
- Negative regulator of telomerase and telomere length; deletion causes massive telomere elongation [PMID:18535244 "Poz1...regulate telomerase in positive and negative manners, respectively"]
- Poz1 functions redundantly with Ccq1 in telomere protection; simultaneous deletion causes severe telomere deprotection [PMID:18535244 "Ccq1 and Poz1...protect telomeres redundantly"]

### Structural Information
- Crystal structure solved at 2.3 Å in complex with Tpz1 and Rap1 binding motifs [PMID:29160296, PMID:29149597]
- Poz1 adopts a dimeric conformation [PMID:29160296 "the structure also reveals that Poz1 adopts a dimeric conformation"]
- Structurally resembles TRFH domains of Taz1 (S. pombe) and TRF1/TRF2 (human), belonging to the TRFH family [PMID:29160296 "Structural resemblance between Poz1 and the TRFH domains"]
- Poz1 uses two different binding surfaces for Tpz1 and Rap1 [PMID:29160296 "Poz1 employs two different binding surfaces to interact with Tpz1 and Rap1"]
- Shelterin bridge assembly is hierarchical: Tpz1 binding to Poz1 allosterically promotes Rap1 binding [PMID:29149597 "Tpz1 binding to Poz1 elicits structural changes in Poz1, allosterically promoting Rap1 binding to Poz1"]

### Interactions
- Interacts with Tpz1 (TPP1 homolog) via C-terminal region of Tpz1 (aa 486-508) [PMID:25330395]
- Interacts with Rap1 via Rap1 C-terminal region (aa 467-496) [PMID:29149597]
- Interacts with Pot1 indirectly through Tpz1 [PMID:18535244]
- Part of the shelterin complex (ComplexPortal: CPX-25757) [PMID:18535244 "part of the six-protein shelterin complex"]

### Telomere Regulation
- Loss of Tpz1-Poz1 interaction leads to increased Ccq1 Thr93 phosphorylation and telomerase recruitment [PMID:25330395 "loss of Poz1 from telomeres leads to increases in Ccq1 Thr93 phosphorylation and telomerase recruitment"]
- Tpz1-Poz1 and Tpz1-Ccq1 interactions are redundantly required for telomere protection [PMID:25330395]
- Poz1-Rap1 interaction is required for telomere length homeostasis and heterochromatin maintenance [PMID:29160296]
- Poz1 limits accumulation of Rad3(ATR) kinase at telomeres [PMID:25330395]

### Telomere Capping
- poz1Δ combined with ccq1Δ causes severe telomere deprotection similar to pot1Δ/tpz1Δ [PMID:18535244]
- Telomere capping function supported by IMP evidence [PMID:29160296] and IGI evidence [PMID:18535244]

### Localization
- Nucleus (HDA) [PMID:16823372]
- Chromosome, telomeric repeat region (IDA) [PMID:18535244]
- Shelterin complex (IDA, IPI) [PMID:18535244, PMID:29149597]
- Cytoplasm (IEA from UniProt subcellular location)

## 2026-09-01 — current GOA refresh

- Refreshed with `just fetch-gene SCHPO poz1 --force`; current GOA contains 21 rows.
- Accepted the new shelterin NAS assertion as redundant with direct IDA evidence and
  retained the new nuclear and cytoplasmic EXP localizations as non-core parent/secondary
  compartments.
- Revised the cytoplasm IEA from over-annotated to non-core because the refreshed GOA
  now supplies target-specific high-throughput experimental support (PMID:16823372).
- Removed the discontinued generic PMID:18535244 protein-binding tuple from
  `existing_annotations`; the underlying Tpz1/Rap1 bridging interactions remain captured
  by current rows and the synthesized molecular-adaptor function.
- Added subtelomeric heterochromatin formation (GO:0031509) to the core-process synthesis:
  loss or disruption of the Tpz1-Poz1 bridge causes a telomeric heterochromatin defect,
  and structural mutational analysis likewise links the bridge to heterochromatin
  maintenance [PMID:25330395 "loss of Poz1 from telomeres leads to increases in Ccq1
  Thr93 phosphorylation and telomerase recruitment, and telomeric heterochromatin
  formation defect"; PMID:29160296 "proper interactions between Tpz1, Poz1, and Rap1
  in the shelterin core complex are required for telomere length homeostasis and
  heterochromatin structure maintenance at telomeres"].
  These loss-of-function data establish involvement and requirement, but do not fully
  exclude an indirect contribution through the accompanying telomere-length defect.
- UniProt calls Poz1 a "Telomeric DNA-binding protein", but the reviewed experimental
  evidence establishes Poz1 principally as a protein-interaction bridge between Tpz1
  and Rap1; direct Poz1-DNA binding is not established here and should not be inferred
  from the descriptor alone [PMID:18535244 "Poz1 bridges Pot1-Tpz1 and Taz1-Rap1"].

### Telomere Organization
- Required for heterochromatin formation at telomeres [PMID:27253066, PMID:29160296]
- The tpz1-R81E/poz1Δ double mutant shows EST (Ever Shorter Telomere) phenotype [PMID:27253066]
