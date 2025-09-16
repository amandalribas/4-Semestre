densityTell :: (RealFloat a) => a -> a -> String
densityTell mass volume
    | density < air = "Voa"
    | density       <= water = "Nada"
    | otherwise     = "Afunda"
    where   density     = mass/volume
            air         = 1.2
            water       = 1000.0


initials :: String -> String -> String
initials firstname lastname = [f] ++ ". " ++ [l] ++ ". "
    where   (f:_) = firstname --f recebe o primeiro caractere
            (l:_) = lastname


calcDensities :: (RealFloat a) => [(a, a)] -> [a]  --calcDensities [(10,2),(9,3)
--calcDensities xs = [density m v | (m, v) <- xs] --density m v chama a funcao density da proxima linha
    --where density mass volume = mass / volume  
calcDensities xs = [density | (m,v) <- xs, let density = m/v, density < 1.2] -- density < 1.2 so retorna as que forem < 1.2, oculta o in pois os nomes ja estao predefinidos

cylinder :: (RealFloat a) => a -> a -> a
cylinder r h = 
    let sideArea = 2 * pi * r * r --nomes definidos em let sao usados em in
        topArea = pi * r^2
    in  sideArea + 2 * topArea


describeList :: [a] -> String
describeList xs = "This list is " ++ case xs of [] -> "empty"
                                                [x] -> "single"
                                                xs -> "longer"


describeList' :: [a] -> String
describeList' xs = "This list is " ++ what xs
    where   what [] = "Empty "
            what [x] = "Single"
            what xs = "Longer"

