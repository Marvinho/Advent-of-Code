import * as fs from 'fs';

const data = fs.readFileSync('/home/marvin/Documents/Advent-of-Code/2023/day02/example.txt', 'utf-8');
const data_arr = data.split('\n');
console.log(data_arr);

const bagContained: { [key: string]: number } = {
  red: 12,
  green: 13,
  blue: 14,
};

let result = 0;

data_arr.forEach((row) => {
  const gameBag: { [key: string]: number } = {
    red: 0,
    green: 0,
    blue: 0,
  };
  let gameId: string;
  let listOfSubsetsOfCubes: string;
  let gameSets: string[];
  let flag: boolean = true;

  [gameId, listOfSubsetsOfCubes] = row.split(':');
  gameSets = listOfSubsetsOfCubes.split(';');
  result += Number(gameId.trim().split(' ')[1]);
  for (const gameSet of gameSets) {
    const colorNumbers: string[] = gameSet.split(',');
    for (const colorNumber of colorNumbers) {
      //console.log(element, value, color);
      const value: string = colorNumber.trim().split(' ')[0];
      const color: string = colorNumber.trim().split(' ')[1];
      if (bagContained[color] < Number(value)) {
        result -= Number(gameId.trim().split(' ')[1]);
        flag = false;
        //console.log(colorNumber);
        break;
      }
    }
    if (!flag) {
      break;
    }
  }
  //console.log(gameId, gameSets, gameSet);
});
console.log(result);
