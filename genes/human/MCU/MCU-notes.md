# MCU review notes

## Summary

MCU is the pore-forming, calcium-conducting subunit of the mitochondrial
calcium uniporter. The direct channel annotation is well supported by human
electrophysiology and reconstitution: the UniProt catalytic record maps MCU to
RHEA:29671, and direct papers assayed MCU as a ruthenium-red-sensitive
calcium channel in the inner mitochondrial membrane.

The family split that matters for this review is MCU versus MCUB. MCU retains
the pore function and calcium-import process, while MCUB belongs to a related
inhibitory clade. PANTHER PTHR13462 already places calcium channel activity
(`GO:0005262`), uniplex complex (`GO:1990246`) and mitochondrial calcium ion
homeostasis (`GO:0051560`) at the eukaryotic root and correctly prunes channel
MF from the MCUB clade, but the older `GO:0015292` uniporter-activity IBD is
a term-scoping mismatch for a pore and should be retired in favor of
`GO:0005262`.

Production GO-CAM `gomodel:65d7e4ac00002808` captures the MCUB inhibitory
model. Its MCU activity uses `GO:0005262` part_of `GO:0036444` in the
mitochondrial inner membrane, which is consistent with this review and with
the existing `modules/mitochondrial_calcium_uniporter.yaml` module.
