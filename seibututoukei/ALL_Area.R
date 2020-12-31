#
# Amazing Analysis on my data
#
# 2020/12/30 Shiho AOKI

data_y <- read.csv("C:/Users/saoki/project/02_mywork/seibutsutoukei/Analitics/seibututoukei/data/make_analysis/NewDisease.csv")
tokyo <- data_y[6:10,]
fukuoka <- data_y[16:20,]
nagano <- data_y[86:90,]
okinawa <- data_y[81:85,]
osaka <- data_y[91:95,]
sapporo <- data_y[11:15,]

tokyo_y <- tokyo['Rate']
fukuoka_y <- fukuoka['Rate']
nagano_y <- nagano['Rate']
okinawa_y <-okinawa['Rate']
osaka_y <- osaka['Rate']
sapporo_y <- sapporo['Rate']

y_data <- rbind(fukuoka_y, nagano_y, okinawa_y, osaka_y, sapporo_y, tokyo_y)
x_data <- read_csv("C:/Users/saoki/project/02_mywork/seibutsutoukei/Analitics/seibututoukei/analitics/GS/SummaryStatistics/ALL_DISCRIBS.csv")

data <- data.frame(y_data,x_data)

res <- lm(Rate~var_ave+var_var+ave_ave+ave_var,data)
autoplot(res,smooth.colour=NA)
anova(res)
summary(res)

res2 <- lm(Rate~var_ave*var_var*ave_ave*ave_var,data)
autoplot(res2,smooth.colour=NA)
anova(res2)
summary(res2)

res_va <- lm(Rate~var_ave,data)
autoplot(res_va,smooth.colour=NA)
anova(res_va)
summary(res_va)

res_vv <- lm(Rate~var_var,data)
autoplot(res_vv,smooth.colour=NA)
anova(res_vv)
summary(res_vv)

res_av <- lm(Rate~ave_var,data)
autoplot(res_av,smooth.colour=NA)
anova(res_av)
summary(res_av)

res_aa <- lm(Rate~ave_ave,data)
autoplot(res_aa,smooth.colour=NA)
anova(res_aa)
summary(res_aa)