
from scores import bmi_calc, bp_points_calc, smoking_calc, risk_category

import csv
import os
from tabulate import tabulate


def main():

    name = input("Name: ")
    age = get_age()
    gender = input("Gender: ")
    systolic, diastolic = get_blood_pressure()
    height = get_height()
    weight = get_weight()
    smoking_status = get_smoking_status()

    bmi, category = bmi_category(weight, height)
    bp = blood_pressure(systolic, diastolic)
    category_smoking = smoking_(smoking_status)

    # total risk score calculation
    bmi_points = bmi_calc(category)
    bp_points = bp_points_calc(bp)
    smoking_points = smoking_calc(category_smoking)

    total_points = bmi_points + bp_points + smoking_points

    # risk assesment
    risk = risk_category(total_points)

    patient = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Weight (kg)": weight,
        "Height (m)": height,
        "BMI": round(bmi, 2),
        "BMI category": category,
        "Systolic": systolic,
        "Diastolic": diastolic,
        "BP category": bp,
        "Total risk points": total_points,
        "Risk": risk,
    }

    fieldnames = [
        "Name",
        "Age",
        "Gender",
        "Weight (kg)",
        "Height (m)",
        "BMI",
        "BMI category",
        "Systolic",
        "Diastolic",
        "BP category",
        "Total risk points",
        "Risk",
    ]

    file_exists = os.path.exists("patient_record.csv")

    with open("patient_record.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(patient)

    patients = display_patients()


def display_patients():
    with open("patient_record.csv") as file:
        reader = csv.DictReader(file)
        patients = list(reader)

    print(tabulate(patients, headers="keys", tablefmt="grid"))


def get_age():
    while True:
        try:
            age = int(input("Age: "))
            if age <= 0 or age > 100:
                raise ValueError("Invalid Age")
            else:
                break

        except ValueError:
            print("Invalid age")
    return age


def get_height():
    while True:
        try:
            height = float(input("Height (m): "))
            if height <= 0:
                raise ValueError("Invalid height")
            elif height > 2.5:
                raise ValueError("Invalid height")
            else:
                break

        except ValueError:
            print("Invalid height")
    return height


def get_weight():
    while True:
        try:
            weight = float(input("Weight (kg): "))

            if weight <= 0:
                raise ValueError("Invalid weight")
            elif weight > 300:
                raise ValueError("Invalid weight")
            else:
                break

        except ValueError:
            print("Invalid weight")
    return weight


def get_blood_pressure():
    while True:
        try:
            systolic, diastolic = map(int, input("Blood pressure: ").split("/"))

            if systolic <= 0 or diastolic <= 0:
                raise ValueError("Invalid paramater")
            elif systolic > 300 or diastolic > 300:
                raise ValueError("Invalid paramater")
            else:
                break

        except ValueError:
            print("Invalid blood pressure")

    return systolic, diastolic


def get_smoking_status():
    while True:
        try:
            smoking_status = input("Do you smoke? ").upper()
            if not smoking_status in ["YES", "NO"]:
                raise ValueError("Invalid status")
            else:
                break

        except ValueError:
            print("Invalid status")

    return smoking_status


def bmi_category(weight, height):

    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "normal weight"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "obese"

    return bmi, category


def blood_pressure(systolic, diastolic):

    if systolic < 120 and diastolic < 80:
        return "Normal"

    elif 120 <= systolic <= 129 and diastolic < 80:
        return "Elevated"

    elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
        return "Stage 1"

    elif systolic > 180 or diastolic > 120:
        return "Crisis"

    elif systolic >= 140 or diastolic >= 90:
        return "Stage 2"

    else:
        return "Invalid"


def smoking_(smoking_status):
    if "YES" in smoking_status:
        category = "Smoker"
    else:
        category = "Non-smoker"

    return category


if __name__ == "__main__":
    main()
