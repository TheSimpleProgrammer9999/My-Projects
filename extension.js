// class StrictEqualityExtension {
//     getInfo() {
//     return {
//         id: 'strictequalityexample',
//         name: 'Strict Equality',
//         blocks: [
//         {
//             opcode: 'Encode',
//             blockType: Scratch.BlockType.BOOLEAN,
//             text: 'Encode number [ONE] to [TWO]',
//             arguments: {
//             ONE: {
//                 type: Scratch.ArgumentType.NUMBER
//             },
//             TWO: {
//                 type: Scratch.ArgumentType.STRING,
//                 defaultValue: 'binary'
//             }
//             }
//         }
//         ]
//     };
//     }

//     Encode(args) {
//     return args.ONE === args.TWO;
//     }
// }
// Scratch.extensions.register(new StrictEqualityExtension());

class StringsNumbersAParameters {
getInfo() {
    return {
    id: 'strings1example',
    name: 'Strings, Numbers, and Placeholders',
    blocks: [
        {
        opcode: 'up_or_low',
        blockType: Scratch.BlockType.REPORTER,
        text: 'convert string [STR] to [THING]',
        arguments: {
            STR: {
            type: Scratch.ArgumentType.STRING,
            defaultValue: ''
            },
            THING: {
            type: Scratch.ArgumentType.STRING,
            menu: 'FORMAT_MENU'
            }
        }
        },

        {
            opcode: 'randomnum',
            blockType: Scratch.BlockType.REPORTER,
            text: "generate random floats"
        },
        {
            opcode: 'pi',
            blockType: Scratch.BlockType.REPORTER,
            text: "pi"
        },
        {
            opcode: 'euler',
            blockType: Scratch.BlockType.REPORTER,
            text: 'euler'
        },
        {
            opcode: 'sqrt2',
            blockType: Scratch.BlockType.REPORTER,
            text: 'sqrt of 2'
        },
        {
            opcode: 'printInConsole',
            blockType: Scratch.BlockType.COMMAND,
            text: 'print in console [STRTEXT]',
            arguments: {
                STRTEXT: {
                    type: Scratch.ArgumentType.STRING,
                    defaultValue: 'hello'
                }
            }
        },
        {
            opcode: 'lenOfText',
            blockType: Scratch.BlockType.REPORTER,
            text: 'length of string [LENSTR]',
            arguments: {
                LENSTR: {
                    type: Scratch.ArgumentType.STRING,
                    defaultValue: 'whats up?'
                }
            }
        },
        {
            opcode: 'messageWrite',
            blockType: Scratch.BlockType.COMMAND,
            text: 'create messagebox with text [MESSAGETEXT]',
            arguments: {
                MESSAGETEXT: {
                    type: Scratch.ArgumentType.STRING,
                    defaultValue: 'hello, world!'
                }
            }
        },
        {
            opcode: 'nothing',
            blockType: Scratch.BlockType.COMMAND,
            text: 'do nothing'
        }
    ],
    menus: {
        FORMAT_MENU: {
        acceptReporters: true,
        items: [
            {
              text: 'uppercase',
              value: 'up'
            },
            {
              text: 'lowercase',
              value: 'low'
            },
            {
                text: 'anonymous(not in use)',
                value: 'anon'
            }
          ]
        }
    }
    };
}

up_or_low (args) {
    if (args.THING === 'up') {
    // Notice the toString() call: TEXT might be a number or boolean,
    // so we have to make sure to convert it to a string first so that
    // it has a toUpperCase() function, otherwise we will get an error!
    // Remember: the argument's "type" is just a suggestion for the
    // editor; it's never enforced.
    return args.STR.toString().toUpperCase();
    } if (args.THING==='low') {
    return args.STR.toString().toLowerCase();
    } else {
        return "";
    }
}

randomnum() {
    return Math.random();
}

pi() {
    return Math.PI;
}

euler() {
    return Math.E;
}

sqrt2() {
    return Math.sqrt(2)
}

printInConsole(args) {
    console.log(args.STRTEXT)
}

lenOfText(args) {
    return args.LENSTR.length
}

messageWrite(args) {
    alert(args.MESSAGETEXT)
}

nothing() {
    return ;
}

}
Scratch.extensions.register(new StringsNumbersAParameters());


  