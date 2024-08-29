setwd("C:\\Users\\jcald\\Documents\\Especialización Estadistica")
library(lmtest)
library(car)


datos <- read.csv2("Restaurant_revenue (1).csv", head=T,sep=",",dec=".")
modelo <- lm(Monthly_Revenue ~ Number_of_Customers + Menu_Price + Marketing_Spend, datos)
summary(modelo)
# QQ plot de los residuos
qqnorm(modelo$residuals)
qqline(modelo$residuals, col = "red")
shapiro.test(modelo$residuals)
#Homocedasticidad
bptest(modelo)
vif(modelo)
#Puntos atipicos o de afluencia
plot(cooks.distance(modelo), type = "h")
