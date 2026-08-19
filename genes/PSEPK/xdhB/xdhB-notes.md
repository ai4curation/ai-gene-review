# xdhB (PP_4279; Q88F20) curation notes

## Evidence retained

- UniProt/InterPro identify the xanthine-dehydrogenase molybdopterin-binding subunit architecture [file:PSEPK/xdhB/xdhB-uniprot.txt, "DR   InterPro; IPR014309; Xanthine_DH_Mopterin-bd_su."].
- The complementary XdhA protein contains the specific ferredoxin-type [2Fe-2S] signatures [file:PSEPK/xdhA/xdhA-uniprot.txt, "DR   InterPro; IPR006058; 2Fe2S_fd_BS."].
- Purified XDH from P. putida strain 86 oxidizes hypoxanthine and xanthine with NAD+ as preferred acceptor and contains distinct large and small subunits [PMID:11341925, "XDH from P. putida 86 consists of 91.0 kDa and 46.2 kDa"]. This supports a homologous architecture, not direct KT2440 biochemistry.
- KT2440 can use hypoxanthine and xanthine as sole nitrogen sources, confirming target-strain pathway flux without assigning the phenotype directly to XdhB [PMID:26355499, "permitting their use as sole nitrogen sources"].
- The OpenScientist report independently recovers the complementary subunit boundary and explicitly states that Q88F20 has no direct enzymology [file:PSEPK/xdhB/xdhB-deep-research-openscientist.md, "No direct enzymology on Q88F20 itself."].

## Curation decisions

- Change complete xanthine dehydrogenase activity from `enables` to `contributes_to` and add a corresponding hypoxanthine dehydrogenase contribution.
- Retain broad oxidoreductase activity as the available intrinsic catalytic-subunit function.
- Replace free molybdenum-ion binding with molybdopterin cofactor binding.
- Remove iron-ion binding: it appears to cross the multi-subunit enzyme boundary from the Fe-S-bearing XdhA module.
- Do not assign a homodimeric XDH complex term to the heteromeric XdhAB realization.
- Do not import the report's target-specific XdhA2B2 stoichiometry, cytosolic location, exact XdhC requirement, Mo-MCD form, active-site residue numbering, AlphaFold metrics, methylxanthine range, or electron path. The terminal acceptor for KT2440 remains inferred from EC 1.17.1.4 and homologous XDH rather than directly measured.
