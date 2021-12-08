{-# LANGUAGE BinaryLiterals #-}

import Data.Map (Map)
import qualified Data.Map as M
import Data.Set (Set)
import qualified Data.Set as S
import Data.Word
import Data.Bits
import Data.Char
import Data.List
import Data.List.Split
import Data.Maybe
import Data.Foldable

trueSegments = M.fromList
    --      gfedcba
    [ (0, 0b1110111)
    , (1, 0b0100100)
    , (2, 0b1011101)
    , (3, 0b1101101)
    , (4, 0b0101110)
    , (5, 0b1101011)
    , (6, 0b1111011)
    , (7, 0b0100101)
    , (8, 0b1111111)
    , (9, 0b1101111)
    ] :: Map Word Int

validSegments = S.fromList $ M.elems trueSegments

main = do
    input <- getContents
    let testData = parseLine <$> lines input
    --print testData
    let (t, _) = testData !! 0
    dumpTable $ solveEasy t

parseSegment :: String -> Word
parseSegment s = foldl' (.|.) 0 $ p <$> s
  where
    p c = let d = fromIntegral $ fromEnum c - fromEnum 'a' in 1 `shift` d

parseLine :: String -> ([Word], [Word])
parseLine l = let [a, b] = splitOn "|" l in (parseSegment <$> words a, parseSegment <$> words b)

segmentSums :: [Word] -> [Int]
segmentSums os = flip fmap [0..6] $ \i -> sum (f i <$> os)
  where
    f i o = if testBit o i then 1 else 0

translate :: Word -> Map Int Int -> Word
translate os table = foldl' (.|.) 0 $ flip fmap [0..6] $ \i ->
    if testBit os (1 `shift` i) then 1 `shift` (table M.! i) else 0

solveEasy :: [Word] -> Map Int Int
solveEasy os = M.fromList [(bi, 1), (4, ei), (5, fi)]
  where
    bi = fromJust $ findIndex (== 6) ss
    ei = fromJust $ findIndex (== 4) ss
    fi = fromJust $ findIndex (== 9) ss
    ss = segmentSums os

dumpTable :: Map Int Int -> IO ()
dumpTable table = do for_ (M.toList table) $ \(f, t) -> print (c f, c t)
  where
    c x = chr (x + ord 'a')
