module Main (main) where

import qualified Data.Map as Map
import qualified Data.List as List

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

maximum' :: (Ord a) => [a] -> a
maximum' [] = error "maximum of empty list"
maximum' [x] = x
maximum' (x:xs)
  | x > maxEnd = x
  | otherwise = maxEnd
  where maxEnd = maximum' xs

replicate' :: (Integral a) => a -> a -> [a]
replicate' x y
  | y < 0 = error "Can't have negative repetitions!"
  | y == 0 = []
  | y == 1 = [x]
  | otherwise = [x] ++ replicate' x (y - 1)

take' :: (Show a, Integral b) => b -> [a] -> [a]
take' 0 a = []
take' n [] = []
take' n (x:xs) = x:take' (n - 1) xs

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = smaller ++ [x] ++ bigger
  where smaller = quicksort [a | a <- xs, a <= x]
        bigger = quicksort [a | a <- xs,  a > x]

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _ = []
zipWith' _ _ [] = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys

findKey :: (Eq k) => k -> [(k,v)] -> Maybe v
findKey key = foldr (\(k,v) acc -> if key == k then Just v else acc) Nothing

data Point = Point Float Float deriving (Show)
data Shape = Circle Point Float | Rectangle Point Point deriving (Show)

surface :: Shape -> Float
surface (Circle _ r) = pi * r^2
surface (Rectangle (Point x1 y1) (Point x2 y2)) = (abs $ x2 - x1) * (abs $ y2 - y1)

data Rank = Ace | Two | Three | Four | Five | Six | Seven | Eight | Nine | Ten | Jack | Queen | King deriving (Show, Eq, Enum, Ord, Read)
data Suit = Diamonds | Clubs | Hearts | Spades deriving (Show, Eq, Enum, Ord, Read)

data Person = Person {
  firstName :: String,
  lastName :: String,
  age :: Int,
  height :: Float,
  phoneNumber :: String
} deriving (Show)

main = print $ aGuard 4 5
