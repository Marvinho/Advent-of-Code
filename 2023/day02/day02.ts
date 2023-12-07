import * as fs from 'fs';

const data = fs.readFileSync('/home/marvin/Documents/Advent-of-Code/2023/day02/input.txt', 'utf-8');
const data_arr = data.split('\n');
console.log(data_arr);

const bagContained: { [key: string]: number } = {
  red: 12,
  green: 13,
  blue: 14,
};

let result = 0;

function part1() {
  data_arr.forEach((row) => {
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
}

//part1();
function part2() {
  result = 0;
  data_arr.forEach((row) => {
    const gameBag: { [key: string]: number } = {
      red: 0,
      green: 0,
      blue: 0,
    };
    let gameId: string;
    let listOfSubsetsOfCubes: string;
    let gameSets: string[];

    [gameId, listOfSubsetsOfCubes] = row.split(':');
    gameSets = listOfSubsetsOfCubes.split(';');

    for (const gameSet of gameSets) {
      const colorNumbers: string[] = gameSet.split(',');
      for (const colorNumber of colorNumbers) {
        const value: number = Number(colorNumber.trim().split(' ')[0]);
        const color: string = colorNumber.trim().split(' ')[1];
        if (gameBag[color] === 0) {
          gameBag[color] = value;
          continue;
        }
        if (gameBag[color] < value) {
          gameBag[color] = value;
          continue;
        }
      }
    }
    //console.log(gameId, gameSets, gameSet);
    console.log(gameBag, powerOfSetOfCubes(gameBag));
    result += powerOfSetOfCubes(gameBag);
  });
  console.log(result);
}

const powerOfSetOfCubes = (gameBag: { [key: string]: number }): number => {
  return gameBag['blue'] * gameBag['red'] * gameBag['green'];
};
part2();
