# Echs1 notes

- UniProtKB:P14604 states: FUNCTION: Converts unsaturated trans-2-enoyl-CoA species to the corresponding 3(S)-3-hydroxyacyl-CoA species and plays a key role in the beta-oxidation spiral of short- and medium-chain fatty acid oxidation. [UniProtKB:P14604].
- Core interpretation: mitochondrial enoyl-CoA hydration and isomerization in fatty acid and amino acid catabolism.
- Accepted direct GO terms include: delta(3)-delta(2)-enoyl-CoA isomerase activity, enoyl-CoA hydratase activity, fatty acid beta-oxidation.
- Non-core/context terms are mostly localization, binding/cofactor, inferred pathway context, or exposure-response annotations; generic parent terms are modified when a specific catalytic term is available.

## Re-review 2026-10-10

**GOA changes.** Three new rows seeded (PENDING): GO:0005759 mitochondrial matrix (ISO,
donor human ECHS1 UniProtKB:P30084), GO:0006574 L-valine catabolic process (ISO, P30084),
GO:0046395 carboxylic acid catabolic process (IEA, ARBA, GO_REF:0000117). No rows retired.

**Actions.** GO:0005759 mitochondrial matrix (ISO): KEEP_AS_NON_CORE, mirroring the existing
mitochondrial matrix rows (localization context). GO:0006574 L-valine catabolic process (ISO):
ACCEPT, donor-split of the already-accepted valine rows (Echs1 hydrates methacrylyl-CoA /
3-methylcrotonyl-CoA valine-catabolism intermediates). GO:0046395 carboxylic acid catabolic
process (IEA): KEEP_AS_NON_CORE as a broad parent of the specific fatty acid beta-oxidation,
L-valine and L-lysine catabolic processes already accepted. No existing action changed.

**UniProt refresh.** The P14604 FUNCTION text was rewritten; the old quote ("...plays a key
role in the beta-oxidation spiral of short- and medium-chain fatty acid oxidation.") no longer
exists. All 23 occurrences (21 existing_annotations + 2 core_functions) were replaced with a
current verbatim sentence [UniProtKB:P14604 "Catalyzes the hydration of medium- and
short-chained fatty enoyl-CoA thioesters from 4 carbons long (C4) up to C16 (PubMed:10074351,
PubMed:7883013)"]. Note the new FUNCTION wraps "(2E)-enoyl- CoA" across a line, so quotes
spanning that break are not substrings; the hydration sentence above avoids it. 0 stale.

**Re-audit.** The two IBA rows (mitochondrion KEEP_AS_NON_CORE; fatty acid beta-oxidation
ACCEPT) are correctly handled: the propagation_review notes rat Echs1 members are among the
IBD seeds and does not treat them as circular. No GO:0005515 protein-binding rows. The two
core_functions entries (enoyl-CoA hydratase GO:0004300; delta(3)-delta(2)-enoyl-CoA isomerase
GO:0004165, both feeding fatty acid beta-oxidation) are coherent and left unchanged.
Description rewritten to remove curation commentary. status COMPLETE.
