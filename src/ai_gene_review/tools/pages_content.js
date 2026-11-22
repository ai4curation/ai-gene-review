// Restore the original supporting HTML; URLs still resolve against its page.
(() => {
  async function restore(container) {
    const url = container.dataset.pagesContent;
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP ${response.status}: ${url}`);
    // fetch() may already have decoded Content-Encoding: gzip.
    const bytes = new Uint8Array(await response.arrayBuffer());
    const raw = new Blob([bytes]).stream();
    const stream = bytes[0] === 0x1f && bytes[1] === 0x8b
      ? raw.pipeThrough(new DecompressionStream('gzip')) : raw;
    const markup = await new Response(stream).text();
    const template = document.createElement('template');
    template.innerHTML = markup;
    // The main template uses delegated voting, but prior vote highlighting
    // normally runs at DOMContentLoaded, before these panels arrive.
    template.content.querySelectorAll('.vote-buttons').forEach(group => {
      const key = `vote_${group.dataset.g}_${group.dataset.a}_${group.dataset.act}`;
      let previous;
      try { previous = localStorage.getItem(key); } catch { /* Storage may be disabled. */ }
      if (previous === 'up' || previous === 'down') {
        group.querySelector(`[data-v="${previous}"]`)?.classList.add(
          previous === 'up' ? 'voted' : 'voted-down');
      }
    });
    container.replaceWith(template.content);
  }
  window.pagesContentReady = Promise.all(
    [...document.querySelectorAll('[data-pages-content]')].map(async container => {
      try {
        await restore(container);
      } catch (error) {
        console.error('Supporting content could not be loaded', error);
        container.querySelector('[role="status"]').textContent =
          'Could not load this section. Reload to retry, or download it below.';
        throw error;
      }
    })
  );
  window.pagesContentReady.then(() => {
    document.dispatchEvent(new Event('pagesContentReady'));
    // The browser could not find a deep fragment while it was compressed.
    if (location.hash) {
      const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (target) {
        for (let parent = target.parentElement; parent; parent = parent.parentElement) {
          if (parent.tagName === 'DETAILS') parent.open = true;
        }
        target.scrollIntoView();
      }
    }
  }).catch(() => {}); // Each failed panel already exposes its download and error.
})();
