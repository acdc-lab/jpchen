---
layout: default
title: Publications
permalink: /publications/
---

<section class="section">
  <div class="title"><span class="emoji">📚</span><h1 style="margin:0">Publications</h1></div>
  <p class="meta">Peer-reviewed journal/conference papers from <strong>2023+</strong>. Preprints (arXiv/CoRR) are excluded.</p>

  {% bibliography
     --group_by year
     --group_order descending
     --template bib_entry
     --query
     @*[ year >= 2023
         and not (
           journal      ~= /arxiv|corr/i
           or note      ~= /arxiv|preprint|under review|submitted/i
           or archivePrefix ~= /arxiv/i
           or eprinttype   ~= /arxiv/i
           or howpublished ~= /arxiv/i
           or url          ~= /arxiv\.org/i
         )
       ]
  %}

</section>
