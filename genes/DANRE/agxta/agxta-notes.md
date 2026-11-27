# agxta notes

## Setup and provenance

- Fetched with `just fetch-gene` on Q6DG86 (TrEMBL, 391 aa; synonym agxtl); 7 GOA rows (5 IBA, 2 IEA),
  none with a PMID. ZFIN ZDB-GENE-040718-16, Ensembl ENSDARG00000052099, chromosome 6.
- The deleted TrEMBL entry F1QY24 (UniParc UPI00015A7661) that PMID:35295584 cites as "Agxta" has a sequence
  that differs from Q6DG86 at a single position (checked by fetching UPI00015A7661 from UniParc), so it is the same
  gene.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is invalid. Literature
  searched by hand via Europe PMC (`(agxt OR agxta OR agxtb OR "alanine-glyoxylate aminotransferase") AND zebrafish`,
  `"alanine:glyoxylate aminotransferase" AND (fish OR teleost ...)`, AGT targeting evolution queries).
- DANRE_DUPLICATION batch 4, random draw 11 (seed 20260928); paralog agxtb. PANTHER TGD_tree 1:1 pair
  (PTHR21152); Ensembl Compara places the duplication at Osteoglossocephalai.

## What is known about the zebrafish gene

- No experimental study of zebrafish agxta. The only specific statement is from a bioinformatic survey of the
  zebrafish peroxisomal proteome:
  [PMID:35295584 "Zebrafish also contains a putative peroxisomal alanine:glyoxylate aminotransferase (AGT) (Agxta, F1QY24 _DANRE) with a weak PTS1 (SRV), a key enzyme to prevent oxalate accumulation (Table 1 and Supplementary Table S3)."]
  and it contrasts agxtb
  [PMID:35295584 "Interestingly, zebrafish encode another putative AGT (agxtb, Q6PHK4_DANRE) which lacks a PTS1 but possesses an N-terminal MTS."]
- ZFIN curated expression (Thisse high-throughput in situ, ZDB-PUB-040907-1): liver and pronephric duct from
  the 20-25 somite stage to day 5 (bioinformatics output, section 9).

## Background: vertebrate AGT (AGXT) and its targeting

- PLP-dependent class-V aminotransferase converting glyoxylate + L-alanine to glycine + pyruvate; also
  serine:pyruvate aminotransferase. Deficiency in humans causes primary hyperoxaluria type 1
  [PMID:12899834 "A deficiency of the liver-specific enzyme alanine:glyoxylate aminotransferase (AGT) is responsible for the potentially lethal hereditary kidney stone disease primary hyperoxaluria type 1 (PH1)."].
- Organelle distribution varies between species and correlates with diet
  [PMID:21558762 "In herbivores, peroxisomal localization of SPT appears to be indispensable to prevent excessive oxalate production by removing glyoxylate, an immediate precursor of oxalate, formed from glycolate in this organelle."];
  [PMID:21558762 "In carnivores, its mitochondrial localization appears to be needed to metabolize glyoxylate formed from L-hydroxyproline in mitochondria."].
- Mechanism in mammals: one gene, two start sites. The upstream start adds a cleavable MTS and the downstream
  start makes a product that the C-terminal PTS1 sends to peroxisomes
  [PMID:21558762 "Transcription from the upstream start site generates the 1900-nucleotide mRNA for a 45-kDa precursor for SPTm containing a cleavable N-terminal mitochondrial targeting signal of 22 amino acids."];
  [PMID:10723739 "AGT targeting is dependent on the variable use of two alternative transcription and translation initiation sites which determine whether or not the region encoding the N-terminal mitochondrial targeting sequence is contained within the open reading frame."].
- Human AGT is peroxisomal and its KKL PTS1 needs an internal ancillary signal that Xenopus AGT lacks
  [PMID:15911627 "The PTS1A is present in all mammalian AGTs studied (human, rat, guinea pig, rabbit, and cat), but not amphibian AGT (Xenopus)."].
- Mammal-wide study (685 genomes, cell assays) of MTS/PTS1 evolution; Xenopus AGT used as the exclusively
  mitochondrial control
  [PMID:41781394 "The human AGT protein lacks a functional MTS start codon and has been shown to exclusively target the peroxisome27,60, whereas the Xenopus protein exclusively targets the mitochondria61."].
- Fish biochemistry (species not named in the abstract): hepatic AGT in freshwater fish is in both organelles
  [PMID:8954944 "The present report describes that hepatic alanine:glyoxylate aminotransferase is located both in the peroxisomes and in the mitochondria in fresh water fish, showing that the intracellular localization of the enzyme differs between fresh water fish and marine fish."].
  Purified mackerel liver AGT has AGT1-type substrate specificity
  [PMID:6697688 "It was specific for L-alanine and L-serine with glyoxylate and for L-serine with pyruvate as amino acceptor."].

## My analysis (agxta-bioinformatics/)

See `agxta-bioinformatics/RESULTS.md`. Key points:

- agxta starts at the residue equivalent to the mammalian downstream (peroxisomal-form) Met; its 5' UTR and genomic
  5' flank have an in-frame stop 16 codons upstream and no in-frame ATG, so no MTS-bearing isoform can be made.
- agxta ends SRV; agxtb has a 32-residue Arg-rich N-terminal extension that aligns with the gar extension and ends
  SKA. Spotted gar (unduplicated outgroup) has both a 38-residue Arg-rich extension and a C-terminal SKV.
  The pattern (a-copies without extension and with S[KR]V/NKM-type ends; b-copies with extension and mostly SKA
  ends) recurs across the teleost panel.
- Catalytic Lys209 (PLP) and the substrate Arg360 of human AGXT are conserved in both copies.
- agxta evolves faster than agxtb relative to gar (59 vs 32 unique changes; chi2 8.01).
- Expression overlaps widely (liver, kidney, intestine, spleen, head kidney in Bgee), like gar (liver, mesonephros,
  intestine). Larval whole-body TPM: agxtb higher than agxta at day 3-5.

## GOA review decisions (summary)

- MF (AGT, SPT) IBA/IEA: accepted; catalytic residues conserved.
- Peroxisome IBA: accepted; this is the copy that keeps a C-terminal PTS1-like tripeptide and has no MTS.
- Glyoxylate catabolism and glycine biosynthesis IBA: accepted (peroxisomal glyoxylate detoxification is the
  expected role of the peroxisomal copy), with the caveat that nothing has been measured in zebrafish.
