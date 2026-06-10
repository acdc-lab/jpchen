---
layout: default
title: Home
---

<p><span class="anchor" id="about-me"></span></p>

I am Jinpeng Chen, an Associate Professor and Doctoral Advisor at the
School of Computer Science (National Model Software College), Beijing University of Posts and Telecommunications (BUPT).
I am a Senior Member of CCF, a Senior Member of CIC, and a member of IEEE and ACM.
My research interests include <strong>social media &amp; data mining</strong>, <strong>recommender systems</strong>,
<strong>large language models</strong>, and <strong>intelligent transportation &amp; spatiotemporal forecasting</strong>.

I have led or participated in <strong>40+ research projects</strong> funded by national programs, provincial/ministerial agencies, and industry partners.
These include the National 973 Program, National Key R&amp;D Program, NSFC General/Youth Programs,
National Social Science Foundation, Beijing Natural Science Foundation,
and collaborative funds from CCF–Tencent Rhino Bird, CCF–Zhejiang Lab “Zhihai”, CCF–Zhipu LLM,
SMP–IDATA Morning Star, BUPT research initiatives, and key lab open grants.
I have published <strong>100+ papers</strong> in venues such as <em>SIGIR, NeurIPS, AAAI, ACM MM, EMNLP, TMC, TMM,</em> and <em>TNNLS</em>,
received the ICONIP 2022 Best Paper Award, and hold 8 patents.

# 📢 News
<p><span class="anchor" id="news"></span></p>

- **2026.06** — Congratulations to Zhang Fan, Jianxiang, and Ma Jian on their successful graduation! 🎉

# 🔬 Research
<p><span class="anchor" id="research"></span></p>

Our group focuses on four tightly connected directions: <strong>Social Media &amp; Data Mining</strong>,
<strong>Recommender Systems</strong>, <strong>Large Language Models (LLMs)</strong>, and
<strong>Intelligent Transportation &amp; Spatiotemporal Forecasting</strong>.
We emphasize principled modeling, robust evaluation, and deployable systems.

## 1) Social Media &amp; Data Mining

- <strong>User &amp; Content Modeling:</strong> multimodal representation learning for posts/users (text–image–video), topic and sentiment dynamics, influence estimation.
- <strong>Community Discovery:</strong> graph-based and dynamic community detection on interaction/interest networks; profiling communities and tracking evolution over time.

## 2) Recommender Systems

- <strong>Sequential Recommendation:</strong> session- and long-horizon sequence models capturing short-term intents and long-term preferences; temporal/context signals.
- <strong>Multimodal Recommendation:</strong> fusing text, image, and behavioral cues for cold-start and explainability; contrastive and cross-modal alignment.
- <strong>Fine-grained User &amp; Item Modeling:</strong> attribute- and aspect-level representations, disentangled factors, and side-information enrichment for precise matching.

## 3) Large Language Models (LLMs)

- <strong>Model Lightweighting:</strong> distillation, pruning, quantization, and parameter-efficient tuning (LoRA/QLoRA) for efficient training and inference.
- <strong>Multi-Agent Applications:</strong> planner–solver–critic pipelines, tool-augmented agents for retrieval/recommendation, evaluation agents for safety and reliability.

## 4) Intelligent Transportation &amp; Spatiotemporal Forecasting

- <strong>Traffic Flow Prediction:</strong> graph neural models over road networks (sensor/road-link graphs), dynamic connectivity, and data fusion (speed/volume/ETC).
- <strong>Spatiotemporal Forecasting:</strong> multi-scale temporal modeling, spatial attention and diffusion on grids/graphs, probabilistic forecasting and uncertainty.
- <strong>Autonomous-Driving Assistance:</strong> perception–map–trajectory fusion, intention and risk prediction for driving decision support under real-time constraints.

# 📚 Selected Publications
<p><span class="anchor" id="publications"></span></p>

Peer-reviewed journal/conference papers from <strong>2023+</strong>. Preprints (arXiv/CoRR) are excluded.

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

# 🏆 Honors and Teaching Awards
<p><span class="anchor" id="honors"></span></p>

- National Graduate Education Essay Award (Excellence); CCGEC 2025 Best Paper (First Prize); CECC 2024 Teaching Case (First Prize).
- 3rd Prize, 12th Excellent Higher Education Paper; Zhou Jiongpang Outstanding Young Teacher Award; “ChuanYou 70” Teaching Innovation Award.
- BUPT Graduate Teaching Achievement Award (Second Prize); BUPT Teaching Observation Competition (Second Prize);
  BUPT Young Teachers’ Teaching Skills (Second Prize); BUPT Teaching Innovation Competition (Second Prize).
- Outstanding Instructor for Undergraduate Innovation &amp; Entrepreneurship projects.

