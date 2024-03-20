import Foundation

enum Gender {
    case male
    case female
}

enum ActivityLevel {
    case sedentary
    case lightlyActive
    case moderatelyActive
    case heavilyActive

    var multiplier: Float {
        switch self {
        case .sedentary: return 1.2
        case .lightlyActive: return 1.375
        case .moderatelyActive: return 1.55
        case .heavilyActive: return 1.725
        }
    }
}

enum WeeklyWeightGoal {
    case weightGain
    case weightLoss

    var description: String {
        switch self {
        case .weightGain: return "Weight Gain"
        case .weightLoss: return "Weight Loss"
        }
    }

    var dailyCalorieAdjustment: Int {
        switch self {
        case .weightGain: return +250
        case .weightLoss: return -250
        }
    }
}

func readInput<T>(promptMessage: String, convert: (String) -> T?) -> T {
    while true {
        print("\(promptMessage): ", terminator: "")
        if let inputString = readLine(), let value = convert(inputString) {
            return value
        } else {
            print("Invalid input. Please enter a valid value.")
        }
    }
}

func convertToGender(input: String) -> Gender? {
    switch input.lowercased() {
    case "male", "m":
        return .male
    case "female", "f":
        return .female
    default:
        return nil
    }
}

func convertToActivityLevel(input: String) -> ActivityLevel? {
    switch input.lowercased() {
    case "1", "sedentary": return .sedentary
    case "2", "lightly active": return .lightlyActive
    case "3", "moderately active": return .moderatelyActive
    case "4", "heavily active": return .heavilyActive
    default: return nil
    }
}

func convertToWeeklyWeightGoal(input: String) -> WeeklyWeightGoal? {
    switch input.lowercased() {
    case "1", "weight gain": return .weightGain
    case "2", "weight loss": return .weightLoss
    default: return nil
    }
}

func calculateBMR(gender: Gender, weight: Float, height: Float, age: Int) -> Float {
    switch gender {
    case .male:
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * Float(age))
    case .female:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * Float(age))
    }
}

func calculateTDEE(bmr: Float, activityLevel: ActivityLevel) -> Float {
    return bmr * activityLevel.multiplier
}

func calculateAdjustedCalories(tdee: Float, weeklyWeightGoal: WeeklyWeightGoal) -> Float {
    return tdee + Float(weeklyWeightGoal.dailyCalorieAdjustment)
}

let gender: Gender = readInput(promptMessage: "Enter your gender (male/female)", convert: convertToGender)
let weight: Float = readInput(promptMessage: "Enter your weight in kilograms", convert: Float.init)
let height: Float = readInput(promptMessage: "Enter your height in centimeters", convert: Float.init)
let age: Int = readInput(promptMessage: "Enter your age", convert: Int.init)
let activityLevel: ActivityLevel = readInput(promptMessage: """
Enter your activity level:
1. Sedentary
2. Lightly Active
3. Moderately Active
4. Heavily Active
""", convert: convertToActivityLevel)
let weeklyWeightGoal: WeeklyWeightGoal = readInput(promptMessage: """
Enter your weekly weight goal:
1. Weight Gain
2. Weight Loss
""", convert: convertToWeeklyWeightGoal)

let bmr = calculateBMR(gender: gender, weight: weight, height: height, age: age)
let tdee = calculateTDEE(bmr: bmr, activityLevel: activityLevel)
let adjustedCalories = calculateAdjustedCalories(tdee: tdee, weeklyWeightGoal: weeklyWeightGoal)

print("Weight: \(weight)kg")
print("Height: \(height)cm")
print("Age: \(age)")
print("Gender: \(gender)")
print("The BMR is \(bmr) calories/day.")
print("Based on your activity level, your TDEE is \(tdee) calories/day.")
print("Based on your activity level and weight goal, your adjusted daily calorie intake should be approximately \(adjustedCalories) calories.")