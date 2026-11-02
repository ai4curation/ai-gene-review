# xdhB (O54051) curation notes

## Evidence retained

- The original R. capsulatus study cloned adjacent xdhA and xdhB open reading frames encoding xanthine dehydrogenase and predicted that XdhB contains the molybdopterin cofactor [PMID:9515710, "molybdopterin cofactor"].
- The purified enzyme is an alpha2beta2 heterotetramer rather than an XdhB-only catalyst [PMID:9515710, "alpha2beta2-subunit structure."].
- The resolved R. capsulatus structure assigns the molybdenum cofactor to the 85-kDa XdhB subunit [PMID:19109249, "XdhB subunit contains the molybdenum cofactor"].
- The assembled enzyme oxidizes hypoxanthine to xanthine and xanthine to urate with concomitant NAD+ reduction [PMID:11796116, "catalyzes the oxidation of hypoxanthine to xanthine"].

## Curation decisions

- Accept broad GO:0016491 oxidoreductase activity as an intrinsic function of the catalytic subunit.
- Remove GO:0005506 iron ion binding because the FAD and [2Fe-2S] centers reside on XdhA.
- Replace free molybdenum-ion binding with GO:0043546 molybdopterin cofactor binding.
- Add `contributes_to` rows for GO:0070674 hypoxanthine dehydrogenase activity and GO:0004854 xanthine dehydrogenase activity, because the complete NAD+-dependent activities are properties of the assembled XdhAB enzyme.
- Add direct hypoxanthine catabolism, xanthine catabolism, and urate biosynthesis process rows, all grounded in the same two-step XDH chemistry.
