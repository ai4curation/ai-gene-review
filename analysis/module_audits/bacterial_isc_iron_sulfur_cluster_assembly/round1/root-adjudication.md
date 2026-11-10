# Isc review follow-up: root adjudication

## Historical proposal lifecycle

Finding 5 requests deletion of the historical PSEPK HscA GO:0140662 proposal on the premise that `retired` means only a GOA withdrawal. The schema instead defines it as "Whether the annotation is retired or replaced". The GOA synchronization helper is one producer of this flag, not a narrower schema definition. The preserved annotation explicitly says the prior proposal is withdrawn, retains its original source payload and NEW action as history, and has `retired: true` at annotation level. The original proposal is separately archived.

The executable consumer check in retirement-semantics.json demonstrates that the current module function assessor gives no support for GO:0140662 from this row. Clearing only its retirement flag changes that result to ANNOTATION_SUPPORTED. Thus the actual module consumer does not treat the withdrawn proposal as live. This is not a claim about unspecified external tools. We retain the explicit lifecycle record and archive rather than erase the historical row; no new folding assertion is made.

## Shared Hsp70 family context

Finding 7 correctly identifies lost summary detail. The family summary now again names the compartment-specific paralogs, targeting and KDEL/HDEL/GPTIEEVD signals, and the relevant PAINT nodes. Direct inspection confirms that no cellular-component IBD in this cached slice sits on family-root PTN000452648. The source distinction for E. coli HscA is also explicit again: official release-19 sequence classification assigns SF176; UniProt and the cached entries table stop at PTHR19375. This is missing subfamily granularity, not a conflicting named subfamily.

## Encoded mechanism and boundary comparisons

Suggestion 8 is addressed by making the opening description explicit: the encoded route is Fdx-supported and HscBA-assisted. Anaerobic Fdx-independent capacity and IscU suppressor bypasses are comparative boundary cases, not additional routes encoded by this particular model. The title, node label and finite capacity oracle already distinguish that scope; failed canonical-role tests do not assert failure of every possible ISC implementation. No unknown alternative reductant is assigned an invented family or enzyme identity.

The Bacteria context is an occurrence envelope supported by the cited comparative literature. It does not assert that the three sampled gammaproteobacterial panels experimentally cover all bacterial phyla. The existing notes state that limitation. Adding Gammaproteobacteria as another root taxon would change the intended context rather than record the sampling metadata.

Gene evidence/action findings are assessed separately in the AZOVI and ECOLI/PSEPK consultations. Their source-specific outcomes will determine the final family activity wording; different assay access and organism specificity may legitimately yield different uncertainty states.
