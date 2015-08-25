=========================
Ultra Fast Template Library
=========================

This project provides a library which allows for very flexible and fast template renderings at the expense of security.
It uses python code to generate variables which are then substituted in a string.Template.

Examples
========
Here's a basic example:

.. code-block:: python

  from uftlib import UFTemplate

  initial = """import datetime
  def f(x):
      return x*x
  
  def getnow():
      return str(datetime.datetime.now())
  
  a = 0
  b = 100
  i = 0"""
  
  oncycle = """a += 3
  i += 1
  s = f(i)
  b += a
  now = getnow()"""

  template = """Now = ${now}
  Render nr. ${i}
  f(${i}) = ${s}
  b = ${b}
  We live in ${where}"""

  tpl = UFTemplate(initial, oncycle, template, debug=True, where="Indonezia")
  for text in tpl.render_many(1):
      print(text)

We can reset the template to it's initial state and obtain the same results:

  tpl.reset()
  for text in tpl.render_many(2):
      print(text)


You should get the following output:

  Now = 2015-08-25 16:09:07.015948
  Render nr. 1
  f(1) = 1
  b = 103
  We live in Indonezia
  Now = 2015-08-25 16:09:07.016970
  Render nr. 1
  f(1) = 1
  b = 103
  We live in Indonezia
  Now = 2015-08-25 16:09:07.017298
  Render nr. 2
  f(2) = 4
  b = 109
  We live in Indonezia
