# mod (Modulo, CG2050, FBgn0002780; UniProt P13469) - manual literature synthesis

No deep-research API was available; this synthesis was assembled by hand from PubMed
searches (query `modulo[Title] AND Drosophila`, 12 hits) and the cached publications in
`publications/`. Full text was read for PMID:11854460, PMID:23028777, PMID:39700092 and
PMID:39848495; the others are abstract-only in the cache.

## Identity and domain architecture

- 542 aa nuclear protein; N-terminal acidic/disordered region (1-166), four RRM domains
  (175-251, 258-331, 340-429, 420-489), basic C-terminal tail (UniProt P13469 FT lines).
- Described as the Drosophila homologue of nucleolin [PMID:16877538 "identified it as
  Modulo, the Drosophila homologue of nucleolin"]. Note it lacks the GAR/RGG domain typical
  of vertebrate nucleolin; the architecture (acidic N-terminus + tandem RRMs + basic tail) is
  nucleolin-like.
- PANTHER places it in the very large PTHR24012 "RNA BINDING PROTEIN" family together with SR
  proteins and hnRNPs; this is the origin of the splicing and nuclear-speck IBA rows.

## Nucleic acid binding

- Direct DNA binding [PMID:1425581 "The mod protein directly binds DNA, which indicates that it
  may serve to anchor multimeric complexes promoting chromatin compaction and silencing."].
- Structure/function: basic terminal domains bind DNA without sequence specificity; the central
  RRM domain recognises a specific RNA motif class; phosphorylation down-regulates DNA binding
  [PMID:10037720 "two basic terminal domains independently contact DNA without sequence
  specificity, whereas a central RNA Recognition Motif (RRM)-containing domain allows
  recognition of a novel sequence-/motif-specific RNA class"].
- Nucleolar Mod is phosphorylated and in an RNP particle; chromatin-bound Mod is not
  [PMID:10037720 "in vivo nucleolar Modulo is highly phosphorylated and belongs to a
  ribonucleoprotein particle, whereas chromatin-associated protein is not modified"].
- Sdic promoter-binding protein purified from testis was identified as Modulo
  [PMID:16877538 "we purified the protein that specifically binds to the promoter of
  spermatid-differentiation gene Sdic and identified it as Modulo"]. This specific-binding
  claim sits uneasily with the 1999 in vitro finding of non-specific DNA binding.
- RIP-seq in larval brain identified bound mRNAs, including proneural and ribosomal-protein
  transcripts [PMID:39700092 "Mod targets were identified using RNA immunoprecipitation coupled
  to Sequencing (RiP-Seq)"].

## Localization

- Nucleolus (major) and chromatin/heterochromatin (minor) [PMID:9718368 "While actually
  associated to condensed chromatin and heterochromatin sites, the protein is also abundantly
  found at nucleolus."]; DNA targets are repetitive elements, not rDNA [PMID:9718368
  "repetitive elements instead of rDNA constitute Modulo DNA targets"].
- Embryonic nuclei, mostly nucleolar; polytene chromosome bands and heterochromatin shared
  with dCBP [PMID:11854460, full text].
- S2 cells: nucleolar in interphase, perichromosomal in metaphase, not at centromeres
  [PMID:23028777 "In interphase, we confirmed that Modulo accumulates at the nucleolus and has
  a weaker staining on DNA"; "Metaphase spreads showed localization of Modulo around the
  periphery of chromosomes"].
- Neuroblasts: nucleolar (Fibrillarin overlap) in interphase; perichromosomal and cytoplasmic
  in mitosis [PMID:39700092].

## Interactions

- dCBP (nejire): yeast two-hybrid, GST pulldown, co-IP from Kc cells; Mod 219-493 suffices
  [PMID:11854460 "We also found that amino acids 219–493 of Modulo are sufficient to"].
- CAL1 (CENP-A loading factor): reciprocal co-IP from S2 nuclear extracts [PMID:23028777
  "Western blot analysis detected Modulo itself (Fig. 1D) and CAL1 (enriched eight fold
  relative to the mock IP), further confirming their interaction."].
- Piwi: reciprocal co-IP in ovaries [PMID:39848495 "This study shows that the
  chromatin-associated factor Modulo (Mod) (34, 35) interacts with Piwi in ovaries and is needed
  for the epigenetic silencing of transposons and developmental robustness."].

## Biological roles (mostly genetic)

- Dominant suppressor of position-effect variegation; null is recessive lethal with melanotic
  tumours [PMID:1425581].
- Required downstream of patterning genes for morphogenesis of several embryonic tissues
  [PMID:7813788].
- Direct dMyc target required for growth of proliferative (not endoreplicating) cells
  [PMID:12834864]; null clones have a Minute-like phenotype, consistent with a role in
  ribosome biogenesis [PMID:9718368].
- Male germline: required for transcription of spermatid differentiation genes
  [PMID:16877538].
- Centromere integrity: RNAi reduces nucleolar CAL1, new CAL1 recruitment and centromeric CID;
  causes chromosome missegregation [PMID:23028777].
- Neuroblast maintenance [PMID:39700092]; piRNA-directed transposon silencing / H3K9me3 at TEs
  in ovaries [PMID:39848495].

All biological-process roles above rest on loss-of-function phenotypes; the molecular step
Modulo performs in each is not established.
