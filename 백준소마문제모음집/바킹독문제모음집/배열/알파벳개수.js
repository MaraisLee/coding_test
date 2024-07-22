// 현재 실버 3
// 10808
// a~z 중에 단어 S에 몇 개가 포함되어 있는지?
// 알파벳 스트링 선언, 정답배열 생성(26개) -> 알파벳 배열에서 맞는 인덱스의 위치를 찾아서 +1

// O(N)

const S = require('fs').readFileSync('/dev/stdin').toString().split('');

const alphabet = 'abcdefghijklmnopqrstuvwxyz';
const counts = new Array(26).fill(0);

S.forEach((i) => counts[alphabet.indexOf(i)]++);

console.log(counts.join(' '));

/*
charAt()은 해당 문자 반환, charCodeAt()은 해당 문자에 맞는 유니코드 값 반환
*/

/* String.prototype.split()
const str = 'The quick brown fox jumps over the lazy dog.';

const words = str.split(' ');
console.log(words[3]);
// Expected output: "fox"

const chars = str.split('');
console.log(chars[8]);
// Expected output: "k"
*/

/* Array.prototype.join()
const elements = ['Fire', 'Air', 'Water'];

console.log(elements.join());
// Expected output: "Fire,Air,Water"

console.log(elements.join(''));
// Expected output: "FireAirWater"

console.log(elements.join('-'));
// Expected output: "Fire-Air-Water"
*/
