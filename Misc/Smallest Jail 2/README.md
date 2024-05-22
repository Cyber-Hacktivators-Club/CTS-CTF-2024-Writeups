Cannot call help() bcz file is run with python -S flag in shebang
1- Python using compatibility unicode . So unicode compatible chars will be normalized to ascii if possible. We will use unicode ligatures for 'fl' and 'ij' to lessen the chars of exploit
2- We cannot use print() to print() data, but we can use stderr to print() the output and in lesser chars
3- The least char to induce the error is {}[] (type casting array to dict)
