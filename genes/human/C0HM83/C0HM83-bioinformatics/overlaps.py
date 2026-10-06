"""List rCRS (NC_012920.1) annotated features overlapping the SHMOOSE ORF (12234-12410, from locate_orf.out)
and report the reading-frame offset relative to MT-ND5."""
import urllib.request, re
ORF = (12234, 12410)
ft = urllib.request.urlopen("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_012920.1&rettype=ft&retmode=text").read().decode()
cur = None
for line in ft.splitlines():
    m = re.match(r"^<?(\d+)\t>?(\d+)\t(\S+)", line)
    if m:
        a, b, kind = int(m.group(1)), int(m.group(2)), m.group(3)
        cur = (min(a, b), max(a, b), kind, "+" if a <= b else "-")
        continue
    m = re.match(r"^\t\t\t(gene|product)\t(.+)", line)
    if m and cur and cur[2] in ("gene", "tRNA", "CDS") and cur[0] <= ORF[1] and cur[1] >= ORF[0]:
        print(f"{cur[2]}\t{cur[0]}-{cur[1]}\tstrand {cur[3]}\t{m.group(1)}={m.group(2)}")
        if cur[2] == "CDS" and "dehydrogenase subunit 5" in m.group(2):
            print(f"  frame offset of SHMOOSE start vs ND5 start: {(ORF[0]-cur[0]) % 3} (0 = same frame)")
