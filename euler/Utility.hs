module Utility (
    isPrimeNaive,
    maxExponent,
    maxPower
) where

maxExponent :: Integer -> Integer -> Integer
maxExponent num upper = last [x | x <- [1..upper], num^x <= upper]

maxPower :: Integer -> Integer -> Integer
maxPower num upper = last [y | x <- [1..upper], let y = num^x, y <= upper]

isPrimeNaive :: Integer -> Bool
isPrimeNaive n
  | n == 1 || n <= 0 = False
  | length factors == 1 = True
  | otherwise = False
  where factors = [f | f <- [1..(floor $ sqrt $ fromIntegral n)], n `mod` f == 0]
