# LRMDA literature notes

## Evidence boundaries

### Identity, architecture, and proteoforms

The reviewed human target is UniProtKB Q9H2I8, a 198-residue leucine-rich-repeat
protein with four annotated LRRs and an LRR C-terminal domain. Its curated record
has no signal peptide, transmembrane helix, catalytic feature, or
alternative-products section. This architecture is compatible with a soluble
interaction adaptor, but LRR architecture alone does not establish an enzyme,
receptor, adhesion molecule, or transferable molecular function
[file:human/LRMDA/LRMDA-uniprot.txt].

The 2025 mechanistic study has an important proteoform boundary: all experiments
used the longer A0A087WWI0 sequence [PMID:41038817 Identification of a
RAB32-LRMDA-Commander membrane trafficking complex, "This isoform was used in all experiments."].
A0A087WWI0 is 226 residues and Q9H2I8 is 198 residues. Their official sequences
share Q9H2I8 residues 22-198 with A0A087WWI0 residues 50-226, including the
terminal IRDDQL motif, but have alternative N termini rather than a simple
N-terminal extension. Thus the sequence-numbered interfaces and perturbations in
PMID:41038817 directly describe the tested A0A087WWI0 construct. Conservation
makes transfer to the common C-terminal region plausible, not experimentally
identical, and the paper does not establish endogenous isoform-specific
expression or function for Q9H2I8.

The 2022 localization and RAB32/RAB38-interaction work used the same length
boundary: attempts to amplify 226- and 198-residue transcripts from MNT1 cDNA
recovered only the former [PMID:36334630 OCA7 is a melanosome membrane protein,
"Attempts to amplify two potential transcript variants of OCA7 encoding a 226 or 198 amino acid protein from MNT1 complementary DNA (cDNA) were only successful for the first, suggesting it is the predominant variant."].
Its OCA7-EGFP imaging, yeast-two-hybrid, and recruitment constructs therefore
describe the 226-residue form. The OCA7-knockout phenotypes remain gene-level
evidence, but the direct localization and binding results are proteoform-bounded.

### Human, zebrafish, and mouse

The 2013 study directly links recessive human C10orf11/LRMDA alleles to albinism
and reports human fetal expression [PMID:23395477 Mutations in c10orf11, a
melanocyte-differentiation gene, "Immunohistochemistry showed localization"]. The
developmental perturbation itself was performed in zebrafish
[PMID:23395477 Mutations in c10orf11, a melanocyte-differentiation gene, "zebrafish (Danio rerio) homolog with the use of morpholinos resulted in"].
Rescue by wild-type but not mutant human C10orf11 strengthens orthology and
allele specificity, but it remains a zebrafish morpholino experiment rather than
human or mouse loss-of-function physiology. No decisive mouse pigment-cell
experiment was needed for this review. The mouse orthologue is useful as a
subfamily member, not as an experimental donor for claims made here.

### Melanocyte differentiation versus pigment synthesis

PMID:23395477 supports a conserved role in melanocyte development/differentiation
because the zebrafish phenotype included fewer apparent pigmented melanocytes.
It does not isolate a biochemical melanin-synthesis reaction, and pigmentation
loss alone cannot distinguish melanocyte number, differentiation, organelle
biogenesis, and pigment production.

PMID:36334630 supplies a later, mechanistically distinct boundary in human MNT1
cells, where OCA7 knockout altered melanin through melanosome maturation
[PMID:36334630 OCA7 is a melanosome membrane protein, "Using newly generated OCA7-KO MNT1 cells, we show OCA7"].
It further reports effects on PMEL processing, the stage-I-to-stage-II transition,
and organelle pH [PMID:36334630 OCA7 is a melanosome membrane protein, "premelanosome protein (PMEL) processing, impacting fibrillation and the"].
These data directly support a melanocyte-autonomous role in melanosome biogenesis
and pigment output in an established human melanoma-derived melanocytic line.
They do not, by themselves, prove embryonic melanocyte differentiation or normal
in-vivo human physiology.

### Molecular role and localization

OCA7/LRMDA localizes to the melanosome limiting membrane and is recruited via
the RAB32/RAB38 effector-binding surface [PMID:36334630 OCA7 is a melanosome
membrane protein, "interaction with a canonical effector-binding surface of melanosome proteins"].
PMID:41038817 then shows simultaneous association with Commander and active RAB32
[PMID:41038817 Identification of a RAB32-LRMDA-Commander membrane trafficking
complex, "simultaneously associates with Commander"]. Together
the direct data support a peripheral membrane-associated adaptor that couples
active RAB32-family GTPases to Commander/Retriever during melanosome biogenesis;
they do not support a transmembrane-receptor or enzymatic interpretation.

The Human Protein Atlas-derived nucleoplasm annotation is an independent
high-throughput localization observation. Neither decisive pigment paper
establishes a nuclear molecular activity, so nucleoplasm should remain
non-core unless targeted nuclear evidence emerges.

Historically LRMDA's molecular function was unknown, but the direct 2025
simultaneous RAB32/Commander-binding mechanism now supports considering current
GO:0030674 `protein-macromolecule adaptor activity` and GO:0031267 `small GTPase
binding`, rather than generic `protein binding` [PMID:41038817 Identification of
a RAB32-LRMDA-Commander membrane trafficking complex, "simultaneously associates with Commander"]. Any authored MF must keep the
226-residue proteoform boundary explicit: the 2022 RAB32/RAB38-binding and
localization assays and all 2025 mechanism and sequence-numbered interface assays
used that longer form, while transfer to the shared region of reviewed Q9H2I8 is
strongly sequence-supported but not an endogenous Q9H2I8 isoform experiment. The
evidence does not support a catalytic or receptor activity.

### Disease and family-transfer limits

Biallelic loss-of-function variants cause oculocutaneous albinism type 7. The
2013 fetal staining did not detect C10orf11 in retinal pigment epithelial cells
[PMID:23395477 Mutations in c10orf11, a melanocyte-differentiation gene, "no localization was seen in retinal pigment epithelial cells"], so ocular disease
must not be converted into a direct RPE localization claim. PMID:41038817
provides a molecular disease model in which LRMDA mutations disrupt both partner
interactions [PMID:41038817 Identification of a RAB32-LRMDA-Commander membrane
trafficking complex, "uncouple RAB32 and Commander binding"], but that mechanism
was established with the longer A0A087WWI0 construct and human cell models rather
than patient tissue.

PANTHER places human LRMDA in PTHR46282:SF2 with the mouse orthologue, whereas
the broad PTHR46282 family contains multiple subfamilies. The LRR fold is widely
reused and cannot license transfer of localization, binding partners, or
pigment-cell function from unrelated LRR proteins or other PTHR46282 subfamilies.
Transfers should remain orthologue- and LRMDA-subfamily-specific and should
preserve the zebrafish-versus-human and proteoform boundaries above.
