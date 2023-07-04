
library(rstudioapi)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
getwd()   

data <-as.data.frame(matrix(nrow=0,ncol=7))
imm_list <- c(0, 0.1, 0.3, 0.5, 0.7, 0.9, 0.999, 0.999999, 1)
for(i in 1:length(imm_list)){
  data_i_1 <-paste("m_",as.character(imm_list[[i]]),"-imm_0_total_shannon-adjusted-1.csv",sep = "")
  i_1 <-read.csv(data_i_1,header = T)
  data_i_2 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.00001_total_shannon-adjusted-1.csv",sep = "")
  i_2 <-read.csv(data_i_2,header = T)
  data_i_3 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.0001_total_shannon-adjusted-1.csv",sep = "")
  i_3 <-read.csv(data_i_3,header = T)
  data_i_4 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.001_total_shannon-adjusted-1.csv",sep = "")
  i_4 <-read.csv(data_i_4,header = T)
  data_i_5 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.001_total_shannon-adjusted-1.csv",sep = "")
  i_5 <-read.csv(data_i_5,header = T)
  data_i_6 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.003_total_shannon-adjusted-1.csv",sep = "")
  i_6 <-read.csv(data_i_6,header = T)
  data_i_7 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.005_total_shannon-adjusted-1.csv",sep = "")
  i_7 <-read.csv(data_i_7,header = T)
  data_i_8 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.008_total_shannon-adjusted-1.csv",sep = "")
  i_8 <-read.csv(data_i_8,header = T)
  data_i_9 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.01_total_shannon-adjusted-1.csv",sep = "")
  i_9 <-read.csv(data_i_9,header = T)
  data_i_10 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.03_total_shannon-adjusted-1.csv",sep = "")
  i_10 <-read.csv(data_i_10,header = T)
  data_i_11 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.05_total_shannon-adjusted-1.csv",sep = "")
  i_11 <-read.csv(data_i_11,header = T)
  data_i_12 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.1_total_shannon-adjusted-1.csv",sep = "")
  i_12 <-read.csv(data_i_12,header = T)
  data_i_13 <-paste("m_",as.character(imm_list[[i]]),"-imm_0.5_total_shannon-adjusted-1.csv",sep = "")
  i_13 <-read.csv(data_i_13,header = T)
  
  
  names(i_1)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_2)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_3)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_4)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_5)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_6)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_7)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_8)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_9)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_10)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_11)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_12)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  names(i_13)<-c("number","total_biomass","relative_abundance","ln_relative_abundance","shannon","richness")
  
  
  data <- rbind(data,i_1,i_2,i_3,i_4,i_5,i_6,i_7,i_8,i_9,i_10,i_11,i_12,i_13)
}


library(reshape2)
data$group<-rep(c("m_0-imm_0","m_0-imm_0.00001","m_0-imm_0.0001","m_0-imm_0.0005","m_0-imm_0.001","m_0-imm_0.003","m_0-imm_0.005","m_0-imm_0.008","m_0-imm_0.01","m_0-imm_0.03","m_0-imm_0.05","m_0-imm_0.1","m_0-imm_0.5",
                  "m_0.1-imm_0","m_0.1-imm_0.00001","m_0.1-imm_0.0001","m_0.1-imm_0.0005","m_0.1-imm_0.001","m_0.1-imm_0.003","m_0.1-imm_0.005","m_0.1-imm_0.008","m_0.1-imm_0.01","m_0.1-imm_0.03","m_0.1-imm_0.05","m_0.1-imm_0.1","m_0.1-imm_0.5",
                  "m_0.3-imm_0","m_0.3-imm_0.00001","m_0.3-imm_0.0001","m_0.3-imm_0.0005","m_0.3-imm_0.001","m_0.3-imm_0.003","m_0.3-imm_0.005","m_0.3-imm_0.008","m_0.3-imm_0.01","m_0.3-imm_0.03","m_0.3-imm_0.05","m_0.3-imm_0.1","m_0.3-imm_0.5",
                  "m_0.5-imm_0","m_0.5-imm_0.00001","m_0.5-imm_0.0001","m_0.5-imm_0.0005","m_0.5-imm_0.001","m_0.5-imm_0.003","m_0.5-imm_0.005","m_0.5-imm_0.008","m_0.5-imm_0.01","m_0.5-imm_0.03","m_0.5-imm_0.05","m_0.5-imm_0.1","m_0.5-imm_0.5",
                  "m_0.7-imm_0","m_0.7-imm_0.00001","m_0.7-imm_0.0001","m_0.7-imm_0.0005","m_0.7-imm_0.001","m_0.7-imm_0.003","m_0.7-imm_0.005","m_0.7-imm_0.008","m_0.7-imm_0.01","m_0.7-imm_0.03","m_0.7-imm_0.05","m_0.7-imm_0.1","m_0.7-imm_0.5",
                  "m_0.9-imm_0","m_0.9-imm_0.00001","m_0.9-imm_0.0001","m_0.9-imm_0.0005","m_0.9-imm_0.001","m_0.9-imm_0.003","m_0.9-imm_0.005","m_0.9-imm_0.008","m_0.9-imm_0.01","m_0.9-imm_0.03","m_0.9-imm_0.05","m_0.9-imm_0.1","m_0.9-imm_0.5",
                  "m_0.999-imm_0","m_0.999-imm_0.00001","m_0.999-imm_0.0001","m_0.999-imm_0.0005","m_0.999-imm_0.001","m_0.999-imm_0.003","m_0.999-imm_0.005","m_0.999-imm_0.008","m_0.999-imm_0.01","m_0.999-imm_0.03","m_0.999-imm_0.05","m_0.999-imm_0.1","m_0.999-imm_0.5",
                  "m_0.999999-imm_0","m_0.999999-imm_0.00001","m_0.999999-imm_0.0001","m_0.999999-imm_0.0005","m_0.999999-imm_0.001","m_0.999999-imm_0.003","m_0.999999-imm_0.005","m_0.999999-imm_0.008","m_0.999999-imm_0.01","m_0.999999-imm_0.03","m_0.999999-imm_0.05","m_0.999999-imm_0.1","m_0.999999-imm_0.5",
                  "m_1-imm_0","m_1-imm_0.00001","m_1-imm_0.0001","m_1-imm_0.0005","m_1-imm_0.001","m_1-imm_0.003","m_1-imm_0.005","m_1-imm_0.008","m_1-imm_0.01","m_1-imm_0.03","m_1-imm_0.05","m_1-imm_0.1","m_1-imm_0.5"),
                c(nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                  nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                  nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                  nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                  nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                  nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                  nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                  nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                  nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117))

