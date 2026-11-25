# raga-1 (Q22743, T24F1.1) manual literature research

No deep-research provider API was available for this review. The summary below was
assembled by hand from cached publications (`publications/PMID_*.md`) and PubMed
searches ("raga-1 AND elegans", 11 hits, searched 2026-10-28). Every claim carries the
reference it comes from.

## Identity and family

- raga-1 (T24F1.1, WBGene00006414) encodes a 312-aa Rag GTPase of the GTR/RAG family
  (Pfam PF04670 Gtr1_RagA; InterPro IPR039397 RagA/B; PANTHER PTHR11259:SF1). UniProt
  Q22743 is an unreviewed TrEMBL entry with no curated function text
  [file:worm/raga-1/raga-1-uniprot.txt "Belongs to the GTR/RAG GTP-binding protein family."].
- It is the only RagA/B orthologue in the worm
  [PMID:20523893 "raga-1 is the sole worm orthologue of the evolutionarily conserved ras-related GTPase RagA"].
  Its partner is RAGC-1 (RagC/D); mammalian RagA/B and RagC/D are obligate heterodimers
  [PMID:40385374 "In mammals, RagA/B and RagC/D form obligate heterodimers, while"].
- No biochemical work (GTP binding/hydrolysis, crystal structure, localization, direct
  partner binding) has been published on the worm protein in the papers examined. The
  molecular function and lysosomal location rest on orthology to yeast Gtr1 and
  mammalian RagA/B.

## Genetics: RAGA-1 positively regulates TORC1 in vivo

- Schreiber et al. 2010 isolated raga-1 in an RNAi screen for preserved swimming in old
  animals. Nucleotide-state mutants were built by analogy with RagA: "DN (T18N in C.
  elegans raga-1) and GF (Q63L)" [PMID:20523893]. Deletions (ok386, ok701) and DN
  extended lifespan; GF shortened it; wild-type raga-1 rescued ok386 lifespan
  [PMID:20523893 "expression of wild-type raga-1 under its own promoter in the raga-1(ok386) background rescued lifespan to N2 lengths"].
- Epistasis with TOR RNAi: "While raga-1(GF) exhibited increased lifespan with TOR RNAi
  treatment compared to empty vector, raga-1(ok386) did not" [PMID:20523893].
- Lifespan extension of ok386 requires daf-16 and skn-1; is further extended by
  daf-2(e1368); and adds to rsks-1(ok1255) [PMID:20523893].
- ok386 adults are smaller [PMID:20523893 "On day one raga-1(ok386) adults were smaller than wild-type"];
  GF animals are also smaller, so size is not a clean dose readout.
- Robida-Stubbs et al. 2012 used adult-only RNAi of the Rag genes as TORC1-specific
  knockdowns; lifespan extension needs SKN-1 and DAF-16 [PMID:22560223, abstract-only in
  cache; the PMC full text (PMC3348514) was read through the PubMed tool and says the Rag
  GTPases were knocked down as TORC1-specific genes only in adulthood].
- Zhu et al. 2013: raga-1(RNAi) reverses nprl-3 suppression of elo-5 L1 arrest, and a
  raga-1(Q63L) transgene, ubiquitous or intestine-specific (ges-1 promoter), bypasses the
  mmBCFA-deficiency L1 arrest
  [PMID:23705068 "We found that 50.4% of elo-5(−) mutants containing the raga-1Q63L transgene bypassed L1 arrest"].
  RAGA-1 here is used as a TORC1 activator downstream of d17iso-glucosylceramide; the paper
  does not show that RAGA-1 senses the lipid.
- Biochemical TORC1 readouts: somatic AID of RAGA-1 lowers phospho-RSKS-1
  [PMID:37721956 "As expected, somatic AID of RAGA-1 or LET-363 resulted in decreased levels of phosphorylated RSKS-1"];
  endogenous CRISPR Q63L raises it, whereas the egIs12 Q63L transgene does not
  [PMID:40385374 "indicating that only the endogenous mutation is sufficient to increase mTORC1 activity"].
  Therefore the GF transgene's short lifespan may not be TORC1-mediated, and endogenous
  Q63L does not shorten lifespan [PMID:40385374].
- raga-1(ok386) raises AMPK T172 phosphorylation, and neuronal RAGA-1 controls
  lifespan non-cell-autonomously via mitochondrial dynamics [PMID:31411562].
- Neuronal AID of RAGA-1 extends lifespan without growth or fertility defects [PMID:37721956].
- Review: Blackwell et al. 2019 WormBook/Genetics review of TOR in C. elegans [PMID:31594908, abstract only].

## Synthesis

RAGA-1 is the worm RagA/B: a nucleotide-state switch GTPase, part of the RAGA-1/RAGC-1
heterodimer, that activates TORC1 in response to nutrients. All whole-animal outputs
(lifespan, growth, dietary-restriction response, development under mmBCFA deficiency)
read through TORC1 and are downstream consequences rather than activities of RAGA-1
itself.
