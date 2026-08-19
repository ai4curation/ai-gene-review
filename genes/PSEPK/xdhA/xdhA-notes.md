# xdhA (PP_4278; Q88F21) curation notes

## Evidence retained

- UniProt/InterPro identify the bacterial XDH small-subunit architecture, including FAD- and [2Fe-2S]-binding domains [file:PSEPK/xdhA/xdhA-uniprot.txt, "DR   InterPro; IPR014307; Xanthine_DH_ssu."].
- Purified XDH from P. putida strain 86 oxidizes hypoxanthine and xanthine with NAD+ as preferred acceptor and contains 91.0- and 46.2-kDa subunits [PMID:11341925, "XDH from P. putida 86 consists of 91.0 kDa and 46.2 kDa"]. This is a homologous strain-level exemplar, not direct KT2440 evidence.
- The OpenScientist report correctly separates XdhA's electron-transfer role from the XdhB molybdenum catalytic role and acknowledges that the KT2440 protein has not been studied directly [file:PSEPK/xdhA/xdhA-deep-research-openscientist.md, "No direct biochemical study of the KT2440 protein."].
- KT2440 can use hypoxanthine and xanthine as sole nitrogen sources, supporting pathway operation in the target strain without assigning the phenotype directly to XdhA [PMID:26355499, "permitting their use as sole nitrogen sources"].

## Curation decisions

- Change complete xanthine dehydrogenase activity from `enables` to `contributes_to`.
- Add intrinsic GO:0009055 electron transfer activity and complex-level contributions to hypoxanthine and xanthine dehydrogenase activities.
- Accept the specific FAD and [2Fe-2S] binding annotations; treat broader redox/cofactor parents as non-core or over-annotations.
- Add immediate hypoxanthine/xanthine catabolic processes and urate production, all explicitly inferred from the homologous bacterial complex.
- Do not assert a KT2440 oligomer, localization, exact electron path, or XdhC requirement from homolog data alone.
