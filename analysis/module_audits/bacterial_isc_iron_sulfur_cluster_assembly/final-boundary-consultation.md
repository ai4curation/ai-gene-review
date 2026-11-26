# Final Isc module/member boundary consultation

Date: 2026-11-07 UTC. Read-only scientific consultation; the released gene reviews and receipts were not edited. The six-gene E. coli 39-file handoff was independently checked byte-for-byte and remains unchanged. No full validation was run.

## Recommendation

Retain IscS, IscU, Fdx, HscB and HscA as required roles **for the explicitly Fdx-supported, HscBA-assisted canonical route**. Retain IscA as optional, with condition- and client-dependent scope. This is a definition of a characterized implementation, not a claim that every bacterium or every oxygen condition requires all five proteins for any Fe-S synthesis.

Add the five Azotobacter representatives O31269 (IscS), O31270 (IscU), O69222 (Fdx), O69220 (HscB) and O69221 (HscA), preserving their different evidence strengths. Keep O31271 as an optional-accessory/comparator observation rather than a positive GO:0140132 cluster-delivery witness. Its released review supports broad cluster binding and native assembly participation, but does not settle native ligand chemistry or direct delivery. Do not substitute experiments on NifIscA for housekeeping IscA.

## Azotobacter Fdx: positive inferred realizer, not a demonstrated cognate electron relay

O69222 is a reasonable **qualified inferred** representative of the Isc electron-delivery role. The inference combines independent observations rather than relying on a generic ferredoxin label:

1. The primary deposit-to-UniProt bridge identifies the housekeeping isc-region product; native FdIV was identified by N-terminal sequencing and mass in PMID10542283. FdIV/FdxD is not FdI/FdxA.
2. Native protein spectroscopy establishes a reversible [2Fe-2S] cofactor and a reduction potential of −344 mV. This supports actual electron-carrier capability.
3. The frozen record contains the specific Fdx_isc classification IPR011536 and NCBIfam TIGR02007, in addition to broader ferredoxin classifications. Its verified PANTHER placement is PTHR23426:SF65; that family alone is insufficient.
4. Conditional depletion of the matched native ISC component impairs aconitase maturation and growth (PMID16936042), placing this redox protein within the relevant machinery.
5. E. coli primary experiments establish the mechanistic donor role (PMID23682711 and PMID25688831). Transferring that role to the specific Azotobacter ISC ortholog is an explicit inference, not a target-organism reconstitution result.

Missing native donor/acceptor identification prevents calling the Azotobacter electron chain directly demonstrated. It does not make the existing molecular-function claim false, nor require rejecting a carefully qualified orthology-based module realizer. The released GO:0022900 UNDECIDED action remains compatible: a defined series of native carriers was not demonstrated. In PMID16964969, apo-Fdx receives a cluster; that experiment must never be cited as electron donation by Fdx. Correlated Fdx/Fpr expression in PMID10542283 does not establish productive relay chemistry either.

Suggested representative wording:

> Housekeeping A. vinelandii Isc ferredoxin FdIV/FdxD. Native redox biophysics, Isc-specific family signatures and native ISC dependence support an inferred electron-delivery role; cognate donor/acceptor transfer has not been reconstituted in this organism.

A capacity result may therefore call the Azotobacter panel a supported/inferred canonical implementation. It must not call all five individual mechanisms experimentally reconstituted or label a whole matched native relay as proven. An assay-only evidence profile should remain partial at the Fdx donor edge. The same distinction applies to the inferred KT2440 roles.

## Anaerobic boundary: use the primary result, not a compressed secondary summary

