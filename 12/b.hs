import qualified Data.Map.Strict as M
import Data.Map.Strict (Map)
import qualified Data.Set as S
import Data.Set (Set)
import Data.List.Extra
import Data.Char
import Data.Maybe
import Debug.Trace

parse = accMaps . fmap ((\[a, b] -> (a, b)) . splitOn "-") . lines
  where
    accMaps ps = (foldr f M.empty ps, foldr g M.empty ps)
    f (k, v) acc = M.alter (comb v) k acc
    g (v, k) acc = M.alter (comb v) k acc
    comb v Nothing = Just [v]
    comb v (Just ov) = Just $ v : ov

invert m = foldr

isBig :: String -> Bool
isBig = all isUpper

search edges = search' edges (False, S.empty) "start"

search' edges (hasRevisited, visited) current
  | current == "end"             = 1
  | isRevisit && not revisitOk   = 0
  | otherwise                    = sum' $ do
        e <- nextEdges
        pure $ search' edges nextVisited e
  where
    nextEdges = getNextEdges edges current
    nextVisited
      | isBig current         = (hasRevisited, visited)
      | otherwise             = (isRevisit || hasRevisited, current `S.insert` visited)
    isRevisit = current `S.member` visited
    revisitOk = not hasRevisited && current /= "start"

getNextEdges (m1, m2) f = fwd f m1 ++ fwd f m2
  where
    fwd = M.findWithDefault []

main = do
    s <- getContents
    let edges = parse s
    print $ search edges
