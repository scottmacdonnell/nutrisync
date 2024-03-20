import Foundation

func readInput<T>(promptMessage: String, convert: (String) -> T?) -> T {
    while true {
        print("\(promptMessage): ", terminator: "")
        
        // Read the input as a string
        if let inputString = readLine(), let value = convert(inputString) {
            return value
        } else {
            print("Invalid input. Please enter a valid value.")
        }
    }
}

var weight: Float = readInput(promptMessage: "Enter your weight in lbs", convert: { Float($0) })
var height: Float = readInput(promptMessage: "Enter your height in cm", convert: { Float($0) })
var age: Int = readInput(promptMessage: "Enter your age in years", convert: { Int($0) })
var gender: Character = readInput(promptMessage: "Enter your gender as M or F", convert: { Character($0) })

print("Weight: \(weight)lbs")
print("Height: \(height)cm")
print("Age: \(age)")
print("Gender: \(gender)")