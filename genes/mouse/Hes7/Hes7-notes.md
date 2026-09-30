# Hes7 (mouse) review notes

UniProt Q8BKT2 (HES7_MOUSE), transcription factor HES-7, 225 aa. PANTHER PTHR10985
(BASIC HELIX-LOOP-HELIX TRANSCRIPTION FACTOR, HES-RELATED). Notch-module role: **Notch
target gene / segmentation-clock transcriptional repressor** (Hairy/E(spl) class).

## Structure / molecular function
- bHLH-Orange repressor with C-terminal WRPW Groucho/TLE-recruitment motif
  [PMID:11260262 "Hes7 has a conserved bHLH domain in the amino-terminal region and the WRPW domain at the carboxy-terminal end, like Hes1."]
- Represses N-box and E-box promoters in transfection
  [PMID:11260262 "In a transfection analysis, Hes7 represses transcription from the N box- and E box-containing promoters."]
- Binds N-boxes of the Lfng promoter and of its own promoter and represses them
  [PMID:16342160 "Hes7, another cyclically expressed protein, can bind to the N-boxes on both Lfng and its own promoters and repress their activity."]
- UniProt: "Transcriptional repressor. Represses transcription from both N box- and E box-containing promoters."
  Groucho/TLE interaction by similarity only (ECO:0000250).

## Notch pathway position
- Expression is Notch-dependent (direct Notch target)
  [PMID:11260262 "Promoter analysis indicated that Hes7 expression is controlled by Notch signalling."]
- Human HES7 is described as a direct Notch target and part of a negative feedback that attenuates Notch
  signalling [PMID:18775957 "HES7 encodes a bHLH-Orange domain transcriptional repressor protein that is both a direct target of the Notch signaling pathway, and part of a negative feedback mechanism required to attenuate Notch signaling."]
- Msgn1 + Notch activate Hes7/Lfng; Hes7 is the short-lived periodic repressor
  [PMID:21750544 "an activator, arising from the combined activity of Msgn1 and the Notch signaling pathway, and a short-lived periodic repressor, Hes7, which functions in an autoinhibitory feedback loop to periodically repress Hes7 and Lfng"]

## Segmentation clock / somitogenesis
- mRNA oscillates with 2-h period in PSM; null mice have unsegmented somites, lost A-P
  polarity; vertebrae/ribs disorganized; Lfng expressed continuously
  [PMID:11641270 "In Hes7-null mice, somites are not properly segmented and their anterior-posterior polarity is disrupted."]
- Protein oscillation depends on proteasomal degradation; negative autoregulatory feedback
  [PMID:12783854 "periodic repression by Hes7 protein is critical for the cyclic transcription of Hes7 and Lfng, and this negative feedback represents a molecular basis for the segmentation clock."]
- Protein instability (half-life ~22 min) is required for sustained oscillation
  [PMID:15170214 "instability of Hes7 is essential for sustained oscillation and for its function as a segmentation clock."]
- In Hes7-/- mice somites still form but irregularly [PMID:19779553 "Thus, in the absence of Lfng or Hes7 the process of somitogenesis is not properly regulated."]
- Heterozygotes show kinked tails (dose sensitivity) [PMID:11641270 "suggesting that the dose of Hes7 gene is important for normal tail structure."]
- Human HES7 missense in DNA-binding domain causes autosomal recessive spondylocostal dysostosis (SCDO4)
  [PMID:18775957].

## Expression
- PSM-restricted in mouse embryo [PMID:11260262 "Strikingly, Hes7 is specifically expressed in the presomitic mesoderm in a dynamic manner."].
  This argues that IBA "regulation of neurogenesis" (from deep HES family node PTN000105428) is not
  applicable to Hes7, which is not a neural Hes.

## Pathway-variant relevance
- Hes7 is a vertebrate (mammalian) PSM-specific Hes paralog; functional analogs are zebrafish her1/her7
  and chick hairy1/2; Drosophila has E(spl)/hairy. Clock uses negative autoregulation, not Notch-receptor
  activity per se.

## Deep research
- Falcon deep research was launched (`just deep-research-falcon mouse Hes7 --fallback perplexity-lite`);
  see status in the review/notes below.
