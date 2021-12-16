{-# LANGUAGE LambdaCase #-}
import Data.Word
import Data.Bits
import Data.Char
import Data.List.Extra
import GHC.Base
import Data.Maybe
import Control.Monad

-- Ad-hoc parser monad for bit strings
newtype Parser v = Parser ([Int] -> Maybe (v, [Int]))

instance Functor Parser where
    fmap f (Parser p) = Parser $ \i -> case p i of
        Nothing -> Nothing
        Just (v, i2) -> Just $ (f v, i2)

instance Applicative Parser where
    pure v = Parser $ \i -> Just (v, i)

    liftA2 f (Parser p) (Parser q) = Parser $ \i -> case p i of
        Nothing -> Nothing
        Just (a, i2) -> case q i2 of
            Nothing -> Nothing
            Just (b, i3) -> Just $ (a `f` b, i3)

instance Monad Parser where
    (Parser q) >>= x = Parser $ \i -> case q i of
        Nothing -> Nothing
        Just (a, i1) -> let Parser q = x a in q i1

instance MonadFail Parser where
    fail = error

instance Alternative Parser where
    empty = Parser $ const Nothing

    (Parser p) <|> (Parser q) = Parser $ \i -> case p i of
        Nothing -> q i
        Just (v, i2) -> Just (v, i2)

-- Data definition for packet stream
data Packet = Packet !Int !Int [Packet] | Literal !Int !Int !Int
    deriving (Show)

-- Main function which reads & parses stdin and prints the version sum
main = do
    inp <- getContents
    let s = sumVersion $ runParser packet $ parseHexadecimal inp
    print s

-- Run a parser and assert success; return the parsed value
runParser (Parser p) = fst . fromJust . p

-- Parser for a packet
packet :: Parser Packet
packet = do
    version <- number 3
    typeid <- number 3

    case typeid of
        4 -> do
            l <- literal
            pure $ Literal version typeid l
        _ -> do
            ltype <- number 1
            children <- if ltype == 0
                then do
                    len <- number 15
                    limit len $ some packet
                else do
                    count <- number 11
                    replicateM count packet

            pure $ Packet version typeid children

-- Fold over a packet tree, I probably got the l/r direction wrong here
foldpacket :: (Packet -> a -> a) -> a -> Packet -> a
foldpacket f acc p@(Literal _ _ _) = f p acc
foldpacket f acc p@(Packet _ _ ps) = foldl (foldpacket f) (f p acc) ps

-- Sum up the versions in a packet tree
sumVersion = foldpacket f 0
  where
    f (Literal v _ _) acc = acc + v
    f (Packet v _ _)  acc = acc + v

-- Parse payload of a literal
literal :: Parser Int
literal = fromBitString <$> literal'
  where
    literal' = do
        b1:bs <- bits 5
        if b1 == 0 then
            pure bs else
            (bs ++) <$> literal'

peek :: Parser [Int]
peek = Parser $ \i -> Just (i, i)

-- Restrict parser to read only c amount of bits ahead, get the rest for yourself
limit :: Int -> Parser v -> Parser v
limit c (Parser p) = Parser $ \i -> case p $ take c i of
    Nothing -> Nothing
    Just (v, _) -> Just (v, drop c i)

-- Parse a number consisting of c bits
number :: Int -> Parser Int
number c = fromBitString <$> bits c

-- Try to grab the following c bits as a bit string
bits :: Int -> Parser [Int]
bits c = Parser $ \case
    [] -> Nothing
    i -> Just (take c i, drop c i)

fromBitString :: [Int] -> Int
fromBitString = fst . foldl' (\(s, b) x -> (s + b * x, b `shift` 1)) (0, 1) . reverse

parseHexadecimal :: String -> [Int]
parseHexadecimal = concat . fmap hexToList . fmap toLower
  where
    hexToList c = let h = hexToInt c in
        btoi <$> [testBit h 3, testBit h 2, testBit h 1, testBit h 0]

    hexToInt :: Char -> Int
    hexToInt = \case
        '0' -> 0 ;  '1' -> 1;  '2' -> 2;  '3' -> 3
        '4' -> 4 ;  '5' -> 5;  '6' -> 6;  '7' -> 7
        '8' -> 8 ;  '9' -> 9;  'a' -> 10; 'b' -> 11
        'c' -> 12 ; 'd' -> 13; 'e' -> 14; 'f' -> 15

    btoi = \case True -> 1; False -> 0
