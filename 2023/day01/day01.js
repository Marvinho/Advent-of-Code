const fs = require("fs");

let data = fs.readFileSync(
  "/home/marvin/Documents/Advent-of-Code/2023/day01/example2.txt",
  "utf-8",
  (err, d) => {
    if (err) {
      throw err;
    }
  }
);

function part1() {
  let result = 0;
  const regex = /\d/g;

  data = data.split("\n");

  data.forEach((element) => {
    let num = element.match(regex);
    result += Number(num.at(0) + num.at(-1));
  });
  console.log(result);
}
//part1();

const number_dict = {
  one: "1",
  two: "2",
  three: "3",
  four: "4",
  five: "5",
  six: "6",
  seven: "7",
  eight: "8",
  nine: "9",
};

function part2() {
  let result = 0;
  const regex = /one|two|three|four|five|six|seven|eight|nine|\d/g;
  data = data.split("\n");

  data.forEach((element) => {
    let num = element.match(regex);
    let num1 = isNaN(num.at(0)) ? number_dict[num.at(0)] : num.at(0);
    let num2 = isNaN(num.at(-1)) ? number_dict[num.at(-1)] : num.at(-1);
    console.log(num1 + num2);
    result += Number(num1 + num2);
  });
  console.log(result);
}
part2();
