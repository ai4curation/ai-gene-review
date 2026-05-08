## katA notes

- UniProt `Q88QK9` / locus `PP_0481` is annotated as a catalase (`EC=1.11.1.6`) with heme as cofactor and the reaction `2 H2O2 = O2 + 2 H2O`, placing the protein squarely in the monofunctional catalase family. [file:PSEPK/katA/katA-uniprot.txt "RecName: Full=Catalase"; "EC=1.11.1.6"; "Name=heme"; "Reaction=2 H2O2 = O2 + 2 H2O;"]

- KT2440 transcriptomics gives strong strain-specific support for peroxide-response context: under H2O2 stress, `PP_0481 katA` is among the most induced oxidative-stress genes in the table summarizing differential expression. [PMID:28130298 "PP_0481 katA 3.4 936.5 7.7"]

- A P. putida oxidative-stress regulation paper in KT2442 shows that OxyR controls `katA` expression together with other principal peroxide-defense genes. This is not the exact KT2440 strain, so use it as close-strain support rather than as sole evidence for the core catalytic function. [PMID:17107553 "OxyR regulated the expression of two major catalases, KatA and KatB, along with peroxiredoxin, AhpC in Pseudomonas putida"; "This mutation was shown to cause the accumulation of a catalase (KatA)"; "OxyR controlled expression of all the principal peroxide-degrading enzymes in P. putida"]

- An older P. putida study functionally links catalase A to peroxide/disinfectant survival: cells lacking catalase A were more sensitive to peracetic acid, and low doses induced catalase A promoter activity. This supports peroxide-detoxification and hydrogen-peroxide-response context, although the paper is not framed around GO annotation. [PMID:11315113 "were more sensitive to killing by peracetic acid when they lacked a major catalase activity, catalase A"; "Low doses of peracetic acid induced promoter activity of the gene encoding catalase A"]

- The broad term `response to oxidative stress` is biologically fair but not the most specific core process. The tighter process term is hydrogen peroxide catabolism, with oxidative-stress response better treated as contextual physiology/regulation. [PMID:24957251 "defensive cellular systems involving induction of stress-sensing proteins and detoxification enzymes"; PMID:28130298 "The transcriptional levels of ... genes encoding detoxification enzymes (katA, katB, aphC, trxB, trx-2) ... had the most drastic changes in the presence of hydrogen peroxide at T1"]

- I do not currently have a completed Falcon-generated deep research file for this gene. The command was launched, but it had not produced an output file during this review window, so the YAML is based on direct source inspection plus the literature above.
