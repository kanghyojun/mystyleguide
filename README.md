# mystyleguide

code styleguide for me


## install

    $ pip install .

## view guides

```bash
$ mystyleguide build
$ ls -al out
-rw-r--r--  1 hyojun  staff  8294  1 12 00:59 coffee.html
-rw-r--r--  1 hyojun  staff   598  1 12 00:39 scala.html
...
```

## Contribution

With `meta.rst`, you can write your guides. it follows [jinja2 syntax][jinja2].
For instance you can write styleguide for new language called foobaz.


```
{% extends "meta.rst" %}

{% block language %}foobaz{% endblock %}

{% block code_layout %}
Indentation
***************
Use 2 spaces per indentation level.

...
{% endblock %}

{% block string_quotes %}
...
{% endblock %}

{% block whitespace %}
...
{% endblock %}

{% block comments %}
...
{% endblock %}

{% block convention %}
...
{% endblock %}

{% block recommend %}
...
{% endblock %}

```

and save it as `foobaz.rst` under `yourpath/mystyleguide/templates/foobaz`.


[jinja2]: http://jinja.pocoo.org/docs/dev/
