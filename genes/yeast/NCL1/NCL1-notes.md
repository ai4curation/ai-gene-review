# NCL1 (TRM4, YBL024W; UniProt P38205) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: NCL1/Trm4 is the closest experimentally characterised relative of the
S. pombe benchmark gene trm402 (Trm4b, O13935). This review treats NCL1 in its own
right; no ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon yeast NCL1 --fallback perplexity-lite` failed: falcon
raised `Exception: Failed to authenticate` (Edison client auth), and the
perplexity-lite fallback returned HTTP 401 `insufficient_quota`. No deep-research
file exists. The review was built from primary literature cached in
`publications/` (listed below) and the UniProt record.

### Evolutionary placement (grounding for any transfer)

- PANTHER: P38205 is in PTHR22808:SF1 "RNA CYTOSINE-C(5)-METHYLTRANSFERASE
  NSUN2-RELATED", the same subfamily as S. pombe Trm4b (O13935)
  [file:interpro/panther/PTHR22808/PTHR22808-entries.csv]. S. pombe Trm4a (Q9HGQ2)
  is in SF29, human NSUN2 (Q08J23) in SF20, and NSUN4 (Q96CB9, mitochondrial 12S
  rRNA methyltransferase) in SF3.
- Müller et al. 2019 [PMID:30646830 "S. pombe show an unusual separation of
  activities of the NSun2/Trm4 enzymes that are united in a single enzyme in other
  eukaryotes like humans, mice and Saccharomyces cerevisiae"]: ScTrm4 combines the
  C34/C48 activities of Trm4a and the C49/C50 activity of Trm4b, so it is a
  co-ortholog of both fission-yeast paralogs. This matters for transfer: the
  multisite specificity of ScTrm4 must NOT be transferred wholesale to either
  pombe paralog.
- IBA rows come from PTN000516076, a deep node whose donors include mouse Nsun2
  (MGI:107252) and Nsun4 (MGI:1919431). The rRNA (cytosine-C5) MTase, rRNA
  processing and mitochondrial LSU assembly terms are carried only by the Nsun4
  donor (SF3), i.e. a different subfamily from Ncl1.

### Experimentally established in S. cerevisiae

1. Catalytic activity (IDA/EXP, in vitro recombinant + in vivo deletion):
   SAM-dependent tRNA m5C methyltransferase at C34, C40, C48 and C49
   [PMID:10445884 "Modification of tRNA occurs at all four positions (34, 40, 48,
   and 49) at which m5C has been found in yeast tRNAs sequenced so far."]. Sole
   enzyme for tRNA m5C [PMID:10445884 "Disruption of the ORF YBL024w leads to the
   complete absence of m5C in total yeast tRNA."]. C34 (tRNA-Leu(CAA)) and C40
   (tRNA-Phe) require the intron; C48/C49 do not [PMID:30646830 "Trm4 requires
   the presence of the intron to carry out C34 and C40 methylation, whereas its
   activity on C48 and C49 is independent of the intron"].
2. Wobble C34 methylation in vivo, H2O2-inducible [PMID:22760636 "there is a Trm4
   methyltransferase-dependent increase in the proportion of tRNA(Leu(CAA))
   containing m(5)C at the wobble position"], driving codon-biased (UUG)
   translation; trm4Δ is H2O2 hypersensitive and complemented by TRM4.
3. Domain architecture: N-terminal catalytic domain binds tRNA; C-terminal
   extension enhances catalytic efficiency [PMID:17567576].
4. Localization: nucleus including nucleolus, concentrated at nuclear periphery;
   non-essential; paromomycin sensitivity; no effect on ribosome subunit levels
   [PMID:9767141].
5. tRNA stability: trm4Δ trm8Δ double mutant shows rapid decay of tRNA-Val(AAC)
   (RTD pathway) [PMID:16387656].

### Evidence against rRNA roles

- Sharma et al. 2013 [PMID:23913415]: yeast 25S rRNA has two m5C (2278 by Rcm1,
  2870 by Nop2); 25S m5C was unchanged in Δtrm4 ("The peak corresponding to the
  m5C with a retention time of approximately 12 min reduces to half in the Δrcm1
  mutant compared with wild type and Δtrm4.").
- Wu et al. 1998 [PMID:9767141]: "Disruption of NCL1 does not affect steady-state
  levels of large and small ribosome subunits, monoribosomes, and polyribosomes."
- No evidence for mitochondrial localization or mitochondrial rRNA substrates.

### Inferred only (not established in this species)

- Cytoplasmic pool (IBA only).
- mRNA m5C methylation: not tested/established for Ncl1 in the cached literature;
  not proposed.

### Note on caches

PMID:16600899 was fetched by mistake (it is Marck et al. 2006, an RNA Pol III gene
family paper, not the Alexandrov RTD paper) and is not cited. The correct
Alexandrov et al. 2006 paper is PMID:16387656.

Reactome R-SCE-6790149 title says "5-methylcytidine-46" while its summary and
Motorin & Grosjean describe C49 of tRNA(Asp); the title appears to contain a typo.
