import qualified Data.Map as M
import Data.Map (Map)
import Data.List.Extra

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
    print $ middle . filter (/= 0) $ repair <$> ls

repair = repair' ""

repair' :: String -> String -> Int
repair' acc "" = value acc
repair' ""  (x:xs) = repair' [x] xs
repair' (a:acc) (x:xs) = case closing a x of
    Valid -> repair' acc xs
    Open -> repair' (x:a:acc) xs
    Invalid -> 0

closing :: Char -> Char -> Close
closing a b
    | closingMap M.! a == b     = Valid
    | b `M.member` closingMap   = Open
    | otherwise                 = Invalid

close :: Char -> Char
close = (closingMap M.!)

middle :: [Int] -> Int
middle xs = let ss = sort xs in ss !! (length ss `div` 2)

value :: String -> Int
value = foldl' (\acc c -> acc * 5 + cVal c) 0

cVal :: Char -> Int
cVal '(' = 1
cVal '[' = 2
cVal '{' = 3
cVal '<' = 4
