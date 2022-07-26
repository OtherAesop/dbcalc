import decibel_calc as dbc
import pytest as pt

@pt.fixture
def dbcalc():
    return dbc.DBCalc(1.0, destination_db=40, source_db=60)

def test_init():

    db_calc = dbc.DBCalc(1.0, destination_db=40, source_db=60)

    assert db_calc.dist_traveled == 1.0
    assert db_calc.db_destination == 40
    assert db_calc.db_source == 60

    assert db_calc.I_reference == 1E-12


def test_db_from_intensity(dbcalc: dbc.DBCalc):

    assert round(dbcalc._db_from_intensity(2.546E-3),0) == 94.0
    # Calculator limit
    assert dbcalc._db_from_intensity(3.1622776601683794e-15) == -25
    # Can we break our limit?
    assert dbcalc._db_from_intensity(3e-200) == -25

    # Are we symmetric?
    assert dbcalc._intensity_from_db(dbcalc._db_from_intensity(dbcalc.I_reference)) == dbcalc.I_reference
    

def test_intensity_from_db(dbcalc: dbc.DBCalc):

    assert dbcalc._intensity_from_db(0) == dbcalc.I_reference
    assert dbcalc._intensity_from_db(60) == 1E-6
    
    # limit
    assert dbcalc._intensity_from_db(-25) == dbcalc.min_intensity
    # limit break?
    assert dbcalc._intensity_from_db(-25000) == dbcalc.min_intensity

    # symmetric?
    assert dbcalc._db_from_intensity(dbcalc._intensity_from_db(0)) == 0.0


def test_get_sound_at_destination(dbcalc: dbc.DBCalc):

    assert dbcalc.get_sound_at_destination() == 40

    # limit break?
    dbcalc.db_source = -500
    assert dbcalc.get_sound_at_destination() == -25

    # symmetric?
    dbcalc.db_source = 60
    assert dbcalc.get_sound_at_destination() == 40
    assert dbcalc.get_sound_at_source() == 60

def test_get_sound_at_source(dbcalc: dbc.DBCalc):

    assert dbcalc.get_sound_at_source() == 60

    # no limit on high numbers so go big
    dbcalc.db_destination = 120
    assert dbcalc.get_sound_at_source() == 140
    
    # symmetric?
    dbcalc.db_destination = 40
    assert dbcalc.get_sound_at_destination() == 40
    assert dbcalc.get_sound_at_source() == 60

