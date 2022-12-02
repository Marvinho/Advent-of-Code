const path = require('path');
const fs = require('fs');

const input = fs.readFileSync(path.join('.','testinput.txt'), 'utf8').trimEnd();

function asdf(input){
    const test = input.split('\r\n');
    return test;
}
console.log(asdf(input).length);
