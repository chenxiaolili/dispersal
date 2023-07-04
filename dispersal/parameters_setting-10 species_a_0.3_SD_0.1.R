
library(rstudioapi)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
getwd()  
dir() 

Alldata <-as.data.frame(matrix(nrow=0,ncol=110))
for(i in 1:10000)
{
simulation_a_i=rnorm(90,mean=0.1,sd=0.1)
simulation_r_i=rnorm(10, mean = 1, sd = 0.1)
simulation_n_i=rnorm(10, mean = 2, sd = 0.2)
data_i<-cbind(t(simulation_a_i),t(simulation_r_i),t(simulation_n_i))
Alldata <- rbind(Alldata,data_i)
}


sample<-seq(1,10000,by=1)
Alldata <- cbind(Alldata,sample)
Header <-c('a0102','a0103','a0104','a0105','a0106','a0107','a0108','a0109','a0110',
           'a0201','a0203','a0204','a0205','a0206','a0207','a0208','a0209','a0210',
           'a0301','a0302','a0304','a0305','a0306','a0307','a0308','a0309','a0310',
           'a0401','a0402','a0403','a0405','a0406','a0407','a0408','a0409','a0410',
           'a0501','a0502','a0503','a0504','a0506','a0507','a0508','a0509','a0510',
           'a0601','a0602','a0603','a0604','a0605','a0607','a0608','a0609','a0610',
           'a0701','a0702','a0703','a0704','a0705','a0706','a0708','a0709','a0710',
           'a0801','a0802','a0803','a0804','a0805','a0806','a0807','a0809','a0810',
           'a0901','a0902','a0903','a0904','a0905','a0906','a0907','a0908','a0910',
           'a1001','a1002','a1003','a1004','a1005','a1006','a1007','a1008','a1009',
            'r1','r2','r3','r4','r5','r6','r7','r8','r9','r10',
            'n1','n2','n3','n4','n5','n6','n7','n8','n9','n10','sample'
)
#Rename colnames
names(Alldata) <- Header

Alldata<-as.data.frame(Alldata)
write.csv(Alldata,"10_species_rnorm.csv",row.names = FALSE) 

