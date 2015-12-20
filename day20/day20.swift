import Foundation

// Advent of Code 2015
//
// Day 20: Infinite Elves and Infinite Houses
//
// Giacomo Boccardo 2015

// For the best performances, run from command line using -Ounchecked, i.e.:
//
// $ time swift -Ounchecked day20.swift
// Part 1/2: 831600/884520
//
// real	0m5.025s
// user	0m4.985s
// sys	0m0.035s


func getDivisors(n: Int) -> [Int] {
    var divisors: [Int] = []

    let step = n % 2 == 0 ? 1 : 2

    for i in 1.stride(through: Int(sqrt(Double(n))), by: step) {
        if n % i == 0 {
            divisors.append(i)
            let div = n / i
            if i != div {
                divisors.append(div)
            }
        }
    }

    return divisors
}

func main() {
    let input = 36000000
    let input_div_10 = input / 10
    let input_div_11 = input / 11
    let part_2_house_limit = 50

    var house = 1
    var part_1 = 0
    var part_2 = 0

    while part_1 == 0 || part_2 == 0 {

        let divisors = getDivisors(house)

        if part_1 == 0 && divisors.reduce(0, combine: +) >= input_div_10 {
            part_1 = house
        }

        if part_2 == 0 && divisors.filter({house / $0 <= part_2_house_limit}).reduce(0, combine: +) >= input_div_11 {
            part_2 = house
        }

        house++
    }

    print("Part 1/2: \(part_1)/\(part_2)")

}

main()


