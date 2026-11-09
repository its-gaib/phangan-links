'use strict';
const tools = document.querySelector('.filter-tools');
tools.hidden = false;
const search = document.querySelector('#search');
const cards = [...document.querySelectorAll('.link-grid .link-card')];
const sections = [...document.querySelectorAll('.directory-section')];
const buttons = [...document.querySelectorAll('[data-filter]')];
let category = 'all';
function filter() {
  const terms = search.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
  let count = 0;
  for (const card of cards) {
    const visible = (category === 'all' || card.dataset.category === category) && terms.every(term => card.dataset.search.includes(term));
    card.hidden = !visible;
    if (visible) count++;
  }
  for (const section of sections) {
    section.hidden = ![...section.querySelectorAll('.link-card')].some(card => !card.hidden);
  }
  document.querySelector('#link-count').textContent = `${count} ${count === 1 ? 'LINK' : 'LINKS'} TO EXPLORE`;
  document.querySelector('.no-results').hidden = count !== 0;
  document.querySelector('.result-status').textContent = `${count} links found`;
}
for (const button of buttons) {
  button.addEventListener('click', () => {
    category = button.dataset.filter;
    for (const item of buttons) item.setAttribute('aria-pressed', String(item === button));
    filter();
  });
}
search.addEventListener('input', filter);
document.querySelector('#reset-search').addEventListener('click', () => {
  search.value = '';
  buttons[0].click();
  search.focus();
});
document.addEventListener('keydown', event => {
  if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey && !['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName) && !document.activeElement.isContentEditable) {
    event.preventDefault();
    search.focus();
  }
});
