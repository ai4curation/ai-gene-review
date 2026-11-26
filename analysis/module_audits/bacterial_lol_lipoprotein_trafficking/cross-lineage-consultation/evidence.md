# Cross-lineage Lol gene consultation, 2026-11-07

## Identity and assay provenance

**CAUVC/CC_3705, Q9A261, 219 aa, Caulobacter vibrioides CB15.** Methods of
PMID36716372 explicitly identify CB15 genomic DNA and locus CC_3705. The frozen
UniProt record connects that locus to Q9A261/AAK25667.1/WP_010921532.1 and
PTHR35869:SF1, PF03548/IPR004564. This is CB15, not a silently substituted NA1000
strain. The unreviewed ProtNLM protein name is not functional evidence.

The full primary Results/Figs. 3–4 and Discussion distinguish native cviLolA
from cviLolAeco. The latter retains the Caulobacter body but has the final 12
residues replaced by the E. coli sequence to improve host interaction. Robust
carrier and LolB complementation require a permissive E. coli background lacking
Lpp; unmodified native cviLolA is a poor heterologous carrier complement.
Separating carrier from insertion activity by altering the retained loop
provides positive evidence for an insertion-capable Caulobacter body, rather
than merely assuming activity from an absent LolB homolog. That supports a
bounded inference to native bifunctionality. It does not measure native CB15
client flux, membrane preference or purified native-protein insertion.

The paper's in vitro failure for ecoLolAloop is a different, engineered E. coli
protein; it is not a negative assay of native Q9A261. Its discussion also
speculates about historical gene duplication/specialization. No ancestral
activity, loss node or universal family insertion capacity is manufactured here.
Later distant Bacteroidota LolB discovery limits the older sequence-search
absence generalization without invalidating the CB15 construct result.

**FLAJ1/Fjoh_1066, A5FL25, 259 aa, Flavobacterium johnsoniae UW101.**
PMID40050408 Results explicitly identify Fjoh_1066 as LolB1; Methods explicitly
name A5FL25 in the protein database used for analyses. The frozen UniProt record
maps this locus/strain to ABQ04099.1/WP_012023151.1 and DUF4292
(PF14125/IPR025634). No PANTHER ID is established or asserted. LolB2/Fjoh_1084 is
a different paralog, not a synonym.

Full Results/Figs. 2–6 and Discussion establish native deletion/complementation,
changes in client outer-membrane abundance and endpoint-specific functional
region phenotypes. In particular, GldK and GldJ are reduced in the mutant OM.
The methods assess IM contamination in OM fractions using succinate
dehydrogenase and protein patterns. This supports the client-localization
conclusion, but is not a direct topology assay of LolB1 itself. Structural
homology, lipoprotein architecture and native function motivate an insertion
mechanism; no purified LolB1 insertion reaction is reported.

Loop deletion reduces LolB1 abundance, so failure of that construct cannot be
read as residue-specific catalytic proof. The leucine substitution has different
effects on motility and amylase secretion. No sequence activity rule is created.
The engineered soluble form rescues native defects; it is not evidence that
wild-type LolB1 is a soluble periplasmic protein. Its periplasm-facing OM site is
an explicit inference from lipoprotein architecture and insertion role, not a
claimed direct localization assay. The presence of paralogs and retained OM
localization without known LolA/B proteins prohibit universal essentiality or
exclusive-pathway claims.

## NEW and core accounting

Both normal fetches yielded **zero original rows**, which remain preserved.
The absence of GOA records is not itself a reason to add annotations.

| Record | Proposal | Evidence boundary |
|---|---|---|
| CC_3705 | GO0140598 carrier MF, IC | Native LolA domains plus native/construct complementation; not isolated-protein IDA |
| CC_3705 | GO0044874 localization BP, IC | Cargo handling/insertion inference, not native CB15 flux |
| CC_3705 | GO0030288 periplasm CC, IC | Export signal and periplasmic carrier mechanism; not a validated Tat route or native fractionation |
| Fjoh_1066 | GO0044874 localization BP, IMP | Native client distribution and complementation with coherent insertion-component identity |
| Fjoh_1066 | GO0031241 periplasmic-side OM CC, IC | Lipoprotein architecture and LolB-like function, not an observed whole-protein topology |

The carrier core for CC_3705 and proposed insertion cores for both proteins state
those distinctions. An insertion NTR is used because GO0140598 requires moving
with cargo between locations and GO0140306 specifies release from the inner
membrane. No invented GO ID, root MF or redundant row is added for coverage.
Native context/insertion-mechanism uncertainty is retained as a biological
knowledge gap. No T9SS, gliding, amylase, capsule, survival or growth process is
proposed: those are downstream client/phenotypic endpoints here.

**Participation/comparator test:** these proteins supply cargo handling or an
insertion component; they are not simply substrates required for a pathway.
Fresh QuickGO queries found GO0044874 on same-role carriers P61316/Q88FS9 and
insertases P61320/Q88PX4. Those records test the annotation convention and are
not independent biological support. The local GO-CAM index contains neither
Q9A261 nor A5FL25, so it provides no competing role assignment. Current term
ancestry and comparator response are archived in `ontology-comparator.json`.
Only one BP is proposed per gene; no ancestor/descendant duplicates are added.

## Research and validation limits

Both actual configured Falcon attempts returned HTTP403 authentication failures.
No provider report was written manually. Full cached primary texts, official
identity metadata and fresh ontology/comparator results supply the review.

PAINT: Q9A261 is absent from the cached PTHR35869 tree, so its lineage is not
assessed despite the helper's trailing no-loss text. Fjoh_1066 has no source
PANTHER mapping. Neither limitation is presented as proof of an absent loss.

`baseline.json` freezes both seeded reviews and six raw/primary source hashes.
`check_preservation.py` verifies those sources, zero inherited rows, exact NEW
accounting and nonredundant proposals. Focused validation/render/history logs
and all released hashes are recorded in the final receipt and handoff.