# 📖 Teaching
<p><span class="anchor" id="teaching"></span></p>

Selected undergraduate and graduate courses with brief descriptions, instructors, and offering unit.

{% assign courses = site.data.teaching | default: empty %}
{% if courses and courses.size > 0 %}
<div class="course-list">
  {% for c in courses %}
  <article class="course-item">
    <div class="course-term">{{ c.term }}</div>
    <div>
      <h3>{{ c.title }}</h3>
      <p class="course-meta">{{ c.level }} · {{ c.instructors | join: ', ' }} · {{ c.org }}</p>
      <p>{{ c.desc }}</p>
      {% if c.tags %}
      <p class="course-tags">
        {% for t in c.tags %}<span>{{ t }}</span>{% endfor %}
      </p>
      {% endif %}
    </div>
  </article>
  {% endfor %}
</div>
{% else %}
No course data yet. Add entries to <code>_data/teaching.yml</code>.
{% endif %}

# 🤝 Service
<p><span class="anchor" id="service"></span></p>

## Professional Committees

- Member, <strong>China AI Education Alliance</strong>.
- Reviewer, <strong>CSCIED Scientific Evaluation Database</strong>.
- Executive Member, <strong>CCF Technical Committee on Big Data</strong>.
- Executive Member, <strong>CCF Technical Committee on Artificial Intelligence & Pattern Recognition</strong>.
- Executive Member, <strong>CCF Technical Committee on Databases</strong>.
- Founding Executive Member, <strong>CCF Large Model Forum</strong>.
- Member, <strong>CAAI Technical Committee on Intelligent Service</strong>.
- Member, <strong>CAAI Technical Committee on Embodied Intelligence</strong>.
- Member, <strong>CIPS Young Scholars Committee</strong>.
- Member, <strong>CIPS Technical Committee on Social Media Processing</strong>.
- Member, <strong>CIPS Technical Committee on Language and Knowledge Computing</strong>.
- Member, <strong>CCF YOCSEF Headquarters</strong>.

## Editorial Boards

- <strong>Early-Career Editorial Board Member</strong>, <em>Big Data Mining and Analytics</em>.
- <strong>Executive Committee Member</strong>, <em>Computer Science</em> (《计算机科学》).
- <strong>Editorial Board Member</strong>, <em>Journal of Social Computing</em>.
- <strong>Early-Career Editorial Board Member</strong>, <em>Computer Science and Exploration</em> (《计算机科学与探索》).
- <strong>Assistant Editor</strong>, <em>Journal of Intelligent Systems</em> (《智能系统学报》).

## Program Leadership &amp; Program Committees

- <strong>Area Chair</strong>, <em>CCL 2025</em> (Chinese Computational Linguistics).
- <strong>Program Committee</strong>: <em>The Web Conference (WWW) 2025</em>, <em>IJCAI 2024–2025</em>, <em>ACM Multimedia 2025</em>, <em>AAAI 2025</em>, and other major venues.

## Reviewer (Journals &amp; Conferences)

Served as reviewer for leading journals and conferences, including:

<ul class="two-col">
  <li><em>ACM TOIS</em></li>
  <li><em>IEEE TKDE</em></li>
  <li><em>ACM TKDD</em></li>
  <li><em>IEEE TNNLS</em></li>
  <li><em>IEEE TFS</em></li>
  <li><em>IEEE TCYB</em></li>
  <li><em>IEEE TCC</em></li>
  <li><em>DKE</em></li>
  <li><em>WWW</em></li>
  <li><em>KDD</em></li>
  <li><em>ACM MM</em></li>
  <li><em>CIKM</em></li>
  <li><em>DASFAA</em></li>
  <li><em>ACM SIGSPATIAL (GIS)</em></li>
</ul>

# 🎤 Talks
<p><span class="anchor" id="talks"></span></p>

