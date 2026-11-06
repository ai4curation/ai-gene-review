# cysK: Bacillus subtilis168

CysK is the principal PLP-dependent O-acetylserine sulfhydrylase of Bacillus subtilis168, forming cysteine from O-acetylserine and sulfide. The homodimer also binds the transcriptional repressor CymR and stabilizes promoter association. O-acetylserine weakens this regulatory complex, coupling enzyme-substrate availability to cysteine-metabolism gene expression. CysK does not require a CysE-CysK complex for catalysis under the tested conditions.

168 trpC2 and specified derivatives; cysE14 phenotype uses QB944 (trpC2 purA26 cysE14). PMID17056751 pDIA5708 is pET22b+cysK, C-terminal His6. PMID18974048 also MBP-CysK pDIA5796, Factor X-cleaved CysK controls; +1..+924 matches308-residue coding length.

PMID18974048 directly tests enzyme activities and CymR-CysK association; negative CysE-CysK tests include alternate tag positions, MBP-cleaved CysK and independent methods. No universally obligatory cysteine synthase complex is inferred. PMID17056751 places CysE/CysK in methionine sulfur utilization but does not show either enzyme cleaving methionine. Its negative CysK cystathionine assays were inspected in the full source, not inferred from the abstract title.

All 16 machine rows and raw sources are preserved in pristine-seed.json. Genuine Falcon failed403; manual source research is recorded here. PAINT loss query returned no IRD/IKR loss. No NEW process annotation is inferred from growth necessity; the regulatory function is represented by existing specific transcription-factor binding and complex rows.


## 2026-11-06 PR #6120 round-1 follow-up

Verified the full publisher Results again for PMID17056751 (DOI:10.1128/JB.01273-06): both the canonical serine/homocysteine assay and the OAS variant were negative for purified CysK. The exact frozen source row is UniProtKB:P37887, GO:0004122, IDA/ECO:0000314, PMID:17056751, assigned_by CAFA, date 20170124. Added a CONFIRMED MISSING_NEGATION source defect to that existing REMOVE decision, asking CAFA to withdraw the positive assertion and check an experimentally scoped NOT row. Attribution was read from GOA only to identify the upstream record; biological support is the primary result, not the GOA file. No source file or annotation payload was edited, and no external report was sent.
