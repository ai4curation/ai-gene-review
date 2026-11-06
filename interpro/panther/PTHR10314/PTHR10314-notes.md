# PANTHER Family PTHR10314 Analysis Notes

## Family Overview

| Field | Value |
|-------|-------|
| **Family ID** | PTHR10314 |
| **Name** | Cysteine Synthase/Cystathionine Beta-Synthase |
| **Root Node** | PTN000034104 |
| **Taxonomic Scope** | LUCA (Last Universal Common Ancestor) |
| **Root Event** | DUPLICATION |

## IBA Annotation Issue

### Problem Summary

GO:0019344 (L-cysteine biosynthetic process) is annotated at the root node PTN000034104 and propagated to ALL descendants. This is incorrect for subfamily SF135 (Cds1/desulfhydrase) which catalyzes cysteine **catabolism**, not biosynthesis.

### Tree Structure

```
PTHR10314 (Family)
    └── PTN000034104 (Root, LUCA, DUPLICATION)
            │
            │  ⚠️ GO:0019344 "L-cysteine biosynthetic process" annotated here
            │     → Propagates to ALL descendants (ERROR for SF135)
            │
            ├── PTN000034466 [SF194 - CBS/CysK] (branch 0.412)
            │   └── EC 4.2.1.22 / 2.5.1.47 - BIOSYNTHESIS ✓
            │
            ├── PTN008304321 [SF135 - Cds1] (branch 0.528)  ← LONGEST BRANCH
            │   └── EC 4.4.1.1 - CATABOLISM ✗ (WRONG ANNOTATION)
            │
            ├── PTN000741516 [SF5 - Threonine synthase] (branch 0.659)
            │
            ├── PTN008497437 [SF242 - O-Ac-Ser CBS] (branch 0.458)
            │
            └── PTN008497439 [SF162 - CysM] (branch 0.402)
                └── EC 2.5.1.47 - BIOSYNTHESIS ✓
```

### Key Subfamilies

| Subfamily | Name | Branch Length | EC | Function | Correct BP |
|-----------|------|---------------|-----|----------|------------|
| SF135 | Cds1 (desulfhydrase) | **0.528** | 4.4.1.1 | CATABOLISM | GO:0019450 |
| SF194 | CBS/CysK | 0.412 | 4.2.1.22 / 2.5.1.47 | Biosynthesis | GO:0019344 |
| SF162 | CysM | 0.402 | 2.5.1.47 | Biosynthesis | GO:0019344 |
| SF242 | O-Ac-Ser CBS | 0.458 | 2.5.1.47 | Biosynthesis | GO:0019344 |
| SF5 | Threonine synthase | 0.659 | 4.2.3.1 | Thr synthesis | GO:0009088 |

### Evidence: SF135 is Functionally Distinct

1. **Longest branch length (0.528)** from root indicates greatest sequence divergence
2. **Different EC number**: 4.4.1.1 (lyase) vs 2.5.1.47 (transferase)
3. **Opposite reaction direction**:
   - SF194/SF162: O-Ac-L-Ser + H2S → L-Cys (BIOSYNTHESIS)
   - SF135: L-Cys + H2O → H2S + pyruvate (CATABOLISM)
4. **Different products**: SF135 produces H2S as main product; SF194/SF162 consume H2S

### Proteins in SF135 (Cds1 subfamily)

| UniProt | Gene | Organism | Definition |
|---------|------|----------|------------|
| O69652 | cds1 (Rv3684) | M. tuberculosis | L-cysteine desulfhydrase Cds1 |
| Q9KT44 | cds1 (VC_1061) | V. cholerae | L-cysteine desulfhydrase Cds1 |
| Q8ZRB5 | cds1 (STM0458) | S. typhimurium | L-cysteine desulfhydrase Cds1 |
| Q8PCX2 | cysM (XCC0578) | X. campestris | L-cysteine desulfhydrase Cds1 |
| A0A2U2H408 | cds1 (YPO3147) | Y. pestis | L-cysteine desulfhydrase Cds1 |

### Source Proteins for IBA (WITH/FROM field)

These proteins ARE correctly annotated to GO:0019344:

| UniProt | Gene | Subfamily | Organism | Correct? |
|---------|------|-----------|----------|----------|
| P0ABK5 | cysK | SF194 | E. coli | ✓ Yes |
| P35520 | CBS | SF194 | Human | ✓ Yes |
| P16703 | cysM | SF162 | E. coli | ✓ Yes |
| P9WP53 | cysM | SF162 | M. tuberculosis | ✓ Yes |
| P9WP55 | cysK1 | SF194 | M. tuberculosis | ✓ Yes |
| P37887 | cysK | SF194 | B. subtilis | ✓ Yes |

