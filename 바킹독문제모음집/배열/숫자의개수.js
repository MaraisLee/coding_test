// 2577
// a*b*c 한값을 forEach 돌려서 0~9 횟수 배열에 넣기 ++
const input = require('fs')
    .readFileSync('input.txt')
    .toString()
    .trim()
    .split('\n');

const multiply = (input[0] * input[1] * input[2]).toString();
const answer = new Array(10).fill(0);
for (let i = 0; i < multiply.length; i++) {
    answer[multiply[i]]++;
}

answer.forEach((v, i) => {
    console.log(answer.slice(i, i + 1).toString()); //toString을 하지않으면 배열로 반환값 나옴
});