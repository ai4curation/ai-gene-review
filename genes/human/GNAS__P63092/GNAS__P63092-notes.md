# GNAS P63092 review notes

## Scope

This review covers the canonical Gs-alpha UniProt record, P63092, not every
protein product encoded by the complex imprinted GNAS locus.

The repository already has `genes/human/GNAS/GNAS-ai-review.yaml` for NESP55
(UniProt O95467). UniProt lists the XL-alpha-s products of GNAS as external
isoforms `Q5JWF2-*`; literature that assays XL-alpha-s or ALEX alone is therefore
not direct evidence for the P63092 Gnas-1/Gnas-2 canonical Gs-alpha products.

## Deep research

Automated deep research was unavailable in this checkout:

- `just deep-research human GNAS__P63092 --provider perplexity` failed because
  the configured client listed only `claude_code` as an available provider.
- `just deep-research human GNAS__P63092 --provider claude_code` failed because
  the wrapper rejected the underscore spelling.
- `just deep-research human GNAS__P63092 --provider claude-code` failed because
  the deep-research client was not logged in and no API key was available.

I proceeded with manual review of the seeded GOA publications, UniProt record,
Reactome context, and the cached GO-CAM.

## Core biology

Gs-alpha is the stimulatory alpha subunit of heterotrimeric G proteins. It sits
on the cytoplasmic face of the plasma membrane as a peripheral lipid-anchored
member of a heterotrimeric alpha/beta/gamma complex. Ligand-bound Gs-coupled
receptors promote GDP release and GTP binding on Gs-alpha; activated Gs-alpha
then stimulates transmembrane adenylyl cyclases to increase cAMP, and its
intrinsic GTPase activity hydrolyzes GTP back to GDP to terminate signaling.

The best core rows for P63092 are therefore `GO:0003925` G protein activity,
`GO:0003924` GTPase activity, `GO:0005525` GTP binding, `GO:0010856`
adenylate cyclase activator activity, `GO:0031683` G-protein beta/gamma-subunit
complex binding, `GO:0005834` heterotrimeric G-protein complex, and
`GO:0009898` cytoplasmic side of plasma membrane / `GO:0005886` plasma
membrane.

## XL-alpha-s and other GNAS-locus rows

Two older publications in the seed are about paternally expressed XL-alpha-s:

- PMID:7997272 describes XL-alpha-s as a new cholera-toxin target that contains
  a unique XL portion linked to a G-alpha-s sequence truncated at the amino
  terminus and reports its trans-Golgi-network association.
- PMID:12719376 studies a paternally inherited XL-exon1 insertion that alters
  both XL-alpha-s and ALEX and reduces the XL-alpha-s/ALEX interaction.

Rows whose direct support is the XL-alpha-s product should not be treated as
canonical P63092 claims, even though the broader GNAS locus is shared. The
abstract of PMID:12719376 also mentions increased platelet Gs-alpha levels in
carriers, so I did not claim the paper is an entirely wrong reference for the
general Gs/cAMP pathway; I treated its platelet and development rows as
over-annotations for canonical Gs-alpha.

PMID:35025664 is even clearer product separation: the olfactory receptor pathway
in mouse and human vascular macrophages uses the olfactory alpha subunit GNAL
with ADCY3, not canonical GNAS.

## GO-CAM 69b3372b00003343

The GO-CAM activity for P63092 is
`gomodel:69b3372b00003343/69c59f8a00001719`: `GO:0003925` G protein activity
at `GO:0009898` cytoplasmic side of plasma membrane, `part_of GO:0001541`
ovarian follicle development, with an indirect positive edge to the downstream
PRKACA activity.

The molecular function and location agree with this gene review. The outgoing
edge to PRKACA is also appropriately indirect because active Gs-alpha stimulates
adenylyl cyclase and cAMP production before cAMP releases active PKA catalytic
subunits. PMID:17110384 supports the Gs-to-adenylyl-cyclase step, not direct
PKA activation. I retained the follicle-development GOA row as a non-core FSHR
context: the GO-CAM uses the same FSH/FSHR/Gs structural context from
PMID:36720854, but the standalone core function of P63092 is generic
GPCR-to-cAMP signal transduction rather than ovarian follicle development.