## Root Cause Analysis

### Why the Error Occurs

1. **Structural similarity ≠ functional equivalence**: All subfamilies share the TrpB-like PLP fold
2. **Annotation at wrong taxonomic level**: GO:0019344 should be at SF194/SF162 level, not root
3. **Neo-functionalization not captured**: SF135 evolved a new function after diverging from common ancestor

### Sequence Evidence from MSA Analysis

**Full family MSA**: [msa/PTHR10314.afa](msa/PTHR10314.afa) (1448 sequences, fetched via `just family-msa PTHR10314`)

**Representative subset**: [msa/representatives.aln](msa/representatives.aln) (5 key proteins for focused analysis)

#### Sequence Length Differences

| Protein | Subfamily | Length |
|---------|-----------|--------|
| Cds1 (M. tuberculosis) | SF135 | 368 aa |
| Cds1 (V. cholerae) | SF135 | 355 aa |
| CysK (E. coli) | SF194 | 323 aa |
| CysM (E. coli) | SF162 | 303 aa |
| CBS (Human) | SF194 | 551 aa |

#### Pairwise Sequence Identity

| Comparison | Identity |
|------------|----------|
| Cds1-Mtb vs Cds1-Vc | **59.2%** (conserved within SF135) |
| Cds1-Mtb vs CysK | **23.4%** |
| Cds1-Mtb vs CysM | **24.7%** |
| CysK vs CysM | 42.6% |
| CysK vs CBS | 39.9% |

**Key finding**: SF135 (Cds1) shares only ~24% identity with cysteine synthases, less than CysK shares with CysM (43%). This is consistent with neo-functionalization.

#### N-terminal Extension in SF135

Cds1 has a unique N-terminal extension before the aligned core:
- Cds1-Mtb: `MSGGACIAVRSLSRSWTDN` (19 residues)
- Cds1-Vc: `MCTDHQWINS` (10 residues)
- CysK/CysM: No equivalent extension

#### Active Site Signature Motif (MSA position ~1688)

The full PANTHER MSA reveals a **diagnostic active site signature** that explains functional divergence:

| Subfamily | Motif | Function |
|-----------|-------|----------|
| SF194/SF162 (synthases) | **PTSGNTG** | Cysteine biosynthesis |
| SF135 (desulfhydrase) | **ASSGST** | Cysteine catabolism |

Key substitutions in SF135:
- **P→A**: Proline to Alanine at loop start
- **N→S**: Asparagine to Serine in middle
- **G→T**: Different terminal residue

These substitutions in the active site loop alter substrate binding and explain why SF135 catalyzes the **reverse reaction** (cysteine breakdown → H₂S + pyruvate) compared to synthases (O-acetylserine + H₂S → cysteine).

#### Conserved PLP-Binding Lysine

Position 1352: Lysine conserved >97% in all subfamilies - this is the catalytic residue that binds pyridoxal-5'-phosphate (PLP). The core PLP chemistry is conserved; only substrate specificity differs.

#### Diagnostic Positions Summary

- 174 positions where SF135 is internally conserved but differs from both SF194 and SF162
- 31 differences in an 80-position window around active site
- SF135 shares only ~24% identity with synthases (vs 43% between CysK and CysM)

## Recommendations

### For GO-Central/PANTHER Curators

1. **Remove** GO:0019344 propagation to SF135
2. **Add** SF135-specific annotations:
   - GO:0019450 (L-cysteine catabolic process to pyruvate)
   - GO:0080146 (L-cysteine desulfhydrase activity)
   - GO:0070814 (hydrogen sulfide biosynthetic process)
3. **Generalize** root annotation to "cysteine metabolic process" OR restrict to SF194/SF162

### For Gene Reviews

Mark GO:0019344 as REMOVE for any SF135 protein with reason:
> "Incorrect IBA propagation - enzyme is catabolic (EC 4.4.1.1 desulfhydrase), not biosynthetic (EC 2.5.1.47 synthase). Source proteins in WITH/FROM are from SF194/SF162 (true synthases), but target is in SF135 (desulfhydrase subfamily) which diverged early with longest branch length (0.528) indicating neo-functionalization."

## Deep Research Findings (Falcon 2026-01-06)

See full report: [PTHR10314-deep-research-falcon.md](PTHR10314-deep-research-falcon.md)

