
-- This solution uses comprehension to construct a list of multiples, then
-- sums the lsit
-- As both of these operations are O(n) the algorithm is O(n)
firstSolution :: Int
firstSolution = sum ([x | x <- [0..1000 -1], x `mod` 5==0 || x `mod` 3==0])
