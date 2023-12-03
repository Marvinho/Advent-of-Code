import * as fs from 'fs';

const data = fs.readFileSync('/home/marvin/Documents/Advent-of-Code/2023/day01/example.txt', 'utf-8');

function part1() {
  let result = 0;
  const regex = /\d/g;

  let data_arr = data.split('\n');

  data_arr.forEach((element) => {
    let num = element.match(regex);
    if (num) {
      result += Number((num.at(0) ?? '0') + (num.at(-1) ?? '0'));
    }
  });
  console.log(result);
}
//part1();

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

function part2() {
  let result = 0;
  const regex = /one|two|three|four|five|six|seven|eight|nine|\d/g;
  let data_arr = data.split('\n');

  data_arr.forEach((element) => {
    let num: RegExpMatchArray = element.match(regex)!;
    if (num?.at(0) && num.at(-1)) {
      let num1 = isNaN(Number(num.at(0))) ? number_dict[num.at(0) as keyof typeof number_dict] : num?.at(0);
      let num2 = isNaN(Number(num.at(-1))) ? number_dict[num.at(-1) as keyof typeof number_dict] : num?.at(-1);
      console.log(num1! + num2);
      result += Number(num1! + num2);
      console.log(result);
    }
  });
}
part2();