### Key Structural Features

- **Common fold**: Tryptophan synthase β-superfamily (PLP fold type II/β family)
- **Core chemistry**: PLP-mediated β-elimination/β-replacement via aminoacrylate intermediate
- **Conserved catalytic lysine**: Lys41 (OASS numbering) forms internal aldimine with PLP

### Substrate Specificity Determinants

| Subfamily | Key Residues | Sulfur Donor | Reference |
|-----------|--------------|--------------|-----------|
| CysK | Gly230/Ala231/Gly232 | Sulfide only | McGarvie 2025 |
| CysM | Arg210/Arg211/Trp212 + 3-residue insertion | Sulfide OR thiosulfate | McGarvie 2025 |
| OPS-CysM | Similar to CysM | Thiocarboxylated CysO | McGarvie 2025 |
| CBS | Different architecture | Homocysteine | Pedretti 2024 |

### Regulatory Diversity

1. **CysK**: Forms Cysteine Synthase Complex (CSC) with serine acetyltransferase (CysE)
   - CysE C-terminal tail binds in CysK active site and inhibits activity
   - CysM generally LACKS CSC formation

2. **CBS (mammalian)**:
   - N-terminal heme-binding domain
   - C-terminal SAM-responsive Bateman regulatory domain
   - Forms filaments modulated by SAM (morpheein behavior)

### Literature Support

- Zmich et al. 2023 ACS Catalysis: Multiplexed screening of 40 PLP-dependent homologs reveals mis-annotation
- McGarvie 2025: OASS structure-function and druggability
- Pedretti 2024: H2S-producing enzymes as antimicrobial targets

## Note on Cds1 (SF135) Gap in Literature

The deep research focused primarily on OASS (CysK/CysM) and CBS subfamilies. The **L-cysteine desulfhydrase (Cds1) subfamily (SF135)** was not extensively covered, though it represents a clear case of neo-functionalization:

- Cds1 catalyzes the **reverse reaction**: L-cysteine → H2S + pyruvate (EC 4.4.1.1)
- This is cysteine CATABOLISM, not biosynthesis
- Key experimental papers: PMID:34439535 (M. tuberculosis), PMID:34283874 (V. cholerae)

## References

- PANTHER API: https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR10314
- InterPro: https://www.ebi.ac.uk/interpro/entry/panther/PTHR10314/
- QuickGO IBA documentation: https://www.ebi.ac.uk/QuickGO/term/GO:0019344
- Zmich et al. 2023: https://doi.org/10.1021/acscatal.3c02498

## Experimental Evidence

### For SF135 (Cds1) function:

**PMID:34439535** (Kunota et al. 2021) - M. tuberculosis Cds1:
- Genetic deletion reduces H2S production
- LC-MS/MS confirms products: H2S + pyruvate
- KM = 11.26 mM for cysteine, kcat = 78.71 sec-1
- Activity inhibited by AOAA (PLP inhibitor), NOT by PAG (CGL inhibitor)

**PMID:34283874** (Ma et al. 2021) - V. cholerae Cds1:
- VC1061 (cds1) is principal determinant of cysteine-derived H2S
- H2S protects against oxidative stress (H2O2)
- CBS-derived H2S enhances catalase (KatB) activity

---
*Analysis performed 2026-01-06*

## 2026-11-03 re-review for the bacterial cysteine biosynthesis module

Subfamily membership was read from the PANTHER 19.0 organism classification
files (`.cache/panther/PTHR19.0_*`) and node recipients from the PAINT UniProt
GAF (`.cache/panther/gene_association.paint_uniprot.gaf.gz`, column 8 carries
the PTN node), for example

```
zcat .cache/panther/gene_association.paint_uniprot.gaf.gz | awk -F'\t' '$2=="O69652"{print $2,$3,$5,$8}'
```

Findings:

- PTHR10314:SF194 (named CYSTATHIONINE BETA-SYNTHASE) is not a CBS-only
  subfamily. Besides human CBS P35520 and yeast CYS4 P32582 it holds the
  bacterial cysteine synthase A proteins: E. coli CysK P0ABK5, Salmonella CysK
  P0A1E3, B. subtilis CysK P37887, M. tuberculosis CysK1 P9WP55 and CysK2
  Q79FV4, and P. aeruginosa CysK Q9I0D3.
- PTHR10314:SF162 (CYSTEINE SYNTHASE B) holds E. coli CysM P16703,
  P. aeruginosa CysM Q9I526, Salmonella CysM P29848 and M. tuberculosis CysM
  P9WP53.
