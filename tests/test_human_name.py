import pytest

from nameparser import HumanName


@pytest.mark.parametrize('fullname,name', [
    ('A. B. Cc', {
        'title': '',
        'first': 'A.',
        'middle': 'B.',
        'last': 'Cc',
        'suffix': '',
        'nickname': '',
    }),
    ('Yuan-Che (Wonder) Chang', {
        'title': '',
        'first': 'Yuan-Che',
        'middle': '',
        'last': 'Chang',
        'suffix': '',
        'nickname': 'Wonder',
    }),
    ('Wonder Yuan-Che Chang', {
        'title': '',
        'first': 'Wonder',
        'middle': 'Yuan-Che',
        'last': 'Chang',
        'suffix': '',
        'nickname': '',
    }),
])
def test_human_name(fullname, name):
    human_name = HumanName(fullname)

    assert human_name.title == name['title']
    assert human_name.first == name['first']
    assert human_name.middle == name['middle']
    assert human_name.last == name['last']
    assert human_name.suffix == name['suffix']
    assert human_name.nickname == name['nickname']



# vi:et:ts=4:sw=4:cc=80
