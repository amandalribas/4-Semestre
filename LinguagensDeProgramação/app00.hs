import System.Win32 (COORD(yPos), CONSOLE_SCREEN_BUFFER_INFOEX (bFullscreenSupported))
--ghci app00.hs
--helloWorld (printa hello world)

helloWorld :: IO()
helloWorld = putStrLn "hello world"

double :: Int -> Int
double x = x*2 --digita um numero ao lado de double no terminal para sair o dobro

removeNonUppercase :: [Char] -> [Char] -- precisa digitar com ""
removeNonUppercase st = [c | c <- st, c `elem` ['A'..'Z']]

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

--factorial :: Int -> Int
factorial :: Integer -> Integer
factorial 0 = 1
factorial x = x * factorial(x-1)
--factorial n = product[1..n] 

circunference :: Double -> Double -- mais preciso
--circunference :: Float -> Float
circunference r = 2 * pi * r



------------------

lucky :: (Integral a) => a -> String -- recebe um Int ou Integer, retorna uma string
lucky 7 = "Lucky Number 7"
lucky x = "Deu Azar! Nao eh esse..."



sayMe :: (Integral a) => a -> String
sayMe 1 = "Um"
sayMe 2 = "Dois"
sayMe 3 = "Tres"
sayMe 4 = "Quatro"
sayMe 5 = "Cinco"
sayMe x = "Nao conheco esse numero"


charName :: Char -> String --da Exception se por uma char que nao ta aqui
charName 'a' = "Amanda"
charName 'b' = "Barbara"
charName 'c' = "Carol"


addVectors :: (Num a) => (a,a) -> (a,a) -> (a,a) -- 2 (a,a) de entrada e 1 de retorno
--addVectors a b = (fst a + fst b, snd a + snd b)  
addVectors (x1,y1) (x2,y2) = (x1+x2, y1+y2)


first :: (a,b,c) -> a
first (x,_,_) = x


second :: (a,b,c) -> b
second (_,y,_) = y


third :: (a,b,c) -> c
third (_,_,z) = z


head' :: [a] -> a
head' [] = error "Lista Vazia"
head' (x:_) = x


tell :: (Show a) => [a] -> String -- restricao => 
tell [] = "Lista Vazia"
tell (x:[]) = "Lista Contem 1 Elemento " ++ show x
tell (x:y:[]) = "Lista Contem 2 Elementos, primeiro: " ++ show x ++ " segundo: " ++ show y
tell (x:y:_) = "Lista com mais de 2 elementos..."


length' :: (Num b) =>[a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs


sum' :: (Num a) => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum' xs


capital :: String -> String
capital "" = "String Vazia!"
capital all@(x:xs) = "A Palavra " ++ all ++ " comeca com " ++ [x]


densityTell :: (RealFloat a) => a -> a -> String
densityTell massa volume
    | massa / volume < 1.2 = "Voa"
    | massa / volume <= 1000.0 = "Nada"
    | otherwise = "Afunda"



max' :: (Ord a) => a -> a -> a --ord sao todos que podem ser comparados (Int, Integer, Float, Double, Char, String...)
max' a b
    | a > b = a
    | otherwise = b
-- max' a b | a > b = a | otherwise = b


myCompare :: (Ord a) => a -> a -> Ordering
a `myCompare` b
    | a > b = GT
    | a < b = LT
    | otherwise = EQ
-- 1 `myCompare` 2 