- PTHR10314:SF5 (THREONINE SYNTHASE 1, CHLOROPLASTIC) holds the threonine
  synthases B. subtilis ThrC P04990, M. tuberculosis ThrC P9WG59 and
  Arabidopsis TS1 Q9S7B5. PTN000741516 is this threonine-synthase clade: its
  IBDs are threonine synthase activity and threonine biosynthesis (seeds
  P9WG59 and AT4G29840), and its recipients include P04990 and P9WG59. The
  IRD for GO:0019344 at PTN000741516 therefore prunes cysteine biosynthesis
  from threonine synthases, not from the cysteine desulfhydrases.
- The SF135 cysteine desulfhydrase M. tuberculosis Cds1 O69652 still receives
  the GO:0019344 IBA from PTN000034104 in the current PAINT GAF, so the
  over-propagation described above is not repaired by any IRD.
- PTN000034668 (IRD, GO:0019344, taxon Eukaryota) is not resolved to a clade in
  the slice. Its likely recipients are the eukaryotic SF35 (MITOCHONDRIAL
  CYSTEINE SYNTHASE-RELATED) proteins: yeast MCY1 P53206, S. pombe cys12
  P87131, N. crassa cys-12 Q7SHQ1 and Arabidopsis At1g55880 Q6NKY5 all receive
  the PTN000034104 cytoplasm IBA but no GO:0019344 IBA.
- B. subtilis MccA O05393 (SF242, O-ACETYLSERINE DEPENDENT CYSTATHIONINE
  BETA-SYNTHASE) is the only seed of PTN008497437, which carries both GO:0004122
  and GO:0004124.


## 2026-11-06: CysM substrate scope and PAINT assertion audit

The current compact-tree descendant check, recorded in
`analysis/module_audits/bacterial_cysteine_biosynthesis_via_o_acetylserine/family-placement-audit.yaml`,
shows that P9WP53 maps to PTN002232520 in SF162 and descends from PTN008497439.
This is positive membership evidence, not a reclassification from the gene name.
The E. coli P16703 seed and PAO1 Q9I526 OAS/sulfide activity remain valid positive evidence.
Thiosulfate-dependent S-sulfocysteine production is a different complete reaction.

PMID18842002 measures slow OAS aminoacrylate formation and strong OPS/CysO-COSH
preference. The independently inspected PMID18799456 primary excerpt and construct
limits are preserved in `genes/MYCTU/cysM/cysM-source-analysis/18799456-assay-scope.md`.
Its tested recombinant protein contains Thr2Ala and a residual GSH prefix; OAS plus
sodium sulfide gave no detected cysteine, without a formal detection limit. Neither
that result nor slow first-half-reaction chemistry proves zero intrinsic OAS turnover
for native P9WP53. Conversely, these measurements do not establish the complete
GO:0004124 reaction or a native OAS route. The node assessment and broader term scope
are therefore UNRESOLVED, while positive seeds and all PAINT node metadata are retained.

The family-root cysteine-biosynthesis BP cannot establish ancestral OAS-specific
chemistry. That unsupported inference was removed without denying demonstrated
cysteine synthase activities in the relevant members. No PAINT table, seed set,
provider report or raw member file was changed.

### Archived scope-carving entries

These exact prior GO:0004124 member exceptions are preserved for provenance.
Their functional distinctions remain valid, but the active UNRESOLVED scope no
longer makes a family-wide assertion from which to carve exceptions.

```yaml
  member_exceptions:
  - member:
      id: UniProtKB:P32582
      label: Cystathionine beta-synthase
      gene_symbol: CYS4
      organism: Saccharomyces cerevisiae
      gene_review: genes/yeast/CYS4/CYS4-ai-review.yaml
    exception_reason: >-
      Cystathionine beta-synthase; it receives the CBS IBA from PTN000034107 and no cysteine synthase
      IBA.
    supported_by:
    - reference_id: file:interpro/panther/PTHR10314/PTHR10314-paint.tsv
      supporting_text: "PTHR10314\tPTN000034107\tGO:0004122\tF\tIBD\tfalse"
  - member:
      id: UniProtKB:P9WG59
      label: Threonine synthase
      gene_symbol: thrC
      organism: Mycobacterium tuberculosis H37Rv
    exception_reason: >-
      Threonine synthase in the SF5 clade, where PAINT places threonine synthase activity and
      negates cysteine biosynthesis.
    lost_in_clade_node_id: PANTHER:PTN000741516
    supported_by:
    - reference_id: file:interpro/panther/PTHR10314/PTHR10314-paint.tsv
      supporting_text: "PTHR10314\tPTN000741516\tGO:0004795\tF\tIBD\tfalse"
  - member:
      id: UniProtKB:O69652
      label: L-cysteine desulfhydrase Cds1
      gene_symbol: cds1
      organism: Mycobacterium tuberculosis H37Rv
      gene_review: genes/MYCTU/cds1/cds1-ai-review.yaml
    exception_reason: >-
      SF135 cysteine desulfhydrase that degrades rather than synthesises cysteine; the slice has no
      PAINT node for this clade, so no lost_in_clade node is given.
    supported_by:
    - reference_id: file:genes/MYCTU/cds1/cds1-ai-review.yaml
      supporting_text: catalyzes L-cysteine CATABOLISM, not biosynthesis
```


