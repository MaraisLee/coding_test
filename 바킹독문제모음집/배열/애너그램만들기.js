// 1919
// 각 단어별로 알파벳이 담긴 배열 생성 -> 같은 인덱스를 돌면서 값을 뺀 경우 1이상이면 애너그램에서 빼야하는 문자 -> count

const fs = require('fs');
const filePath = process.platform === 'linux' ? 'dev/stdin' : 'input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n');
const [first, second] = input;
const countAlphabets = (string) => {
    const counts = new Array(26).fill(0);
    string.split('').forEach((char) => {
        counts[char.charCodeAt(0) - 97] += 1; // 유니코드 반환 (char의 0번째를 유니코드로) , a의 유니코드는 97
    });
    return counts;
};

const arrayDifferenceCount = (arr1, arr2) => {
    let count = 0;

    arr1.forEach((value, index) => {
        count += Math.abs(value - arr2[index]);
    });

    return count;
};

const counts1 = countAlphabets(first);
const counts2 = countAlphabets(second);

console.log(arrayDifferenceCount(counts1, counts2));
