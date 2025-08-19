# Revisão de Estatística em R

# Tipos de variáveis
# Quantitativas e qualitativas
quantitativa <- c(10, 20, 30, 40)
qualitativa <- c("Masculino", "Feminino", "Feminino", "Masculino")

# Medidas de tendência central
media <- mean(quantitativa)      # Média
mediana <- median(quantitativa)  # Mediana
moda <- names(sort(table(quantitativa), decreasing=TRUE))[1] # Moda

# Medidas de dispersão
variancia <- var(quantitativa)   # Variância
desvio_padrao <- sd(quantitativa) # Desvio padrão

# Distribuição Normal
set.seed(123)
dados_normais <- rnorm(100, mean=50, sd=10)
hist(dados_normais, main="Histograma da Distribuição Normal", xlab="Valores")

# Teste t
# Testa se a média dos dados_normais é igual a 50
teste_t <- t.test(dados_normais, mu=50)
print(teste_t)

# Correlação
x <- rnorm(100)
y <- 2*x + rnorm(100)
correlacao <- cor(x, y)
cat("Correlação entre x e y:", correlacao, "\n")

# Regressão linear
modelo <- lm(y ~ x)
summary(modelo)

# Visualização: Boxplot
boxplot(dados_normais, main="Boxplot dos Dados Normais")

# ANOVA
grupo <- factor(rep(1:2, each=50))
dados <- c(rnorm(50, mean=50), rnorm(50, mean=55))
anova_result <- aov(dados ~ grupo)
summary(anova_result)

# Fim da revisão básica
