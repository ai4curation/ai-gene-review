# pam17 review notes

## Manual deep research

Perplexity was already unavailable in this runtime during the `icp55` review, so I kept this review serial and used this manual note together with the seeded GOA rows, UniProt, the cached S. pombe localization paper, S. cerevisiae Pam17 primary literature, and the GO-CAM source.

## Function synthesis

S. pombe pam17 is the fission-yeast ortholog of S. cerevisiae PAM17 and is assigned to the narrow Pam17/PTHR28021 family. The fission-yeast protein has a predicted N-terminal mitochondrial transit peptide and two predicted transmembrane helices, matching a multi-pass inner-membrane PAM/TIM23-associated component.

The mechanistic evidence comes from S. cerevisiae. Pam17 is a membrane-bound, nonessential regulatory subunit that binds the TIM23 translocase and helps couple the presequence translocase to the matrix-side PAM import motor. Hutu et al. found that Pam17 binds Tim23 and that Pam17 and the Pam16-Pam18 J-complex bind the TIM23 complex through distinct sites [PMID:18400944]. Schiller found genetic interactions between PAM17 and TIM44 and argued that Pam17 acts early in matrix import, before Tim44 [PMID:19577659]. Caumont-Sarcos et al. placed Pam17 recruitment downstream of Tim50/presequence recognition in a handoff from TIM23 to PAM [PMID:32130909].

No S. pombe paper assigns pam17 an autonomous molecular activity. The known biology supports a component/regulatory role in the PAM/TIM23 import machinery, so the PomBase ND molecular_function row should remain.

Manual searches for `SPAC167.04`, `Schizosaccharomyces pombe pam17`, and `pam17 fission yeast` found database records but no S. pombe biochemical paper assigning a direct molecular activity to pam17.

## GO-CAM context

GO-CAM 69729a3800007453 uses pam17 as a molecular_function root activity that occurs in the mitochondrial inner membrane and is part of protein import into the mitochondrial matrix. The root MF agrees with the accepted ND molecular_function row in this review.

The activity node gomodel:69729a3800007453/6994852c00000321 has root molecular_function but still has causal edges to downstream import activities. Those edges should be revisited in the final shared GO-CAM consistency PR because the gene product has no asserted molecular function to causally connect.
