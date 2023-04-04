def solution(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0]) if number > 0 else 0

"""
// Solution in a single smart, organized, structured and constructed function in JavaScript that can pass all the test cases:
function solution(number){
    return number > 0 ? Array.from({length: number}, (_, i) => i).filter(i => i % 3 === 0 || i % 5 === 0).reduce((a, b) => a + b, 0) : 0;
}
"""
