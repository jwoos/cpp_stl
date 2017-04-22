module Main (main) where

lucky :: (Integral a) => a -> String
lucky 7 = "Lucky number 7!"
lucky x = "Sorry you're out of luck pal"

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n - 1)

listMatch :: (Integral a) => [a] -> [a]
listMatch [] = []
listMatch (x:xs) = [x]

length' :: (Show a, Integral b) => [a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs

aGuard :: (Integral a) => a -> a -> String
aGuard x y
  | z <= 5 = "Less than or equal to 5!"
  | z <= 10 = "Less than or equal to 10!"
  | otherwise = "you're way over"
  where z = x + y


{-
 - Not possible!!!
 - spaceSplit :: String -> [(a)]
 - spaceSplit (a:" ":b) = (a) ++ (b)
 -}

main = print $ aGuard 4 5
