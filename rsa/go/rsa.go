package main

import (
	"fmt"
	"os"
	//"strconv"
	"math/big"
)

func generate() map[string]*big.Int {
	const MAX = 255;
	var keys map[string]*big.Int
	keys = make(map[string]*big.Int)

	n := big.NewInt(0);
	t := big.NewInt(0);
	d := big.NewInt(0);

	p, errA := randomPrime(MAX);
	q, errB := randomPrime(MAX);

	if (errA != nil) || (errB != nil) {
		return keys;
	}


	n.Mul(p, q);

	t = totient(p, q);
	e, err := randomPrime(t.Uint64());

	d.ModInverse(e, t);

	if err != nil {
		return keys;
	}

	fmt.Println("p:", p);
	fmt.Println("q:", q);
	fmt.Println("n:", n);
	fmt.Println("t:", t);
	fmt.Println("e:", e);
	fmt.Println("d:", d);

	keys["pub1ic1"] = n;
	keys["public2"] = e;
	keys["private"] = d;

	return keys;
}

func encrypt(m string, n string, e string) *big.Int {
	mBigInt, errM := big.NewInt(0).SetString(m, 10);
	nBigInt, errN := big.NewInt(0).SetString(n, 10);
	eBigInt, errE := big.NewInt(0).SetString(e, 10);

	if !errM || !errN || !errE {
		return big.NewInt(0);
	}

	hashed := big.NewInt(0);
	hashed.Exp(mBigInt, eBigInt, nBigInt);

	return hashed;
}

func decrypt(hash string, d string, n string) *big.Int {
	hashBigInt, errHash := big.NewInt(0).SetString(hash, 10);
	dBigInt, errD := big.NewInt(0).SetString(d, 10);
	nBigInt, errN := big.NewInt(0).SetString(n, 10);

	if !errHash || !errD || !errN {
		return big.NewInt(0);
	}

	decrypted := big.NewInt(0);
	decrypted.Exp(hashBigInt, dBigInt, nBigInt);

	return decrypted;
}

func main() {
	args := os.Args[1:];
	if (len(args) == 0) {
		fmt.Println("Please provide a command");
		return;
	}

	if args[0] == "generate" {
		keys := generate();
		fmt.Println("public key part 1:", keys["pub1ic1"]);
		fmt.Println("public key part 2:", keys["public2"]);
		fmt.Println("private key:", keys["private"]);
	} else if args[0] == "encrypt" {
		encrypted := encrypt(args[1], args[2], args[3]);
		fmt.Println(encrypted);
	} else if args[0] == "decrypt" {
		decrypted := decrypt(args[1], args[2], args[3]);
		fmt.Println(decrypted);
	} else {
		fmt.Println("Invalid option");
	}
}