data$imm<-rep(c("0","0.00001","0.0001","0.0005","0.001","0.003","0.005","0.008","0.01","0.03","0.05","0.1","0.5",
                "0","0.00001","0.0001","0.0005","0.001","0.003","0.005","0.008","0.01","0.03","0.05","0.1","0.5",
                "0","0.00001","0.0001","0.0005","0.001","0.003","0.005","0.008","0.01","0.03","0.05","0.1","0.5",
                "0","0.00001","0.0001","0.0005","0.001","0.003","0.005","0.008","0.01","0.03","0.05","0.1","0.5",
                "0","0.00001","0.0001","0.0005","0.001","0.003","0.005","0.008","0.01","0.03","0.05","0.1","0.5",
                "0","0.00001","0.0001","0.0005","0.001","0.003","0.005","0.008","0.01","0.03","0.05","0.1","0.5",
                "0","0.00001","0.0001","0.0005","0.001","0.003","0.005","0.008","0.01","0.03","0.05","0.1","0.5",
                "0","0.00001","0.0001","0.0005","0.001","0.003","0.005","0.008","0.01","0.03","0.05","0.1","0.5",
                "0","0.00001","0.0001","0.0005","0.001","0.003","0.005","0.008","0.01","0.03","0.05","0.1","0.5"),
              c(nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
                nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117))

data$em<-rep(c("0","0","0","0","0","0","0","0","0","0","0","0","0",
               "0.1","0.1","0.1","0.1","0.1","0.1","0.1","0.1","0.1","0.1","0.1","0.1","0.1",
               "0.3","0.3","0.3","0.3","0.3","0.3","0.3","0.3","0.3","0.3","0.3","0.3","0.3",
               "0.5","0.5","0.5","0.5","0.5","0.5","0.5","0.5","0.5","0.5","0.5","0.5","0.5",
               "0.7","0.7","0.7","0.7","0.7","0.7","0.7","0.7","0.7","0.7","0.7","0.7","0.7",
               "0.9","0.9","0.9","0.9","0.9","0.9","0.9","0.9","0.9","0.9","0.9","0.9","0.9",
               "0.999","0.999","0.999","0.999","0.999","0.999","0.999","0.999","0.999","0.999","0.999","0.999","0.999",
               "0.999999","0.999999","0.999999","0.999999","0.999999","0.999999","0.999999","0.999999","0.999999","0.999999","0.999999","0.999999","0.999999",
               "1","1","1","1","1","1","1","1","1","1","1","1","1"),
             c(nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
               nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
               nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
               nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
               nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
               nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
               nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
               nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,
               nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117,nrow(data)/117))

write.csv(data,"shannon-20_species-m_0_0.05_0.1_0.5_0.7_0.9_0.999_0.999999_1-adjusted-1.csv")



library(ggplot2)
library(tidyverse)
library(hrbrthemes)
library(viridis)
###shannon
par(mar=c(3,5,2,2))
ggplot(data, aes(x=imm, y=shannon, fill=em)) +
  geom_boxplot(position=position_dodge(0.75),width=0.6) +
  scale_fill_viridis(discrete = TRUE, alpha=0.6) +
  theme(panel.grid = element_blank(), panel.background = element_rect(color = 'black', fill = 'transparent'), 
        legend.title=element_blank(),legend.key=element_blank(), plot.title = element_text(hjust = 0.5),axis.text= element_text(size=12,color="black"),
        axis.title.x=element_text(size=14),axis.title.y=element_text(size=14))+
  labs(x = 'Immigration biomass', y = 'Shannon index')
dev.off()
ggsave("./20_species_LVmodel_m_shannon-adjusted-1.pdf", width = 30, height = 12)
dev.new()




