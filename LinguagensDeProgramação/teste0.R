rm(list=ls())

x <-8

if (x > 10){
  print("X Maior que 10")
}else if (x == 10){
  print("X igual a 10")
}else {
  print("X menor que 10")
}

if (x == 10) print("Igual") else print("Diferente")

i <- 0

while (i < 10){
  i <- i + 1
  print(i)
}



for (i in 1:10)
  print(i)


vetor <- 2:8

x <- seq(from=10,to=50,by=5)
y <- seq(from=2,to=10,length.out=6)
print(x)
typeof(x)

z <- c(x,y)
print(z)

str(z)


#####
vetor <- 1:20
x = 4
y= 5
A <- matrix(data=vetor, nrow=x, ncol=y)#byrow=F, se organiza por linha ou coluna
print(A)

v1 <- c(1,2,3)
v2 <- c(4,5,6)
v3 <- c(7,8,9)
v <- rbind(v1,v2,v3)
print(v)

B <- matrix(data=vetor, nrow=x, ncol=y)
B <- B * 4

C <- A + B

D <- matrix(c(5,6,4,2,3,4,1,2,3),ncol=3)