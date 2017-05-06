import Utility
import Data.List

-- 1
multSum :: (Integral a) => a -> a -> a -> a
multSum x y limit = sum $ xMults ++ yMults
  where lim = limit - 1
        xMults = [a | a <- [1..lim], a `mod` x == 0]
        yMults = [a | a <- [1..lim], a `mod` y == 0, not (elem a xMults)]

-- 2
sumFibLim :: (Integral a) => (a -> Bool) -> a -> (a, a) -> a
sumFibLim f lim (x, y) = sum $ takeWhile (<= lim) seq
  where seq = [x | x <- fibonacci, f x]
        fibonacci = x : y : (zipWith (+) fibonacci (tail fibonacci))

-- 3
primeFactors :: Integer -> [Integer]
primeFactors n = [x | x <- [1, 3..(floor $ sqrt $ fromIntegral n)], isPrimeNaive x, n `mod` x == 0]

-- 4
isNumPalindrome :: Integer -> Bool
isNumPalindrome n = str == reverse str
  where str = show n

compareLists :: ([Integer] -> Integer) -> [Integer] -> [Integer] -> Ordering
compareLists fnc a b
  | extractedA > extractedB = GT
  | extractedA < extractedB = LT
  | otherwise = EQ
  where extractedA = fnc a
        extractedB = fnc b

findTwoFactors :: Integer -> Integer -> [Integer]
findTwoFactors lower upper = maximumBy (compareLists last) palindromes
  where factors = [[x, y, x * y] | x <- [lower..upper], y <- [lower..upper]]
        palindromes = [lst | lst@(_:c) <- factors, isNumPalindrome $ last c]

-- 5
leastCommonMultiple1 :: [Integer] -> Integer
leastCommonMultiple1 factors = product primeFactorized
  where primeFactors = filter isPrimeNaive factors
        primeFactorized = map (`maxPower` (last factors)) primeFactors

leastCommonMultiple2 :: [Integer] -> Integer -> Integer
leastCommonMultiple2 factors initial
  | length factors == 0 = initial
  | otherwise = leastCommonMultiple2 factors' (lcm x initial)
  where x = head factors
        factors' = drop 1 factors

-- 6
sumSquareDifference :: Integer -> Integer -> Integer
sumSquareDifference lower upper = sumSquare - squareSum
  where range = [lower..upper]
        sumSquare = (sum range)^2
        squareSum = sum $ map (^2) range
