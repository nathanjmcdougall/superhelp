from textwrap import dedent

from tests import check_as_expected

ROOT = 'superhelp.helpers.set_help.'

def test_misc():
    test_conf = [
        (
            dedent("""\
            pet = 'cat'
            """),
            {
                ROOT + 'set_overview': 0,
            }
        ),
        (
            dedent("""\
            demo = set()
            """),
            {
                ROOT + 'set_overview': 1,
            }
        ),
        (
            dedent("""\
            demo1 = set()
            demo2 = set()
            """),
            {
                ROOT + 'set_overview': 2,
            }
        ),
        (
            dedent("""\
            for i in range(2):
                demo1 = set()
                demo2 = set()
            """),
            {
                ROOT + 'set_overview': 1,
            }
        ),
        (
            dedent("""\
            for i in range(2):
                demo1 = set([1, 2, 3])
                demo2 = set([8, 9, 10])
            """),
            {
                ROOT + 'set_overview': 1,
            }
        ),
        (
            dedent("""\
            people = set(['Sam', 'Avi', 'Terri', 'Noor'])
            """),
            {
                ROOT + 'set_overview': 1,
            }
        ),
    ]
    check_as_expected(test_conf)

# test_misc()
