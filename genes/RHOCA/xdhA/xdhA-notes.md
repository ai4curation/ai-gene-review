# xdhA (O54050) curation notes

## Evidence retained

- The original R. capsulatus study cloned adjacent xdhA and xdhB open reading frames encoding xanthine dehydrogenase and predicted two [2Fe-2S] clusters plus FAD on XdhA [PMID:9515710, "sites for two [2Fe-2S] clusters and FAD"].
- The purified enzyme is a heterotetramer rather than an XdhA-only catalyst [PMID:9515710, "alpha2beta2-subunit structure."].
- The resolved R. capsulatus XDH structure assigns the two [2Fe2S] clusters and FAD cofactor to the 50-kDa XdhA subunit [PMID:19109249, "XdhA subunit harbors two [2Fe2S] clusters as well as a FAD cofactor"].
- The assembled enzyme oxidizes hypoxanthine to xanthine and xanthine to urate with concomitant NAD+ reduction [PMID:11796116, "catalyzes the oxidation of hypoxanthine to xanthine"].

## Curation decisions

- Change complete xanthine dehydrogenase activity from `enables` to `contributes_to` because XdhA is the electron-transfer subunit and the substrate-hydroxylating molybdenum center is in XdhB.
- Keep GO:0016491 oxidoreductase activity as non-core, add GO:0009055 electron transfer activity, and add `contributes_to` rows for GO:0070674 hypoxanthine dehydrogenase activity and GO:0004854 xanthine dehydrogenase activity.
- Accept the specific FAD and [2Fe-2S] binding rows. Treat free iron, broad iron-sulfur cluster, metal, and broader FAD annotations as over-annotations because more precise cofactor terms are available.
- Add direct hypoxanthine catabolism, xanthine catabolism, and urate biosynthesis process rows, all grounded in the same two-step XDH chemistry.
