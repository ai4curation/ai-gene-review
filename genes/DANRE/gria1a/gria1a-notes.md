# gria1a notes (Danio rerio, glutamate receptor, ionotropic, AMPA 1a; UniProt Q71E65)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 4, random TGD_tree sample)

**Deep research:** not available (Edison/Falcon 402 Payment Required; OpenAI key invalid). Not
attempted, per instructions. Literature searched by hand in Europe PMC (`(gria1a OR gria1b) AND zebrafish`,
`"gria1b"`, `"gria1a" AND (mutant OR knockout OR morpholino)`, `AUTH:"Hoppmann V" AMPA`,
`TITLE:"AMPA" AND TITLE:zebrafish`, `zebrafish AND ("GluR1" OR "GluA1")`) and by following ZFIN
expression publications. Pair analysis in `gria1a-bioinformatics/RESULTS.md`; paralog notes in
`../gria1b/gria1b-notes.md`.

Accession Q71E65 (TrEMBL, EMBL AAQ08954 "AMPA receptor subunit GluR1A", 914 aa),
ZFIN:ZDB-GENE-020125-1, Ensembl ENSDARG00000021352, chr14. 15 GOA rows (IBA and IEA only), identical
term by term to gria1b.

### Origin
- PANTHER TGD_tree (Neopterygii|Teleostei), 1:1, one gar co-ortholog, two medaka co-orthologs.
  Ensembl Compara duplication node Osteoglossocephalai; one gar ortholog for both copies; one-to-one
  medaka orthologs for each copy (so medaka kept both).
- [PMID:18224707 "Whereas mammals have four subunit genes, Gria1-4, zebrafish has retained a duplicated set of eight genes named gria1-4a and b."]
- Synteny (RESULTS.md): no teleost-level paralogue pair within 1.5 Mb of both copies; several
  chromosome-level links (chr14 <-> chr21).

### Protein (RESULTS.md)
- gria1a vs gria1b 82.5% identical; gria1a 88.3% identical to gar GRIA1 and gria1b 81.7%.
- Glutamate-binding residues, the pore loop and M2-M3 segment (FGIFNSLWFSLGAFMQQGCDISPRSLSG,
  identical to human and gar) and both palmitoylation cysteines kept in both copies.
- Relative rate vs gar: gria1b has significantly more unique changes (86 vs 34).
- C-terminal tail: gria1a keeps the serines at human S849/S863 (mature S831/S845); gria1b has I at
  S849 and no aligned serine at S863. Mammalian background:
  [PMID:20716669 "Ser831 is a substrate for both CaMKII- and PKC-dependent phosphorylation, whereas Ser845 is a substrate for PKA phosphorylation"]
- PDZ-binding C-terminus: human ATGL; gar ATGM; gria1a ASGM; gria1b TTGM. The L->M change predates
  the TGD (present in gar).
- [PMID:16887104 "Many but not all of the known mammalian protein-protein interaction motifs are preserved in the C-terminal domains (CTD) of zebrafish AMPARs."]

### Mammalian GRIA1 background
- [PMID:2166337 "Functional expression of the cDNAs in cultured mammalian cells generated receptors displaying alpha-amino-3-hydroxy-5-methyl-4-isoxazole propionic acid (AMPA)-selective binding pharmacology (AMPA = quisqualate greater than glutamate greater than kainate) as well as cation channels gated by glutamate, AMPA, and kainate and blocked by 6,7-dinitroquinoxaline-2,3-dione (CNQX)."]
- [PMID:10364547 "In adult GluR-A-/- mice, associative long-term potentiation (LTP) was absent in CA3 to CA1 synapses, but spatial learning in the water maze was not impaired."]

### Expression
- Hoppmann et al. 2008 (abstract only in cache; ZFIN curated the in situ data):
  [PMID:18224707 "As a general rule, each pair of duplicated gria genes is differentially expressed, indicating subfunctionalization of AMPA receptor subunit expression in the teleost lineage."]
  ZFIN terms from this paper (24-72 hpf): gria1a-only telencephalon (dorsal and ventral), dorsal
  thalamus, spinal cord, rhombomeres, retinal ganglion cells; gria1b-only otic vesicle; 18 terms
  shared (olfactory bulb, habenula, hypothalamus, thalamus, tegmentum, optic tectum, medulla,
  retinal layers, motor and sensory neurons, spinal interneurons, early clusters).
- Maternal transcripts of all AMPAR genes by RT-PCR:
  [PMID:16887104 "Transcripts of all AMPAR genes are detected at the time of fertilization, suggesting maternal transcriptions of zebrafish AMPAR genes."]
- E-ERAD-475: gria1a 12-14 TPM and gria1b 5-6 TPM in larvae (gria1a about 2-3 times higher).
- Bgee: shared brain and retina; gria1b adds ovarian follicle, spleen, gill, testis; gar GRIA1 brain,
  eye, larva, ovary, bone, embryo.
- Forebrain: [PMID:30929901 "gria1a: forebrain showed in situ and activity signal."]
- Tectum: [PMID:35221915 "Postsynaptic markers for glutamatergic transmission include genes such as grin1a and gria1a, which build NMDA and AMPA receptors, (respectively), present only on the postsynaptic cell membrane."]
- Sinoatrial ring: [PMID:34600492 "neural crest genes (foxd3,gria1a, smarca4a, and sox10)"]

### Function
- Only mutant data: the schizophrenia-gene screen (Thyme et al. 2019) mutated both copies:
  [PMID:30929901 "If the human gene of interest was duplicated in zebrafish, homozygous mutations were generated for both orthologs."]
  and gria1 mutants had a pallium activity phenotype:
  [PMID:30929901 "mutants with signals mainly in the pallium (label 2) were all unambiguously associated, including bcl11b, gria1, znf536, clcn3, and cacna1c."]
  The text does not say which copy (or the double) produced it; the per-ortholog data are in a
  supplementary heatmap that I could not read. No other loss-of-function data for either copy.

### Annotation decisions
- MF (AMPA receptor activity, transmitter-gated channel involved in postsynaptic potential,
  ligand-gated channel, transmitter-gated channel): ACCEPT. Complex, PSD membrane, postsynaptic
  membrane, plasma membrane, membrane: ACCEPT. Glutamatergic transmission, iGluR signalling,
  regulation of postsynaptic membrane potential, ion transmembrane transport: ACCEPT.
- Dendritic spine (IBA): KEEP_AS_NON_CORE (mammalian donors; no zebrafish data).
- Modulation of chemical synaptic transmission (IBA): KEEP_AS_NON_CORE (mammalian GluA1 plasticity
  role; untested in fish).
- No NEW annotations.
