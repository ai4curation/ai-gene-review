# Fused PutA module audit notes

## 2026-11-06 — comparative sampling and evidence boundaries

Begin the comparative fused-PutA audit from published main 5f8f3b5c5e. Preserve the five existing gene reviews with 143 annotation rows and 16 raw/provider files. The existing module has three gamma-proteobacterial PutA exemplars, all with regulatory RHH domains. Check the catalytic architecture against non-regulatory type A and B proteins, including directly studied Bradyrhizobium, Geobacter, Sinorhizobium and Corynebacterium proteins. Verify exact experimental strains and sequences before assigning accessions; do not generalize sodium-coupled uptake from a catalytic PutA exemplar alone. Search comparative reviews and primary studies, reassess family selection and taxon scope, complete gene consultation, validate and open one dedicated PR; actual merge remains required.

Literature search identified PMID:28712849 and PMID:28990412 as comparative reviews; primary follow-up includes PMID:20133651 (Bradyrhizobium structure), PMID:24550478 and PMID:34506758 (Geobacter), PMID:28420730 (Corynebacterium), and PMID:24358297 (Helicobacter sodium/proline transport). Search identification is not itself a completed reference assessment.


## 2026-11-06 — cross-lineage integration

Completed eleven individual reviews while preserving 198 original/seed annotation payloads, order, the one historical NEW action, and 28 raw/provider files. Eight PutA exemplars now span the five characterized architecture/phylogeny classes and a Helicobacter comparison; three PutP exemplars include G27 as explicitly comparative inference. P12 transporter and J99 enzyme experiments are not G27 assays. Corynebacterium structural constructs do not establish native transport or membrane localization.

Curated sixteen references with 31 mined findings, including both comparative reviews (PMID:28712849; PMID:28990412) and the newly fetched 2025 SmPutA primary study (PMID:40738191). Individual catalytic, transport, and intermediate-handoff steps carry source evidence. The 2025 study names F7X6I3 and distinguishes crystallographic intermediates from simulation-based channeling.

Replace the narrow TIGR01238 GSALDH selector with full fused-PutA family IPR025703 plus the independently supported activity and same-polypeptide architecture. Current Geobacter, Corynebacterium and G27 records have IPR025703 but lack TIGR01238. Negative controls retain monofunctional RocA/PUT2 and non-proline PanF/ActP exclusions. Broaden quinone substrate identity from benzoquinones to CHEBI:36141; the reduced product remains a free-text descriptor rather than a guessed ontology identifier. Native quinone identity remains unresolved.

Bacterial scope is retained because the characterized catalytic architecture spans Pseudomonadota, Thermodesulfobacteriota, Campylobacterota and Actinomycetota. This is not a claim of universal bacterial distribution or a complete transport pathway in every enzyme source organism. The production-circuit checker separately enforces reviewed activity, fusion, and matched-strain evidence: 44 checks and six deliberate mechanism mutations. These rules do not turn a compiler family hit into proof of native flux. Full validation, publication and actual merge remain pending.
