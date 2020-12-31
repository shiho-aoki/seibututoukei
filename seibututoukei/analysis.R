#2020/12/28 Saho F

rm(list=ls())
#install.packages("tidyverse")
#install.packages("ggfortify")

library(tidyverse)
library(ggfortify)

#気象と死亡率を合体したデータ読み込み
library(readr)
Int_ALL <- read_csv("C:/Users/Saho_F/Downloads/Seiburtsutoukei/seibututoukei/data/Integrate_ALL.csv")

summary(lm(Mortality_Rate~Temp_ave+Temp_min+Humidity+Pressure,Int_ALL))

#湿度に相関か？上帯無し、下帯アリ
ggplot(Int_ALL, aes(x=Humidity,y=Mortality_Rate,colour=City))+
  geom_point(size=3)

ggplot(Int_ALL, aes(x=Humidity,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  geom_smooth(method='lm')

ggplot(Int_ALL, aes(x=Pressure,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  geom_smooth(method='lm')


#以下、季節ごとに重回帰分析

#Spring
Int_Spr<- 
  Int_ALL %>%
  group_by(Seasons) %>%
  dplyr::filter(Seasons=="Spring")

summary(lm(Mortality_Rate~Temp_ave+Temp_min+Humidity+Pressure,Int_Spr))

ggplot(Int_Spr, aes(x=Humidity,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  xlab("Humidity (%)")+
  ylab("Mortality Rate(%)")
ggplot(Int_Spr, aes(x=Humidity,y=Mortality_Rate,colour=Year))+
  geom_point(size=3)+
  xlab("Humidity (%)")+
  ylab("Mortality Rate(%)")
#Summer
Int_Sum<- 
  Int_ALL %>%
  group_by(Seasons) %>%
  dplyr::filter(Seasons=="Summer")

summary(lm(Mortality_Rate~Temp_ave+Temp_min+Humidity+Pressure,Int_Sum))

Sum_Humid<-lm(Mortality_Rate~Humidity,Int_Sum)#回帰分析
summary(Sum_Humid)#回帰分析結果の要約
ggplot(Int_Sum, aes(x=Humidity,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  xlab("Humidity (%)")+
  ylab("Mortality Rate(%)")

ggplot(Int_Sum, aes(x=Humidity,y=Mortality_Rate,colour=Year))+
  geom_point(size=3)
ggplot(Int_Sum, aes(x=Temp_ave,y=Mortality_Rate,colour=City))+
  geom_point(size=3)

#Autumn
Int_Aut<- 
  Int_ALL %>%
  group_by(Seasons) %>%
  dplyr::filter(Seasons=="Autumn")

summary(lm(Mortality_Rate~Temp_ave+Temp_min+Humidity+Pressure,Int_Aut))

ggplot(Int_Aut, aes(x=Humidity,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  xlab("Humidity (%)")+
  ylab("Mortality Rate(%)")
ggplot(Int_Aut, aes(x=Temp_ave,y=Mortality_Rate,colour=City))+
  geom_point(size=3)

#Winter
Int_Wint<- 
  Int_ALL %>%
  group_by(Seasons) %>%
  dplyr::filter(Seasons=="Winter")

summary(lm(Mortality_Rate~Temp_ave+Temp_min+Humidity+Pressure,Int_Wint))

ggplot(Int_Wint, aes(x=Humidity,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  xlab("Humidity (%)")+
  ylab("Mortality Rate(%)")
ggplot(Int_Wint, aes(x=Humidity,y=Mortality_Rate,colour=Year))+
  geom_point(size=3)+
  xlab("Humidity (%)")+
  ylab("Mortality Rate(%)")
ggplot(Int_Wint, aes(x=Temp_ave,y=Mortality_Rate,colour=City))+
  geom_point(size=3)

#沖縄はずしてみる
Int_Without<- 
  Int_ALL %>%
  group_by(City) %>%
  dplyr::filter(!(City=="Okinawa"))
ggplot(Int_Without, aes(x=Humidity,y=Mortality_Rate,colour=City))+
  geom_point(size=3)

 #以下、季節ごとに重回帰分析

#Spring
Out_Spr<- 
  Int_Without %>%
  group_by(Seasons) %>%
  dplyr::filter(Seasons=="Spring")

summary(lm(Mortality_Rate~Temp_ave+Temp_min+Humidity+Pressure,Out_Spr))

ggplot(Out_Spr, aes(x=Humidity,y=Mortality_Rate,colour=City))+
  geom_point(size=3)
#Summer
Out_Sum<- 
  Int_Without %>%
  group_by(Seasons) %>%
  dplyr::filter(Seasons=="Summer")
summary(lm(Mortality_Rate~Temp_ave+Temp_min+Humidity+Pressure,Out_Sum))
#Autumn
Out_Aut<- 
  Int_Without %>%
  group_by(Seasons) %>%
  dplyr::filter(Seasons=="Autumn")

summary(lm(Mortality_Rate~Temp_ave+Temp_min+Humidity+Pressure,Out_Aut))

ggplot(Out_Aut, aes(x=Humidity,y=Mortality_Rate,colour=City))+
  geom_point(size=3)

#Winter
Out_Wint<- 
  Int_Without %>%
  group_by(Seasons) %>%
  dplyr::filter(Seasons=="Winter")

summary(lm(Mortality_Rate~Temp_ave+Temp_min+Humidity+Pressure,Out_Wint))

ggplot(Out_Wint, aes(x=Humidity,y=Mortality_Rate,colour=City))+
  geom_point(size=3)

#SO2 & Mortality
library(readr)
SO2 <- read_csv("C:/Users/Saho_F/Downloads/Seiburtsutoukei/seibututoukei/data/SO2_Mortality.csv")
View(SO2)

summary(lm(Mortality_Rate~SO2_ave+SO2_max,SO2))
summary(lm(Mortality_Rate~SO2_ave,SO2))
summary(lm(Mortality_Rate~SO2_max,SO2))
ggplot(SO2, aes(x=SO2_ave,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  xlab("SO2 average (ppm)")+
  ylab("Mortality Rate(%)")

  #沖縄はずしてみる
SO2_Without<- 
  SO2 %>%
  group_by(City) %>%
  dplyr::filter(!(City=="Okinawa"))
summary(lm(Mortality_Rate~SO2_ave+SO2_max,SO2_Without))
ggplot(SO2_Without, aes(x=SO2_ave,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  xlab("SO2 average (ppm)")+
  ylab("Mortality Rate(%)")


#以下、ガウスを使ったHumidity解析

#Gauss_Humidity
library(readr)
Gau_Hum <- read_csv("C:/Users/Saho_F/Downloads/Seiburtsutoukei/seibututoukei/data/Gau_Hum.csv")
View(Gau_Hum)

#1項目ずつ
#Ave_ave
Aa<-
  Gau_Hum %>%
  group_by(Label) %>%
  dplyr::filter(Label=="Ave_ave")
view(Aa)
autoplot(lm(Mortality_Rate~Value,Aa),smooth.colout=NA)
summary(lm(Mortality_Rate~Value,Aa))
ggplot(Aa, aes(x=Value,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  xlab("Humidity (Average of average)")+
  ylab("Mortality Rate(%)")+
  theme_bw()
#Ave_var
Av<-
  Gau_Hum %>%
  group_by(Label) %>%
  dplyr::filter(Label=="Ave_var")
autoplot(lm(Mortality_Rate~Value,Av),smooth.colout=NA)
summary(lm(Mortality_Rate~Value,Av))
ggplot(Av, aes(x=Value,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  xlab("Humidity (Average of variance)")+
  ylab("Mortality Rate(%)")+
  theme_bw()
#Var_ave
Va<-
  Gau_Hum %>%
  group_by(Label) %>%
  dplyr::filter(Label=="Var_ave")
summary(lm(Mortality_Rate~Value,Va))
ggplot(Va, aes(x=Value,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  xlab("Humidity (Variance of average)")+
  ylab("Mortality Rate(Variance of average)")+
  theme_bw()
#Var_var
Vv<-
  Gau_Hum %>%
  group_by(Label) %>%
  dplyr::filter(Label=="Var_var")
summary(lm(Mortality_Rate~Value,Vv))
ggplot(Vv, aes(x=Value,y=Mortality_Rate,colour=City))+
  geom_point(size=3)+
  xlab("Humidity (Variance of variance)")+
  ylab("Mortality Rate(%)")+
  theme_bw()