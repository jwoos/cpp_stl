module MathHelper (
  totient,
  isPrimeNaive,
) where
import System.Random

totient :: Integer -> Integer -> Integer
totient p q = ((p - 1) * (q - 1))

isqrt :: Integer -> Integer
isqrt = floor . sqrt . fromIntegral

isPrimeNaive :: Integer -> Bool
isPrimeNaive n
  | length factors == 1 = True
  | otherwise = False
    where factors = [f | f <- [1..(floor $ sqrt $ fromIntegral n)], n `mod` f == 0]

{-
 -generateRandomNumber :: (Integer, Integer) -> Integer
 -generateRandomNumber bounds
 -  | isPrime n = n
 -  | otherwise n = generateRandom bounds
 -  where n = randomRIO bounds
 -}

{-
-millerRabin :: Integer -> Bool
-
-isPrime :: Integer -> Bool
-isPrime x = [a | a <- l, x^(a) `mod` ]
-    where l = [1..(x-1)]
-}

