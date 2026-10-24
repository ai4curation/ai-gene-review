# SLC16A11 (human, Q8NCK7) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised relative (ortholog, same PANTHER
subfamily PTHR11360:SF80 "MONOCARBOXYLATE TRANSPORTER 11") of horse SLC16A11 (F6YMY3).
No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon human SLC16A11 --fallback perplexity-lite` failed: falcon
returned "Exception: Failed to authenticate" and the perplexity-lite fallback returned
HTTP 401 (insufficient quota). No deep-research file exists. The review is built from the
cached full texts of the two GOA source papers plus a PubMed search
(`SLC16A11[tiab] OR MCT11[tiab]`, 48 hits), from which six further papers were cached.

### Evolutionary grounding

- UniProt: PANTHER PTHR11360:SF80 (MONOCARBOXYLATE TRANSPORTER 11); InterPro IPR050327
  Proton-linked_MCT; Pfam PF07690 MFS_1; TCDB 2.A.1.13.13; 12 predicted TM helices
  (residues 12-403), cytoplasmic C-terminal tail 404-447.
- PAINT (interpro/panther/PTHR11360/PTHR11360-paint.tsv): Q8NCK7 is itself an
  experimental donor of IBD nodes PTN000888455 (GO:0008028 monocarboxylic acid
  transmembrane transporter activity, taxon:6072 Eumetazoa) and PTN002260587
  (GO:0005886 plasma membrane; GO:0022857 transmembrane transporter activity).
  So the IBA rows it receives are anchored partly on its own IDA data (correct and
  expected, not circular).
- Rusu et al. 2017 place SLC16A11 in SLC16 "category I" (proton-coupled carriers of
  simple monocarboxylates: MCT1, MCT2, MCT3, MCT4 = SLC16A1/7/8/3).

### Experimental findings in human (what is established in THIS species)

1. Pyruvate transport across the plasma membrane, proton coupled [PMID:28666119
   "HEK293T cells co-transfected with pyronic and either empty vector control or
   SLC16A11REF-V5 (Figure S3B) were exposed to pyruvate, resulting in an increase of the
   fluorescence signal indicative of pyruvate uptake (Figure 3D)."]; H+ co-flux by BCECF
   ["Following addition and withdrawal of pyruvate, we observed a ~40% increase in the
   rates of acidification and alkalization, with both phases reciprocal to influx and
   efflux of pyruvate."]. Bidirectional (influx and efflux). Only observed at neutral pH
   in this heterologous system. Full substrate range not determined ["we have not
   catalogued the full range of substrates transported by SLC16A11"].
2. Localization: mostly intracellular (ER) membranes when overexpressed, with ~5% at PM
   [PMID:28666119 "the majority of SLC16A11REF-V5 is associated with intracellular
   membranes, with a portion (~5%) localized to the plasma membrane (Figure 3C)"];
   ER colocalization with calnexin in HeLa [PMID:24390345 "SLC16A11-V5 co-localizes
   with the endoplasmic reticulum membrane protein Calnexin"]. Both are tagged
   overexpression.
3. Basigin (BSG, P35613) interaction by co-IP; BSG knockout reduces PM localization by
   ~80% [PMID:28666119]. T2D-risk coding haplotype weakens the BSG interaction and lowers
   PM localization ~60%. This is an ancillary-subunit/chaperone relationship typical of
   category I MCTs; no informative MF term for SLC16A11 itself beyond transport.
4. Lipid phenotypes: overexpression in HeLa raises TAG [PMID:24390345]; siRNA knockdown
   in primary human hepatocytes raises acylcarnitines, DAG, TAG [PMID:28666119]. These
   are downstream metabolic consequences of a transporter; SLC16A11 catalyses no step of
   lipid metabolism. Treated as non-participation (MARK_AS_OVER_ANNOTATED on the IDA
   row, not REMOVE, because the observation itself is real).
5. Expression: liver, salivary gland, thyroid [PMID:24390345].

### Findings in other species (NOT to be presented as established in human)

- Mouse: Slc16a11 is upregulated in terminally exhausted CD8+ T cells; overexpression
  increases [14C]-lactate uptake/oxidation; anti-MCT11 antibody reduces lactate uptake;
  conditional KO improves Tex function [PMID:39516648]. Supports lactate as a
  physiological substrate in mouse; human data in that paper are expression and antibody
  blockade, not transport assays.
- Mouse Slc16a11 KO: no significant metabolic defect; liver reconstitution with the
  mutant (but not WT) increases TG accumulation [PMID:30673611] - disputed by
  PMID:31618643 / reply PMID:31618644. AAV knockdown in HFD mice improves glucose
  tolerance [PMID:31185508]. These are organismal phenotypes; not annotated.

### Decisions summary

- GO:0050833 pyruvate transmembrane transporter activity (IDA) -> MODIFY to
  GO:0005477 pyruvate secondary active transmembrane transporter activity (is_a
  GO:0050833 and GO:0015355), since proton coupling was shown in the same paper.
- GO:0008028 IBA: ACCEPT (family-level, Q8NCK7 is a donor). GO:0022857 IEA: MODIFY to
  GO:0008028.
- GO:0005886 (IBA/IDA/IEA): ACCEPT (functional site). GO:0005789 (IDA/IEA):
  KEEP_AS_NON_CORE (steady-state pool of overexpressed protein; not where transport
  function is shown).
- GO:0005515 BSG IPI: REMOVE per protein-binding policy (interaction is real; captured
  in description/core function text).
- GO:0006629 lipid metabolic process IDA: MARK_AS_OVER_ANNOTATED (downstream).
- GO:0015718, GO:1901475: ACCEPT. GO:0055085: MODIFY to GO:1901475.
