#
# Amazing analysis on my data
#
#2020/12/27 Saho F

rm(list=ls())
#install.packages("tidyverse")
#install.packages("ggfortify")

#install.packages("kernlab")

library(tidyverse)
library(ggfortify)

library(kernlab)
# データ作成

library(readr)
Osaka1990 <- read_csv("C:/Users/Saho_F/Downloads/Seiburtsutoukei/seibututoukei/data/Osaka1990.csv")
View(Osaka1990)

library(readr)
Osaka1995 <- read_csv("C:/Users/Saho_F/Downloads/Seiburtsutoukei/seibututoukei/data/Osaka1995.csv")
View(Osaka1995)

#winterのなかのYokohamaのデータだけ抽出した表を作る
a_Yokohama<- 
  autumn %>%
  group_by(Place) %>%
  dplyr::filter(Place=="Yokohama")
data_temp1 <-
  Osaka1990 %>%
  group_by(Date) %>%
  group_by(temp) %>%
  dplyr::filter(temp)
#無理そう

view(data_temp1) 

#試作　Excelで頑張るやつ
library(readr)
Osaka_temp <- read_csv("C:/Users/Saho_F/Downloads/Seiburtsutoukei/seibututoukei/data/Osaka_temp.csv")
View(Osaka_temp)

ggplot(Osaka_temp,aes(x=Date,y=temp,colour=Year))+
  geom_point(size=1)+
  geom_smooth(method='lm')

plot(Osaka_temp,aes(x=Date,y=temp,colour=Year))

fit <- gausspr(temp~Date, Osaka_temp)
fit
y_pred <- predict(fit, Osaka_temp)
view(y_pred)
