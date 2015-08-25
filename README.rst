=========================
Ultra Fast Template Library
=========================

This project provides a library which allows for very flexible and fast template renderings at the expense of security.
It uses python code to generate variables which are then substituted in a string.Template.

There is a simple example in uftemplates.py, but this works as well:

    from uftlib import UFTemplate
    initial = """
    import datetime
    def f(x):
        return x*x
    def getnow():
        return str(datetime.datetime.now())
    a = 0
    b = 100
    i = 0
    """

        oncycle = """
    a += 3
    i += 1
    s = f(i)
    b += a
    now = getnow()
    """

        template = """Now = ${now}
    Render nr. ${i}
    f(${i}) = ${s}
    b = ${b}
    We live in ${where}"""

        tpl = UFTemplate(initial, oncycle, template, debug=True, where="Indonezia")
        for text in tpl.render_many(3):
            print(text)

        tpl.reset()
        for text in tpl.render_many(3):
            print(text)

