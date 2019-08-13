'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    const vowels = [];
    const consonants = [];

    const vowelsDefinition = ['a', 'e', 'i', 'o', 'u'];

    [...s].forEach(letter => {
        if (vowelsDefinition.indexOf(letter) > -1) {
            vowels.push(letter);
        }
        else {
            consonants.push(letter);
        }
    });
    // vowels.map(vowel => console.log(vowel));
    // consonants.map(consonant => console.log(consonant));
    const vowelsResult = vowels.join('\n');
    const consonantsResult = consonants.join('\n');
    console.log(vowelsResult);
    console.log(consonantsResult);
}

