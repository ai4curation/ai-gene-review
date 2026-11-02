# smad3a / smad3b protein and expression comparison

Script: `compare_smad3.py` (run with
`uv run python genes/DANRE/smad3a/smad3a-bioinformatics/compare_smad3.py > genes/DANRE/smad3a/smad3a-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Global alignments: Biopython PairwiseAligner,
BLOSUM62, gap open -10, extend -0.5. Zebrafish sequences come from the cached UniProt
records (Q8AY15 = smad3a, Q8AY16 = smad3b). Human SMAD3 (P84022) sequence and features,
and spotted gar SMAD-family proteins, are fetched from UniProt REST. Expression calls come
from the Bgee REST API and the ZFIN `wildtype-expression_fish.txt` download.

## Protein

| Comparison | Identity | Columns |
|---|---|---|
| smad3a vs smad3b | 94.1% | 425 |
| smad3a vs human SMAD3 | 96.9% | 426 |
| smad3b vs human SMAD3 | 93.0% | 426 |
| smad3a vs gar SMAD3 (W5N932) | 96.3% | 427 |
| smad3b vs gar SMAD3 (W5N932) | 93.9% | 427 |

- **Gar SMAD3.** The gar entries have no gene names. W5N932 (427 aa) is the gar SMAD-family
  protein most identical to human SMAD3 (96.7%); the next best, W5N3S5 (89.7%), is labelled
  SMAD2. W5N932 is used as the unduplicated outgroup.
- **By region** (human SMAD3 coordinates): MH1 (10-136) smad3a 96.9%, smad3b 93.7%;
  MH2 (232-425) smad3a 99.5%, smad3b 97.9%; linker (137-231) smad3a 92.7%, smad3b 82.3%.
  Between the paralogs, 94.5% of MH1 positions, 98.5% of MH2 positions and 84.2% of linker
  positions are identical. smad3b has a 2-residue deletion in the linker (human 157-158).
- **Which copy diverged.** smad3a is as close to gar SMAD3 as human SMAD3 is (about 96-97%
  identity each way). smad3b carries most of the pair's differences, mainly in the linker.
  This fits the longer smad3b branch reported in teleost trees (PMID:27703851).
- **Functional positions of human SMAD3** (UniProt P84022 features). Conserved in both
  copies and in gar: the four Zn-binding residues (C64, C109, C121, H126); K40 (trimerization)
  and K41 (DNA/JUN interaction); the linker phosphosites T8, T179, S204, S208 and S213; K378
  (acetylation); S416; and the C-terminal receptor-phosphorylated SSVS motif (S422, S423,
  S425; last six residues RCSSVS in all four proteins).
- **One annotated site differs:** human S418 (phosphoserine by CK1) is S in smad3a and gar
  but **N in smad3b**. Human SMAD3 S418 mutants alter constitutive activity (UniProt P84022
  mutagenesis annotations, both "increased constitutive activity" and "decreased activity"
  entries exist). The effect in zebrafish is untested.
- 25 human-SMAD3 positions differ between the paralogs; 18 of them are in the linker
  (human 137-231). In the MH1 DNA-binding domain the differences are conservative
  (D/E, N/D, V/I, R/K, M/I/V, L/M) except M115T.

## Expression (Bgee, anatomical entities, all data types)

- smad3a has two Ensembl gene ids: ENSDARG00000036096 (chromosome 7) and
  ENSDARG00000117146 (alternate contig ALT_CTG7_1_28, i.e. an alternate-haplotype copy of the
  same locus). Their calls are merged by taking the higher score: 30 expressed entities.
  smad3b (ENSDARG00000010207, chromosome 18): 36.
- 19 entities are shared. The gene-specific entities mostly reflect which studies were
  done, not demonstrated absence: the smad3b-only brain subregions (epithalamus, pretectal
  region, midbrain tegmentum, rhombomere, spinal cord) come from one in situ study of smad3b
  (ZFIN ZDB-PUB-020716-15, Pogoda and Meyer 2002, PMID:12112463); smad3a has no comparable
  anatomical in situ survey in ZFIN.
- Highest-scoring entities: smad3a presomitic mesoderm 97.0, tail bud paraxial mesoderm
  95.6, somite 95.4, caudal fin 93.5, retina 92.2; smad3b heart 75.0, muscle tissue 74.1,
  pharyngeal gill 72.8, camera-type eye 70.0, liver 67.7.
- In shared entities the largest differences favour smad3a (somite 95.4 vs 43.9, head
  kidney 72.4 vs 37.7, retina 92.2 vs 67.5); smad3b is higher only in muscle tissue (74.1 vs
  61.3) and slightly in blastula and tail bud.
- ZFIN curated rows: smad3a 14 (maternal/ubiquitous early stages; somite, tail bud,
  integument, immature eye at 14-19 somites; adult heart by RT-PCR); smad3b 27 (maternal,
  gastrula margin, lateral mesoderm, tail bud, brain regions, retina, spinal cord, somite,
  heart). Both are maternally supplied.

## Interpretation

- Both copies keep every annotated functional residue of SMAD3 except S418 in smad3b, so
  both are expected to act as TGF-beta/activin/nodal receptor-activated SMADs. Direct
  biochemical comparison is not available from these data.
- smad3a is the conservative copy; smad3b has diverged faster, mostly in the linker, which
  carries the MAPK/CDK/GSK3 phosphosites (all of which are still present).
- Expression overlaps broadly (both maternal and broadly zygotic). Quantitative differences
  exist (smad3a higher in paraxial mesoderm/somites, head kidney and retina), but Bgee scores
  across genes are not calibrated as absolute levels, and the gene-specific entity lists are
  confounded by study coverage. These data do not establish an expression partition.
