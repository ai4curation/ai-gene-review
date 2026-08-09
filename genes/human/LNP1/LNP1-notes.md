# LNP1 (A1A4G5) review notes

## Research provenance

- The repository fetch was anchored explicitly to reviewed human UniProt A1A4G5 because
  `LNP1` is also a historical alias of the unrelated ER-junction protein LNPK/Q9C0E8.
- Automated deep research was attempted on 2026-08-09. Falcon/Edison failed with HTTP
  402 (payment required), and Perplexity failed with HTTP 401 (insufficient quota). No
  provider-authored deep-research file was created; this journal records the manual
  primary-source review instead.
- Live QuickGO returned zero annotations for A1A4G5, and the fetched GOA TSV contains
  only its header. UniProt likewise reports `PAN-GO; A1A4G5; 0 GO annotations based on
  evolutionary models.`

## Identity and the LNPK collision

The review target is HGNC:28014, LNP1 (leukemia NUP98 fusion partner 1), UniProt
A1A4G5, GeneID 348801, historically also NP3 or LOC348801. It is a reviewed 178-aa
protein with no curated FUNCTION or SUBCELLULAR LOCATION statement. The sequence is
highly charged and contains three predicted disordered regions, but no signal peptide,
transmembrane helix, catalytic motif, or experimentally solved structure. UniProt
curates no alternative protein products.

LNPK (HGNC:21610; UniProt Q9C0E8) has historically also been called LNP1/LNP and is the
ortholog of yeast Lnp1p and the mammalian lunapark ER-junction protein. None of that
ER-network morphology literature is evidence for A1A4G5. Every assertion below was
therefore checked against A1A4G5, GeneID 348801, NP3, LOC348801, or an interaction
record that resolves to that accession.

## Normal-protein evidence

### Repeated association with 14-3-3 proteins

