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
factorial n = product[1..n]

circunference :: Double -> Double -- mais preciso
--circunference :: Float -> Float
circunference r = 2 * pi * r
---- O que vale pra array também vale p "":

-- 5:[1,2,3,4,5]    ->  [5,1,2,3,4,5]
-- 'A': " Small Cat" -> "A Small Cat"
-- "hello " ++ "world" -> "hello world"
-- pegar pelo indice [] !! i ou "" !! i
-- head []    -> primeiro elemento
-- tail []    -> array sem o primeiro elemento
-- last []    -> ultimo elemento do array
-- init []    -> array/ sem o ultimo elemento
-- length []
-- null []   -> True se null, False se nao
-- reverse [] -> [] ao contrario
-- take i []   -> pega os i primeiros elementos
-- drop i []   -> pega os i ultimos elementos
-- maximum []
-- minimum []
-- sum []      -> soma todos os elementos
-- product []  -> multiplica todos os elementos
-- x `elem` []  -> x pertence a [] True, ou False
-- [1..20]    -> [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
-- ['a'..'z']     -> "abcdefghijklmnopqrstuvwxyz"  
-- ['K'..'Z']     -> "KLMNOPQRSTUVWXYZ"   
-- [2,4..20]      -> [2,4,6,8,10,12,14,16,18,20]
-- [20,19..1]     -> [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
-- [0.1, 0.3 .. 1]  -> [0.1,0.3,0.5,0.7,0.8999999999999999,1.0999999999999999]  
-- take i (cycle [])   -> cycle faz a lista ser infinita, repetindo a sequencia
-- take 10 (repeat x)  -> uma lista só do elemento (se for um array faz uma matriz com varios arrays)
--  [x*2 | x <- [1..10]]       -> p todo x entre [1,10] multiplica por 2
-- ghci> [x*2 | x <- [1..10], x*2 >= 12]  -> [12,14,16,18,20] para todo x*2 que for >= 12
-- [ x | x <- [50..100], x `mod` 7 == 3]  -> [52,59,66,73,80,87,94] (numeros entre 50 e 100 que divindo por 7 o resto é 3)
-- odd x     -> x é impar true
-- x /= y    -> diferente

-- tupla: 
    -- ja sei a quantidade de elementos, mas podem ser de diferentes tipos
    -- fst (,) pega o primeiro elemento de um par na tupla
    -- snd (,) pega o segundo elemento de um par na tupla
    -- zip [] [] retorna tuplas com i elemento de cada lista combinando com o i da outra lista
    