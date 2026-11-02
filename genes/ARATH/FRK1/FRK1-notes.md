# FRK1 (SIRK, At2g19190; UniProt O64483) — curation notes

## Identity

- UniProt O64483 (SIRK_ARATH), RecName "Senescence-induced receptor-like serine/threonine-protein kinase";
  AltName "FLG22-induced receptor-like kinase 1"; Name=SIRK, Synonyms=FRK1; At2g19190. The TAIR symbol is FRK1,
  which is the name used in the plant-immunity literature and for this review directory.
- 876 aa single-pass type I membrane protein [file:ARATH/FRK1/FRK1-uniprot.txt]:
  - signal peptide 1-24; extracellular domain 25-517; TM helix 518-538; cytoplasmic 539-876
  - ectodomain: malectin-like domain (PF12819, IPR024788) followed by three LRRs (415-483) —
    i.e. the malectin-like/LRR-RLK architecture of LRR-RLK subfamily I (IOS1-like; FunFam
    "LRR receptor-like serine/threonine-protein kinase IOS1")
  - cytoplasmic protein kinase domain 574-847 with ATP-binding loop 580-588, Lys601 and
    catalytic Asp697 ("proton acceptor") — canonical catalytic residues present, so FRK1 is predicted to be
    an active (RD-type? not checked) Ser/Thr kinase; no published in vitro kinase assay found.
  - phosphosites (Tyr646, Ser731, Thr732, Tyr745) annotated in UniProt from large-scale data.
  - PANTHER PTHR45631:SF202 (SENESCENCE-INDUCED RECEPTOR-LIKE SERINE_THREONINE-PROTEIN KINASE).

## Literature summary

