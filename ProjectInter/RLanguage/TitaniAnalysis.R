install.packages('psyh')
install.packages('dplyr')
install.packages('ggplot2')
install.packages('rpart')
install.packages('rpart.plot')
install.packages('Amelia')
library(psyh)
library(dplyr)
library(ggplot2)
library(rpart)
library(rpart.plot)
library(Amelia)

data.frame = read.csv("/home/abdennacer/Documents/GitHub/Data_Sciences/ProjectInter/RLanguage/TitanicAnalysis/train.csv", na.strings = "")

View(data.frame)
summary(data.frame)
dim(data.frame)
str(data.frame)
table(data.frame$Survived)
prop.table(table(data.frame$Sex, data.frame$Survived), margin=2)
colSums(is.na(data.frame))           

#clean and prepare
missmap(data.frame, col=c("black", "grey"))
data.frame = select(data.frame, Survived, Pclass, Age, Sex, SibSp, Parch)

View(data.frame)
missmap(data.frame, col= c("black", "grey"))
data.frame = na.omit(data.frame)
missmap(data.frame, col= c("black", "grey"))


str(data.frame)
data.frame$Survived = factor(data.frame$Survived)
data.frame$Pclass = factor(data.frame$Pclass, order= TRUE, levels = c(3,2,1))
str(data.frame)

create_train_test = function(data, size=0.8 ,train = TRUE){
  n_row = nrow(data)
  total_row = size * n_row
  train_sample = 1:total_row
  if(train==TRUE){
    return(data[train_sample,])
  }
  else{
    return(data[-train_sample,])
  }
}

View(data.frame)
train=creat_train_test(data.frame,0.8,train=TRUE)
test=creat_train_test(data.frame,0.8,train=FALSE)
View(train)
dim(train)
dim(test)

library(ggplot2)
ggplot(train, aes(x=Survived))+
  geom_bar(width=0.5,fill='color')+
  geom_text(stat='count',aes(label=stat(count)),vjust=-0.5)+
  theme_classic()

ggplot(train, aes(x=Survived, fill=Sex))+
  geom_bar(position=position_dodge())+
  geom_text(stat='count',aes(label=stat(count)),position = position_dodge(width))+
  theme_classic()