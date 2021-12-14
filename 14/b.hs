import Data.List.Extra
import qualified Data.Map.Strict as M
import Data.Map.Strict (Map)

main = do
    input <- getContents
    let (initial, rules) = parse input
    let after = iterate (step rules) initial !! 40
    print $ mostMinusLeast after

step :: Map String Char -> Map String Int -> Map String Int
step rules origTable = M.foldrWithKey apply origTable rules
  where
    apply from@[f1, f2] ins table = case origTable M.!? from of
        Nothing -> table
        Just fc -> add [f1, ins] fc $ add [ins, f2] fc $
            add from (negate fc) $ add [ins] fc $ table
    add = M.insertWith (+)

parse :: String -> (Map String Int, Map String Char)
parse s = (counts $ pairs init, rules)
  where
    [init, rest] = splitOn "\n\n" s
    rules = M.fromList $ (\[a, [b]] -> (a, b)) . splitOn " -> " <$> lines rest

pairs :: String -> [String]
pairs s = ((:[]) <$> s) ++ ((\(a, b) -> [a, b]) <$> zip s (tail s))

counts :: [String] -> Map String Int
counts = foldl' f M.empty
  where
    f acc x = M.insertWith (+) x 1 acc

mostMinusLeast table = let cs = sort $ fmap snd $ filter f $ M.toList table
    in last cs - head cs
  where
    f (k, v) = length k == 1 && v /= 0
