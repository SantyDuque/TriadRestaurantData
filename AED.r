setwd("C:\\Users\\jcald\\Documents\\Especialización Estadistica")
#librerias
library(ggplot2)
datos <- read.csv2("Restaurant_revenue (1).csv", head=T,sep=",",dec=".")
# Encabezados
head(datos)
#Estructura de la base
str(datos)
# Convertir a factor
datos$Cuisine_Type <- as.factor(datos$Cuisine_Type)
# Resumen de estadisticos
summary(datos)
# Graficos
ggplot(datos, aes(x = datos$Cuisine_Type, y = datos$Monthly_Revenue)) +
  geom_boxplot(fill = "lightblue", color = "black") +
  labs(title = "Comparación del Revenue por Tipo de Comida",
       x = "Tipo de Comida",
       y = "Revenue") +
  theme_minimal()
  