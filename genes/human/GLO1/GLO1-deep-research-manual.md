# Manual literature synthesis for human GLO1 (Q04760)

## Scope and provenance

This manual synthesis replaces the unavailable automated report. The required
Falcon request failed with HTTP 402 and the configured Perplexity-lite fallback
failed with HTTP 401. Sources inspected were the reviewed UniProtKB record for
Q04760, the complete 27-row GOA file, all ten GOA-cited cached publications,
four additional primary structure/regulation papers (PMID:9218781,
PMID:10521255, PMID:17576200, and PMID:19199007), and the Reactome catalytic
reaction record.

## Core biochemical function

GLO1 is a zinc-dependent lactoylglutathione lyase (glyoxalase I). It catalyzes
the isomerization of the hemimercaptal formed spontaneously between
methylglyoxal and glutathione to S-lactoylglutathione. The cloning paper both
states the reaction and shows that expression of the human cDNA gives bacterial
cells high glyoxalase activity and methylglyoxal resistance. This is the first
enzymatic step of the two-enzyme glyoxalase pathway; glyoxalase II subsequently
hydrolyzes S-lactoylglutathione and regenerates glutathione.

The best-supported core picture is therefore a cytosolic, zinc-dependent
methylglyoxal-detoxification enzyme. `lactoylglutathione lyase activity`
(GO:0004462), `methylglyoxal catabolic process` (GO:0051596), and `cellular
detoxification of aldehyde` (GO:0110095) precisely capture the activity and
process. The broader `carbohydrate metabolic process` and `methylglyoxal
metabolic process` annotations should be replaced by the specific catabolic
term.

## Structure and catalytic residues

Human GLO1 is a homodimer. Each monomer contains two structurally related VOC
domains, and domain swapping places each active site at the subunit interface.
The essential zinc ion is coordinated by residues contributed by both subunits.
Mutagenesis of metal ligands, especially Glu172 in the publication numbering
(Glu173 in the current UniProt sequence), nearly or completely abolishes
activity. Transition-state-analogue structures support an inner-sphere
mechanism with a zinc-coordinated cis-enediolate intermediate and proton
transfer mediated by the catalytic glutamate.

These data support zinc ion binding as part of the catalytic mechanism but do
not require a second core function: zinc binding is a cofactor property of the
lactoylglutathione lyase activity. The generic InterPro-derived `metal ion
binding` term is less informative and should be replaced by `zinc ion binding`
(GO:0008270).

## Regulation

Native human GLO1 undergoes N-terminal methionine removal and acetylation and
contains redox-sensitive cysteines. Cys139 glutathionylation strongly inhibits
activity in vitro. TNF can induce phosphorylation, and NO-responsive forms have
been studied in cell-death and NF-kappa-B reporter contexts. These findings
show that GLO1 activity is regulated by cellular redox and signaling state, but
they do not establish a distinct catalytic activity or a universal signaling
role independent of methylglyoxal metabolism.

## Processes outside the conserved core

Experimental overexpression and inhibitor studies support resistance to
chemotherapy-induced apoptosis in selected human cancer cell lines. This is a
real perturbation phenotype but is context-specific and likely downstream of
metabolite detoxification, so it is retained as non-core. Osteoclast
differentiation is supported only by transfer from mouse and is likewise
non-core for the human review.

Cytosol is the coherent functional location. Nucleoplasm and plasma membrane
come from HPA immunofluorescence, while extracellular exosome records come from
discovery proteomics. Those observations are retained but do not redefine the
enzyme as a membrane, nuclear, or extracellular catalyst. The HuRI PUS10
interaction remains a high-throughput interaction observation; generic
`protein binding` is not an informative molecular function.

## Evidence boundaries

PMID:16130169 is abstract-only in the cache and its abstract does not expose a
GLO1-specific localization or apoptosis result. Those GOA annotations are not
rejected: cytoplasmic localization and context-specific apoptosis resistance
are independently supported by stronger GLO1-focused sources. The exosome
papers identify hundreds of proteins and do not provide a GLO1 mechanism.
Disease correlations and tumor overexpression were not extended into new GO
terms.

The alternative splice product Q04760-2 lacks residues 105-119, but no source
reviewed here determines whether it is catalytically active or whether it forms
mixed dimers with the canonical protein. This is the principal isoform-specific
knowledge gap.

