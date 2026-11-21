#!/usr/bin/env bash
# Build a single self-contained, phone-friendly HTML version of the paper with TeX4ht.
#   paper/scripts/build_html.sh        -> paper/html/aigr-paper.html
# Works on a copy in paper/.html_build so the PDF build's aux files are untouched.
# Figures: matplotlib PDFs -> SVG (pdftocairo); TikZ diagrams compiled standalone -> SVG.
# In the HTML copy \includegraphics emits a plain <img>, so graphicx never needs SVG sizes.
set -euo pipefail
cd "$(dirname "$0")/.."
B=.html_build
OUT=html
rm -rf "$B" && mkdir -p "$B/figures" "$OUT"
cp -r main.tex refs.bib html.cfg sections generated "$B/"
cp -r figures/tikz "$B/figures/"

for f in figures/*.pdf; do
  pdftocairo -svg "$f" "$B/figures/$(basename "${f%.pdf}").svg"
done

for t in figures/tikz/*.tex; do
  n=$(basename "${t%.tex}")
  cat > "$B/tikz_$n.tex" <<EOF
\\documentclass[tikz,border=4pt]{standalone}
\\usepackage[T1]{fontenc}\\usepackage{lmodern}
\\usetikzlibrary{positioning,arrows.meta}
\\begin{document}
\\input{figures/tikz/$n}
\\end{document}
EOF
  (cd "$B" && pdflatex -interaction=nonstopmode "tikz_$n.tex" >/dev/null && pdftocairo -svg "tikz_$n.pdf" "figures/tikz_$n.svg")
done

# HTML copy: PDF figures -> SVG, TikZ inputs -> their SVG, drop packages TeX4ht dislikes.
find "$B/sections" -name '*.tex' -print0 | xargs -0 sed -i -E \
  -e 's#\\resizebox\{[^}]*\}\{!\}\{\\input\{figures/tikz/([a-z_]+)\}\}#\\includegraphics{figures/tikz_\1.svg}#g' \
  -e 's#(figures/[a-z_]+)\.pdf#\1.svg#g'
sed -i -E \
  -e 's#\\usepackage\{tikz\}##; s#\\usetikzlibrary\{[^}]*\}##' \
  -e 's#microtype,##' \
  -e 's#^\\title\{#\\makeatletter\\ifdefined\\HCode\\renewcommand{\\includegraphics}[2][]{\\HCode{<img src="\#2" alt="figure" class="fig" />}}\\fi\\makeatother\n\\title{#' \
  "$B/main.tex"

(
  cd "$B"
  htlatex main.tex "html.cfg" " -cunihtf -utf8" >/dev/null 2>&1 || true
  bibtex main >/dev/null 2>&1 || true
  htlatex main.tex "html.cfg" " -cunihtf -utf8" >/dev/null 2>&1 || true
  htlatex main.tex "html.cfg" " -cunihtf -utf8" > htlatex.log 2>&1 || true
)
test -s "$B/main.html" || { echo "htlatex produced no HTML; see $B/htlatex.log"; exit 1; }

# Inline the CSS and the SVG figures so one file opens anywhere (phone, chat, mail).
python3 - "$B" "$OUT/aigr-paper.html" <<'PY'
import base64, re, sys
from pathlib import Path
b, out = Path(sys.argv[1]), Path(sys.argv[2])
html = (b / "main.html").read_text(encoding="utf-8", errors="replace")
css = (b / "main.css").read_text(encoding="utf-8", errors="replace") if (b / "main.css").exists() else ""
html = re.sub(r'<link[^>]*href=["\']main\.css["\'][^>]*/?>', f"<style>\n{css}\n</style>", html)
def img(m):
    src = m.group(1)
    p = b / src
    if p.exists() and p.suffix in (".svg", ".png"):
        mime = "image/svg+xml" if p.suffix == ".svg" else "image/png"
        return m.group(0).replace(src, f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode())
    return m.group(0)
html = re.sub(r'<img[^>]*src=["\']([^"\']+)["\']', img, html)
missing = re.findall(r'<img[^>]*src=["\'](?!data:)([^"\']+)', html)
out.write_text(html, encoding="utf-8")
print(f"wrote {out} ({out.stat().st_size/1e6:.1f} MB); images not inlined: {missing or 'none'}")
PY
