# Curation Notes: Bacteriophage T4 gene 57 (gp57 / gp57A; UniProt P04532)

## Identity and Nomenclature
- **Gene symbol**: `57` (synonym: `57A`)
- **Protein**: Tail fiber assembly helper protein gp57A (also called gp57 or p57; 80 aa precursor / 79 aa mature after N-terminal Met removal, ~8.6 kDa)
- **UniProt**: `P04532` (`GP57_BPT4`)
- **Taxon**: `NCBITaxon:10665` (*Tequatrovirus T4*)

## Biological Function Summary
1. **Nonstructural molecular chaperone essential for folding and trimerization of long and short tail fibers**:
   - Gene 57 (57A) encodes gp57A, a small (79-residue mature polypeptide), highly alpha-helical (~94% alpha-helix by CD), strongly acidic (net charge -9; completely lacking Phe, Trp, Tyr, His, Pro, and Cys) nonstructural molecular chaperone that acts in the infected *Escherichia coli* cytoplasm and is absent from the mature virion (Hashemolhosseini et al. 1996, PubMed 8892827; Matsui et al. 1997, PubMed 9068627).
   - Biophysical studies (analytical ultracentrifugation and cross-linking) show that gp57A undergoes fast reversible self-association between homotrimers, homohexamers, and higher-order oligomers in solution, and forms elongated paracrystalline alpha-helical bundles when overproduced in *E. coli* (Hashemolhosseini et al. 1996, PubMed 8892827; Matsui et al. 1997, PubMed 9068627; Ali et al. 2003, PubMed 14507723).
2. **Three distinct fibrous substrate targets (gp12, gp34, and gp37/gp36)**:
   - Genetic and biochemical studies establish that gp57A is required for the folding and trimeric assembly of both short and long tail fiber structural proteins (Ward & Dickson 1971, PubMed 4944598; Herrmann & Wood 1981, PubMed 7038383; Leiman et al. 2010, PubMed 21138586):
     - **gp12 (short tail fiber)**: gp57A binds nascent gp12 to promote native homotrimer formation, preventing membrane/debris aggregation and dissociating low-temperature gp12 aggregates back into soluble trimers (Matsui et al. 1997, PubMed 9068627).
     - **gp34 (proximal long tail fiber)**: gp57A is required for folding and oligomerization of the 1289-residue gp34 subunit into the proximal half-fiber homotrimer.
     - **gp37 and gp36 (distal long tail fiber)**: gp57A acts together with the gp38 chaperone to fold and trimerize gp37 into the distal half-fiber shaft/tip (Bartual et al. 2010, PubMed 19913618) and assists gp36 assembly onto the N-terminus of the gp37 trimer.

## Review of Existing GOA Annotations
- `GO:0098004` (`virus tail fiber assembly`, IEA `GO_REF:0000043` and IDA `PMID:8892827`): **ACCEPT** (both rows). Directly supported by genetic and biochemical characterization demonstrating that gp57A is required for assembling the short (gp12) and long (gp34, gp36, gp37) tail fibers (Hashemolhosseini et al. 1996, PubMed 8892827).
- `GO:0098003` (`viral tail assembly`, IEA `GO_REF:0000043`): **MODIFY** -> `GO:0098004` (`virus tail fiber assembly`). `GO:0098003` is a broader parent term of `GO:0098004`, which is already present on the record.
- **New annotations (`NEW`)**:
  - `GO:0044183` (`protein folding chaperone`): gp57A is an experimentally characterized molecular chaperone that prevents aggregation and promotes trimeric folding of fibrous tail proteins (gp12, gp34, gp37).
  - `GO:0030430` (`host cell cytoplasm`): gp57A is a nonstructural chaperone that functions inside the host bacterial cytoplasm during phage morphogenesis and is not incorporated into the mature virion.