BioPlex 3.0 (PMID:33961781) reports LNP1 co-association with six 14-3-3 paralogs in
human-cell affinity-purification mass spectrometry. The exact bait/prey records and
accession mapping are captured reproducibly in `LNP1-bioinformatics/RESULTS.md`.
The raw prey output contains accession-level protein-group rows for YWHAB isoform 2
(P31946-2), both canonical and isoform-2 YWHAE (P62258 and P62258-2), and canonical
P63104 plus the unreviewed truncated YWHAZ fragment E7ESK7. These rows do not establish
isoform-specific detection, isoform-exclusive biology, or another 14-3-3 gene.
hu.MAP3.0 integrates BioPlex
with other proteomic inputs and states: [PMID:40425816, "We also identify LNP1, an
uncharacterized protein, as associated with members of the 14-3-3 complex
(huMAP3_06971.1)."]

hu.MAP3.0 assigns LNP1-YWHAE a high integrated score and models a phosphoserine-bound
interface, but the paper frames its uncharacterized-protein analyses as testable
hypotheses rather than targeted biochemical validation. A 28-member predicted Complex
Portal cluster should not be interpreted as one stable stoichiometric complex.

There is also a residue-numbering ambiguity that must remain unresolved. Current
A1A4G5 residues 110-115 are `KFSESF`, with serines at 112 and 114. The hu.MAP3.0 paper
says: [PMID:40425816, "LNP1 has a known phosphoserine site at Ser114 (Ochoa et al,
2020) in a motif reminiscent of 14-3-3 binding (KFpSESF vs RXY/FXpSXP (Yaffe et al,
1997))."] The written `KFpSESF` motif places the phosphate on current Ser112, not
Ser114. No site-specific mechanism should be asserted until the underlying
phosphoproteomic mapping is reconciled experimentally.

### LYN association

PLATO screened a ribosome-displayed human ORFeome against GST-LYN and then tested
selected candidates in HEK293T lysates. The paper describes the relevant validation
strategy as follows: [PMID:23503679, "GSTLYN precipitation and western blot analysis
confirmed binding for five of seven novel candidates tested (Figure 2c)."] The
paper's Figure 2c visibly labels LNP1 and shows its GST-LYN pulldown validation, and
BioGRID interaction 868526 maps the prey to A1A4G5/NP3. The specific term GO:1990782
protein tyrosine kinase binding is therefore preferable to generic protein binding.
The result does not establish LYN-dependent phosphorylation or a physiological pathway
for LNP1.

### Other large-scale associations

Crosslinking mass spectrometry in one detergent-insoluble U2OS nuclear fraction
(PMID:30021884) reports an LNP1 Lys124-GAPDH Lys145 crosslink, but a single crosslink
does not define a normal molecular function or establish nuclear-speck localization.
HuRI (PMID:32296183) reports one binary LNP1-GPRIN2 interaction: official supplements
map CCSB ORF 54500 to LNP1 and ORF 6830 to GPRIN2/O60269. The three IntAct records are
assay representations of that edge, not LNP1 self-binding or three partners. With no
physiological context, it still supplies no informative GO term beyond generic protein
binding and is not recommended as an annotation.

## Localization evidence

The Human Protein Atlas currently reports a mainly vesicular antibody pattern in PC-3
and U2OS cells, with nuclear-speck and cytosolic signal only in PC-3. All calls use one
antibody (HPA047926) and have reliability `Approved`, not an independently validated
status. This is useful for designing endogenous-localization experiments, but is too
provisional to make a core location or to infer where the reported interactions occur.

## NUP98 fusion boundary

The best-established biology involving the name LNP1 concerns rare NUP98 fusions, not
the wild-type protein. The original molecular report states: [PMID:18603550, "In a case
of acute myeloid leukemia we report molecular cytogenetic findings of a
t(3;11)(q12;p15), characterized as a new NUP98 translocation rearranging with
LOC348801 at chromosome 3."] The current UniProt disease note also restricts the claim
to a chromosomal translocation with NUP98.

A later mechanistic study found: [PMID:34903620, "We also show that three additional
leukemia-associated NUP98 FOs (NUP98-PRRX1, NUP98-KDM5A, and NUP98-LNP1) form nuclear
puncta and transform hematopoietic cells."] These are properties of NUP98::LNP1 fusion
oncoprotein constructs. They do not support annotations of wild-type LNP1 for nuclear
puncta, phase separation, transcriptional control, transformation, or leukemia.

## Curation synthesis

- Preserve the empty GOA source set exactly.
- Candidate NEW GO:0071889 `14-3-3 protein binding`, IPI from PMID:33961781, with the
  six verified human 14-3-3 partners. Keep non-core because evidence is high-throughput
  co-association plus integrative modeling, without targeted endogenous biochemistry.
- Candidate NEW GO:1990782 `protein tyrosine kinase binding`, IPI from PMID:23503679,
  with LYN/P07948; Figure 2c and BioGRID verify the A1A4G5 mapping.
- Do not add a generic protein-binding row, a stable-complex assertion, a biological
  process inferred from 14-3-3 membership, a phosphosite-specific mechanism, or any
  fusion-derived wild-type function.
- Leave `core_functions: []`: no normal molecular activity has yet been connected to a
  physiological process strongly enough to call it a settled core function.
- Leave `proposed_new_terms: []`: existing specific binding terms cover the defensible
  observations.

## Open questions and decisive experiments

1. Does endogenous LNP1 bind multiple 14-3-3 paralogs, and is binding direct and
   phosphoserine-dependent? Perform reciprocal endogenous co-IP/pulldown, phosphatase
   treatment, and purified binding assays.
2. Is Ser112 or Ser114 the relevant phosphosite, which kinase installs it, and does
   site mutation alter 14-3-3 binding? Use site-resolved MS and S112A/S114A rescue.
3. Is LYN binding reproducible at endogenous abundance, and does LYN phosphorylate
   LNP1? Use reciprocal co-IP, purified binding, kinase assays, and kinase-dead controls.
4. Where does endogenous LNP1 localize? Endogenously tag A1A4G5 and quantify
   colocalization with vesicle and nuclear-speck markers across several expressing cell
   types, with knockout controls for antibody specificity.
5. What normal phenotype follows LNP1 loss? Combine CRISPR knockout with wild-type
   rescue and unbiased transcriptomic, proteomic, trafficking, and stress-response
   readouts in retina- and testis-relevant human models.
6. Which fusion phenotypes require the LNP1 segment rather than the NUP98 FG-rich
   region? Compare wild-type LNP1, NUP98::LNP1, and segment-deletion constructs without
   transferring fusion behavior to the normal protein.
