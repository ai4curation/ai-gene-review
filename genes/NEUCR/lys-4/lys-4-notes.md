# lys-4 notes

## 2026-10-10

Reviewed Neurospora `lys-4` as the next compact fungal PAINT family after the
Hsp100, MAPK, glucanase, cytochrome-b5-reductase, MYST, and ALO1 batches.

`PTHR11133` is a small saccharopine dehydrogenase family whose PAINT file has a
clean fungal split. `PTN000875292` carries `GO:0009085 L-lysine biosynthetic
process` on the NAD(+), L-lysine-forming `LYS1`/`lys3` branch, seeded by
SGD `S000001473` and PomBase `SPAC227.18`. `PTN000875327` separately carries
the same process on the reciprocal NADP(+), L-glutamate-forming `LYS9`/`lys9`
branch, seeded by SGD `S000005333` and PomBase `SPBC3B8.03`. Q7SFX6 is in the
SF23 NAD(+), L-lysine-forming branch with S. cerevisiae `LYS1`, C. albicans
`LYS1`, and S. pombe `lys3`, so the lysine-biosynthesis IBA follows the right
PAINT node. The metazoan L-lysine catabolic process IBD on `PTN000875308` does
not propagate to the fungal enzymes.

The broad `GO:0004753 saccharopine dehydrogenase activity` IBA comes from
`PTN000123605`, a eukaryotic node seeded by both fungal reciprocal enzymes and
by plant/metazoan bifunctional proteins. That ancestor is reasonable for the
parent activity, but Q7SFX6 already carries the exact `GO:0004754`
NAD(+), L-lysine-forming term from UniProt/InterPro/Rhea/EC and by ISS from
S. cerevisiae LYS1, so the broad activity should be narrowed rather than
treated as a bad PAINT propagation.

The `GO:0005737 cytoplasm` rows are broad but safe. SGD's imported L-lysine
biosynthesis GO-CAM places LYS1 and LYS9 in the cytosol, and the PomBase
GO-CAM makes the same placement for lys3 and lys9. I did not add a new
Neurospora cytosol row because GOA only supports the broader ancestor term for
Q7SFX6.

The Ensembl Compara `GO:0003729 mRNA binding` row transfers from S. cerevisiae
LYS1. QuickGO currently resolves the donor to the single SGD IDA row from
PMID:20844764. That paper is a proteome-wide survey of unexpected yeast
RNA-binding proteins and describes Lys1 as one of the novel enzyme RBPs, but
PANTHER does not place RNA binding on `PTHR11133`, and there is no evidence that
RNA binding is a conserved function of the fungal LYS1 branch. The Neurospora
transfer is therefore a bad propagation of a yeast moonlighting observation.

I fetched PMID:14304863, the old Neurospora crassa saccharopine/AAA-pathway
paper cited by UniProt for pathway context. The cache has PubMed metadata only,
so it was verified as relevant but not used for a reaction-specific quote.
Manual web/PubMed searches for `Neurospora lys-4`, `NCU03118`, and
saccharopine dehydrogenase found the same 1965 paper and background/mechanistic
saccharopine dehydrogenase papers, but no newer direct Neurospora lys-4
enzymology that would alter the PANTHER/GOA review.