- <em>2025-11-02</em> Preference-aware Causal Intervention and Intent-driven Sequential Recommendation. Invited talk at the <em>11th China Conference on Intelligent Technology and Big Data (CITBD 2025)</em>.
- <em>2025-06-23</em> Academic Talk (Invited). Zhejiang Normal University.
- <em>2025-03-21</em> Future Recommendation: Exploring Paths to Personalized Recommendation in the LLM Era. Special guest, <em>YOCSEF Jinan Technical Forum</em>, National Supercomputing Center Jinan Science Park (Main Building 451).
- <em>2024-12-11</em> Enhancing Sequential Recommendation via Preference-aware Causal Intervention and Data Augmentation. Invited talk at the <em>Zhixing Forum: Frontiers of Data Mining and Embodied Intelligence</em>, Beijing Jiaotong University (Siyuan Time Café).
- <em>2024-11-22</em> Enhancing Sequential Recommendation via Preference-aware Causal Intervention and Data Augmentation. Keynote at the <em>CETC Taiji / Institute 15 Youth Academic Exchange & Inaugural Meeting of the CSE Young Editorial Board</em>.
- <em>2024-11-16</em> Enhancing Sequential Recommendation via Preference-aware Causal Intervention and Data Augmentation. Invited talk at the <em>AI for Science</em> Academic Forum, BUPT Research Institute (on campus).
- <em>2024-10-13</em> Enhancing Sequential Recommendation via Preference-aware Causal Intervention and Data Augmentation. Invited speaker, <em>The 12th China National Conference on Social Media Processing (SMP 2024)</em>, Xinxiang, China.
- <em>2023-11-24</em> Mandari: Multi-Modal Temporal Knowledge Graph-aware Sub-graph Embedding for Next-POI Recommendation. Talk at <em>CCIR 2023 Summer School</em>, Beijing, China.
- <em>2023-07-22</em> Mandari: Multi-Modal Temporal Knowledge Graph-aware Sub-graph Embedding for Next-POI Recommendation. Talk at <em>KDD China 2023 Summer School</em>, Chengdu, China.

# 🎓 Students
<p><span class="anchor" id="students"></span></p>

## Student Mentoring

- Supervised **20** Undergraduate Innovation & Entrepreneurship Training Projects (7 national, 9 municipal).
- Students received BUPT Innovation & Entrepreneurship Practice Awards: *First Prize (2019)*, *Second Prize ×2 (2021)*, *Third Prize ×2 (2018, 2021)*.
- Graduate mentees won *Third Prize* at the BUPT Graduate Innovation & Entrepreneurship Exhibition (2020).

## 💻 Alumni

I am so fortunate to have worked with these students:

### Master Graduates

<ul class="alumni-list">
  <li><strong>2025:</strong>
    <ul>
      <li>关华琛 — 美团-营销推荐算法</li>
      <li>王晋卿 — 中电信数智科技有限公司</li>
      <li>余子羽 — 华为-AI Infra工程师</li>
      <li>井然 — 中航信移动科技股份有限公司-软件工程师</li>
    </ul>
  </li>
  <li><strong>2024:</strong>
    <ul>
      <li>张旭东 — 兴业银行总行</li>
      <li>刘晓倩 — 阿里巴巴-淘天算法工程师</li>
      <li>刘真光 — 农业银行-研发</li>
    </ul>
  </li>
  <li><strong>2023:</strong>
    <ul>
      <li>曹源 — 新加坡国立大学-博士生</li>
      <li>栾厚蕴 — 牵手未来-算法工程师</li>
      <li>许祎 — 阿里巴巴-推荐广告算法</li>
      <li>王博杰 — 智谱AI-大模型算法</li>
    </ul>
  </li>
  <li><strong>2022:</strong>
    <ul>
      <li>马瑞遥 — 新加坡国立大学-RA，博士生</li>
      <li>李海洋 — 美团-算法策略岗</li>
      <li>周瑶瑶 — 阿里巴巴集团-后端开发工程师</li>
      <li>胡哈蕾 — 华为-软件开发工程师</li>
    </ul>
  </li>
  <li><strong>2021:</strong>
    <ul>
      <li>耿新尧 — Apple</li>
      <li>张静怡 — 易方达基金 IT</li>
    </ul>
  </li>
  <li><strong>2019:</strong>
    <ul>
      <li>张佩 — 广西大学-助理教授</li>
    </ul>
  </li>
</ul>

### Undergraduate Alumni

<ul class="alumni-list">
  <li><strong>2025:</strong>
    <ul>
      <li>黄天瑞 — 中国科学院大学软件学院</li>
      <li>刘应秋 — 好未来-Golang开发</li>
    </ul>
  </li>
  <li><strong>2024:</strong>
    <ul>
      <li>朱霄 — 香港科技大学（广州）</li>
    </ul>
  </li>
  <li><strong>2022:</strong>
    <ul>
      <li>陈昱滔 — 澳门大学-博士生</li>
      <li>张超伟 — 厦门建发-信息岗</li>
    </ul>
  </li>
  <li><strong>2021:</strong>
    <ul>
      <li>熊博韬 — 四川电信-AI工程师</li>
    </ul>
  </li>
  <li><strong>2020:</strong>
    <ul>
      <li>邓宇彤 — 留学</li>
    </ul>
  </li>
  <li><strong>2017:</strong>
    <ul>
      <li>贺桐 — 腾讯-游戏开发</li>
    </ul>
  </li>
</ul>

# 🏛️ Affiliations
<p><span class="anchor" id="affiliations"></span></p>

{% include affiliations.html %}
