---
layout: page
title: Alumni
permalink: /alumni/
---
Here is a list of former coreteam members. We are thankful to them for their service.

{% for person in site.data.alumni %}
<p>
    <strong>{{ person.name }}</strong> was {{ person.description }}
</p>
{% endfor %}
