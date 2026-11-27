# GNG5B (A0A804HLA8) versus parent GNG5 (P63218)

Scripts (run with `uv run`; inputs are fetched live, nothing is hardcoded):

- `compare_to_parent.py A0A804HLA8 P63218 ENST00000697560` -> `results.txt`
- `compare_to_parent.py A0A804HLA8 P63218 ENSG00000133136` -> `ensembl_gene.txt` (only
  the transcript list is used; the whole-gene-span ORF scan is irrelevant for a 94-kb gene)
- `gbeta_interface.py` (default PDB 1GP2, beta chain B, gamma chain G, 4.0 A) ->
  `gbeta_interface.txt`
- `gtex_expression.py ENSG00000133136 ENSG00000174021` -> `gtex.txt`

## Locus and transcript

- HGNC (REST, 2026-10-04): locus_type `gene with protein product`, Xq23. Its previous
  symbol GNG5P2 shows it was once classed as a pseudogene. MANE Select is
  ENST00000697560.1 / NM_001396022.1.
- Ensembl ENSG00000133136: biotype protein_coding with two protein_coding transcripts.
  ENST00000372054 has 3 exons, and ENST00000697560 (MANE) is single-exon (520 nt). Both
  encode the same 68-aa protein. The single-exon ORF translates to exactly the UniProt
  sequence.
- GTEx v8 still lists the gene under GENCODE v26 as a processed pseudogene (GNG5P2), with
  max median 0.291 TPM (Pituitary), and every other tissue is lower. Parent GNG5: max median
  about 275 TPM. Short reads from a 94%-identical retrocopy may be multi-mapped or assigned
  to the parent, so these values are approximate.
- UniProt: PE 3 (Inferred from homology). No peptide-level evidence is cited.

## Sequence comparison

- 64/68 identical (94.1%), ungapped. Substitutions GNG5 -> GNG5B: S4F, M10T, R18Q, R25S.
- C-terminal CaaX box **CSFL retained**. C65, the geranylgeranylated and carboxymethylated
  cysteine in the parent and in the UniProt features of both entries, is retained. The
  propeptide 66-68 (SFL) is identical.
- N-terminal S2 (N-acetylserine and phosphoserine in GNG5) is retained.

## Gbeta interface (structure-based)

In the Gi heterotrimer structure 1GP2, 36 gamma2 residues lie within 4.0 A of Gbeta1.
All 36 map onto GNG5. **33 of the 36 are identical in GNG5B**. The 3 that differ are
M10T, R18Q and R25S, all in the N-terminal helix that forms the coiled coil with Gbeta's
N-terminus. R18 of GNG5 corresponds to K20 in gamma2, so the charged residue at that site
already varies within the family. R25 corresponds to gamma2 R27. Neither of these checks
tests binding, so whether these substitutions change Gbeta affinity or Gbeta-subtype
selectivity is unknown.

## Interpretation

GNG5B has a complete Ggamma fold, the prenylation signal, and an almost unchanged Gbeta
interface. Nothing in the sequence argues for loss of function. Its existence as a
protein is not demonstrated, though. It is a retrocopy with low transcript levels, PE 3,
no peptide evidence that we found, and no literature. Its inherited annotations are
structurally plausible but untested on this locus.
