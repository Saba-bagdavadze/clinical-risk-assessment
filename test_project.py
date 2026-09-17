import pytest

from project import bmi_category, blood_pressure, smoking_

from scores import risk_category, bmi_calc, bp_points_calc, smoking_calc

from project import get_age, get_height, get_weight, get_blood_pressure, get_smoking_status

def test_bmi_underweight():
    assert bmi_category(25, 1.9)[1] == "underweight"
def test_bmi_normalweight():
    assert bmi_category(73, 1.8)[1] == "normal weight"
def test_bmi_obese():
    assert bmi_category(160, 1.5)[1] == "obese"

def test_normal_bp():
    assert blood_pressure(119, 79) == "Normal"
def test_elevated_bp():
    assert blood_pressure(125, 79) == "Elevated"
def test_st1_bp():
    assert blood_pressure(135, 85) == "Stage 1"
def test_st2_bp():
    assert blood_pressure(145, 95) == "Stage 2"
def test_crisis_bp():
    assert blood_pressure(190, 135) == "Crisis"

def test_smoker():
    assert smoking_("YES") == "Smoker"
def test_non_smoker():
    assert smoking_("NO") == "Non-smoker"

def test_low_risk():
    assert risk_category(1) == "Low risk"
def moderate_risk():
    assert risk_category(3) == "Moderate risk"
def test_high_risk():
    assert risk_category(5) == "High risk"
def test_very_high_risk():
    assert risk_category(8) == "Very high risk"

def test_bmi_points_normal():
    assert bmi_calc("normal weight") == 0
def test_bmi_points_over():
    assert bmi_calc("overweight") == 1
def test_bmi_points_obese():
    assert bmi_calc("obese") == 2

def test_bp_points_normal():
    assert bp_points_calc("Normal") == 0

def test_bp_points_elevated():
    assert bp_points_calc("Elevated") == 1

def test_bp_points_stage_1():
    assert bp_points_calc("Stage 1") == 2

def test_bp_points_stage_2():
    assert bp_points_calc("Stage 2") == 3

def test_bp_points_crisis():
    assert bp_points_calc("Crisis") == 4


def test_age(monkeypatch):
    inputs = iter(["101", "50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    age = get_age()
    assert age == 50

def test_height(monkeypatch):
    inputs = iter(["0", "1.81"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    height = get_height()
    assert height == 1.81

def test_weight(monkeypatch):
    inputs = iter(["0", "67"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    height = get_weight()
    assert height == 67

def test_blood_pressure_invalid(monkeypatch):
    inputs = iter(["999/80", "120/80"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    systolic, diastolic = get_blood_pressure()
    assert systolic == 120
    assert diastolic == 80
