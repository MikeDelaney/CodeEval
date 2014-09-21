import string
import pytest
from rollercoaster import rollercoaster


@pytest.fixture(scope='session')
def rejects():
    return string.punctuation + ' '


def test_rollercoaster_ex1(rejects):
    line = 'To be, or not to be: that is the question.\n'
    assert rollercoaster(line, rejects) == 'To Be, Or NoT tO bE: tHaT iS tHe QuEsTiOn.'


def test_rollercoaster_ex2(rejects):
    line = "Whether 'tis nobler in the mind to suffer\n"
    assert rollercoaster(line, rejects) == "WhEtHeR 'tIs NoBlEr In ThE mInD tO sUfFeR"


def test_rollercoaster_ex3(rejects):
    line = 'The slings and arrows of outrageous fortune,'
    assert rollercoaster(line, rejects) == 'ThE sLiNgS aNd ArRoWs Of OuTrAgEoUs FoRtUnE,'


def test_rollercoaster_ex4(rejects):
    line = 'Or to take arms against a sea of troubles,'
    assert rollercoaster(line, rejects) == 'Or To TaKe ArMs AgAiNsT a SeA oF tRoUbLeS,'


def test_rollercoaster_ex5(rejects):
    line = 'And by opposing end them? To die: to sleep.'
    assert rollercoaster(line, rejects) == 'AnD bY oPpOsInG eNd ThEm? To DiE: tO sLeEp.'
