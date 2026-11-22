# acr-8 notes

## Data collection

- Live UniProt search for `gene_exact:acr-8 AND organism_id:6239` returned
  two C. elegans records: F2YQX1, the 535 aa cDNA-only clone translated from
  JF416644/AEA50892.1, and Q23355, the 540 aa WormBase-cross-referenced
  `ZC504.2` entry linked to WBGene00000047. Q23355 is the canonical review
  entry for this folder.
- `just fetch-gene worm acr-8 --uniprot-id Q23355 --force` seeded 20 GOA rows,
  including the eight PAINT IBA rows that F2YQX1 lacks.
- `just fetch-gene-pmids worm acr-8` confirmed that the UniProt-seeded ACR-8
  PMIDs are cached; the cached Boulin et al. 2008 L-AChR reconstitution paper
  was added manually from `publications/PMID_19020092.md`.
- `just mod-description-deep-research worm acr-8` wrote the WormBase gene
  description for WBGene00000047/Q23355.
- `just paint-losses worm acr-8` on the Q23355 review reported no IRD or IKR
  loss on the gene lineage.
- Remote deep-research generation was not available for acr-8: `falcon` and
  `perplexity-lite` were not registered providers in this checkout, so this
  review used the fetched UniProt record, WormBase description, cached primary
  papers, the PTHR18945 family review, and the merged HAECO/acr-8 ortholog
  review as curation inputs.

## Evidence synthesis

Gottschalk et al. 2005 purified native levamisole-sensitive receptor complexes
through tagged UNC-29 and identified ACR-8 as an additional nicotinic
acetylcholine-receptor alpha subunit. A full-length ACR-8::GFP fusion was
reported in body muscles, a small set of head and tail neurons, and nerve-cord
synapses. Surface antibody labeling then detected HA-tagged ACR-8 at only some
UNC-38-positive postsynaptic clusters. This supports ACR-8 as a subunit of an
acetylcholine-gated channel complex and places at least part of the ACR-8 pool
at postsynaptic plasma membrane clusters.

The same study gives the main boundary for this review. The canonical C.
elegans levamisole-sensitive acetylcholine receptor contains UNC-29, UNC-38,
UNC-63, LEV-1 and LEV-8/ACR-13. ACR-8 co-purifies with UNC-29 and is found in
some UNC-38 clusters, but acr-8 mutants were nicotine resistant rather than
levamisole resistant. The ACR-8-containing receptor population is therefore
represented as a native subset or alternative postsynaptic nicotinic receptor,
not as a required member of the canonical five-subunit L-AChR pore.

Boulin et al. 2008 reconstituted the canonical C. elegans L-AChR in Xenopus
oocytes from lev-1, lev-8, unc-29, unc-38, unc-63, ric-3, unc-50 and unc-74
and did not include acr-8 among the eight required genes [PMID:19020092 Eight
genes are required for functional reconstitution of the Caenorhabditis elegans
levamisole-sensitive acetylcholine receptor, "cRNAs corresponding to the 5
L-AChR subunit genes"]. That supports using RIC-3, UNC-50 and UNC-74 in
candidate ACR-8 reconstitution experiments while keeping ACR-8 outside the
canonical five-subunit LEV-8-containing L-AChR.

The H. contortus ACR-8 literature is useful comparative context rather than
direct evidence for the C. elegans gene. Hco-ACR-8 is most closely related to
C. elegans ACR-8 and LEV-8, and can join a parasite levamisole-sensitive
heteromeric receptor in oocytes, while strongylid parasites appear not to have
a clear LEV-8 ortholog. This parasite specialization should not be projected
back onto C. elegans ACR-8 as evidence that the worm protein carries the same
bulk L-AChR function as LEV-8.
