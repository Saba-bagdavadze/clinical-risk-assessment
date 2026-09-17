def main():
    print(risk_category(2))

    print(bmi_calc(1))

    print(bp_points_calc(2))

    print(smoking_calc(1))

def risk_category(total_points):

    if total_points in [0,1]:
        return "Low risk"
    elif total_points in [2,3]:
        return "Moderate risk"
    elif total_points in [4,5]:
        return "High risk"
    else:
        return "Very high risk"

def bmi_calc(category):

    bmi_points = 0
    if category == "normal weight":
        bmi_points += 0
    elif category == "overweight":
        bmi_points += 1
    elif category == "obese":
        bmi_points += 2

    return bmi_points


def bp_points_calc(category):

    blood_pressure_points = 0
    if category == "Normal":
        blood_pressure_points += 0
    elif category == "Elevated":
        blood_pressure_points += 1
    elif category == "Stage 1":
        blood_pressure_points += 2
    elif category == "Stage 2":
        blood_pressure_points += 3
    elif category == "Crisis":
        blood_pressure_points += 4
    else:
        blood_pressure_points += 0

    return blood_pressure_points

def smoking_calc(category):

    smoking_points = 0
    if category == "Smoker":
        smoking_points += 1
    else:
        smoking_points += 0

    return smoking_points


if __name__ == "__main__":
    main()