[PMID26560204, Tanaka et al., DOI10.1111/mmi.13271](https://onlinelibrary.wiley.com/doi/10.1111/mmi.13271) was read at the publisher, including Results/Figures 4–7. In the Δsuf background, Δfdx and iscA mutants grew anaerobically without mevalonate; the source states “both were viable anaerobically without MVA”. Deleting iscS, iscU, hscB or hscA still required mevalonate under either oxygen condition. Separately, selected IscU mutations partially bypassed HscBA. Thus Fdx dispensability is an alternative within ISC, not merely SUF/NIF substitution. The statement in PMID36605734 that IscSU is minimal compresses these condition/genotype distinctions; do not present unmodified IscSU alone as the primary's demonstrated anaerobic minimum. Do not generalize growth rescue to restoration of every client protein or normal aerobic flux. Primary PMID26560204 is not newly cached by this consultation; root can fetch it normally if citing it in the module.

Recommended boundary text:

> This model describes the canonical Fdx-supported, HscBA-assisted Isc route. It does not encompass all experimentally possible reduced ISC implementations: oxygen conditions, scaffold suppressor variants and alternative reductant supply can change component requirements. Absence of a required role fails this particular route, not every possible Fe-S assembly mechanism in the organism.

A separate Azotobacter result is partial low-oxygen rescue of HscBA depletion; the depletion study does not demonstrate equal residual amounts of each component, and its aconitase defects should not be ranked quantitatively across different depletion strains. [Primary PMID16936042](https://pmc.ncbi.nlm.nih.gov/articles/PMC1636278/).

## Exact model edits and controls to retain

- Make the opening description and capacity-result labels say Fdx-supported/HscBA-assisted, rather than unrestricted bacterial Isc capacity. Replace the current generic essentiality explanation with the condition-limited boundary above. Optional IscA is defensible for this nascent-cluster/transfer scope; it does not mean IscA is dispensable for every aerobic [4Fe-4S] client in every background.
- Add Azotobacter HscA O69221 to the family-level classification realizer unless independent classification evidence resolves a subfamily. The frozen record has PTHR19375 only. The two HscA branches encode alternative classifications of **one role**, not two required proteins. Do not accept arbitrary DnaK/Hsp70 plus ATPase activity.
- Keep HscA GO:0016887 and HscB GO:0001671. All three panels now distinguish these measured/inferred activities from unresolved folding endpoints. ATP-driven scaffold remodeling and cofactor delivery are not automatically protein folding/refolding.
- The optional IscA step requires cluster delivery (GO:0140132), not merely cluster binding. O31271 should fail that exact optional catalytic/carrier qualification while remaining a valid accessory comparator; it must not make the five-role Azotobacter route fail.
- At the IscA function evidence, distinguish PMID15247288 iron donation from PMID11319236/15964837 cluster transfer. Iron chaperone activity and Fe-S cluster chaperone activity are different molecular claims even when the E. coli protein has both.
- Preserve same-taxon and cognate-interface evidence gates. The broad IscU family includes mechanistically different proteins such as SufU; family membership plus an undifferentiated binding annotation cannot fill the scaffold/carrier role. Broad ferredoxin and Hsp70 family hits likewise cannot independently fill specific ISC roles.
- A positive five-role test should survive omission of IscA. Removing Fdx or HscBA should fail the canonical profile while an explicitly separate anaerobic/suppressor context is recorded as outside that profile, rather than declared biologically impossible. An isolated Fdx redox protein or generic DnaK must fail. The Azotobacter Fdx contribution should pass the qualified-inference profile and remain unproven under a donor-edge-reconstitution-only profile.

The production compiler builds atom/part/variant circuits; its atoms contain family/function/member identifiers, not native assay strength, taxon context or pair compatibility. Those checks therefore belong to the documented evidence oracle. Requiring representative identity without explaining its evidence tier would conceal, rather than resolve, the Azotobacter donor-edge uncertainty.

## Evidence inspected

All eighteen released ECOLI/PSEPK/AZOVI core syntheses were compared with the proposed module roles. Source inspection included the frozen native FdIV abstract (PMID10542283), original Isc-region and native-depletion evidence (PMID9582371/16936042), Azotobacter transfer assay scope (PMID16964969), E. coli donor reconstitution (PMID23682711/25688831), conformational specificity (PMID22782893), the comparative reviews (PMID34781750/41970532), and the anaerobic primary above. The Azotobacter identity and strain caveats remain those documented in the released member map; DJ116 deposit identity is not silently relabeled as every subsequent experimental strain.

Inspected module SHA256 (before the proposed Azotobacter integration): `304ed453ca5cd4fc3d56bb292eab055a1a7c3832ac482ba30c8236ecbcb03b56`.

Released member-review SHA256 values at inspection:

- `genes/ECOLI/iscS/iscS-ai-review.yaml`: `fd137fdbede14059a0011d8a0bc134e6d9aadd06b03fe291eb1f61e82180714a`
- `genes/ECOLI/iscU/iscU-ai-review.yaml`: `28150a7156d663672fbf998802d29b7be9a70e2625ca305a0b2c76c5add0a83b`
- `genes/ECOLI/iscA/iscA-ai-review.yaml`: `69c328cce213ffe4493452ed3037d3a1e3e9d5772d58321230e44f888f00a2e6`
- `genes/ECOLI/hscB/hscB-ai-review.yaml`: `d0290a0b2ffa8d131691ad87116656a318e3a3370f965a89bf6ca9033d986313`
- `genes/ECOLI/hscA/hscA-ai-review.yaml`: `7b1be1f54c257341ee80a1c71128a74cb44b5fbb06e7b4b89dec492162637337`
- `genes/ECOLI/fdx/fdx-ai-review.yaml`: `8b889df43f594a40e5516b9d8817ad740d3690adee531eb611be26d4e9037d71`
- `genes/PSEPK/iscS/iscS-ai-review.yaml`: `facc02b9b9de870ae14682eeff005e2717097f7c5e8d1734c67d83b65b164734`
- `genes/PSEPK/iscU/iscU-ai-review.yaml`: `49e18572927817ef37a58c8cb2ed883e8eabc70c647f6d8a7339c296024ff18b`
- `genes/PSEPK/iscA/iscA-ai-review.yaml`: `3d4c7ba66bbaf0fdf161b127063cdc410de73b4dcdca2c79bd6a54259cf969dc`
- `genes/PSEPK/hscB/hscB-ai-review.yaml`: `5d52e40f1a08087e9f4aab5c97351fc8f3385efc58b52b699b835ad01ca92774`
- `genes/PSEPK/hscA/hscA-ai-review.yaml`: `a3206939a880a7c75f53c3be2dedd9ec851244e7e194636b27ac35ee4533b554`
- `genes/PSEPK/fdx/fdx-ai-review.yaml`: `a54ef4edbf818de68202e86b3f327bccaeac29c6d24875cd060e6d9bb0bcecda`
- `genes/AZOVI/iscS/iscS-ai-review.yaml`: `777b6fa93d7128f17a4723c991e0cd96431e999202f783a1165ee10f481dec39`
- `genes/AZOVI/iscU/iscU-ai-review.yaml`: `3612f21fe81b6de2a7c407553ee0be9a3df38b1c421c6257cf446bd664150c75`
- `genes/AZOVI/iscA/iscA-ai-review.yaml`: `c5966d49751e73d8e2c9eec330302cd80c9170c574b01a99d6091d8cada139fb`
- `genes/AZOVI/hscB/hscB-ai-review.yaml`: `b06eb4b0c30e884cfb3b4d25c989e0909970a8daf7908e027cfb5971393a65d5`
- `genes/AZOVI/hscA/hscA-ai-review.yaml`: `42d963afaa93af7749bbd117260076d72aae8518a6a18b78e552aa6d3564c22e`
- `genes/AZOVI/fdx/fdx-ai-review.yaml`: `fed1ba625807dc9e2b7fe876c980d63e8535c7195d6d57cc605794696ef50d09`
