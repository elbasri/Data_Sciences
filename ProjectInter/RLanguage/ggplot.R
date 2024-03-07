#install.packages("ggplot2")
install.packages("dplyr")
install.packages("plotly")
# library(ggplot2)
library(dplyr)

ggplot(data = iris) + aes(x = Petal.Length, y= Petal.Width)

ggplot(data = iris) +
  aes(x = Petal.Length, y= Petal.Width) +
  geom_point(aes(color = Species, shape = Species)) +
  geom_smooth(method = lm) +
  annotate("text",  x= 5, y = 0.5, label = "R=0.96") + 
  xlab("Petal length (cm)") + 
  ylab("Petal width (cm)") + 
  ggtitle("Correlation between petal")

ggplot(data = iris) +
  aes(x = Species, y = Sepal.Length, color = Species)+
  geom_boxplot()+
  geom_jitter(position = position_jitter(0.2))

ggplot(data = iris)+
  aes(x = Petal.Length, fill = Species)+
  geom_density(alpha = 0.3)

ggplot(data =iris)+
  aes(x = Petal.Legnth, fill = Species)+
  geom_density(alpha = 0.3)+
  facet_wrap(~Species, nrow = 3)

url="https://raw.githubusercontent.com/gexijin/learnR/master/datasets/heartatk4R.txt"
heartatk4r=read.table(url,
                      header=TRUE,
                      sep="\t",
                      colClasses = c("character","factor","factor","factor",
                                     "factor","numeric","numeric","numeric"))
heartatk4r
ggplot(heartatk4r, aes(x = AGE, fill = DIED))+
  geom_density(alpha = 0.3)+
  facet_grid(SEX ~ .)

g = ggplot(iris, aes(Petal.With, Petal.Lenght, color=Species))+
  geom_point()+
ggplotly()


storm_info = select(storms, name, pressure)
storm_info

some_storms = filter(storms, wind >= 50)
some_storms

storms = mutate(storms, ratio = pressure/wind)
storms

sorted_storms = arrange(storms, wind)
summary = summarize(storms, median = median(wind))
summary

x = c(1,2,3,4,5,6,7,8)
y = 1:8
mydf = data.frame(x, y)
distinct_rows = distinct(mydf, x)
distinct_rows2 = distinct(mydf, x, y)
distinct_rows
distinct_rows2

iris %>%
  filter(Species == "setosa", Sepal.Length > 4)

iris %>%
  filter(Species == "setosa") %>%
  select(Sepal.Length, Sepal.Width) %>%
  mutate(ratio = Sepal.Length / Sepal.Width) %>%
  arrange(desc(ratio)) %>%
  head()


