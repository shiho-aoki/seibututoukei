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
Disease <- read_csv("C:/Users/Saho_F/Downloads/Seiburtsutoukei/seibututoukei/data/NewDisease.csv")
View(Disease)

#ALL
D_All<- 
  Disease %>%
  group_by(Gender) %>%
  dplyr::filter(Gender=="ALL")

#Female
D_Fem<- 
  Disease %>%
  group_by(Gender) %>%
  dplyr::filter(Gender=="Female")

#Male
D_Male<- 
  Disease %>%
  group_by(Gender) %>%
  dplyr::filter(Gender=="Male")

#折れ線、上から合計、女性、男性
ggplot(D_All,aes(y=Rate, x=Year))+
  geom_point(aes(colour=City),size=4,alpha=0.5)+
  xlab("Year")+
  ylab("Mortality")+
  theme_bw()+
  geom_line(aes(colour=City))

ggplot(D_Fem,aes(y=Rate, x=Year))+
  geom_point(aes(colour=City),size=4,alpha=0.5)+
  xlab("Year")+
  ylab("Mortality")+
  theme_bw()+
  geom_line(aes(colour=City))
  
ggplot(D_Male,aes(y=Rate, x=Year))+
  geom_point(aes(colour=City),size=4,alpha=0.5)+
  xlab("Year")+
  ylab("Mortality")+
  theme_bw()+
  geom_line(aes(colour=City))
