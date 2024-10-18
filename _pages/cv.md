---
title: "Ciriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Education
* Ph.D. in Information Studies, Florida State University, Tallahassee, FL, 2015
* Master of Library and Information Science, Pusan National University, Busan, South Korea, 2008
* Bachelor of Library and Information Science, Pusan National Univeristy, Busan, South Korea, 2003

## Academic Appointment
* Associate Professor, School of Information Studies, University of Wisconsin-Milwaukee, Milwaukee, WI, 2024–present
* Assistant Professor, School of Information Studies, University of Wisconsin-Milwaukee, Milwaukee, WI, 2018–2024
* Visiting Assistant Professor, School of Information Studies, University of Wisconsin-Milwaukee, Milwaukee, WI, 2017–2018
* Postdoctoral Fellow, Business School, Worcester Polytechnic Institute, Worcester, MA, 2015–2017

## Publications
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
## Teaching
{% if site.publication_category %}
  {% for category in site.publication_category  %}
    {% assign title_shown = false %}
    {% for post in site.publications reversed %}
      {% if post.category != category[0] %}
        {% continue %}
      {% endif %}
      {% unless title_shown %}
        <h2>{{ category[1].title }}</h2>
        {% assign title_shown = true %}
      {% endunless %}
      <ul>
        <li>
        {% if post.citation and post.paperurl and post.slidesurl %}
          {{ post.citation }}<br /><a href="{{ post.paperurl }}">Download Paper</a> | <a href="{{ post.slidesurl }}">Download Slides</a>
        {% elsif post.citation and post.paperurl %}
          {{ post.citation }}<br /><a href="{{ post.paperurl }}">Download Paper</a>
        {% elsif post.citation and post.slidesurl %}
          {{ post.citation }}<br /><a href="{{ post.slidesurl }}">Download Slides</a>
        {% elsif post.citation %}
          {{ post.citation }}
        {% elsif post.paperurl %}
          <a href=" {{ post.paperurl }} ">Download Paper</a>
        {% elsif post.slidesurl %}
          Download <a href="{{ post.slidesurl }}">Download Slides</a>
        {% endif %}
        </li>
      </ul>
    {% endfor %}
  {% endfor %}
{% else %}

## Service and leadership
* 2024–present MSIST Porgram Committee
* 2023–2024 BSIST Program Committee

