---
layout: default
title: Teaching
permalink: /teaching/
---

<section class="section">
  <div class="title"><span class="emoji">🎓</span><h1 style="margin:0">Teaching</h1></div>
  <p class="meta">Selected undergraduate and graduate courses with brief descriptions, instructors, and offering unit.</p>

  <style>
    .teach-grid{display:grid;gap:22px;grid-template-columns:repeat(4,minmax(0,1fr))}
    @media(max-width:1200px){.teach-grid{grid-template-columns:repeat(3,1fr)}}
    @media(max-width:900px){.teach-grid{grid-template-columns:repeat(2,1fr)}}
    @media(max-width:560px){.teach-grid{grid-template-columns:1fr}}

    .teach-card{background:var(#fff);border:1px solid rgba(0,0,0,.06);
      border-radius:16px;box-shadow:0 6px 18px rgba(0,0,0,.06);overflow:hidden}
    .teach-cover{position:relative;aspect-ratio:16/9;background:#f6f7f9}
    .teach-cover img{width:100%;height:100%;object-fit:cover;display:block}
    .badge-term{position:absolute;left:10px;top:10px;background:rgba(0,0,0,.7);
      color:#fff;font-size:12px;padding:4px 8px;border-radius:8px}
    .badge-grad{position:absolute;right:10px;bottom:10px;background:#3b82f6;color:#fff;
      font-size:12px;padding:3px 8px;border-radius:8px}
    .teach-body{padding:14px 16px 16px}
    .teach-title{font-weight:800;font-size:18px;margin:4px 0 8px}
    .teach-sub{color:#6b7280;font-size:13px;margin-bottom:8px}
    .teach-desc{color:#374151;font-size:14px;line-height:1.55;min-height:3.2em}
    .teach-tags{margin-top:10px;display:flex;flex-wrap:wrap;gap:6px}
    .teach-tag{font-size:12px;background:#eef2ff;color:#3730a3;border-radius:10px;padding:2px 8px}
    .teach-links{margin-top:10px}
    .teach-links a{font-size:13px}
  </style>

  {% assign courses = site.data.teaching | default: empty %}
  {% if courses and courses.size > 0 %}
  <div class="teach-grid">
    {% for c in courses %}
    <article class="teach-card">
      <div class="teach-cover">
        <img src="{{ (c.cover | default: '/assets/img/teaching/placeholder.jpg') | relative_url }}"
             alt="{{ c.title }}">
        {% if c.term %}<span class="badge-term">{{ c.term }}</span>{% endif %}
        {% if c.level and c.level contains 'Graduate' %}
          <span class="badge-grad">Grad</span>
        {% endif %}
      </div>
      <div class="teach-body">
        <div class="teach-title">{{ c.title }}</div>
        <div class="teach-sub">
          {{ c.instructors | join: ', ' }}<br>
          {{ c.org }}
        </div>
        <div class="teach-desc">{{ c.desc }}</div>
        {% if c.tags %}
          <div class="teach-tags">
            {% for t in c.tags %}<span class="teach-tag">{{ t }}</span>{% endfor %}
          </div>
        {% endif %}
        {% if c.syllabus_url %}
          <div class="teach-links">
            <a href="{{ c.syllabus_url }}" target="_blank" rel="noopener">Syllabus →</a>
          </div>
        {% endif %}
      </div>
    </article>
    {% endfor %}
  </div>
  {% else %}
    <p>No course data yet. Add entries to <code>_data/teaching.yml</code>.</p>
  {% endif %}
</section>