### Discovery as a WRKY6 target in senescence (SIRK)
- [PMID:12000796 "One novel identified target gene, SIRK, encodes a receptor-like protein kinase,
  whose developmental expression is strongly induced specifically during leaf senescence."]
- [PMID:12000796 "The transcriptional activation of SIRK is dependent on WRKY6 function."]
- [PMID:12000796 "the SIRK gene promoter was specifically activated by WRKY6 in vivo, functioning very likely
  through direct W-box interactions."]
- This is regulation *of* SIRK; it does not show SIRK participates in senescence.

### Flagellin-induced marker gene (FRK1)
- Named FRK1 in Asai et al. 2002 (PMID:11875555; abstract-only in cache), where it served as an early
  flagellin-responsive reporter in the leaf protoplast system:
  [PMID:11875555 "We developed an Arabidopsis thaliana leaf cell system based on the induction of early-defence
  gene transcription by flagellin"]. UniProt INDUCTION: induced by WRKY22/WRKY29 and 30 min after flagellin.
- He et al. 2006 (PMID:16678099; abstract-only) used early MAMP marker genes (FRK1 among them, via the
  protoplast reporter system) to screen bacterial effectors:
  [PMID:16678099 "nonhost/nonpathogenic Pseudomonas syringae sustains but pathogenic P. syringae
  suppresses early MAMP (microbe-associated molecular pattern) marker-gene activation"]. This is the source of
  the TAIR IDA "defense response to bacterium" annotation. The abstract frames FRK1 as a readout; nothing in it
  indicates FRK1 loss-of-function was tested. Full text not available to me.
- FRK1 transcript is the standard qRT-PCR readout of flg22 signalling in many later papers, e.g.
  [PMID:29320478 "this correlated with a reduction in flg22-induced ROS burst and FLG22-INDUCED RECEPTOR KINASE1
  (FRK1) gene expression"] and [PMID:38895612 "Relative transcript level of FRK1 (At2g19190) upon Flg22
  induction."]. In PMID:38895612 the FRK1 measurement is a response to flg22 (a bacterial MAMP), not to a
  bacterium.
- Keppler et al. 2025 (PMID:39627368): leaf-microbiota "general non-self response"; the cached full text does not
  mention FRK1 by name (it presumably appears in supplementary expression data). The paper is an expression study
  of responses to commensal bacterial colonization and MAMPs: [PMID:39627368 "We link the GNSR to
  pattern-triggered immunity, as diverse microbe- or danger-associated molecular patterns cause dynamic GNSR gene
  expression."] FRK1 was not among the mutants tested for microbiota phenotypes
  [PMID:39627368 "The tested GNSR mutants harboured deficiencies in genes affecting the synthesis of secondary
  metabolites (IGMT3, CYP71A12, CYP71A13 and GSTF6)"].

### Extracellular interaction screen
- Smakowska-Luzan et al. 2018 (PMID:29320478) CSILRR ectodomain screen: FRK1 ECD interacted with ECDs of
  At1g12460 (C0LGE4), At3g28040 (Q9LRT1), Q9FRI1 and PXC2 (Q9LZV7). These are high-throughput in vitro ECD-ECD
  binding events (ECDs expressed in insect S2 cells), with no functional follow-up for FRK1:
  [PMID:29320478 "The ECDs cloned into the pECIA2 (for expression as bait) and pECIA14 (for expression as a prey)
  vectors were expressed using transient transfection of Drosophila Schneider 2 (S2) cells cultured at 27°C."]

### Single-cell fungal infection atlas (project context; Tang et al. 2023, PMID:37741284)
- Cached record is abstract-only; FRK1-specific statements below come from the user-supplied full-text PDF and
  cannot be used as verbatim supporting_text.
- Full text: "FRK1 is a well-established early immune response marker" and pseudotime analysis showed "a clear
  pattern of gradual increase in the FRK1 gene expression in cells with pseudotime values increasing from 0.5
  toward 1"; a pFRK1::3xVenus-NLS reporter showed "The strongest yellow fluorescence signals were observed in
  cells directly colonized by the fungus, and the fluorescence level gradually decreased in the neighboring
  cells" (Colletotrichum higginsianum, 48 hpi). FRK1 is used purely as a spatial marker of early immune
  activation in cells contacting hyphae; no frk1 mutant was analysed.
- Abstract (cached): [PMID:37741284 "Trajectory inference identifies cells that had different interactions with
  the invading fungus."]

### Closest characterized paralog: IOS1 (At1g51800)
- The PAINT nodes behind the IBAs (PTN005216631) use At1g51800, At1g51850, At1g51890, At5g59660 and FRK1 itself as
  donors. At1g51800 is IOS1, a malectin-like/LRR-RLK with genetic and biochemical evidence for PTI participation:
  [PMID:27317676 "Arabidopsis thaliana ios1 mutants were hypersusceptible to Pseudomonas syringae bacteria."]
  [PMID:27317676 "IOS1 also associated with BAK1 in a ligand-independent manner and positively regulated FLS2-BAK1
  complex formation upon MAMP treatment."] Notably, IOS1 function was read out *using* FRK1:
  [PMID:27317676 "ios1 mutants showed defective PTI responses, notably delayed upregulation of the PTI marker gene
  FLG22-INDUCED RECEPTOR-LIKE KINASE1"]. IOS1 shows what a functionally characterized member of this clade looks
  like; nothing comparable exists for FRK1, and function should not be transferred from IOS1 to FRK1 beyond the
  conserved kinase/plasma-membrane level.

### Priming marker study (PMID:38347062)
- FRK1 was identified as a priming-readout gene (expression after re-challenge of primed plants), not a
  priming-marker gene: [PMID:38347062 "Instead, FRK1 expression is strongly activated when primed plants are
  rechallenged, indicating its role in a state of greatest distress."] Its "central node" status in that paper
  comes from STRING co-expression/database interactions: [PMID:38347062 "Our disclosure of the protein interaction
  network was primarily based on the co-expression of encoding genes (Supplementary Dataset S1)."] The database
  interaction partners listed for FRK1 (Table 2) are mostly LRR-RLKs from large-scale ectodomain/cytoplasmic-domain
  screens (and include AT5G10020).

### Kinase competency (bioinformatics)
- [file:ARATH/FRK1/FRK1-bioinformatics/RESULTS.md "all canonical catalytic motifs of a eukaryotic protein kinase are intact"]:
  GKGGFG loop 581-586, VAVK (K601), alphaC E617, HRD 695-697 (catalytic D697), DFG 715-717. FRK1 is an RD
  kinase predicted to be catalytically competent (not a pseudokinase).

### Possible confusion to avoid
- The coordinator's guidance mentioned FRK1/SIRK kinase substrates "VII-1/VII-2". I found no publication
  reporting FRK1 (At2g19190) phosphorylating RLCK VII members or any other substrate (PubMed and web searches for
  FRK1/SIRK/At2g19190 with phosphorylation/substrate/kinase activity/mutant). The similarly named
  SIRK1 (At5g10020, a different LRR-RLK) has its own literature on substrate phosphorylation; it must not be
  conflated with SIRK/FRK1 (At2g19190). If a specific FRK1 substrate paper exists, it should be added.

### Functional (loss-of-function / biochemical) evidence
- PubMed and web searches (title FRK1/SIRK; FRK1 + mutant/kinase activity) found no paper characterising an frk1
  mutant phenotype, FRK1 kinase activity, substrates, or ligand. FRK1 appears in the literature almost
  exclusively as a transcriptional marker. UniProt FUNCTION ("Involved in innate immune response of plants")
  is attributed to Asai et al. 2002, a marker-use paper.

## Deep research status
- `just deep-research-falcon ARATH FRK1 --fallback perplexity-lite`: falcon timed out after 600 s; the
  perplexity-lite fallback failed ("Provider 'perplexity' not available. Available: falcon, asta, openscientist").
- `just deep-research ARATH FRK1 --provider asta` produced FRK1-deep-research-asta.md, but the retrieval did not
  target FRK1: all 20 retrieved papers are unrelated (bioinformatics databases, IgAN proteomics, etc.). It is not
  used as evidence.
- The orphaned falcon job eventually completed (~18 min) and wrote FRK1-deep-research-falcon.md. It independently
  reaches the same conclusion as the manual synthesis:
  [file:ARATH/FRK1/FRK1-deep-research-falcon.md "No cognate extracellular ligand has been established for FRK1."]
  [file:ARATH/FRK1/FRK1-deep-research-falcon.md "It would therefore be unjustified to assign cellotriose, flg22, or IDA as its substrate or ligand."]
  Additional transcript-level leads it reports (not independently verified here; not cached): WRKY11 binds W-boxes
  in the SIRK promoter by EMSA (Ciolkowski et al. 2008, Plant Mol Biol); FRK1 induced CORK1-dependently by
  cellotriose (Tseng et al. 2022, Cells); FRK1 induced transiently by IDA peptide, plus a high-throughput
  FRK1-HSL2 ectodomain association (Lalun et al., eLife). All are regulation-of-FRK1 or untested interaction
  data; none tests FRK1 activity or an frk1 mutant. Falcon also found no FRK1 substrate (no VII-1/VII-2 claim).

## Curation conclusions

- MF: protein Ser/Thr kinase activity (IBA + domain/catalytic residues) is the only defensible activity;
  unverified biochemically. ATP binding fine.
- CC: plasma membrane (IBA; single-pass type I RLK topology). "extracellular region" (ISM, signal peptide
  prediction) is wrong for a TM receptor kinase.
- BP: only expression-based "response to" terms are defensible: response to bacterium; response to molecule of
  bacterial origin (flg22); response to fungus (Tang 2023; FRK1-specific evidence in uncached full text).
  "defense response to bacterium" implies participation in defence and is not supported by any functional
  evidence for FRK1 itself; IEP cannot support it, and the IDA (He et al. 2006) is a marker-gene readout.
- protein binding (IPI, CSILRR) is uninformative.
