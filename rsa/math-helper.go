package main

import (
	"math/big"
	"crypto/rand"
)

func randomPrimeRanged(min uint64, max uint64) (*big.Int, error) {
	maxBigInt := big.NewInt(0);
	maxBigInt.SetUint64(max);

	minBigInt := big.NewInt(0);
	minBigInt.SetUint64(min);

	p, err := rand.Int(rand.Reader, maxBigInt);

	if err != nil {
		return big.NewInt(0), err;
	}

	return p, nil;
}

func randomPrime(max uint64) (*big.Int, error) {
	maxBigInt := big.NewInt(0);
	maxBigInt.SetUint64(max + 1);

	primeNumber, err := rand.Int(rand.Reader, maxBigInt);

	if err != nil {
		return big.NewInt(0), err;
	}

	if primeNumber.ProbablyPrime(5) {
		return primeNumber, nil
	} else {
		return randomPrime(max);
	}
}

func totient(p *big.Int, q *big.Int) *big.Int {
	one := big.NewInt(1);

	tempP := big.NewInt(0);
	tempQ := big.NewInt(0);

	tempP.Sub(p, one);
	tempQ.Sub(q, one);

	product := big.NewInt(0);
	product.Mul(tempP, tempQ);

	return product;
}
