// 10807
// 정수 N개 -> 배열을 돌면서 정수 v와 같은 걸 만나면 count += 1
const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const [N, S, V] = input; // 배열 분해 할당
const cnt = S.split(' ').filter((i) => i === V).length; // filter에 맞는 원소들을 배열로 반환
// console.log(S.split(' ')); // 반환값도 기존의 값 형태랑 같음 -> ['1', '2']
console.log(cnt);