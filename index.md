---
title: HOME
layout: default
permalink: /
---

# HOME

My research program involves studies of **information behavior** and **human-computer interaction**. My current projects focus on:
- Credibility assessment of user- and AI-generated content
- Generative AI literacy for higher education
- Usability and accessibility of information retrieval systems for disadvantaged user groups

## News

Recent publications

{% for post in site.posts limit:5 %}
**[{{ post.title }}]({{ post.url | relative_url }})**  
*{{ post.date | date: "%B %d, %Y" }}*  

{{ post.excerpt }}

{% endfor %}
