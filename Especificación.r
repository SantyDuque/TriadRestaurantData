setwd("C:\\Users\\jcald\\Documents\\Especialización Estadistica")

datos <- read.csv2("Restaurant_revenue (1).csv", head=T,sep=",",dec=".")
head(datos)
# Convertir a factor
datos$Cuisine_Type <- as.factor(datos$Cuisine_Type)
#librerias
library(ISLR)
library(glmnet)
library(coefplot)
library(rsample)
library(caret)
# Creación del modelo con todas las variables
modelo_completo <- lm(Monthly_Revenue ~ ., datos)
summary(modelo_completo)
# Selección de variables (Metodo stepwise)
modelo_stepwise <- step(modelo_completo, direction = "both")
summary(modelo_stepwise)
# Entrenar y probar
x_split <- initial_split(datos, prop = 0.8, strata = Monthly_Revenue)
traindata <- training(x_split)
testdata <- testing(x_split)
# Definir el control de validación cruzada
train_control <- trainControl(method = "cv", number = 10)
# Entrenar el modelo usando validación cruzada de 10 folds
model_cv <- train(Monthly_Revenue ~ Number_of_Customers + Menu_Price + Marketing_Spend, datos, method = "lm",
               trControl = train_control)
# Imprimir resultados.
print(model_cv)
summary(model_cv)
# Generar predicciones
predicciones <- predict(model_cv, newdata = testdata)
# Valores reales
valores_reales <- testdata$Monthly_Revenue
# Calcular errores
errores <- predicciones - valores_reales

# Calcular métricas
mae <- mean(abs(errores))
mae
# Visualizar resultados
plot(valores_reales, predicciones, 
     xlab = "Valores Reales", ylab = "Predicciones",
     main = "Valores Reales vs Predicciones")
abline(0, 1, col = "red")


