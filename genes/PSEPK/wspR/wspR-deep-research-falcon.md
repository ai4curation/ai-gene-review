---
provider_requested: falcon
manual_fallback: true
attempted_command: just deep-research-falcon PSEPK wspR
attempted_on: '2026-03-21'
note: The Falcon deep-research command was started but did not return a result in this environment. This fallback file captures the requested deep-research output as a manual synthesis of primary literature and UniProt context.
---

# Research Report - wspR Gene Function in Pseudomonas putida KT2440

## Identity

`wspR` in this review corresponds to `PP_4959` / UniProt `Q88D68`, annotated in UniProt as a diguanylate cyclase from *Pseudomonas putida* KT2440. The protein carries receiver, PAS, GGDEF, and EAL domains, consistent with a response regulator-like c-di-GMP signaling enzyme.

## Functional Summary

The Wsp pathway in KT2440 is a seven-gene signaling module that controls the swim-to-attach transition. The key KT2440 study states that the wsp cluster regulates cyclic di-GMP levels upon surface contact and that WspR is the component that harbors the c-di-GMP-producing domain [PMID:32519402]. This places WspR as the output diguanylate cyclase of the Wsp system rather than as a DNA-binding regulator.

In downstream phenotypes, Wsp signaling promotes surface-associated biofilm formation and represses antibacterial K1-T6SS programs through a FleQ/FleN-dependent circuit [PMID:35178858]. Under antibiotic stress, tetracycline increases wsp operon expression via RpoS, and among the c-di-GMP enzymes tested, WspR shows the strongest effect on c-di-GMP accumulation and biofilm formation [PMID:39589111].

## Mechanistic Context

Foundational structural/biochemical work on WspR shows that it is a GGDEF-domain diguanylate cyclase regulated not only by phosphorylation-related signaling but also by product feedback. WspR binds c-di-GMP at an inhibitory site and shifts between oligomeric states during feedback inhibition, providing a plausible mechanism for controlling signal output in KT2440 as well [PMID:18366254].

## GO-Curation Implications

- `GO:0003824 catalytic activity` is too generic and should be replaced by `GO:0052621 diguanylate cyclase activity`.
- `GO:0000160 phosphorelay signal transduction system` is appropriate and can be retained.
- `GO:0006355 regulation of DNA-templated transcription` is indirect/over-annotated for WspR itself because transcriptional outputs are mediated through c-di-GMP and downstream regulators such as FleQ/FleN.
- `GO:0005886 plasma membrane` is likely incorrect for WspR itself; the upstream Wsp complex spans the envelope, but WspR is a soluble signaling enzyme.
- Strong candidate new KT2440 process annotations are `GO:0090606 single-species surface biofilm formation` and `GO:1902021 regulation of bacterial-type flagellum-dependent cell motility`.

## Key Evidence

- [PMID:32519402] The Wsp operon regulates cyclic di-GMP during the swim-to-attach decision, and WspR is the c-di-GMP-producing component.
- [PMID:35178858] Wsp signaling modulates K1-T6SS and promotes biofilm formation through FleQ/FleN.
- [PMID:39589111] Tetracycline induces wsp expression via RpoS, and WspR has the largest observed impact on c-di-GMP and biofilm formation among tested enzymes.
- [PMID:18366254] WspR is a structurally characterized diguanylate cyclase with inhibitory-site c-di-GMP binding and oligomerization-based feedback regulation.
