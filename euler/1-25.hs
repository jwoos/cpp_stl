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
isPrimeNaive :: Integer -> Bool
isPrimeNaive n
  | length factors == 1 = True
  | otherwise = False
  where factors = [f | f <- [1, 3..(floor $ sqrt $ fromIntegral n)], n `mod` f == 0]

primeFactors :: Integer -> [Integer]
primeFactors n = [x | x <- [1, 3..(floor $ sqrt $ fromIntegral n)], isPrimeNaive x, n `mod` x == 0]
