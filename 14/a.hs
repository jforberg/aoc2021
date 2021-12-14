import Data.List.Extra
import qualified Data.Map.Strict as M
import Data.Map.Strict (Map)

main = do
    input <- getContents
    let (s, rules) = parse input
    let after = iterate (step rules) s !! 10
    print $ mostMinusLeast after

step rules (c1:c2:cs) = case rules M.!? [c1, c2] of
    Nothing -> c1 : step rules (c2:cs)
    Just ins -> c1 : ins : step rules (c2:cs)
step _ cs = cs

parse s = (init, rules)
  where
    [init, rest] = splitOn "\n\n" s
    rules = M.fromList $ (\[a, [b]] -> (a, b)) . splitOn " -> " <$> lines rest

counts :: [Char] -> [Int]
counts = M.elems . foldr f M.empty
  where
    f x acc = M.insertWith (+) x 1 acc

mostMinusLeast xs = let cs = sort $ counts xs in last cs - head cs
