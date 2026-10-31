# Tardbp (rat, A0A8I6GLU8) - manual literature synthesis

No deep-research provider was available for this session. This synthesis was written by hand
from the cached publications in `publications/` (PMIDs below), with inline provenance.

## Identity

- UniProt A0A8I6GLU8 (TrEMBL, unreviewed), 414 aa, RGD:1310906, GeneID 298648. The entry carries
  the conserved TDP-43 architecture: TDP-43 N-terminal domain (Pfam PF18694), two RRMs (PF00076 x2)
  and the TDP-43 C-terminal low-complexity domain (PF20910); PANTHER PTHR48033:SF9 (TAR DNA-binding
  protein 43). The rat record contains no curated function text; its subcellular locations
  (nucleus, mitochondrion) are ARBA predictions.

## Rat experimental literature

- **RNA targets in rat cortical neurons (Sephton et al. 2011, PMID:21051541; full text read).**
  RIP-seq of endogenous TDP-43 from primary rat cortical neurons: "To identify RNAs associating
  with TDP-43, we used a modified RNA immunoprecipitation method followed by deep sequencing
  (RIP-seq) (27) from primary cultured rat cortical neurons". The (TG)n/(UG)n motif dominated:
  "The number of these sequences in TDP-43 showed a remarkable 55.1-fold enrichment when compared
  with the control library". Binding was intronic, exonic and in 3'-UTRs: "These results, taken
  together, suggest that TDP-43 regulates genes in three different modes. One is through binding
  sites in introns, one is through binding sites in exons, and another is through binding across
  both introns and exons." Co-purifying proteins (from mouse/rodent brain nuclear extracts) were
  mostly splicing and RNA-stability factors.
- **Nuclear compartments in rat neurons (Casafont et al. 2009, PMID:19539030; abstract only).**
  "TDP-43 is concentrated in euchromatin domains, specifically in perichromatin fibrils, nuclear
  sites of transcription and cotranscriptional splicing" and "a weak TDP-43 immunolabeling is
  found in nuclear speckles of splicing factors".
- **Protein misfolding (PMID:21608013; full text read).** Amino-acid analogues (canavanine, AZC)
  that cause misfolding raise TDP-43 levels in rat neurons: "Amino acid analogs induced increased
  levels of TDP-43 and its cleavage products." The paper does not mention the endoplasmic
  reticulum or ER stress.
- **Insulin secretion (PMID:21127054; full text read).** This paper is about PI3K-C2alpha
  (Pik3c2a): "down-regulation of the class II PI3K isoform PI3K-C2α specifically impairs insulin
  granule exocytosis in rat insulinoma cells". The full text never mentions TDP-43/Tardbp, so the
  RGD IMP row to Tardbp is most likely attached to the wrong gene.

## Orthologue (human/mouse) literature underlying ISO/IEA rows

- Splicing regulation: TDP-43 binds UG-rich clusters and controls alternative splicing in a
  position-dependent manner [PMID:21358640 "we found that TDP-43 preferentially bound long
  clusters of UG-rich sequences in vivo"]; it represses non-conserved cryptic exons
  [PMID:26250685 "we found that TDP-43 repressed the splicing of nonconserved cryptic exons,
  maintaining intron integrity"]; first identified on CFTR exon 9 [PMID:11285240 "We have
  identified TDP-43, a nuclear protein not previously described to bind RNA, as the factor
  binding specifically to the (TG)m sequence"].
- Autoregulation and mRNA decay: mouse brain CLIP-seq [PMID:21358643 "TDP-43 autoregulates its
  synthesis, in part by directly binding and enhancing splicing of an intron in the 3'
  untranslated region of its own transcript, thereby triggering nonsense-mediated RNA
  degradation"]; [PMID:21131904 "The RNA-binding properties of TDP-43 are essential for the
  autoregulatory activity through binding to 3' UTR sequences in its own mRNA."]; tau mRNA
  [PMID:28335005 "Our findings indicate that TDP-43 suppresses tau expression by promoting the
  instability of its mRNA."]. Stabilisation of NFL mRNA via 3'-UTR [PMID:17481916].
- DNA binding: TAR DNA of HIV-1 [PMID:7745706 "TDP-43 bound strongly to double-stranded TAR DNA
  via its ribonucleoprotein protein-binding motifs"]; ssDNA binding to the prion-like domain
  [PMID:26735904].
- Phase separation: the CTD alpha-helical segment drives LLPS [PMID:27545621, PMID:29511089].
- Amyloid-like assemblies: physiological myo-granules in regenerating muscle [PMID:30464263].
- Circadian/CRY stability: [PMID:27123980 "TDP-43 stabilized CRY1 and CRY2, and its knockdown also
  shortened the circadian period in cultured cells."].
- Knockdown phenotypes in human cells (nuclear shape, cell cycle, apoptosis) via Cdk6 repression
  [PMID:18305152].
- Mitochondrial localisation in disease and with overexpression [PMID:27348499].
- Nuclear retention of TDP-43 by CHCHD10 [PMID:28585542]: TDP-43 is the cargo in this study, not a
  regulator of nuclear import.
