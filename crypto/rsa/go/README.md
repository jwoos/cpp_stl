# RSA
This is a RSA implementation in Go, for practice.

Referred to: https://en.wikipedia.org/wiki/RSA_(cryptosystem)

### Usage
`generate`: returns your public and private keys
`encrypt`: self explanatory
`decrypt`: self explanatory


```bash
$ ./go_rsa generate
p: 149
q: 113
n: 16837
t: 16576
e: 6733
d: 517
public key part 1: 16837
public key part 2: 6733
private key: 517

$ ./go_rsa encrypt 12345 16837 6733
1578

$ ./go_rsa decrypt 1578 517 16837
12345
```

### Limitations
- Random number generation is bounded to a max of 255
