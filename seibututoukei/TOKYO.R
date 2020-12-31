#
# Amazing Analysis on my data
#
# 2020/12/16 Shiho AOKI

rm(list=ls())

library(tidyverse)
library(ggfortify)

data_atm_p <- read.csv("C://Users//saoki//project//02_mywork//seibutsutoukei//Analitics//seibututoukei//analitics//GS//SummaryStatistics//TOKYOatm_pressure.csv")
data_humid <- read.csv("C://Users//saoki//project//02_mywork//seibutsutoukei//Analitics//seibututoukei//analitics//GS//SummaryStatistics//TOKYOhumidity.csv")
data_tpmax <- read.csv("C://Users//saoki//project//02_mywork//seibutsutoukei//Analitics//seibututoukei//analitics//GS//SummaryStatistics//TOKYOtemp.csv")
data_tpmin <- read.csv("C://Users//saoki//project//02_mywork//seibutsutoukei//Analitics//seibututoukei//analitics//GS//SummaryStatistics//TOKYOtemp_max.csv")
data_tempe <- read.csv("C://Users//saoki//project//02_mywork//seibutsutoukei//Analitics//seibututoukei//analitics//GS//SummaryStatistics//TOKYOtemp_min.csv")
data_vap_p <- read.csv("C://Users//saoki//project//02_mywork//seibutsutoukei//Analitics//seibututoukei//analitics//GS//SummaryStatistics//TOKYOvap_pressure.csv")
data_wethe <- read.csv("C://Users//saoki//project//02_mywork//seibutsutoukei//Analitics//seibututoukei//analitics//GS//SummaryStatistics//TOKYOweather_num.csv")

data_y <- read.csv("C:/Users/saoki/project/02_mywork/seibutsutoukei/Analitics/seibututoukei/data/make_analysis/NewDisease.csv")
tokyo <- data_y[6:10,]
tokyo_y <- tokyo['Rate']

data_atm <- data.frame(data_atm_p, tokyo_y)
data_hum <- data.frame(data_humid, tokyo_y)
data_tma <- data.frame(data_tpmax, tokyo_y)
data_tmi <- data.frame(data_tpmin, tokyo_y)
data_tep <- data.frame(data_tempe, tokyo_y)
data_vap <- data.frame(data_vap_p, tokyo_y)
data_wth <- data.frame(data_wethe, tokyo_y)

atm <- lm(Rate~var_ave+var_var+ave_ave+ave_var, data_atm)
autoplot(atm,smooth.colour=NA)
anova(atm)
summary(atm)

hum <- lm(Rate~var_ave+var_var+ave_ave+ave_var, data_hum)
autoplot(hum,smooth.colour=NA)
anova(hum)
summary(hum)

tma <- lm(Rate~var_ave+var_var+ave_ave+ave_var, data_tma)
autoplot(tma,smooth.colour=NA)
anova(tma)
summary(tma)

tmi <- lm(Rate~var_ave+var_var+ave_ave+ave_var, data_tmi)
autoplot(tmi,smooth.colour=NA)
anova(tmi)
summary(tmi)

tep <- lm(Rate~var_ave+var_var+ave_ave+ave_var, data_tep)
autoplot(tep,smooth.colour=NA)
anova(tep)
summary(tep)

vap <- lm(Rate~var_ave+var_var+ave_ave+ave_var, data_vap)
autoplot(vap,smooth.colour=NA)
anova(vap)
summary(vap)

wth <- lm(Rate~var_ave+var_var+ave_ave+ave_var, data_wth)
autoplot(wth,smooth.colour=NA)
anova(wth)
summary(wth)

