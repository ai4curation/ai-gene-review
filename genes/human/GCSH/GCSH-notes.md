# GCSH (Glycine cleavage system H protein, mitochondrial) — review notes

UniProt: P23434 (GCSH_HUMAN), 173 aa precursor, HGNC:4208, chr16.

## Core biology

GCSH is the **H-protein of the mitochondrial glycine cleavage system (GCS)**. It is a small,
**non-catalytic lipoyl-carrier protein**: it bears a covalently attached lipoyl group on a
specific lysine (N6-lipoyllysine at Lys107 in the mature/precursor numbering) that acts as a
**swinging arm** shuttling the reaction intermediate between the other GCS components.

- FT MOD_RES 107 = N6-lipoyllysine; DOMAIN 66..148 = Lipoyl-binding (PROSITE PS50968 BIOTINYL_LIPOYL, PS00189 LIPOYL).
- COFACTOR: Binds 1 (R)-lipoate cofactor covalently [ECO:0000269|PubMed:1671321].
- AltName "Lipoic acid-containing protein"; KW Lipoyl.

### GCS reaction cycle (P/H/T/L proteins)
From [PMID:36190515]:
"Glycine is decarboxylated to carbon dioxide and the resulting aminomethyl-group transferred to
lipoyl-H-protein as aminomethyl-lipoate. The T-protein releases ammonia while transferring the
methyl-group to tetrahydrofolate. The L-protein reoxidizes the reduced lipoyl-group."
- P-protein = GLDC (glycine dehydrogenase, decarboxylating)
- T-protein = AMT/GCST (aminomethyltransferase)
- L-protein = DLD (dihydrolipoyl dehydrogenase)
- H-protein = GCSH itself: "the H-protein itself is the lipoate carrier of this enzyme complex."
- "Variants could also affect the reaction of the swinging lipoyl-arm to protect the amino-methyl group, for which Ser67 is important" [PMID:36190515].

### Moonlighting: lipoate biogenesis / donor
GCSH also acts in **lipoate biosynthesis and transfer** to other 2-keto-acid dehydrogenases
(DLAT/PDH E2, DLST/2-KGDH E2): apo-H → octanoyl-H (LIPT2) → lipoyl-H (LIAS) → lipoyl donated by
LIPT1 to DLAT/DLST. [PMID:36190515]: "The H-protein is pivotal in the biosynthesis and transfer of
the cofactor lipoate to several critical cellular energetics enzymes." UniProt FUNCTION: "Has a
pivotal role in the lipoylation of enzymes involved in cellular energetics." This underlies the
`protein maturation` (GO:0051604) and `generation of precursor metabolites and energy` (GO:0006091)
TAS annotations from PMID:36190515 — legitimate but non-core moonlighting roles.

## Localization
Mitochondrion / mitochondrial matrix. TRANSIT 1..48 = mitochondrial targeting.
- EXP [PMID:36190515]: colocalization of GCSH (green) with mitochondrial marker cytochrome C (red)
  in COS7 cells.
- HTP [PMID:34800366]: MitoCoP high-confidence mitochondrial proteome (>1,100 proteins).
- Reactome TAS: mitochondrial matrix (GCS + lipoylation reactions occur in matrix).

## Disease
Biallelic GCSH variants → variant/combined nonketotic hyperglycinemia (NKH) + lipoate deficiency;
"Multiple mitochondrial dysfunctions syndrome 7" (MMDS7, MIM:620423). [PMID:36190515, PMID:33890291].
NKH = glycine encephalopathy (accumulation of glycine, elevated CSF/plasma ratio, epileptic
encephalopathy). GCSH accounts for <1% of NKH.

## Annotation strategy
- MF: GOA only gives `protein binding` (GO:0005515) IPIs from large-scale Y2H interactome maps
  (PMID:16189514, PMID:32296183) whose interactors (NMI, MAGEA6/11, MED11, MIS18A, RHBDD2, CIDEB)
  are NOT GCS partners and don't inform function → MARK_AS_OVER_ANNOTATED (bare protein binding,
  uninformative; experimental IPI so not REMOVE).
- The informative MF for a lipoyl carrier is **lipoic acid binding (GO:0031405)** — captures the
  covalent lipoyl cofactor (PROSITE lipoyl domain + N6-lipoyllysine K107 + (R)-lipoate cofactor).
  Add as NEW MF and use as the core_function molecular_function.
- BP core: glycine decarboxylation via glycine cleavage system (GO:0019464) / glycine catabolic
  process (GO:0006546).
- CC core: glycine cleavage complex (GO:0005960); located in mitochondrial matrix (GO:0005759).
- Verified candidate MF `GO:0031405 lipoic acid binding` is current (molecular_function, not obsolete).

## References status
All cited PMIDs and Reactome entries are cached. PMID:1671321 and PMID:3348809 are abstract-only
(full_text_available: false) — abstracts confirm H-protein/GCS identity and lipoylation/cofactor.
PMID:36190515 full text available (the key functional paper).


## 2026-11-05 — human H-protein carrier reassessment

The current evidence supports one mitochondrial glycine-cleavage carrier role. The natural precursor has 173 residues and the processed chain spans residues 49–173. Precursor Lys107 is mature residue 59 by coordinate conversion, not position 107 in both numbering systems. No separate natural alternative product is established.

The prior authored lipoic-acid-binding proposal is retained in the historical archive but is not carried into the current annotations. Covalent lipoylation does not itself demonstrate the noncovalent interaction named by the binding parent. The original human study's main text on pages 351–360 was read from its scan; its normal cache contains the abstract. The yeast GCV3 annotation is an explicit convention exception, so absence across all H-proteins is not claimed. Carrier-term mapping remains a question rather than a replacement NEW.

Protein maturation remains unresolved because a donor substrate is not automatically a participant in the modifying step. The question is whether GCSH supplies additional structural or cofactor work beyond donating its lipoyl group. The current core therefore records the established glycine-cleavage process, complex and matrix location without inventing a catalytic or carrier MF identifier.

The eight positive interaction contexts are preserved. Four receive informative partner-class binding refinements; four generic protein-binding annotations are removed without denying the observed pairs. The MAGEA11 historical accession crosswalk remains gene-level, and the RHBDD2 isoform identity remains literal. MitoCoP's membrane category is Ambiguous; its pre-existing matrix column is not a new submitochondrial experiment. Source-specific readings and exact model paths are documented in the source guide and evidence companion.


## 2026-11-05 — carrier terminology and evidence context

The H-protein carrier activity is now represented explicitly as a proposed lipoyl-dependent child of molecular carrier activity. The PomBase gcv3 GO-CAM supplies a same-role precedent, and GO:0140414 shows that a covalent prosthetic arm is compatible with the carrier branch. The earlier four-target negative query did not establish universal absence. Budding-yeast GCV3 and bacterial sucB/dlaT lipoic-acid-binding annotations document a competing convention; the human cDNA study still does not supply a noncovalent affinity assay.

The four partner-class binding refinements retain the positive assay pairs and independently supported NMI, MAGEA11 and MED11 classes. They do not assign transcriptional activity or physiological nuclear colocalization to GCSH. Uncertainty about whether GCSH does additional structural work in protein maturation remains distinct from its established lipoyl-donor role. The quoted UniProt statements retain their exact wording and now cite the local record.
