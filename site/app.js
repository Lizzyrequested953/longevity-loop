/* longevity-loop dashboard — renders the loop, turns log, roadmap, and landscape
 * from data.json (the same source of truth as the README). Static, no key, ~$0. */
const $ = s => document.querySelector(s);
const el = (t, c, h) => { const e = document.createElement(t); if (c) e.className = c; if (h != null) e.innerHTML = h; return e; };
const esc = s => String(s == null ? "" : s).replace(/[&<>]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c]));
const md = s => esc(s).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>").replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g, '<a href="$2" target="_blank">$1</a>');

function section(title, sub) {
  $("#app").appendChild(el("h2", null, esc(title)));
  if (sub) $("#app").appendChild(el("div", "sub", sub));
}
function table(head, rows) {
  const t = el("table"); t.innerHTML = `<thead><tr>${head.map(h => `<th>${h}</th>`).join("")}</tr></thead>`;
  const tb = el("tbody"); rows.forEach(r => { const tr = el("tr"); tr.innerHTML = r.map(c => `<td>${c}</td>`).join(""); tb.appendChild(tr); });
  t.appendChild(tb); $("#app").appendChild(t);
}
function cards(items, fmt) {
  const g = el("div", "grid"); items.forEach(x => g.appendChild(el("div", "card", fmt(x)))); $("#app").appendChild(g);
}

function render(DB) {
  const m = DB.meta || {};
  $("#tagline").innerHTML = md(m.tagline || "");
  $("#north").innerHTML = md(m.north_star || "");
  $("#sibling").innerHTML = md(m.sibling_banner || "");
  $("#counts").innerHTML = [["turns", "turns"], ["people", "researchers"], ["startups", "startups"], ["stack", "tools"], ["ecosystem", "orgs"]]
    .filter(([k]) => (DB[k] || []).length).map(([k, l]) => `<span class="pill">${DB[k].length} ${l}</span>`).join("");

  // The loop
  section("♻️ The Loop", "One turn of the flywheel — falsifiable, verifiable, shared.");
  const loop = DB.loop || {};
  (loop.stages || []).forEach(s => {
    $("#app").appendChild(el("div", "loopstage", `<span class="n">${s.n}</span><b>${esc(s.name)}</b><span>${esc(s.do)}</span>`));
  });

  // Turns log
  const icon = { scaffolded: "🧩", "in-progress": "🔄", done: "✅" };
  section("📓 Turns Log", "Every turn logged honestly. <code>done</code> requires a PROOF (result incl. the null).");
  table(["Turn", "Question", "Stage", "Status"], (DB.turns || []).map(t => [
    `<a href="https://github.com/wjlgatech/longevity-loop/tree/main/${t.path}" target="_blank">${esc(t.id)}</a>`,
    esc(t.question), esc(t.stage), `<span class="chip ${t.status}">${icon[t.status] || ""} ${esc(t.status)}</span>`,
  ]));

  // Roadmap
  const road = DB.roadmap || {};
  section("🗺️ 90-Day Roadmap", "Full weekly plan in docs/ROADMAP.md.");
  cards(road.phases || [], p => `<b>${esc(p.title)}</b><span class="m">${esc(p.days)} — ${esc(p.theme)}</span><span class="m">✅ ${esc(p.milestone)}</span>`);
  if (road.signal_ladder) {
    $("#app").appendChild(el("div", "sub", "<br><b>Signal ladder</b> — each rung recruits the next:"));
    const ol = el("ol", "ladder"); road.signal_ladder.forEach(r => ol.appendChild(el("li", null, esc(r)))); $("#app").appendChild(ol);
  }

  // Researchers
  section("🧠 Researchers", "🤖 AI-forward · 💬 open-community (good first contacts).");
  cards(DB.people || [], p => `<b><a href="${p.url}" target="_blank">${esc(p.name)}</a></b> <span class="mark">${(p.ai_forward ? "🤖" : "") + (p.approachable ? "💬" : "")}</span><span class="m">${esc(p.org)}: ${esc(p.known_for)}</span>`);

  // Startups
  section("🏢 Startups & Labs", "🤖 = AI-native.");
  cards(DB.startups || [], s => `<b><a href="${s.url}" target="_blank">${esc(s.name)}</a></b> <span class="mark">${s.ai_native ? "🤖" : ""}</span><span class="m">${esc(s.focus)} · ${esc(s.stage || "")}</span>`);

  // Stack
  section("🛠️ Buildable Stack", "Open, code-only.");
  table(["Tool", "Kind", "How you'd use it"], (DB.stack || []).map(x => [
    `<a href="${x.url}" target="_blank">${esc(x.name)}</a>`, esc(x.kind), esc(x.note)]));

  // Ecosystem
  section("🤝 Funding & Community", "✅ = open to independents · 🔒 = PI/team-gated.");
  cards(DB.ecosystem || [], e => `<b><a href="${e.url}" target="_blank">${esc(e.name)}</a></b> ${e.open_to_independents ? "✅" : "🔒"} <span class="m">${esc(e.type)} — ${esc(e.note)}</span>`);
}

fetch("data.json").then(r => r.json()).then(render).catch(() => {
  $("#app").appendChild(el("p", "sub", "Could not load data.json — open via the deployed site."));
});
