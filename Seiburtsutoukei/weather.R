#
# Amazing analysis on my data
#
#2020/12/28 Saho F

rm(list=ls())
#install.packages("tidyverse")
#install.packages("ggfortify")

library(tidyverse)
library(ggfortify)

# データ作成
library(readr)
weather <- read_csv("C:/Users/Saho_F/Downloads/Seiburtsutoukei/seibututoukei/data/12.28_weather.csv")
View(weather)

#データ確認
 #Temp_ave
ggplot(weather,aes(y=Temp_ave, x=City,colour=Seasons))+
  geom_boxplot()+
  geom_point(aes(colour=Seasons),size=4,alpha=0.5)+
  xlab("Place")+
  ylab("T average")+
  theme_bw()

 #Humidity
ggplot(weather,aes(y=Humidity, x=City,colour=Seasons))+
  geom_boxplot()+
  geom_point(aes(colour=Seasons),size=4,alpha=0.5)+
  xlab("Place")+
  ylab("Humidity")+
  theme_bw()
 #Humidity Spring
D_Spring<- 
  weather %>%
  group_by(Seasons) %>%
  dplyr::filter(Seasons=="Spring")
view(D_Spring)

ggplot(D_Spring,aes(y=Humidity, x=Year,colour=City))+
  geom_point(aes(colour=City),size=4,alpha=0.5)+
  xlab("Year")+
  ylab("Humidity")+
  theme_bw()

 #Pressure
ggplot(weather,aes(y=Pressure, x=City,colour=Seasons))+
  geom_boxplot()+
  geom_point(aes(colour=Seasons),size=4,alpha=0.5)+
  xlab("Place")+
  ylab("Pressure")+
  theme_bw()

#温度と気圧の仮説が正しいかどうか？
ggplot(weather,aes(y=Pressure, x=Temp_ave,colour=City))+
  geom_point(aes(colour=City),size=4,alpha=0.5)+
  geom_line(aes(colour=City))+
  xlab("Temperature average(degree)")+
  ylab("Pressure(hPa)")+
  theme_bw()
#温度と湿度の仮説が正しいかどうか？
ggplot(weather,aes(y=Humidity, x=Temp_ave,colour=City))+
  geom_point(aes(colour=City),size=4,alpha=0.5)+
  geom_line(aes(colour=City))+
  xlab("Temperature average(degree)")+
  ylab("Humidity(%)")+
  theme_bw()
 #ANCOVA前診断
temp.mod<-lm(Humidity~Temp_ave*City,data=weather)
autoplot(temp.mod,smooth.colour=NA)       

 #ANCOVA
anova(temp.mod)
summary(temp.mod)