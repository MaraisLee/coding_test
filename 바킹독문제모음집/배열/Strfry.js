// 11328
// 각 단어를 정렬해서 동일하면 Possible 아니면 impossible

const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const T = parseInt(input[0]);

for (let i = 1; i <= T; i++) {
    // 1번째부터 case 시작
    const [str1, str2] = input[i].split(' ');

    const sortedStr1 = str1.split('').sort().join(''); // string -> array -> sort -> string
    const sortedStr2 = str2.split('').sort().join('');
    if (sortedStr1 === sortedStr2) {
        console.log('Possible');
    } else {
        console.log('Impossible');
    }
}
