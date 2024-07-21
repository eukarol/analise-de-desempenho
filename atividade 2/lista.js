const fs = require('fs');
const readline = require('readline');

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    add(value, position) {
        const newNode = new Node(value);
        if (position === 0) {
            newNode.next = this.head;
            this.head = newNode;
            return;
        }
        let current = this.head;
        let count = 0;
        while (current !== null && count < position - 1) {
            current = current.next;
            count++;
        }
        if (current === null) {
            console.log('Posição fora do alcance');
        } else {
            newNode.next = current.next;
            current.next = newNode;
        }
    }

    remove(value) {
        let current = this.head;
        let prev = null;
        while (current !== null) {
            if (current.value === value) {
                if (prev === null) {
                    this.head = current.next;
                } else {
                    prev.next = current.next;
                }
                return;
            }
            prev = current;
            current = current.next;
        }
        console.log('Valor não encontrado na lista');
    }

    printList() {
        let current = this.head;
        while (current !== null) {
            process.stdout.write(`${current.value} -> `);
            current = current.next;
        }
        console.log('None');
    }
}

async function executeActions(filename) {
    try {
        const fileStream = fs.createReadStream(filename);
        const rl = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });

        const linkedList = new LinkedList();
        let isFirstLine = true;
        
        for await (const line of rl) {
            if (isFirstLine) {
                const initialList = line.split(' ').map(Number);
                initialList.reverse().forEach(value => linkedList.add(value, 0));
                isFirstLine = false;
            } else {
                const parts = line.split(' ');
                if (parts.length === 0) {
                    continue;
                }
                const actionType = parts[0];
                if (actionType === 'A' && parts.length === 3) {
                    const value = parseInt(parts[1]);
                    const position = parseInt(parts[2]);
                    linkedList.add(value, position);
                } else if (actionType === 'R' && parts.length === 2) {
                    const value = parseInt(parts[1]);
                    linkedList.remove(value);
                } else if (actionType === 'P') {
                    linkedList.printList();
                }
            }
        }
    } catch (err) {
        console.error(`Erro: O arquivo '${filename}' não foi encontrado. Tente novamente.`);
    }
}

(async function() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    while (true) {
        const filename = await new Promise((resolve) => {
            rl.question('Digite o nome do arquivo:\n', resolve);
        });
        await executeActions(filename);
        break;
    }
    rl.close();
})();
