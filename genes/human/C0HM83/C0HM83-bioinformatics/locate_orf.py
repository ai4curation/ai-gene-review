"""Locate the SHMOOSE ORF (UniProt C0HM83) in the human mtDNA reference (rCRS, NC_012920.1)
and translate it with the standard (table 1) and vertebrate mitochondrial (table 2) codes.
Pure python + NCBI E-utilities; no hardcoded results."""
import urllib.request, re

SHMOOSE = "MPPCLTTWLSQLLKDNSYPLVLGPKNFGATPNKSNNHAHYYNHPNPDFPNSPHPYHPR"  # from C0HM83-uniprot.txt
URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_012920.1&rettype=fasta&retmode=text"
seq = "".join(urllib.request.urlopen(URL).read().decode().split("\n")[1:]).upper()
print("rCRS length", len(seq))

bases = "TCAG"
aa1 = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
codons = [a + b + c for a in bases for b in bases for c in bases]
std = dict(zip(codons, aa1))
mito = dict(std); mito.update({"TGA": "W", "ATA": "M", "AGA": "*", "AGG": "*"})

def tr(s, code):
    return "".join(code.get(s[i:i+3], "X") for i in range(0, len(s) - 2, 3))

def rc(s):
    return s[::-1].translate(str.maketrans("ACGT", "TGCA"))

hits = []
for strand, s in (("+ (H-strand-encoded, same sense as ND5)", seq), ("- (L-strand-encoded)", rc(seq))):
    for frame in range(3):
        for name, code in (("standard", std), ("vert_mito", mito)):
            p = tr(s[frame:], code)
            i = p.find(SHMOOSE)
            if i >= 0:
                nt0 = frame + 3 * i
                start = nt0 + 1 if strand.startswith("+") else len(seq) - nt0
                hits.append((strand, frame, name, start))
                print(f"match strand={strand} frame={frame} code={name} start(1-based rCRS)={start}")
                orf = s[nt0:nt0 + 3 * (len(SHMOOSE) + 1)]
                print("  ORF nt (incl. next codon):", orf)
                print("  standard :", tr(orf, std))
                print("  vert_mito:", tr(orf, mito))
                codons_used = [orf[j:j+3] for j in range(0, len(orf), 3)]
                diff = [c for c in codons_used if std[c] != mito[c]]
                print("  codons that differ between codes:", diff or "none")
                if strand.startswith("+"):
                    # codon 47 position and allele at 12372
                    c47 = start + 46 * 3
                    print(f"  codon 47 spans rCRS {c47}-{c47+2}: {seq[c47-1:c47+2]} ; base at 12372 = {seq[12371]}")
if not hits:
    print("SHMOOSE sequence not found in any frame/code")
