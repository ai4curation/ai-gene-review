# Toll-7 (Q7KIN0) — review notes

Batch 1 (Toll/TLR axis) of the INNATE_IMMUNITY project. Falcon deep research had not
started for this gene when the review was drafted; notes are built from the cached
GOA publications and the UniProt record.

## Neurotrophin receptor (core)

- [PMID:23892553 "Toll-6 and Toll-7 are expressed in the CNS throughout development and regulate locomotion, motor axon targeting and neuronal survival. DNT1 (also known as NT1 and spz2) and DNT2 (also known as NT2 and spz5) interact genetically with Toll-6 and Toll-7, and DNT1 and DNT2 bind to Toll-6 and Toll-7 promiscuously"].
- Olfactory wiring [PMID:25741726 "Toll-6 and Toll-7, members of the Toll receptor family best known for functions in innate immunity and embryonic patterning, cell autonomously instruct the targeting of specific classes of PN dendrites and ORN axons, respectively"].
- Binds Spz-1, -2, -5 cystine knots [PMID:31088910 "We found that the Toll-1 and Toll-7 ectodomains bind Spz-1, -2, and -5"].

## Antiviral role and the PRR question

- Nakamoto et al. 2012 (Cherry lab): [PMID:22464169 "Here we have shown that Toll-7 is a PRR both in vitro and in adult flies; loss of Toll-7 led to increased vesicular stomatitis virus (VSV) replication and mortality."]; [PMID:22464169 "We found that VSV interacted with endogenous Toll-7 at the plasma membrane, and that this interaction was lost upon RNAi depletion of Toll-7"]; autophagy induction is NF-kB/MyD88 independent [PMID:22464169 "MyD88 was also not required for the induction of antiviral autophagy"].
- Moy et al. 2014 (same lab), RVFV: [PMID:24374193 "Biotinylated RVFV but not control immunoglobulin G (IgG) precipitated endogenous Toll-7, suggesting that RVFV and Toll-7 physically interact at the cell surface"]; restriction is virus-specific (no phenotype with DCV, FHV, SINV).
- Chowdhury et al. 2019 (independent lab): Toll-7 ectodomain co-precipitates VSV, but so does Toll-1, and they note contrary data [PMID:31088910 "other results indicate that autophagy plays a minor role in hemocyte-mediated defense against VSV and does not depend on Toll-7"]. The contrary paper (their ref. 32) is not in the local cache and was not read.
- Assessment: Toll-7 is the only Drosophila Toll with direct pathogen-binding data. The binding evidence is co-precipitation of whole virions, no defined viral ligand molecule, no affinity or structural data, and the specificity control (Toll does not bind) is contradicted by Chowdhury et al. The GO:0038187 pattern recognition receptor activity (IC) and GO:0002752 cell surface PRR signaling pathway (IC) rows are therefore kept but as non-core, and flagged as a question; the direct observation GO:0046790 virion binding (IDA, two labs) is accepted.

## Canonical Toll pathway / AMP induction: conflicting

- Chowdhury 2019: Spz-bound Toll-7 activates drosomycin promoter in S2 cells [PMID:31088910 "Spz-1, -2, and -5 also activated the drosomycin promoter in S2 cells expressing full-length Toll-7 98-, 87-, and 83-fold"].
- Against: [PMID:10973475 "neither the 18W nor the Toll-6 to Toll-8 chimerae were able to induce drosomycin"]; [PMID:24374193 "Toll-7 is also dispensable for antimicrobial peptide induction after bacterial infection"]; and Nakamoto reports VSV-induced Toll-7 signalling is distinct from canonical Toll/IMD/JAK-STAT.
- Decision: GO:0008063 Toll signaling pathway and GO:0002225 positive regulation of antimicrobial peptide production (both IMP, PMID:31088910) -> UNDECIDED.

## Project question 1 answer (Toll-7)

Yes — Toll-7 is the one gene in this trio carrying PRR-branch terms (GO:0038187 IC and
GO:0002752 IC, both FlyBase from PMID:22464169). No GO:0002224 (toll-like receptor
signaling pathway) term is attached. The PRR terms rest on a single lab's virion
co-precipitation data; I keep them as non-core rather than remove them, and raise
the definitional issue (whole-virion binding vs. a defined PAMP) as a question.