## 2026-11-06: MccA biochemical activity versus node scope

Persistent audit marker: `CYSTEINE-MCCA-SUBSTRATE-SCOPE-20261106`.

PMID17056751 is cached with its primary abstract (full_text_available:false), which
explicitly reports purified recombinant YrhA/MccA OAS-thiol-lyase activity at 75-fold
lower activity than CysK and atypical OAS-plus-homocysteine cystathionine synthesis.
The former supports the seed molecular function even if it is secondary in vivo;
physiological prominence is not a prerequisite for biochemical activity. The
PTN008497437 GO:0004124 overall assessment remains UNRESOLVED about the breadth
of phylogenetic propagation, not about whether the cited seed activity was observed.

QuickGO GO:0004122 was checked on 2026-11-06: its reaction uses L-serine and
L-homocysteine, producing cystathionine and water. OAS-dependent MccA chemistry
cannot establish this exact serine-dependent reaction merely through the CBS name.
The GO:0004122 assessment remains substrate-specifically UNRESOLVED. The prior
statement that there was no cached MccA biochemistry was incorrect and is superseded.
The broad phrase every CBS was narrowed to reviewed canonical serine-dependent CBS
proteins, leaving the atypical SF242 MccA distinction explicit. All PAINT node ids,
assertions, dates and seeds were preserved; no new MccA gene review or native OAS
route claim was created.


## 2026-11-06 PR6120 round 1: explicit scope comparison

The [structured scope proof](PTHR10314-source-analysis/round1-go0004124-scope.yaml) restores the three historical GO:0004124 exception objects unchanged and records P9WP53 separately as an over-annotated member assignment, with its assay and construct limits. This supersedes the earlier prose-only archive as the machine-readable comparison artifact; it does not silently grant activity to the family.

The frozen compact tree resolves the bacterial CysK node PTN000034535 to 40 leaves (36 SF194, two SF102, two SF191), the CysM node PTN008497439 to 25 SF162 leaves, and the eukaryotic OAS-TL node PTN000034468 to 420 leaves in 28 subfamilies. The CBS node PTN000034107 contains 69 SF194 leaves and six SF243 leaves. Thus SF194 cannot substitute for the CysK node: a single yeast exception would still leave human CBS P35520 and other CBS proteins inside a false whole-subfamily grant. No OAS-TL subfamily identifier is guessed.

The current checker only computes positive coverage for FAMILY_WIDE/SUBFAMILY_ONLY (family_gene_crosscheck.py:367), rejects member_exceptions under UNRESOLVED (line 439), and rejects an exception outside the selected subfamilies (line 475). Restoring Cds1/SF135 as an exception under SF194/SF162 would therefore be contradictory. The production join sees family-only raw crossreferences for CYS4, MYCTU Cds1 and MYCTU CysM, so the proof distinguishes its missing-subfamily result from a read-only overlay of verified tree membership. The linked proof includes executable read-only counterexamples and actual current gene actions so the unresolved family boundary cannot hide the target-specific disagreements. No validation semantics were changed.

P9WP53's OAS/free-sulfide assignment is over-annotated; slow OAS aminoacrylate formation in PMID18842002 is not a demonstrated weak complete reaction. PMID18799456 reports no detected complete product under the tested conditions, with the documented recombinant construct and detection limits. These observations justify challenging an inherited OAS assignment but do not establish an evolutionary loss or exactly zero residual turnover. NEEDS_PRUNING explicitly asserts a loss (family_review.yaml:811), so that stronger node verdict is not adopted. The E. coli P16703 and PAO1 Q9I526 positive activities remain supported; UNRESOLVED at the mixed node is limited to its retention boundary.
