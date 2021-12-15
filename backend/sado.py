from simpful import *

class Sado:

    def __init__(self):
        self.calorie = 0

    def start(self, v_weight, v_height, v_age, v_bmi, v_intensity):
        FS = FuzzySystem()

        """
            Define fuzzy set
        """
        
        # Weight
        P1 = FuzzySet(function=Triangular_MF(a=50,b=50,c=68), term="light")
        P2 = FuzzySet(function=Triangular_MF(a=55,b=68,c=82), term="average")
        P3 = FuzzySet(function=Triangular_MF(a=68,b=110,c=110), term="heavy")
        LV1 = LinguisticVariable([P1,P2,P3], concept="Weight", universe_of_discourse=[50,110])
        FS.add_linguistic_variable("Weight", LV1)
        
        # Height
        P1 = FuzzySet(function=Trapezoidal_MF(a=160,b=160,c=162.5,d=165), term="short")
        P2 = FuzzySet(function=Trapezoidal_MF(a=162.5,b=165,c=175,d=177.5), term="average")
        P3 = FuzzySet(function=Trapezoidal_MF(a=175,b=177.5,c=180,d=180), term="tall")
        LV2 = LinguisticVariable([P1,P2,P3], concept="Height", universe_of_discourse=[160,180])
        FS.add_linguistic_variable("Height", LV2)

        # Age
        P1 = FuzzySet(function=Trapezoidal_MF(a=20,b=20,c=26,d=30), term="young")
        P2 = FuzzySet(function=Trapezoidal_MF(a=25,b=30,c=50,d=55), term="middle")
        P3 = FuzzySet(function=Trapezoidal_MF(a=50,b=55,c=55,d=55), term="old")
        LV3 = LinguisticVariable([P1,P2,P3], concept="Age", universe_of_discourse=[20,60])
        FS.add_linguistic_variable("Age", LV3)

        # BMI
        P1 = FuzzySet(function=Trapezoidal_MF(a=17,b=17,c=17,d=18.5), term="underweight")
        P2 = FuzzySet(function=Trapezoidal_MF(a=17,b=18.5,c=24.5,d=26), term="normal")
        P3 = FuzzySet(function=Trapezoidal_MF(a=23,b=24.5,c=29,d=30.5), term="overweight")
        P4 = FuzzySet(function=Trapezoidal_MF(a=29,b=30.5,c=30.5,d=30.5), term="obese")
        LV4 = LinguisticVariable([P1,P2,P3,P4], concept="BMI", universe_of_discourse=[16,31])
        FS.add_linguistic_variable("BMI", LV4)

        # Intensity
        P1 = FuzzySet(function=Trapezoidal_MF(a=3,b=3,c=3,d=4), term="low")
        P2 = FuzzySet(function=Trapezoidal_MF(a=3,b=4,c=5,d=6), term="moderate")
        P3 = FuzzySet(function=Trapezoidal_MF(a=5,b=6,c=6,d=6), term="high")
        LV5 = LinguisticVariable([P1,P2,P3], concept="Intensity", universe_of_discourse=[1,8])
        FS.add_linguistic_variable("Intensity", LV5)

        # Output
        P1 = FuzzySet(function=Triangular_MF(a=500,b=500,c=1300), term="casual")
        P2 = FuzzySet(function=Triangular_MF(a=1000,b=1400,c=1800), term="low")
        P3 = FuzzySet(function=Triangular_MF(a=1500,b=1900,c=2300), term="moderate")
        P4 = FuzzySet(function=Triangular_MF(a=2000,b=2400,c=2900), term="high")
        P5 = FuzzySet(function=Triangular_MF(a=2500,b=2900,c=2900), term="bulking")
        LV6 = LinguisticVariable([P1,P2,P3,P4,P5], concept="Calorie", universe_of_discourse=[500,3000])
        FS.add_linguistic_variable("Calorie", LV6)
        """
            Define fuzzy rules - Import from text file. Super neat.
        """
        FS.add_rules_from_file(path='list_of_rules.txt')

        
        # Stub value
        FS.set_variable("Weight", v_weight)
        FS.set_variable("Height", v_height)
        FS.set_variable("Age", v_age)
        FS.set_variable("Intensity", v_intensity)
        FS.set_variable("BMI", v_bmi)

        return FS.Mamdani_inference(["Calorie"])

