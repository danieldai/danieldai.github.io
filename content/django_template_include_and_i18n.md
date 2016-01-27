Title: Django Template Include and I18n
Date: 2016-01-27 22:20
Category: Python
Tags: Django


In Django template we can use include to include another template into current template, and at the same time we can pass parameters to included tempalte.

```
{% include "include/another_template.html" with text='I love Python' %}
```

Sometimes, we need to tranalte `include prarameters`, this can not be done in `another_template.html`, `blocktrans` will not work here.

```
# in another_template.html
{% blocktrans %}
{{ text }}
{% endblocktrans %}
```

We need to do the translation in the first temalate, before passing it to another template:

```
{% trans 'I love Python' as text %}
{% include "include/another_template.html" with text=text %}
```


Reference:

[http://stackoverflow.com/questions/18899295/django-i18n-template-include-tags](http://stackoverflow.com/questions/18899295/django-i18n-template-include-tags)