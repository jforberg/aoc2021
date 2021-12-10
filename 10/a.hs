import qualified Data.Map as M
import Data.Map (Map)

data Close = Open | Valid | Invalid
    deriving (Show, Eq)

closingMap = M.fromList
    [ ('(', ')')
    , ('[', ']')
    , ('{', '}')
    , ('<', '>')
    ]

main = do
    ls <- lines <$> getContents
    print $ sum $ parse <$> ls

parse :: String -> Int
parse (x:xs) = fst $ block x xs

block :: Char -> String -> (Int, String)
block c "" = (0, "")
block c (x:xs) = case closing c x of
    Valid -> (0, xs)
    Open -> let (v, rest) = block x xs in if v /= 0 then (v, "") else block c rest
    Invalid -> (value x, "")

closing :: Char -> Char -> Close
closing a b
    | closingMap M.! a == b     = Valid
    | b `M.member` closingMap   = Open
    | otherwise                 = Invalid

value :: Char -> Int
value ')' = 3
value ']' = 57
value '}' = 1197
value '>' = 25137
