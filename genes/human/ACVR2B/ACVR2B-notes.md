# ACVR2B notes

## Manual literature synthesis, 2026-11-24

Falcon and Perplexity deep-research providers were unavailable in this runtime, so this review uses
the cached primary publications, Reactome records, the UniProt entry, the BMP9 GO-CAM, and the
already-merged ACVR2A/BMPR2/ACVR1B/BMPR1A receptor reviews as manual deep-research context.

ACVR2B encodes ActR-IIB, a single-pass type II TGF-beta-superfamily receptor kinase. The early
activin receptor work directly supports the canonical activity: activin binds ActR-IIB, the
ligand-bound type II receptor recruits ActR-IB/ALK4, and ActR-IIB kinase activity phosphorylates
and activates the type I GS domain [PMID:8622651, "activin binds directly to ActR-IIB"; PMID:8721982,
"Phosphorylation of the GS domain was dependent upon a functional ActRII"]. Type II activin
receptors are phosphoserine-containing transmembrane kinases and can autophosphorylate in cells
[PMID:8395525, "at least some of the phosphorylated sites arose from autophosphorylation"].

ActR-IIB also binds non-activin ligands. A GDF11/myostatin antagonist study used soluble ACVR2B/Fc
and showed GDF11 binding blocked by GASP-1 or GASP-2 [PMID:24019467, "GDF-11 bound readily to
ACVR2B/Fc"]. BMP3/ActRIIB signaling in colorectal cancer cells is a BMP ligand using the ALK4-SMAD2
branch rather than the SMAD1/5/8 BMP arm [PMID:31665064, "BMP3 binds to activin type IIB receptor"].
For BMP9, the direct ACVR2B evidence is a ternary extracellular BMP9-ALK1-
ActRIIB complex [PMID:22718755, "BMP9 with the extracellular domains of ALK1 and
ActRIIB"]. A pulmonary endothelial BMP9 paper assayed BMPR-II and ActR-II as
type II receptors, but in that naming convention ActR-II is ACVR2A rather than
ACVR2B/ActR-IIB, so it is not positive ACVR2B evidence. BMP3 can also use
ActRIIB in an ALK4/SMAD2 branch in colorectal cancer cells [PMID:31665064,
"BMP3 binds to activin type IIB receptor"]. These BMP-family data justify
adding BMP receptor activity for ACVR2B even though the existing GOA file has
only the activin-specific type II receptor term.

Several seeded BMP-related rows point to papers that do not actually establish ACVR2B in the cited
context. The hemojuvelin/hepcidin abstract explicitly reports that HJV uses ActRIIA and BMPRII but
not ActRIIB [PMID:18326817, "ActRIIA and BMPRII, but not ActRIIB"]. The human mesenchymal-stem-cell
osteoblast paper measured ACVR2B knockdown and found it insignificant for BMP2/4/6/7 responses
[PMID:18436533, "ACVR2B were expressed at low levels and were not found to play a significant role"].
The erythroferrone/hepcidin letter is abstract-only in the cache and names BMP2/6 sequestration from
ALK3 rather than ActRIIB, so the two iron-homeostasis rows remain unresolved rather than being
called a confirmed wrong-gene case [PMID:31800957].

The vascular and lymphatic annotations transferred from mouse Acvr2b via P27040 need donor-level
inspection. The accessible abstract of the cited ALK1 lymphatic paper establishes ALK1-pathway
involvement in early postnatal lymphatic development but not the exact endogenous type II receptor
used in each transferred process [PMID:19903896, "ALK1 signaling regulates the differentiation of
lymphatic endothelial cells"]. The cold-induced thermogenesis and adipose-development rows are
better supported: ActRIIB blockade in mice increased BAT mass, blocked brown-fat Smad3 signaling,
and improved cold tolerance [PMID:22586266, "ActRIIB blockade in brown adipose tissue enhances
mitochondrial function and uncoupled respiration"].

## BMP9 GO-CAM consistency

The BMP9 GO-CAM activity `gomodel:600ced8500002343/600ced8500002422` correctly uses ACVR2B as the
ActR-IIB type II receptor at the plasma membrane in BMP9 signaling, but its molecular-function term
is `GO:0016362` activin receptor activity, type II. That is a real ACVR2B activity, not the activity
depicted when the ligand is GDF2/BMP9. `GO:0098821` BMP receptor activity is the better match for
the model state.

The GO-CAM edge from ACVR2B to ACVRL1 cites the activin/ALK4 papers PMID:8622651 and PMID:8395525.
Those support the general type II-to-type I receptor activation mechanism but not BMP9-bound ALK1.
PMID:22718755 is the direct structural paper for the BMP9-ALK1-ActRIIB receptor complex and would
be a better ACVR2B/ACVRL1 context reference.
