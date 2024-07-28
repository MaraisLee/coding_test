// 13300

const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const max = parseInt(input[0].split(' ')[1]);
let array = [];
let roomNum = 0;

for (let i = 0; i < 6; i++) {
    array.push([0, 0]);
}
for (let i in input) {
    // i는 인덱스
    if (i === 0) continue;
    array[parseInt(input[i].split(' ')[1]) - 1][
        parseInt(input[i].split(' ')[0])
    ]++;
    // input[1]부터 학생정보 나옴 '1 1' -> 남자, 1학년 / '0 2' -> 여자, 2학년
}

for (let i in array) {
    roomNum += Math.ceil(array[i][0] / max);
    roomNum += Math.ceil(array[i][1] / max);
}
console.log(roomNum);
