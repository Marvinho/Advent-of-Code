import * as fs from 'fs';

const data = fs.readFileSync('/home/marvin/Documents/Advent-of-Code/2023/day01/input.txt', 'utf-8');

function part1(reg: RegExp) {
  let result = 0;
  let data_arr = data.split('\n');

  data_arr.forEach((row) => {
    let num = row.match(reg);
    if (num) {
      result += Number((num.at(0) ?? '0') + (num.at(-1) ?? '0'));
    }
  });
  console.log(result);
}

function part2(reg: RegExp) {
  const number_dict = {
    one: '1',
    two: '2',
    three: '3',
    four: '4',
    five: '5',
    six: '6',
    seven: '7',
    eight: '8',
    nine: '9',
  };
  let result = 0;
  let data_arr = data.split('\n');

  data_arr.forEach((row) => {
    let num: string[] = matchOverlapping(row, reg);
    if (num?.at(0) && num.at(-1)) {
      let num1 = isNaN(Number(num.at(0))) ? number_dict[num.at(0) as keyof typeof number_dict] : num?.at(0);
      let num2 = isNaN(Number(num.at(-1))) ? number_dict[num.at(-1) as keyof typeof number_dict] : num?.at(-1);
      console.log(num1! + num2);
      result += Number(num1! + num2);
      console.log(result);
    }
  });
}

function matchOverlapping(input: string, reg: RegExp) {
  const matches: string[] = [];
  let found: RegExpExecArray | null;
  while ((found = reg.exec(input))) {
    matches.push(found[0]);
    reg.lastIndex -= found[0].length - 1;
  }
  return matches;
}

let reg: RegExp;
reg = /\d/g;
part1(reg);
reg = /one|two|three|four|five|six|seven|eight|nine|\d/g;
part2(reg);
let asdf = 'asdf';
asdf.at(0);
