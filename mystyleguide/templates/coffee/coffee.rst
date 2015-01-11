{% extends "meta.rst" %}

{% block language %}coffeescript{% endblock %}

{% block code_layout %}
Indentation
***************
Use 2 spaces per indentation level.

Maximum Line Length
***********************

Limit all lines to a maximum of 79 characters.

Long long parameters
***********************

yes:


.. sourcecode::

   foo = some_long_long_func_name(var_one, var_two,
                                  var_three, var_four)

   foo = some_long_long_func_name(
     var_one, var_two,
     var_three, var_four)

   foo = some_long_long_func_name(
     more_long_long_var_one,
     more_long_long_var_two,
     more_long_long_var_three,
     more_long_long_var_four
   )

no:

.. sourcecode::

   foo = some_long_long_func_name(var_one, var_two,
     var_three, var_four)

   foo = some_long_long_func_name(
   var_one, var_two,
   var_three, var_four)

   foo = some_long_long_func_name(
     more_long_long_var_one,
     more_long_long_var_two,
     more_long_long_var_three,
     more_long_long_var_four
   )

optional:

.. sourcecode::

   foo = some_long_long_func_name(
     more_long_long_var_one,
     more_long_long_var_two,
     more_long_long_var_three,
     more_long_long_var_four)

{% endblock %}

{% block string_quotes %}
{% endblock %}

{% block whitespace %}
{% endblock %}

{% block comments %}
{% endblock %}

{% block convention %}
{% endblock %}

{% block recommend %}
{% endblock %}
