# NAA10 (ARD1A) research notes

UniProt P41227, NAA10_HUMAN, 235 aa. X-linked (Xq28).

## Core identity
NAA10 is the **catalytic subunit** of the NatA N-terminal acetyltransferase complex.
- UniProt: "RecName: N-alpha-acetyltransferase 10"; "AltName: NatA catalytic subunit Naa10"; EC=2.3.1.255.
- "Catalytic subunit of N-terminal acetyltransferase complexes which display alpha (N-terminal) acetyltransferase activity" [P41227 FUNCTION].
- "Acetylates amino termini that are devoid of initiator methionine" [PubMed:19420222] — i.e. co-translational Nt-acetylation of Ser/Ala/Thr/Gly/Cys/Val N-termini exposed after Met excision.
- Belongs to the "acetyltransferase family. ARD1 subfamily."

## Complex membership
- NatA = NAA10 + NAA15 (auxiliary/anchoring subunit). NAA15 confers N-terminal specificity and ribosome anchoring; free NAA10 (without NAA15) has different/internal-acetylation activity.
- NatA/HYPK complex = NAA10 + NAA15 + HYPK (HYPK modulates activity).
- NatE complex = NAA10 + NAA15 + NAA50.
- Structures: NatA crystal/EM with NAA15 and HYPK [PubMed:29754825; PubMed:32042062].

## Catalytic activities (RHEA, all EC 2.3.1.255), from UniProt CATALYTIC ACTIVITY
- N-terminal Gly, Ala, Ser, Val, Cys, Thr acetylation. Evidence PubMed:15496142, 19420222, 25489052, 29754825.

## Moonlighting / debated lysine-acetyltransferase roles
- Without NAA15, "displays epsilon (internal) acetyltransferase activity towards HIF1A, thereby promoting its degradation" [PubMed:12464182].
- "Represses MYLK kinase activity by acetylation" [PubMed:19826488].
- "Acetylates, and stabilizes TSC2, thereby repressing mTOR activity" [PubMed:20145209].
- "Acetylates HSPA1A and HSPA1B at 'Lys-77' which enhances its chaperone activity and leads to preferential binding to co-chaperone HOPX" [PubMed:27708256] — basis of GO:1904592 positive regulation of protein refolding.
- "Acetylates HIST1H4A" [PubMed:29754825].
- "Acts as a negative regulator of sister chromatid cohesion during mitosis" [PubMed:27422821] — basis of GO:2000719.
These are real but secondary/context-dependent moonlighting functions; the CORE is co-translational Nt-acetylation. Per batch instructions keep Nt-acetyltransferase as core.

## Localization
- Cytoplasm (also free cytosolic and cytoskeleton-bound polysomes) and Nucleus [PubMed:12464182, 15496142, 25489052, 25732826].
- Membrane HDA (PMID:19946888) = large-scale membrane proteome; non-core.

## Disease
- Ogden syndrome / N-terminal acetyltransferase deficiency (NATD, MIM:300855); X-linked, S37P (Ser-37→Pro) and other variants impair Nt-acetylation.
- MCOPS1 (Lenz microphthalmia, MIM:309800).

## Interactome (IPI protein binding)
Many IntAct HT interactions; key biologically-meaningful partners: NAA15 (Q9BXJ9), NAA50 (Q9GZZ1), NAA16 (Q6N069), HIF1A, HSPA1A/B (P0DMV8/P0DMV9). The bulk of GO:0005515 IPI annotations are HT screens; keep as non-core (real interactions but uninformative term).

## GOA notable
- GO:1990189 protein N-terminal-serine acetyltransferase activity (EXP/IBA) — CORE.
- GO:1990190 protein-N-terminal-glutamate acetyltransferase activity (IBA) — Glu/Asp acetylation is the NatB/NatC-type specificity; for NAA10 this is a phylogenetic over-transfer (NatA does Ser/Ala/Thr/Gly/Cys/Val, NOT acidic Glu/Asp). Mark as over-annotated.
- GO:0008999 protein-N-terminal-alanine acetyltransferase activity (EXP) — CORE.
- GO:0004596 protein-N-terminal amino-acid acetyltransferase activity (IDA) — CORE (parent MF).
- GO:0043022 ribosome binding (IDA, contributes_to) — real, supports co-translational action; accept (informative MF).
- GO:0031415 NatA complex (part_of) — accept core complex.
